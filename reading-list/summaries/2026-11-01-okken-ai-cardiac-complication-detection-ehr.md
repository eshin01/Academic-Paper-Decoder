# Development of an artificial intelligence algorithm for automated detection of cardiovascular intervention-related complications

**Authors:** Okken A, Wanders R, Klappe A, Beukema KF, Oirbans T, Noordzij PG, van Lent A, Haanemaaier SH, Balt JC (nine authors — Departments of Cardiology and of Anaesthesiology and Intensive Care Medicine, St. Antonius Hospital, Nieuwegein, The Netherlands; **two authors are at Parnas, IT-Services and Consultancy, Groningen**, a commercial IT consultancy, disclosed on the author line)
**Journal:** Netherlands Heart Journal, 2026; 34(11): 407–413 (published 21 October 2026)
**Decoded:** 2026-11-01
**Analysis basis:** **FULL TEXT** (retrieved from PubMed Central, PMC13694613). The complete body was read — introduction, methods including the ten-step development process, statistical analysis, results, discussion, limitations, implementation and cost discussion, conclusion and the journal's "What's new?" box. **The two supplementary tables are not retrievable**, and they matter here: Table S1 holds the initial case-identification results on the training data and Table S2 the per-complication model performance. The main text reports only **ranges** across the four complications. Two of the four models are nonetheless fully reconstructable from sentences in the Discussion, and Section 5 does that.

