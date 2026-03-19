# ATEX Risk Assessment

**Project:** ArlaFoods / ARLA001
**Phase:** Analyse
**Date:** 2026-03-19

---

# ATEX RISK ASSESSMENT ANALYSIS
## TRACE HEATING Installation Documentation

---

## 1. EXECUTIVE SUMMARY

This document is a **Danish installation guide for trace heating systems** (Heatcom Corporation A/S). While it contains safety-relevant information, **it does NOT constitute a formal ATEX risk assessment** and demonstrates significant gaps in ATEX compliance documentation for potentially hazardous area applications.

---

## 2. ATEX APPLICABILITY ASSESSMENT

### 2.1 Missing Hazard Classification
- **No ATEX category designation** (Category 1G, 2G, 3G for gases; 1D, 2D, 3D for dusts)
- **No indication of intended use** in potentially explosive atmospheres
- **No reference to ATEX Directive 2014/34/EU**

### 2.2 Application Context Uncertainty
The document does not specify:
- Whether the trace heating system is intended for **hazardous areas**
- What **Group** (I, II) or **Category** applies
- If equipment is certified under ATEX or IECEx

---

## 3. CRITICAL TECHNICAL GAPS

### 3.1 Electrical Safety Issues (ATEX-Relevant)

| Issue | ATEX Requirement | Document Status |
|-------|------------------|-----------------|
| **RCD Protection** | Required (max. 30 mA) | ✓ Mentioned (§5) |
| **Earthing/Bonding** | Critical for Zone equipment | ✓ Mentioned briefly |
| **Cable Damage Inspection** | Mandatory before use | ✓ Referenced (§5) |
| **Surface Temperature** | Maximum limiting (T-class) | ✗ **NOT SPECIFIED** |
| **Energy Limitation** | Intrinsic safety concepts | ✗ **ABSENT** |
| **Fault Analysis** | Short-circuit/overload scenarios | ✗ **ABSENT** |

### 3.2 Missing Critical Safety Parameters

**Temperature Classification (T-Class)**
- No maximum surface temperature declared
- No T-class assignment (T1-T6 for ATEX II equipment)
- Thermal runaway scenarios not addressed

**Power Density & Heat Dissipation**
- No maximum wattage per unit length specified
- No thermal stability analysis under fault conditions
- Relevant for ignition temperature assessment

**Cable Construction**
- Outer sheath material suitability not verified for ATEX
- Flex-cracking resistance not mentioned
- Conductor insulation breakdown thresholds not provided

---

## 4. OPERATIONAL SAFETY DEFICIENCIES

### 4.1 Installation Practices

| Requirement | Status | Risk |
|---|---|---|
| Authorized electrician supervision | ✓ Stated | MEDIUM |
| Cable routing/stress management | ✓ Detailed | LOW |
| Mechanical protection | ✓ Mentioned | MEDIUM |
| Non-metallic pipe aluminum wrapping | ✓ Required | LOW |
| Connection weatherproofing | ✓ Drain requirement | LOW |
| **Surface temperature monitoring** | ✗ MISSING | **HIGH** |
| **Thermostat/cutoff certification** | ✗ MISSING | **HIGH** |

### 4.2 Documentation Deficiencies

**Missing ATEX-Critical Information:**
- ✗ Declaration of Conformity reference
- ✗ Technical construction file reference
- ✗ Notified Body number (if Category 1/2)
- ✗ Test certificates or certification marks
- ✗ User manual ATEX-specific section
- ✗ Maintenance procedures (ATEX requirements)
- ✗ Inspection intervals for hazardous area use

---

## 5. RISK ANALYSIS

### 5.1 Identified Hazards

