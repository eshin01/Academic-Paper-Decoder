# Predictive model for acute kidney injury in critical patients with pulmonary embolism based on machine learning: A multicenter clinical study

**Authors:** Zhang P (Nephrology and Rheumatology, Tongde Hospital of Zhejiang Province, Hangzhou), Zhang Q (Rheumatology and Immunology, Second Affiliated Hospital of Zhejiang Chinese Medical University; Rheumatology and Chinese Medicine, 962nd Hospital of the PLA, Harbin), Wang S (Tongde Hospital of Zhejiang Province), Shen J, Chen J (Respiratory and Critical Care Medicine, 962nd Hospital of the PLA), Zhao X (Infectious Diseases, 962nd Hospital of the PLA), Zhao S (Respiratory and Critical Care Medicine, 962nd Hospital of the PLA) — 7 authors, China
**Journal:** Medicine (Baltimore), 2026; 105(46): e51017 (published 2026-11-13)
**Decoded:** 2026-11-21

**Analysis basis:** **FULL TEXT** (retrieved from PubMed Central, PMC13773385). Introduction, all Methods including study population, external validation, the PE and AKI definitions, covariate collection, the sample-size estimate and the statistical plan; all Results including baseline characteristics, feature selection, model evaluation, model interpretation, the web calculator and the PESI comparison; and the complete Discussion with its limitations and conclusions. **All three main tables came through intact** — the baseline table, the eight-model performance table across all three datasets, and the PESI comparison — so every number below is verified against the paper's own tables. **All figures are unreachable** (Figures 1–6), as are Supplemental Digital Content 1–11, which costs the participant flow diagram, the LASSO trajectories, the ROC/calibration/decision curves, the SHAP plots, the per-set model metrics tables and the hyperparameter table.

**Source links (verified):**
- DOI: https://doi.org/10.1097/MD.0000000000051017
- PubMed: https://pubmed.ncbi.nlm.nih.gov/43024281/
- Full text used: https://pmc.ncbi.nlm.nih.gov/articles/PMC13773385/

**Basis of link verification.** Direct URL fetching is blocked from this session (`doi.org` does not resolve under the network policy here), so verification was done against the live PubMed/NLM record. According to PubMed, a query for PMID 43024281 returned this exact title, these seven authors with these affiliations, *Medicine (Baltimore)* volume 105 issue 46 article e51017, DOI `10.1097/MD.0000000000051017`, and MeSH terms including Pulmonary Embolism, Acute Kidney Injury, Machine Learning and Severity of Illness Index; a PMID-to-PMCID conversion returned **PMC13773385**; and the full text was then retrieved from PubMed Central by that PMC ID and matches the record. Both halves of the chain were confirmed independently.

**Funding: NOT REPORTED.** No funding statement appears anywhere in the retrieved text.
**Conflicts of interest: NOT REPORTED.** No competing-interests statement appears anywhere in the retrieved text. Author contributions are given in full.
**Ethics:** approval and informed consent were **waived**, stated and justified — both databases are retrospective and de-identified. MIMIC-IV access was granted to a certified team member (**record ID 72870037**).
**Reporting guidelines: STROBE and TRIPOD are explicitly claimed.** The paper states that "Risk-factor selection adhered to the Strengthening the Reporting of Observational Studies in Epidemiology and Transparent Reporting of a multivariable prediction model for Individual Prognosis Or Diagnosis guidelines." **Section 4 records why this is the most striking claim in the entry.**
**A public web calculator is deployed.** The paper gives its address as `https://shareapp-2026-pe-aki.streamlit.app/`. **I am reporting that address as the paper states it; I could not reach it from this session and am not asserting that it resolves.**

---

## 1. The Gist

**Seven researchers in China built a tool that tries to predict which critically ill patients with a blood clot in the lungs will go on to suffer kidney failure. They trained it on one American ICU database, tested it on a second, got a respectable-looking score, and put a free calculator on the internet. The score is real. The tool, at the setting it actually runs at, misses about two-thirds of the patients it is supposed to catch — and the paper never says so.**

Start with the clinical problem, which is genuine. A **pulmonary embolism** is a blood clot that travels to the lungs. The paper notes it is the **third most common fatal cardiovascular disease worldwide**, after heart attack and stroke. When it is severe, the heart struggles to push blood through the blocked lungs, blood pressure falls, and the kidneys — which are extremely sensitive to blood flow — can fail. That kidney failure is called **acute kidney injury (AKI)**, and it makes everything worse. So a tool that flags who is heading for kidney failure, early, would be useful.

**What they did.** They used two large, free, de-identified American intensive-care databases. **MIMIC-IV** (one Boston hospital, 2008–2019) supplied **2,187 patients** for building and internally checking the model. **eICU** (208 US hospitals, 2014–2015) supplied **2,183 patients** for an **external check** — testing the model on data it had never seen, from completely different hospitals. **That external step is genuinely good practice and most papers in this reading list do not do it.**

They screened **58 candidate variables**, narrowed to **20**, then to **10 final predictors**: high blood pressure, heart failure, pneumonia, sepsis, being on a ventilator, breathing rate, LDL cholesterol, blood oxygen level, lactate, and a severity score called **OASIS**. They then trained **eight different algorithms** and picked the best.

**The headline results.** The winner was **XGBoost**, a gradient-boosting model. Its ability to rank patients by risk — measured as **AUROC**, where 0.5 is a coin flip — was **0.825** on the training data, **0.771** on the internal check, and **0.757** on the external check. **That transportability is decent.** A drop of only 0.014 crossing from one database to another is better than several papers in this list managed.

**And now the problem, which is in the paper's own table.**

**An AUROC measures ranking across every possible cut-off. A deployed calculator uses one cut-off.** And at the cut-off this model actually uses, in the external validation, **its sensitivity was 0.345.**

**That means it caught 345 out of every 1,000 patients who developed kidney injury, and missed the other 655.** In absolute numbers: of **1,185 patients with AKI** in the external database, the model flagged about **409** and **missed about 776**. It raised an alarm on only **499 of 2,183 patients** in total.

**And it was not always like that.** In the internal check, sensitivity was **0.746** — catching about three-quarters. **Crossing to the second database, sensitivity fell from 74.6% to 34.5%, a collapse of more than half, while specificity rose from 62.7% to 91.0%.** The model became far more reluctant to call anyone high-risk.

**Why? Because the two databases disagree about how common kidney injury is.** In MIMIC-IV, **78.88%** of these patients had AKI. In eICU, **54.28%**. **That is a 24.6 percentage-point gap.** A probability threshold tuned where four in five patients have the outcome will fire far less often where only half do. **The ranking transported. The decision rule did not.** The paper reports both sets of numbers in adjacent rows of the same table and never connects them.

**Second problem, and this one undermines the model's own explanation of itself.** The paper reports that **LDL cholesterol** was one of the three variables contributing most to predicted risk. But look at the paper's own baseline table: LDL in patients who developed AKI was **81.41 mg/dL**, and in those who did not, **81.31 mg/dL** — **a difference of one-tenth of one unit, with P = 0.532**, meaning no detectable association at all. Total cholesterol (P = 0.608), triglycerides (P = 0.899) and HDL (P = 0.156) were all equally null.

**A variable whose two group medians differ by 0.1 mg/dL cannot credibly be the second-biggest driver of a risk prediction.** And there is a likely explanation visible in the same table: **the lipid values are distributed far too narrowly for 2,187 intensive-care patients.** LDL ranges across the middle half of patients from only 72.2 to 92.6 mg/dL; HDL from 37.3 to 45.2. Real lipid panels in critically ill people scatter much more widely. **A tight cluster hugging the median is the classic fingerprint of a variable that was mostly missing and filled in with the average** — and a cholesterol panel is not something anyone routinely draws on a patient with a life-threatening lung clot. **The paper reports no missing data anywhere: no counts, no patterns, no imputation method, not one sentence.**

