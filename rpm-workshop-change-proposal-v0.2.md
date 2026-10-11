# RPM Apps Workshop — Change Proposal v0.2
Generated: 2026-04-07

---

## Section 1: Feedback Source Summary

### Source 1: Recording Transcript — `GMT20260407-150429_Recording_as_1920x1080.txt`
**Participants:** Gunnar (workshop author), Jan (T&Q SME), Chan (joined briefly), Connor/Noel (background)

A screen-share review session covering the full v0.1 workshop. Gunnar and Jan went page-by-page through T&Q sections together. Key themes:
- Confirmed the **Tell-Show-Do** structure is correct for labs; T&Q overview should be 10–15 min level-set only
- Identified **configurator content is organized wrong** (by functional grouping, should be page-by-page by UX page number)
- Screenshots throughout configurator and application review sections are **wrong page / wrong section**
- The configurator **lab is giving away answers** — should make participants interpret the case study themselves
- Data errors: **5-tier hierarchy, missing Opportunity file**
- T&Q application review section needs to match the **13-section UX app structure** (Jan gave a full breakdown of all sections on the call)
- **Data flow direction** is inverted in Data Integration section (spoke pulls from hub, not hub pushes to spoke)
- **V3 compatibility warning**: T&Q content will need revamping in a few months once V3 screens are finalized

### Source 2: Enablement Content V0.1 Notes — `Enablement Content V0.1 Notes.docx`
**Author:** Jan (primary T&Q SME)

Structured written notes covering every section of the workshop. Mirrors and extends the transcript feedback with precise, itemized corrections. Key areas:
- ICM terminology fix (SPM Overview)
- Employee file schema rename (User ID → Employee ID)
- Detailed breakdown of what Data Hub Setup section is missing (attribute mapping steps, boolean explanations, common pitfalls)
- Precise per-section corrections for configurator pages 1.00–1.09
- Lab corrections: wrong hierarchy tier count/naming, "CW" files mystery, answer-key-style format
- Application Review: granular screenshot and section organization fixes aligned to UX app numbering
- Data Integration flow direction fix

### Source 3: Chan's Direct Feedback — `Workshop Feedback from Chan.txt`
**Author:** Chan (Segmentation & Capacity SME)

Focused specifically on Day 2 content (Segmentation and Capacity Planning). Chan flagged:
- **Segmentation**: thin questions section, data structure misconception (banded format is app-generated, not upstream), configurator lab steps that blend configurator with template app, wrong/missing page labels
- **Capacity Planning**: NTE description is factually wrong (not set by finance), ramping profile description needs improvement, wrong screenshots in lab (C1 shows Segmentation screen), bottoms-up approval level consistency error
- **Both modules**: model review sections use incorrect module labels

### Source 4: Configuration Guides
Three official product team guides were reviewed for structure and technical accuracy:

- **T&Q Configuration Guide V3.0** — Covers hierarchy configuration (2–10 levels per model), configuration questions (top-level + model-specific), post-config tasks, V3 architecture decisions (Polaris, ADO replacing imports, scenario planning across all functionality), ADO setup steps, known issues
- **GTM Capacity Planning Config Guide V2.0** — Single model (Template SS & GCP – Spoke PROD); 5 key architecture decisions including fixed 2-level Job Family hierarchy, single-year forward planning, Position list for historical tracking, optional Role Grade granularity; ADO manual setup steps
- **Segmentation & Scoring Config Guide V2.0** — Same single model as GTM Capacity; 6 architecture decisions including UCP (Unacceptable Customer Profile) for account exclusion, shadow rules for conflict resolution, multiple wallet sizing methods, shadow input modules for performance

---

## Section 2: Proposed Changes by Workshop Page

### `00-overview.html` — Workshop Overview / Getting Started

