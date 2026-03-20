---
titel: "Præinspektion 80 NH3-anlæg Unibio Kalundborg - ATEX Findings"
kategori: NH3
version: "1.0"
oprettet: 2026-03-12
opdateret: 2026-03-12
forfatter: "3P Technology (Auto-extracted)"
status: "active"
tags: ["nh3", "atex", "præinspektion", "indledende-inspektion", "unibio", "ex-materiel", "60079-14"]
source_file: "Inspektionsrapport_Præinspektion_80_NH3_Anlæg_Projekt_nr_3230100_Unibio_KA_TNG_2026-02-19.pdf"
source_type: "inspection_report"
---

# Præinspektion 80 NH3-anlæg Unibio Kalundborg — ATEX Findings

## Summary

TNG Engineering ApS udførte præinspektion (indledende inspektion og ibrugtagningskontrol) af 80 NH3-anlæg hos Unibio A/S, Kalundborg, den 16. februar 2026 (Projekt nr. 3230100). Anlægget var ikke 100% færdigmonteret på inspektionstidspunktet. Inspektionen identificerede en række afvigelser fra ATEX-kravene (DS/EN 60079-14), inkl. beskadigede kabelforskruninger, manglende opmærkning, og fejl i potentialudligning. Der kræves opfølgende inspektion når udeståender er afhjulpet.

## Background

- **Kunde:** Unibio A/S, Asnæsvej 2A, 4400 Kalundborg
- **Kontaktperson:** Mathias Jørgensen
- **Inspektør:** Tomm Giiff, TNG Engineering ApS
- **Inspektionsdato:** 16. februar 2026
- **Projekt nr.:** 3230100
- **Anlæg:** 80 NH3-anlæg — ammoniaktank og fordamper placeret i det fri, omgivet af betonbassin
- **CE-mærkning:** Unibio A/S (maskinanlæg jf. Maskindirektiv 2006/42/EU)
- **Status ved inspektion:** Ikke 100% færdigmonteret — installationsarbejde i gang
- **P&ID:** Diagram 80PID20240702
- **Zoneklassificering:** Udarbejdet af Niras

## Standards & Requirements

- **DS/EN 60079-14** — Elektriske installationer i eksplosionsfarlige områder (primær standard)
- **DS/EN 60079-1** — Eksplosionsbeskyttelsestype Ex d (tryksikker kapsling)
- **DS/EN 60079-17** — Inspektion og vedligeholdelse, udgave 2017
- **DS/EN 60204-1, kapitel 18** — Verificering af elektrisk materiel
- **DS/EN 62305-3, kapitel 6.2.2** — Lynbeskyttelse, beskyttelsesforbindelser
- **ATEX-direktiv 2014/34/EU** — Materielkrav for eksplosionsfarlige områder
- **Maskindirektiv 2006/42/EU** — CE-mærkning
- **AT bekendtgørelse nr. 428 (2022)** — Anvendelse af tekniske hjælpemidler
- **AT bekendtgørelse nr. 478, bilag 1 afsnit 1.8** — ATEX-direktiv 1999/92/EF

## Best Practices

- Zoneklassificering skal foreligge fra kompetent ingeniørfirma (her: Niras) inden inspektion
- Alle eksplosionsbeskyttede komponenter skal have korrekt beskyttelseskategori for zonen:
  - Zone 2 (Gas gruppe IIA, Temp. klasse T1): **EX II 3G IIA T1 Gc**
  - Zone 1: **EX II 2G IIA T1 Gb**
  - Zone 0: **EX II 1G IIA1 Ga**
- Kabelforskruninger i EX d materiel skal monteres med korrekt tilspændingsværktøj — aldrig med grber/gripetang
- Alle disponible (ubenyttede) ledere i kabler til EX materiel skal monteres til nagelfast terminal eller isoleres med krympeflex
- Beskyttelsesleder (G/G-kabel) er obligatorisk til alt EX instrumenteringsudstyr
- Fundament jordring og lynbeskyttelse skal dokumenteres i el-teknisk dokumentation
- Potentialudligning imellem metallisk rørbro og betonfundament: **≥ 16 mm²** (som nedleder: **50 mm²**)
- Alle TAG-numre på mekanisk og elektrisk materiel skal være etableret inden indledende inspektion

## Known Pitfalls