**Third, I found two errors in the paper's own performance table, and one of them is in the headline model's row.** Accuracy, precision and F1 are not independent numbers — you can rebuild all three from sensitivity, specificity and how common the outcome is. **I did that for all eight models in the external validation. Six of the eight reconcile exactly.** Two do not. **The winning XGBoost model's F1 score is printed as 0.456; from its own sensitivity and specificity it must be 0.486.** And the LightGBM row is printed with **exactly the same sensitivity and specificity as XGBoost** yet a different accuracy and precision — **which is arithmetically impossible**, since accuracy depends only on those three quantities. Solving backwards, LightGBM's accuracy, precision and F1 are all consistent with a sensitivity of about **0.300**, not the printed 0.345 — **so its sensitivity appears to have been copied from the row above.**

**Fourth, the comparison the paper makes is against the wrong thing, and the right comparison is sitting in its own table.** The paper benchmarks itself against **PESI**, the Pulmonary Embolism Severity Index — **a score designed to predict death within 30 days, not kidney injury.** Beating a mortality score at predicting kidney failure is close to meaningless. Meanwhile, in the eight-model table, **plain old logistic regression scored 0.741 externally against XGBoost's 0.757** — a gap of 0.016, with overlapping confidence intervals. **So the sophisticated model barely beats the simple one where it counts.** Notice where it does win: on the training data, 0.825 against 0.748. **The fancy model's advantage is largest where it was fitted and nearly gone where it was tested.**

**And a detail that complicates the top predictor.** The single most influential variable was **OASIS**, a severity score. **One of OASIS's ten components is urine output.** And one of the two official criteria for diagnosing AKI is **low urine output**. So the strongest predictor shares a component with the thing being predicted. On top of that, **being on a ventilator and breathing rate are each counted twice** — once inside OASIS and again as standalone predictors in the same ten-variable model.

**What this paper is.** A real external validation — which deserves credit — wrapped around a model whose deployed decision rule misses most of the cases it exists to find, whose own explanation names a variable with no association to the outcome, whose performance table contains arithmetic that does not close, and which has been published as a public calculator with no calibration statistics reported at all. **The clinical question is worth asking. This answer is not yet usable.**

## 2. Study Snapshot

**Study type:** retrospective analysis of two public critical-care databases, developing a prediction model with internal and **external** validation. **The title calls it a "multicenter clinical study." It is neither a clinical study nor meaningfully two centres** — MIMIC-IV is one Boston hospital and eICU is 208 hospitals, which the paper itself states, yet the abstract describes "2 centers."

**Development data.** **MIMIC-IV**, from Beth Israel Deaconess Medical Center and MIT, covering more than 70,000 critical patients admitted **2008–2019**. **2,580** first-admission ICU patients with critical PE were screened; **393 with chronic kidney disease were excluded**; **2,187** were enrolled — which I verified reconciles exactly (2,580 − 393 = 2,187). Median age **66**, **1,099 female (50.25%)** and **1,088 male (49.75%)**.

**External validation data.** **eICU-CRD v2.0**, from Philips Healthcare and MIT: **139,367 patients, 200,859 ICU admissions, 208 US hospitals, 2014–2015**. PE identified by ICD codes, **n = 2,183**, with "identical inclusion and exclusion criteria."

**How PE was defined.** ICD-9 codes in the **415** category and ICD-10 code **I26**.

**How AKI was defined.** **KDIGO 2012 criteria**, requiring **either** a rise in serum creatinine of 0.3 mg/dL or more within 48 hours, or 50% or more above baseline within 7 days, **or a urine output below 0.5 mL/kg per hour for 6 hours or more.** Staging was reported: in MIMIC-IV, **no AKI 462 (21.12%), stage I 354 (16.19%), stage II 898 (41.06%), stage III 473 (21.63%)** — which I verified sums to 2,187, with stages I–III summing exactly to the 1,725 AKI cases. **72 patients (3.29%) received continuous renal replacement therapy.**

**The outcome rates, and the gap that matters.** **MIMIC-IV: 1,725 of 2,187 had AKI — 78.88%.** **eICU: 1,185 of 2,183 — 54.28%.** Both verified. **A gap of 24.6 percentage points.** For context the paper supplies itself: a RIETE-registry study of **30,532 patients with acute PE found 26% with AKI at baseline** — so the development cohort's rate is **about three times** the figure in the literature the paper cites.

**Covariates.** Extracted by PostgreSQL, **restricted to the first 24 hours of ICU admission**, covering demographics, comorbidities, vital signs, laboratory values, severity scores and interventions.

**Sample size.** The paper states that with an AKI prevalence of **77.67%** (taken from another study), 10 variables and an R² of 0.30, the minimum required sample was **264**, giving **20.59 events per parameter**. I verified that 264 × 0.7767 ÷ 10 = 20.50, so the figure describes **the minimum, not the actual sample** — which had 1,725 events and therefore 172.5 events per parameter.

**Analysis.** MIMIC-IV **randomly split 70% training / 30% internal validation**; eICU external. Variable selection by **LASSO plus multivariable logistic regression**, with "core predictors identified after 500 bootstrap iterations with Bonferroni correction." **58 candidates were screened; 20 retained with non-zero coefficients after 500 iterations of 10-fold cross-validation; 10 selected by multivariable logistic regression.** Eight models built: decision tree, K-nearest neighbours, LightGBM, logistic regression, naïve Bayes, random forest, support vector machine and XGBoost. Evaluated by ROC curves, calibration analysis and **decision curve analysis**. SHAP for feature importance. **NRI and IDI against PESI.** Software R v4.4.2 and DCPM v6.12.4.

**The ten final predictors.** Hypertension, heart failure, pneumonia, sepsis, ventilation, respiratory rate, partial pressure of oxygen, **LDL cholesterol**, lactate, and **OASIS** (Oxford Acute Severity of Illness Score).

**Discrimination.** **XGBoost: training AUROC 0.825 (95% CI 0.800–0.850), internal validation 0.771 (0.728–0.814), external validation 0.757 (0.737–0.777).** Train-to-internal drop **0.054**; internal-to-external drop **0.014**.

**The full external-validation metrics for XGBoost, which the paper prints and does not discuss.** **Sensitivity 0.345. Specificity 0.910. Accuracy 0.603. Precision 0.820. F1 0.456. Kappa 0.242. Brier score 0.206. PRAUC 0.433.** For comparison, internal validation: **sensitivity 0.746, specificity 0.627, Brier 0.137.**

**The other seven models externally**, by AUROC: logistic regression **0.741 (0.720–0.762)**, random forest **0.716**, naïve Bayes **0.710**, LightGBM **0.702**, support vector machine **0.687**, K-nearest neighbours **0.681**, decision tree **0.667**.

**Calibration.** Reported only qualitatively: calibration plots "approximated the diagonal, indicating close agreement between predicted and observed probabilities." **Brier scores are given. No calibration slope, no calibration-in-the-large, no observed-to-expected ratio is reported anywhere** — for any model, on any dataset.

**Clinical utility.** Decision curve analysis "demonstrated a higher net benefit than both the treat-all and treat-none strategies," in an unreachable figure.

**Interpretation.** SHAP identified **OASIS as the dominant predictor**, with **partial pressure of oxygen** and **LDL cholesterol** also substantial. Two worked examples are given: for a positive case, PO₂ of 72.8 mm Hg contributed +1.5 units and OASIS of 36 contributed +0.79; for a negative case, PO₂ of 134 mm Hg contributed −0.862 and OASIS of 19 contributed −0.783.

**The PESI comparison.** "Model 1" is described as a **nomogram score** built from the ten variables; "Model 2" is PESI. Model 1 beat PESI on AUROC in training (**0.748 vs 0.702**), internal validation (**0.756 vs 0.713**) and external validation (**0.754 vs 0.708**). **NRI 0.223 / 0.355 / 0.274** and **IDI 0.041 / 0.069 / 0.061** across the three sets, all P < .001.

**The calculator.** "An open-access web calculator was subsequently developed to estimate the probability of AKI in critical PE," which "returns individualized AKI probabilities." The paper gives the address as `https://shareapp-2026-pe-aki.streamlit.app/`.

**Limitations the authors state, in full, and there are only two:** "the absence of a large-scale nationwide epidemiological survey and the lack of repeated sampling for trajectory modeling."

**Not reported or not retrievable:** **any missing-data count, pattern or imputation method** — nothing at all; **any calibration slope, intercept or O:E ratio**; **the fitted model itself** (no coefficients, no nomogram points, so no reader can compute a prediction by hand); **whether LASSO ran on the 70% training split or on all 2,187 MIMIC patients**; **any hospital-level grouping within eICU's 208 hospitals**; **funding**; **conflicts of interest**; the proportion of AKI events occurring within the first 24 hours; and all figures and all eleven supplemental files.

