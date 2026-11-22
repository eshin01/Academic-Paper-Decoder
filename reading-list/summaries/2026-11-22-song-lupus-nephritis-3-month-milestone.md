# A machine learning-based predictive tool for complete renal response in lupus nephritis leverages the 3-month treatment milestone

**Authors:** Song S, Fan Y, Zhang X, Cheng J, Gao D, Zhang J, Ding T, Ji L, Zhang Z — 9 authors, all Department of Rheumatology and Clinical Immunology, Peking University First Hospital, and Beijing Key Laboratory of Precision Diagnosis and Treatment for Major Rheumatic and Immune Diseases, Beijing, China
**Journal:** Renal Failure, 2026; 48(1): 2751782 (e-published 2026-11-11)
**Decoded:** 2026-11-22

**Analysis basis:** **FULL TEXT** (retrieved from PubMed Central, PMC13757897). Introduction, all Methods including study design, inclusion and exclusion criteria, data collection, the outcome definition, model development and validation, and the statistical plan; all Results; and the complete Discussion with its limitations and conclusions. **All three tables came through intact** — the baseline table, the 3-month and 6-month follow-up table, and the model-performance table — so every number below is verified against the paper's own tables. **The figures themselves are unreachable, but their descriptive captions came through**, which supplies the training-set AUCs from Figure 1, the Brier scores from Figure 3, and all four cell counts from Figure 4. **Supplementary Tables 1 and 2 are unreachable**, which costs both multivariable regression outputs.

**Source links (verified):**
- DOI: https://doi.org/10.1080/0886022X.2026.2751782
- PubMed: https://pubmed.ncbi.nlm.nih.gov/43015004/
- Full text used: https://pmc.ncbi.nlm.nih.gov/articles/PMC13757897/

**Basis of link verification.** Direct URL fetching is blocked from this session (`doi.org` does not resolve under the network policy here), so verification was done against the live PubMed/NLM record. According to PubMed, a query for PMID 43015004 returned this exact title, these nine authors with these affiliations, *Renal Failure* volume 48 issue 1 article 2751782, DOI `10.1080/0886022X.2026.2751782`, and MeSH terms including Lupus Nephritis, Prospective Studies, Random Forest, Proteinuria and Machine Learning; a PMID-to-PMCID conversion returned **PMC13757897**; and the full text was then retrieved from PubMed Central by that PMC ID and matches the record. Both halves of the chain were confirmed independently.

**Funding, conflicts of interest, ethics approval, informed consent, data availability and author contributions: NOT RETRIEVABLE.** None of these statements appears anywhere in the retrieved PMC body. Taylor & Francis journals normally carry funding, disclosure and ethics statements, so these are most likely held in journal metadata outside the article body. **I am recording them as not retrievable rather than absent, and I am not reporting any funder, disclosure or approval I have not seen.** The study is described as prospective with enrolment from January 2017 to May 2024, which would ordinarily require ethics approval and consent.
**Reporting guideline: none named.** **TRIPOD** applies directly to this study type and is not mentioned — and Section 4 records where that leaves this list's running observation after three consecutive entries.

---

## 1. The Gist

**Nine rheumatologists in Beijing followed 400 people with lupus kidney disease for a year and asked a simple, useful question: how early can you tell whether the treatment is going to work? Their answer is three months — and the honest version of their finding is narrower and more interesting than the headline suggests.**

Start with the disease. **Lupus** is a condition in which the immune system attacks the body's own tissues. When it attacks the kidneys, that is **lupus nephritis**, and the paper notes it affects **35% to 60%** of lupus patients, usually within the first five years. It is the main reason lupus patients progress to kidney failure.

Treatment is months of immune-suppressing drugs, and the goal is **complete renal response (CRR)** — the kidneys calming down enough that protein stops leaking into the urine. European guidelines ask for this **within 6 to 12 months.** The clinical problem is obvious: **if a patient is not going to respond, you want to know early, so you can change the drugs rather than waiting a year to find out.**

**And here is the gap the paper identifies, correctly.** Existing prediction tools use only information from the start of treatment — age, blood tests, kidney biopsy — and they do not work well. The paper cites a major lupus trial where baseline variables predicted 6-month response with an **AUROC of just 0.55** — essentially a coin flip.

**What they did.** A **prospective cohort of 400 patients** with active lupus nephritis, enrolled at Peking University First Hospital between **January 2017 and May 2024** and followed for 12 months. They collected everything at the start, then again at 3 and 6 months. They built **four machine learning models plus a logistic regression**, trained on 70% of the data and tested on the held-out 30%. Then they compared two versions: **baseline information only**, versus **baseline plus the 3-month follow-up.**

**The results.**

- **296 patients (74%) achieved complete renal response at 12 months**
- **Baseline-only models: AUROC at most 0.746** — barely useful, as expected
- **Adding 3-month data: the Random Forest reached 0.862 (95% CI 0.775–0.949)**
- **The single most influential predictor was the 3-month urine protein level**

**So the answer to "how early can you tell?" is three months. That much is well supported, and the paper deserves credit for asking the right question and for building the cohort to answer it.**

**Now the thing that has to be said about what is being predicted.**

**Complete renal response is defined by urine protein.** Specifically, protein falling below 0.5 with stable kidney function. **And the model's strongest predictor is the urine protein level at 3 months.** So the model predicts "will protein be low at 12 months" using "is protein low at 3 months."

**And look at how low it already was.** In the group who eventually achieved response, the median 3-month urine protein was **0.54** — essentially *at* the 0.5 threshold that defines the outcome. In the group who did not respond, it was **2.75**.

**So a large part of what the model has discovered is that patients who are already in remission at 3 months are usually still in remission 9 months later.** That is true, and clinically real, and **it is a weaker claim than predicting who will respond.** It is persistence, not prophecy.

**Except the paper then does something genuinely good, and it is the best analysis in the study.** They split patients four ways — by whether baseline protein was high or low, and by whether 3-month protein was above or below 1.3 — and reported the response rate in each box:

- **Started high, came down low: 91.0%** (111 of 122)
- **Started low, stayed low: 88.6%** (62 of 70)
- **Started high, stayed high: 63.9%** (23 of 36)
- **Started low, stayed high: 44.9%** (40 of 89)

**The group that did best was not the group that was always fine. It was the group that started badly and improved.** 91.0% against 88.6%. And the group that did worst — 44.9% — was the group that started *mildly* and failed to improve.

**That answers the persistence objection.** If the model were only detecting "low protein stays low," the always-low group would win. It does not. **The fall itself carries information**, over and above where the patient ended up. **And I verified that all four boxes sum exactly** to the 317 patients with 3-month data and the 236 responders among them.

**Three more things I found.**

**First, the real limit on this study is not 400 patients — it is about 24.** Because 74% responded, the thing being predicted is the *minority*: failure. Rebuilding the paper's performance table from its own sensitivity and specificity figures — **all ten rows reconcile exactly**, which is itself a good sign — the 3-month test set works out at about **95 patients containing roughly 24 treatment failures.** **That is what the headline estimate rests on**, and it is why the confidence interval runs from **0.775 to 0.949** — a span of 0.174, meaning the true performance could be anywhere from fairly good to near-perfect.

**Second, the Random Forest scored 100% on its own training data, and the paper never mentions it.** From the figure descriptions: training AUROC of **exactly 100.00%** for Random Forest in both versions of the model, and 99.59% and 100% for XGBoost. **A model that scores 100% on the data it was fitted to has memorised it.** The gap to the test set is **26.4 points** for the baseline Random Forest and **13.8 points** with 3-month data. **The paper correctly headlines the test figures rather than the training ones — but a 100% is a warning light, and it goes unremarked.** The telling contrast is in the same figure: **logistic regression's baseline training score was 69.07% against a test score of 74.60% — it did slightly better on new data than on its own**, which is what a model that has not overfitted looks like.

**Third, the paper reports calibration — and converting it tells a more modest story.** A **Brier score** measures how far predicted probabilities sit from what actually happened; lower is better. Random Forest scored **0.134** on the test set. **But a model that does nothing at all — just announcing "everyone has a 25.55% chance of failing," the known base rate — scores 0.1902.** So the model's probabilities are **about 30% better than saying nothing.** That is real and it is a lot less impressive than 0.862 sounds. And the training Brier of **0.008** sits beside that 100% training AUROC: **memorisation, not evidence of calibration.**

**What this paper is.** A careful, honestly-reported prospective study that asks a genuinely useful clinical question and gets a defensible answer — **the first three months are the informative window, and early protein reduction is what matters** — supported by one excellent four-group analysis that survives the obvious objection. **Limited by a single centre, roughly 24 events behind its headline number, one train/test split, and a central claim about added value that the paper never formally tests.**

