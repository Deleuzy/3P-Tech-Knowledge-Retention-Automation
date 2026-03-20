# ATEX Zone Classification — 3P Teknik Standard Reference

## Regulatory Basis
- ATEX Directive 2014/34/EU (equipment)
- ATEX Directive 1999/92/EC (workplace)
- EN 60079-10-1 (explosive gas atmospheres — classification)
- DS/EN 60079-14 (electrical installation design)

## Zone Definitions — Gas/Vapour

| Zone | Description | Frequency |
|------|-------------|-----------|
| Zone 0 | Explosive atmosphere continuously present | > 1000 h/yr |
| Zone 1 | Explosive atmosphere likely in normal operation | 10–1000 h/yr |
| Zone 2 | Explosive atmosphere unlikely, only briefly | < 10 h/yr |

## Equipment Categories

| Zone | Required Category | Marking |
|------|-------------------|---------|
| Zone 0 | Category 1G | Ex ia / Ex ma |
| Zone 1 | Category 1G or 2G | Ex d / Ex e / Ex ia |
| Zone 2 | Category 1G, 2G or 3G | Ex n / Ex ec |

## Minimum Marking Requirements
Equipment must show: `II 2G Ex [type] [gas group] [temp class] [cert body][cert no]`

Example: `II 2G Ex d IIB T4 DNV 12ATEX0001`

## Common Defects to Check
- Zone boundary not drawn on P&ID or area classification drawing
- Equipment category lower than required for zone
- Gas group mismatch (IIA used in IIB/IIC environment)
- Temperature class not verified against process temperature
- No ATEX certificate referenced on equipment data sheet
- Junction boxes without Ex-certified cable glands