## 3. How Strong Is This Evidence? (Grade 2 out of 5)

**The external validation is real and deserves credit. Almost everything built on top of it does not hold up: the deployed model misses most of the cases it exists to catch, its own top-three explanation names a variable with no association to the outcome, its performance table contains arithmetic that does not close, and a public probability calculator has been released with no calibration statistics of any kind.**

**What is genuinely worth crediting, because it is not nothing.**

**A true external validation on a separate database.** Development in MIMIC-IV and testing in eICU — different hospitals, different years, different documentation culture. This is technique 284's cross-database transportability test, and **most entries in this reading list do not attempt it.** It was the reason this paper was chosen.

**And the transportability of the ranking is decent.** AUROC fell only **0.014** from internal (0.771) to external (0.757). Compare entry 78, where moving to a second scanner brand produced non-overlapping confidence intervals. **Here the ranking genuinely held up.**

**Full performance metrics for all eight models on all three datasets.** Nine metrics each, including PRAUC, Kappa and Brier. **This is the paper's single best decision, and it is what made every criticism below possible** — including finding the arithmetic errors. A paper reporting only AUROC would have concealed the sensitivity collapse entirely.

**Decision curve analysis**, AKI staging reported, the CKD exclusion stated and counted, the MIMIC access record ID given, ethics properly justified, author contributions in full, and the calculator's address published rather than promised.

**So why 2.**

**The deployed decision rule misses about two-thirds of cases, and the paper does not mention it.** External sensitivity **0.345**. Of 1,185 patients with AKI, roughly **776 go unflagged**. The paper's stated purpose is "early recognition of high-risk individuals"; **a tool that misses 65.5% of them does not serve that purpose**, and the abstract instead describes the model as showing "the most stable discrimination, calibration, and clinical benefit."

**Sensitivity collapsed from 0.746 to 0.345 crossing databases, and this was predictable.** Prevalence fell from **78.88% to 54.28%**. A probability cut-off chosen where four in five patients have the outcome will classify far fewer as positive where only half do — which is exactly what happened, with specificity rising from 0.627 to 0.910 in compensation. **The ranking transported; the operating point did not. Both numbers are printed in the same table, in adjacent blocks, and never compared.**

**The 24.6-point prevalence gap is itself unexplained, and the likely explanation threatens the validation.** KDIGO AKI requires creatinine **or** urine output. **Yesterday's entry established, from a paper using the same eICU database, that urine output is available in only about 51.5% of eICU encounters.** If AKI by the urine criterion cannot be ascertained for much of eICU, then **the outcome is not the same variable in the two cohorts** — and an external validation against a differently-ascertained label is measuring something other than transportability. The paper does not raise this. It also does not reconcile its 78.88% against the **26%** in the RIETE registry it cites in its own introduction.

**LDL cholesterol is reported as a top-three contributor and has no univariate association with the outcome.** Medians **81.41 vs 81.31 mg/dL**, **P = 0.532**. Total cholesterol, triglycerides and HDL are all equally null. **This is not a subtle inconsistency; the two groups' medians differ by one-tenth of one unit.** And the lipid distributions are implausibly narrow for 2,187 ICU patients — LDL's middle half spanning just 72.2 to 92.6 — which is **the signature of a mostly-missing variable filled in with the average.**

**No missing-data reporting whatsoever.** Not a count, not a pattern, not an imputation method, for a study that screened **58 candidate variables** including lipid panels, coagulation studies and arterial blood gases out of ICU databases. **This is the single largest reporting gap**, and it is what makes the LDL finding uninterpretable rather than merely odd.

**No calibration slope, intercept or observed-to-expected ratio — while shipping a probability calculator.** The calculator "returns individualized AKI probabilities." Calibration is asserted qualitatively ("approximated the diagonal") with Brier scores as the only quantitative support, **and the external Brier was 0.206 against 0.137 internally — 50% worse.** Set this against yesterday's entry, which reported a calibration slope of **1.011 with a 95% interval of 0.970–1.055**. **Here a probability-producing public tool is released with no equivalent number at all**, across a 24.6-point prevalence shift.

**Two arithmetic inconsistencies in the performance table, one in the winning model's row.** Six of eight external rows reconcile exactly from sensitivity, specificity and prevalence. **XGBoost's F1 is printed as 0.456 and must be 0.486.** **LightGBM is printed with sensitivity and specificity identical to XGBoost's but a different accuracy and precision, which is impossible** — its three derived metrics are all consistent with a sensitivity near **0.300**, suggesting the printed value was copied from the row above.

**The comparator is a mortality score, and the comparator that matters is in the paper's own table.** **PESI predicts 30-day death, not kidney injury.** Beating it at AKI prediction establishes very little. Meanwhile **logistic regression reached 0.741 externally against XGBoost's 0.757** — a 0.016 gap with overlapping intervals — while on training data the gap was **0.077**. **The gradient-boosting advantage is largest where the model was fitted and nearly absent where it was tested**, which is the signature of the complexity buying optimism rather than signal (technique 273).

**And the PESI comparison uses a different model from the headline.** "Model 1" is a **nomogram** with AUROCs of 0.748 / 0.756 / 0.754 — which match the **logistic regression** row, not XGBoost's 0.825 / 0.771 / 0.757. **So the NRI and IDI improvements belong to the nomogram while the headline AUROC belongs to XGBoost, and the switch is never flagged.**

**The top predictor shares a component with the outcome.** **OASIS includes urine output**; **low urine output is one of the two KDIGO criteria for AKI.** Also **ventilation and respiratory rate are each counted twice**, once within OASIS and again as standalone predictors.

**Detection and prediction cannot be separated.** Predictors come from the **first 24 hours**; the outcome is "AKI occurring during ICU admission" under windows of 48 hours and 7 days. **AKI arising within that same first 24 hours is not excluded**, and there is no index date, no washout and no incident-only definition — entry 77's defect exactly (technique 277). Supporting signs sit in the baseline table: **serum creatinine itself differs significantly (0.80 vs 0.90, P < .001)**, and creatinine *is* the AKI definition. It was not retained among the final ten, which helps, but the ambiguity is unresolved.

**No hospital-level grouping in eICU**, whose 208 hospitals are treated as a single "center" — the check yesterday's entry performed and which showed absolute AUROC swinging 0.091 across hospital groups within that very database.

**And whether feature selection was contaminated is not stated.** The baseline table and univariate comparisons cover all 2,187 patients; the selection section says 58 candidates were screened without specifying whether this used the 70% training split or the whole MIMIC cohort. **If the latter, the internal validation is contaminated**, which would explain part of the 0.825-to-0.771 drop.

**Funding and conflicts are both absent.** **And the limitations section names neither of the real limitations** — it offers only "the absence of a large-scale nationwide epidemiological survey" and "the lack of repeated sampling for trajectory modeling," neither of which is a defect of this study.

**Why not 1.** Because the external validation was genuinely performed, the ranking genuinely transported, and **the full metric table was published** — which is honest reporting even though the authors did not read their own numbers. A paper that printed only "external AUROC 0.757" would deserve less, and would have been harder to catch.

**Why not 3.** Entries 80, 81 and 82 earned 3 with headline numbers that were optimistic but *supported by what was reported*, and with limitations sections that named the right problems. **Here the headline claim — a tool for early recognition of high-risk patients — is contradicted by the paper's own sensitivity figure, the model's own explanation names a null variable, the performance table does not internally reconcile, and the tool is already public.** That is a mismatch between claim and evidence, which is what entry 77 scored 2 for.

**What would make this a 4, concretely.** **Report sensitivity at a threshold re-chosen for the external prevalence**, and say plainly what the internal threshold does there. **Report missing data and the imputation method**, which would either rehabilitate LDL cholesterol or remove it. **Drop LDL cholesterol or explain it** — a variable at P = 0.532 needs an argument. **Report the calibration slope and intercept** on all three sets, which the calculator's existence makes mandatory. **Correct Table 2.** **Replace PESI with the logistic regression already in the table** as the honest comparator. **Define an index date and restrict to incident AKI.** **Group the eICU analysis by hospital.** **And state which data the LASSO saw.** Most of these need no new data.