## 2. Study Snapshot

**Study type:** **prospective single-centre cohort** with development and internal testing of a prediction model. **No external validation**, stated in the limitations as necessary before clinical implementation. **Not a trial** — treatment was real-world and individualised.

**Setting and enrolment.** Department of Rheumatology and Clinical Immunology, Peking University First Hospital, patients diagnosed between **January 2017 and May 2024**. **Inclusion:** meeting the 1997 revised ACR or 2012 SLICC criteria for lupus; meeting the 2003 ISN/RPS classification for lupus nephritis; **age 18 or over**; and **active lupus nephritis at the initiation of induction therapy, which served as the study baseline.** **Exclusion:** incomplete medical data; end-stage renal disease; pregnancy or lactation; other autoimmune disease apart from Sjögren's syndrome; malignancy; **follow-up under one year**; and non-adherence to medication. Follow-up was **every 1–3 months during the active phase and every 3–6 months during the stable phase.**

**Cohort.** **400 patients.** **338 (84.5%) female.** Median age **32 years (IQR 25–44)**. Median lupus nephritis duration **1.58 years (0.25–6.92)**. Median baseline SLEDAI disease-activity score **16 (11–20)**. **239 (59.8%) treatment-naive.** **216 (54.0%) biopsy-proven** — the rest declined biopsy, which the paper names as a possible source of selection bias. All four percentages verified.

**The outcome.** **Complete renal response at 12 months**, defined per the **KDIGO 2021 guideline** as a reduction in 24-hour urinary total protein to **below 0.5 g/g**, together with **normal or stable serum creatinine not exceeding 115% of baseline.** Anyone not meeting both criteria at 12 months was classified non-response. **A note on the units: "g/g" is the unit of a urine protein-to-creatinine ratio, whereas 24-hour urinary total protein is measured in grams per 24 hours — and the paper reports it in grams throughout, with the Figure 4 cutoff given as "1.3 g/24h." So the stated threshold and the measured variable are two different quantities.** Numerically similar in practice; still a mismatch in the primary endpoint's definition.

**Treatment, real-world and individualised.** All patients received daily oral glucocorticoid, median prednisone **60 mg/day (IQR 50–60)**; **57 (14.3%)** had glucocorticoid pulse therapy. Immunosuppressants per Table 1: **mycophenolate mofetil 180 (45.0%)**, **cyclophosphamide 142 (35.5%)**, other agents **78 (19.5%)** — summing correctly to 400. **Biologics 29 (7.3%)**, hydroxychloroquine **357 (89.3%)**, ACE inhibitor or ARB **264 (66.0%)**. **A discrepancy worth recording: the Results text states "cyclophosphamide in 180 patients (45%), mycophenolate mofetil in 142 (35.5%)" — which reverses the two drugs relative to Table 1. A later sentence in the same section agrees with the table, so the error is in the first sentence.**

**Data collected.** Clinical features, SLEDAI, complete blood count, serum albumin, creatinine, eGFR (CKD-EPI 2021), complements C3 and C4, urine sediment, 24-hour urinary total protein, a full autoantibody panel, immunoglobulins, and all treatment details.

**Model development.** Five models: **Random Forest, support vector machine, Elastic Net, XGBoost, and conventional logistic regression.** The paper explains its choice, which is unusual and creditable: these algorithms "balance predictive accuracy, robustness, and interpretability for small-to-moderate structured clinical datasets, while avoiding overparameterized deep learning architectures prone to overfitting." Data split **randomly 70% training / 30% testing, stratified on the outcome.** **SMOTE was applied only to the training data.** Elastic Net tuned by grid search with cross-validation; the others by **repeated 10-fold cross-validation within the training set.** **"Model development and hyperparameter tuning were conducted using the training set, with performance evaluation carried out on the held-out testing set."**

**Variable selection, explicitly stated.** **"we firstly performed univariable analysis to select variables with statistically significant differences between the CRR and the non-CRR groups in the training cohort."** **Collinearity was examined with Pearson correlation and variance inflation factors**, and acted on: **"Given the strong correlations between 24hUTP and Alb (r > 0.7), and between eGFR and Scr (r > 0.7), Alb and Scr were excluded from the multivariable analysis."**

**Missing data.** **"Variables with missing values < 5% were imputed using Random Forest imputation."** R version 4.4.1.

**Baseline differences between responders and non-responders.** Responders had lower baseline urine protein (**2.20 g [1.27–4.55] vs 4.18 g [2.31–6.82], p < 0.001**), higher albumin (**28.4 vs 26.6 g/L, p = 0.015**), shorter disease duration (**1 year [0.2–5.35] vs 4.3 years [1.05–9.30], p < 0.001**) and were more often treatment-naive (**63.2% vs 50.0%, p = 0.020**). **No significant differences** in clinical manifestations, autoantibodies, complements, blood counts, urine sediment, glucocorticoid dosing, hydroxychloroquine or ACE-inhibitor use. **SLEDAI was not significantly different univariately (16 vs 14, p = 0.062).** **But the initial immunosuppressive regimen did differ (p = 0.003), with cyclophosphamide given to 50.0% of non-responders against 30.41% of responders (p < 0.001).**

**Follow-up availability, and an asymmetry the paper does not explain.** **"A total of 317 patients with complete 3-month follow-up and 394 with 6-month follow-up data constituted the further analysis population."** So **83 patients (20.75%) are missing from the 3-month analysis but only 6 (1.5%) from the 6-month analysis** — the 3-month visit was missed **nearly 14 times more often** than the later one, which is the opposite of ordinary attrition. **Since the stated imputation rule covers only variables missing under 5%, those 83 were excluded rather than imputed, and they are never characterised.** Response rates in the reduced populations match the whole cohort closely: 3-month **236 CRR (74.45%) / 81 non-CRR (25.55%)**; 6-month **292 (74.11%) / 102 (25.89%)** — both verified to sum correctly.

**What changed by 3 months.** Significant differences between responders and non-responders were present **by the 3-month visit** for urine protein, albumin and C3, **in absolute values, absolute change from baseline and percentage change from baseline (all p < 0.05)**. **Crucially, by 6 months those absolute improvements were no longer significantly different between groups** — the paper's basis for arguing the divergence happens inside the first three months. Creatinine, eGFR and urine casts differed at both time points. Anti-dsDNA positivity, pyuria and haematuria differed at neither.

**The key 3-month figures.** 24-hour urine protein: responders **0.54 (0.19–1.31)**, non-responders **2.75 (1.30–4.97)**, p < 0.001. Albumin: **37.50 (33.60–40.25)** against **30.4 (27.40–35.70)**, p < 0.001. Urine casts: **4.24% against 20.99%**, p < 0.001.

**Model performance, all five models at both time points.** **Baseline-only, on the test set:** logistic regression **0.746 (0.654–0.838)**, SVM **0.738 (0.604–0.803)**, Random Forest **0.736 (0.643–0.829)**, Elastic Net **0.730 (0.631–0.828)**, XGBoost **0.664 (0.565–0.762)**. **With 3-month data:** **Random Forest 0.862 (0.775–0.949)**, Elastic Net **0.832 (0.731–0.932)**, logistic regression **0.826 (0.725–0.926)**, SVM **0.811 (0.699–0.923)**, XGBoost **0.769 (0.666–0.871)**. Sensitivity, specificity, accuracy, PPV, NPV and F1 are given for every model at both time points. **The best Random Forest: sensitivity 83.3%, specificity 77.1%, accuracy 78.7%, PPV 0.556, NPV 0.931, F1 0.667.**

**Training-set AUROCs, from the Figure 1 description.** **Baseline-only: Random Forest 100%, XGBoost 99.59%**, SVM 70.22%, Elastic Net 69.76%, logistic regression 69.07%. **Baseline plus 3-month: Random Forest and XGBoost both 100%**, Elastic Net 91.46%, SVM 91.42%, logistic regression 90.64%.

**Calibration and clinical utility.** Calibration assessed by **calibration curves and Brier scores**. Random Forest **Brier 0.008 training and 0.134 testing**; logistic regression **0.122 and 0.160**. **No calibration slope, intercept or observed-to-expected ratio is reported.** **Decision curve analysis** showed greater net benefit than treat-all, treat-none **and the logistic regression model** across a broad range of thresholds in both cohorts.

**Interpretation.** SHAP identified, in order: **3-month urine protein, lupus nephritis duration, percentage reduction in urine protein from baseline to 3 months, baseline urine protein, and 3-month C3.** Multivariable regression (in an unreachable supplement) identified **high 3-month urine protein, elevated creatinine and positive urine casts** as independent predictors of failure.

