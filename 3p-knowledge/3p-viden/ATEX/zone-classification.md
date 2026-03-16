---
titel: "Zone Classification — Checklist and Methodology"
kategori: "ATEX"
version: "1.0"
oprettet: "2026-03-06"
opdateret: "2026-03-06"
forfatter: "3P Technology"
status: "active"
tags: [atex, zone-classification, checklist, safety]
relevans: "At startup of any ATEX project"
---

# Zone Classification — Checklist and Methodology

## Summary

Zone classification is the foundation of ATEX compliance. This document provides a step-by-step checklist for determining whether an area is Zone 0, 1, 2 (gas) or Zone 20, 21, 22 (dust). Incorrect classification leads to undersized equipment, regulatory violations, and safety risks.

## Background

ATEX zones define the frequency and duration of explosive atmospheres. A Zone 0 area requires continuous presence of explosive gas (rare in practice), while Zone 2 requires only occasional or accidental release. Many 3P projects have started with wrong zone classifications, requiring expensive redesigns. The Unibio project initially misclassified the ammonia storage area as Zone 2 when it should have been Zone 1, costing 8 days of rework.

## Standards & Requirements

- EN 60079-14: Electrical installations in hazardous areas (classification of areas)
- EN 60079-19: Equipment inspection and maintenance
- Danish DS 427 (implements EN 60079 series)
- ATEX Directive 2014/34/EU
- IEC 60079-14:2013

## Best Practices

1. **Always start with P&ID and SDS (Safety Data Sheet)** — Never rely on verbal descriptions
2. **Identify all release sources** — Tanks, valves, connections, vents, drains
3. **Calculate ventilation impact** — Natural vs. forced ventilation changes classification
4. **Document assumptions** — What ventilation rate did you assume? What if it fails?
5. **Classify conservatively** — If unsure between Zone 1 and 2, go with Zone 1
6. **Get customer sign-off** — Have the customer (process engineer) confirm the classification
7. **Review during design** — Don't wait until installation to verify zones

## Known Pitfalls

| Pitfall | Consequence | Cost |
|---------|-------------|------|
| Assuming ventilation that isn't reliable | Equipment undersized, potential explosion | Redesign + 2-4 weeks delay |
| Not checking all release sources | Missed sources reclassify zone later | Equipment swap, 5-10 days |
| Misreading SDS flash point | Wrong substance hazard assessment | Complete redesign, €50K+ |
| Forgetting to account for worst-case scenario | System fails in rare event | Safety risk, liability |
| Not documenting ventilation rate | Can't defend classification to inspector | Non-compliance, project stopped |

## Checklist

### Phase 1: Gather Input Documents
- [ ] P&ID (Process and Instrumentation Diagram) — current version
- [ ] SDS (Safety Data Sheet) — for each substance in the area
- [ ] Equipment layout drawing — shows all potential release sources
- [ ] Ventilation diagram — natural and forced ventilation details
- [ ] Customer approval for zone definition — signed

### Phase 2: Identify Hazards
- [ ] List all substances present (ammonia, hydrocarbons, solvents, etc.)
- [ ] For each substance, note:
  - [ ] Flash point (°C)
  - [ ] Boiling point (°C)
  - [ ] LEL (Lower Explosive Limit) — % by volume
  - [ ] UEL (Upper Explosive Limit) — % by volume
  - [ ] Ignition temperature (°C)
- [ ] Identify all release sources:
  - [ ] Tank vents
  - [ ] Connection points
  - [ ] Valve leakage
  - [ ] Pump seals
  - [ ] Drain systems
  - [ ] Relief valves
  - [ ] Process connections

### Phase 3: Assess Release Frequency
- [ ] Is release continuous? (Zone 0)
- [ ] Is release during normal operation? (Zone 1)
- [ ] Is release only during abnormal/maintenance? (Zone 2)
- [ ] Ventilation rate adequate to dilute release? (natural or forced)
- [ ] Worst-case scenario: what if ventilation fails?

### Phase 4: Determine Zone
- [ ] Mark zones on electrical layout drawing
- [ ] Measure distances for boundaries (typically 1-2 meters from source)
- [ ] Document rationale for each zone decision
- [ ] Get customer sign-off on zone boundaries

## Lessons Learned

### Unibio Ammonia Storage Area (2025)

**Initial Classification:** Zone 2
**Actual Classification:** Zone 1
**Root Cause:** Initial assessment assumed forced ventilation would always be operational. Designer didn't account for ventilation system failure mode.

**What Happened:** After design review, customer's process engineer noted that ammonia storage has no redundant ventilation. Single exhaust fan failure = continuous ammonia release. This makes it Zone 1, not Zone 2.

**Cost:** 
- Equipment swap: 3 days engineering + €15K equipment cost
- Schedule delay: 8 days (had to re-order Zone 1 rated devices)
- Total loss: ~€40K + 8 days

**Action for Next Time:**
- Always ask: "What happens if ventilation fails?"
- Request ventilation system redundancy documentation
- Never assume forced ventilation without confirmation of backup systems
- Escalate ventilation questions to customer's process engineer early

## References

- EN 60079-14:2013 — Full standard for electrical classification of hazardous areas
- ATEX Notified Body Database — Equipment certification lookup: https://nando.ec.europa.eu/
- 3P Internal Standard — Zone Classification Template (see _templates/)
- Unibio Project File — Complete case study with drawings and lessons learned