## 4. The Editor's Concerns

**1. The deployed decision rule misses roughly two-thirds of cases, and the paper reports the number without reading it.** External sensitivity **0.345**: of **1,185** AKI patients, about **776 are missed**; the model fires on **499 of 2,183**. **For a tool whose stated purpose is early recognition of high-risk individuals, recall is the metric that matters and it is the one that failed.** The abstract calls this model "the most stable" in "discrimination, calibration, and clinical benefit." **The number is in Table 2 and contradicts the sentence.**

**2. Sensitivity collapsed from 0.746 to 0.345 crossing databases, and the prevalence shift explains it.** Internal prevalence **78.88%**, external **54.28%**. **A fixed probability threshold tuned at the higher prevalence stops firing at the lower one** — which is why specificity simultaneously rose from 0.627 to 0.910. **AUROC barely moved (0.771 to 0.757) because AUROC averages over all thresholds and is blind to which one you deploy.** This is the most important finding in the entry and the paper's two adjacent table blocks contain everything needed to see it.

**3. The 24.6-point prevalence gap may mean the outcome is not the same variable in both cohorts.** KDIGO AKI needs creatinine **or** urine output. **Yesterday's entry — using this same eICU database — established that urine output is available in only about 51.5% of encounters.** Where the urine criterion cannot be evaluated, AKI is systematically under-diagnosed. **So this may be an external validation against a differently-ascertained label**, which is entry 79's label-divergence problem (technique 297) in a new setting. The paper also never reconciles **78.88%** with the **26%** it cites from the RIETE registry — a threefold discrepancy in its own introduction.

**4. LDL cholesterol is a top-three SHAP contributor with no univariate association at all.** Medians **81.41 (AKI) vs 81.31 (no AKI)**, **P = 0.532**. Total cholesterol P = 0.608, triglycerides P = 0.899, HDL P = 0.156 — the whole lipid panel is null. **A 0.1 mg/dL median difference cannot drive a risk prediction.** This is the mirror of entry 77's backwards SHAP directions (technique 278): there the explanation contradicted the epidemiology; **here the explanation contradicts the paper's own baseline table.**

**5. The lipid distributions look imputed, and no missing-data information exists to check.** LDL's interquartile range spans **72.2 to 92.6 mg/dL**; HDL's **37.3 to 45.2**. **These are far too tight for 2,187 critically ill patients**, and tightness around the median is what mean or median imputation produces. **A cholesterol panel is not routinely drawn on a patient with a life-threatening pulmonary embolism**, so heavy missingness is the expected state. **The paper reports no missingness and no imputation method anywhere** — for 58 screened candidates including coagulation studies and blood gases. Note what this would mean if true: **LDL would be acting as a marker of who got a lipid panel**, which is a measurement-process signal — precisely the signal yesterday's entry explicitly declined to include on transportability grounds.

**6. Two arithmetic inconsistencies in Table 2, one in the winning model's own row.** Accuracy, precision and F1 are determined by sensitivity, specificity and prevalence. **Six of eight external rows reconcile exactly.** **XGBoost's F1 is printed as 0.456 and must be 0.486 from its own sensitivity of 0.345 and specificity of 0.910** (its accuracy 0.603 and precision 0.820 both reconcile correctly). **LightGBM is printed with sensitivity 0.345 and specificity 0.910 — identical to XGBoost — yet accuracy 0.578 and precision 0.800**, which cannot both be true since accuracy depends only on those three quantities; **solving backwards, its accuracy, precision and F1 are all consistent with sensitivity ≈ 0.300**, so the printed 0.345 appears copied from the row above. **Neither error changes the conclusion, and both show the table was not checked** — technique 313 run on a performance table rather than a baseline one.

**7. The comparator is a mortality score; the comparator that matters is in the same paper.** **PESI predicts 30-day death.** It was never designed for AKI, so outperforming it at AKI prediction is close to uninformative, however significant the NRI and IDI. **Meanwhile logistic regression scored 0.741 externally against XGBoost's 0.757 — a 0.016 gap with overlapping intervals (0.720–0.762 vs 0.737–0.777).** And the training gap was **0.077**. **The gradient-boosting advantage is largest where it was fitted and nearly gone where it was tested** — the pattern technique 273 identifies, and the thing a reader most needs told.

**8. The PESI comparison silently uses a different model from the headline.** "Model 1" is a **nomogram**, with AUROCs **0.748 / 0.756 / 0.754**. Those match the **logistic regression** row (0.748 / 0.756 / 0.741), not XGBoost's (0.825 / 0.771 / 0.757). **So the NRI and IDI gains belong to the nomogram while the headline discrimination belongs to XGBoost, and the paper's narrative moves between them without saying so.** Two models, one story.

**9. The top predictor contains a component of the outcome definition.** **OASIS's ten components include urine output.** **KDIGO AKI includes urine output below 0.5 mL/kg/h for 6 hours or more.** So the dominant predictor and the outcome share an input. **And ventilation and respiratory rate are each double-counted** — inside OASIS and again as standalone predictors in the same model, which inflates their apparent contribution and makes the SHAP attribution hard to read.

**10. Detection and prediction are not separated.** Predictors are from the **first 24 hours**; the outcome is AKI "occurring during ICU admission" over 48-hour and 7-day windows, **with no exclusion of AKI that had already developed in those first 24 hours**, no index date and no washout. **This is entry 77's defect (technique 277), and the baseline table carries the warning signs**: serum creatinine itself differs significantly (0.80 vs 0.90, P < .001), as does BUN. Neither was retained among the final ten, which limits the damage, but **the paper never reports how many events were prevalent rather than incident.**

**11. No hospital-level grouping within eICU.** Its **208 hospitals** are treated as one "center." Yesterday's entry, on this same database, found absolute AUROC swinging **0.091** across hospital groups — so a single pooled external figure conceals real between-hospital variation (technique 331).

**12. Whether the feature selection was contaminated is not stated.** The baseline table and univariate tests cover **all 2,187** patients; the LASSO section does not say whether the 58-candidate screen used the 70% training split or the full MIMIC cohort. **If the full cohort, the 30% internal validation is contaminated** — which would account for part of the 0.054 drop from 0.825 to 0.771. One sentence would settle it.

**13. Two order-of-magnitude extraction errors sit unremarked in the baseline table.** **Partial thromboplastin time is reported with a median of 368.79 seconds** (normal is roughly 25–35 seconds) and **fibrinogen with a median of 38.50 mg/dL** (normal is roughly 200–400 mg/dL). Both are wrong by about tenfold, consistent with mis-mapped database fields. **Neither variable entered the final model, so the headline is not corrupted** — but a baseline table published with every patient in catastrophic coagulopathy shows the extraction was not sanity-checked.

**14. The sample-size calculation describes the wrong sample and the wrong parameter count.** The stated minimum of 264 with 20.59 events per parameter reproduces exactly (264 × 0.7767 ÷ 10 = 20.50) — **it characterises the minimum, not the actual sample**, which had 172.5 events per parameter. More substantively, **the relevant denominator is the 58 candidates screened, not the 10 kept**, and selection across 58 candidates carries optimism no sample-size formula addresses (technique 311).

**15. The limitations section names neither real limitation.** In full: "the absence of a large-scale nationwide epidemiological survey and the lack of repeated sampling for trajectory modeling." **Neither is a defect of this study.** Unmentioned: the sensitivity collapse, the prevalence gap, the absence of missing-data reporting, the absence of calibration statistics, the deployed threshold, the LDL anomaly, and the CKD exclusion of 393 patients (15.2% of those screened) — which removes the group at highest renal risk.

**16. STROBE and TRIPOD are claimed, and TRIPOD's core items are missing — one day after an entry that named nothing and met them.** The paper states adherence to both. **TRIPOD requires missing data to be reported and its handling described; calibration to be reported with slope and intercept; the full model to be presented so a reader can compute a prediction; and participant flow with numbers at each stage.** **None of the first three is met**, and the fourth exists only in an unreachable figure. **Set against entry 83, decoded yesterday: it named no reporting guideline and satisfied essentially all of those items — a calibration slope with a width-0.085 interval, missing data quantified and sensitivity-tested, the complete model published.** **Two consecutive entries, in opposite directions, make the standing rule as sharp as it can get: naming a checklist tells you nothing about whether the work behind it was done. Read the methods.**