**The stratified analysis.** Patients were split by median baseline urine protein and by an optimal 3-month cutoff of **1.3 g/24h** (Youden index). Response rates: **high baseline → low at 3 months 91.0% (111/122)**; **low → low 88.6% (62/70)**; **high → high 63.9% (23/36)**; **low → high 44.9% (40/89)**. **I verified these sum to 317 patients and 236 responders exactly.** The paper reports **a risk ratio of 1.89 (95% CI 1.59–2.26)** for achieving response with low 3-month protein; **recomputing from the four cells gives 1.79, which sits inside that interval but does not reproduce the point estimate exactly.**

**Limitations the authors state.** **Single-centre**, with external validation in multiethnic multicentre cohorts "necessary before clinical implementation." **Some patients declined kidney biopsy**, which "may introduce selection bias." **SHAP "remains a post-hoc tool whose ultimate utility must be tested through prospective clinical validation."** And a thoughtful one: **the models were developed on real-world data "in which treatment strategies were individualized and dynamically adjusted according to disease activity, treatment response, adverse events, and patient preferences," and "such complex and time-varying treatment factors could not be fully incorporated."** They also raise and explain their own unusually high response rate, and flag the SLEDAI finding as unexpected.

**Not reported or not retrievable:** **funding, conflicts, ethics approval, consent, data availability and author contributions**; **any calibration slope, intercept or O:E ratio**; **any formal test of the incremental value of 3-month data** — no paired AUROC comparison, no NRI or IDI; **any characterisation of the 83 patients missing 3-month data**; **any split-stability or repeated-split analysis**; **any reporting guideline**; **both multivariable regression tables** (Supplementary Tables 1 and 2); and all figures as images.

## 3. How Strong Is This Evidence? (Grade 3 out of 5)

**A careful, well-reported prospective study that asks a genuinely useful clinical question, answers it defensibly, and backs the answer with one excellent analysis that survives the obvious objection. It earns a 3 rather than a 4 because the headline number rests on roughly 24 events from a single split at one hospital, and because the paper's central claim — that 3-month data adds value — is never formally tested.**

**What is genuinely well done.**

**It is prospective, which almost nothing in this reading list is.** Enrolment at the initiation of induction therapy, a defined baseline, scheduled follow-up at 1–3 month intervals, and a 12-month outcome. **That design eliminates in one stroke most of the defects that dominated the last two entries** — there is no ICD-code outcome, no complete-case trawl through a billing database, and no two-database label divergence.

**Variable selection was performed in the training cohort, and the paper says so explicitly.** This is exactly the sentence entry 84 failed to write and which left its internal validation ambiguous. **Here it is unambiguous.**

**Collinearity was examined and acted on.** Pearson correlations and variance inflation factors, with albumin and creatinine dropped for correlating above 0.7 with urine protein and eGFR respectively. **Set this against entry 84, which entered a composite severity score alongside two of its own components.**

**SMOTE was applied only to the training data**, stated clearly — the same correct practice entry 77 followed.

**Hyperparameters were tuned by repeated 10-fold cross-validation inside the training set**, with evaluation on the held-out test set. **So the reported figures are not selection scores** — the defect that capped entries 80 and 81.

**A logistic regression comparator runs throughout**, in every table, at both time points, and in the decision curve analysis. **This is the comparator that matters** (technique 347), and unlike entry 84 the paper foregrounds rather than buries it — and reports honestly that logistic regression actually **won** the baseline-only comparison at 0.746 against Random Forest's 0.736.

**The full metric set is reported for all five models at both time points** — AUROC with intervals, sensitivity, specificity, accuracy, PPV, NPV and F1. **I rebuilt all ten test-set rows from sensitivity, specificity and prevalence, and every one reconciles exactly.** After yesterday's two inconsistencies this is worth saying plainly: **this paper's performance table is internally consistent throughout.**

**Figure 4 is the best thing in the study and it reconciles exactly.** The four-group stratification sums to 317 patients and 236 responders, matching Table 2 precisely. **And substantively it answers the strongest objection to the whole paper**, as Section 4 explains.

**The algorithm choice is justified rather than assumed** — explicitly on grounds of sample size and overfitting risk, with deep learning explicitly declined. **That is a sentence most papers skip.**

**And the handling of two awkward findings is exemplary.** The **74% response rate** is higher than most reports, and the paper says so, offering its tertiary-care setting and proactive monitoring as the explanation. The **SLEDAI result** — higher baseline disease activity predicting *better* response — is flagged as **"unexpected"** and **"not been previously reported"**, with a mechanism offered as hypothesis *and* an alternative explanation named: **"it could also reflect a unique characteristic of our tertiary care cohort."** **Compare entry 77's unremarked backwards SHAP directions and entry 84's LDL cholesterol.** This is how an anomaly should be reported.

**The limitations are real and specific** — single centre, biopsy selection bias, SHAP as post-hoc only, and a genuinely sophisticated point about individualised real-world treatment that "could not be fully incorporated into the current models."

**So why not a 4.**

**The headline rests on about 24 events.** Because 74% responded, the predicted class is treatment *failure*. Reconstructing from the paper's own figures, the 3-month test set is about **95 patients containing roughly 24 failures.** **That is the entire evidential basis of the 0.862** — and it is why the interval spans **0.775 to 0.949**, a width of 0.174. I confirmed by Hanley–McNeil that about 24 events and 71 non-events produce an interval of roughly that width. **"400 patients" is the cohort; 24 is the estimate.**

**One train/test split, with no stability analysis.** Hyperparameter tuning used repeated cross-validation, which is correct, but **the final 0.862 is a single draw from a single 70/30 split** (technique 306). With 24 test events a different split could move it materially. **Entry 83 ran its whole pipeline 1,000 times; here there is nothing.**

**The central claim is never formally tested.** The paper's thesis is that adding 3-month data **"markedly improved"** performance. **But no paired comparison is reported** — no DeLong test on the same patients, no NRI, no IDI. And **the two models are not even built on the same population**: baseline-only on 400, with-3-month on 317. Their intervals also overlap (0.643–0.829 against 0.775–0.949). **The direction is well supported by other evidence in the paper** — Figure 4's 91.0% against 44.9%, the risk ratio, and logistic regression improving from 0.746 to 0.826 on its own terms — **but the specific incremental-value claim is asserted rather than quantified.** Entry 84, for all its faults, computed NRI and IDI.

**Calibration is reported but not estimated.** Calibration curves and Brier scores, with **no slope, no intercept, no observed-to-expected ratio.** And converting the Brier tells a flatter story: **0.134 on the test set against 0.1902 for a model that just announces the base rate — about a 30% improvement.** The training Brier of **0.008** sits next to a training AUROC of **100%**, so it is memorisation rather than calibration evidence. **And SMOTE shifts predicted probabilities away from the true prevalence with no recalibration step reported**, so the Brier scores are computed on distorted probabilities. **This is better than entry 84, which reported no calibration number at all, and clearly below entry 83's slope of 1.011 with a 0.085-wide interval.**

**The 100% training AUROC goes unremarked.** Random Forest scored exactly **100.00%** on its training data in both model versions. **That is memorisation**, with gaps to test of **26.4** and **13.8** points. **The paper correctly headlines the test figures, so nothing is overclaimed — but a 100% deserved a sentence**, particularly since the same figure shows logistic regression scoring **69.07% training against 74.60% test**, a *negative* gap, which is what a model that has not overfitted looks like.

**The predictor and the outcome are the same measurement nine months apart.** Response is *defined* by urine protein below 0.5; the top predictor is urine protein at 3 months, whose median in the eventual-responder group was **0.54** — at the threshold. **Figure 4 largely rescues this** (see Section 4), but the framing "accurately predicts 12-month response" overstates what a measurement that overlaps the outcome definition can establish.

**83 patients (20.75%) vanish from the 3-month analysis and are never characterised.** And the pattern is strange: only **6 (1.5%)** are missing at 6 months. **The 3-month visit — the entire subject of the paper — was missed nearly 14 times more often than the later one**, and those patients fall outside the stated imputation rule, so they were dropped. **Entry 83's standard of characterising the excluded with standardized differences is not met.**

**A treatment imbalance is reported and never discussed.** **Cyclophosphamide went to 50.0% of non-responders against 30.41% of responders, p < 0.001.** The obvious reading is confounding by indication — sicker patients got the harder drug. **The paper reports it once and never returns to it**, though it does acknowledge the general problem in its limitations.

**Two smaller defects.** The Results text **reverses cyclophosphamide and mycophenolate** relative to Table 1 in its first sentence. And the primary outcome is defined in **"g/g"**, the unit of a protein-to-creatinine ratio, while the measured variable is 24-hour total protein in grams.

**Single centre, no external validation** — stated, and named as required before implementation. **No reporting guideline named.** **And funding, conflicts and ethics are all absent from the retrievable text.**

