Here is the extracted information in a structured Markdown file:

---
titel: Template ATEX Check
kategori: ATEX
version: 1
oprettet: 2026-03-17
opdateret: 2026-03-17
forfatter: AI-ekstraktion
status: aktiv
tags: [atex]
---

## Resumé
This document outlines the preparation for the mandatory initial inspection and pre-commissioning control of the 80 NH3 ammonia system at Kalundborg. Key findings indicate several deviations requiring remediation before commissioning approval.

## Baggrund
Project: Unibio NH3 - 80 NH3 Anlæg
Customer: Unibio A/S
Location: Asnæsvej 2A, 4400 Kalundborg
Date: 2026-03-17

## Standarder og Krav
* DS/EN 60079-14:2024
* DS/EN 62305-3
* ATEX directives (2014/34/EU)

## Best Practices
* All EX equipment must carry valid certificate (IECEx or ATEX)
* Cable glands must be EX-certified and correctly torqued to IP rating
* Junction boxes in Zone 1 must be EX d or EX e rated and fully closed
* PE conductor cross-section ≥50mm² for lightning protection bonding
* All instrument cables in Zone 1: shielded, min 0.75mm²
* Periodic inspection schedule established and documented
* Equipment category matches zone classification on P&ID

## Kendte Problemer og Afvigelser
* Damaged EX d cable glands on NH3 instruments
* Loose junction box cover on 80HLS002 in Zone 1
* Missing PE conductor on NH3 panel earth bar
* Lightning protection bonding insufficient (6mm² vs required ≥50mm²)
* Equipment marking not verified against zone classification on P&ID

## Tjekliste
* Verify certificates for EX equipment (80PT004, 80HLS002)
* Replace damaged EX d cable glands on all NH3 instruments
* Tighten and re-certify junction box cover on 80HLS002
* Upgrade lightning protection bonding conductor 6mm² → 50mm²
* Install missing PE conductor on NH3 panel
* Obtain and file EX certificates for 80PT004 and 80HLS002
* Commission full lightning protection survey (DS/EN 62305-3)
* Set up periodic inspection schedule per DS/EN 60079-17

## Lessons Learned
* Ensure proper installation and certification of EX equipment and cable glands
* Verify lightning protection bonding meets required specifications
* Cross-check equipment categories against zone classification on P&ID

## Referencer
* Equipment TAGs:
  * 80PT004: Pressure Transmitter
  * 80HLS002: High Level Switch
  * 80LT001: Level Transmitter
  * 80AV001: Actuated Valve
  * 80YV002: Solenoid Valve
  * Q2180: Motor Breaker
  * Q2190: Motor Breaker
* Cable specifications:
  * Shielded, min 0.75mm²
* Terminal references:
  * +NH3-X2082:1
* Zone classifications:
  * Zone 0, Zone 1, Zone 2
* Required actions with priority:
  * Critical: Replace damaged EX d cable glands, tighten and re-certify junction box cover, upgrade lightning protection bonding
  * High: Install missing PE conductor, obtain and file EX certificates
  * Medium: Commission full lightning protection survey, set up periodic inspection schedule