## 5. Statistics Spotlight

Three concepts, numbered from 343 in the running list in `queue.md`. The first is the most practically important thing in this entry.

**An AUROC is threshold-free, so it can transport while the decision rule collapses — and only the deployed threshold affects patients.**

This paper's headline is that discrimination held up across databases: **AUROC 0.771 internally and 0.757 externally**, a drop of only 0.014. **That is true and it is good.** It is also not what a clinician experiences.

**What AUROC measures.** Take one patient who developed kidney injury and one who did not. **AUROC is the probability the model gives the first a higher risk score than the second.** It is a statement about **ranking**, computed by sweeping across **every possible cut-off** and averaging. 0.5 is a coin flip.

**What a deployed tool does.** It picks **one** cut-off. Above it, you get an alert; below it, you do not. **AUROC never tells you which cut-off was chosen or how it behaves.**

**Here is what happened in this paper.** With the ranking essentially unchanged, **sensitivity fell from 0.746 internally to 0.345 externally — catching 74.6% of cases, then 34.5%.** Specificity moved the other way, from **0.627 to 0.910**. In absolute terms, out of **1,185** external patients with AKI, roughly **776 were missed**, and the model raised an alarm on just **499 of 2,183** patients.

**And the cause is identifiable.** AKI prevalence was **78.88%** in the development database and **54.28%** in the validation database — **a 24.6 percentage-point drop.** A model trained where four in five patients have the outcome learns to output high probabilities; a threshold set there sits low in the distribution. **Move to a population where only half have the outcome, the whole distribution of predicted probabilities shifts down, and the same fixed threshold now sits high — so it fires far less often.** Sensitivity falls, specificity rises, and **AUROC, which never looks at any single threshold, barely notices.**

**The everyday version.** Think of a sorting machine for apples that ranks them by ripeness — and it ranks beautifully, best to worst, in any orchard. **Now you add a rule: "put anything above this ripeness line in the export box."** You tuned that line in an orchard where most apples were ripe. **In a new orchard where only half are ripe, the same line lets almost nothing through.** The machine's *ranking* is as good as ever. **The export box is nearly empty.** You have not got a worse sorter; you have got the wrong line.

**Watch out for:** a paper reporting external validation **as a single AUROC**, with the statement that performance was "maintained" or "comparable." **AUROC transporting tells you the ranking survived, and nothing about the tool.** Three questions. **What were sensitivity and specificity at the deployed threshold, in each dataset separately?** **What was the outcome prevalence in each, and did it change?** **And was the threshold re-chosen for the new population, or carried over?** **The diagnostic pattern is unmistakable once you look for it: sensitivity and specificity moving in opposite directions across cohorts, with AUROC roughly flat, means the threshold did not transport.** And the practical consequence is severe — **a tool can be published with good external discrimination and still miss most of the cases it was built to find.**

**A variable with no association to the outcome cannot credibly be a top contributor — and a suspiciously narrow spread tells you why.**

The paper reports that **LDL cholesterol** was among the three largest contributors to predicted AKI risk, by SHAP. **Its own baseline table says LDL cholesterol has no relationship with AKI at all.**

**The numbers.** Patients who developed kidney injury had a median LDL of **81.41 mg/dL**. Those who did not had **81.31 mg/dL**. **A difference of one-tenth of one unit, with P = 0.532** — far from any threshold of significance, on 2,187 patients. And the whole lipid panel is equally flat: total cholesterol **P = 0.608**, triglycerides **P = 0.899**, HDL **P = 0.156**.

**What SHAP is, and what it is not.** **SHAP** attributes a model's prediction to its input variables: it answers *how much did this variable move this model's output*. **That is a question about the model, not about the world.** A variable can carry large SHAP values because the model leaned on it — including when the model leaned on noise. **SHAP is not evidence that a variable is associated with the outcome.** A univariate test is. **When the two disagree this sharply, the SHAP ranking is describing an artefact.**

**Now the likely mechanism, visible in the same table.** Look at how tightly the lipids are distributed. The middle half of patients span LDL **72.2 to 92.6 mg/dL** and HDL **37.3 to 45.2 mg/dL**. **Real lipid values in 2,187 critically ill people scatter far more than that** — you would expect LDL from perhaps 40 to 180. **A distribution clustered tightly around its own median is the fingerprint of a variable that was largely missing and filled in with the average.** And this is exactly the variable you would expect to be missing: **nobody routinely orders a cholesterol panel on a patient with a life-threatening lung clot.**

**If that is what happened, LDL is not measuring cholesterol. It is measuring whether a lipid panel was drawn** — which depends on how stable the patient was, how long they stayed, and local ordering habits. **That is a measurement-process signal, and it will not transport between hospitals.** **The paper reports no missing data anywhere, so none of this can be checked** — which is why the finding is uninterpretable rather than merely surprising.

**The everyday version.** You study what predicts exam success and find "wore a watch" among your top three factors. Then you look: 90% of students had no watch recorded, and you filled those in with "average watch." **Your variable is no longer about watches. It is about which students got their accessories noted down** — probably the ones a teacher spent time with. **The model found a real pattern in your data and a meaningless one in the world.**

**Watch out for:** any SHAP, feature-importance or variable-ranking figure presented as biological or clinical insight. **Two free checks. First, cross the importance ranking against the paper's own baseline table — does each "important" variable actually differ between outcome groups?** **Second, look at the interquartile ranges: a laboratory value with an implausibly narrow spread in a sick population has probably been imputed.** And the third question, which this paper cannot answer: **what fraction of each variable was missing, and how was it filled?**

**Accuracy, precision and F1 are determined by sensitivity, specificity and prevalence — so you can check a performance table, and it is worth doing.**

This paper prints nine metrics for each of eight models on each of three datasets. **Most of those numbers are not independent**, which means a reader can rebuild them and see whether the table closes.

**The arithmetic.** If you know the **sensitivity** (share of true cases caught), the **specificity** (share of true non-cases correctly cleared) and the **prevalence** (how common the outcome is), you can reconstruct the whole confusion matrix, and from it:

- **Accuracy** = sensitivity × prevalence + specificity × (1 − prevalence)
- **Precision** = true positives ÷ all flagged
- **F1** = the harmonic mean of precision and sensitivity

**Note the important special property: accuracy depends on nothing except those three quantities.** So **two models with the same sensitivity and specificity, evaluated on the same patients, must have identical accuracy.** There is no freedom.

**What I found doing this on the external-validation block.** Prevalence is 54.28% (1,185 of 2,183). **Six of the eight models reconcile exactly** — decision tree, K-nearest neighbours, logistic regression, naïve Bayes, random forest and support vector machine, all three derived metrics matching to within 0.002. **Two do not.**

**XGBoost, the winning model.** From its printed sensitivity of 0.345 and specificity of 0.910, accuracy comes to **0.603** (printed 0.603, correct) and precision to **0.820** (printed 0.820, correct). **But F1 comes to 0.486, and the paper prints 0.456.** Four of five numbers reconcile and one does not, so **the headline model's F1 is misreported by 0.030.**

**LightGBM is the clearer error.** It is printed with **sensitivity 0.345 and specificity 0.910 — exactly XGBoost's** — yet accuracy **0.578** and precision **0.800** against XGBoost's 0.603 and 0.820. **That is impossible.** Solving backwards from its own accuracy, precision and F1, all three are consistent with a sensitivity of about **0.300**. **So LightGBM's true sensitivity is near 0.300 and the printed 0.345 appears to have been copied from the row above.**

**Neither error changes any conclusion.** Both show the table was never checked — and the check takes minutes.

**The everyday version.** A shop's till roll says 40 items sold at £5 each and £250 taken. **You do not need the stock records to know something is wrong**; 40 × 5 = 200. **The internal arithmetic of a report is checkable without any outside information, and reports that fail that check have not been proofread.**