**Why not 2.** Entry 84 scored 2 because its headline was contradicted by its own sensitivity figure, its explanation named a null variable, its table did not reconcile, and its tool was already public. **None of that applies here.** Every table reconciles, the strongest predictor is genuinely and strongly associated with the outcome, the comparator is the right one, selection was in the training set, and nothing is deployed. **What is claimed is close to what is shown.**

**What would make this a 4, concretely.** **Report a paired comparison of the baseline and 3-month models on the same patients** — a DeLong test or NRI/IDI — which is the paper's central claim and needs no new data. **Report the calibration slope and intercept**, and recalibrate after SMOTE. **Repeat the train/test split many times and report the spread of the AUROC.** **Characterise the 83 patients missing 3-month data.** **And discuss the cyclophosphamide imbalance.** **All five use data the authors already have.** External validation would take it further still.

## 4. The Editor's Concerns

**1. The predictor and the outcome are the same measurement at two times — and this is the paper's central interpretive problem.** Complete renal response is **defined** as urine protein below 0.5 with stable creatinine. The strongest SHAP predictor is **urine protein at 3 months**. And in the eventual-responder group that 3-month median was **0.54 (IQR 0.19–1.31)** — essentially *at* the defining threshold, with the lower quartile well below it. **So a substantial part of the model's accuracy is the observation that patients already in remission at 3 months are generally still in remission at 12.** That is clinically true, worth knowing, and **a different and weaker claim than predicting who will respond.** It is not leakage — the two measurements are nine months apart and nothing from month 12 entered the model — but it means "accurately predicts 12-month CRR" is a generous description of what has been shown.

**2. And Figure 4 is how the paper answers that, which is why it is the best analysis in the study.** Stratifying by baseline protein (median split) and 3-month protein (cutoff 1.3): **started high and came down, 91.0% (111/122); started low and stayed low, 88.6% (62/70); started high and stayed high, 63.9% (23/36); started low and stayed high, 44.9% (40/89).** **The best-performing group is not the always-low group — it is the group that fell.** If the model were only tracking "low stays low," that could not happen. **So the reduction carries information beyond the level reached**, and the paper's emphasis on early proteinuria *reduction* is earned. **I verified all four cells sum to 317 patients and 236 responders exactly**, matching Table 2.

**3. A pattern inside Figure 4 that the paper does not discuss.** Among patients still high at 3 months, **those who started high did better (63.9%, n=36) than those who started low (44.9%, n=89).** That is backwards from the intuition that worse baseline disease means worse outcomes. **Two readings:** the started-high group may still have been falling steeply with further to go, or the groups may differ in how much change the arbitrary cutoffs imply — a patient at baseline 2.0 falling to 1.4 is labelled "low → high" despite barely moving, while one at 6.0 falling to 1.2 is "high → low." **I computed the intervals: 48.2–79.6% against 34.6–55.3%, which nearly touch, so the inversion is suggestive rather than established.** Worth a sentence it does not get.

**4. The limiting number is about 24, not 400.** With 74% responding, the predicted class is failure — the minority. Rebuilding the performance table from its own sensitivity and specificity figures (all ten rows reconcile, and the positive class is confirmed as non-response from a PPV of 0.403 alongside a sensitivity of 0.936), the 3-month test set is about **95 patients with roughly 24 failures.** **The headline 0.862 rests on those 24**, which is exactly why its interval spans **0.775 to 0.949.** A Hanley–McNeil calculation on 24 events and 71 non-events gives a width of about 0.197, consistent with the reported 0.174. **"A prospective cohort of 400" is the cohort; 24 is the estimate.**

**5. A training AUROC of exactly 100% is a warning light, and it is not remarked on.** Random Forest scored **100.00%** in training for both model versions; XGBoost **99.59%** and **100%**. **Gaps to test: Random Forest +26.4 points at baseline and +13.8 with 3-month data; XGBoost +33.2 and +23.2.** **The paper does the right thing in headlining the test set**, so nothing is overclaimed — but a perfect training score means the model memorised its training data, and that belongs in the text. **The instructive contrast is in the same figure: logistic regression went 69.07% training to 74.60% test — a negative gap**, which is the signature of a model that did not overfit, and it is also the model that *won* the baseline-only comparison.

**6. Calibration is reported but not estimated, and converting the Brier deflates the headline.** Calibration curves plus Brier scores, with **no slope, no intercept, no observed-to-expected ratio.** Random Forest's test Brier of **0.134** must be read against the **0.1902** that a model announcing only the base rate would achieve: **roughly a 30% improvement.** And the training Brier of **0.008** beside a 100% training AUROC is memorisation, not calibration. **Compounding this, SMOTE was applied to the training data**, which shifts predicted probabilities away from the real prevalence, **and no recalibration step is reported** — so the Brier scores are computed on distorted probabilities. **Across three consecutive entries this now forms a clean ladder: entry 83 reported a calibration slope of 1.011 with a 0.085-wide interval; entry 85 reports a Brier score and no slope; entry 84 reported no calibration number at all.**

**7. The paper's central claim is asserted, not tested.** The thesis is that 3-month data **"markedly improved"** prediction. **No paired comparison appears** — no DeLong test on common patients, no NRI, no IDI. The two models are built on **different populations (400 against 317)**, so they are not directly comparable, and their intervals overlap (**0.643–0.829** against **0.775–0.949**). **The direction is nonetheless well supported from three other angles**: Figure 4's 91.0% against 44.9%, the reported risk ratio, and logistic regression rising from 0.746 to 0.826 within its own model family. **So the finding is probably right and the specific claim of incremental value is unquantified** — which is striking given that entry 84, a far weaker paper, computed NRI and IDI.

**8. One split, no stability analysis.** Tuning used repeated 10-fold cross-validation inside the training set, which is right. **But the reported 0.862 is one draw from one 70/30 split** (technique 306), and with 24 test events the split-to-split variation could be large. **Entry 83 repeated its entire pipeline 1,000 times and reported the spread at cutpoint, metric and patient level. Here there is nothing** — and it is the cheapest possible addition.

**9. A fifth of the cohort disappears from the 3-month analysis, uncharacterised, and the pattern is odd.** **317 of 400 had complete 3-month data (83 missing, 20.75%)**, against **394 of 400 at 6 months (6 missing, 1.5%)**. **The 3-month visit — the subject of the paper — was missed nearly 14 times more often than the later one.** That is the reverse of ordinary attrition, and it is unexplained. **The stated imputation rule covers only variables missing under 5%, so these 83 were excluded rather than imputed**, and nothing is reported about how they differed. **Given that the entire thesis concerns the 3-month milestone, the patients with no 3-month measurement are precisely the group whose exclusion could bias the result.** Response rates in the reduced population match the whole cohort closely (74.45% against 74.0%), which is reassuring but not sufficient.

**10. A treatment imbalance that points at confounding by indication, reported once and dropped.** **Cyclophosphamide was given to 50.0% of non-responders against 30.41% of responders (p < 0.001)**, in a cohort where the paper itself says treatment was "individualized and dynamically adjusted." **The natural reading is that sicker patients received the more aggressive drug**, so the association runs from severity to both treatment and outcome. **The paper notes the imbalance and never returns to it.** Credit where due: it does name the general problem in its limitations, and cyclophosphamide does not appear among the final predictors. **But the specific imbalance is large, significant, and in a treatment variable, and deserved more than one sentence.**

**11. SLEDAI is the mirror image — and here the paper handles it well.** Higher baseline disease activity emerged as an independent **protective** factor, which is counter-intuitive. **Table 1 shows it was not significant univariately (16 against 14, p = 0.062)**, so the finding rests on multivariable adjustment of a univariately-null variable — and it sits slightly oddly with the stated selection rule of univariate significance in the training cohort. **But the paper flags it as "unexpected" and "not been previously reported," offers a mechanism as hypothesis (more severe activity prompting more aggressive therapy), and names the alternative explicitly: "it could also reflect a unique characteristic of our tertiary care cohort."** **That is the correct treatment of an anomaly, and it is what entries 77 and 84 failed to do.**

**12. A text-versus-table contradiction.** The Results text states **"cyclophosphamide in 180 patients (45%), mycophenolate mofetil in 142 (35.5%)"**, while **Table 1 gives mycophenolate 180 (45.00%) and cyclophosphamide 142 (35.50%)** — the two drugs reversed. A later sentence in the same section (**"a higher proportion of non-CRR patients receiving CYC (50% vs 30.4%)"**) matches the table, and the table's own rows sum correctly (90 + 52 = 142; 140 + 40 = 180). **So the error is in the first sentence.** It does not affect any result, but it is the kind of slip that a proofread catches.

