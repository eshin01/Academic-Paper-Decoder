# Scalable and accurate deep learning with electronic health records

- **Authors:** Alvin Rajkomar, Eyal Oren, … Greg S. Corrado, Jeffrey Dean (Google Inc, with UCSF, University of Chicago Medicine, and Stanford collaborators; 35 authors)
- **Venue:** npj Digital Medicine, 2018;1:18 (published May 8, 2018)
- **DOI link:** https://doi.org/10.1038/s41746-018-0029-1
- **PubMed link:** https://pubmed.ncbi.nlm.nih.gov/31304302/ (PMID 31304302)
- **Full-text link:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6550175/ (PubMed Central, open access)
- **Basis:** FULL TEXT — analyzed from the complete open-access article retrieved from PubMed Central (introduction, results, discussion, methods; supplement not retrieved). Identifiers verified against the live PubMed/NLM record; direct URL browsing is blocked in this environment, so links are constructed from that verified record.
- **Decoded:** 2026-09-02

---

# The Gist

Google researchers asked: instead of building a separate, hand-crafted prediction tool for every hospital question — who might die, who might bounce back after discharge, who will stay a long time — what if a computer just read the patient's *entire* medical record, every lab, medication, vital sign, and even the doctors' and nurses' typed notes? Using records from 216,221 hospital stays at two US academic medical centers (about 46 billion pieces of data), their deep-learning models predicted in-hospital death, 30-day readmission, long hospital stays, and discharge diagnoses more accurately than the standard scoring tools hospitals actually use — and without any expert first choosing which variables matter.

# Study Snapshot

- **Study type:** Retrospective prediction-modeling study — models were trained and tested on past hospital records, then compared against traditional risk scores on the same data. No patients were treated differently; low on the evidence ladder for clinical benefit.
- **Data (n):** 216,221 hospitalizations from 114,003 adult patients (staying at least 24 hours) at UCSF (2012–2016) and University of Chicago Medicine (2009–2016); only the Chicago data included free-text notes. Altogether 46,864,534,945 data "tokens."
- **Outcomes predicted:** in-hospital death (occurred in 2.3% of stays), unplanned 30-day readmission (12.9%), stay of 7+ days (23.9%), and each patient's complete set of billing diagnoses (from 14,025 possible codes).
- **Headline numbers:** predicting death at 24 hours after admission, the model's AUROC was 0.95 and 0.93 at the two hospitals versus 0.85 and 0.86 for an augmented early-warning score; readmission 0.77/0.76 vs 0.70/0.68; long stay 0.86/0.85 vs 0.76/0.74. At equal sensitivity, false alarms for mortality alerts were roughly cut in half (work-up-to-detection ratio ~7.4–8.0 vs ~14.3–15.4).
- **Who ran it:** almost all authors were Google employees; academic partners provided data. Funding/conflict statements are not reported in the text retrieved.
- **Reproducibility:** patient data cannot be shared (privacy), and the code depends on Google's internal computing platforms and was not released.

# How Strong Is This Evidence?

**Grade: 3/5 — a rigorous, large-scale proof that "feed in everything" works, but still a retrospective study of predictions, not care.**

The methodology is genuinely careful: two hospitals rather than one, a hidden test set never touched until final evaluation, confidence intervals from 1,000 bootstrap resamples, calibration checks, and comparisons against strengthened versions of the risk scores hospitals really use. The scale (46 billion data points, including messy free-text notes) was unprecedented for general hospital patients. But the design's ceiling is firm: it shows the models *would have* predicted past events well. It cannot show that acting on those predictions helps anyone — the authors say plainly that prospective trials are needed. And it was designed, run, and evaluated by the company whose technology it showcases, on data and code others cannot fully re-examine.

# The Editor's Concerns

