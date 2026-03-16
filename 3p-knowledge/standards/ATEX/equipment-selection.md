---
titel: "Equipment Selection & Specification — ATEX Rated Devices"
kategori: "ATEX"
version: "1.0"
oprettet: "2026-03-06"
opdateret: "2026-03-06"
forfatter: "3P Technology"
status: "active"
tags: [atex, equipment, specification, certification]
relevans: "During design phase for any ATEX project"
---

# Equipment Selection & Specification — ATEX Rated Devices

## Summary

Selecting ATEX-rated equipment requires understanding Equipment Protection Levels (EPL), equipment groups, and Ex markings. Wrong equipment in the wrong zone creates safety risks and regulatory violations. This document covers how to read Ex markings, match equipment to zones, and verify IECEX certification.

## Background

ATEX compliance depends entirely on using certified equipment in the correct zones. Many projects have ordered equipment based on incomplete specifications, then discovered during commissioning that the device doesn't meet requirements. The challenge is that ATEX certificates are complex and equipment suppliers sometimes provide incomplete datasheets. 3P has learned to always request the full IECEX certificate and cross-check against the zone requirements.

## Standards & Requirements

- EN 60079-15: Non-sparking equipment for ATEX
- EN 60079-2: Pressurized enclosures (Ex p)
- EN 60079-7: Increased safety (Ex e)
- EN 60079-6: Oil immersion (Ex o)
- IECEX System: International certification body
- ATEX Certificate: Required for all equipment in zones

## Best Practices

1. **Always request the full IECEX certificate** — Don't rely on marketing datasheets
2. **Verify EPL matches zone** — Zone 1 requires minimum EPL Gb
3. **Check temperature class** — T4, T3, T2, T1 (T4 = coldest, T1 = hottest)
4. **Document equipment rationale** — Why this device, why this EPL
5. **Build equipment list early** — Long lead times (8-16 weeks for ATEX rated devices)
6. **Get pre-approval from customer** — Some customers mandate specific suppliers
7. **Account for spare parts** — ATEX devices can be hard to source later

## Known Pitfalls

| Pitfall | Consequence | Cost |
|---------|-------------|------|
| Ordering non-certified "similar" equipment | Equipment fails compliance inspection | Complete redesign + new procurement |
| Wrong temperature class | Device failure in hot ambient | Equipment damage + schedule delay |
| Misreading EPL (Ga vs. Gb vs. Gc) | Equipment undersized for zone | Equipment swap + 4-6 week delay |
| Ordering equipment without checking lead time | Delivery in 16 weeks, need it in 4 | Project delayed, penalties |
| Not verifying supplier IECEX accreditation | Fake/non-compliant equipment delivered | Compliance failure, liability |

## Checklist

### Phase 1: Define Equipment Requirements
- [ ] Zone classification completed (Zone 0/1/2 or Zone 20/21/22)
- [ ] Temperature classification determined (T1-T6)
- [ ] Gas group identified (IIA, IIB, IIC) or dust group
- [ ] Required EPL level noted (see table below)
- [ ] Ambient temperature range documented
- [ ] Equipment type identified (PLC, valve, sensor, indicator, etc.)

### Phase 2: Select Equipment
- [ ] Search IECEX database for certified equipment
- [ ] Request full IECEX certificate (not just datasheet)
- [ ] Verify certificate validity (expiration date, accreditation status)
- [ ] Check equipment marking:
  - [ ] ATEX symbol (diamond with "ATEX")
  - [ ] Year of production
  - [ ] Notified Body number
  - [ ] Equipment group and category
- [ ] Verify temperature class matches project requirement
- [ ] Confirm spare parts availability
- [ ] Check lead time (typically 8-16 weeks for ATEX)

### Phase 3: Verify Against Zone
- [ ] EPL Ga required for Zone 0 (equipment with no ATEX rating acceptable)
- [ ] EPL Gb required for Zone 1 (most equipment)
- [ ] EPL Gc acceptable for Zone 2 (standard industrial equipment with ATEX rating)
- [ ] Document rationale for each equipment choice

## Minimum EPL Requirements by Zone

| Zone | Minimum EPL | Description |
|------|-----------|-------------|
| Zone 0 | Ga | Equipment with very high reliability; continuous explosive atmosphere |
| Zone 1 | Gb | Equipment with high reliability; occasional explosive atmosphere during normal operation |
| Zone 2 | Gc | Standard ATEX equipment; rare/brief explosive atmosphere |

## How to Read ATEX Markings

Example: **II 2G Ex db eb IIC T4 Gb**

Breaking it down:
- **II** = Equipment Group II (not mines)
- **2** = Category (2 = high risk, for Zones 1 & 2)
- **G** = Gas atmosphere (not dust)
- **Ex db** = Protection type (d = flameproof enclosure, b = increased safety connections)
- **eb** = Additional protection (e = increased safety, b = increased safety connections)
- **IIC** = Gas group (IIC = most stringent, includes hydrogen & acetylene)
- **T4** = Temperature class (T4 = max surface temp 135°C)
- **Gb** = Equipment Protection Level (b = high reliability)

## Lessons Learned

### Ammonia Sensor Specification Error (Unibio Project, 2025)

**Initial Specification:** Gas detector rated for IIA, T3
**Required Specification:** IIB or higher (ammonia is Group IIA), T4
**Root Cause:** Project engineer copied equipment from previous hydrogen project without updating gas group.

**What Happened:** Equipment ordered, arrived, then discovered during compliance review that detector wasn't rated for ammonia vapors. Supplier couldn't provide IIB version in time. Had to rush-order from secondary supplier at 40% premium + 3-week delay.

**Cost:** €8K extra equipment + 3 weeks schedule delay

**Action for Next Time:**
- Always check gas group against SDS
- Have equipment list reviewed by safety officer before procurement
- Build 2-week buffer into equipment delivery schedule
- Maintain approved vendor list with lead times

## References

- IECEX Database: https://www.iecex.com/
- EN 60079-14:2013 — Zone classification standard
- 3P Equipment Approval List — See internal database for approved suppliers and lead times
- ATEX Notified Bodies: https://nando.ec.europa.eu/