**13. A unit mismatch in the primary endpoint.** Response is defined as urine protein below **"0.5 g/g"** — the unit of a protein-to-creatinine **ratio**. But the measured variable throughout is **24-hour urinary total protein**, reported in grams, with the Figure 4 cutoff given as **"1.3 g/24h."** **KDIGO 2021 states complete response as proteinuria below 0.5 g/g by urine protein-creatinine ratio, so the paper has imported a ratio-based threshold and applied it to a 24-hour collection.** The two are numerically similar in practice and the conclusions are unlikely to change, **but the study's primary endpoint is stated in units that do not match the variable actually measured.**

**14. The reported risk ratio does not quite reproduce.** The paper gives **1.89 (95% CI 1.59–2.26)** for achieving response with low 3-month protein. **From Figure 4's own cells — 173 of 192 against 63 of 125 — I get 1.79.** That sits comfortably inside the reported interval, so the two are compatible; the point estimate may have been computed on all 400 rather than the 317 with 3-month data. **A minor discrepancy, recorded rather than ignored.**

**15. Single centre, no external validation, and the model is not published in usable form.** The limitations name external validation in multiethnic multicentre cohorts as necessary "before clinical implementation," which is correct. **And unlike entry 84, nothing has been deployed** — no calculator, no public tool. **But neither are the model's coefficients or decision rules published**, and the two multivariable regression tables sit in an unreachable supplement, so **no reader can compute a prediction or check the model independently.**

**16. No reporting guideline named — and after three consecutive entries the running observation is now fully triangulated.** **TRIPOD** applies directly here and is not mentioned. The three-entry sequence: **entry 83 named no guideline and satisfied nearly every TRIPOD item in substance**, calibration slope included; **entry 84 claimed STROBE and TRIPOD and missed TRIPOD's core items** — no missing-data reporting, no calibration slope, no usable model; **entry 85 names no guideline and lands in between** — missing data addressed and collinearity examined and selection correctly placed, but calibration reported without a slope, the model not presented in usable form, and the 83 excluded patients uncharacterised. **Three papers, three different combinations of claim and substance, decoded on three consecutive days. The rule stands: the checklist is a claim about intent and tells you nothing about what was done. Read the methods.**

## 5. Statistics Spotlight

Three concepts, numbered from 350 in the running list in `queue.md`. The first is the conceptual heart of the paper and the paper's own best analysis resolves it.

**When your predictor and your outcome are the same measurement at two different times, "prediction" is partly persistence — and a two-by-two of level against change is how you find out.**

This study predicts **complete renal response at 12 months**, which is **defined** as urine protein below 0.5 with stable kidney function. Its strongest predictor is **urine protein at 3 months.**

**So the headline is: we predict whether protein will be low later, using how low protein is now.**

**And here is how close that is.** In the group who eventually achieved response, median 3-month protein was **0.54** — essentially *at* the 0.5 threshold that defines the outcome, with a quarter of them already at 0.19 or below. In the non-response group it was **2.75**. **Many of the eventual responders had already met the proteinuria criterion at 3 months.**

**Why this matters, and why it is not cheating.** Nothing from month 12 entered the model; the two measurements are nine months apart; this is a legitimate prospective design. **But there are two very different claims available, and they are easy to confuse.** The strong claim is *we can tell in advance who will respond.* The weak claim is *people who are already better tend to stay better.* **A model built this way will score well on the second claim even if it knows nothing about the first** — because medical measurements are autocorrelated. Today's blood pressure predicts next year's blood pressure. Today's weight predicts next year's weight. **That is a fact about measurements persisting, not about a model understanding anything.**

**Now the test — and this paper ran it.** Split patients two ways at once: by **where they started** and by **where they got to.** Four boxes:

- **Started high, came down low: 91.0%** responded (111 of 122)
- **Started low, stayed low: 88.6%** (62 of 70)
- **Started high, stayed high: 63.9%** (23 of 36)
- **Started low, stayed high: 44.9%** (40 of 89)

**Read the top two rows against each other.** If the model were only detecting persistence — low protein stays low — **the always-low group should do best.** It does not. **The group that started badly and improved did best of all**, 91.0% against 88.6%.

**That is the whole answer.** The **change** carries information over and above the **level**. Early reduction in protein is genuinely prognostic, not merely a restatement of being well already. And the worst group — 44.9% — is the one that started *mildly* and failed to improve, which no persistence story predicts.

**The everyday version.** You want to know which students will pass the final exam, and your predictor is their mark on a test three months earlier. Of course it works — **but mostly because good students stay good.** To find out whether the mid-term told you something *extra*, split four ways: strong-and-stayed-strong, weak-but-improved, strong-but-slipped, weak-and-stayed-weak. **If "weak but improved" beats "strong and stayed strong," then improvement is the real signal and you have learned something about trajectory, not just about talent.** That is precisely the comparison this paper makes and wins.

**Watch out for:** any model whose top predictor is an earlier measurement of its own outcome — "baseline HbA1c predicts diabetes control," "early tumour shrinkage predicts response," "3-month proteinuria predicts remission." **Three questions. Is the predictor the same quantity as the outcome, measured earlier? How close is the predictor's value to the threshold that defines the outcome? And did the paper separate the level from the change?** **If the answer to the last is no, the "prediction" may be nothing more than autocorrelation** — and the way to settle it costs nothing more than a two-by-two table.

**A Brier score means almost nothing until you divide it by the base-rate Brier.**

This paper reports **Brier scores** as its calibration evidence: **0.134** for Random Forest on the test set and **0.008** in training.

**What a Brier score is.** For each patient the model states a probability; you square the gap between that probability and what actually happened (1 or 0); you average over everyone. **Lower is better, and 0 is perfect.** It bundles two things — whether the model ranks patients correctly, and whether its probabilities are honest numbers.

**Why 0.134 does not speak for itself.** Consider the laziest possible model: it ignores every patient and announces the known base rate, **"everyone has a 25.55% chance of not responding."** **Its Brier score is the prevalence times one minus the prevalence: 0.2555 × 0.7445 = 0.1902.**

**So the floor is not zero. It is 0.1902.** And the model scored 0.134.

**The Brier skill score** makes this explicit: one minus your Brier divided by the no-skill Brier. **1 − 0.134 ÷ 0.1902 = 0.296.** **The model's probabilities are about 30% better than announcing the base rate.** That is real, and it is a much flatter statement than an AUROC of 0.862 suggests. For comparison, logistic regression's test Brier of 0.160 gives a skill score of **0.159** — about 16%.

**And now the training Brier, which is the instructive one.** **0.008** looks spectacular. It sits beside a **training AUROC of exactly 100%**. **Those two facts together mean one thing: the model memorised its training data.** A Brier near zero on data you fitted is not calibration evidence; it is the same memorisation showing up in a second metric.

**One further complication specific to this paper.** **SMOTE** was applied to the training data — synthesising extra examples of the minority class to balance it. **That is correct practice for the ranking problem and it systematically distorts the probabilities**, because the model now believes failure is far commoner than 25.55%. **Fixing this requires a recalibration step, and none is reported**, so the Brier scores are computed on probabilities shifted by the resampling. Entry 77 hit this same problem from the other side; **entry 83 solved it by fitting its calibration layer on unweighted data so the probabilities matched the real prevalence.**

**The everyday version.** A weather forecaster announces a Brier score of 0.134 for predicting rain. **Impressive?** It depends entirely on the climate. **In a desert where it rains 5% of days, simply saying "5%" every day scores 0.0475 — far better than 0.134, with no skill whatsoever.** In a place where it rains half the time, saying "50%" scores 0.25, so 0.134 is a genuine achievement. **The same number is excellent or embarrassing depending on the base rate, and you cannot tell which without being told it.**

**Watch out for:** a Brier score reported alone, or offered as the only calibration evidence. **Three habits. Compute the no-skill Brier — prevalence times one minus prevalence — and take the ratio.** **Ask for a calibration slope and intercept as well**, because Brier mixes ranking and probability accuracy and cannot separate them. **And if any resampling or class-weighting was used, ask what recalibration followed**, because the probabilities will otherwise be systematically wrong even when the ranking is right.

**The limiting number is events, not patients — and a train/test gap is the quantity to read.**

The paper studies **400 patients.** That sounds comfortable. **The estimate rests on about 24.**

**Why.** The outcome is complete renal response, achieved by **74%** of patients. So the thing the model has to detect is the *minority* — the **26%** who fail. **And precision in a prediction problem is governed by the number of events in the smaller class, not by how many people you enrolled.**

**Working it through from the paper's own numbers.** The test set was 30% of the analysis population. The 3-month analysis used **317** patients, so the test set is about **95**, of which about **25.55%** — roughly **24** — were failures. **I checked this by rebuilding all ten reported test rows from sensitivity, specificity and prevalence; every one reconciles, which confirms both the test-set size and that the "positive" class really is non-response.**

