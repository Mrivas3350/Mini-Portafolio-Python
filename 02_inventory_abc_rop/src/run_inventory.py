"""
run_inventory.py
ABC + Stock de seguridad + Punto de pedido (ROP)
Entrada: data/demand_last_60_days.csv
Salida: outputs/abc_rop.csv
"""
from __future__ import annotations
import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data" / "demand_last_60_days.csv"
OUT = BASE / "outputs" / "abc_rop.csv"

SERVICE_LEVEL_Z = {0.90: 1.28, 0.95: 1.65, 0.97: 1.88, 0.98: 2.05, 0.99: 2.33}

def classify_abc(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["annual_value"] = df["annual_demand"] * df["unit_cost"]
    df = df.sort_values("annual_value", ascending=False)
    df["cum_share"] = (df["annual_value"].cumsum() / df["annual_value"].sum()).round(4)

    def abc_bucket(x: float) -> str:
        if x <= 0.80:
            return "A"
        if x <= 0.95:
            return "B"
        return "C"

    df["abc"] = df["cum_share"].apply(abc_bucket)
    return df

def main(service_level: float = 0.95) -> None:
    z = SERVICE_LEVEL_Z.get(service_level, 1.65)
    raw = pd.read_csv(DATA)
    demand_cols = [c for c in raw.columns if c.startswith("d_")]

    raw["avg_daily_demand"] = raw[demand_cols].mean(axis=1)
    raw["std_daily_demand"] = raw[demand_cols].std(axis=1).fillna(0)
    raw["annual_demand"] = (raw["avg_daily_demand"] * 365).round(0)

    raw["safety_stock"] = (z * raw["std_daily_demand"] * (raw["lead_time_days"] ** 0.5)).round(0)
    raw["demand_during_lt"] = (raw["avg_daily_demand"] * raw["lead_time_days"]).round(0)
    raw["reorder_point_rop"] = (raw["demand_during_lt"] + raw["safety_stock"]).round(0)

    out = classify_abc(raw)[[
        "sku","abc","unit_cost","lead_time_days",
        "avg_daily_demand","std_daily_demand",
        "annual_demand","annual_value",
        "safety_stock","reorder_point_rop"
    ]].sort_values(["abc","annual_value"], ascending=[True,False])

    OUT.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(OUT, index=False)
    print(f"OK → Generado: {OUT}")

if __name__ == "__main__":
    main()
