# ATEX Risk Assessment

**Project:** ArlaFoods / ARLA001
**Phase:** Analyse
**Date:** 2026-03-19

---

# ATEX Risk Assessment Analysis
## TRACE HEATING Installation Document

---

## 1. EXECUTIVE SUMMARY

**Assessment Status:** ⚠️ **INCOMPLETE ATEX COMPLIANCE DOCUMENTATION**

This installation guide lacks formal ATEX (Directive 2014/34/EU) risk assessment documentation. While containing operational safety guidance, it does not demonstrate systematic hazard identification, risk evaluation, or ATEX-specific compliance measures for potentially explosive atmospheres.

---

## 2. DOCUMENT CLASSIFICATION

| Parameter | Finding |
|-----------|---------|
| **ATEX Declarations** | None present |
| **Equipment Category** | Not specified |
| **Explosive Atmosphere Reference** | Absent |
| **Risk Assessment Framework** | Not evident |
| **Technical File Reference** | Not included |

---

## 3. HAZARD IDENTIFICATION

### 3.1 Electrical Hazards (ATEX-Relevant)

| Hazard | Source | Severity |
|--------|--------|----------|
| Electrical shock | Improper connection/isolation | High |
| Arc/spark generation | Cable damage, poor connections | High |
| Overheating | Excessive current, insulation failure | High |
| Ground faults | Missing/inadequate earthing | High |

**Critical Gap:** No ATEX surface temperature limits specified (Category 2/3 equipment typically requires T-class ratings: T1-T6).

### 3.2 Thermal Hazards

- Uncontrolled heat generation at junction points
- No maximum surface temperature specification
- No reference to ATEX temperature classifications

### 3.3 Mechanical Hazards

- Cable damage during installation
- Inadequate strain relief
- No mention of mechanical protection for hazardous areas

---

## 4. MISSING ATEX-SPECIFIC ELEMENTS

### 4.1 Mandatory Documentation Gaps

```
Required for ATEX Compliance:
✗ Equipment marking (e.g., II 2G Ex db IIC T4 Gb)
✗ Group and Category classification
✗ Gas/vapour/dust classification
✗ Temperature class declaration
✗ Conformity Assessment procedure reference
✗ EC Declaration of Conformity
✗ Technical Construction File reference
```

### 4.2 Risk Assessment Deficiencies

| Requirement | Status | Evidence |
|------------|--------|----------|
| Hazard classification | Missing | No reference to IEC 60079 series |
| Probability assessment | Missing | No risk matrix |
| Consequence analysis | Missing | No severity classification |
| Mitigation measures | Partial | General electrical safety only |
| Residual risk statement | Missing | None |

---

## 5. TECHNICAL SAFETY MEASURES IDENTIFIED

### 5.1 Present Controls

✓ **RCD Protection:** 30 mA residual current device mandated
✓ **Earthing:** Ground conductor/screen connection required
✓ **Installation Authority:** Licensed electrician requirement
✓ **Cable Integrity:** Prohibition on damaged cable use
✓ **Connector Drainage:** Condensation prevention specified
✓ **Insulation Standards:** Material temperature rating verification

### 5.2 Insufficient Controls for ATEX

✗ No surface temperature monitoring
✗ No cable sheath thermal rating (e.g., PVC/XLPE limits)
✗ No emergency isolation procedures
✗ No maintenance schedules
✗ No inspection/testing protocols (per IEC 60079-19)

---

## 6. INSTALLATION PRACTICES ANALYSIS

### 6.1 Positive Aspects

- Physical separation guidance (avoid tension/damage)
- Proper routing specifications
- Thermal insulation requirements
- Connector location (above ground level)
- Material compatibility (aluminum foil for non-metallic pipes)

### 6.2 ATEX-Critical Gaps