**And that is precisely why the headline interval is so wide.** The Random Forest's AUROC is **0.862 with a 95% interval of 0.775 to 0.949** — a span of **0.174**. A standard calculation for an AUROC with 24 events and 71 non-events gives a width of about 0.197, consistent with what is reported. **Read plainly: the true performance is somewhere between "decent" and "near-perfect," and 400 patients were not enough to narrow it further, because only 104 of them failed and only about 24 of those landed in the test set.**

**Now the companion diagnostic: the train/test gap.** From the figure descriptions, **Random Forest scored exactly 100.00% on its training data** in both model versions, against test scores of 73.63% and 86.22% — **gaps of 26.4 and 13.8 points.** XGBoost: 99.59% to 66.35%, and 100% to 76.85% — gaps of **33.2** and **23.2**.

**A model that scores 100% on data it was fitted to has memorised that data.** For an unconstrained Random Forest this is expected behaviour, not misconduct — but it means **the training number carries no information about performance** and the gap is what you should look at.

**And the contrast inside the same figure is the lesson.** **Logistic regression scored 69.07% in training and 74.60% in testing — a negative gap.** It did slightly *better* on data it had never seen. **That is what a model with too few parameters to memorise anything looks like** — and it was also the model that *won* the baseline-only comparison.

**The everyday version.** A student who scores 100% on the practice paper they have already seen the answers to has told you nothing about the exam. **A student who scores 69% on practice and 75% on the real exam has told you they actually learned the material.** The practice score is not the finding; **the gap between practice and exam is.**

**Watch out for:** any reported training-set performance, and especially a perfect or near-perfect one. **Three questions. How many events are in the test set — not how many patients are in the study?** **How wide is the interval, and does that width match the event count?** **And what is the gap between training and test performance for each model?** **A large gap means the model memorised; a perfect training score means it memorised completely; and a negative gap, counter-intuitively, is the most reassuring thing on the page.**

## 6. Jargon Translator

**Systemic lupus erythematosus (SLE, lupus)** — a disease in which the immune system attacks the body's own tissues, affecting skin, joints, blood, kidneys, lungs and brain.

**Lupus nephritis (LN)** — lupus attacking the kidneys. Affects **35%–60%** of lupus patients, usually within five years, and is the main route to kidney failure.

**Complete renal response (CRR)** — the treatment goal: kidneys calm enough that protein stops leaking into urine. **Defined here as urine protein below 0.5 with creatinine normal or no more than 115% of baseline.**

**24-hour urinary total protein (24hUTP)** — all the protein in a full day's urine, collected and measured. **The central measurement in this paper**: it defines the outcome *and* is the strongest predictor.

**Protein-to-creatinine ratio (g/g)** — a different way of measuring urine protein, from a single sample rather than a full day. **The paper's stated threshold uses this unit while its measurements use the 24-hour collection** — a mismatch noted in Section 4.

**Proteinuria** — protein in the urine. The hallmark of kidney damage in lupus, and what treatment aims to reduce.

**Serum creatinine (Scr) and eGFR** — a waste product the kidneys clear, and the filtration rate estimated from it. **Together, the standard measure of how well kidneys are working.**

**Induction therapy** — the intensive first phase of treatment aimed at bringing active disease under control. **Its start was this study's baseline.**

**SLEDAI** — a score summing up how active lupus is across the whole body. **Median 16 here.** Counter-intuitively, a *higher* baseline score predicted *better* kidney response — which the paper flags as unexpected.

**KDIGO 2021** — the international kidney guideline that supplied the response definition.

**ISN/RPS classification** — the system for grading what lupus has done to the kidney on biopsy. **54% of patients here had a biopsy; the rest declined.**

**Cyclophosphamide, mycophenolate mofetil** — two standard immune-suppressing drugs. **Cyclophosphamide is generally the more aggressive option**, which is why its imbalance between groups matters.

**Prospective cohort** — a study that enrols patients and follows them forward in time, collecting data as it happens. **Stronger than looking back through old records**, and rare in this reading list.

**Random Forest** — many decision trees averaged together. **Here it scored 100% on its own training data, which means it memorised it.**

**XGBoost, support vector machine, Elastic Net** — three other standard algorithms. **Elastic Net is a penalised regression that shrinks unhelpful variables toward zero.**

**SMOTE** — a method that invents extra synthetic examples of the rarer outcome to balance the training data. **Applied to training only here, which is correct** — but it distorts predicted probabilities unless you recalibrate afterwards.

**Training set / test set** — the data a model learns from, and the untouched data used to judge it. **70/30 here, split once.**

**Repeated 10-fold cross-validation** — splitting the training data many ways to choose settings without peeking at the test set. **Correctly used here for tuning.**

**AUROC** — the chance the model scores a patient who will fail above one who will respond. 0.5 is a coin flip. **0.862 here, with the outcome's minority class as the target.**

**Positive predictive value (PPV) and negative predictive value (NPV)** — of those flagged, how many really fail; of those cleared, how many really respond. **0.556 and 0.931 for the best model.**

**F1 score** — a single number combining the share of failures caught and the share of flags that were right. **0.667 here.**

**Brier score** — average squared error of the predicted probabilities. **Lower is better, but it must be read against the base rate** — technique 351.

**Brier skill score** — your Brier divided by the no-skill Brier, subtracted from one. **About 0.30 here: roughly 30% better than just quoting the base rate.**

**Calibration slope** — the standard check on whether predicted probabilities are honest. **Not reported here** — the gap this entry shares with entry 84 and that entry 83 filled.

**Decision curve analysis (DCA)** — asks whether using the model beats treating everyone or nobody, across different levels of concern. **Performed here against treat-all, treat-none and logistic regression.**

**SHAP** — attributes a prediction to its inputs. **Describes the model, not the biology** — and the paper says so itself, calling it "a post-hoc tool."

**Variance inflation factor (VIF)** — a measure of how much variables overlap with each other. **Examined here, and acted on** by dropping albumin and creatinine.

**Risk ratio (RR)** — how many times more likely one group is to have an outcome than another. **1.89 reported here; 1.79 when recomputed from the paper's own four cells.**

**TRIPOD** — the reporting guideline for prediction-model studies. **Not named here.**

## 7. What You Can (and Can't) Say

**You can say:**

"In a prospective single-centre cohort of 400 patients with active lupus nephritis followed for 12 months, 296 (74%) achieved complete renal response."

"Models using baseline information alone discriminated poorly, with test-set AUROCs of at most 0.746; adding 3-month follow-up data raised the best model's test-set AUROC to 0.862 (95% CI 0.775–0.949)."

"The Random Forest model's test-set sensitivity was 83.3%, specificity 77.1%, accuracy 78.7%, PPV 0.556, NPV 0.931 and F1 0.667, with a Brier score of 0.134."

"SHAP identified 3-month urine protein as the most influential predictor, followed by disease duration, the percentage reduction in urine protein by 3 months, baseline urine protein, and 3-month C3."

"Differences between responders and non-responders in urine protein, albumin and C3 were already significant at 3 months and did not widen further by 6 months."

"Patients with 3-month urine protein at or below 1.3 g were about 1.9 times as likely to achieve complete response; stratified by both baseline and 3-month levels, response rates were 91.0% for high-then-low, 88.6% for low-then-low, 63.9% for high-then-high and 44.9% for low-then-high."

"Variable selection was performed in the training cohort, collinear variables were excluded after examining correlations and variance inflation factors, and SMOTE was applied only to the training data."

"The authors state that external validation in multiethnic, multicentre cohorts is necessary before clinical implementation."

**You cannot say:**

"The model accurately predicts who will respond to treatment." **The strongest predictor is urine protein, which is also what defines the outcome** — and the eventual responders' median 3-month protein was 0.54, essentially at the 0.5 threshold. **Much of the performance reflects patients already in remission staying in remission.**

"Three-month data markedly improves prediction." **The direction is well supported, but the improvement was never formally tested** — no paired comparison on the same patients, no NRI or IDI — and the two models were built on different populations (400 and 317) with overlapping confidence intervals.

"The model achieves an AUROC of 0.862." **Better stated as 0.862 with a 95% interval of 0.775 to 0.949**, resting on roughly 24 treatment failures in a test set of about 95.

"This was validated in 400 patients." **It was tested in about 95**, of whom about 24 had the outcome being predicted, from a single 70/30 split.

"The model is well calibrated." **No calibration slope, intercept or observed-to-expected ratio is reported.** The test Brier of 0.134 compares against 0.1902 for simply announcing the base rate — about a 30% improvement — and SMOTE distorted the probabilities with no recalibration reported.

