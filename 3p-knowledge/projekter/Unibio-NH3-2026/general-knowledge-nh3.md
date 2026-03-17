---
titel: NH3 Installation & Commissioning Preparation for Unibio
kategori: NH3
version: 1
oprettet: 2026-03-17
opdateret: 2026-03-17
forfatter: AI-ekstraktion
status: aktiv
tags: [nh3]
---

## Resumé
Detne dokument er en forberedelsesrapport for den obligatoriske førkommisionering kontroll og præinspektion af det 80 NH3 ammiasystem på Kalundborg for Unibio. Dokumentet fastlægger de nødvendige indsigter og handlinger, der skal udføres inden forløbet og førkommissioneringgodkendelsen kan blive givet.

## Baggrund
Project: Unibio-NH3-2026
Customer: Unibio A/S
Location: Asnæsvej 2A, 4400 Kalundborg
Category: NH3 / ATEX
Date: 13 March 2026

## Standarder og Krav
- DS/EN 60079-14:2024
- DS/EN 62305-3
- ATEX direktiver (EU ATEX directives)
- Art. 13 (equipment marking)
- DS/EN 60204-1 (requirements for electrical equipment of machines)
- DS/EN 60079-17 (periodic inspection and testing of electrical equipment in hazardous areas)

## Best Practices
1. **EX-certified cable glands:**
   - Glands must be correctly torqued to IP rating.
   - Replace all non-compliant glands before commissioning.
2. **Junction box remediation:**
   - Junction boxes in Zone 1 must be EX d or EX e rated and fully closed.
   - Tighten loose cover on 80HLS002 to IP66 rating.
3. **Lightning protection:**
   - Upgrade bonding conductor to 50mm².
   - Full LP survey required.
4. **Periodic inspection:**
   - Set up a periodic inspection schedule per DS/EN 60079-17.
5. **Equipment certificate verification:**
   - Verify all EX equipment certificates before commissioning.

## Kendte Problemer og Afvigelser
- **Kritiske forskebsser:**
  - Damaged EX d cable glands on NH3 instruments in Zone 1.
  - Junction box cover loose on 80HLS002.
  - Lightning protection bonding insufficient — 6mm² vs required ≥50mm².
- **Høj priority afvigelser:**
  - Missing PE conductor on NH3 panel earth bar.
  - Equipment marking not verified against zone classification on P&ID.
- **Medium priority afvigelser:**
  - Commission full lightning protection survey (DS/EN 62305-3).
  - Set up periodic inspection schedule per DS/EN 60079-17.

## Tjekliste
Tjeklisten følger herunder for det nødvendige arbejde at udføres:
1. **Årsag 1** (§9.3): Erstat alle skadede eksfors certificerede forbindelser på alle NH3 instrumenter i Zone 1, før forløbet.
2. **Årsag 2** (§10.4): Tæt på eksfors certificeret forbindelses cover på 80HLS002 før forløbet.
3. **Årsag 3** (§5.3): Opgrader lynbeskyttelse bonding conductor til 50mm². 
4. **Årsag 4** (§8.2.2): Anbringe PE-afledning på NH3 konturarmer bar.
5. **Årsag 5** (Art. 13): Verificere alle æquipment markerings inden forløbet.
6. **Årsag 6** (§6.3.3): Verificere alle instrumentkabler i Zone 1: skjoldede, 0.75mm² minimale.

## Lessons Learned
- Fordele af udarbejdelse af en detaljeret forberedelsesrapport før forløbet.
- Mulighed for at opfylde alle krav med henvisning til relevant specifikation.

## Referencer
- Instrumenter med ét tag:
  - 80PT004 Pressure Transmitter
  - 80HLS002 High Level Switch
  - 80LT001 Level Transmitter
- Solenoide udgange, eksfors:
  - Q2180, GV2ME14
- ATEX-cat og Zone:
  - DS/EN 60079-14 §8.2.2
  - ATEX 2014/34/EU Art. 13