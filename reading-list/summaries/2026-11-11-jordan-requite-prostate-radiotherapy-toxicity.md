# Exploratory machine-learning evaluation of clinical and dosimetric features in late prostate radiotherapy toxicity

**Authors:** Jordan K, Talbot CJ, Kelleher JD, Lyng F, Meade AD (five authors — School of Physics, Clinical & Optometric Sciences and the Centre for Radiation and Environmental Science, Technological University Dublin; St. Vincent's Private Hospital, Dublin; Division of Genetics and Genome Biology, Leicester Cancer Research Centre, University of Leicester; ADAPT Research Centre, School of Computer Science and Statistics, Trinity College Dublin. **No commercial affiliations.**)
**Journal:** Clinical and Translational Radiation Oncology, 2026; 62: 101305
**Decoded:** 2026-11-11

**Analysis basis:** **FULL TEXT** (retrieved from PubMed Central, PMC13744349) — the complete Introduction, all five Methods sub-sections, all five Results sub-sections, the full Discussion with limitations, Conclusion, CRediT statement, Ethics declaration, Funding and Declaration of Competing Interest. **Every figure and the entire supplementary appendix are unreachable** — Figures S1–S6 and Tables S1–S3, which hold the toxicity distribution over follow-up, the feature-correlation matrix, the patient-level SHAP heatmaps, the feature-rank stability summary, the SHAP distributions across repeats, **the permutation null distributions**, the hyperparameter grids and the repeat-level performance variability. Section 4 says where that matters.

**Source links (verified):**
- DOI: https://doi.org/10.1016/j.ctro.2026.101305
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42999685/
- Full text used: https://pmc.ncbi.nlm.nih.gov/articles/PMC13744349/

**Basis of link verification.** Direct URL fetching is blocked from this session (`doi.org` does not resolve under the network policy here), so verification was done against the live PubMed/NLM record. According to PubMed, a query for PMID 42999685 returned this exact title, these five authors with these affiliations, *Clinical and Translational Radiation Oncology* volume 62 article 101305, DOI `10.1016/j.ctro.2026.101305`, publisher identifier `S2405-6308(26)00200-4` and PMC ID `PMC13744349`; the full text was then retrieved from PubMed Central by that PMC ID and matches the record. Both halves of the chain were confirmed independently.

**Funding: present but partly stripped by the extraction and therefore partly unreportable.** The statement reads "K.J is funded by and. This research is supported by funding from the under Grant number [HRB Grant Code:]" — **the funder names and the grant code were removed by the extraction and I am not guessing them.** The surviving fragment indicates a Health Research Board grant.

**Competing interests: complete and explicit.** "The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper."

**Ethics: two approvals, both numbered.** This analysis was approved by the **Technological University Dublin Research Ethics Committee (REC-19-34)**; the parent REQUITE study was reviewed and approved by **North West – Great Manchester East Ethics Committee (UK, reference 14 NW 0035)**. **Written informed consent from all participants**, including for publication, conducted per the Declaration of Helsinki.

**Reporting guideline: none named.** TRIPOD+AI would be the fitting one for a prediction-model study, and Section 4 notes its absence against what the paper actually did.

**Software:** Python 3.12, scikit-learn 1.6.

---

## 1. The Gist

**This is a study that found almost nothing, and it is one of the best papers decoded in this reading list.**

The clinical question is real and unsolved. About half of all cancer patients receive radiotherapy, and for prostate cancer it works well — but some men develop lasting bowel or urinary problems afterwards and some do not, given the same dose. If you could tell in advance who, you could change the plan for them. Decades of work have gone into trying, using the two things every radiotherapy department already has: **the patient's clinical details, and the dose maps showing how much radiation each organ received.**

**229 men from the REQUITE cohort, three machine-learning models, and the answer is: those two things barely help.**

For **bowel (gastrointestinal) toxicity**, the models reached areas under the curve of **0.573, 0.571 and 0.587** — where 0.5 is a coin flip and 1.0 is perfect. Permutation testing confirmed this was **genuinely above chance** (p = 0.036, 0.047, 0.022). So there is a signal. It is just very small: my arithmetic puts **AUC 0.587 at about 2.4% of the variance** in who develops toxicity, and translates it into the only terms that matter at a bedside — **a positive result moves a man from a 47% chance to a 55% chance, and a negative result from 53% to 63%.** Both land where you would do exactly the same thing either way.

For **urinary (genitourinary) toxicity**, the models came in **below chance** — 0.465, 0.455, 0.466 — and the authors did something unusual and exactly right: having seen below-0.5 values, they ran **two-sided** permutation tests to ask whether that inverse pattern was itself systematic. It was not (p = 0.150–0.412). **It is noise around 0.5. There is nothing there.**

**And here is the finding that makes this paper matter beyond radiotherapy.** Rectal dose — summarised as equivalent uniform dose — was **the top-ranked predictor in every single cross-validation repeat, across all three models**, with the right sign, and it is biologically established that rectal irradiation causes bowel toxicity. **Maximally stable explanation. Correct explanation. True explanation. And the model still cannot usefully discriminate.** The authors write it plainly:

> *"Models may repeatedly identify rectal dose or patient and treatment characteristics as influential while providing insufficient discrimination for individual risk stratification and limit clinical utility."*

**Yesterday's entry argued that explanations get used as confirmation and that plausibility is not validation. This is the experiment that proves it.** The explanation here is as good as explanations get. The model is worth about eight percentage points of predictive value. **The two are independent, and this paper demonstrates it rather than asserting it.**

## 2. Study Snapshot

**Study type:** a **retrospective analysis of a prospective multicentre observational cohort** — an exploratory prediction-model development and internal-evaluation study. No external validation, no randomisation, no intervention. The title's word "exploratory" is doing honest work.

**Source cohort:** **REQUITE**, a prospective multicentre observational study established specifically "to validate radiotherapy toxicity prediction models and investigate determinants of individual radiosensitivity." All patients received external beam radiotherapy.

**Participants: 229 men with prostate cancer.** All had "a complete record of baseline clinical, treatment and dosimetric data together with longitudinal toxicity assessments." **No missing data in the final analysis dataset, so no imputation was required** — an unusual and clean position. **The size of the parent REQUITE prostate cohort is not reported**, and Section 4 treats that as the study's main unexamined gap.

**Outcome definition, and it is thoughtful.** Toxicity was assessed with **CTCAE version 4.0** before radiotherapy, within three months after, and at **12, 24 and 48 months**. Individual events were grouped into composite GI and GU endpoints by anatomical system. Crucially, **toxicity was defined as a Grade ≥1 increase relative to each patient's own baseline**, "such that only new or worsening symptoms were considered treatment-related." The endpoints were increased late GI and GU toxicity occurring **at least 12 months after radiotherapy**, as binary variables, referred to as G1+ GI and G1+ GU.

**Event counts — and one discrepancy I found.** GI: **107 patients (46.7%)**, which reproduces exactly (107/229 = 46.72%). GU: **the abstract says 125 (54.6%) while the Methods and Results both say 126 (55%)**. Each figure is internally consistent with its own percentage (125/229 = 54.59%; 126/229 = 55.02%), so this is a one-patient transcription slip rather than an arithmetic error. **It changes no conclusion.** I use the body figure of 126 below, and Section 4 reports it because checking is the job.

**Predictors, prespecified.** Candidate predictors were "selected a priori from published evidence and clinical relevance to reduce redundancy," covering patient characteristics, treatment-related variables, and dose–volume metrics for rectum and bladder. **Continuous dosimetric variables were collapsed into equivalent uniform dose (EUD)** using the **Niemierko formulation**, with **organ-specific parameters derived from published literature**, after converting cumulative dose–volume histograms to differential volume fractions. The stated purpose: "reduced correlation between individual dose–volume histogram parameters while retaining information on the uniform dose distribution within each organ." The full feature list is in a table that did not extract; the predictors named in the prose are **rectal EUD, bladder EUD, PTV volume, age, BMI, previous abdominal surgery, pre-radiotherapy TURP and bladder TUR.**

**Models:** three, chosen for contrast — **L1-regularised logistic regression** and **Elastic Net logistic regression** as interpretable linear models, and **XGBoost** as "a non-linear ensemble method capable of modelling complex feature interactions." Separate models for each endpoint with endpoint-specific feature sets.

**The validation architecture, which is the paper's strongest feature.**
- **Repeated nested stratified cross-validation:** an outer loop of **five stratified folds repeated five times**, giving **25 outer validation sets per endpoint.** **Hyperparameters were optimised exclusively within the inner loop** — "This framework ensured separation between model training and performance evaluation."
- Continuous variables standardised **within the training data** via a pipeline fitted only on the corresponding training folds.
- **Out-of-fold predictions:** within each repeat, predictions from the five outer test folds were pooled "so that each patient contributed one independent OOF prediction." Metrics computed per repeat, then summarised across repeats. **ROC-AUC was specified a priori as the primary measure of discrimination.**
- **Thresholds set on training data only.** Within each outer fold, OOF predictions were generated for the outer *training* set via the inner cross-validation, the optimal threshold selected by **Youden's J statistic**, and that threshold **"subsequently fixed and applied to the corresponding unseen outer test fold."** Sensitivity, specificity and F1 were then computed from the resulting test-fold classifications.
- **Patient-level bootstrap:** **2,000 resamples**, sampling patients with replacement and "preserving all OOF predictions belonging to the sampled patient across the repeated cross-validation procedure." Performed on stored OOF predictions after model development; **"models were not refitted during bootstrapping."**
- **Outcome-label permutation testing: 1,000 iterations**, with labels permuted while predictors were held unchanged, and **"the complete repeated nested cross-validation pipeline was then repeated, including inner-loop hyperparameter optimisation, model fitting and generation of OOF predictions."** One-sided tests for above-chance discrimination; **and, because some models came in below chance, two-sided tests were additionally run** to ask "whether the observed inverse discrimination represented a systematic predictive pattern."

**Interpretation, done out-of-fold.** SHAP values were **"calculated within each outer validation fold and were retained only for patients in the corresponding unseen test fold"** — LinearExplainer for the penalised regressions with the transformed outer training data as background, TreeExplainer for XGBoost. Global importance from pooled OOF absolute SHAP values; patient-level profiles averaged across repeats; and **stability assessed separately within each repeat**, summarised by "the mean, standard deviation and median feature rank across repeats, together with the best and worst observed rank and the frequency with which each feature appeared among the three highest-ranked predictors." The paper states that **"SHAP analyses were considered exploratory"** and were used "to describe model behaviour and the stability of learned feature contributions rather than to infer independent, causal or clinically validated associations."

**Results.**
- **GI discrimination:** mean pooled OOF ROC-AUC **0.573** (L1), **0.571** (Elastic Net), **0.587** (XGBoost). Sensitivity **0.628–0.658**, specificity **0.487–0.518**.
- **GU discrimination: below chance** — **0.465** (L1), **0.455** (Elastic Net), **0.466** (XGBoost). Sensitivity **0.402–0.579**, specificity **0.390–0.551**.
- **Permutation testing:** GI **p = 0.036, 0.047, 0.022** against mean null values of approximately 0.5 — "supported a small predictive signal." GU: **p = 0.150–0.412**, "no significant evidence of predictive discrimination ... despite observed ROC-AUCs below 0.5."
- **SHAP, GI:** **rectal EUD was the highest-ranked predictor across all three models** and showed the largest overall contributions, with higher values producing positive SHAP values. **Previous abdominal surgery** was also consistently influential, particularly in the penalised regressions. Age, BMI and PTV volume showed smaller, model-dependent contributions.
- **SHAP, GU:** bladder EUD, PTV volume, BMI and age were most prominent "although their relative importance varied between models." Pre-radiotherapy TURP and bladder TUR contributed comparatively little.
- **Stability:** for GI, **rectal EUD "showed the greatest stability, ranking first in all repeats across all three models."** Previous abdominal surgery was consistently high in the penalised regressions; PTV volume was consistently top-three for XGBoost. **GU rankings "were more model dependent,"** though bladder EUD was relatively consistent.

**Context the paper supplies on prior work:** models combining clinical and dosimetric variables "have reported AUCs of approximately **0.66–0.81**," and deep-learning approaches "have achieved AUCs of up to **0.81** for acute rectal toxicity." The paper's own reading: the lower values here "are consistent with reports that clinical predictors alone may provide limited discrimination for late toxicity endpoints," and it notes that its validation apparatus was used "to reduce optimistic estimates."

**Limitations stated by the authors:** 229 is "relatively modest for machine-learning development, limiting model complexity and increasing uncertainty"; the **G1+ endpoint "differs from conventional Grade ≥ 2 endpoints"** and a one-grade increase "may include relatively mild symptoms," though it is clinically interpretable and increased the available events; the binary endpoint "did not capture symptom type or longitudinal trajectory"; **dosimetry was based on treatment-planning dose**, not accumulated delivered dose, and did not account for anatomical change; **whole-organ EUD "may not capture spatial dose or relevant substructures"** — specifically the bladder neck and urethra for GU; and **"validation was internal to this cohort, limiting assessment of generalisability."**

**The authors' own forward conclusion:** that "relevant information describing individual radiosensitivity is absent from conventional clinical and dosimetric variables in this cohort," that late radiation injury is "biologically heterogeneous, with similar physical dose distributions potentially producing substantially different outcomes," that **genomic susceptibility has previously shown predictive information** for selected late endpoints, and that integration with "genomic, lipidomic, metabolomic or other molecular measurements" may be needed.

**Not reported or not reachable:** the parent REQUITE cohort size and any inclusion flow; **any calibration assessment** — the paper reports discrimination only, start to finish; all figures and supplementary tables; the funder names and grant code.

## 3. How Strong Is This Evidence? (Grade 4 out of 5)

**The fourth 4 out of 5 in this list, and the first awarded to a study that found essentially nothing. The execution is at 5 level; a design ceiling holds the grade to 4.**

This needs stating plainly, because the instinct with a near-null result is to grade it down. **A study that correctly establishes the absence of a usable signal is as valuable as one that establishes its presence** — more so here, because the literature contains AUCs of 0.66 to 0.81 for the same clinical question, and somebody had to check whether those survive proper validation.

**What earns the grade.**

**The permutation test is done the hard way, and almost nobody does it.** One thousand iterations, each re-running **the complete pipeline including inner-loop hyperparameter optimisation.** The shortcut — permuting labels and refitting a single pre-tuned model — produces a null that is too narrow, because it omits the variance contributed by model selection. **I verified the consequence arithmetically:** against a Hanley–McNeil asymptotic null SE of 0.0383, the three GI AUCs sit 1.91, 1.85 and 2.27 standard deviations above 0.5, implying one-sided p-values of 0.028, 0.032 and 0.012. The paper reports **0.036, 0.047 and 0.022.** **Every reported value is modestly larger than the asymptotic approximation — exactly the direction a correctly-widened null produces.** That is positive evidence the permutation was implemented honestly rather than approximated.

**The two-sided test, added for the right reason.** Observing a below-chance AUC, most papers either ignore it or report it as "no better than chance." These authors asked the sharper question: is the *inverse* discrimination systematic — has the model learned real signal with the wrong sign? **That would have been an interesting positive finding.** They tested for it and reported that it was not there.

**The operating threshold is selected on training data only.** Youden's J computed from inner-CV predictions on the outer *training* set, then fixed and applied to the unseen test fold. **Entry 70 of this list, four days ago, was criticised for selecting its Youden point on the pooled out-of-fold predictions it then reported.** This paper does the correct thing, which is harder to implement and almost never seen.

**SHAP computed out-of-fold.** Values calculated within each outer fold and retained **only for patients in the corresponding unseen test fold.** Most SHAP analyses in medicine are computed on training data or the whole dataset; this is the explanation analogue of out-of-fold prediction, and it is the only version that tells you anything about generalisable model behaviour.

**Feature-importance stability quantified with rank statistics** — mean, SD, median, best and worst rank across repeats, plus top-three frequency. **Rectal EUD ranked first in all repeats across all three models**, which is maximal stability and is reported as such rather than asserted.

**Collinearity handled by design rather than by hope.** Dose–volume histogram parameters are notoriously inter-correlated; collapsing them into organ-specific EUD via the Niemierko formulation with literature-derived parameters is a principled solution applied before modelling.

**The baseline-corrected endpoint.** Defining toxicity as a one-grade increase *from each patient's own baseline* means stable pre-existing symptoms are not counted as treatment harm. That correction is rarely made and it is the right one.

**And the conclusion is exactly the size of the evidence.** "Routine clinical and dosimetric variables provided limited predictive information for late GI toxicity but did not reliably discriminate GU toxicity." No hedging upward, no "promising," no "warrants clinical investigation." The abstract's own highlights say "**GU models showed no evidence of discrimination beyond chance.**"

**One more thing worth noticing: the study had near-ideal conditions.** Event rates of 46.7% and 55.0% mean almost perfectly balanced classes — the easiest possible setting for a classifier, with no class-imbalance penalty. Prespecified features. Zero missing data. A prospective multicentre source cohort. **It had everything going for it and still found 2.4% of the variance.** That makes the negative result stronger, not weaker.

**What holds it to 4.**

**229 patients, and no denominator.** This is the complete-data subset of a larger prospective cohort, and **the parent size is never given** — no flow from enrolled to analysed, no comparison of included against excluded men. Selecting on complete records is a selection mechanism, and Section 4 argues it plausibly favours better-resourced centres and healthier attenders. Direction unknown, magnitude unknown, unexaminable from what is reported.

**Internal validation only**, stated by the authors. For a negative finding this matters less than for a positive one — you are not claiming transportable performance — but it still means the result is about this cohort.

**No calibration anywhere.** Discrimination from start to finish. For a model this weak, calibration is arguably moot; it is still an omission in a prediction-model paper, and TRIPOD+AI would have asked for it.

**No reporting guideline named**, despite the study doing more of what TRIPOD+AI asks than most papers that cite it.

**And the 125-versus-126 slip.** Trivial in effect, and the only arithmetic inconsistency I found in the paper.

**Why not 5.** The ceiling is the design: a single modest cohort, internally validated, with an unexamined selection into it. **Why not 3.** Because the execution is better than anything else in this list, the claim and the evidence match precisely, and the paper reports the number that undercuts the field it belongs to.

## 4. The Editor's Concerns

**1. The paper's most important sentence is in the Discussion, and it resolves yesterday's problem.** Rectal EUD ranked first in all 25 repeats across all three models, with the correct sign, for a mechanism that is biologically established. By every available measure, **that is a perfect explanation.** And the model carrying it has an AUC of 0.587. The authors state the consequence: "**Models may repeatedly identify rectal dose or patient and treatment characteristics as influential while providing insufficient discrimination for individual risk stratification.**" **Entry 73 yesterday argued that explanation plausibility is not validation; this paper is the demonstration.** It should be cited whenever someone offers a stable SHAP ranking as evidence that a model works.

**2. The gap between this study's AUCs and the literature's deserves a harder look than the paper gives it.** Prior clinical-and-dosimetric models report **0.66–0.81**; deep learning up to **0.81**. My conversion: those correspond to roughly **8% to 28% of outcome variance**, against this study's **2.4%**. The paper attributes the difference to "treatment technique, toxicity definition, follow-up and available predictors" — all genuine. **But it also supplies the other candidate explanation and declines to press it:** "Nested cross-validation, patient-level bootstrapping and outcome-label permutation testing were used to **reduce optimistic estimates**." Studies lacking those safeguards report higher numbers. **The most parsimonious reading of a tenfold variance gap between this analysis and its predecessors is that this one was measured more carefully**, and the paper is entitled to say so more directly than it does.

**3. A numerator with no denominator — the same gap as yesterday's entry.** 229 men with complete records, out of a REQUITE prostate cohort of unstated size. **Complete dosimetry plus four follow-up visits over 48 months is not a neutral filter**: it plausibly selects men treated at better-resourced centres, with better record-keeping, who were well enough to keep attending. Any of those could move a toxicity-prediction result in either direction. A single sentence giving the parent cohort size and a comparison of included against excluded men would have settled it.

**4. No calibration, in a paper that otherwise does everything.** Every metric reported is discrimination or a threshold-derived classification. **A prediction model's probabilities can be badly wrong even when its ranking is adequate** — entry 67 in this list devoted a whole section to exactly that failure. Here the models are too weak for calibration to rescue anything, so the omission costs little in substance; it is conspicuous given the care taken everywhere else, and it is one of the few places where a TRIPOD+AI checklist would have changed the paper.

**5. The endpoint buys events at the cost of clinical meaning, and the paper says so without quite drawing the conclusion.** A **one-grade** CTCAE increase from baseline produces event rates of **46.7%** and **55.0%** — far above conventional Grade ≥2 late-toxicity rates. The authors note it "may include relatively mild symptoms" and "differs from conventional Grade ≥ 2 endpoints." **The implication for a reader is that this study's near-null result is about predicting *any* worsening, including mild and possibly transient worsening.** It is entirely possible that severe toxicity — the thing a clinician would change a plan for — is more predictable, and that this design could not see it. The paper's chosen endpoint was defensible and arguably necessary at n=229; the residual uncertainty should be stated as such.

**6. Planning dose, not delivered dose.** Flagged by the authors. Worth underlining because it bounds the whole exercise: the prostate, rectum and bladder move and change volume over a multi-week course, so the planned dose map is an approximation of what the tissue received. **If a real dose–response signal exists, planning dose is a blurred measurement of the exposure**, and blurring the exposure attenuates any association toward null. That is a mechanism by which this study could understate a genuine effect, and it sits alongside the authors' own preferred explanation (that the biology is simply missing from these variables).

**7. Whole-organ EUD may be the wrong summary for GU, and the authors identify exactly why.** "Whole-bladder EUD may not adequately represent dose to urinary substructures, such as the bladder neck and urethra, which may be more relevant to individual GU symptoms." **That is a specific, testable explanation for why GU came in at chance while GI did not** — the rectum is relatively homogeneous in its radiation response, the bladder is not. It makes the GU null a finding about the measurement rather than necessarily about the biology, and the paper says so.

**8. The two-sided permutation result deserves more prominence than it gets.** Finding three AUCs below 0.5 and then formally testing whether the inversion is systematic is a genuinely sophisticated move, and the answer — **p = 0.150 to 0.412, so it is sampling noise** — is what licenses the clean statement "no evidence of discrimination beyond the null distribution." **Without that test, three below-chance AUCs would have been an embarrassing curiosity; with it, they are an interpretable null.** It appears in one short Results paragraph.

**9. No reporting guideline named, in a paper that out-performs most that name one.** This is now the fourth consecutive entry where checklist adherence and methodological care diverge: entry 69 named TRIPOD+AI and deposited the checklist; entry 70 named STROBE while being arguably more careful; entry 71 named none; entry 73 named none and called for an explainability checklist that does not exist. **This paper names none and does more of what TRIPOD+AI asks than any of them.** The pattern is now consistent enough to be worth stating as a rule: **the checklist is not the quality signal.**

**10. Credit for a sentence most papers would have omitted.** On SHAP: it was used "to describe model behaviour and the stability of learned feature contributions **rather than to infer independent, causal or clinically validated associations** with an increase in toxicity score related to radiotherapy." And: "explanations derived from poorly performing models may not reflect reproducible clinical associations." **That second clause is written in the Introduction — before any result is reported.** The authors anticipated the misreading of their own SHAP output and pre-empted it.

## 5. Statistics Spotlight

Ten techniques, numbered from 244 in the running list in `queue.md`. The first three are the load-bearing ones, and the first is the one this entire paper exists to demonstrate.

**A statistically significant AUC can be clinically worthless — and here is how to convert one into the only terms that matter.**

The GI models were **significantly** better than chance: permutation p-values of 0.036, 0.047 and 0.022. A reader who stops at "p < 0.05" concludes the models work. **Convert instead.**

**Step one: what AUC means.** An AUC is the probability that the model gives a higher score to a randomly chosen man who *will* develop toxicity than to a randomly chosen man who will not. A coin gets 0.5. **The best model here gets 0.587** — so if you line up one future-toxicity patient and one non-toxicity patient and ask the model which is which, it is right **58.7%** of the time instead of 50%.

**Step two: turn it into a probability a patient could act on.** With GI toxicity occurring in **46.7%** of this cohort, and taking the best corner of the reported ranges (sensitivity **0.658**, specificity **0.518**):

$$\text{PPV} = \frac{0.658 \times 0.467}{0.658 \times 0.467 + 0.482 \times 0.533} = \frac{0.3073}{0.5642} = 54.5\%$$

$$\text{NPV} = \frac{0.518 \times 0.533}{0.518 \times 0.533 + 0.342 \times 0.467} = \frac{0.2761}{0.4358} = 63.3\%$$

**So: before the test, this man had a 47% chance of bowel toxicity. The model says "high risk." Now he has a 55% chance. The model says "low risk." Now he has a 37% chance of toxicity instead of 53%.**

**Nothing you would do changes at either number.** You would not withhold curative radiotherapy from a man at 55% risk of a one-grade bowel symptom, and you would not relax your organ-sparing from a man at 37%. **The model is statistically real and clinically inert.**

**Step three, the sanity check: how much of the variation does it explain?** Using technique 224, **AUC 0.587 is about 2.4% of the variance** in who develops toxicity. The other 97.6% is elsewhere.

**The everyday version.** A weather service announces, after years of data, that it can predict rain tomorrow 58.7% of the time instead of 50%. The improvement is real and measurable. **You would still take the umbrella exactly as often as before**, because nothing in your decision turns on a swing from 47% to 55%. Significance says the effect exists; **magnitude says whether to care.**

**Watch out for:** a paper whose abstract reports a p-value for discrimination and no positive predictive value. Also note the specificity here — around **0.50**, meaning the model flags **half the men who will never develop toxicity.** **Always convert an AUC to the pre-test-to-post-test movement at the actual prevalence before deciding whether a model is useful.**

**A below-chance AUC: noise, or a signal with the wrong sign? The two-sided permutation test is how you tell.**

Three GU models came in **below 0.5**: 0.465, 0.455, 0.466. This looks like failure, and most papers treat it as a synonym for "no signal." **It is not — there are two genuinely different explanations, and distinguishing them matters.**

**Explanation one: sampling noise.** An AUC estimated from a finite sample wobbles around its true value. If the truth is exactly 0.5, roughly half your estimates land below it. Nothing is wrong and nothing is there.

**Explanation two: a real inverted relationship.** The model may have found genuine signal and attached the wrong sign — predicting high risk for the men who do well. **That would be a positive finding**, because a reliably inverted predictor is a predictor; you flip it and use it.

**How the paper distinguishes them, and this is the clever part.** One-sided permutation tests answer only "is performance *above* chance?" So the authors added **two-sided** tests "to determine whether performance differed from chance in either direction and to assess whether the observed inverse discrimination was greater than expected from sampling variation alone." The result: **p = 0.150 to 0.412.** Explanation one. **Noise.**

**Verify it yourself.** Under the null, an AUC's sampling standard deviation is approximately

$$SE = \sqrt{\frac{n_1 + n_2 + 1}{12\, n_1 n_2}}$$

With 126 GU events and 103 non-events, that is **0.0384**. The observed 0.455 sits **1.17 standard deviations** below 0.5, giving a two-sided p of about **0.24** — right inside the reported 0.150–0.412 range. **The arithmetic agrees: these are ordinary fluctuations.**

**The everyday version.** You flip a coin 20 times and get 8 heads. Is the coin biased toward tails? Maybe — or maybe that is what fair coins do one time in four. **You cannot tell from the direction; you have to ask how far a fair coin wanders.** The permutation test asks exactly that, using your own data and your own pipeline to define "wanders."

**Watch out for:** a below-chance AUC reported without a two-sided test, and the opposite error — treating a below-chance result as evidence of an inverted predictor without testing whether the inversion exceeds noise. **And note the asymmetry in what you may conclude:** here the null is informative *because* the study was powered for the effect size it was looking for, which is technique 250.

**Permutation testing that re-runs the entire pipeline — including hyperparameter selection.**

This is the methodological choice that makes the paper's p-values trustworthy, and it is almost never made.

**The shortcut.** Permute the outcome labels, refit your already-tuned model, record the AUC, repeat. Fast, and **wrong in a specific direction.**

**Why it is wrong.** Your reported AUC is not the output of one model — it is the output of **a procedure** that searched a hyperparameter grid, picked the best settings by inner cross-validation, and then evaluated. That search is itself a source of optimism: given enough settings to try, some will fit the training folds better by luck. **If your null distribution is built without the search, it is too narrow**, because it omits the very variance your real estimate contains. Narrow null, inflated significance.

**What this paper did.** For each of **1,000** permutations, "the complete repeated nested cross-validation pipeline was then repeated, **including inner-loop hyperparameter optimisation**, model fitting and generation of OOF predictions." So the null answers the right question: *how well does this whole procedure do when the labels mean nothing?*

**And here is the verification, which I find genuinely satisfying.** Compare the reported permutation p-values against the asymptotic formula, which assumes a single fixed model:

- L1, AUC 0.573 → 1.91 SD above 0.5 → asymptotic p **0.028**; reported **0.036**
- Elastic Net, AUC 0.571 → 1.85 SD → asymptotic p **0.032**; reported **0.047**
- XGBoost, AUC 0.587 → 2.27 SD → asymptotic p **0.012**; reported **0.022**

**Every reported p-value is larger than the formula predicts** — and that is precisely the signature of a null distribution correctly widened by model-selection variance. **If the reported values had been *smaller* than the asymptotic approximation, I would suspect the shortcut.** They are not. The permutation was done properly.

**The everyday version.** You want to know whether your talent-scouting system beats chance. **The shortcut:** take the scout you already decided was best, give him random player ratings, see how he does. **The honest version:** give random ratings to the *whole process* — hiring twelve scouts, auditioning them, picking the best — and see how well *that* does. The second null is wider, because part of your real success was the luck of picking a scout who happened to look good on the audition data.

**Watch out for:** "permutation testing confirmed above-chance performance" with no statement of what was permuted and what was re-run. **The question to ask is: was the hyperparameter search inside the permutation loop?** If not, the p-value is optimistic by an unstated amount.

**247. Select the operating threshold on training data only.** Sensitivity and specificity depend on where you cut the probability. This paper computed Youden's J from inner-CV predictions on the outer **training** set, fixed it, and applied it to the unseen test fold. **Entry 70 of this list selected its Youden point on the pooled out-of-fold predictions it then reported** — tuning the operating point on the same numbers used to report performance, which inflates the sensitivity/specificity pair while leaving the AUC untouched. **This is the correct procedure and it is the fix for technique 212.** When a paper reports a Youden-optimal sensitivity and specificity, ask which data chose the threshold.

**248. Out-of-fold SHAP.** We accept without argument that performance must be measured on held-out data. **The same applies to explanations.** SHAP computed on training data tells you which features the model leaned on *in the data it had already seen* — which can be driven by the same overfitting the held-out evaluation exists to detect. This paper calculated SHAP "within each outer validation fold" and retained values **only for patients in the corresponding unseen test fold.** **If a paper's feature-importance analysis was computed on the full dataset or the training set, it is the explanation equivalent of reporting training accuracy.** Ask.

**249. A stable, correct, biologically true explanation can sit on a useless model.** Rectal EUD: **first-ranked in every repeat, across all three models**, correct sign, established mechanism. Model AUC: **0.587.** **Explanation quality and model utility are independent dimensions**, and this paper is the cleanest demonstration available. The practical consequence: **a convincing feature-importance plot is not evidence that a model discriminates, and a model that discriminates well need not have a tidy explanation.** Check them separately, always. Yesterday's entry 73 argued this; today's entry proves it.

**250. Check reported p-values against the asymptotic null, and check what the study could have detected.** Two cheap arithmetic moves. First, the Hanley–McNeil null SE above lets you ask whether a reported p is plausible for the sample size — and in which direction it deviates, which is diagnostic. Second, **minimum detectable effect** (technique 204): with these sample sizes, 80% power at one-sided α = .05 requires an AUC of about **0.595**. The observed GI value of **0.587** sits just below that threshold, **which is exactly why its p-values are 0.022–0.047 rather than anything smaller.** And the crucial contrast with entry 70: there, three underpowered nulls risked being miscited as "no effect." **Here the study's conclusion also says "limited or no useful discrimination" — which is precisely what a study powered to detect 0.60 is entitled to say when it finds 0.587 and 0.465. The claim and the power match.**

**251. Equivalent uniform dose as a principled answer to collinearity.** Dose–volume histogram parameters — V50, V60, V70, mean dose, max dose — are different summaries of one curve and are heavily inter-correlated. Feed them all to a model and attribution smears across them arbitrarily (technique 236). This paper collapsed them into **organ-specific EUD** via the Niemierko formulation with literature-derived parameters, "reducing correlation between individual dose–volume histogram parameters while retaining information on the uniform dose distribution." **The general lesson: when several of your predictors are transformations of one underlying measurement, combine them using domain knowledge before modelling** — rather than relying on regularisation to sort it out afterwards, which it does arbitrarily.

**252. Baseline-corrected endpoints: what they fix, and what they cost.** Defining toxicity as a **one-grade increase from each patient's own baseline** fixes a real problem: a man with pre-existing urinary symptoms should not be counted as harmed by radiotherapy for symptoms he already had. **The cost is that the endpoint becomes sensitive to mild change** — event rates of 46.7% and 55% here, against far lower conventional Grade ≥2 rates. **So this study's null is about predicting *any* worsening, not about predicting the severe toxicity a clinician would change a plan for.** Both are legitimate endpoints; they are different questions, and a near-null on the first does not establish a near-null on the second.

**253. Complete-case analysis without a parent denominator.** 229 men "with a complete record" of baseline, treatment, dosimetric and longitudinal toxicity data, from a prospective multicentre cohort of unstated size. **Zero missing data is a genuine analytic advantage — no imputation assumptions enter at all — and it is purchased by a selection you cannot inspect.** Complete dosimetry plus four follow-up visits across 48 months plausibly favours better-resourced centres and healthier attenders. **The fix is one sentence: how many were enrolled, how many analysed, and how did they differ?** This is technique 240 from yesterday, arriving in a primary study rather than a review.

## 6. Jargon Translator

**Radiotherapy / external beam radiotherapy** — treating cancer with targeted radiation from outside the body. For localised prostate cancer it is a curative option alongside surgery.

**Late toxicity** — side effects that persist or appear long after treatment, here at least 12 months out, as distinct from the acute effects during and just after radiotherapy.

**GI and GU toxicity** — gastrointestinal (bowel: urgency, bleeding, frequency) and genitourinary (bladder and urethra: frequency, urgency, obstruction). Different organs, different mechanisms, which is why the paper modelled them separately.

**CTCAE** — the standard scale for grading side-effect severity, 1 (mild) to 5 (death). **Grade ≥2 is the usual threshold for "clinically meaningful"; this study used a one-grade increase from each patient's own baseline instead**, which is more sensitive and less specific to serious harm.

**Dose–volume histogram (DVH)** — a curve showing how much of an organ received how much radiation. Its summary numbers (V50, V70, mean dose) are all descriptions of the same curve, hence heavily correlated.

**Equivalent uniform dose (EUD)** — one number standing in for a whole non-uniform dose distribution: the uniform dose that would produce the same biological effect. Collapses a correlated set of DVH parameters into a single principled summary.

**Organ at risk / PTV** — a healthy structure you try to spare, and the planning target volume, the region deliberately irradiated with a margin for movement and setup error.

**Normal tissue complication probability (NTCP) model** — the classical dose-only approach to predicting side effects, which this study's machine learning was meant to improve on by adding clinical variables.

**TURP / bladder TUR** — transurethral resection of the prostate or of a bladder tumour: prior procedures through the urethra that might plausibly affect later urinary toxicity. Both contributed little here.

**L1-regularised logistic regression / Elastic Net** — regression that shrinks weak predictors' coefficients toward or exactly to zero, so it fits and selects simultaneously. Interpretable by construction.

**XGBoost** — gradient-boosted decision trees: sequential trees each correcting the last one's errors. Flexible, non-linear, and a black box without added explanation.

**Nested cross-validation** — two loops. The inner one chooses settings; the outer one measures performance on data the inner loop never saw. Without the nesting, tuning on the data you evaluate on inflates the result.

**Out-of-fold prediction** — a prediction for a patient made by a model that never trained on that patient. The only kind that estimates real-world performance.

**Stratified folds** — splits that preserve the outcome proportion in each fold, so no fold ends up with too few events.

**ROC-AUC** — the probability the model scores a true case above a true non-case. 0.5 is a coin flip; **below 0.5 means worse than a coin, which is what technique 245 is about.**

**Youden's J** — sensitivity + specificity − 1. Maximising it picks the "best balance" cut-point; **which data you maximise it on determines whether the resulting numbers are honest.**

**Bootstrap confidence interval** — resample your own patients with replacement, recompute, repeat, and read off the middle 95%. Here 2,000 resamples at patient level, preserving each sampled patient's full set of predictions.

**Permutation test** — shuffle the outcome labels, redo the analysis, repeat, and build a picture of what chance looks like. **The decisive detail is how much of the analysis you redo** — technique 246.

**SHAP** — assigns each predictor a share of credit for a prediction. **A statement about the model, not about the disease** (technique 236).

**Calibration** — whether predicted probabilities match observed rates. **Not assessed in this paper at all.**

## 7. What You Can (and Can't) Say

**You can say:**

"In 229 men from the prospective REQUITE cohort, machine-learning models using routine clinical variables and whole-organ radiation dose summaries achieved areas under the curve of 0.573 to 0.587 for late bowel toxicity — above chance on permutation testing, but far too weak for individual risk prediction."

"For late urinary toxicity the same approach showed no discrimination at all; the models came in below chance, and two-sided permutation testing confirmed that this was sampling noise rather than an inverted signal."

"Rectal equivalent uniform dose was the top-ranked predictor in every cross-validation repeat across all three models, with higher dose raising predicted risk — consistent with established radiobiology."

"The authors conclude that conventional clinical and dosimetric variables are unlikely to capture the variation in late toxicity, and point toward substructure dosimetry and patient-specific biological markers."

"The study demonstrates that a stable, biologically plausible feature-importance ranking can coexist with a model that cannot usefully discriminate."

**You cannot say:**

"Machine learning predicts radiotherapy side effects." Not from this. **AUC 0.587 moves a man from a 47% to a 55% chance** — the paper's own word is "limited."

"The model works for bowel toxicity but not urinary." It is statistically above chance for bowel and clinically unusable for both. The honest split is "a tiny real signal" versus "no signal."

"Rectal dose predicts bowel toxicity, so this model is validated." **That is the precise inference the paper exists to block.** Rectal dose matters biologically and is the model's top feature; the model still does not discriminate.

"Previous studies got AUCs of 0.8, so this one must have done something wrong." The reverse reading is at least as likely: this analysis used nested cross-validation, out-of-fold evaluation, patient-level bootstrapping and full-pipeline permutation testing specifically "to reduce optimistic estimates."

"Radiotherapy toxicity is unpredictable." The study shows that **these variables, in this cohort, with this endpoint** carry little information. The authors note that genomic susceptibility has shown predictive value for selected late endpoints.

"Half of men get lasting bowel problems after prostate radiotherapy." The 46.7% figure is **any one-grade CTCAE increase from that man's own baseline** at 12 months or beyond — a far lower bar than conventional Grade ≥2 reporting.

"The findings apply to other centres." **Validation was internal to this cohort**, and the authors say so.

"The model's probabilities are reliable." **Calibration was never assessed.**

**The honest one-sentence version:** *five researchers took 229 men from a prospective multicentre cohort, applied three models to the clinical and dose data every radiotherapy department already holds, validated them about as carefully as this list has ever seen — nested cross-validation, out-of-fold predictions and SHAP, patient-level bootstrapping, and permutation testing that re-ran the entire pipeline a thousand times — and reported honestly that the answer is roughly 2% of the variance for bowel toxicity and nothing at all for urinary, while demonstrating along the way that a perfectly stable and biologically correct explanation can sit on top of a model nobody should use.*

## 8. Bottom Line for Your Life

**If you are having or have had prostate radiotherapy:** nothing here changes your treatment, and the useful message is reassuring in an odd way. **Nobody can currently tell you in advance whether you will get lasting bowel or urinary side effects** from your clinical details and dose plan — and this study is the careful demonstration of that, not a failure to look. What *does* work is the thing your team already does: keeping the dose to your rectum and bladder as low as the treatment allows. **Rectal dose was the one variable that mattered consistently**, which is exactly why planning effort goes there.

**If you are a radiation oncologist or physicist:** the actionable finding is the GU one, and it is a measurement hypothesis rather than a dead end. **Whole-bladder EUD showed nothing**, and the authors name the likely reason — "dose to urinary substructures, such as the bladder neck and urethra, which may be more relevant to individual GU symptoms." **If you are contouring whole bladder for toxicity modelling, this study is an argument for substructure dosimetry instead.** For GI, rectal EUD behaved exactly as radiobiology predicts and still did not deliver individual risk stratification.

**If you build or review clinical prediction models:** this is the paper to copy, and five specific habits are worth lifting. **Run the hyperparameter search inside the permutation loop.** **Choose your operating threshold on training data only.** **Compute SHAP out-of-fold.** **Quantify feature-rank stability across repeats**, not just once. And **report the result you got** — the abstract's own highlight reads "GU models showed no evidence of discrimination beyond chance," which is a sentence most papers would have found a way around.

**If you read AI-in-medicine claims:** take one conversion away from this entry. **When a paper reports a significant AUC, work out what it does to a patient's probability.** Here: 47% to 55% on a positive, 53% to 63% on a negative. Four percentages and a pocket calculator tell you more about whether a model is useful than any p-value will. **Significance says the effect exists; magnitude says whether to care.**

**And one for anyone reading feature-importance plots:** the most quoted number in this paper will be that rectal dose ranked first every single time. **It did, and the model is still not usable.** A tidy explanation is evidence about the explanation.

**This is education, not medical advice.** Nothing here should change anyone's cancer treatment or radiotherapy plan. If something in this paper bears on your own care, that is a conversation with your oncologist.

---

## Appendix: shelf, deferred papers, status on 2026-11-11

**Landmark check for the past week.** According to PubMed, five records, four previously assessed. The one new entry is **"Deep learning-based gait analysis predicts multisystem health phenotypes"** (PMID 43003904, [DOI](https://doi.org/10.1038/s41591-026-04725-8), *Nature Medicine*, 9 November 2026) — **no abstract, no author list, and a DOI one digit from the gait foundation model already on the deferred list** (`...04725-8` against `...04724-9`). That pattern identifies it as the journal's accompanying commentary or research briefing rather than a primary study, **so it does not displace the queue.** It does tell us the journal is giving the gait paper prominence, which strengthens the case for decoding the primary article once a full text is reachable.

**Shelf status: five spares remain** after today, in the order set on 2026-11-10 — **(B)** bone-tumour review arguing reference-standard instability is the binding constraint (PMID 42997475, PMC13742044); **(C)** diabetic retinopathy at AUROC 0.972 from eight routine labs, shelved for a sceptical reading because two predictors are the other microvascular complications (42974596, PMC13727297); **(D)** glaucoma visual-field prediction with external validation on two different OCT devices (42997014, PMC13740841); **(E)** MIBC pathological complete response with 102 models screened and a calibration-slope CI of 0.469–1.639 (42997524, PMC13741961); **(F)** bitewing positioning errors trained entirely on mannequins (42981213, PMC13734376).

**Next run takes shelf item (C)**, the diabetic retinopathy model — because today's entry supplies the perfect contrast. **This paper reports AUC 0.587 and ~2.4% of variance after validating as hard as anyone in this list; (C) reports AUROC 0.972, which technique 224 converts to roughly 80% of variance, from eight routine laboratory values.** Two of those eight predictors are nephropathy and neuropathy — the other two microvascular complications of diabetes, routinely coded alongside retinopathy. **Read side by side, the pair is the clearest available lesson in what validation rigour does to a reported number**, and the first question for (C) is whether its headline survives the question "could the label be inside the inputs?"

**Deferred papers — four, all re-checked today.** **Gait foundation model**, *Nature Medicine* (PMID 42995231, [DOI](https://doi.org/10.1038/s41591-026-04724-9)) — **day 3**, no PMC copy, abstract-only date **2026-11-30**. **Nature personal health agent** (PMID 42907512, [DOI](https://doi.org/10.1038/s41586-026-11161-8)) — **day 22**, weekly re-check, next 2026-11-12. **BMJ review of LLM-trial reporting completeness** (PMID 42869550, [DOI](https://doi.org/10.1136/bmj-2026-100855)) — **day 29, and its twenty-one-day threshold fires tomorrow, 2026-11-12, when it takes priority** under the standing rule if its PMC body is still empty. Today's entry adds a fourth consecutive data point to the pattern that review quantifies: **this paper names no reporting guideline while doing more of what TRIPOD+AI asks than any of entries 69, 70, 71 or 73.** ***Annals* *Choosing Wisely*** (PMID 42896192, [DOI](https://doi.org/10.7326/ANNALS-26-01667)) — **day 22**, weekly re-check, abstract-only date 2026-11-19.

**Watch item:** PM Heart trial results (protocol PMID 42893738), quarterly.