"Random Forest achieved near-perfect performance." **It achieved exactly 100% on its own training data, which means it memorised it.** Its test performance was 0.862.

"Machine learning outperformed conventional statistics." **Not at baseline** — logistic regression won that comparison at 0.746 against Random Forest's 0.736. With 3-month data the gap was 0.862 against 0.826, with heavily overlapping intervals.

"Higher baseline disease activity protects the kidneys." **The paper reports this and explicitly flags it as unexpected**, offering both a mechanism and the alternative that it reflects their tertiary-care cohort. It was also not significant univariately (p = 0.062).

"Cyclophosphamide worsens renal outcomes." **It was given to 50% of non-responders against 30% of responders — almost certainly because sicker patients received it.** This is confounding by indication, not a drug effect.

"74% of lupus nephritis patients achieve complete response." **That is this cohort's rate**, which the paper itself notes is higher than most reports and attributes to its tertiary-care setting with close monitoring and proactive adjustment.

"The tool can be used in clinic." **Single centre, no external validation, nothing deployed, and the model's coefficients are not published** — so no reader can even compute a prediction.

**The honest one-sentence version:** *a careful prospective study that asks a genuinely useful question — how early can you tell whether lupus nephritis treatment is working — and answers it defensibly at three months, with one excellent four-group analysis showing that the fall in urine protein carries information beyond the level reached, limited by a headline estimate resting on about 24 treatment failures from a single split at one hospital, a calibration claim supported only by a Brier score that is about 30% better than quoting the base rate, an unremarked training AUROC of exactly 100%, and a central incremental-value claim that is asserted rather than tested.*

## 8. Bottom Line for Your Life

**If you or someone you love has lupus nephritis:** the useful fact here is one your kidney doctor already works with, and it is worth knowing. **The first three months of treatment carry a lot of information.** In this study, patients whose urine protein had fallen substantially by three months did well — **91% of those who started high and came down achieved full remission at a year** — while those whose protein had not moved did considerably worse. **This does not mean a poor three-month result is a verdict.** Even in the worst group, 45% still achieved remission by 12 months, and the paper is careful to say that some immunosuppressant drugs simply take longer to work and that **whether to change treatment at three months "requires further evaluation."** **What it does mean is that the three-month visit and the urine protein test at that visit matter — so keep the appointment and do the collection properly.**

**If you treat lupus nephritis:** the clinically actionable finding is the four-group stratification, not the AUROC. **Three-month urine protein below about 1.3 g was associated with roughly 90% eventual complete response, and above it with roughly 50%** — and crucially, **where the patient got to mattered more than where they started.** A patient who began with severe proteinuria and fell steeply did better than one who began mildly and did not move. **That reframes the three-month visit from a progress check into a decision point.** The cautions are the paper's own: single centre, a 74% response rate higher than most cohorts, and no evidence yet that acting on the prediction improves anything — which the authors name as the next study to do.

**If you build prediction models, this entry offers one test to copy and three cheap additions.** **The test to copy is Figure 4.** When your predictor is an earlier measurement of your own outcome — and in medicine it very often is — **split patients by starting level and by level reached, and look at all four boxes.** If the group that improved beats the group that was always fine, the change carries real information; if not, you have measured autocorrelation. **It costs one table and it is the difference between a defensible claim and an overstated one.** **The three additions: convert your Brier score into a skill score against the base rate before calling anything well calibrated; report a calibration slope, and recalibrate if you used SMOTE or class weighting; and repeat your train/test split many times and report the spread rather than one number.**

**And the habit worth taking from this entry regardless of field.** **Count the events, not the people.** This study has 400 patients, which sounds solid, and its headline estimate rests on roughly 24 treatment failures in a held-out test set. **That is why its confidence interval runs from 0.775 to 0.949 — a range covering "useful" to "almost perfect."** Whenever you see a prediction model, find the number in the smaller outcome class and in the test set specifically. **If the paper does not make that number easy to find, work it out from the sensitivity and specificity — and if the interval is wide, the event count is usually the reason.**

**One more, about perfect scores.** When a paper reports how its model did on the data it was trained on, **a score of 100% is not an achievement — it is a statement that the model memorised its homework.** The number to read is the gap to the test set. Here that gap was 26 points for one model and 14 for another. **And the most reassuring thing on the whole page was the plain logistic regression scoring 69% on training and 75% on the test — doing better on data it had never seen, which is what a model that genuinely learned something looks like.**

**If you are reading the coverage:** expect "AI predicts lupus kidney treatment response at three months" with the 0.862 figure. **Three things will likely be missing.** That the strongest predictor is the same measurement that defines the outcome, so a good part of the result is that people already in remission stay in remission — a limitation the paper's own four-group analysis addresses better than the headline does. That the estimate rests on about 24 treatment failures, which is why its interval is nearly 0.2 wide. And that the claim of improvement over baseline-only models, which is the paper's whole thesis, was never formally tested.

**This is education, not medical advice.** Nothing here should change what you do about your own treatment, and no model discussed here is validated for clinical use. Decisions about immunosuppressive therapy for lupus nephritis belong with your own rheumatologist or nephrologist.

---

## Appendix: the pre-registered questions, verification, landmark screen, and status on 2026-11-22

**Both pre-registered questions, answered — the first affirmatively and with a wrinkle, the second with a clear place on a three-entry ladder.** Set yesterday, written down before reading.

**(1) "Does the 3-month milestone add anything over baseline variables alone — is this predicting CHANGE or re-predicting a LEVEL?"** — **Yes, it adds, and the paper makes this its headline: baseline-only test AUROC at most 0.746 against 0.862 with 3-month data.** **But the change-versus-level question is the sharper one and the answer is "both, and the paper proves the change part itself."** The level objection is serious: the outcome **is** urine protein below 0.5, the top SHAP predictor **is** urine protein at 3 months, and the eventual-responder group's 3-month median was **0.54** — at the threshold. **So much of the discrimination is persistence.** **What rescues it is Figure 4**, which stratifies by baseline *and* 3-month level: **high→low 91.0% (111/122) beats low→low 88.6% (62/70)**, so the group that fell did better than the group that was always fine — **which persistence alone cannot produce.** **I verified the four cells sum to 317 patients and 236 responders exactly.** **The wrinkle the paper does not discuss:** among those still high at 3 months, **started-high did better (63.9%, n=36) than started-low (44.9%, n=89)** — intervals 48.2–79.6% against 34.6–55.3%, nearly touching, so suggestive rather than established. **And the incremental-value claim itself was never formally tested** — no paired AUROC comparison, no NRI, no IDI, and the two models sit on different populations (400 against 317) with overlapping intervals.

**(2) "Is calibration reported as a slope with an interval or only as a plot — and with n=400 and a 12-month outcome, how many events are there to estimate it from?"** — **Neither extreme: calibration curves plus Brier scores, with NO slope, NO intercept and NO observed-to-expected ratio.** **And converting the Brier deflates it: Random Forest's test score of 0.134 against the 0.1902 a base-rate-only model achieves is a skill score of just 0.296 — about a 30% improvement.** The training Brier of **0.008** sits beside a **training AUROC of exactly 100%**, so it is memorisation rather than calibration evidence. **Compounding it, SMOTE shifted the training prevalence with no recalibration step reported.** **On the event count: 104 non-responders in all, and about 24 in the 3-month test set of roughly 95** — which is why the headline interval spans **0.775–0.949**, width 0.174, matching a Hanley–McNeil estimate of about 0.197 for 24 events and 71 non-events. **This places entry 85 precisely in the middle of a three-entry ladder: entry 83 reported a calibration slope of 1.011 with a 0.085-wide interval; entry 85 reports a Brier and no slope; entry 84 reported no calibration number at all.**

**Arithmetic verified today — everything reconciles, which after yesterday is worth stating plainly.** **Cohort:** 296 + 104 = **400**; CRR **74.0%**; female 338 = **84.50%**; treatment-naive 239 = **59.75%**; biopsy 216 = **54.00%** — all exact. **Immunosuppressants:** 180 + 142 + 78 = **400**; CYC 90 + 52 = **142**; MMF 140 + 40 = **180**. **Follow-up populations:** 3-month 236 + 81 = **317** (74.45% / 25.55% exact); 6-month 292 + 102 = **394**. **Table 3: I rebuilt all TEN test-set rows from sensitivity, specificity and prevalence — every one reconciles** (PPV, NPV, accuracy and F1 all within 0.025), which also confirms the test-set sizes (~120 baseline, ~95 at 3 months) and establishes that **the positive class is non-response**, from a PPV of 0.403 alongside a sensitivity of 0.936. **Figure 4: 122 + 70 + 36 + 89 = 317** and **111 + 62 + 23 + 40 = 236** — both exact. **Brier skill scores:** RF test **+0.296**, RF training **+0.958**, LR test **+0.159**, LR training **+0.359**, against a no-skill Brier of **0.1902**. **Train-test gaps:** RF **+26.37** and **+13.78** points, XGBoost **+33.24** and **+23.15**, logistic regression **−5.53** and **+8.08**. **Hanley–McNeil on 24 events and 71 non-events gives an interval width of 0.197 against the reported 0.174** — consistent. **No arithmetic error of my own, and no correction of mine to record.**

