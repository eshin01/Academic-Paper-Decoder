# Machine Learning Estimation of Gestational Age at Delivery Using Linked Mother–Infant Electronic Health Records Across Two Health Systems

**Authors:** Bejan CA, Yang X, Pham A, Qassem L, Abraham A, Choi L, Rosenbloom ST, Garmire LX, Phillips EJ (nine authors — Department of Biomedical Informatics, Vanderbilt University Medical Center; Division of Maternal Fetal Medicine, Department of Obstetrics and Gynecology, VUMC; Department of Biostatistics, VUMC; Department of Medicine, VUMC; Department of Computational Medicine and Bioinformatics, University of Michigan; Division of Neonatology, Children's Hospital of Philadelphia. **No commercial AI-company affiliations** — the first model-development paper in this list in some weeks with none.)
**Journal:** Pharmacoepidemiology and Drug Safety, 2026; 35(11), article e70516
**Decoded:** 2026-11-06

**Analysis basis:** **FULL TEXT** (retrieved from PubMed Central, PMC13719529) — the complete Introduction, Methods, Results, Discussion, Conclusion, Author Contributions, Funding, Disclosure and Conflicts of Interest statements, plus **Table 1 and Table 2 in full**. **Figures 1–3 and Supporting Tables S1–S18 are not retrievable**, so the cohort flow diagram, the 30-panel predictor analysis, the performance plots, the hyperparameter grid, the three predictor configurations C1 and C2, the temporally stratified results and **the delivery-status stratified results** are described from the body text only. That last gap matters and Section 4 says why: the paper's most important limitation is quantified only in a table I cannot read.

**Source links (verified):**
- DOI: https://doi.org/10.1002/pds.70516
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42957585/
- Full text used: https://pmc.ncbi.nlm.nih.gov/articles/PMC13719529/

**Basis of link verification.** Direct URL fetching is blocked from this session (`doi.org` does not resolve under the network policy here), so verification was done against the live PubMed/NLM record. According to PubMed, a query for PMID 42957585 returned this exact title, these nine authors with these affiliations, *Pharmacoepidemiology and Drug Safety* volume 35 issue 11, DOI `10.1002/pds.70516`, article identifier `e70516` and PMC ID `PMC13719529`; the full text was then retrieved from PubMed Central by that PMC ID and matches the record. Both halves of the chain were confirmed independently.

**Funding: fully reported, with grant numbers.** C.A.B., A.P., L.C., T.R. and E.J.P. are supported by **R21HD113234**; X.Y. by **T32GM141746**; L.X.G. by **R01LM012373, R01LM012907, R03OD039978 and R01HD084633**. All NIH. **Disclosures: reported in detail and separately from the conflicts statement.** A.P. receives industry-sponsored research grant funding from the Novocuff medical device company and serves on a DSMB for an NIH-funded VUMC study. E.J.P. has received consulting fees and royalties from UpToDate, consulting fees from Janssen, AstraZeneca, Intellia, Verve and Glenmark, and grant funding from the NIH, the NHMRC of Australia and the Leo Foundation, all stated as unrelated to the published work. **Conflicts of interest: "The authors declare no conflicts of interest."** Recorded alongside the disclosures above, which is how it should be read.

**Reporting guideline: TRIPOD+AI, named in the Methods, with the completed checklist deposited as supporting information.** The third paper in this list to name TRIPOD+AI and the first to deposit the filled-in checklist.

**Ethics:** approved **with waiver of consent** by the Institutional Review Boards at both sites — VUMC **IRB# 231322** and UMich **HUM# 00168171**. Two approval numbers for two sites, both stated.

**Code and data: no availability statement appears anywhere in the retrieved text.** Not "code unavailable" — *not addressed*. For a paper whose entire claim is reproducibility of a pipeline, that absence is the single sharpest irony in it, and Section 4 returns to it.

---

## 1. The Gist

**This paper asks a question almost no medical-AI paper asks: can somebody else rebuild my method from scratch and get it to work?**

The clinical problem is unglamorous and enormous. To study whether a drug taken in pregnancy harmed a baby, you must know **when** in the pregnancy it was taken — a drug at six weeks and the same drug at thirty weeks are different exposures entirely. That requires knowing how long the pregnancy was. And in electronic health records, that number is frequently **missing, incomplete or simply wrong.** Pregnant people are excluded from almost every randomised trial, so these flawed records are most of what we have for judging drug safety in pregnancy.

So: two teams, two health systems, **88,689 mother–infant pairs** between them. Vanderbilt built a model to estimate gestational age at delivery from routine record data — mother's age, birth weight, APGAR scores, diagnosis codes. Then **a different team at the University of Michigan rebuilt the whole pipeline independently and retrained it on their own patients.**

**Three things make this worth your attention.**

**The models work, and the paper proves it against the right comparison.** At Vanderbilt the ensemble landed **within one week of the clinical estimate for 85.1% of pregnancies** and within two weeks for 94.3%, with a mean absolute error of **4.4 days.** At Michigan, **93.1%** within a week, 97.8% within two, **2.8 days** mean error. Crucially, the paper also reports what you get from guessing the same number every time: a constant median prediction manages **51.7%** within a week. So the machine learning buys **+33.4 percentage points** and cuts the average error by **61%**. Most papers in this list never tell you what guessing would have achieved.

**It refuses to call the second site "external validation," and it is right to refuse.** The Michigan models were **retrained on Michigan data.** So this does not show that Vanderbilt's fitted model works elsewhere — it shows that the *recipe* works elsewhere. The paper states this distinction in plain words: the analysis evaluated "cross-site reproducibility of the development process and portability of the workflow, rather than transportability of the VUMC-fitted models." **In sixty-eight papers, that is the most precise self-description I have read.** Section 5 teaches why the distinction is the whole ballgame.

**And it fails exactly where it matters most, and says so.** The models work well for full-term and late-term deliveries and **substantially worse for preterm.** Preterm babies are 14.3% of the Vanderbilt cohort — and they are the pregnancies that drug-safety research cares about most, because preterm birth is often the outcome being studied. The paper names this, names the consequence (misclassified exposure windows biasing drug-safety estimates), and tells you to use the models cautiously in preterm analyses.

## 2. Study Snapshot

**Study type:** a **retrospective prediction-model development and evaluation study** on routinely collected linked mother–infant EHR data, with **independent reimplementation and site-specific retraining at a second health system.** No prospective arm, no randomisation, no intervention.

**Sites and years:** Vanderbilt University Medical Center (Research Derivative, >5.5 million patients, mother–infant linkages since 2005), deliveries **2005–2025**; University of Michigan Medicine (approximately 5 million patients, records back to 2006), deliveries **2012–2024**.

**Cohort flow, which reconciles exactly at both sites:**
- VUMC: **91,471** initial dyads from **68,659** mothers → one infant per mother retained, non-live-births and inadequate prenatal care excluded → **60,057 (65.7%)** → with a valid parsed gestational-age estimate → **54,344**
- UMich: **55,733** initial dyads from **39,969** mothers → **37,861 (67.9%)** → **34,345**
- My arithmetic: 60,057/91,471 = 65.66% and 37,861/55,733 = 67.93%, both matching the printed figures. **9.5% of VUMC and 9.3% of UMich dyads were then dropped for a missing or unparseable gestational-age expression.**
- Train/test: VUMC **43,475 / 10,869**; UMich **27,476 / 6,869**. Both sum **exactly** to their totals and both are **80.000% / 20.000%.**

**Population (Table 1).** Maternal age at delivery **28.9 years (SD 5.8)** at VUMC, **31.8 (SD 5.3)** at UMich. Predominantly White mothers — **56.2%** VUMC, **68.6%** UMich. Infants **51.5%** and **51.2%** male. Clinical gestational age: mean **269.5 days (SD 18.8)** and **270.9 (SD 16.3)**; **median 274 days in both datasets**; IQR 265–280 and 266–280; range **127–306** and **123–314** days. Delivery status at VUMC: preterm **14.3%**, early term 25.9%, full term 51.3%, late term 8.0%, postterm 0.4%. **Every count in Table 1 — race, infant sex, delivery status — sums exactly to the site total at both sites.** That is three independent breakdowns times two sites, all exact.

**The reference standard, and this is the crux.** The outcome being predicted is the **clinical gestational age (CGA)** — "the birth attendant's final assessment of the infant's gestational age," extracted from free text like "39 weeks 2/7" by regular expression and converted to days. **"The underlying clinical dating method could not be determined from the available records at either institution."** So the target is itself an estimate of unknown provenance. Section 4 explains why that is a limitation and also, for this particular purpose, the right target.

**Models:** random forest, gradient boosting, and an ensemble that **averages the two.** Fivefold cross-validation on the training set for hyperparameter tuning by grid search, then retraining on the full training set and a single evaluation on the held-out test set. A **quantile transformation** was applied to the left-skewed CGA values. **Constant baselines using the training-set mean and median were implemented as comparators** — unprompted, and reported in the main results table.

**Predictors, in three nested configurations:** C1 maternal records only; C2 adding EHR-specific elements; C3 adding paediatric (infant) records. The EHR-specific set is **infant birth weight, 1-minute and 5-minute APGAR scores, number of previous pregnancies, number of fetuses.** ICD-based predictors from maternal records cover preterm, term/postterm, fetal growth restriction and excessive fetal growth; from infant records, preterm, term/postterm, small for gestational age and large for gestational age. Demographics include **maternal age, maternal race and ethnicity, infant sex, and infant race and ethnicity.** ICD codes were encoded as **the number of distinct days or visits on which they were assigned during pregnancy** — chosen after a pilot comparison against binary and category-level encodings.

**Missing data:** **birth weight was available for only 25% of pregnancies and 5-minute APGAR for 42%.** Both were imputed with the **training-set median**, applied to the test set. Where multiple values existed for one infant, **the maximum was taken.**

**Leakage control, done deliberately.** To define the window over which ICD codes were counted, pregnancy duration was estimated from the delivery date plus **the training-set median CGA**, explicitly *not* the dyad's own CGA — "use of the dyad-specific CGA was avoided to prevent target leakage." Section 4 notes what that careful choice costs at the tails.

**Evaluation:** proportion of estimates within **±7 days** and **±14 days** of the reference standard, plus **mean absolute error.** **95% confidence intervals by bootstrapping — 1,000 resampled test sets with replacement, taking the 2.5th and 97.5th percentiles.** Prespecified stratifications: **temporal** (deliveries before versus on/after 1 October 2015, the ICD-9-CM to ICD-10-CM transition) and **by delivery status** (preterm, early term, full term, late term, postterm, with the standard day cutoffs given).

**Headline results (Table 2), with the paper's own bootstrap intervals:**
- VUMC test set, n = 10,869. Mean baseline: 41.5% (40.5–42.4) within 1 week, 72.4% within 2, MAE 12.3 days (12.0–12.6). Median baseline: 51.7% (50.8–52.6), 80.0%, MAE 11.4 (11.1–11.7). Random forest: **85.2% (84.5–85.9)**, 93.9%, MAE **4.4 (4.2–4.5)**. Gradient boosting: 84.0%, 93.7%, MAE 4.6. **Ensemble: 85.1% (84.4–85.8), 94.3% (93.9–94.8), MAE 4.4 (4.2–4.5).**
- UMich test set, n = 6,869. Mean baseline: 42.7%, 75.1%, MAE 11.0. Median baseline: 53.0%, 81.6%, MAE 10.4. Random forest: 92.9%, 97.5%, MAE 2.8. Gradient boosting: 91.1%, 97.0%, MAE 3.1. **Ensemble: 93.1% (92.5–93.7), 97.8% (97.5–98.2), MAE 2.8 (2.7–2.9).**
- **Pearson correlation** between predicted and reference: **0.86–0.89** at VUMC, **0.94–0.95** at UMich.
- **Performance improved with each predictor configuration** C1 → C2 → C3, and **improved for deliveries on or after 1 October 2015.** The per-stratum numbers are in supporting tables I cannot read.

**Predictor associations reported from the training sets** (VUMC n = 43,475, UMich n = 27,476): an **inverted U-shaped** relation between maternal age and gestational age; higher 5-minute APGAR tracking longer gestation; mean gestational age highest among Asian mothers and lowest among Black mothers (**VUMC 271.7 vs 267.2 days; UMich 273.0 vs 268.1 days** — differences of 4.5 and 4.9 days, which I reproduce exactly from the printed means); fetal growth restriction codes associated with lower gestational age (262.3 vs 270.6 and 264.5 vs 272.3 days); SGA codes lower (262.7 vs 270.0; 259.0 vs 270.6) and LGA codes higher (275.3 vs 269.1; 276.8 vs 270.6); **excessive fetal growth codes showing no significant difference**; and an infant-sex difference at VUMC of **0.6 days** that the paper itself calls "unlikely to be clinically meaningful."

**Not reported, or not reachable:** variable importance for any model; the preterm stratum's actual numbers; the mother–infant linkage algorithm and its success rate (**explicitly unavailable to the study team**); the clinical dating method behind the reference standard (**explicitly undeterminable**); any code or data availability statement; model performance by race or ethnicity group (**explicitly acknowledged as not evaluated**).

## 3. How Strong Is This Evidence? (Grade 4 out of 5)

**The second 4 out of 5 in this list, two days after the first, and it earns it on reporting discipline rather than on study design.** Entry 67 got a 4 for having a genuine prospective validation cohort. This paper has nothing prospective at all. What it has instead is **a claim small enough to be fully supported, and a refusal to inflate it.**

**What earns it:**

**It states precisely what it did and did not demonstrate.** "Because the machine learning models were retrained at UMich, this analysis evaluated cross-site reproducibility of the development process and portability of the workflow, rather than transportability of the VUMC-fitted models." Every incentive in publishing pushes toward calling this "external validation." The paper declines, in the Methods and again in the Discussion. **This one sentence is worth more than most papers' entire limitations sections**, and Section 5 teaches the distinction it protects.

**It reports constant baselines, in the main results table, unprompted.** Mean and median predictions: 41.5% and 51.7% within a week, MAE 12.3 and 11.4 days. This is how you prove a model is doing work rather than exploiting a narrow outcome distribution — and with a median of 274 days and an IQR of just 265–280, this outcome is *extremely* narrow. Without the baselines, "85% within one week" would be uninterpretable. **Most papers in this reading list do not report a baseline at all.**

**Bootstrap confidence intervals on every single metric**, by a stated method (1,000 resamples, percentile intervals), for quantities that have no convenient closed form. Not one bare point estimate in Table 2.

**Both stratifications were planned and both were reported honestly, including the one that embarrasses the method.** The delivery-status stratification is the paper's own worst news, and it appears in the abstract, the results, the discussion, the limitations and the conclusion.

**Leakage was considered and actively designed against.** The decision to derive the ICD-counting window from the training-set median rather than the dyad's own gestational age is exactly the sort of thing that gets skipped, and skipping it would have inflated every number in the paper.

**TRIPOD+AI named, with the completed checklist deposited.** Two IRB approval numbers. Grant numbers for every funded author. Industry disclosures itemised by company. This is what full reporting looks like.

**Every arithmetic breakdown reconciles exactly** — cohort flow percentages at both sites, three Table 1 breakdowns at both sites, both train/test splits to three decimal places. Six independent sums, all exact.

**The three predictor configurations map onto real data environments** rather than being an ablation for its own sake: C1 is what you have in administrative claims, C2 is an EHR without mother–infant linkage, C3 is a linked EHR. That is a genuinely useful thing to report, because a reader can locate their own situation.

**What keeps it from 5:**

**No external validation of a fitted model exists anywhere in the paper.** By design, and stated — but it means nobody has yet shown that a model trained at one site produces usable numbers at another without being retrained. For a tool meant to fill gaps across "large-scale real-world" datasets, that is the test that matters, and it has not been run.

**The reference standard is an estimate of undeterminable origin.** Everything in Table 2 is agreement with a birth attendant's assessment, not accuracy against truth.

**The subgroup that the stated purpose depends on is the one that fails**, and I cannot see by how much because the number lives in a supporting table.

**No code availability statement.** For a paper about reproducibility, this is the sharpest gap in it.

## 4. The Editor's Concerns

**1. The reference standard is itself a model output of unknown provenance — and for this purpose that is defensible, which is subtler than it sounds.** The target is "the birth attendant's final assessment," and the paper says outright that the dating method behind it could not be determined. It could be a first-trimester ultrasound, accurate to a few days; it could be a last-menstrual-period date, accurate to a couple of weeks; it could be a Ballard examination of the newborn. So **"MAE 4.4 days" means "4.4 days from what a clinician wrote down," not "4.4 days from conception plus 280."** If CGA itself carries several days of error, the model's true error is larger — and unknowable. **But notice what the tool is for:** filling in gestational age where the record is blank, so that a pharmacoepidemiology study can proceed. The thing you want to recover is *what would have been recorded*. Measured against that goal, agreement with CGA is not a compromise — it is the correct target. The paper never spells this out, and it is the strongest available defence of its own design.

**2. The preterm failure has two mechanisms the paper does not connect, and both are in its own Methods.** The paper reports that performance is substantially worse for preterm deliveries, and treats it as an empirical finding to be improved later. My reading of the Methods says it is close to structural. **First: birth weight was available for only 25% of pregnancies, and the missing 75% were imputed with the training-set median** — and since the median gestational age is 274 days, that imputed value is a *full-term* birth weight. So for a preterm dyad with no recorded weight, the model is handed a normal-weight infant and will pull its estimate toward term. Birth weight is plausibly the single most informative predictor of prematurity, and it is replaced by a term-looking constant in three cases out of four. **Second: the ICD-counting window was derived from the training-set median CGA of 274 days**, applied to every dyad. For a pregnancy that actually lasted 30 weeks, that window reaches about 64 days back **before conception**, sweeping in pre-pregnancy diagnoses; for a postterm pregnancy it is too short. **So the feature-extraction window is systematically mis-sized in exactly the tails that perform worst.** Both choices are individually reasonable — the second is specifically there to prevent leakage — and together they bias the method against the subgroup the stated purpose needs most. This is my inference from the paper's own text, not a claim the paper makes.

**3. The Michigan advantage is probably era, not site, and the paper half-says so.** Vanderbilt spans 2005–2025; Michigan spans 2012–2024. The ICD-9 to ICD-10 transition was 1 October 2015. So roughly **52% of Vanderbilt's calendar span sits in the ICD-9 era against about 29% of Michigan's**, and the paper reports that performance was better after the transition at both sites while attributing Michigan's edge to "reduced reliance on ICD-9-CM predictors." **The 4.4-versus-2.8-day gap is therefore confounded by calendar time, and should not be read as "Michigan's data are better" or "the second implementation was better."** The paper also offers a second era explanation — earlier years had "more limited ultrasound technology," meaning the *reference standard itself* was noisier back then. Both explanations point the same way. I cannot size the effect, because the temporally stratified numbers are in Table S17.

**4. Mean absolute error is the wrong headline for a threshold-based use, and the paper's own band metrics show why.** MAE 4.4 days is an average, and averages hide tails. From the published bands: **5.7% of the Vanderbilt test set — about 620 pregnancies — were off by more than two weeks**, and 2.2% (about 151) at Michigan. The CGA range runs down to 127 days, so some of those errors can be very large. In pharmacoepidemiology, **two weeks is routinely the difference between a first-trimester and a second-trimester exposure**, which is the difference between a plausible teratogenic window and an implausible one. The right question for this use case is not "what is the average error?" but "what fraction crosses a decision boundary, and which direction do they cross in?" The paper supplies the first half with its ±1 and ±2 week bands — a better choice than MAE — and does not address direction at all.

**5. Race and ethnicity are used as predictors, with a 4.5–4.9 day population difference, and no subgroup performance analysis.** The paper is unusually direct about this: "model performance was not evaluated across maternal race and ethnicity groups, even though race and ethnicity were included as predictors," followed by a precise statement of the harm — biased models misestimating gestational age for some groups, leading to exposure misclassification and underrepresentation in pregnancy research. **Credit for naming the gap and the mechanism; it remains a gap.** Two things are worth adding. The reported difference — Black mothers' mean gestational age lowest, Asian mothers' highest — reflects well-documented disparities driven by social and structural factors, not biology, so **using race as an input bakes a social pattern into what reads as a clinical estimate.** And the magnitude provides some reassurance: a 4.5-day between-group difference is roughly the size of the whole model's mean error, so race can only be doing modest work in any individual prediction. "Modest" is not "none," and nobody has measured which way it cuts.

**6. No code availability statement, in a paper whose thesis is reproducibility.** The retrieved text contains Author Contributions, Funding, Disclosure, Conflicts of Interest and a long list of supporting tables — and nothing about code or data access. The paper demonstrates that a second team *can* rebuild the pipeline from the published description, which is a real and underrated result. But the cheapest possible strengthening of a reproducibility claim is to publish the code, and this paper does not mention it either way.

**7. Live births only, so the hardest cases are untested — stated plainly.** The method requires a linked infant record, so pregnancies ending in stillbirth, ectopic pregnancy, spontaneous abortion or termination, and pregnancies still ongoing at data extraction, are all outside it. The paper says exactly this, notes that these are the settings "where identification and dating may be most challenging," and points at the ConcePTION Pregnancy Algorithm as a complement.

**8. The linkage the whole study rests on is a black box to its own authors.** Mother–infant linkages were "established and maintained by the respective institutional data resources prior to this study," and **"details of the procedures used to establish the preexisting mother–infant linkages and the proportion of mother–infant pairs successfully linked at each institution were not available to the study team."** So nobody knows how many dyads were missed, or whether the ones that linked differ systematically from the ones that did not — which is a selection-bias channel of unknown size. The paper flags it as a limitation. Flagging an unmeasurable unknown is the right move, and it is still an unmeasurable unknown.

**9. The comparison with prior work is fair but asymmetric.** The paper benchmarks against Zhu et al. (Medicaid claims, 114,117 pregnancies, Super Learner ensemble: 85.1% within 1 week, 96.4% within 2) and describes its own results as "comparable or improved." Precisely: **Vanderbilt is identical at one week (85.1% versus 85.1%) and 2.1 points worse at two weeks (94.3% versus 96.4%); the improvement comes entirely from Michigan** (93.1% and 97.8%). Both halves of "comparable or improved" are true — they just apply to different sites. Worth stating exactly, since the Michigan figure is also the one confounded by era.

**10. Two minor reporting nits, for completeness.** The imputation rule takes **the maximum** of multiple recorded birth weights or APGAR scores, which is an unexplained choice — a maximum is a reasonable guess at "most complete record" but a defensible alternative is the first recorded value, and for a growing infant the maximum weight is biased upward. And Michigan's full-term share is printed as **53.3%** where 18,333/34,345 is 53.38%, which rounds to 53.4%; a truncation rather than a rounding. **This is the only arithmetic discrepancy I found in the entire paper, and it is in the third significant figure of one descriptive percentage.**

## 5. Statistics Spotlight

Ten techniques, numbered from 194 in the running list in `queue.md`. The first three are the load-bearing ones.

**Reproducibility of a pipeline, portability of a workflow, and transportability of a model are three different claims. Most papers conflate them.**

This paper's central methodological virtue is getting this right, so it is worth laying out carefully. Suppose you build a prediction model at Hospital A and then involve Hospital B. There are three genuinely distinct things you might show.

**Transportability of a fitted model.** You take the *trained model* — the actual fitted trees, with their learned split points — and run it unchanged on Hospital B's patients. This asks: *do the relationships this model learned still hold somewhere else?* It is the hardest test and the most clinically relevant one, because it is what happens when a hospital installs software. It is also where models usually fall over, because coding practices, patient mix and measurement habits differ.

**Reproducibility of a development process.** You give Hospital B your *method description* — inclusion criteria, predictor definitions, algorithm, tuning procedure — and a different team rebuilds it and trains it on B's own patients. This asks: *is the recipe good enough to be followed, and does the approach work on a different population?* It does not test whether your fitted model travels, because the model is refitted from scratch.

**Portability of an analytic workflow.** The narrowest: does the code or procedure *run* in another institution's data environment at all, given different schemas and vocabularies?

**This paper did the second and third. It says so.** "Because the machine learning models were retrained at UMich, this analysis evaluated cross-site reproducibility of the development process and portability of the analytic workflow, rather than transportability of the VUMC-fitted models."

**Why the distinction decides what you may conclude.** Entry 55 in this list flagged a model whose external result *beat* its internal one as a red flag — because a fitted model performing better on unseen data than on its own usually means something leaked or the external case mix was easier. Here Michigan (2.8 days) also beats Vanderbilt (4.4 days), and it is **not** that red flag, precisely because the model was refitted. Michigan's number is a fresh internal result on a different population, not an external one. **Read "the second site did better" as a red flag only when the same fitted model was used at both.** Get this wrong in either direction and you will either dismiss a sound paper or trust an unsound one.

**The everyday version.** Transportability is handing someone your sourdough starter and seeing whether their loaf rises. Reproducibility of the process is handing them your written recipe and seeing whether they can make good bread with their own starter, flour and oven. Portability of the workflow is whether your recipe's instructions even make sense in their kitchen. **All three are worth knowing. Only the first tells you whether *your* starter works in *their* kitchen** — and only the first is what people usually mean when they say "externally validated."

**Watch out for:** papers that describe site-specific retraining and then use the phrase "external validation," or "validated in an independent cohort," in the abstract. The tell is a sentence in the Methods saying the models were retrained or refit at the second site. If they were, no fitted model was tested anywhere, and a reader planning to install the software has learned nothing about whether it will work.

**Minimising mean absolute error on a lopsided outcome pulls every prediction toward the middle — so the rare tail fails by construction, not by accident.**

The paper reports that preterm deliveries do substantially worse. Here is why that is close to inevitable, from the paper's own numbers.

The outcome distribution is extremely concentrated. **Median 274 days. Interquartile range 265–280 days** — so half of all pregnancies sit inside a 15-day window. Full-term and early-term together are **77.2%** of the Vanderbilt cohort. Preterm is **14.3%**, and the range extends down to 127 days.

Now think about what a model minimising average error does with a case it is unsure about. Suppose it sees an infant with no recorded birth weight, no preterm diagnosis code yet, and an average-aged mother. The honest answer is "I don't know." The *error-minimising* answer is **"274 days"** — because that is where the mass is. Guessing near the mode is almost free: the penalty for being wrong about a rare case is small in the average, and the reward for being right about the common case is large.

**A tiny worked example.** You must give one number for a pregnancy you know nothing about. If 85% of pregnancies are 260–290 days and 15% are 200–259, then guessing 274 gives you a small error 85% of the time and a large error 15% of the time. Guessing 250 — hedging toward the preterm group — gives you a *moderate* error almost always. **Average error is lower for the first strategy.** So the model shrinks toward the mode, and the 15% pay for it.

**That is regression toward the mean, and it is not a bug in the algorithm — it is the loss function doing what it was asked.** The predictions are compressed relative to the truth: too high for short pregnancies, too low for long ones.

**Here is how to spot it in any paper.** Look for the scatterplot of predicted against actual. If the cloud's slope is visibly **flatter than the 45-degree line**, predictions are compressed and the tails are being shrunk inward. The Pearson correlations here — 0.86–0.89 and 0.94–0.95 — are *entirely compatible* with that compression, because correlation measures whether the ranking is right, not whether the magnitudes are. The scatterplots are in Figure 3, which I cannot see.

**Watch out for:** reporting only an overall MAE or R² for a skewed outcome, then being surprised that the clinically important tail performs badly. **If your decision depends on the tail, the tail is your outcome — and the fix is to change the loss function (weight the rare cases up, or model the tail separately), not to collect more of the same data.** This paper does the honest thing instead: it reports the stratum separately and tells you to be careful. The next version should reweight.

**Bootstrap confidence intervals: how to get uncertainty for a statistic with no formula.**

Every number in Table 2 carries a 95% interval, obtained by **resampling the test set 1,000 times with replacement, recomputing the metric each time, and taking the 2.5th and 97.5th percentiles.** This is worth understanding because it is the general-purpose tool for exactly this situation.

**Why a formula wouldn't work here.** "Proportion of estimates within 7 days of the reference" is a proportion, so you might reach for the binomial formula. But that would be wrong in a subtle way: it would treat the model as fixed and the only uncertainty as which patients you sampled, and it has no way to express the uncertainty in **MAE**, which is a mean of absolute differences with no standard textbook interval. The bootstrap handles both without needing a formula for either.

**The intuition.** Your test set of 10,869 pregnancies is one draw from a population. You cannot go get another one. But you can *simulate* getting another one by drawing 10,869 pregnancies from your own test set **with replacement** — so some appear twice, some not at all. That resample is a plausible alternative test set. Compute your metric on it. Do that 1,000 times and you have 1,000 plausible values of the metric; the middle 95% of them is your interval.

**A tiny worked example.** Say you have 10 patients and 8 are within a week: 80%. Resample 10 with replacement and maybe you draw 7 of the 8 successes and 3 of the 2 failures — 70%. Again: 90%. Again: 80%. After 1,000 rounds you have a spread, and its 2.5th-to-97.5th percentile range tells you how much the 80% could have wobbled by luck of the draw. With 10 patients that range is enormous. With 10,869 it is narrow — the paper's ensemble interval is **84.4% to 85.8%**, about 1.4 points wide.

**What the intervals here actually tell you.** Compare the ensemble (85.1%, interval 84.4–85.8) with gradient boosting (84.0%, interval 93.3–94.2 at two weeks; at one week, 83.3–84.6). **Those one-week intervals barely overlap**, so the ensemble's edge over gradient boosting is probably real but small. Now compare either against the median baseline (51.7%, interval 50.8–52.6): **nowhere near overlapping.** That is the comparison that matters, and the intervals make it unambiguous.

**Watch out for two things.** First, **the bootstrap quantifies sampling variability only** — the luck of which patients are in your test set. It says nothing about whether your reference standard is right, whether your population resembles anyone else's, or whether a predictor was imputed into uselessness. Yesterday's entry 68 made this point at a sample size of 38.8 million; it applies at 10,869 too. **The intervals in Table 2 are honest and narrow and do not address a single one of this paper's real limitations.** Second, **resampling the test set repeatedly does not make the test set bigger.** The intervals are conditional on the one dataset you have; if it is unrepresentative, the bootstrap will give you a tight interval around the wrong answer.

**197. Always report what guessing would have achieved.** This paper's single most useful reporting choice. A constant median prediction gets **51.7%** of pregnancies within a week and MAE **11.4 days**; the ensemble gets **85.1%** and **4.4 days** — **+33.4 percentage points and a 61% error reduction.** Without the baseline, "85% within one week" is unreadable, because an outcome whose interquartile range is 15 days wide can be predicted fairly well by a ruler. **Whenever a paper reports accuracy on a narrow or heavily imbalanced outcome and gives you no constant-prediction comparator, compute it yourself from the reported distribution before you believe the headline.**

**198. Proportion-within-tolerance beats correlation for a continuous prediction used at a threshold.** The Pearson r values of 0.86–0.95 are the least informative numbers in the paper, because correlation measures whether the *ordering* is right, is inflated by a wide outcome spread, and is completely blind to systematic compression — a model that predicted exactly half the true deviation from the mean every time would still show a near-perfect correlation. The ±1 week and ±2 week bands answer the question a user actually has: **how often is this close enough to act on?** The paper leads with the bands and relegates r to a figure caption, which is the right ordering.

**199. Median imputation when most values are missing turns a predictor into a constant — exactly where it would have mattered.** Birth weight was available for 25% of pregnancies; the other 75% received the training-set median, which is a full-term weight. So the single most informative signal about prematurity is replaced by a term-looking value in three cases out of four. **Before accepting median imputation, ask: is the value missing at random, or is it missing for the same reason it would have been informative?** The paper's own suggested fix — multiple imputation using other predictors available at prediction time, excluding the outcome — is the right one.

**200. A feature-extraction window derived from the outcome's average is biased at the tails.** Counting ICD codes "during pregnancy" requires knowing when pregnancy started, which requires the gestational age you are trying to predict. Using the dyad's own value would be leakage; the paper correctly uses the training-set median instead. **But a 274-day window applied to a 210-day pregnancy reaches 64 days before conception**, importing unrelated diagnoses, and a 274-day window applied to a 295-day pregnancy misses three weeks of it. The careful anti-leakage choice introduces a tail-dependent feature error. **When a lookback window is defined using a population average of the thing you are predicting, the window is wrong by exactly the amount your prediction error will be — check the tails.**

**201. When the reference standard is itself an estimate, "accuracy" means agreement — and sometimes agreement is the right target.** The usual reading is that a soft reference standard caps what you can claim. True here: MAE 4.4 days is distance from a birth attendant's note of undeterminable method. **But the purpose decides.** This tool exists to fill blank gestational-age fields in EHR research, so what you want to recover is *what would have been recorded*. Measured against that, agreement with the clinical estimate is not a compromise — it is correct. **Ask what the number will be used for before deciding whether a soft reference standard is a flaw or the specification.**

**202. Using race as a predictor without subgroup performance evaluation.** Maternal and infant race and ethnicity were inputs. Mean gestational age differed by 4.5–4.9 days across groups — a real, documented disparity driven by social and structural factors, not biology. Feeding it in as a predictor **encodes a social pattern into something that reads as a clinical measurement.** The magnitude offers partial reassurance (4.5 days is about the size of the whole model's mean error, so race can only be doing modest work in any one prediction), but **the only way to know which way it cuts is to report performance by group**, which the paper acknowledges it did not do. **Any model with race as an input owes its readers a per-group error table.**

**203. A coding-system transition is a free natural experiment in data drift.** The ICD-9-CM to ICD-10-CM switch on 1 October 2015 gives a clean date on which the meaning of every diagnosis feature changed, and the paper exploits it by stratifying on it — finding better performance afterwards. **But it also confounds the site comparison**, because Vanderbilt's 2005–2025 span sits roughly 52% in the ICD-9 era against Michigan's roughly 29%. So the 4.4-versus-2.8-day gap is substantially a calendar-era effect. **Whenever two cohorts cover different calendar spans and the features are administrative codes, era is a confounder before site is** — and the fix is to compare them within a common window.

## 6. Jargon Translator

**Gestational age** — how far along a pregnancy is, counted in weeks and days from the start. "39 weeks 2/7" means 39 weeks and 2 days, which is 275 days. Term is 37 weeks and up; preterm is under 37.

**Mother–infant dyad** — one mother linked to one of her babies in the record system, so that information from both charts can be used together. The linking is what makes the infant's birth weight and APGAR scores available as clues about the pregnancy.

**Pharmacoepidemiology** — studying how drugs behave in real populations rather than in trials. In pregnancy it is nearly the only option, because pregnant people are excluded from almost all randomised trials.

**Exposure window** — the stretch of pregnancy during which a drug was taken. Getting it wrong by two weeks can move an exposure from the first trimester to the second, which changes what harm is biologically plausible.

**Mean absolute error (MAE)** — add up how far off each prediction was, ignoring whether it was too high or too low, and divide by the number of predictions. An average, so it hides tails.

**Random forest** — build hundreds of decision trees, each on a random slice of the data and the predictors, then average their answers. Averaging cancels out individual trees' quirks.

**Gradient boosting** — build trees one after another, each new tree focusing on the cases the previous ones got wrong. Often slightly sharper than a forest, and often slightly more prone to chasing noise.

**Ensemble** — combine several models' predictions. Here, simply averaging the forest and the boosting outputs; it came out best at both sites by a small margin.

**Fivefold cross-validation** — split the training data into five parts, train on four and test on the fifth, rotate through all five, and average. It lets you tune settings without touching the real test set.

**Hyperparameter / grid search** — settings you choose rather than learn, like how deep a tree may grow. Grid search tries a list of combinations and keeps the best.

**Quantile transformation** — reshaping a lopsided distribution so the values spread out evenly, which stops extreme values dominating. Used here on gestational age, which is left-skewed because pregnancies can end much too early but not much too late.

**Target leakage** — when a predictor secretly contains the answer, so the model looks brilliant in testing and fails in use. This paper explicitly avoided it when defining its ICD lookback window.

**Bootstrapping** — building a confidence interval by resampling your own data with replacement, hundreds or thousands of times, and reading off the middle 95% of the results. The general-purpose tool when no formula exists.

**ICD-9-CM / ICD-10-CM** — the diagnosis-coding systems US healthcare bills with. The US switched on 1 October 2015, and ICD-10 is far more detailed, so a feature built from diagnosis codes means something different before and after that date.

**APGAR score** — a 0-to-10 score of a newborn's condition at 1 and 5 minutes, covering colour, pulse, reflexes, muscle tone and breathing.

**Small / large for gestational age (SGA / LGA), fetal growth restriction (FGR)** — codes for a baby smaller or bigger than expected for how far along the pregnancy was, and for a fetus not growing as expected.

**TRIPOD+AI** — the reporting checklist for clinical prediction models built with machine learning. It says what a paper must disclose. It is a reporting standard, not a quality standard: following it means you told the reader everything, not that what you did was good.

**Transportability versus reproducibility versus portability** — whether *your trained model* works elsewhere; whether *your method* can be rebuilt elsewhere; whether *your code* runs elsewhere. Section 5 unpacks why conflating the first two is the most common overclaim in medical AI.

## 7. What You Can (and Can't) Say

**You can say:**

"Machine-learning models using routine record data estimated gestational age at delivery within one week of the clinical estimate for 85% of pregnancies at Vanderbilt and 93% at Michigan, against 52% for simply guessing the median."

"A second team at a different health system rebuilt the same pipeline independently from the published description and got it working on their own patients, which is evidence the method is reproducible."

"The models were substantially less accurate for preterm deliveries, and the authors say so and advise caution in analyses involving preterm births."

"About 6% of Vanderbilt estimates and 2% of Michigan estimates were off by more than two weeks."

"This could help fill in missing gestational ages in record-based research on drug safety in pregnancy, which is one of the few ways to study a population excluded from clinical trials."

**You cannot say:**

"The model was externally validated." It was not, and the paper is explicit that it was not. The second site retrained from scratch, so no fitted model was tested anywhere outside its own data.

"Michigan's data are better than Vanderbilt's," or "the second implementation was better." Vanderbilt's records reach back to 2005 and Michigan's to 2012, straddling the ICD-10 transition very differently. The gap is substantially calendar era, and the paper points that out itself.

"The models estimate gestational age to within 4.4 days." They agree with a clinician's recorded estimate to within 4.4 days on average. The clinician's estimate has its own error, of unknown size, and the paper says the dating method behind it could not be determined.

"AI can date pregnancies." It can reproduce a *recorded* date at *delivery*, using the infant's birth weight and newborn diagnoses. It is working backwards from the birth, not forwards from conception, and it needs the baby's chart to do it.

"This works for difficult pregnancies." The study covers **live births only**, with a linked infant record. Stillbirths, miscarriages, terminations, ectopic pregnancies and ongoing pregnancies — where dating is hardest — are entirely untested, as the paper states.

"Performance is equitable across groups." Unknown. Race and ethnicity were used as predictors and performance by group was not evaluated; the paper names this as an unresolved gap.

"Reproducibility was demonstrated, so the method is trustworthy." Reproducibility of the *process* was demonstrated at *two* academic medical centres with mature mother–infant linkage. Both have large research data warehouses and dedicated informatics departments. Whether the recipe survives in a community hospital's record system is a separate question.

**The honest one-sentence version:** *a careful, fully reported study showing that a sensible recipe for recovering gestational age from linked mother–infant records can be rebuilt at a second hospital and works well for ordinary term births, poorly for the preterm births that matter most to the research it is meant to serve, and has never been tested as a fitted model anywhere but where it was trained.*

## 8. Bottom Line for Your Life

**If you are a patient or a parent:** nothing here changes anyone's care. This is plumbing for researchers — a way to recover a number that was supposed to be in the chart and wasn't, so that studies of medication safety in pregnancy can be done at all. The reason it matters to you indirectly is real, though: because pregnant people are excluded from nearly every drug trial, almost everything known about medication safety in pregnancy comes from records like these, and the records are patchy. Better patching means less guessing in the advice you eventually get.

**If you are a clinician:** the practical message is in the stratified result. These estimates are good enough for ordinary term pregnancies and **not** good enough for preterm ones. If you ever see a study whose exposure windows were derived this way, the preterm subgroup is where to direct your scepticism — and the authors would agree with you, because they say so.

**If you do record-based research:** this is a usable method with a clearly marked failure mode, and the three predictor configurations tell you what to expect in your own data environment — claims-only, EHR without linkage, or linked EHR. Two cautions. Check whether your birth weight field is populated: **it was available in only a quarter of pregnancies here**, median-imputed in the rest, and that is very likely a large part of why preterm fails. And do not quote the 2.8-day figure as the method's accuracy; quote 4.4, or better, quote the band that matters for your own decision boundary.

**If you are designing a study:** this paper is worth copying for four specific habits. **Report the constant baseline** — it is the only thing that makes "85% within a week" interpretable on an outcome whose interquartile range is 15 days. **Put a bootstrap interval on every metric**, including the ones with no closed-form formula. **Prespecify the stratification that might embarrass you**, and publish it. And **describe what you demonstrated in the narrowest true words** — "reproducibility of the development process and portability of the analytic workflow, rather than transportability of the fitted models" is a sentence to keep.

**If you are reading medical-AI claims generally:** this paper is the clearest available illustration that **"tested at a second hospital" can mean three completely different things**, and that only one of them tells you whether software will work when installed. The tell is one sentence in the Methods about whether the model was retrained. Look for it every time.

**This is education, not medical advice.** Nothing here should change anyone's treatment or any decision about medication in pregnancy. Those are conversations with a clinician.

---

## Appendix: deferred papers and shelf, status on 2026-11-06

**Landmark check for the past week, per the trigger's step 2.** According to PubMed, a search of JAMA, Lancet, NEJM, Nature, Nature Medicine and BMJ for AI, machine-learning, deep-learning or LLM titles entered between 2026-10-30 and 2026-11-06 returned **exactly two records**, neither a primary study: a NEJM Clinical Decisions case report on AI scribes for clinical notes (PMID 42981576, [DOI](https://doi.org/10.1056/NEJMclde2600746), 395(18):1864-1866, no abstract) and a Lancet commentary on governing AI for reliable research (PMID 42962694, [DOI](<https://doi.org/10.1016/S0140-6736(26)02159-8>), no abstract). **Neither displaces the queue pick.** The AI-scribe case report is noted as a possible future entry if a primary scribe trial appears.

**Deferred papers — all three re-checked today against the live PubMed record; none has a PMC copy, so none is retrievable.**

**1. "The anatomy of a personal health agent" — Nature (PMID 42907512, [DOI](https://doi.org/10.1038/s41586-026-11161-8), 659(8139):197-207).** **Deferred, day 17.** Weekly re-check schedule, next 2026-11-12. The open-source framework may be inspectable even if the paper is not.

**2. BMJ review of LLM-trial reporting completeness (PMID 42869550, [DOI](https://doi.org/10.1136/bmj-2026-100855), 395:e100855).** **Deferred, day 24 — and this one reaches its own twenty-one-day threshold on 2026-11-12 under the rule that fired yesterday.** Standing instruction: **if no PMC body by 2026-11-12, decode abstract-only and say so explicitly.** Its abstract is unusually rich (461 records; mean completeness TRIPOD-LLM 40%, CONSORT 2025 44%, CONSORT-AI 59%, CHART 52%, SPIRIT 2025 51%, SPIRIT-AI 57%, WHO dataset 61%) and Moons and Collins — the TRIPOD authors — are among the twelve. **It is the most relevant paper on the shelf to this list's purpose, and today's entry makes it more so**: this is the third paper here to name TRIPOD+AI and the first to deposit the completed checklist, which is exactly the behaviour that review measures.

**3. *Annals of Internal Medicine*, overuse and false restraint in LLM *Choosing Wisely* recommendations (PMID 42896192, [DOI](https://doi.org/10.7326/ANNALS-26-01667)).** **Deferred, day 17.** Weekly re-check, next 2026-11-12; abstract-only date set at 2026-11-19. Standing note carried unchanged: the overuse rate of **5.4%, 95% CI 0.6%–12.2%** has an interval far too wide for 4,050 responses (a plain binomial interval would be about 4.7%–6.2%), because it is correctly computed across the **15 recommendations** rather than the responses — a clustering signature, and the right way to report a clustered benchmark.

**Shelf status: four spares remain**, in order — (3) bipolar speech/NLP, 6,373 features on 160 people (PMID 42967232, PMC13723951); (4) NOTIFY-DISCUSS qualitative study of a deployed AI tool (42965008); (5) precision-psychiatry six-stage framework review (42947584); (6) explainable-AI urology review of 70 studies (42960345). **Next run takes spare (3)** — a 6,373-features-on-160-people study, which after today's paper will be a sharp contrast in sample-size discipline and a natural home for teaching the curse of dimensionality.

**Watch item:** PM Heart trial results (protocol PMID 42893738), quarterly.