**Source: Cable Thermal Characteristics**
| Hazard | Mechanism | Consequence | Severity |
|--------|-----------|-------------|----------|
| **Thermal runaway** | Uncontrolled heating due to thermostat failure or overpowering | Ignition of flammable atmosphere | **CRITICAL** |
| **Mechanical damage** | Installation stress or external impact | Insulation breach → electrical ignition | **HIGH** |
| **Moisture ingress** | Condensation in connection boxes | Leakage current / tracking | **MEDIUM** |
| **Inadequate bonding** | Loose grounding connection | Static discharge potential | **MEDIUM** |
| **Overcurrent** | Fault scenarios | Heat generation above design limits | **HIGH** |

### 5.2 Residual Risk Assessment

**Without formal ATEX certification documentation:**
- **Probability of hazardous failure**: INDETERMINATE (cannot verify control measures)
- **Consequence if failure occurs**: SEVERE (potential explosion/fire)
- **Overall Risk Level**: **UNACCEPTABLE** for use in explosive atmospheres without manufacturer ATEX certification

---

## 6. REGULATORY COMPLIANCE STATUS

### 6.1 ATEX Directive 2014/34/EU Assessment

| Requirement | Compliance Status |
|-------------|-------------------|
| **Equipment Classification** | ✗ NOT DECLARED |
| **Conformity Assessment Module** | ✗ NOT REFERENCED |
| **Technical Documentation** | ✗ INCOMPLETE (per Annex VIII) |
| **Declaration of Conformity** | ✗ NOT PROVIDED |
| **Notified Body Involvement** | ✗ NOT MENTIONED |
| **User Instructions** | ⚠ PARTIAL (no ATEX section) |
| **Maintenance Procedures** | ✗ NOT ATEX-SPECIFIC |
| **Labeling/Marking** | ✗ NOT ADDRESSED |

### 6.2 EN Standards Non-Compliance

Document does not reference:
- **EN 60079-14** (Electrical installations - hazardous areas)
- **EN 60079-15** (Non-sparking equipment)
- **EN 60079-19** (Repair and modification)
- **EN 60079-7** (Increased safety equipment)

---

## 7. SPECIFIC TECHNICAL CONCERNS

### 7.1 Thermal Stability

**Critical Gap**: No information on:
- Self-regulating vs. constant-wattage cable type
- Thermostat specifications and reliability
- Behavior under fault conditions (short-circuit to ground)
- Maximum sustained operating temperature

**ATEX Implication**: Equipment may exceed T-class limits during faults.

### 7.2 Electrical Connection Details

Document specifies:
- ✓ RCD max. 30 mA (good)
- ✗ **No specification of circuit breaker rating**
- ✗ **No fault loop impedance analysis**
- ✗ **No arc flash assessment**
- ⚠ Grounding mentioned but not detailed

### 7.3 Mechanical Integrity

Installation guidance addresses:
- ✓ Cable routing
- ✓ Support spacing (0.3 m intervals with fiberglass tape)
- ✗ **No inspection protocol for mechanical damage in service**
- ✗ **No guidance on repair/replacement in hazardous areas**

---

## 8. RECOMMENDATIONS

### 8.1 Immediate Actions (Use Prohibition Level)

**DO NOT use this equipment in ATEX zones without:**

1. **Manufacturer's ATEX Certification Document**
   - Certificate of Conformity
   - ATEX marking (II 2G Xx or equivalent)
   - Technical construction file (per Annex VIII)

2. **System-Level ATEX Risk Assessment**
   - Determine explosive atmosphere parameters (Group II vs. I)
   - Classify zones (0/1/2 for gas; 20/21/22 for dust)
   - Select appropriate equipment categories
   - Verify T-class compatibility

3. **Authorized Installation Certification**
   - Work by ATEX-certified installer (per EN 60079-19)
   - Commissioning test report
   - As-built documentation

### 8.2 Documentation Requirements

Manufacturer (Heatcom) must provide:
- [ ] ATEX Declaration of Conformity
- [ ] Surface temperature data / T-class
- [ ] Fault condition analysis
- [ ] Notified Body assessment (if Cat. 1/2)
- [ ] ATEX-specific safety supplement to installation guide
- [ ] Maintenance/inspection procedures

### 8.3 Site-Level Controls

For each