**Three discrepancies found in the paper, all minor and all recorded.** **(a) A text-versus-table contradiction:** the Results text says "cyclophosphamide in 180 patients (45%), mycophenolate mofetil in 142 (35.5%)" while **Table 1 reverses the two drugs**; a later sentence in the same section agrees with the table and the table's rows sum correctly, **so the error is in the first sentence.** **(b) A unit mismatch in the primary endpoint:** complete response is defined as urine protein below **"0.5 g/g"** — a protein-to-creatinine **ratio** unit — while the measured variable throughout is **24-hour total protein in grams**, with the Figure 4 cutoff given as "1.3 g/24h"; KDIGO 2021's threshold is PCR-based, **so a ratio threshold has been applied to a 24-hour collection.** Numerically similar in practice, but the primary endpoint is stated in units that do not match the variable measured. **(c) The reported risk ratio of 1.89 (95% CI 1.59–2.26) recomputes to 1.79** from Figure 4's own cells (173/192 against 63/125) — inside the interval, so compatible, but not an exact reproduction; possibly computed on all 400 rather than the 317 with 3-month data.

**The missingness asymmetry, which is this entry's least-discussed real problem.** **317 of 400 had complete 3-month data (83 missing, 20.75%)** against **394 of 400 at 6 months (6 missing, 1.5%)** — **the 3-month visit was missed 13.8 times more often than the later one**, the reverse of ordinary attrition, and unexplained. **The stated imputation rule covers only variables missing under 5%, so those 83 were excluded rather than imputed, and they are never characterised.** Since the paper's entire thesis concerns the 3-month milestone, **the fifth of the cohort with no 3-month measurement is exactly the group whose exclusion could bias the central finding.** Entry 83's standard — characterise the excluded with standardized mean differences — is not met. Mildly reassuring: response rates in the reduced population track the whole cohort closely (74.45% against 74.0%).

**Positive practice worth carrying forward.** **A prospective design with a defined baseline at induction**, scheduled follow-up and a 12-month outcome — rare in this list and the reason most of entries 83 and 84's defects cannot arise here. **Variable selection explicitly performed in the training cohort**, the sentence entry 84 omitted. **Collinearity examined with Pearson correlations and VIFs and acted on** (albumin and creatinine dropped at r > 0.7) — the check entry 84 skipped with OASIS. **SMOTE applied to training only**, stated. **Hyperparameters tuned by repeated 10-fold cross-validation inside the training set**, with evaluation on held-out data. **A logistic regression comparator throughout**, in every table at both time points and in the decision curve — **and the honest report that it WON the baseline-only comparison** (0.746 against 0.736). **Full metrics for five models at two time points, all ten rows internally consistent.** **Decision curve analysis against treat-all, treat-none AND logistic regression.** **The algorithm choice justified on sample-size and overfitting grounds, with deep learning explicitly declined.** **The 74% response rate raised and explained.** **The anomalous SLEDAI finding flagged as "unexpected" with a mechanism offered as hypothesis and the cohort-artefact alternative named explicitly** — the correct treatment of an anomaly, and what entries 77 and 84 failed to do. **And a genuinely sophisticated limitation about individualised real-world treatment that "could not be fully incorporated into the current models."**

**What could not be verified.** **Funding, conflicts of interest, ethics approval, informed consent, data availability and author contributions** — none appears in the retrieved PMC body; Taylor & Francis journals normally carry these, so they are recorded as **not retrievable rather than absent**, and no funder, disclosure or approval is reported that was not seen. **Supplementary Tables 1 and 2**, costing **both multivariable regression outputs** — so the baseline and 3-month independent predictors, including the SLEDAI coefficient, cannot be checked. **All figures as images** (the descriptive captions did come through, which is how the training AUROCs, Brier scores and Figure 4 cell counts were obtained). **Any calibration slope or intercept.** **Any formal test of incremental value.** **Any characterisation of the 83 patients missing 3-month data.** **Any split-stability analysis.** **Any reporting guideline.** **And the model itself** — no coefficients or decision rules are published, so no reader can compute a prediction. **Nothing was reproduced that was not seen.**

**Reporting-guideline pattern — three consecutive entries now triangulate it completely.** 71, 73, 74, 75, 77, 78 named none; 69 named TRIPOD+AI with a deposited checklist; 70 named STROBE; **76 measured the phenomenon at 40% mean TRIPOD-LLM completeness**; 79 named six instruments and applied them; 80 named TRIPOD with a checklist; 81 named none; 82 named none visible; **83 named NO guideline and satisfied nearly every TRIPOD item in substance**, calibration slope included; **84 CLAIMED STROBE and TRIPOD and missed TRIPOD's core items**; **85 names NO guideline and lands in between** — missing data addressed, collinearity examined, selection correctly placed in the training set, **but** calibration reported without a slope, the model not presented in usable form, and the excluded 83 uncharacterised. **Three papers, three different combinations of claim and substance, decoded on three consecutive days.** **The rule is now as thoroughly established as this list can make it: naming a checklist is a claim about intent and tells you nothing about what was done. Read the methods.**

**Deferred status, 2026-11-22.** **Gait foundation model (42995231) — day 14, re-checked today, still no PMC copy**; abstract-only date **2026-11-30**, eight days out. Largest multiplicity problem this list will have faced (**1,887 of 3,210 tested phenotypes called significant**); first question remains what false-discovery-rate procedure ran across those 3,210 tests. **And today adds a fifth side to the running connection.** Entry 82 had **15 independent units dressed as 4,050**; the gait paper has **3,210 tests whose dependence structure decides whether 1,887 findings mean anything**; entry 83 is the **positive case**, identifying its independent unit and splitting on it; entry 84 is the **deployment case**, treating 208 hospitals as one centre; **and entry 85 is the event-count case — 400 patients whose headline estimate rests on about 24 treatment failures, which is why its interval is 0.174 wide.** **All five ask the same question from different directions: how many independent pieces of information were actually there?** Techniques 205, 327, 331, 343 and 352 are one idea seen five ways.

**Landmark check, 2026-11-15 → 11-22 — sixteen records, and for the first time in this run EVERY ONE had already been assessed** on 2026-11-18, 11-19, 11-20 or 11-21: the two *Nature* News items on the Riemann hypothesis and amateur astronomy (43064755, 43064747), the four earlier *Nature* AI news pieces, the *Science* editorial, the hypothalamic ageing atlas, the twisted-perovskite and Amazonian-deciduousness papers, the poxvirus structure, the generational-cognition cohort, the two *Nature Mental Health* papers now on the shelf as (L) and (M), and the remaining commentary. **No new records; nothing displaces the queue.**

**Plan set on 2026-11-22.** **Next run takes shelf item (J)** — **facial phenotyping in sickle cell disease**, PMID 43019377, PMC13759072, *PLOS Digital Health* 2026: **308 smartphone photographs**, 154 electrophoresis-confirmed cases and 154 age- and sex-matched controls aged 5 months to 19 years, recruited in **Kinshasa, DRC**; an interpretable **linear SVM with recursive feature elimination under leave-one-out cross-validation**. **Three reasons it follows today naturally.** It is a **global-health study on low-cost hardware**, the first in this list, which raises a different question from every entry so far: not whether the model is accurate but whether the alternative is anything at all. It makes **today's event-count lesson sharper still** — 308 images in total, so every performance figure rests on a few hundred observations and **leave-one-out cross-validation is the one resampling scheme whose variance behaves worst** (322, 352). And **recursive feature elimination inside leave-one-out cross-validation is a classic optimism trap**: if the feature selection ran once on all 308 images before the resampling, the reported accuracy is a selection score, not an estimate. **Two questions written down now, before reading. (1) Was the recursive feature elimination nested INSIDE the leave-one-out loop, or run once on all 308 images first (311, 331)?** **(2) The design is 154 matched cases and 154 matched controls, so prevalence is 50% by construction — what would the positive predictive value be in a real screening population, where sickle cell prevalence is a few percent (275)?** **Shelf after today: three spares — (K) next-day alcohol craving from EEG, HRV and phone sensing, (L) antidepressant versus placebo functional connectivity, (M) ADHD/anxiety transdiagnostic biotypes.**

**Standing watch item:** PM Heart trial results (protocol PMID 42893738), quarterly.