- **Prediction is not prevention.** A model that flags a patient likely to die tells you nothing about whether anything can be done, or whether alerts change behavior. No patient outcomes were tested — the authors acknowledge this openly.
- **"Multiple centers" means the recipe worked twice, not that one model traveled.** A separate model was trained for each hospital. The hard problem — training at one site and deploying at another — was explicitly *not* solved here, and the authors say so.
- **The developer graded its own homework, against baselines it implemented itself.** To their credit, they *strengthened* the traditional scores before comparing (e.g., adding 24 lab tests to the early-warning score). But the comparison design, data access, and evaluation all sat with Google.
- **Some wins are modest in absolute terms.** Readmission prediction at AUROC 0.76–0.77 is better than 0.68–0.70 but still leaves many errors — nowhere near the near-certainty the "beats doctors' tools" framing might suggest.
- **Predicting billing codes is partly predicting paperwork.** Discharge "diagnoses" are administrative ICD-9 codes, whose quirks (nearly identical codes with different digits) the authors themselves note inject noise.
- **The notes question stays open.** Only one hospital's data had free-text notes, so the study can't say how much the notes actually contributed — the authors caution against that comparison across hospitals.
- **Not reproducible externally.** No shareable data, no shareable code — reasonable given privacy and infrastructure, but it means trust rests on description, not replication.
- **What this study did well:** hidden held-out test set; bootstrap confidence intervals; calibration reported (and a statistically literate refusal to use the Hosmer–Lemeshow test, which becomes misleading at huge sample sizes); realistic cohort choices (keeping patients other studies exclude, because a live system wouldn't know to exclude them); a clinically meaningful alert-burden metric, not just AUROC; and an attribution case study showing *which* chart elements drove a prediction — an early, influential answer to the "black box" objection.

# Statistics Spotlight

**1. Discrimination (AUROC) vs. calibration — two different kinds of "accurate."**
- *What they are:* Discrimination asks: can the model *rank* a sicker patient above a healthier one? That's AUROC — the probability a randomly chosen patient who died gets a higher risk score than one who survived (0.5 = coin flip, 1.0 = perfect). Calibration asks something different: when the model says "20% risk," do about 20 of 100 such patients actually have the event?
- *How this paper used it:* Mortality AUROC was 0.93–0.95 (excellent ranking), readmission 0.75–0.77 (decent but imperfect ranking). The authors also plotted predicted-versus-actual probability curves to check calibration — and deliberately skipped the classic Hosmer–Lemeshow calibration test because with 200,000+ records it flags trivial, meaningless discrepancies as "significant."
- *The theory, with an analogy:* A weather forecaster has good discrimination if rainy days consistently got higher rain forecasts than sunny days — even if she always forecasts too high. She's well calibrated if it rains on about 70% of her "70%" days. You want both: a mis-calibrated but discriminating model ranks patients well but lies about absolute risk, which matters when a number like "20% chance of death" is shown to a family.
- *Watch out:* Papers love AUROC because it photographs well; calibration is reported far less often. When you see only an AUROC, you know the model ranks — you don't know its probabilities mean anything. Also note the Hosmer–Lemeshow lesson in reverse: with huge samples, *any* statistical significance test becomes hair-trigger; "statistically significant" stops meaning "practically important."

**2. Work-up-to-detection ratio (number needed to evaluate) — the statistic that measures alert fatigue.**
- *What it is:* Of the patients an alert flags, how many must clinicians investigate to find one true case? It converts abstract accuracy into staff workload.
- *How this paper used it:* At a fixed 80% sensitivity for catching deaths, the deep-learning model's ratio was about 7.4–8.0 patients evaluated per true case, versus 14.3–15.4 for the traditional score — half the false alarms for the same catch rate.
- *The theory, with a worked example:* Suppose 100 patients will die and your alert catches 80 of them (80% sensitivity). If it also flags 1,060 survivors, clinicians chase 1,140 alerts to find 80 real cases — about 14 work-ups per catch. Cut the false flags to 512 and it's about 7.4 per catch. Same sensitivity, half the wasted effort — and wasted effort is why real alert systems get ignored (the "cry wolf" effect hospitals call alert fatigue).
- *Watch out:* This ratio depends on how common the outcome is. A tool with a great ratio in a high-risk ICU can have a terrible one on a general ward where the event is rare. Ask "per how many patients, with what event rate?" before being impressed.

**3. Train/validation/test splits and the bootstrap — how honest accuracy numbers are made.**
- *What it is:* The data was split 80/10/10: 80% to teach the model, 10% to tune it, and a final 10% kept locked away ("hidden") until the very end, used exactly once to report results. Uncertainty came from the bootstrap: resampling the test set 1,000 times and recomputing accuracy to get a 95% confidence interval.
- *How this paper used it:* Every headline AUROC comes from that untouched test set, with bootstrap intervals like 0.95 (0.94–0.96).
- *The theory, with an analogy:* A model tested on data it trained on is a student grading their own memorized homework. The hidden test set is a sealed final exam. The bootstrap answers a second question — "would the score wobble with a different batch of similar patients?" — by shuffling-with-replacement the exam takers 1,000 times and seeing how much the grade moves.
- *Watch out:* A hidden test set from the *same* hospital and years still shares the site's habits, coding quirks, and patient mix. Honest internal testing (this paper) is necessary but not sufficient; the true exam is a different hospital, later years — external validation, which remained future work here.

# Jargon Translator

- **Electronic health record (EHR):** the hospital's complete digital chart — orders, labs, vitals, medications, notes.
- **FHIR (Fast Healthcare Interoperability Resources):** a standard container format for exchanging health data between different hospitals' systems; the paper's key plumbing trick.
- **Token:** one discrete piece of data fed to the model — a lab value, a medication name, a single word from a note.
- **Recurrent neural network / LSTM:** a deep-learning architecture that reads data as an ordered sequence, suited to events unfolding over time.
- **Attention-based model (TANN):** an architecture that learns which pieces of the record to weight most for a prediction — the mechanism behind the paper's "what did the model look at" case study.
- **Ensembling:** averaging several different models' predictions, usually beating any single one.
- **Early-warning score (NEWS/aEWS):** simple point-based tools hospitals use to flag deteriorating patients from a handful of vital signs and labs.
- **ICD-9 codes:** the standardized billing-diagnosis catalog (~14,025 codes here) hospitals attach to each stay.
- **Attribution / saliency:** techniques that highlight which inputs most influenced a specific prediction.

# What You Can (and Can't) Say

**Fair to say:**
- "In 2018, Google showed that deep learning reading a patient's entire raw record — notes included — predicted death, readmission, and long stays more accurately than the standard hospital risk scores, across two academic medical centers."
- "It halved the false-alarm burden of mortality alerts at the same catch rate in retrospective testing."
- "Its key innovation was scalability: one data pipeline for many prediction tasks, with no expert selecting variables."

**Not fair to say:**
- "Google's AI knows when you'll die" — it ranked risk well in past data; a 0.95 AUROC is not prophecy, and no live deployment was tested.
- "This proved AI improves hospital care" — no care was changed and no outcomes were measured; the authors call for prospective trials.
- "The model works at any hospital" — each hospital got its own separately trained model; cross-site transfer was explicitly unsolved.
- "It replaces doctors' judgment" — it predicts events and billing codes, which is a narrow slice of clinical reasoning.

# Bottom Line for Your Life

This paper marks the moment "just feed the whole chart to the AI" became credible — and its playbook (standardize the plumbing, let the model find what matters, show your work with attention highlights) shaped nearly every hospital-AI system that followed, including today's medical language models. For you as a reader of health headlines, its lasting lessons are the questions it teaches: does the model just *rank* well, or are its probabilities *honest* (calibration)? How many false alarms per true catch? And was it tested anywhere other than where it was built? One study is one data point — a foundational one — and it measured predictions, not lives saved. This is an educational breakdown, not medical advice.

---

**Sources** (based on articles retrieved from PubMed / PubMed Central; identifiers verified against the live NLM record — URL browsing is blocked in this environment, so links are constructed from that verified record):
- DOI: https://doi.org/10.1038/s41746-018-0029-1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/31304302/
- Full text (PMC, open access): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6550175/