| Aspect | Deficiency |
|--------|-----------|
| **Cable selection** | No ATEX-certified cable reference |
| **Termination kits** | No ATEX compliance specification |
| **Environmental conditions** | No zone classification reference |
| **Operational limits** | No duty cycle or intermittency guidance |
| **Inspection intervals** | Absent |

---

## 7. REGULATORY COMPLIANCE ASSESSMENT

### 7.1 ATEX Directive 2014/34/EU Requirements

| Requirement | Compliance |
|-------------|-----------|
| Equipment category definition | ❌ Not addressed |
| Notified Body involvement | ❌ No evidence |
| Conformity assessment | ❌ Not documented |
| CE marking prerequisites | ❌ Missing |
| Technical documentation | ❌ Incomplete |
| Instructions in Danish | ✓ Provided |

### 7.2 Harmonized Standards Non-Compliance

- **IEC 60079-14** (Electrical installations in hazardous areas) – Not referenced
- **IEC 60079-18** (Equipment not capable of igniting explosive atmospheres) – Not assessed
- **IEC 60079-19** (Repair, overhaul, inspection, maintenance) – No procedures

---

## 8. RISK MATRIX

### 8.1 Current State Assessment

```
Hazard: Uncontrolled Surface Temperature in ATEX Zone
  Probability (Installation errors): Medium-High
  Consequence (Ignition): Critical
  → Risk Level: UNACCEPTABLE without ATEX controls

Hazard: Cable Damage During Installation
  Probability: Medium (manual installation)
  Consequence: Electrical ignition source
  → Risk Level: HIGH (inadequate mitigations)

Hazard: Inadequate Earthing
  Probability: Medium (field installation)
  Consequence: Static accumulation/electrical hazard
  → Risk Level: HIGH
```

---

## 9. RECOMMENDATIONS

### 9.1 Immediate Actions Required

1. **Obtain ATEX Declaration of Conformity** from manufacturer
2. **Verify Equipment Category:**
   - Category 2G (Group II, Category 2, Gas)
   - Category 3G (if lower risk environment)
3. **Specify Temperature Class** (T1-T6 rating per IEC 60079-0)
4. **Provide Technical File** reference with:
   - Surface temperature calculations
   - Cable thermal specifications
   - Electrical schematic (ATEX-compliant)

### 9.2 Documentation Enhancements

| Addition | Priority |
|----------|----------|
| Surface temperature limits (°C) | **CRITICAL** |
| ATEX marking/classification | **CRITICAL** |
| Zone suitability statement | **CRITICAL** |
| Cable sheath material temp. rating | **HIGH** |
| Inspection/maintenance schedule (IEC 60079-19) | **HIGH** |
| Fault scenario analysis | **MEDIUM** |

### 9.3 Installation Procedure Modifications

```
Add to installation guide:
- Pre-installation ATEX compliance checklist
- Temperature monitoring during commissioning
- Photo documentation of cable routing
- Earthing resistance testing (target: <1 Ω)
- Annual inspection protocol
- Defect reporting procedure
```

---

## 10. RESIDUAL RISK STATEMENT

**Current State:** Without ATEX certification documentation and temperature class specification, **residual risk cannot be quantified or accepted** for use in explosive atmospheres.

**Required Certification Level:** Formal ATEX Annex VIII (Notified Body) technical documentation or manufacturer's Declaration of Conformity under Annex VI.

---

## 11. CONCLUSIONS

| Finding | Assessment |
|---------|------------|
| **ATEX Readiness** | Non-compliant |
| **Functional Safety** | Partial (general electrical safety only) |
| **Explosive Atmosphere Suitability** | **Unverified** |
| **Installation Risk** | **HIGH** without ATEX controls |

**Recommendation:** **DO NOT DEPLOY** in classified hazardous areas (ATEX Zones) until formal ATEX compliance documentation is obtained and installation procedures are amended to reference ATEX standards.

---

**Document Assessment Date:** [Current]  
**Assessor Status:** Technical compliance review only – legal/regulatory interpretation requires competent authority consultation.
