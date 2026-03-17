---

titel: ds en 60079 standard
kategori: ATEX
version: 1
oprettet: 2026-03-17
opdateret: 2026-03-17
forfatter: AI-ekstraktion
status: aktiv
tags: [atex]

## Resumé
Dette dokument beskriver en præinspektion for Unibio NH3 — 80 anlæg, hvor 7 afgørende for at løse før commissioning godkendelse. Hovedsbasis for dette dokument er DS/EN 60079-14:2024 og DS/EN 62305-3. Dokumentet indeholder også en omfattende liste med åbne handlinger med prioriteringer og tidslinjer.

## Baggrund
Unibio A/S har anmodet om præinspektion og commissioning foranlægget Unibio NH3 — 80NH3 anlæg, der er blevet udført af TNG Engineering ApS (16. februar 2026). Præinspektionen har identificeret 7 afgørende afviklingsproblemer.

**Kunde**: Unibio A/S  
**Sted**: Asnæsvej 2A, 4400 Kalundborg  
**Date**: 13. marts 2026  

## Standarder og Krav
Følgende standarder er relevante for dette projekt:

- **DS/EN 60079-14:2024**: ATEX installation og commissioning
- **DS/EN 62305-3**: Nævningerbeskyttelse system og inspection

## Best Practices
- Alle EX enheder måtte have gyldige certificater ved levering og installation.  
- Kabel glands for EX instrumenter i Zone 1 måtte være korrekt torqued og certificerede.  

## Kendte Problemer og Afvigelser
Følgende afviklingsproblemer er identificeret:

- De udledte resultater viser det følgende:
  - DS/EN 60079-14 §6.1: Enheder manglede certifikater.
  - DS/EN 60079-14 §9.3: EX d kabel glands på NH3 instrumenter var beskadiget, og de ikke var torquet korrekt.
  - DS/EN 60079-14 §10.4: En jolleboks i Zone 1 havde en løs lokk.
  - DS/EN 60079-14 §5.3: En mindre PE ledning på NH3 skadepanelen havde ingen PE ledning.
  - DS/EN 62305-3 §2.1: Nævningerbeskyttelssystem og inspection var mangelfuldt og ikke godkendt af en godkendt LP Surveyør.
  - Zone klassificering på P&ID havde ikke gyldigt ATEX certificat.

## Tjekliste
Følgende handlinger måtte udføres før commissioning:

1. Erstat alle defekte EX Cable Glands, med nye EX d-godskepledte kabel glands på alle NH3 instrumenter i Zone 1. (Prioriteret)
2. Afvigt jolleboks dekka på 80HLS002 før commissioning. (Prioriteret)
3. Afvigt mindre PE ledning på NH3 skadepanelen og installer en ny 50mm2 PE ledning af bedste kvalitet (Prioriteret)
4. Udfør en fuld nævningerbeskyttelse system og inspection i henhold til DS/EN 62305-3. (Prioriteret)
5. Udfør en periodic inspection plan i henhold til DS/EN 60079-17. (Mellemsvær)

## Lessons Learned
I fremtidige projekt, bør holdere fastn på følgende:

1. Alle ledende personer skal være opmærksom på ATEX og DS/EN standarder.
2. Godkendte certifikater skal være på plads før installationen.
3. Alle afviklingsforhold skal være testet, før installation.
4. Alle ledende løsninger skal være under overvågning og revision før commissioning.

## Referencer
- **Tag** number: 80PT004, 80HLS002, 80LT001, 80AV001, 80YV002  
- **Kabel specifikation**: 0.75mm2 (Shielded)  
- **Terminal referencers**: +NH3-X2082:1  
- **Zone klassificering**: Zone 1 (EX II 2G IIA)  
- **DS/EN standarder**: DS/EN 60079-14 §6.1, DS/EN 60079-14 §10.4, DS/EN 60079-14 §12.2, DS/EN 62305-3 §5.3  DS/EN 60079-14 §9.3  
- **EQipment modeller og ratings**:  AVIEX FIP-IV-T (Pressure transmitter), EX II 2G IIA, Zone 1  (T4 GB); EX II 2G IIA, Zone 1  (T3 GB); EX II 2G IIA, Zone 2  (T4 GB); EX II 2G IIA, Zone 1  (T4 GB).  
- **Required actions with priority**: Før Commissioning: 
  - Erstat alle defekte EX Cable Glands, med nye EX d-godskepledte kabel glands på alle NH3 instrumenter i Zone 1. (Prioriteret)
  - Afvigt jolleboks dekka på 80HLS002 før commissioning. (Prioriteret)
  - Afvigt mindre PE ledning på NH3 skadepanelen og installer en ny 50mm2 PE ledning af bedste kvalitet (Prioriteret)
  - Udfør en fuld nævningerbeskyttelse system og inspection i henhold til DS/EN 62305-3. (Prioriteret)
- **EQipment model numbers and ratings**:  Schneider GV2ME14 (Motor breaker), 6-10 Amp (Safe area)
- **Supplier names and document numbers**: 3P Teknik A/S (DS/EN standarder, kabel glands, EX d godskepledte kable glands.),  TNG Engineering ApS (præinspektion på Unibio NH3 80 anlæg.)