| # | Status | Change Type | What to Change | Source | Priority |
|---|--------|-------------|----------------|--------|----------|
| O-1 | **Done** (verified 2026-04-19) | Delete | Remove sentence about "pay attention to the red tab decisions in configurator" — Gunnar confirmed this is unclear/inaccurate and should be taken out | Transcript + Notes | High |
| O-2 | **Done** (verified 2026-04-19) | Rewrite | Change language around "Do capacity planning before you finalize the territory hierarchy" — reframe as a judgment call; both often happen in parallel; remove prescriptive ordering. Verified at lines 399, 409, 412. | Transcript + Notes | High |
| O-3 | **Done** (applied 2026-04-19) | Add context | Add brief note that T&Q content reflects V2; V3 screens will differ and content will be updated in a future version. Implemented as `callout-note` "T&Q content reflects V2" at end of "About This Workshop" section. | Transcript | Medium |
| O-4 | **Done** (applied 2026-04-19) | Rewrite / Extend | Expand the **"About This Workshop"** section. Keep the existing two opening paragraphs; add three new subsections (`<h3>`): "What we assume you bring" (pre-built vs from-scratch mindset), "What we will actually do" (pre-project assets → real client data → T&Q first as the Application-Led Workshop app), and "When the base app isn't enough" (extension labs). Full revised text below. | Gunnar (2026-04-16) | High |

#### O-4 detail: revised "About This Workshop" section

