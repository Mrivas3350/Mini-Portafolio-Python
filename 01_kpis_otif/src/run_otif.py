"""
run_otif.py
Calcula OTIF (On Time In Full) por cliente y por mes.
Entrada: data/orders.csv
Salida: outputs/otif_summary.csv
"""
from __future__ import annotations
import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data" / "orders.csv"
OUT = BASE / "outputs" / "otif_summary.csv"

def compute_otif(df: pd.DataFrame) -> pd.DataFrame:
    for c in ["order_date", "promise_date", "delivery_date"]:
        df[c] = pd.to_datetime(df[c], errors="coerce")

    df["on_time"] = df["delivery_date"] <= df["promise_date"]
    df["in_full"] = df["qty_delivered"] >= df["qty_ordered"]
    df["otif"] = df["on_time"] & df["in_full"]
    df["month"] = df["order_date"].dt.to_period("M").astype(str)

    summary = (
        df.groupby(["month", "customer"], as_index=False)
        .agg(
            orders=("order_id", "nunique"),
            on_time_rate=("on_time", "mean"),
            in_full_rate=("in_full", "mean"),
            otif_rate=("otif", "mean"),
            qty_ordered=("qty_ordered", "sum"),
            qty_delivered=("qty_delivered", "sum"),
        )
    )
    for c in ["on_time_rate", "in_full_rate", "otif_rate"]:
        summary[c] = (summary[c] * 100).round(1)

    return summary.sort_values(["month", "customer"])

def main() -> None:
    df = pd.read_csv(DATA)
    summary = compute_otif(df)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(OUT, index=False)
    print(f"OK → Generado: {OUT}")

if __name__ == "__main__":
    main()