**Watch out for:** performance tables giving accuracy, precision, recall and F1 side by side. **Rebuild two or three rows.** When a row fails, note *which* number is the odd one — a single wrong F1 is a typo, while an accuracy inconsistent with its own sensitivity and specificity means two rows got crossed. **And when several models share identical sensitivity and specificity to three decimals, be suspicious before you even calculate**: genuinely different algorithms rarely land on exactly the same operating characteristics. This is technique 313 — *check that the tables decompose* — applied to a performance table instead of a baseline one, and it is just as cheap.

## 6. Jargon Translator

**Pulmonary embolism (PE)** — a blood clot that travels to the lungs and blocks blood flow. The paper calls it the **third most common fatal cardiovascular disease worldwide**, after heart attack and stroke.

**Critical PE** — the severe end, where blood pressure falls or the heart is failing. Here operationally it means PE patients admitted to intensive care.

**Acute kidney injury (AKI)** — a sudden drop in kidney function. The kidneys depend on blood flow, so they fail early when circulation does.

**KDIGO 2012 criteria** — the standard AKI definition. **Either** creatinine rising 0.3 mg/dL in 48 hours or 50% in 7 days, **or urine output below 0.5 mL/kg per hour for 6 hours.** **The "or urine output" half is where this paper's two databases probably diverge.**

**Creatinine** — a waste product cleared by the kidneys; when they fail it rises. **It is part of the AKI definition, so it cannot be used innocently as a predictor of AKI.**

**MIMIC-IV** — a free de-identified database from one Boston hospital, over 70,000 critical patients, 2008–2019.

**eICU-CRD** — a free de-identified database from **208 US hospitals**, 139,367 patients, 2014–2015. **Despite the paper's wording, this is not "one center."**

**External validation** — testing a model on data from different hospitals that played no part in building it. **The strongest routine test of whether a model travels, and the reason this paper was chosen.**

**ICD codes** — the international system of diagnosis codes. PE is category **415** in ICD-9 and **I26** in ICD-10. Identifying disease by billing code is convenient and imprecise.

**OASIS (Oxford Acute Severity of Illness Score)** — a severity score from first-day data. **Its ten components include urine output — which is also half of the AKI definition**, so the paper's top predictor overlaps its own outcome.

**PESI (Pulmonary Embolism Severity Index)** — a score predicting **death within 30 days** of a PE. **Not designed to predict kidney injury**, which is why using it as the benchmark here proves little.

**LASSO** — a method that shrinks unhelpful variables' coefficients to zero, picking a subset. Used here to cut 58 candidates to 20.

**XGBoost (extreme gradient boosting)** — a powerful algorithm building many small decision trees in sequence. Accurate and not directly interpretable.

**AUROC** — the chance the model ranks a true case above a true non-case. **Measures ranking across all cut-offs; says nothing about the one actually used** — technique 343.

**PRAUC** — area under the precision-recall curve. **Depends on prevalence**, so it is not comparable across cohorts with different event rates.

**Sensitivity (recall)** — the share of real cases the model catches. **0.345 externally here, meaning 65.5% missed.** **The metric that matters for an early-warning tool.**

**Specificity** — the share of real non-cases correctly cleared. **Rose from 0.627 to 0.910 externally**, the mirror image of the sensitivity collapse.

**Precision** — of the patients flagged, the share who really had the outcome. **0.820 externally** — when it fires it is usually right; it just rarely fires.

**F1 score** — a single number combining precision and recall. **Printed as 0.456 for the winning model; from its own sensitivity and specificity it must be 0.486.**

**Kappa** — agreement corrected for chance. **0.242 externally** — weak.

**Brier score** — average squared error of predicted probabilities; lower is better. **0.137 internally, 0.206 externally — 50% worse.** **But Brier mixes ranking and probability accuracy, so it cannot substitute for a calibration slope.**

**Calibration** — whether a predicted 30% risk corresponds to 30% of such patients having the event. **Asserted here only as plots that "approximated the diagonal." No slope, intercept or observed-to-expected ratio is reported for any model.**

**SHAP (Shapley Additive eXplanation)** — attributes a prediction to its inputs. **It describes the model, not the world.** A variable can have a large SHAP value and no real association — technique 344.

**Decision curve analysis (DCA)** — asks whether using a model beats treating everyone or nobody across thresholds of concern. Performed here, in an unreachable figure.

**NRI and IDI** — two measures of how much a new model improves classification or discrimination over an old one. **Reported here against PESI, and for the nomogram rather than the headline XGBoost model.**

**Nomogram** — a point-based score you can compute by hand. **"Model 1" in the PESI comparison is a nomogram, not XGBoost** — a switch the paper does not flag.

**TRIPOD** — the reporting guideline for prediction-model studies. **Claimed here; its core items on missing data, calibration and model presentation are not met.**

## 7. What You Can (and Can't) Say

**You can say:**

"In 2,187 critically ill patients with pulmonary embolism from MIMIC-IV, 1,725 (78.88%) developed acute kidney injury, and in 2,183 patients from the eICU database, 1,185 (54.28%) did."

"An XGBoost model using ten routinely available variables achieved AUROC 0.825 (95% CI 0.800–0.850) in training, 0.771 (0.728–0.814) in internal validation and 0.757 (0.737–0.777) in external validation on a separate database."

"Discrimination transported well across databases, falling only 0.014 from internal to external validation."

"At its operating threshold in external validation the model had sensitivity 0.345, specificity 0.910, precision 0.820, accuracy 0.603 and a Brier score of 0.206."

"The ten predictors were hypertension, heart failure, pneumonia, sepsis, ventilation, respiratory rate, partial pressure of oxygen, LDL cholesterol, lactate and the OASIS severity score, selected from 58 candidates by LASSO and multivariable logistic regression."

"SHAP analysis identified OASIS as the dominant contributor, with partial pressure of oxygen and LDL cholesterol also substantial."

"The model outperformed the PESI score on AUROC in all three datasets, with positive and significant NRI and IDI."

"A public web calculator was deployed; the paper gives its address."

**You cannot say:**

"The model identifies patients at high risk of kidney injury." **At its external operating point it misses about 65.5% of them** — roughly 776 of 1,185 — and fires on only 499 of 2,183 patients.

"External validation showed the model performs well in new hospitals." **The ranking transported; the decision rule did not.** Sensitivity fell from 0.746 to 0.345 while specificity rose from 0.627 to 0.910.

"Performance was comparable across cohorts." **True of AUROC only.** The two cohorts' AKI rates differ by 24.6 percentage points, which is what moved the operating point.

"LDL cholesterol is a risk factor for AKI in critical pulmonary embolism." **The paper's own table gives medians of 81.41 versus 81.31 mg/dL with P = 0.532** — no association at all. The whole lipid panel is null.

"SHAP shows which factors cause kidney injury." **SHAP describes the model's behaviour, not the biology**, and here one of its top three variables has no measurable relationship with the outcome.

"The model is well calibrated." **No calibration slope, intercept or observed-to-expected ratio is reported for any model on any dataset** — only plots described as approximating the diagonal, and a Brier score that worsened 50% externally.

"It beats existing tools." **It was compared against PESI, a 30-day mortality score never designed to predict kidney injury.** In the paper's own table, **plain logistic regression reached 0.741 externally against XGBoost's 0.757**, with overlapping intervals.

"Machine learning outperformed conventional modelling." **Only where it was fitted.** The gap over logistic regression was 0.077 in training and 0.016 externally.

"The NRI and IDI show the XGBoost model improves on PESI." **Those comparisons use the nomogram**, whose AUROCs (0.748/0.756/0.754) match the logistic regression row, not XGBoost's.

"OASIS independently predicts AKI here." **OASIS includes urine output, which is one of the two KDIGO criteria for AKI**, so predictor and outcome share a component — and ventilation and respiratory rate are each counted twice, inside OASIS and separately.

"The model predicts future kidney injury." **Predictors come from the first 24 hours and AKI arising in that same window is not excluded**, with no index date and no washout, so prediction and detection cannot be separated.

"This is a multicenter clinical study." **It is a retrospective analysis of two public databases**, and eICU alone comprises 208 hospitals rather than one "center."

"It is ready for clinical use because there's a calculator." **The calculator is public and ships the threshold whose sensitivity fell to 0.345 externally**, with no calibration statistics reported.

