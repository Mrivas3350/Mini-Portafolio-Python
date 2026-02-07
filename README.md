# Mini Portafolio Python – Supply Chain & Operaciones (por Jorge Maximiliano Rivas)

Este mini portafolio demuestra cómo aplico **Python** a problemas típicos de **Supply Chain / Operaciones**:
- Automatización de reportes (CSV/Excel)
- KPIs (OTIF, fill rate, lead time)
- Inventarios (ABC, stock de seguridad, punto de pedido)
- Análisis exploratorio y generación de salidas listas para compartir

> **Requisitos:** Python 3.10+  
> Instalar dependencias: `pip install -r requirements.txt`

## Estructura
- `01_kpis_otif/` → cálculo de OTIF y tablero simple en CSV
- `02_inventory_abc_rop/` → clasificación ABC + punto de pedido (ROP) y stock de seguridad
- `03_report_automation/` → script para consolidar archivos y generar reporte final

Cada carpeta incluye:
- `README.md` (explica el objetivo)
- `data/` (dataset de ejemplo)
- `src/` (código listo para correr)
- `outputs/` (archivos generados)

## Cómo correr rápido
1) KPI OTIF
```bash
python 01_kpis_otif/src/run_otif.py
```

2) Inventarios ABC + ROP
```bash
python 02_inventory_abc_rop/src/run_inventory.py
```

3) Automatización de reporte
```bash
python 03_report_automation/src/run_report.py
```

## Notas
- Los datos son **ficticios** (demo).
- El objetivo es mostrar **criterio de negocio** + **capacidad técnica**.
