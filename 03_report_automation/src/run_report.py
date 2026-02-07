"""
run_report.py
Consolida snapshots diarios y genera un reporte semanal en Excel.
Entrada: data/stock_snapshots/*.csv
Salida: outputs/weekly_stock_report.xlsx
"""
from __future__ import annotations
import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
IN_DIR = BASE / "data" / "stock_snapshots"
OUT = BASE / "outputs" / "weekly_stock_report.xlsx"

def main() -> None:
    files = sorted(IN_DIR.glob("stock_*.csv"))
    if not files:
        raise SystemExit(f"No se encontraron archivos en {IN_DIR}")

    frames = [pd.read_csv(f) for f in files]
    all_data = pd.concat(frames, ignore_index=True)
    all_data["date"] = pd.to_datetime(all_data["date"], errors="coerce")

    summary = (
        all_data.groupby("sku", as_index=False)
        .agg(
            avg_stock=("stock_on_hand", "mean"),
            min_stock=("stock_on_hand", "min"),
            max_stock=("stock_on_hand", "max"),
            avg_open_po=("open_po_qty", "mean"),
        )
    )
    summary["avg_stock"] = summary["avg_stock"].round(0).astype(int)
    summary["avg_open_po"] = summary["avg_open_po"].round(0).astype(int)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(OUT, engine="openpyxl") as writer:
        summary.to_excel(writer, sheet_name="Resumen", index=False)
        all_data.sort_values(["sku","date"]).to_excel(writer, sheet_name="Consolidado", index=False)

    print(f"OK → Generado: {OUT}")

if __name__ == "__main__":
    main()
