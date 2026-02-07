# Python Portfolio – Supply Chain & Operations

This repository shows how I apply **Python** to real-world problems in **Supply Chain / Operations**.

The focus is not only technical, but also **business-oriented**:
KPIs, inventory decisions and report automation to support management.

## Use cases covered
- 📊 **OTIF KPI (On Time In Full)** by customer and period
- 📦 **Inventory management**: ABC classification, safety stock and reorder point (ROP)
- ⚙️ **Report automation**: consolidation of daily files into a weekly Excel report

All data used is **dummy/demo**, created only to showcase methodology and logic.

---

## Projects

### 1️⃣ OTIF – On Time In Full KPI
- Calculates **On Time**, **In Full** and **OTIF %**
- Aggregated by customer and month
- Typical KPI used in industrial and FMCG environments

📄 Output:  
`01_kpis_otif/outputs/otif_summary.csv`

![OTIF KPI](assets/01_otif_real_png)

---

### 2️⃣ Inventory – ABC + Safety Stock + Reorder Point
- ABC classification based on annual consumption value
- Safety stock calculation using demand variability
- Reorder Point (ROP) based on lead time demand

📄 Output:  
`02_inventory_abc_rop/outputs/abc_rop.csv`

![ABC ROP](assets/02_abc_rop_real.png)

---

### 3️⃣ Report Automation – Weekly Stock Report
- Consolidates daily stock snapshots
- Generates a weekly Excel report ready for sharing
- Reduces manual work and reporting time

📄 Output:  
`03_report_automation/outputs/weekly_stock_report.xlsx`

![Weekly Stock](assets/03_weekly_stock_real.png)

---

## How to run locally

```bash
pip install -r requirements.txt
python 01_kpis_otif/src/run_otif.py
python 02_inventory_abc_rop/src/run_inventory.py
python 03_report_automation/src/run_report.py