**Source links (verified):**
- DOI: https://doi.org/10.1007/s12471-026-02082-2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42905390/
- Full text (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC13694613/

**Basis of link verification.** Direct URL fetching is blocked from this session (`doi.org` does not resolve under the network policy here). Verification was done against the live PubMed/NLM record: a query for PMID 42905390 returned this exact title, these nine authors, Netherlands Heart Journal volume 34 issue 11 pages 407–413, DOI `10.1007/s12471-026-02082-2` and PMC ID `PMC13694613`; the full text was then retrieved from PubMed Central by that PMC ID and matches. Both halves of the chain were confirmed independently.

**Funding: not reported in the text retrieved. Competing interests: no statement in the text retrieved** — notable because two of the nine authors work for a commercial IT consultancy that evidently helped build the tool, which is disclosed on the author line but not in a declaration. **Reporting: the paper states that "Model development and validation were reported in accordance with the PROBAST-AI guidelines"** — see Section 4; PROBAST+AI is an appraisal instrument rather than a reporting guideline.

**Ethics:** approval from the hospital's medical ethical committee is stated; data were anonymised before extraction and all analysis ran on a compute cluster inside the hospital.

> **Why this paper today.** All four deferred papers were re-checked and remain blocked; the JAMA OpenEvidence study (PMID 42879271, PMC13673371) reached **day 17** of serving an empty PMC body. This was spare #4, flagged a week ago for one number: **positive predictive value of 47.5% alongside specificity of 99.4%.** In every previous paper in this list, a PPV that low at a specificity that high has been a fatal problem. Here it is the design working as intended — and understanding why is the cleanest lesson about base rates this list has had. It is also the **first audit-and-registration tool** decoded here rather than a prediction model, the first paper to report **what it cost**, and one of only a handful with a **properly blinded reference standard**.

---

## 1. The Gist

Every heart procedure carries a risk of something going wrong — a stroke, bleeding, fluid squeezing the heart, a paralysed breathing nerve. Hospitals are supposed to count these. Counting them is how you notice you have a problem and fix it.

They do not get counted. At this Dutch hospital, complications were logged correctly in the designated part of the patient record **no more than 50% of the time at best**. So data managers spend about **100 hours a year** reading patient files by hand to find the ones that were missed.

Nine authors at St. Antonius Hospital built software to do that reading. They took **every one of the 6,564** pulmonary vein isolations, coronary angioplasties and aortic valve implantations performed between 2017 and 2022 — no exclusions — and trained a system on the first portion to find four specific complications in the records of the later portion. It reads both the tidy stuff (lab results, medications, procedure logs) and the messy stuff (clinical notes, discharge letters).

**They deliberately tuned it to miss nothing, accepting that it would raise false alarms.** It worked. For stroke, tamponade and phrenic nerve palsy it found **100%** of cases; for bleeding **94.4%**, missing 2 of 36.

And the number that looks alarming: **positive predictive value of 47.5%** for stroke. Of the records it flagged, fewer than half had a real stroke.

**For this job, that is excellent, and the paper's own sentence shows why.** Out of 3,565 patients, the stroke model hands a data manager a shortlist of **40 records**, and all **19** real strokes are in it. The person reads 40 files instead of 3,565. Twenty-one wasted reads is a rounding error against the time saved.

Across all four complications: **127 records reviewed instead of over 6,500, to find all 79 complications.** The system cost **€20,000–30,000** to build and **€10,000 a year** to run, and it is in use today.

The same arithmetic that destroys a screening test here makes a filing clerk twenty-eight times faster. **Whether a low PPV is a disaster or a feature depends entirely on what happens to a false positive** — and in this paper, nothing happens to it except that somebody reads a file.

## 2. Study Snapshot

**Study type:** development and internal temporal validation of an **automated case-finding (audit) tool**. This is important and different from everything else in this list: the tool is not predicting anything. The complication has already happened and is already described somewhere in the record. The task is *retrieval*, not prognosis.

**Where and when:** St. Antonius Hospital, Nieuwegein, Netherlands. All PVI, PTCA and TAVI procedures 2017–2022.

**Who:** **6,564 patients**, with "no additional inclusion or exclusion criteria beyond data availability" — a choice the authors state was made "to reflect routine clinical practice and to ensure representativeness of the target population."

**Split:** a training and test set of **2,999** and a **prospective validation set of 3,565**. 2,999 + 3,565 = 6,564, which reconciles. The word "prospective" describes a forward-in-time split of retrospectively extracted records rather than prospective data collection — but a temporal split is the right design, and better than the random splits several papers in this list used.

**What it looks for:** four complications defined by the **Dutch Heart Registration (NHR)** — bleeding, cardiac tamponade, CVA (stroke) and phrenic nerve palsy. The bleeding definition was widened to cover clinically relevant events: bleeding that prolonged the hospital stay, required surgery, or required transfusion.

**What it reads:** registered diagnoses, procedure logs, medication, laboratory measurements, clinical notes and discharge letters — from the index admission and **up to 30 days after discharge, including readmissions and interdepartmental transfers**. Data were standardised to the **OMOP Common Data Model** and **ZIB**, a Dutch information standard mandatory in all hospitals, with portability to other hospitals as the stated reason.

**The explicit design objective:** "The primary objective was to achieve 100% sensitivity to avoid missing any complication, accepting a lower specificity and—consequently—false positives." Stated up front, which matters for how every number below should be read.

**How the reference standard was built — and this is the strongest part of the paper.** Clinical presentations of each complication were worked out in workshops with clinicians and translated into data statements, which flagged candidate records. Those records were then reviewed by hand, **independently by two authors with consensus adjudication by a third for ambiguous cases**, and — stated explicitly — **"No model predictions or outputs were available to the reviewers during the labeling process."** The reviewers were blinded. Two papers decoded in the past week had unblinded reference standards; this one does it right. Additionally: "A random sample of non-selected files, as well as a cross-check with existing registry data, did not identify additional complication cases" — an attempt to check whether the flagging step itself had missed anything.

**The step worth copying.** Step 3 of the ten-step process assessed "whether the identified patterns were clinically plausible, removing spurious signals from the model." The worked example given: the model found **administration of fluoroscopic contrast** to be predictive of stroke, and the team removed it, because contrast is given for the CT scan that **diagnoses** the stroke. A variable caused by the diagnosis was found masquerading as a predictor of it, and deliberately deleted.

**Models:** random forest and boosting classifiers for the structured data; **transformer embeddings** for the free text (Sentence-Transformers, `all-MiniLM-L6-v2`); hyperparameter optimisation with **Optuna**, "exclusively on the training dataset," optimising F-score to favour sensitivity. The three streams — structured model, unstructured model, and the criteria-based approach — were combined into a final ensemble by **logistic regression trained with five-fold cross-validation**. Missing values were left to the models rather than imputed, and no records were dropped. Analyses in Python, scikit-learn 1.2.2.

**Headline results (ranges across the four complications):** sensitivity **94.4–100%**, specificity **99.4–100%**, PPV **47.5–81%**, F-score **0.64–0.87**.

**Reconstructed in Section 5, because the per-complication table is not retrievable:**
- **Stroke (CVA): TP 19, FN 0, FP 21, TN 3,525.** Prevalence 0.533%. Sensitivity 100%, specificity 99.41%, PPV 47.5%, F-score 0.644. **Every low end of all four reported ranges is this model.**
- **Bleeding: TP 34, FN 2, FP 8, TN 3,521.** Prevalence 1.01%. Sensitivity 94.44%, PPV 80.95%, F-score 0.872. **The high ends of the PPV and F-score ranges are this model.**

**Overall yield:** **79 complications** in the validation set — which is the 2.2% incidence the paper quotes (79/3,565 = 2.22%, not 79/6,564) — found by reviewing **127 records**. That is an aggregate PPV of 62.2% and a **28-fold reduction** in records a human must read.

**Costs, which nothing else in this reading list reports:** approximately **€20,000–30,000** to implement, **€10,000 per year** recurring. Existing manual review consumes about **100 hours a year**. The tool is currently in use at the hospital.

**One of the four is not a model.** For phrenic nerve palsy "due to the limited number of patients with this complication, it was not feasible to develop a meaningful AI model for it. This model used selected criteria only" — a hand-written rule. The paper reports only **2 cases** of it.

## 3. How Strong Is This Evidence? (Grade 3/5)

**A note on grading, because this is a different kind of paper.** The last twelve entries were prediction models, and the yardstick has been: does the claim about future patients survive contact with new data? This paper makes a narrower, more checkable claim — *this software finds the complications in our records, and it saves our data managers most of their reading* — and that claim is supported by the evidence presented. The limits are about **transportability**, not internal validity.

**What this paper does well, and several items are firsts for this list:**

**A blinded reference standard.** Two independent reviewers, third-party adjudication, and an explicit statement that no model output was visible during labelling. The PECARN paper (entry 61) had to list unblinding as its first limitation; this paper simply did it properly.

**A check on the reference standard's own completeness.** They sampled records the flagging step had *not* selected, and cross-checked against the existing registry. That is asking the right question — "did our screen miss cases?" — and almost nobody asks it.

**A leakage proxy found and deliberately removed, with the reason stated.** The fluoroscopic-contrast example is the clearest instance of this in sixty-four papers. The variable was genuinely predictive and genuinely useless, because it was a downstream consequence of making the diagnosis. Removing it cost accuracy and bought validity.

**A genuine temporal split**, develop on the earlier 2,999, validate on the later 3,565.

**Every consecutive procedure, no exclusions**, with the reason stated.

**The design objective declared in advance.** "The primary objective was to achieve 100% sensitivity… accepting a lower specificity and—consequently—false positives." When a paper tells you what it optimised for before showing you the numbers, the numbers become interpretable.

**Outcome definitions taken from a national registry** rather than invented, with the one extension (clinically relevant bleeding) specified.

**Tuning confined to the training set**, with the ensemble combiner cross-validated.

**Data standardised to OMOP and ZIB with portability as the explicit rationale** — a design decision aimed at the problem most papers in this list ignore entirely.

**Costs and workload reported.** €20,000–30,000 setup, €10,000/year, against 100 hours a year of existing manual review, and 127 records to read instead of 6,500+. **This is the first paper in sixty-four to say what its tool costs.** It changes the discussion from "does it work" to "is it worth it," which is the question a hospital actually asks.

**Honest about its weakest component.** The paper states plainly that phrenic nerve palsy could not support a model and was handled with criteria only.

**Honest about the bleeding misses and why.** Two of 36 missed, with the reason given — bleeding is a continuum from a small bruise to a life-threatening haemorrhage, and any threshold trades misses against false alarms.

**Why it is not a 4:**

**No external validation, and it is not listed as a limitation.** One hospital, one EHR vendor, one country's registry definitions — for a tool that is already deployed. The OMOP/ZIB standardisation is a thoughtful preparation for portability but is not a test of it. The limitations section covers the bleeding threshold, the small case counts and the per-complication development effort, and never raises another hospital.

**The completeness check is unquantified, and at this prevalence that matters a great deal.** Stroke occurs in 0.533% of these patients. Sampling 100 non-selected records and finding nothing has a **58.6% chance** of happening even if the flagging step were missing cases at the full base rate. You need about **300 records** for an 80% chance of turning up a single missed case. The sample size is not stated, so the ceiling on the whole system's sensitivity is not actually bounded.

**A structural circularity the paper does not name.** The pattern statements did two jobs: they selected the candidate pool from which the gold standard was built, *and* they are one of the three inputs to the final ensemble. A complication documented in a way no statement caught is therefore both absent from the labels and invisible to a third of the model — so it can never appear as a false negative.

**A component that is not a model is reported inside the model's performance range.** Phrenic nerve palsy, 2 cases, criteria only — yet its sensitivity and specificity sit inside the abstract's "94.4–100%" and "99.4–100%". A sensitivity of 100% on 2 cases has an exact confidence interval of **15.8% to 100%**.

**The wrong reporting instrument is named.** See Section 4.

**No competing-interests statement**, with two authors at a commercial IT consultancy.

**What would make it a 4:** state the size of the non-selected random sample; run the tool at a second hospital, which is what the OMOP standardisation was built for; and report the per-complication confusion matrices in the main text rather than ranges.

## 4. The Editor's Concerns

**The paper names PROBAST-AI as its reporting guideline, and PROBAST+AI is not one.** PROBAST, and its AI extension, is a **risk-of-bias appraisal tool** — an instrument readers, reviewers and systematic reviewers use to judge a prediction-model study. The matching **reporting** guideline for authors is TRIPOD, and TRIPOD+AI for machine-learning studies. Saying "model development and validation were reported in accordance with the PROBAST-AI guidelines" uses the appraisal checklist as though it were a reporting checklist. Self-appraising against PROBAST+AI is a perfectly sensible thing to do and naming something beats naming nothing — two of the last five papers named nothing — but PROBAST+AI does not ask for the items TRIPOD+AI asks for, and several of those items (per-outcome performance tables, calibration, a complete participant flow) are the ones this paper is thin on.

**Only ranges are reported in the main text.** Four complications, four metrics, and the reader gets "94.4–100%", "99.4–100%", "47.5–81%", "0.64–0.87". Which complication sits where is in a supplementary table. As Section 5 shows, two of the four can be recovered exactly from narrative sentences — but a reader should not have to, and the other two cannot be.

**"Near 100% sensitivity and specificity" in the journal's What's new box omits the number that governs the value.** The box says the tool works "with near 100% sensitivity and specificity." Both true. But the entire proposition — read 127 files instead of 6,500 — is a statement about **positive predictive value**, and PPV appears nowhere in the box. A reader of the highlights learns the two most flattering metrics and not the operationally decisive one.

**The 2.2% incidence and the 79 complications describe the validation set, which the text does not say.** 79 of 6,564 is 1.20%; 79 of 3,565 is 2.22%. The quoted 2.2% therefore belongs to the validation half, and so does the 79. The main text presents both figures without naming the denominator, and a reader would reasonably attach them to the full 6,564.

**Calibration is never mentioned, which here is defensible but should be said.** The ensemble combines three probability streams with logistic regression, so it produces probabilities — but it is used as a binary triage filter, so whether a predicted 30% means 30% is largely irrelevant. That is a reasonable position. It is also the first paper in this list where skipping calibration is the right call rather than an omission, and a sentence saying so would have been worth more than the calibration curve.

**The "prospective validation set" is a temporal split.** All 6,564 records come from 2017–2022 and were extracted retrospectively; the 3,565 are the later portion. A temporal split is genuinely better than a random one — the UTI paper (entry 59) had three calendar years and chose random, which cost it a grade — so the design deserves the credit. The word does not.

**Where I am uncertain, stated plainly.** Tables S1 and S2 are not retrievable, so I cannot report the per-complication metrics for tamponade or phrenic nerve palsy, nor the initial case-identification yield on the training data. The two confusion matrices in Section 5 are **reconstructed, not printed** — each from a narrative sentence plus one reported figure, with three independent cross-checks apiece, but reconstructed. Subtracting the reconstructed stroke and bleeding cases (19 + 36 = 55) from the 79 total leaves 24 for tamponade and phrenic nerve palsy combined, and subtracting their shortlists (40 + 42 = 82) from 127 leaves 45 records; I have not attempted to split those further. No funding or competing-interests statement appears in the retrieved text.

## 5. Statistics Spotlight

Three things. The first is the base-rate problem running in the opposite direction to every previous appearance of it in this list.

### A low positive predictive value is a catastrophe for a test and a feature for a filter

This list has flagged low PPV as a serious problem several times. Here it is the intended outcome, and the difference is entirely about what happens next to a false positive.

Start from the paper's own sentence, which is the clearest single statement of the base-rate problem anywhere in this reading list:

> "for a complication such as CVA, scrutinizing thousands of patient records, the algorithm will produce a shortlist of 40 records for manual review. This shortlist contained all 19 CVA cases, resulting in no missed event."

Work it out. There are 3,565 patients in the validation set and 19 had a stroke — a prevalence of **0.533%**. The tool flagged 40. All 19 real cases are among them, so **21 of the 40 flags are false**. PPV = 19/40 = **47.5%**, exactly the low end of the reported range.

Now, why is the PPV so low when the specificity is so high? Because there are so many more well patients than sick ones. Specificity is 99.41%, meaning the tool wrongly flags **0.59%** of the 3,546 patients without a stroke:

> 0.0059 × 3,546 ≈ **21 false positives**

And 21 is the same order of magnitude as 19. **At a prevalence below 1%, even a 99.4% specific tool produces roughly one false alarm per real case.** That is not a flaw in the tool; it is arithmetic.

**Here is how expensive it would be to fix.** Holding sensitivity at 100% and prevalence at 0.533%:

- specificity 99.0% → PPV **34.9%** (about 35 false alarms)
- specificity 99.4% → PPV **47.2%** (about 21 false alarms) ← where the tool actually is
- specificity 99.9% → PPV **84.3%** (about 3.5 false alarms)
- specificity 99.94% → PPV **89.9%** (about 2 false alarms)

To move PPV from 47.5% to 90% you must push specificity from **99.41% to 99.94%** — cutting false positives by a factor of ten. That is an enormous amount of additional engineering, and here it would buy almost nothing, because the cost of a false positive is **one person opening one file.**

**Contrast two uses of the identical numbers.** Imagine a test with these exact operating characteristics told a patient they had probably had a stroke. Fewer than half of those told would have had one; the other half would get imaging, anxiety, possibly treatment. Unusable. Now imagine it hands a data manager a list of 40 files out of 3,565. **The 21 false positives cost 21 file-reads.** Same statistics, opposite verdict.

**The general rule, and it is the most useful thing in this paper:** PPV only matters in proportion to what a false positive triggers. **Ask what happens to a false positive before deciding whether a PPV is acceptable.** If the answer is "a treatment," "a scan," or "a phone call to a patient," demand a high PPV. If the answer is "a human looks at the record," a PPV of 50% at a twenty-eight-fold workload reduction is a very good trade. The matching question for sensitivity is the same in reverse: here a false *negative* means a complication goes unregistered forever, which is why the authors pinned sensitivity at 100% and let PPV fall where it fell.

### Reconstructing a confusion matrix from a sentence rather than from percentages

Three times in the past week this list has recovered a 2×2 table from published percentages. This paper needs a different move, because the main text gives only ranges across four complications — so the percentages alone are not attributable to any one model.

The way in is the narrative. From "a shortlist of 40 records" and "contained all 19 CVA cases," with a validation set of 3,565:

> **TP = 19 · FN = 0 · FP = 21 · TN = 3,525**

Then check it against every reported figure: sensitivity 19/19 = **1.000** (matches the 100% top of the range); specificity 3,525/3,546 = **0.9941** (matches the 99.4% bottom); PPV 19/40 = **0.4750** (matches 47.5% exactly); F-score 38/59 = **0.644** (matches 0.64). **Four independent confirmations.** And the useful consequence: **every low end of every reported range is the stroke model**, which the paper never says.

The bleeding model yields to the same approach from a different sentence — "an F‑score of 0.87, albeit with two false negative cases out of 36 total cases":

> TP = 34, FN = 2. Solve F = 2TP/(2TP + FP + FN) = 0.87 for FP → **FP = 8**, TN = 3,521.

Check: sensitivity 34/36 = **0.9444** (matches 94.4%); PPV 34/42 = **0.8095** (matches the 81% high end); F-score 68/78 = **0.8718** (matches 0.87). Three confirmations.

**So the paper's four ranges turn out to be bounded at the bottom by stroke and at the top by bleeding**, and two of the four models are now fully specified — from prose, with no access to the supplementary table.

**The technique: when a paper reports ranges instead of per-group results, mine the Discussion for a worked example.** Authors routinely illustrate their tool with one concrete case ("40 records, 19 cases," "two misses out of 36"), and a concrete case plus one reported metric is usually enough to pin the whole table. Then verify against every other number in the paper. If three or four independent checks land, the reconstruction is right.

### Why a negative random-sample check needs a stated sample size

The reference standard here was built from records the pattern statements flagged. That raises an obvious worry: if a complication was documented in some way the statements did not anticipate, it never entered the gold standard — so the model cannot be penalised for missing it, and "100% sensitivity" means 100% of what the screen found.

To their credit the authors saw this and checked: "A random sample of non-selected files, as well as a cross-check with existing registry data, did not identify additional complication cases."

That is exactly the right check. But a negative result from it only means something if the sample was big enough to have found something. **Stroke occurs in 0.533% of these patients.** If you draw *n* non-selected records at random and the missed-case rate is the full base rate, the chance of finding **zero** cases anyway is 0.99467ⁿ:

- n = 50 → **76.6%** chance of finding nothing even so
- n = 100 → **58.6%**
- n = 200 → **34.3%**
- n = 320 → **18.1%**
- n = 1,000 → **0.5%**

So sampling 100 records and finding nothing is close to uninformative: it would have happened more often than not regardless. **You need about 300 records for an 80% chance of turning up a single missed case.** The paper does not state the size of its sample.

**The everyday version.** Suppose one jellybean in 200 in a jar is black, and you want to check whether there are any black ones at all. Pull out ten and see none: that tells you almost nothing — you would expect to see none. Pull out six hundred and see none and you have genuinely learned something. **The informativeness of a negative check is entirely about how many chances you gave it.**

**The watch-out, which generalises well beyond this paper:** whenever a study reports that it "checked for missed cases and found none," "reviewed a random sample and found no errors," or "audited a subset with no discrepancies," **find the size of that subset and compute the probability of a null result arising anyway.** Rare outcomes make reassuring negative audits very cheap to obtain by accident. Here it is the one gap between a genuinely careful piece of work and an airtight one.

## 6. Jargon Translator

**Complication** — "an unwanted and potentially harmful outcome of a medical treatment or procedure," in the paper's own words.

**PVI (pulmonary vein isolation)** — a catheter procedure that burns or freezes small areas inside the heart to treat atrial fibrillation.

**PTCA / PCI (percutaneous transluminal coronary angioplasty)** — opening a narrowed heart artery with a balloon, usually leaving a stent.

**TAVI (transcatheter aortic valve implantation)** — replacing a heart valve through a catheter rather than open surgery.

**Cardiac tamponade** — blood or fluid building up around the heart and squeezing it so it cannot fill properly. An emergency.

**CVA (cerebrovascular accident)** — a stroke.

**Phrenic nerve palsy** — damage to the nerve that drives the diaphragm, a known risk of freezing procedures near the right pulmonary veins. Only 2 cases here.

**Under-registration** — complications happening but never being recorded. At this hospital, logging in the designated field was "no higher than 50% accurate at best."

**PDCA cycle (Plan-Do-Check-Act)** — the standard quality-improvement loop. It cannot work if the "Check" step has no data, which is the whole motivation for this paper.

**NHR (Dutch Heart Registration)** — the national registry whose complication definitions this tool uses.

**Structured vs unstructured data** — tick-boxes, codes, lab values and timestamps versus the free text a clinician types. Most of what matters clinically lives in the free text, which is why it is hard to count.

**EPRS / EHR** — the electronic patient record system. Here, Epic.

**OMOP Common Data Model** — an international standard for reshaping hospital data into common tables, so that software written at one hospital can run at another.

**ZIB** — a Dutch information standard, mandatory for all hospitals.

**Weakly supervised** — training on labels generated by rules rather than by exhaustive expert review. Cheaper, and its weakness is that the rules bound what can be labelled at all.

**Gold standard / reference standard** — the answer treated as correct for scoring. Here, human review of flagged records, with the reviewers blinded to the model.

**Transformer embedding** — turning a block of text into a list of numbers that captures its meaning, so a model can compute with it. Here the `all-MiniLM-L6-v2` model via Sentence-Transformers.

**Random forest / boosting** — two families of decision-tree model. Forests average many trees grown in parallel; boosting builds them in sequence, each correcting the last.

**Ensemble** — combining several models' outputs into one. Here three streams joined by logistic regression.

**Optuna** — a library for automatically searching hyperparameter settings.

**Sensitivity** — of the complications that really happened, the share the tool found.
**Specificity** — of the patients with no complication, the share the tool correctly left alone.
**Positive predictive value (PPV) / precision** — of the records the tool flagged, the share that had a real complication. **Depends on how common the thing is.** See Section 5.

**F-score** — the harmonic mean of PPV and sensitivity, as a single balance number. Falls when you buy sensitivity with false positives, which is why this paper's F-scores (0.64–0.87) look modest by design.

**Base rate / prevalence** — how common the thing is. The quantity that makes PPV collapse when it is small, no matter how specific the test.

**PROBAST / PROBAST+AI** — a tool for *appraising* the risk of bias in a prediction-model study. Not a reporting guideline; TRIPOD and TRIPOD+AI are. See Section 4.

## 7. What You Can (and Can't) Say

**Fair to say:**

- ✅ "At one Dutch hospital, complications were correctly logged in the designated record field no more than 50% of the time." The paper's own statement about its institution.
- ✅ "A tool reading both structured data and clinical free text found all 19 strokes in 3,565 patients by flagging 40 records." Directly stated, and the arithmetic reconstructs.
- ✅ "It found 100% of strokes, tamponades and phrenic nerve palsies, and 94.4% of bleeds, missing 2 of 36." Stated.
- ✅ "To find all 79 complications a human read 127 records instead of over 6,500." Stated; a 28-fold reduction against the validation set.
- ✅ "It cost about €20,000–30,000 to build and €10,000 a year to run, and it is in use." Stated — and the only cost figure in this reading list.
- ✅ "The team found that contrast administration predicted stroke and deliberately removed it, because contrast is given for the scan that diagnoses the stroke." Stated, and an exemplary bit of practice.
- ✅ "The reviewers who built the reference standard could not see the model's output." Stated explicitly.
- ✅ "The complication rate in the validation set was 2.2%." 79 of 3,565.

**Not fair to say:**

- ❌ "The AI predicts complications." It does not predict anything. The complication has already happened and is already written in the record; the tool is finding it. The paper is clear that prediction "remains beyond the scope of the current project."
- ❌ "A positive predictive value of 47.5% means the tool is unreliable." For a tool whose false positives cost one file-read each, it is a good trade. The same PPV in a patient-facing test would be unusable. **What a false positive triggers decides whether the number is acceptable.**
- ❌ "Specificity above 99% means few false positives." At a 0.533% prevalence, 99.41% specificity still produces about **21 false alarms for 19 real cases**.
- ❌ "All four complications were detected by AI models." Phrenic nerve palsy had 2 cases and the paper states a meaningful model was "not feasible"; it used "selected criteria only." Its metrics nonetheless sit inside the abstract's ranges.
- ❌ "Sensitivity was 100% for phrenic nerve palsy, so that model is reliable." That is 2 out of 2, exact 95% confidence interval **15.8% to 100%**.
- ❌ "The gold standard was complete, because a random sample found no missed cases." The sample size is not reported, and at this prevalence a sample of 100 would have found nothing more than half the time anyway.
- ❌ "It was validated prospectively." The "prospective validation set" is the later portion of a retrospectively extracted 2017–2022 dataset — a temporal split, which is good, but not prospective collection.
- ❌ "This will work at other hospitals." Single hospital, single EHR vendor, Dutch registry definitions. The OMOP and ZIB standardisation was chosen to make portability possible; it has not been tested, and external validation is not among the stated limitations.
- ❌ "The tool saves 100 hours a year." 100 hours is what the *current manual* process costs. The paper reports the reduction in records to review, not the post-implementation time, so the hours saved are implied rather than measured.
- ❌ "Reported according to AI reporting standards." The paper names PROBAST-AI, which is an appraisal instrument. TRIPOD+AI is the reporting guideline.

## 8. Bottom Line for Your Life

If you are about to have a heart procedure and someone quotes you a complication rate, this paper is a reason to take that number seriously — and also a reason to know where it comes from. **Hospitals routinely fail to record their own complications.** At this one, the designated field in the patient record was right less than half the time, and finding the rest took a hundred hours a year of someone reading files. That is not negligence; it is what happens when recording a bad outcome is an unpaid extra task at the end of a long day. The rates in consent conversations and national registries rest on this plumbing, and the plumbing leaks.

Which makes this an unglamorous but genuinely good use of the technology: software that reads the notes and hands a human a shortlist. Nobody's diagnosis is being made by a machine. The machine is doing the filing.

For anyone appraising research, this paper teaches the most practically useful thing in the list so far.

**A positive predictive value cannot be judged without knowing what a false positive does.** This tool's PPV for stroke is **47.5%** — of the records it flags, fewer than half contain a real stroke. In a patient-facing test that would be a scandal. Here a false positive means **one person opens one file**, and the tool cuts the reading from 3,565 records to 40 while missing nothing. **Same arithmetic, opposite verdict.** And the arithmetic is worth internalising for its own sake: at a prevalence of 0.5%, even 99.4% specificity yields about one false alarm per real case, and dragging PPV up to 90% would require pushing specificity to **99.94%** — a tenfold cut in false positives, to save about nineteen file-reads. Nobody should spend that engineering. **Before you accept or reject a PPV, ask what happens next.**

And one habit from the same paper, which is the gap between careful work and airtight work: **when a study says it "checked a random sample and found no problems," find the sample size and do the arithmetic.** At a 0.5% base rate, checking 100 records and finding nothing would have happened **59% of the time** even if cases were being missed at the full rate. Reassuring negative audits of rare things are very easy to obtain by accident. **A negative result is only as informative as the number of chances you gave it.**

---

## Appendix — deferred-paper status, 2026-11-01

- **Google, "The anatomy of a personal health agent"** (Nature, PMID 42907512): no PubMed Central copy. Unchanged.
- **BMJ, LLM-trial reporting completeness review** (PMID 42869550): no PMC copy; Scite paywalled. Unchanged.
- **Annals of Internal Medicine, Choosing Wisely benchmark** (PMID 42896192): no PMC copy. Unchanged. Standing note: the overuse rate of 5.4% with a 95% CI of 0.6–12.2% is a clustering signature — that interval is almost certainly computed across the 15 recommendations rather than the 4,050 responses.
- **JAMA, "Clinician Use of an AI-Enabled Clinical Information Platform"** (PMID 42879271, PMC13673371): PMC record exists and serves an **empty body for the seventeenth consecutive day.** Standing instruction unchanged — **if still empty on 2026-11-05 (day 21), decode abstract-only and say so explicitly.**

---

*This is an educational analysis of a published scientific paper, not medical advice. Nothing here is guidance about heart procedures or their risks. If you are facing a cardiac intervention, discuss its specific risks with your cardiologist.*
