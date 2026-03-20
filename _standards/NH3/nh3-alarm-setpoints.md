# NH3 Alarm Setpoints — 3P Teknik Standard Reference

## Regulatory Basis
- EN 378 (Refrigeration systems and heat pumps)
- DS/EN 14816 (Fixed firefighting systems — NH3 suppression)
- Arbejdstilsynet AT-vejledning C.0.1 (Ammonia — Danish WHS)

## Standard Alarm Thresholds

| Level | Threshold | Action |
|-------|-----------|--------|
| Warning (Alarm 1) | 25–50 ppm | Flash alarm, ventilation on |
| Evacuation (Alarm 2) | 150–300 ppm | Horn + flash, evacuation |
| Shutdown | 300 ppm | Full system shutdown |
| IDLH (immediate danger) | 300 ppm | Emergency response |
| ERPG-2 | 150 ppm | Protective actions for public |

## Cable & Sensor Requirements
- Sensor type: Electrochemical or IR (ATEX certified if Zone 1/2)
- Cable: Min 0.75 mm² multicore, screened
- Sensor supply: 18–36 VDC (e.g. GP-NOVA-M geopal)
- 4–20 mA loop: AI input, IW-series terminal recommended
- Fault relay: Must be monitored (NC contact, fail-safe)

## Relay Output Mapping (typical)
- Relay 1 → Alarm 1 (30–50 ppm) — Flash
- Relay 2 → Alarm 2 (150–300 ppm) — Horn + Flash
- Relay 3 → Fault (open circuit / power loss)

## Common Defects to Check
- Alarm 2 threshold above 300 ppm — non-compliant
- Fault relay wired NO instead of NC — not fail-safe
- No drain in junction box — condensation risk
- Sensor not ATEX certified in classified zone
- Missing RCD protection on sensor supply circuit