**The honest one-sentence version:** *a genuine and creditable external validation across two ICU databases, showing that the model's ranking travels, wrapped around a tool that at its deployed threshold misses about two-thirds of the kidney injuries it exists to catch, whose own top-three explanation names a variable with P = 0.532 and a 0.1 mg/dL median difference, whose performance table contains two arithmetic inconsistencies including the winning model's F1, whose comparator is a mortality score while the logistic regression that nearly ties it sits in the same table, and which claims TRIPOD adherence while reporting no missing data, no calibration slope and no usable model specification.*

## 8. Bottom Line for Your Life

**If you or someone you love is in intensive care with a blood clot in the lungs:** nothing here changes any treatment, and no clinician should be using this calculator to make decisions about you. **The clinical fact behind the paper is worth knowing, though:** kidney injury is a common and serious complication of severe pulmonary embolism — the registry the paper cites found it in **26%** of acute PE patients, and in intensive care the rates are far higher. **Doctors watch kidney function closely in this situation already**, by checking creatinine and urine output. **That is the monitoring that matters, and it does not depend on any model.**

**If you are a clinician who finds a free risk calculator online:** this paper is a case study in why a published AUROC is not permission to use a tool. **The number that decides whether a calculator helps you is its sensitivity at the threshold it actually uses, in a population like yours.** Here that number is **0.345** — it misses roughly two-thirds of cases — and you would never learn it from the abstract, which describes the model as showing "the most stable discrimination, calibration, and clinical benefit." **Two questions to ask of any such tool: what fraction of real cases does it catch at its default setting, and was that setting checked in a population with my patients' event rate?** If the answer to the second is no, the first number does not apply to you.

**If you build prediction models, this entry contains one cheap habit and one cheap check.** **The habit: when you validate externally, re-report sensitivity and specificity for each cohort separately, state each cohort's outcome prevalence, and say whether you re-chose the threshold.** This paper had all the data needed and printed the numbers in adjacent table blocks without comparing them. **A 24.6-point prevalence shift will move your operating point, every time, and an AUROC will not warn you.** **The check: before submitting, rebuild your own accuracy, precision and F1 from your sensitivity, specificity and prevalence.** Six of this paper's eight external rows reconcile and two do not — including the winning model's F1. **It takes minutes and it is the difference between a table a reader can trust and one they cannot.**

**And one habit for anyone who reads these papers.** When a paper shows you a variable-importance or SHAP chart, **cross it against the paper's own baseline table.** Here the chart's number-two variable, LDL cholesterol, differs between outcome groups by **0.1 mg/dL with P = 0.532.** That comparison takes thirty seconds and it is the single most informative thing you can do with a feature-importance figure. **A model can lean heavily on a variable that means nothing** — and when it does, the explanation it offers you is about the model, not about the patient.

**The thing worth taking from reading entries 83 and 84 back to back.** Yesterday's paper **named no reporting guideline** and did nearly everything a prediction-model checklist asks: missing data quantified and sensitivity-tested, calibration reported with a slope and a tight interval, the complete model published. **Today's paper states that it adhered to TRIPOD** and reports **no missing data at all, no calibration slope, and no model specification a reader could use.** **Decoded one day apart, they make the point better than any argument could: the checklist is a claim, not a result. Read the methods.**

**If you are reading the coverage:** expect "AI predicts kidney failure in pulmonary embolism patients" with the 0.757 external figure. **Three things will be missing.** That the tool misses about two-thirds of cases at the threshold it ships with. That one of its three headline predictors has no association with the outcome in the paper's own table. And that the comparison it wins is against a score built to predict something else entirely, while the plain logistic regression that nearly matches it sits two rows above in the same table.

**This is education, not medical advice.** Nothing here concerns any diagnosis or treatment decision, and no model discussed here is validated for clinical use. Questions about the care of a critically ill person belong with the treating team.

---

## Appendix: the pre-registered questions, verification, landmark screen, and status on 2026-11-21

**Both pre-registered questions, answered — and the second one less cleanly than hoped.** Set yesterday, written down before reading.

**(1) "How much performance was lost between MIMIC-IV and eICU, and was the web calculator deployed before or after that was known?"** — **Discrimination lost almost nothing: AUROC 0.771 → 0.757, a drop of 0.014.** But **the operating point lost almost everything: sensitivity 0.746 → 0.345**, a 53.8% relative collapse, with specificity rising 0.627 → 0.910 and the Brier score worsening 50% (0.137 → 0.206). **The prevalence shift from 78.88% to 54.28% is sufficient to explain it.** On the calculator: **it was deployed with full knowledge of the external results** — the paper reports them in Table 2 and then describes the calculator in §3.5 — and **it ships the untransported threshold with no calibration slope, intercept or observed-to-expected ratio reported anywhere.** So the answer is: deployed after, with the degradation visible in the authors' own table and unremarked.

**(2) "Was the external validation genuinely held out — features selected and hyperparameters fixed on MIMIC-IV before eICU was touched — or does the paper report eICU numbers that informed model choice?"** — **The eICU set does appear genuinely held out**; nothing suggests it informed selection, and the model with the best *training* AUROC was carried forward. **But a different contamination question opened in its place and the paper does not close it:** the statistical plan says MIMIC-IV was split 70/30 and that "variable selection was performed by integrating LASSO and multiple logistic regression," **without stating whether the 58-candidate screen used the 70% training split or all 2,187 patients.** Table 1 and every univariate comparison cover all 2,187. **If selection saw the whole MIMIC cohort, the 30% internal validation is contaminated**, which would account for part of the 0.054 drop from 0.825 to 0.771. **One sentence would settle it and the paper does not contain it.**

**Arithmetic verified today — the cohort reconciles perfectly and the performance table does not.** **Cohort cascade:** 2,580 screened − 393 CKD (15.2%) = **2,187**, as stated; 1,725 + 462 = 2,187; **AKI 78.88%** exact; sex 1,099 + 1,088 = 2,187; **eICU 1,185/2,183 = 54.28%** exact. **AKI staging:** 462 + 354 + 898 + 473 = **2,187**, with stages I–III summing exactly to **1,725**. **Sample size:** 264 × 0.7767 ÷ 10 = **20.50** against the stated 20.59, confirming the figure describes the minimum rather than the actual sample (which had 172.5 events per parameter). **Prevalence gap 24.60 points, ratio 1.45×**; and 78.88% is **3.03×** the 26% in the RIETE registry the paper cites itself.

**Table 2, external-validation block — rebuilt all eight rows from sensitivity, specificity and prevalence.** **Six reconcile exactly** (decision tree, K-nearest neighbours, logistic regression, naïve Bayes, random forest, support vector machine — all three derived metrics within 0.002). **Two do not.** **XGBoost: accuracy 0.603 and precision 0.820 both reconcile, but F1 must be 0.486 against the printed 0.456 — the headline model's F1 is misreported by 0.030.** **LightGBM: printed with sensitivity 0.345 and specificity 0.910, identical to XGBoost, yet accuracy 0.578 and precision 0.800 against XGBoost's 0.603 and 0.820 — arithmetically impossible, since accuracy is determined by sensitivity, specificity and prevalence alone.** Solving backwards, LightGBM's accuracy (0.578), precision (0.800) and F1 (0.433) are **all** consistent with a sensitivity near **0.300**, so the printed 0.345 appears copied from the row above. **Neither error changes any conclusion; both show the table was not checked.**

**At the external operating point, in absolute numbers:** of 1,185 AKI patients the model flags about **409** and misses about **776 (65.5%)**; it fires on **499 of 2,183** patients in total.

**The comparator analysis.** External AUROC: XGBoost **0.757 (0.737–0.777)** against plain logistic regression **0.741 (0.720–0.762)** — gap **0.016** with **overlapping** intervals. Internal: 0.771 against 0.756, gap 0.015, intervals overlapping heavily. **Training: 0.825 against 0.748, gap 0.077** — the only set where XGBoost clearly leads. **The advantage is largest where the model was fitted and nearly gone where it was tested.** And the PESI comparison's "Model 1" AUROCs (**0.748 / 0.756 / 0.754**) match the **logistic regression** row, not XGBoost's (0.825 / 0.771 / 0.757), **so the NRI and IDI gains belong to the nomogram while the headline discrimination belongs to XGBoost** — a switch the paper never flags.

