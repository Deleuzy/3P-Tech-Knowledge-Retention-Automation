---
titel: Unibio NH3-projekt specifikation
kategori: NH3 / ATEX
version: 1
oprettet: 2026-03-17
opdateret: 2026-03-17
forfatter: AI-ekstraktion
status: aktiv
tags: [Unibio, NH3, ATEX]
---

## Resumé
Dokumentet omhandler forberedelse til obligatorisk initial indsigt og præindspektion af 80 NH3-ammoniaksystem på Unibios lokation i Kalundborg. Deviationer identificeret under indsigtene har ført til nødvendighed for remediation før godkendelse kan gives.

## Baggrund
- Projekt: Unibio-NH3-2026
- Kunden: Unibio A/S
- Sted: Kalundborg, Asnæsvej 2A 
- Engineer: 3P Teknik A/S
- Dato: 13. marts 2026

## Standarder og Krav
- DS/EN 60079-14:2024
- DS/EN 60204-1
- DS/EN 62305-3
- ATEX direktiver (2014/34/EU)

## Best Practices
- Enhver EX-equipment skal være udstyret med gyldigt certificate (IECEx eller ATEX)
- Jordforbindelse for lightning protection skal være i mindst 50mm²
- Alle instrumentkabeler i Zone 1 skal være beskyttet mod skadelige udgasser
- Junction boxes i Zone 1 skal være EX certificerede og lukket

## Kendte Problemer og Afvigelser
- Jordforbindelse for lightning protection mangler (6mm² vs 50mm²)
- Skadet EX d kabelstikning på NH3-instrumenter
- Fattelig eks-gecer forfatter på eks-instrumenter
- Missing PE-forledning på NH3-panelet

## Tjekliste
- Alle EX-equipment skal have gyldigt certificate:
  - 80PT004, 80HLS002 require Certificate veriification
- Alle EX instrumenter skal have nye, EX certificerede kabelstikninger:
  - 80PT004, 80HLS002, 80LT001 (Q2180, Q2190 ikke EX-equipment)
- Alle junction boxes i Zone 1 skal være lukket:
  - 80HLS002: Junction box cover loose
- Jordforbindelse for lightning protection skal opgraderes:
  - 50mm² vs 6mm²
- PE-forledning på NH3-panel skal installeres:
  - I mindst 50mm²
- Alle eks-instrumenter skal have eks-mærkning:
  - I overensstemmelse med zone kategori fra P&ID

## Lessons Learned
- Tæt observation af eks-equipment og -installationer under indsigt og præindspektion
- Opgradering af jordforbindelse for lightning protection
- Opdatering af eks-certifikater og -mærkninger
- Installering af PE-forledninger på NH3-panelet

## Referencer
- Eks-equipment med TAG-numre:
  - 80PT004, 80HLS002, 80LT001, 80AV001, 80YV002, Q2180, Q2190
- Kabel-specifikationer:
  - Min. 0,75mm², beskyttelse mod skadelige udgasser
- Terminal-referencer:
  - +NH3-X2082:1
- Zone klassifikation:
  - Zone 0/1/2
- Eks-ratings:
  - EX II 2G IIA, EX II 2G IIC, EX d, EX e