**Location:** [docs/00-overview.html:99-101](docs/00-overview.html#L99-L101) — replace the current `<h2>About This Workshop</h2>` block (current content is two `<p>` paragraphs ending before `<h2>How Each Module Flows</h2>`).

**Current text (to be replaced):**

> The **RPM Apps Technical Enablement Workshop** is a hands-on technical enablement program for Anaplan delivery practitioners — Solutions Consultants, Solution Architects, and Technical Consultants — who will be implementing or supporting the Anaplan Revenue Performance Management (RPM) application suite.
>
> This is not a lecture series. It is a structured sequence of demonstrations, discussions, and hands-on labs designed to take you from *knowing about* these applications to being capable of *configuring, explaining, and delivering* them for real customers.

**New text (approved 2026-04-16):**

> **About This Workshop**
>
> The **RPM Apps Technical Enablement Workshop** is a hands-on technical enablement program for Anaplan delivery practitioners — Solutions Consultants, Solution Architects, and Technical Consultants — who will be implementing or supporting the Anaplan Revenue Performance Management (RPM) application suite.
>
> This is not a lecture series. It is a structured sequence of demonstrations, discussions, and hands-on labs designed to take you from *knowing about* these applications to being capable of *configuring, explaining, and delivering* them for real customers.
>
> ### What we assume you bring
>
> This workshop assumes you already understand what pre-built applications are — and what they are not — and the prescribed methodology used to prepare, configure, and deliver them. If your Anaplan background is in from-scratch model building, be aware that delivering a pre-built application is fundamentally different work. The configurator, the data inputs, and the post-generation steps are not optional shortcuts around custom modeling — they *are* the delivery method.
>
> ### What we will actually do
>
> We will start by briefly reviewing the common assets that are expected to be shared with you during the pre-project phase — what to ask for, what to expect, and how to read what you receive. As we move into configuration, we will work with the data the client has provided. Not dummy data — real territories, real products, real hierarchies. This data is the input that drives configuration, and configuration is the input that drives what gets built into the client tenant. Treat this step with the weight it deserves: the decisions you make here determine what shows up in the app.
>
> With that input in hand, we will configure and build the **Territory & Quota** application first. T&Q is the application you will use during your Application-Led Workshops with clients — the one that demonstrates what comes out of the box. We will spend a full lab exploring the generated app in depth, because there is a lot to cover.
>
> ### When the base app isn't enough
>
> From there, we will look at scenarios where the base application needs to be extended. Several labs will walk through building and deploying extensions, ranging from straightforward changes to more involved work that requires more careful design upfront.

**HTML structure note for whoever applies this:** The new subsections use `<h3>` tags. The existing `<h2>How Each Module Flows</h2>` block immediately following should remain unchanged.

---

### `00-case-study.html` — Case Study Overview

| # | Change Type | What to Change | Source | Priority |
|---|-------------|----------------|--------|----------|
| CS-1 | Fix | Fix hierarchy tier count: currently shows 4-tier, must be **5-tier**: Geo → Area → Region → Sub-Region → Territory | Transcript + Notes | High |
| CS-2 | Fix | Add missing **Opportunity** file to data set files list — currently only shows Opportunity Line. Opportunity is the parent record and must be included | Transcript + Notes | High |
| CS-3 | Verify | Confirm no references to "CW underscore" or "CloudWorks_" prefixed files exist in the case study data set list — source of these files is unknown | Transcript + Notes | High |

---

### `01-spm-overview.html` — SPM Overview

| # | Change Type | What to Change | Source | Priority |
|---|-------------|----------------|--------|----------|
| SPM-1 | Terminology | Change "split allocation" to **"crediting allocation and logic"** in ICM overview | Notes | Medium |

---

### `tq-01-overview.html` — T&Q Functional Overview

| # | Change Type | What to Change | Source | Priority |
|---|-------------|----------------|--------|----------|
| TQ-1 | Fix | Update territory hierarchy tier limit: change "more than 5 tiers" to **"up to 10 tiers (default)"** — V3 default will be 10 | Transcript + Notes | High |
| TQ-2 | Add | Add **Product** to the required data objects section — it's almost always required in practice (notes suggest labeling it "almost always required") | Notes | Medium |
| TQ-3 | Fix | Employee file schema: rename **"User ID" → "Employee ID"** and **"Username" → "Employee Name"** — "user" has a different connotation in Anaplan | Transcript + Notes | High |
| TQ-4 | Fix | Remove or correct statement that "primary key must match the Anaplan user ID" — it doesn't need to match anything; it just needs to be a unique employee identifier | Transcript + Notes | High |
| TQ-5 | Add | Add **role start date / end date** fields to employee file schema | Notes | Medium |
| TQ-6 | Clarify | V2 territory file: remove language "all tiers as columns" — V2 requires one file with all hierarchy levels, but this phrasing is confusing | Notes | Medium |
| TQ-7 | Add | Note that **Planning Measure** is a required list (not a data set in the same way) — decide whether to mention it here or leave out (flagged as optional by Jan) | Notes | Low |

---

### `03-configurator-walkthrough.html` — Configurator Review

**Overall structural change (HIGH priority):** The entire section must be restructured from functional groupings to **page-by-page UX page order** (1.00 through 1.09). Each section must be labeled with the exact UX page number and name (e.g., "1.03 Scenario Planning"), not a functional description. Screenshots must come from the exact UX page being described.

| # | Change Type | What to Change | Source | Priority |
|---|-------------|----------------|--------|----------|
| CR-1 | Restructure | Rebuild section structure page-by-page: **1.00 Getting Started → 1.01 Data Hub Setup → 1.02 Hierarchy Setup → 1.03 Scenario Planning → 1.04 Planning Measures → 1.05 Optimizer → 1.06 Target and Allocation → 1.07 Territory Assignment → 1.08 Resource Assignment → 1.09 Rule Engine Setup** (confirm exact page numbering against live app) | Transcript + Notes | High |
| CR-2 | Fix | Remove all functional section names (e.g., "Transactional Data Routing") — replace with UX page number + name | Transcript + Notes | High |
| CR-3 | Fix | **All screenshots** must be replaced with screenshots from the exact UX page being described. Multiple current screenshots are confirmed wrong (e.g., "Getting Started" section uses a 1.01 Data Hub Setup screenshot) | Transcript + Notes | High |
| CR-4 | Refocus | Remove all content that describes the **generated app's UX and functionality** (e.g., ramp types: fast/regular/slow) — this section must focus exclusively on what is configured in the Configurator, not how the generated app works | Transcript + Notes | High |
| CR-5 | Improve | For each configurator page, use **the app's own in-page notes/instructions** as the basis for describing each input table — the app is largely self-documenting | Transcript | Medium |

**Page-specific changes within Configurator Review:**

| # | Page | Change Type | What to Change | Source | Priority |
|---|------|-------------|----------------|--------|----------|
| CR-6 | 1.01 Data Hub Setup | Expand | Section is not robust enough. Add: (a) steps to map core data objects from customer data against Anaplan data objects; (b) using Objects/Attributes in configurator to map existing attributes, renaming as needed; (c) how to add new attributes when no match exists; (d) ensuring data formats are correct | Notes | High |
| CR-7 | 1.01 Data Hub Setup | Reframe | "Three Critical Booleans" — reframe from configurator steps to **"things to consider before starting implementation"**: Are you using existing data hub? Are you using ADO? These aren't selections made during configuration in V3 | Transcript + Notes | High |
| CR-8 | 1.01 Data Hub Setup | Add | Explain the three booleans properly: *Enable for Calculations* (creates list from attribute), *Enable for Validation* (checks new data against existing list), *Enable for Auto Create* (generated saved views/actions to add new items on import) | Notes | Medium |
| CR-9 | 1.01 Data Hub Setup | Add | Add common pitfalls: Order/Order Details + Opportunity/Opportunity Line — customers often only have 1 file; note that duplicate attributes across header/detail levels cause errors and should be addressed | Notes | Medium |
| CR-10 | 1.02 Hierarchy Setup | Fix | Clarify that this covers **all hierarchies in the app**, not just territory hierarchy (including any custom ones added in Data Hub Setup) | Notes | Medium |
| CR-11 | 1.02 Hierarchy Setup | Delete | Remove the last 3 bullets on "key settings" (flagged as incorrect/irrelevant) | Notes | Medium |
| CR-12 | 1.04 Planning Measures | Fix | Replace screenshot — current screenshot is from wrong page | Notes | High |
| CR-13 | 1.05 Optimizer | Fix | Replace screenshot — current screenshot is from wrong page | Notes | High |
| CR-14 | 1.06 Target and Allocation | Add | Add **time granularity** (at which targets are planned) to key settings | Notes | Medium |
| CR-15 | 1.06 Target and Allocation | Fix | Change wording on "Critical" tip: "Every extra dimension (such as product, industry, etc…)" — confirm exact language with Jan's note | Notes | Medium |
| CR-16 | 1.07 Territory Assignment | Fix | Correct conceptual error: all assignment methods **will all generate** — you are NOT "configuring which to enable." You are configuring **at what level of the hierarchy** each assignment method takes effect | Transcript + Notes | High |
| CR-17 | 1.07 Territory Assignment | Improve | Note that in-app instructions on the UX page are good guides for this section | Transcript | Low |
| CR-18 | 1.08 Resource Assignment | Fix | Remove mention of "full vs split" and "ramping" — the configurator does NOT cover these. This page configures the **level at which assignments and approvals happen** | Notes | High |
| CR-19 | Account Capacity (section 13) | Remove/Move | This section is in an incorrect order; likely remove or reposition | Notes | Medium |
| CR-20 | 1.09 Rule Engine Setup | Fix | Correct focus: NOT about configuring priority/conflicts — it's about configuring which **attributes are relevant for (1) eligibility and (2) rules** | Notes | Medium |

---

### `04-configurator-exercise.html` — Lab: Configurator

**Overall structural change (HIGH priority):** The lab currently gives away answers (it functions as an answer key + exercise combined). This must be separated: participants should interpret the case study and decide what to enter, with a linked answer key separate from the exercise prompts.

| # | Change Type | What to Change | Source | Priority |
|---|-------------|----------------|--------|----------|
| LAB-1 | Restructure | Convert to exercise-only format: prompt participants to go to each configurator page, look at the case study, and fill in the inputs themselves. Provide a separate answer key link (not inline) | Transcript + Notes | High |
| LAB-2 | Restructure | Organize lab page-by-page matching configurator structure (1.00 → 1.09), mirroring the updated Configurator Review section | Transcript + Notes | High |
| LAB-3 | Fix | Fix hierarchy: **4-tier → 5-tier** and fix naming to align to case study template (Geo → Area → Region → Sub-Region → Territory) | Transcript + Notes | High |
| LAB-4 | Remove | Remove all references to "CW_" or "CloudWorks_" prefixed files — source unknown, likely incorrect | Transcript + Notes | High |
| LAB-5 | Fix | Data Hub Setup: remove booleans as configurator steps; fix Attributes section instructions and screenshot — current ones do not make sense | Notes | High |
| LAB-6 | Fix | Hierarchy Setup: correct tier count and naming; replace screenshot (current one is unhelpful) | Notes | High |

---

### `07-spoke-app-walkthrough.html` — T&Q Application Review (UX App Walkthrough)

**Overall structural change (HIGH priority):** The application review must be reorganized to exactly mirror the T&Q app's 13-section structure. Jan provided a comprehensive breakdown of all sections and sub-pages on the call (see detail below).

| # | Change Type | What to Change | Source | Priority |
|---|-------------|----------------|--------|----------|
| AR-1 | Restructure | Reorganize to match the 13-section app structure in order: 1 (Overview/Landing), 2 (Historical Sales), 3 (Scenario Planning), 4 (Target Setup), 5 (Approvals), 6 (Resource/People), 7 (Territory & Account Assignment), 8 (Strategic Accounts — optional), 9 (Named Accounts — optional), 10 (Quotas), 11 (Rule-Based Assignment), 12+ (Assumptions/Admin) | Transcript | High |
| AR-2 | Fix | **All screenshots** where the screenshot doesn't match the section being described must be replaced. Multiple confirmed wrong: Section 3 Scenario Planning uses a Section 2 screenshot, Section 6/7 area uses wrong pages | Transcript | High |
| AR-3 | Rewrite | Section 3 (Scenario Planning): focus content on **pages 3.6–3.9** — 3.1–3.5 are rarely used. Cover account assignment comparison across scenarios (3.6) and optimizer setup (3.7–3.9) | Transcript | Medium |
| AR-4 | Add | Section 5 (Approvals): add section explaining the approval workflow (4 sub-pages; approved targets become read-only via Dynamic Cell Access) | Transcript | Medium |
| AR-5 | Improve | Section 6 (People/Resource): highlight **TBH (To Be Hired) reps** as a key integration point with Capacity Planning app | Transcript | Medium |
| AR-6 | Fix | Section 6 (People): Split into sub-sections: 6.1 people roster + TBH, 6.2 rep-to-territory assignment, 6.3 manager assignment, 6.4 overlay assignment | Transcript | Medium |
| AR-7 | Fix | Resource & Quota: currently combines sections 6 and 10 — separate into distinct sections: Resource Setup (section 6) and Quota (section 10) | Notes | High |
| AR-8 | Fix | Resource & Quota: Remove "raw vs discrete" quota terminology — this is not standard language; has never been used | Notes | High |
| AR-9 | Fix | Resource & Quota: Move Admin Setup to its own section at the bottom; include screenshot from "Model Assumptions and Inputs" UX page | Notes | Medium |
| AR-10 | Fix | Resource & Quota: Update screenshot from 10.1 (not 6.1) for quota section | Notes | High |
| AR-11 | Fix | Territory Management: Change first screenshot to be from **7.1** | Notes | High |
| AR-12 | Fix | Potential Spend (Application Review): Remove APCD; fix screenshot | Notes | Medium |
| AR-13 | Fix | Scenario Planning subsection: Replace screenshot with one from **page 3.6** | Notes | High |
| AR-14 | Fix | Target Setup: Change "Finance provides annual or quarterly targets" → **"Finance provides targets at the time granularity specified in the configurator"** (can also be monthly) | Notes | Medium |
| AR-15 | Add | Target Setup: Add section for **page 4.7** — logic on setting bottoms-up quotas and how this can be used in addition to tops-down targets | Notes | Medium |
| AR-16 | Fix | Administration: Replace **both screenshots** | Notes | High |
| AR-17 | Consider | Sections 8 (Strategic Accounts) and 9 (Named Accounts): Jan suggests these don't need to be covered; if included, go page-by-page | Transcript | Low |

**Jan's full app structure breakdown for reference (use to guide AR-1):**
- **Section 1** (3 pages): Home/directory, 2x sales management dashboards (landing pages for sales managers)
- **Section 2** (3 pages): Historical sales data; 2.1 addressable market by account; 2.3 account info + segment override (important: segment is key attribute)
- **Section 3** (multiple sub-pages): Focus on 3.6 (account assignment scenario comparison) + 3.7–3.9 (optimizer setup)
- **Section 4** (8 pages): 4.1 load targets; 4.2–4.8 cascade targets
- **Section 5** (4 pages): Approval workflow management
- **Section 6** (6 pages): 6.1 people roster + TBH; 6.2 rep-to-territory; 6.3 manager; 6.4 overlay
- **Section 7** (multiple pages): Territory hierarchy + account assignments; 7.2 manual assignment; 7.3 map/lasso assignment; 7.5–7.7 additional assignment pages
- **Section 10**: Quotas — most important page is individual seller quota with ramp; overrides per measure per seller
- **Section 11**: Rule-based account assignment
- **Assumptions**: Model Assumptions and Inputs (key admin page with mappings and parameters)

---

### `tq-02-sample-data.html` — T&Q Sample Data / Data Structure

| # | Change Type | What to Change | Source | Priority |
|---|-------------|----------------|--------|----------|
| SD-1 | Fix | Fix **5-tier hierarchy** throughout (Geo → Area → Region → Sub-Region → Territory) — all references to 4-tier must be updated | Notes | High |
| SD-2 | Add | Add Opportunity file alongside Opportunity Line; clarify parent/child relationship | Transcript + Notes | High |
| SD-3 | Add | Add Product to data objects (almost always required) | Notes | Medium |
| SD-4 | Fix | Rename User ID → Employee ID, Username → Employee Name in employee schema | Notes | High |
| SD-5 | Fix | Remove/correct "primary key must match Anaplan user ID" language — it is simply a unique employee identifier | Transcript + Notes | High |
| SD-6 | Add | Add role start date / end date to employee schema | Notes | Medium |
| SD-7 | Fix | Territory file V2/V3 note: remove "all tiers as columns" language; clarify V2 requires one file with all hierarchy levels | Notes | Medium |

---

### `06-ado-integration.html` — Data Integration

| # | Change Type | What to Change | Source | Priority |
|---|-------------|----------------|--------|----------|
| DI-1 | Fix | **Correct data flow direction for V2**: Change "hub pushes to spoke" → **"spokes pull from hub"** | Transcript + Notes | High |

---

### Segmentation Pages (`seg-01` through `seg-08`)

| # | Page | Change Type | What to Change | Source | Priority |
|---|------|-------------|----------------|--------|----------|
| SEG-1 | seg-01-overview / Questions | Expand | Expand segmentation questions from 1 to more — add: "How many segments make sense?" and "What attributes distinguish one segment from another?" | Chan Feedback | Medium |
| SEG-2 | seg-02-sample-data | Fix | Firmographic data: clarify that the **banded format is produced within the app**, not coming from upstream systems | Chan Feedback | High |
| SEG-3 | seg-02-sample-data | Fix | Employee dataset: label as **nice-to-have, not required** for segmentation | Chan Feedback | Medium |
| SEG-4 | seg-04-lab | Fix (S1) | Fix incorrect page label on S1 | Chan Feedback | High |
| SEG-5 | seg-04-lab | Fix (S2.02) | Remove or replace "Configure Segment list" step — **this page does not exist** in the app | Chan Feedback | High |
| SEG-6 | seg-04-lab | Rewrite (S3) | Separate configurator content from template app content — S3 currently blends both | Chan Feedback | High |
| SEG-7 | seg-04-lab | Rewrite (S4) | Same as S3 — S4 blends configurator and template app; split them | Chan Feedback | High |
| SEG-8 | seg-04-lab | Fix (S4.02) | Remove or correct: the revenue method is **not a selectable option** in this context | Chan Feedback | High |
| SEG-9 | seg-05-post-gen | Update | Post-gen deck content can be updated — review and refresh | Chan Feedback | Low |
| SEG-10 | seg-06-model-review | Fix | Correct key module labels — currently labeled differently than in the document | Chan Feedback | Medium |
| SEG-11 | seg-07-comodeler-lab / App Review | Fix | Correct UCP description: **UCP defines which accounts to EXCLUDE** from all planning activities (not a general segmentation concept) | Chan Feedback | Medium |

---

### Capacity Planning Pages (`cap-01` through `cap-08`)

| # | Page | Change Type | What to Change | Source | Priority |
|---|------|-------------|----------------|--------|----------|
| CAP-1 | cap-01-overview | Fix | **NTE is NOT set by finance.** Correct: NTE is **derived from current headcount, growth %, and attrition %** | Chan Feedback | High |
| CAP-2 | cap-02-sample-data | Improve | Ramping Profile description: clarify it can **vary by role AND geo** — current description too simplistic | Chan Feedback | Medium |
| CAP-3 | cap-01-overview (Configurator Review) | Fix | Inaccurate description of "Role Job Family Hierarchy" — correct to: you are configuring **applicable ramping dimensions and role analysis** | Chan Feedback | High |
| CAP-4 | cap-01-overview (Configurator Review) | Add | Clarify: default app starts at L1 of Job Family from top-down; handles L2 of Job Family HC on step 2 | Chan Feedback | Medium |
| CAP-5 | cap-01-overview (Configurator Review) | Add | Add configuration of **Cost per Head** and **Finance Budget import level** | Chan Feedback | Medium |
| CAP-6 | cap-04-lab | Fix (C1) | Replace incorrect picture — currently shows **Segmentation guided setup**, should show Capacity | Chan Feedback | High |
| CAP-7 | cap-04-lab | Fix (C4) | Replace incorrect picture on C4 | Chan Feedback | High |
| CAP-8 | cap-04-lab | Fix (C5) | Bottoms-up and **approval level must be the same** — fix the lab instructions to clarify this constraint (bottoms-up approval) | Chan Feedback | High |
| CAP-9 | cap-06-model-review | Fix | Correct key module labels — currently not labeled according to the document | Chan Feedback | Medium |

---

## Section 3: New Content from Config Guides

The three configuration guides contain technical detail that is currently absent or underdeveloped in the workshop. The following areas should be used to strengthen specific pages:

### T&Q Configuration Guide V3.0 → Strengthens `03-configurator-walkthrough.html` and `tq-01-overview.html`

1. **V3 Architecture Changes** (major additions):
   - T&Q has moved to **Polaris** from Classic — significant for large-scale, sparse data models
   - **ADO links replace import actions** — Data Hub is no longer required in the workspace for V3
   - Moved from Combination lists to modules dimensioned by both lists (for account-to-territory and rep-to-territory assignments)
   - **Scenario planning is enabled across all functionalities** in V3

2. **Hierarchy Configuration Details** — Useful for Configurator Review 1.02:
   - Hierarchy screen manages all composite hierarchies across both models (T&Q Planning + SPM Optimizer)
   - Number of levels shown represents combined levels across selected models
   - Min: 2 levels, Max: **10 levels per model** (important correction to current workshop content)

3. **ADO Manual Setup** — Strengthen `06-ado-integration.html`:
   - Full step-by-step for manually creating ADO links when PAF generation fails
   - Covers: Source Data tab → Add data → Create link → Map → Push data
   - Include note about cloning to ALM models

4. **Known Issues / Post-Gen Tasks** — Could add a practical callouts box to `05-post-gen-steps.html`:
   - Post-config task categories: Post-Configuration Adjustments, Model Settings (time/versions/roles), Action Settings (mappings/validations/cleanup), UX Settings (context/filters/actions)

### GTM Capacity Planning Config Guide V2.0 → Strengthens `cap-01` through `cap-05`

1. **Architecture Decision: Fixed 2-Level Job Family Hierarchy**:
   - Sales Role list must always serve as the bottom level — useful callout for configurator review
   - This is a known constraint to warn implementers about

2. **Architecture Decision: Position List for Employee Tracking**:
   - Positions use start/end dates to track role changes over time — critical for tenure and ramp calculations
   - Strengthen `cap-02-sample-data.html` employee data explanation

3. **Architecture Decision: Optional Role Grade Granularity**:
   - Default mode: no Role Grade (faster implementation)
   - Optional: Role Grade mode for more precision — good to surface as a configuration choice in the workshop

4. **Architecture Decision: Single-Year Forward-Looking Horizon**:
   - All forward-looking planning is limited to 1 year — good to note as a known constraint

5. **Architecture Decision: Centralized Data Hub (ADO)**:
   - Spoke model pulls from Data Hub — reinforces the correct data flow direction fix for all modules

### Segmentation & Scoring Config Guide V2.0 → Strengthens `seg-01` through `seg-05`

1. **UCP (Unacceptable Customer Profile)**:
   - Design decision: identify and flag accounts to exclude from ALL planning activities upfront
   - Critical to call out in `seg-07-comodeler-lab.html` (aligns with Chan's correction)

2. **Shadow Rules for Conflict Resolution**:
   - One-to-many relationship between user-facing Rule List and Shadow Rule List
   - High performance via Polaris sparse data handling
   - Useful technical context for any rule engine discussion

3. **Multiple Wallet Sizing Methods**:
   - Revenue-based, employee-count-based, etc.
   - Users select method based on industry drivers
   - Could enrich the segmentation overview section

4. **Shadow Input Modules**:
   - High-volume customers use shadow modules to capture inputs before pushing to calculation engine
   - Prevents large-scale recalculations on every data entry
   - Worth a brief mention in segmentation technical overview

5. **Data Load Template / ADO Step-by-Step**:
   - Same ADO manual setup process as T&Q guide — consistent across all three apps
   - Could be consolidated into a shared ADO reference section for all Day 2 apps

---

## Section 4: Open Questions

These items require Gunnar's decision before building v0.2:

| # | Question | Context | Impacted Pages |
|---|----------|---------|----------------|
| Q-1 | **V3 compatibility scope**: How much V3 architecture content should be included now vs. deferred to a "V3 edition"? The transcript confirmed T&Q content will need significant rework once V3 screens are finalized. Should we add a visible "V3 Note" banner to T&Q pages, or build a parallel V3 track? | Jan flagged on call that V3 screens are substantially different and the content will need revamping in a few months | tq-01 through tq-07, 03-configurator-walkthrough, 04-configurator-exercise |
| Q-2 | **Configurator lab answer key**: Should the answer key be a separate HTML page linked from the lab, or a collapsible/hidden section on the same page? | Transcript: Gunnar + Jan agreed lab should not give away answers; need to decide format | 04-configurator-exercise |
| Q-3 | **Screenshots**: Who will provide the updated screenshots for the configurator and application review pages? Jan offered to help supply specific screenshots. Should this be a separate asset delivery step before the build, or should placeholders be built in first? | Transcript: Jan offered help; Gunnar confirmed accuracy > speed for screenshots | 03-configurator-walkthrough, 04-configurator-exercise, 07-spoke-app-walkthrough |
| Q-4 | **Planning Measure in T&Q required data objects**: Jan was unsure whether to include Planning Measure in the required data objects list. It is a required list but not a data set in the same way. Include or exclude? | Notes | tq-02-sample-data |
| Q-5 | **Sections 8 & 9 (Strategic/Named Accounts)**: Jan said these don't need to be covered in depth. Should they be removed entirely from the Application Review, kept as optional/brief sections, or flagged as "advanced topics"? | Transcript | 07-spoke-app-walkthrough |
| Q-6 | **Configurator page numbering**: The workshop currently uses functional section names. Jan referenced page numbers like 1.01, 1.03 etc. Need to confirm the exact page numbering from the live app to ensure labels are accurate before rebuilding | Transcript + Notes | 03-configurator-walkthrough, 04-configurator-exercise |
| Q-7 | **Segmentation configurator lab scope**: Chan flagged that S3 and S4 blend the configurator and template app together. Should the lab be restructured to cover only configurator steps, with template app exploration in a separate section? | Chan Feedback | seg-04-lab |
| Q-8 | **Post-gen content refresh**: Both Chan and the config guides reference separate post-gen PowerPoint decks (Segmentation 2.0, GTM Capacity Planning V2.0 post-gen PPT). Should these be summarized and embedded in the workshop post-gen pages, or linked externally? | Chan Feedback + Config Guides | seg-05-post-gen, cap-05-post-gen |
| Q-9 | **"CloudWorks" data files**: Neither Jan nor Gunnar knows where the "CW underscore" files referenced in the lab are coming from. Need to confirm: are there separate CW-prefixed files, or should the lab use the single shared sample data set? | Transcript + Notes | 04-configurator-exercise, tq-02-sample-data |
| Q-10 | **ADO section consolidation**: All three config guides have identical ADO manual setup steps. Should there be one shared ADO reference page for the workshop, or keep app-specific ADO notes on each app's data integration page? | Config Guides | 06-ado-integration, seg-05-post-gen, cap-05-post-gen |

---

*End of Change Proposal v0.2*
*Sources: Recording transcript (2026-04-07), Enablement Content V0.1 Notes (Jan), Workshop Feedback from Chan (Chan), T&Q Config Guide V3.0, GTM Capacity Config Guide V2.0, S&S Config Guide V2.0*