| Pitfall | Observation | Standard Reference | Afhjælpning |
|---------|-------------|-------------------|-------------|
| Beskadigede EX d kabelforskruninger | Ukorrekt tilspændingsværktøj brugt ved montering → grater, metallisk beskadigelse | DS/EN 60079-1, DS/EN 60079-14 | Gennemgå og udskift alle beskadigede. Brug korrekt værktøj + følg leverandørens manual |
| Løstliggende samlemuffer i EX instrumentering | TAG 80HLS002: disponible ledere monteret i løse samlemuffer | DS/EN 60079-14 | Demonter samlemuffer. Tilslut disponible ledere til nagelfast terminal eller isoler med krympeflex |
| Manglende beskyttelsesleder til EX instrument | TAG 80HLS002: ingen PE-leder fremført til instrumentet | Udstyrets installationsvejledning | Udskift kabel til type med beskyttelsesleder (G/G) |
| Ubeskyttede disponible ledere | Ledere tilhørende display i 80HLS002 ikke sikret mod berøring af spændingsføring | DS/EN 60079-14 | Monter krympeflex på disponible ledere |
| Utilstrækkelig lynbeskyttelse/jordforbindelse | 6 mm² beskyttelsesleder opgivet som lynbeskyttelse for rørbro — understøtter ikke kravet | DS/EN 62305-3 kap. 6.2.2 | Opgrader til ≥16 mm² (≥50 mm² hvis nedleder) |
| Manglende el-teknisk dokumentation | Lynbeskyttelsessystem og potentialudligning ikke dokumenteret | — | Opdater dokumentation med faktiske installationsforhold |
| Ufærdig installation ved inspektion | Kabelopmærkning, TAG-numre, potentialudligning, afspærringsventiler, Resopal-skilte mangler | DS/EN 60079-14 | Færdiggør alle punkter inden indledende inspektion |

## Checklist

- [ ] Verificer at alle EX d kabelforskruninger er ubeskadigede — udskift om nødvendigt
- [ ] Kontrollér at korrekt tilspændingsværktøj anvendes ved montering af EX d kabelforskruninger
- [ ] Tjek at alle disponible ledere i EX instrumenter er tilsluttet terminal eller isoleret med krympeflex (ikke i løse samlemuffer)
- [ ] Bekræft at beskyttelsesleder (G/G kabel) er fremført til ALLE EX instrumenter
- [ ] Mål og dokumentér potentialudligningsforbindelsen rørbro↔betonfundament (krav: ≥16 mm² / ≥50 mm²)
- [ ] Verificer zoneklassificering (P&ID 80PID20240702) svarer til installeret materielkategori
- [ ] Tjek at al EX materiel har korrekt kategori: Zone 2 = EX II 3G IIA T1 Gc minimum
- [ ] Gennemgå ALLE sammenlignelige instrumenter på anlæg for samlemuffer i EX materiel
- [ ] Sørg for at samtlige TAG-numre er påsat inden indledende inspektion
- [ ] Kompletér kabelopmærkning, fleksible slangers opmærkning, og Resopal-skilte
- [ ] Dokumentér lynbeskyttelsessystem i el-teknisk dokumentation
- [ ] Verificer installation jf. DS/EN 60204-1, kapitel 18
- [ ] Indhent fotograferingstilladelse fra kunde inden inspektion

## Lessons Learned

**Projekt:** Unibio 80 NH3-anlæg, Projekt 3230100, Kalundborg

- **Root Cause:** Installationen var ikke afsluttet på inspektionstidspunktet. Derudover var ukorrekt monteringsværktøj anvendt til EX d kabelforskruninger, og installationsmanualerne for EX instrumenter var ikke fulgt konsekvent for lederhåndtering.
- **What Happened:** Præinspektion afslørte 7+ afvigelsespunkter inkl. beskadigede kabelforskruninger i tryksikker kapsling, samlemuffer i EX instrumenter, manglende PE-ledere, og utilstrækkelig dokumentation af lynbeskyttelse. Anlægget var ikke godkendt til idriftsættelse.
- **Cost/Impact:** Anlægget er ikke 100% færdigmonteret — kræver opfølgende indledende inspektion når samtlige afvigelser er afhjulpet. Forsinkelse i ibrugtagning.
- **Key Findings:** 7+ afvigelsespunkter på 49-siders rapport. Ingen alvorlige fund der ikke kan afhjælpes.

## References

- Inspektionsrapport: "Præinspektion 80 NH3-anlæg" — TNG Engineering ApS, 16. februar 2026
- Handlingsplan: "Handlingsplan_Inspektionsrap_Præinspek_80_NH3_Anlæg_Projekt_3230100"
- P&ID: 80PID20240702
- Zoneklassificering: Niras
- Projekt nr.: 3230100
- Kunde: Unibio A/S, Asnæsvej 2A, 4400 Kalundborg

---
*Auto-extracted from: Inspektionsrapport_Præinspektion_80_NH3_Anlæg_Projekt_nr_3230100_Unibio_KA_TNG_2026-02-19.pdf — 2026-03-12*
