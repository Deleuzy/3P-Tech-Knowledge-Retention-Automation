# EPLAN Diagram Conventions — 3P Teknik Standard Reference

## Regulatory Basis
- IEC 81346 (reference designation system)
- IEC 60617 (graphical symbols for diagrams)
- EN 60204-1 (safety of machinery — electrical equipment)

## 3P Teknik Naming Conventions
- Terminal blocks: X + number (e.g. X1, X2252)
- Analogue inputs: AI + number (e.g. AI1, AI3)
- Digital inputs: DI + number (e.g. DI3, DI4, DI5)
- Contactors/relays: K + number (e.g. K1221, K1242)
- UV references: UV + number (e.g. UV1, UV3, UV4, UV5)
- Wiring: -W_ prefix + component ID (e.g. -W_80GGS002)
- Cable cross-reference: Component/page notation (e.g. /16.2, /16.3)

## Cable Sizing Minimums
| Circuit type | Min cross-section |
|---|---|
| Control signals (24V DC) | 0.75 mm² |
| Analogue loops (4–20 mA) | 0.75 mm² screened |
| Power circuits (230V) | 1.5 mm² |
| Motor circuits | Per IEC 60204-1 |

## Diagram Check Requirements
- Every terminal must have a unique number
- Cross-references must be correct (page/row notation)
- Cable designation must match wire list
- Signal type labelled on each connection (AI, DI, DO, AO)
- Supply voltage shown on each page (24V, 230V etc.)
- Earth/screen connections shown and labelled

## Common Defects to Check
- Duplicate terminal numbers
- Cross-reference points to wrong page
- Missing cable screen connection to earth
- Signal type not labelled
- Wire cross-section not noted on cable designation
- Inconsistent reference designation across pages
