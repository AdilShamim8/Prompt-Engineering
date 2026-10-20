# Research Data Management Prompts

Companion prompts to the main researchers guide for the unglamorous layer that determines whether research is verifiable: organizing data, documenting provenance, archiving for reuse, and handling the privacy and ethics obligations that come with research data.

***

## 1. Data Management Plan Drafting

**Prompt:**
```
Draft a data management plan for my study: [DESCRIBE STUDY — design, data types,
volume, duration]. Funder requirements if known: [LIST or "general best practice"].
Cover:
1. What data will be created: formats, estimated volumes, and which are
   "primary" (would be impossible to recreate) versus "derived"
2. Documentation and metadata: naming conventions, README contents, the
   metadata standard closest to my discipline
3. Storage and backup during the project: the 3-2-1 arrangement adapted to my
   constraints (institutional storage, access controls, recovery plan)
4. Preservation after the project: what gets archived, where, for how long,
   and in what license
5. Access and sharing: what can be shared openly, what requires restricted
   access, what cannot be shared and why
6. Responsibilities and timing: who does each of these, at which project stage
Where I have not decided, mark [DECISION NEEDED] — do not fill it in for me.
```

- **Purpose:** The plan funders increasingly require and projects always need.
- **Why it works:** The primary-vs-derived distinction drives every later decision about what deserves the strongest protection.
- **Use Case:** Grant applications, ethics submissions, project kickoff.
- **Expert Variation:**
```
Add the repository-selection matrix: candidate archives for my data type with
their deposit requirements, embargo options, and persistence guarantees.
```

***

## 2. File Organization & Naming Convention

**Prompt:**
```
Design the file organization for my project: [DESCRIBE — data types, team size,
field, any existing habits worth keeping].
1. Directory structure: a tree that separates raw (never modified), processed
   (scripted from raw), analysis, outputs, and documentation.
2. Naming convention: one pattern covering date, content, version, and
   researcher — with the sort order chosen so chronological = alphabetical.
3. The README requirements: what every directory's README must answer.
4. Three worked example filenames showing the convention in action.
5. The migration plan: how to move existing chaos into this structure without
   breaking references in current analyses.
```

- **Purpose:** A structure your future self and collaborators can navigate without you.
- **Why it works:** Raw/processed separation is the single convention that prevents the classic "which version is real" catastrophe.
- **Use Case:** New projects, rescuing existing projects.
- **Expert Variation:**
```
Generate the integrity checker: a script skeleton that flags raw files modified
after their initial creation, and processed files newer than their source
scripts.
```

***

## 3. Provenance & Codebook Documentation

**Prompt:**
```
Create the provenance documentation for my dataset: [DESCRIBE dataset — origin,
collection instrument, cleaning steps, transformations].
1. The provenance chain: source → raw capture → cleaned → analysis-ready, with
   the tool/script and decision made at each arrow.
2. The codebook: for each variable — name, label, type, allowed values or range,
   units, missing-data codes AND their meanings, derivation if computed.
3. The decision log: judgment calls made during cleaning (exclusions, recodes,
   imputations) with the rule applied and the record count affected.
4. The known-issues section: what is wrong with this dataset that a secondary
   user must know — written candidly.
```

- **Purpose:** Documentation that makes reuse possible and audit survivable.
- **Why it works:** The decision log and known-issues sections capture the information that lives in researchers' heads and dies with their involvement.
- **Use Case:** Data publication, multi-study teams, thesis handoffs.
- **Expert Variation:**
```
Add the reuse test: the 5 questions a secondary analyst would ask first —
verify my documentation answers each before archiving.
```

***

## 4. Privacy & De-identification Planning

**Prompt:**
```
My dataset contains: [DESCRIBE — direct identifiers, quasi-identifiers, sample
size, population]. Sharing goal: [open deposit / restricted access / internal only].
1. Direct identifiers: list what must be removed or separated, and the storage
   arrangement for the key linking codes to identities.
2. Quasi-identifiers: assess re-identification risk from combinations
   (rare values, small cells, geography + demographics) — show your reasoning.
3. The de-identification options for my data type: generalization, suppression,
   top/bottom coding — with what each costs in analytical utility.
4. Residual risk statement: what risk remains after my chosen approach, and
   the access controls that compensate.
5. Compliance flags: what my local ethics/privacy regime likely requires —
   marked [VERIFY WITH ETHICS BOARD/IRB], not asserted.
```

- **Purpose:** Sharing data honestly without sharing people.
- **Why it works:** Treats re-identification as a combinatorial problem (which it is) rather than a redaction checklist.
- **Use Case:** Data publication, collaborative analysis, cross-border data sharing.
- **Expert Variation:**
```
Design the k-anonymity check: how to measure whether each record is
indistinguishable from at least k-1 others on the quasi-identifier set I kept.
```

**Limitations & verification:** Privacy law and ethics requirements are jurisdiction- and institution-specific — the model's flags are reminders, not rulings. Final approach requires your IRB/ethics board and, where applicable, institutional counsel.

***

## 5. Archival & Reuse Package

**Prompt:**
```
Assemble the reuse package for my completed study: [DESCRIBE]. The package must
include:
1. Data files: analysis-ready data with codebook, plus the minimum raw extracts
   needed to verify cleaning
2. Code: commented scripts from raw to results, with the environment captured
3. Documentation: README, provenance chain, decision log, known issues
4. The reproduction path: the ordered steps from package to every table and
   figure in my paper
5. License choice: what others may do with it, and why that fits my funder and
   community norms
6. The 30-minute test: what a competent stranger should be able to reproduce
   in half an hour — define and state it in the README.
```

- **Purpose:** The artifact that turns "available on request" into actual availability.
- **Why it works:** The 30-minute test sets a falsifiable standard for the package's quality.
- **Use Case:** Journal data-availability policies, supplementary deposits, thesis archiving.
- **Expert Variation:**
```
Add the citation scaffold: the data citation (with persistent identifier
placeholder), the code citation, and the suggested acknowledgment text for
reuse.
```

**Limitations & verification:** Run the 30-minute test yourself with a colleague before deposit — the gap between "should be reproducible" and "is reproducible" is where packages die.

***

## 6. Data Loss Pre-Mortem

**Prompt:**
```
Run a pre-mortem on my data management: [DESCRIBE storage, backup, access,
team setup]. It is 2 years later and I have lost data. Write the story:
1. The 4 most probable loss scenarios for my setup (hardware, sync conflicts,
   accidental deletion, access/ownership gaps — e.g., a departing student's
   accounts).
2. For each: the early indicator I could watch for, and the protection that
   prevents it.
3. The recovery test: the specific exercise that proves my backups actually
   restore — scheduled, not assumed.
4. The ownership map: who controls each storage location, and what happens to
   each when roles change.
```

- **Purpose:** Experiencing data loss in imagination, where it is free.
- **Why it works:** The departing-team-member scenario and the untested backup are the two most common real endings — both are preventable only if foreseen.
- **Use Case:** Project reviews, thesis supervision, lab onboarding.

***

## Shared Verification Rules for All Data Management Prompts

1. **Institutions override templates.** Ethics boards, funders, and repositories have binding requirements the model does not know — treat its output as a draft for their checklists.
2. **Test restores, not backups.** An untested backup is a hope; schedule the recovery exercise or it does not exist.
3. **Raw is sacred.** Whatever else the workflow touches, raw data is write-once; enforce that structurally (permissions, not discipline).
4. **Privacy decisions are auditable decisions.** Document what was de-identified, how, and who approved — the record is as important as the technique.