**The LDL-C contradiction, from the paper's own Table 1.** Non-AKI **81.31 (70.56–91.93)** against AKI **81.41 (72.55–92.80)**, **P = .532** — a median difference of **0.10 mg/dL**. Total cholesterol P = .608, triglycerides P = .899, HDL P = .156: **the entire lipid panel is null**, yet LDL is retained as one of ten "independent risk factors" and reported by SHAP as a top-three contributor. **And the distributions are implausibly narrow for 2,187 ICU patients** — LDL's interquartile width is **20.41 mg/dL (25.1% of its median)** and HDL's **7.89 mg/dL (19.5%)** — the signature of a mostly-missing variable imputed to its median. **The paper reports no missing data anywhere**, so this cannot be checked, which is what makes it uninterpretable rather than merely odd.

**Two order-of-magnitude extraction errors found in Table 1.** **Partial thromboplastin time, median 368.79 s (IQR 288.06–439.80)** against a normal range of roughly 25–35 s; **fibrinogen, median 38.50 mg/dL (IQR 29.10–60.67)** against a normal range of roughly 200–400 mg/dL. Both wrong by about tenfold, consistent with mis-mapped database fields. **Neither variable entered the final model, so the headline is not corrupted** — but a published baseline table in which every patient appears to be in catastrophic coagulopathy shows the extraction was not sanity-checked.

**The OASIS overlap, checked against the published OASIS definition.** OASIS's components are pre-ICU length of stay, age, GCS, heart rate, mean arterial pressure, respiratory rate, temperature, **urine output**, mechanical ventilation and elective surgery. **KDIGO AKI includes urine output below 0.5 mL/kg/h for ≥6 hours.** So the paper's dominant predictor shares a component with its outcome. **And ventilation and respiratory rate are each double-counted** — inside OASIS and again as standalone predictors in the same ten-variable model.

**Positive practice worth carrying forward, because there is some.** **A genuine external validation on a separate database** (284) — the reason this paper was picked, and more than most entries attempt. **Decent AUROC transportability**, 0.014 internal-to-external. **Full nine-metric reporting for all eight models on all three datasets** — the paper's best decision, and **the reason every criticism above was findable**; a paper reporting AUROC alone would have hidden the sensitivity collapse completely. **Decision curve analysis run.** **AKI staging reported**, so the severity mix is visible. **The CKD exclusion stated and counted.** **The MIMIC access record ID given** (72870037). **Ethics waiver justified.** **Author contributions in full.** **And the calculator's address published** rather than promised.

**What could not be verified.** All six figures and all eleven supplemental files, costing: the participant flow diagram with numbers at each stage; the LASSO coefficient trajectories and cross-validation curves; the correlation matrix and variance-inflation factors (which would have shown whether OASIS collinearity with ventilation and respiratory rate was examined); the ROC, calibration and decision curves for all three sets; the SHAP summary and dependence plots; the per-set model metric tables S5–S7; the hyperparameter table S8; and the calculator screenshots. **Also absent from the text entirely: funding, conflicts of interest, any missing-data information, any calibration slope or intercept, the fitted model's coefficients, and the proportion of AKI events that were prevalent rather than incident.** **I did not attempt to reach the calculator URL and am not asserting it resolves — I report it only as the address the paper states.** **Nothing was reproduced that was not seen.**

**Reporting-guideline pattern — and entries 83 and 84 are the sharpest possible pair.** 71, 73, 74, 75, 77, 78 named none; 69 named TRIPOD+AI with a deposited checklist; 70 named STROBE; **76 measured the phenomenon at 40% mean TRIPOD-LLM completeness**; 79 named six instruments and applied them; 80 named TRIPOD with a checklist; 81 named none; 82 named none visible; **83 named none and satisfied nearly every TRIPOD+AI item in substance**; **84 names STROBE and TRIPOD and misses TRIPOD's core items** — missing data reported and handled, calibration with slope and intercept, and the full model presented so a reader can compute a prediction. **Decoded one day apart, in opposite directions.** **The standing rule is now as firmly established as this list can make it: naming a checklist is a claim about intent, not a result. Read the methods.**

**Deferred status, 2026-11-21.** **Gait foundation model (42995231) — day 13, re-checked today, still no PMC copy**; abstract-only date **2026-11-30**, nine days out. Largest multiplicity problem this list will have faced (**1,887 of 3,210 tested phenotypes called significant**); first question remains what false-discovery-rate procedure ran across those 3,210 tests. **And today extends the three-way connection to four.** Entry 82 had **15 independent units dressed as 4,050**; the gait paper has **3,210 tests whose dependence structure decides whether 1,887 findings mean anything**; entry 83 is the positive case, identifying its independent unit and splitting on it; **and entry 84 is the deployment case — it treated 208 hospitals as one "center," so its single pooled external figure conceals exactly the between-hospital variation entry 83 measured at 0.091 in that same database.** **All four are the same question: how many independent things were really examined?**

**Landmark check, 2026-11-14 → 11-21 — eighteen records, all screened, none displacing the queue.** **Fifteen were already assessed** on 2026-11-18, 11-19 or 11-20. **Two are new *Nature* News items**, neither medical: **43064755** on a claimed AI-assisted proof of the Riemann hypothesis (mathematics) and **43064747** on amateur astronomers using AI to search for planets (astronomy). **One is a genuine medical-AI paper and goes to the shelf as (M)** — see below.

**SHELF ADDITION — 2026-11-21.**

**(M) Deep learning of brain-behavior dimensions identifies transdiagnostic biotypes in youth with ADHD and anxiety disorders** — PMID 43061158, **PMC13784670**, DOI 10.1038/s44220-026-00740-3, *Nature Mental Health* 2026;4(11):1686–1700, Jiao Y et al. (Iowa, Stanford, UT Austin, Penn). **3,508 children aged 9–11 from the Adolescent Brain Cognitive Development study**, integrating functional connectivity with cognitive and behavioural measures; **two reproducible brain-behaviour dimensions** (cognitive control; emotion-attention regulation) yielding **three biotypes** (externalizing-disinhibited, internalizing-distressed, mixed dysregulation); **generalised to 224 age-matched Healthy Brain Network participants** and reported as "detectable before symptom onset, indicating preclinical expression." **Why it earns a slot: this would be the list's first unsupervised subtype-discovery paper**, a genre with its own characteristic failure mode — clusters that are artefacts of the algorithm and the distance metric rather than features of the population. **First questions: what establishes that three is the right number of biotypes rather than two or five; was the 224-participant replication used to select the solution or only to test it; and does "detectable before symptom onset" rest on prospective data or on cross-sectional comparison?** Note it **shares authors with shelf item (L)** (Tong X, Fonzo GA, Zhang Y), so decoding both would also give a within-group comparison of reporting practice. E-published 2026-10-16, so not a landmark displacing a queued pick.

**Plan set on 2026-11-21.** **Next run takes shelf item (I)** — **complete renal response in lupus nephritis**, PMID 43015004, PMC13757897, *Ren Fail* 2026: **a prospective cohort of 400** followed 12 months, four ML models, reporting **AUC, calibration AND decision-curve analysis plus SHAP**. **Three reasons it follows today naturally.** It is **prospective**, which almost nothing in this list is, so it escapes the retrospective-database problems that dominated entries 83 and 84. It **reports calibration explicitly** — the thing entry 84 omitted while shipping a probability calculator — so it is the right paper on which to ask whether the calibration is *estimated* (entry 83's slope interval of 0.085) or merely *asserted* (entry 84's "approximated the diagonal"). And its stated hook is that it "leverages the 3-month treatment milestone," which is **a change-versus-level question** (technique 287). **Two questions written down now, before reading. (1) Does the 3-month milestone add anything over baseline variables alone — is this predicting CHANGE or re-predicting a LEVEL?** **(2) Is the calibration reported as a slope with an interval, or only as a plot — and with n=400 and a 12-month outcome, how many events are there to estimate it from (336)?** **Shelf after today: three spares — (J) sickle-cell facial phenotyping with LOOCV on 308 smartphone photos, (K) next-day alcohol craving from EEG, HRV and phone sensing, (L) antidepressant versus placebo functional connectivity, plus (M) added today.**

**Standing watch item:** PM Heart trial results (protocol PMID 42893738), quarterly.
