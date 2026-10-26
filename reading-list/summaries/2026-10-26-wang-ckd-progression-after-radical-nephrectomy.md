# Identification and validation of a chronic kidney disease prediction model after radical nephrectomy: a multicenter cohort retrospective study

**Authors:** Wang X, Zhang T, Wang J, Yan Y, Wang H, Song K, Yu Y, Zhang Z, Zou B, Yao C, Zheng J, Liu J, Liu H, Zhang X, Guan C, Xu L, Zhang N, Jiao W (18 authors across eight Chinese centres — Affiliated Hospital of Qingdao University, Qilu Hospital of Shandong University, Weifang People's Hospital, Cancer Hospital of Shandong First Medical University, People's Hospital of Rizhao, Zibo Central Hospital, Linyi People's Hospital, Weihai Central Hospital — plus Juntendo University, Tokyo)
**Journal:** Annals of Medicine, 2026; 58(1): 2737504 (published 29 September 2026)
**Decoded:** 2026-10-26
**Analysis basis:** **FULL TEXT** (retrieved from PubMed Central, PMC13629762; 45,652 characters). Figures are described in the PMC rendering's alt-text and used where noted; the supplementary tables (hyperparameter search spaces, full DeLong matrices, calibration table) were not viewable, so anything living only there is marked as not retrieved.

**Source links (verified):**
- DOI: https://doi.org/10.1080/07853890.2026.2737504
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42808223/
- Full text (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC13629762/

**Basis of link verification.** Direct URL fetching is blocked from this session (`doi.org` does not resolve under the network policy here). Verification was done against the live PubMed/NLM record: a query for PMID 42808223 returned this exact title, these eighteen authors, Annals of Medicine volume 58 issue 1 article 2737504, DOI `10.1080/07853890.2026.2737504` and PMC ID `PMC13629762`; the full text was then retrieved from PubMed Central by that PMC ID and matches. Both halves of the chain were confirmed independently.

**Funding: not reported in the text provided.** **Competing interests: not reported in the text provided.** **No reporting guideline (TRIPOD or otherwise) is named.**

**Ethics:** approved by the Ethics Committee of the Affiliated Hospital of Qingdao University; individual consent waived as retrospective, with no identifiable patient information included.

> **Why this paper today.** The four deferred papers are still blocked, all re-checked this morning: Google's personal health agent (Nature, PMID 42907512), the BMJ review of LLM-trial reporting (PMID 42869550) and the Annals of Internal Medicine Choosing Wisely benchmark (PMID 42896192) have no PubMed Central copies, and the JAMA OpenEvidence study (PMID 42879271) **still serves an empty PMC body, now day 11**. This paper was spare #4, flagged in the queue four days ago for one specific reason: its internal validation AUC was 0.751 and its external AUC 0.755 — **essentially no drop**, which after a fortnight of watching every model lose ground on new data was unusual enough to be worth decoding on its own. The explanation turned out to have three parts, and the more important finding was somewhere else entirely.

---

## 1. The Gist

When a kidney has cancer, surgeons often remove the whole thing. You are then living on one kidney, and for a sizeable minority of people the remaining kidney cannot keep up: kidney function slides over the following years into what doctors call chronic kidney disease. It would be useful to know in advance who that will happen to.

Eighteen doctors across eight Chinese hospitals pulled the records of 649 such patients and built a computer model to predict it, using ten pieces of information available around the time of surgery. About a third of patients — 224 of 649 — did decline over the next three years.

The model works moderately. Shown one patient who declined and one who did not, it picks the right one about 75 times in 100.

Here is the part worth your attention. The model was built at one hospital and tested at seven others, and **the score barely changed** — 0.751 at home, 0.755 away. That almost never happens; models usually get noticeably worse somewhere new.

But the score that held steady was hiding something. The seven other hospitals had patients who were **nearly twice as likely to decline** — 46 in 100 against 24 in 100. The model was still good at putting patients in the right *order*, worst to best. It was badly wrong about the actual *numbers* it gave them, consistently telling patients their risk was lower than it really was.

So: ranking travelled, probabilities did not. The authors found this, measured it, explained exactly why, and said the model needs recalibrating before anyone uses it elsewhere. That honesty is why this is the best-graded paper in this reading list in over a week.

## 2. Study Snapshot

**Study type:** a **retrospective multicentre cohort study** used to develop and externally evaluate a clinical prediction model. Retrospective means working backwards through records already collected. The cohort structure means patients were free of the outcome at the start and followed forward in records, so the predictors genuinely precede the outcome — which, unlike yesterday's paper, makes this real prediction rather than same-day identification. On the evidence ladder, above a cross-sectional study, below a trial.

**The clinical question:** who, after having a whole kidney removed for renal cell carcinoma, will see their chronic kidney disease stage worsen within three years.

**Number of patients (n):** **649** across **eight** centres.
- **Primary cohort: 329** from the Affiliated Hospital of Qingdao University, randomly split 7:3 into **229 training** and **100 internal validation**.
- **External evaluation cohort: 320** from the other **seven** hospitals.

Those add up exactly: 229 + 100 = 329, and 329 + 320 = 649.

**The funnel, and it is a large one.** **698** patients screened at the primary centre and **748** at the external centres — **1,446 in total, of whom 649 (44.9%) were analysed.** The exclusions, primary / external: age under 18 (18 / 13), **follow-up under three years (214 / 234)**, preoperative CKD stage above 3 (36 / 27), no renal function measured at 36–39 months (43 / 97), no preoperative renal function (58 / 57). Those sum exactly to the stated 369 and 428.

**Note what the largest exclusion is.** Follow-up shorter than three years removed **30.7%** of the primary pool and **31.3%** of the external pool. People who died, moved away or stopped attending are not in this study — and for a kidney-decline outcome that is not a neutral loss.

**The outcome:** whether CKD stage went **up** (worse) by three years, graded against the 2002 KDOQI criteria, using eGFR calculated by the CKD-EPI 2021 equation. Baseline was the most recent preoperative measurement; follow-up was the measurement 36–39 months after surgery, taking the one nearest 36 months where several existed.

**How often it happened:** **224 of 649 (34.51%)** overall — and this is the number the whole paper turns on, because it was **23.7% in the primary cohort and 45.6% in the external cohort.** The external patients were **1.92 times** more likely to progress. Those rates reproduce the overall figure exactly (78 + 146 = 224).

**The ten predictors — and how they were chosen, which is the methodological high point.** Age, sex, BMI, hypertension, diabetes, preoperative serum creatinine, preoperative eGFR, **post-to-preoperative serum creatinine ratio**, tumour size, and surgical approach.

These were **prespecified from the group's own previously published single-centre study**. The paper states it directly: "Predictor selection was therefore not performed using a new data-driven feature-selection procedure in the current cohort... **No predictors were selected or excluded according to univariable P values in the current study.**" That one decision removes an entire category of optimism, and almost nothing in this reading list has done it.

**Preprocessing, in the right order.** Continuous predictors Z-scored using **means and standard deviations estimated exclusively from the training set** and applied unchanged elsewhere. **SMOTE applied exclusively to the training set**, with the internal and external cohorts keeping their real class balance. Both correct, both stated.

**Models:** LightGBM, XGBoost, random forest, support vector machine and logistic regression, with grid-search hyperparameter tuning under five-fold cross-validation on the training set, refitted on the full training set and then evaluated without further modification.

**Evaluation:** AUC with 95% intervals, accuracy, sensitivity, specificity, **paired DeLong tests for every pairwise AUC comparison in both the internal and external cohorts**, Brier scores, decision curve analysis, SHAP — and, unusually, **calibration intercept and calibration slope with confidence intervals**, with the estimation method spelled out (the intercept from a logistic regression carrying the logit of predicted probability as an offset).

**An admission most papers would not make.** The external cohort was consulted when picking the winning algorithm, and the authors say so, twice, and change their terminology accordingly: "Because results from the external cohort contributed to this comparative assessment and model selection, the external cohort is interpreted as an **external evaluation cohort rather than as independent confirmation** of a LightGBM model finalized a priori."

**Funding / competing interests / reporting guideline:** **none reported in the text provided.**

### The results

**LightGBM, across the three datasets:** training AUC **0.8604**, internal validation **0.7508** (95% CI 0.6399–0.8617) with accuracy 0.7200, external **0.7549** (95% CI 0.7022–0.8076) with accuracy 0.6813.

**All five models externally:** LightGBM 0.7549, random forest 0.7292, XGBoost 0.7187, and then a collapse — **SVM 0.5635 and logistic regression 0.5603**, both close to a coin flip.

**DeLong tests.** Internally LightGBM beat XGBoost (p = 0.0120), random forest (p = 0.0360), SVM (p = 0.0214) and logistic regression (p = 0.0067). Externally it beat XGBoost (p = 0.0397), SVM and logistic regression (both p < 0.001), but **not random forest (p = 0.1119)** — which the authors report plainly.

**Calibration, which is where the story is.** LightGBM's Brier score went from **0.1558** internally to **0.2553** externally. Its calibration intercept went from **−0.29 (95% CI −1.07 to 0.49)** — an interval comfortably containing the ideal value of zero — to **+0.61 (95% CI 0.27 to 0.95)**, an interval that **excludes zero**. A positive intercept means the model **systematically underestimated risk**, and the authors tie it directly to the cause: "consistent with the substantially higher incidence of CKD progression in the external cohort (45.6% vs. 23.7% in the primary cohort)." They add that slopes below 1 indicate overly extreme predictions and conclude this supports "the need for recalibration before application to populations with different baseline risk."

**SHAP** ranked preoperative eGFR, tumour size, the post-to-preoperative creatinine ratio, preoperative creatinine and age as the five most influential.

**The external 2×2 for LightGBM, reconstructed:** 146 progressed and 174 did not; **83 true positives, 63 missed, 135 correctly cleared, 39 false alarms** — reproducing the reported accuracy of 0.6813 exactly. The model flags 38.1% of patients, with a PPV of 0.680 against a flag-everyone baseline of 0.456.

## 3. How Strong Is This Evidence? (Grade 4/5)

**Grade: 4/5 — a modest model, built and reported with real methodological discipline, whose most valuable result is a failure it chose to measure.**

**What it genuinely supports.** That ten routinely available variables around the time of radical nephrectomy rank patients by three-year risk of kidney function decline with an AUC around 0.75, and that this ranking ability survives transfer to seven other hospitals. And — more usefully — that **the probabilities the model produces do not survive that transfer**, in a direction and magnitude predictable from the difference in how common the outcome is.

**What it does not support.** That the model's risk estimates can be used as they stand anywhere other than Qingdao. The authors say this themselves.

**Why this earns a 4, and the list is substantial.**

**Predictors were prespecified from a prior published study, with no univariable screening in this cohort.** This is the single most consequential good decision in the paper and it is rare. It means there was no feature-selection optimism to be paid later — and it is a large part of why the internal and external AUCs agree.

**Preprocessing was fitted on the training set only**, with the Z-score parameters carried over unchanged, and **SMOTE was applied only to training data** while the evaluation cohorts kept their true class balance. Getting both of these right is less common than it should be.

**Eight centres, with the external cohort drawn from seven hospitals entirely separate from the development site** — and those cohorts genuinely differ, significantly, on age, preoperative creatinine, preoperative eGFR, the creatinine ratio, sex, surgical approach and the outcome itself. That is a real test, not a formality.

**Calibration intercept and slope reported with confidence intervals, and the estimation method described** — the offset-term construction for the intercept is spelled out. Almost no paper in this reading list has done this properly, and it is what makes the central finding visible at all.

**Paired DeLong tests across all five models in both cohorts**, including the honest reporting of the one comparison that failed (LightGBM vs random forest, p = 0.1119).

**The exclusion accounting is exact**, broken down by reason and by cohort, and the components sum correctly.

**And the disclosure about model selection.** They looked at the external cohort when choosing the winner; they say so; and they **renamed the cohort** from "validation" to "evaluation" to signal it. That sentence — "rather than as independent confirmation of a LightGBM model finalized a priori" — is the kind of thing that only gets written by people trying to be understood rather than believed.

**What holds it at 4 rather than 5.**

**Nearly a third of screened patients were excluded for having less than three years of follow-up** — 214 of 698 and 234 of 748. For an outcome measured at three years this is unavoidable in design, but it is not neutral: patients who died, deteriorated into care elsewhere or stopped attending are systematically absent, and kidney decline and death are related. A further 43 and 97 were dropped for having no renal function measured in the 36–39 month window. **The surviving cohort is healthier and better-followed than the population a clinician would apply this to**, and the paper does not discuss the direction of that bias.

**One predictor is measured after the exposure it helps predict.** The **post-to-preoperative serum creatinine ratio** requires a postoperative creatinine. That is legitimate early-postoperative prediction, and clinically sensible — but it means the model cannot be used before surgery to inform the decision to operate, which is the moment a patient would most want it. The paper does not say when the postoperative value was drawn.

**The outcome is a change from a baseline that is also a predictor.** CKD stage is defined by eGFR bands, and preoperative eGFR is both an input and the thing that determines how far you are from the next band. Someone sitting just above a boundary needs only a small decline to "progress". This is the coupling problem, and the SHAP analysis ranking preoperative eGFR first is what you would expect from it. The paper does not address it.

**No reporting guideline is named**, no funding statement, no competing-interests statement.

**Where 4/5 sits.** Comparable to the propofol sedation paper three days ago: a modest result reported with enough care that you can check it, by authors who tell you where their own evidence is weak. Not a 5 because of the attrition, the unaddressed baseline coupling, and the missing declarations — none of which touches the central finding.

## 4. The Editor's Concerns

**Discuss the direction of the follow-up exclusion.** Thirty percent of each pool left for having under three years of follow-up. Say who those patients were, even roughly — comparing the excluded on the variables already in hand would take one table and would tell a reader whether the model applies to the sicker patients it was built to help.

**State when the postoperative creatinine was measured.** The ratio is the third most influential predictor and the whole clinical use case depends on the timing. A reader cannot currently tell whether this is a day-one model or a three-month model.

**Address the coupling between preoperative eGFR and an outcome defined by eGFR bands.** Report performance with preoperative eGFR removed, or model follow-up eGFR adjusted for baseline. Preoperative eGFR being the top SHAP feature for an outcome defined as crossing an eGFR threshold is exactly what pure arithmetic would produce.

**Recalibrate, and show it.** The paper correctly diagnoses the problem and prescribes the fix in its discussion. Doing it — a logistic recalibration of intercept and slope, refitted in the external cohort and reported — would have turned a diagnosis into a deliverable, and the data were in hand.

**Name a reporting guideline.** TRIPOD+AI exists for exactly this study design, and most of its items are already satisfied.

**Add funding and competing-interests statements.**

**Say what the collapse of SVM and logistic regression to AUC ≈ 0.56 means.** Two of five models fell to near chance externally while three held. That is a striking result about model fragility and it passes without comment.

### What this study did well

- **Prespecified all ten predictors from a previously published study** and stated explicitly that no variable was selected on univariable P values in this cohort.
- **Fitted standardisation parameters on the training set only** and applied them unchanged downstream.
- **Applied SMOTE to the training set only**, leaving both evaluation cohorts at their true event rates.
- **Used seven genuinely separate hospitals** as the external cohort, and reported that they differ significantly from the development site on seven characteristics including the outcome.
- **Reported calibration intercept and slope with confidence intervals**, and described how each was estimated.
- **Ran paired DeLong tests across all five models in both cohorts**, and reported the comparison that did not reach significance.
- **Diagnosed its own calibration failure, quantified it, identified the cause (45.6% vs 23.7% event rate), and prescribed recalibration.**
- **Disclosed that the external cohort informed model selection, and renamed it accordingly** — the single most honest sentence in this month's reading.
- Gave an exact, itemised exclusion accounting for both cohorts that sums correctly.
- Confirmed a complete-case analysis with no imputation, and said which variables caused the exclusions.

## 5. Statistics Spotlight

### Concept 1: Where the optimism gets paid — and why "no drop" can be the least interesting number in the paper

This paper was chosen for the reading list because of one apparent oddity: internal validation AUC 0.7508, external AUC 0.7549. Essentially no loss. Every other model this fortnight lost ground on new data. The explanation has three parts, and working through them is more instructive than the oddity.

**Part one: the drop already happened, one step earlier.** The full sequence is **training 0.8604 → internal validation 0.7508 → external 0.7549.** The model lost **0.110** of AUC going from the data it was fitted on to data it had not seen — a large, entirely normal loss. It then lost nothing more going to other hospitals. **The optimism was real and it was paid in full; it was just paid at the first step rather than the second.**

**An everyday analogy.** A student's score drops sharply between practising with the answer key open and sitting a real mock exam. It then barely moves between the mock and the actual exam. Nobody concludes the real exam was easy. The honest comparison is practice-with-answers against the real thing, and that gap was large.

**Part two: the internal number is barely a measurement.** The internal validation set had **100 patients**. Its 95% confidence interval runs **0.6399 to 0.8617** — a width of **0.222**. The external interval, from 320 patients, runs **0.7022 to 0.8076**, a width of **0.105**, less than half as wide.

An interval spanning 0.64 to 0.86 is consistent with a nearly useless model and with a very good one. **Comparing a precise number against an imprecise one and finding "no difference" is not a finding** — the imprecise one could not have shown a difference.

**A tiny worked example.** Two bathroom scales. One reads to the nearest 100 grams, one to the nearest 10 kilograms. Step on both: 72.4 kg and 70 kg. Have you detected a discrepancy? No — the second instrument cannot resolve one.

**Part three, and the real reason: there was less optimism available to lose.** Most prediction papers choose their variables by looking at the development data — running univariable tests, LASSO, Boruta, stepwise selection. Every one of those decisions is fitted to that particular sample, and all of it evaporates on new data. **This paper did none of it.** The ten predictors were fixed in advance from a previously published study, and the authors state outright that "no predictors were selected or excluded according to univariable P values in the current study."

**Prespecifying the predictors removes a whole category of optimism before any model is fitted.** That is why the development-to-validation gap here appears once and then stops.

**Watch out.** When a paper reports internal and external performance that match, three questions, in order. **Was a training-set figure also reported, and what was the drop to internal?** **How big was the internal set, and how wide is its interval?** And **were the predictors chosen using this data or fixed beforehand?** Matching numbers are reassuring only when the internal estimate was precise enough to have disagreed.

### Concept 2: Discrimination transported, calibration collapsed — and the event rate explains it exactly

This is the paper's real finding, and it is the clearest example of the distinction this reading list keeps returning to.

**The two questions a model answers.** **Discrimination** asks whether the model puts patients in the right *order* — measured by AUC. **Calibration** asks whether the *numbers* mean anything — if it says 30%, do about 30% of those patients actually have the outcome?

**What happened here.**

- **AUC: 0.7508 internally → 0.7549 externally.** Ordering transported perfectly.
- **Brier score: 0.1558 → 0.2553.** Probability accuracy got substantially worse.
- **Calibration intercept: −0.29 (95% CI −1.07 to 0.49) → +0.61 (95% CI 0.27 to 0.95).**

**How to read those intercepts.** Zero is perfect. Internally, the interval runs from −1.07 to 0.49 and **contains zero** — no evidence of systematic bias. Externally the interval runs from 0.27 to 0.95 and **excludes zero** — the model is systematically wrong, and a positive intercept means it is **underestimating** risk.

**Why, and the authors give the reason.** The outcome occurred in **23.7%** of the development cohort and **45.6%** of the external cohort — **1.92 times as often.** A model learns the background rate of the population it was trained on and bakes it in. Move it somewhere the event is nearly twice as common and every probability it emits is too low. The ordering is unaffected, because everyone is shifted by roughly the same amount.

**A worked illustration.** Suppose the model tells four external patients their risk is 10%, 20%, 30% and 40%. Suppose the true risks are 20%, 38%, 55% and 70%. The ordering is perfect — patient four really is the highest risk. Every single number is badly wrong, and a clinician using a 30% threshold to decide on close monitoring would reassure three patients who should be watched.

**An everyday analogy.** A thermometer with a calibration fault reads consistently 5 degrees low. It will still tell you correctly which of two rooms is warmer — perfect discrimination. It will also tell you it is safe to go out in a T-shirt when it is freezing. Which failure matters depends entirely on whether you are comparing or deciding.

**What makes this paper good rather than merely instructive:** the authors found this, measured it with the right statistics, named the cause, and concluded that the model needs "recalibration before application to populations with different baseline risk." They did not bury a stable AUC and move on — which, with a stable AUC in hand, would have been easy and common.

**Watch out.** **A model that transports its discrimination has not necessarily transported anything a patient can use.** If a tool is going to show someone a percentage, AUC cannot tell you whether that percentage is honest — only a calibration intercept, slope, Brier score or calibration plot can. And when you see a calibration intercept reported, read its sign: **positive means risks are being understated, negative means overstated.** The good news is that miscalibration is usually repairable, which is why this finding is a to-do item rather than a verdict.

### Concept 3: Two of five models fell to a coin flip, and the paper does not mention it

Buried in the external results table is something the text passes over.

**External AUCs:** LightGBM **0.7549**, random forest **0.7292**, XGBoost **0.7187** — then **support vector machine 0.5635** and **logistic regression 0.5603**.

**An AUC of 0.50 is a coin flip.** Two of the five models landed at about 0.56. On the external data they were close to worthless, while three others held up at around 0.72 to 0.75.

**Why this is worth noticing.** In most papers in this reading list the models cluster tightly — every algorithm lands within a few hundredths and the choice between them is noise. Here the field split clean in two. That is a signal about the problem, not about the leaderboard: **something in the external hospitals' data breaks the two models that assume a particular shape of relationship** — logistic regression assumes effects combine in a straight line on the log-odds scale, and an SVM assumes a particular kind of boundary — while the three tree-based models, which carve the data into regions, survive.

**A worked intuition.** Suppose kidney decline risk rises slowly with age until about 65 and then sharply. A tree can learn "above 65, different rule." A straight-line model has to compromise, fitting one average slope. At the development hospital, where the age distribution is one shape, the compromise works tolerably. At seven hospitals with a different age mix — and the paper reports that age differed significantly — the compromise fails.

**An everyday analogy.** Two sets of directions to a friend's house. One lists landmarks: "left at the church, right after the bridge." The other says: "head north-east for about four kilometres." In the town you know, both work. In the next town over, the landmark directions still make sense of what you see; the compass bearing walks you into a river.

**Why the paper should have said something.** It selected its model partly on external performance and reported the numbers accurately — but a reader skimming the conclusion takes away "LightGBM was best," when the table says something more interesting and more useful: **that model choice mattered enormously here, in a way it has not in most comparable studies, and that the flexible models were the robust ones.**

**Watch out.** Read down the full external column, not just the top row. **A tight cluster of models means the choice does not matter and you should take the simplest. A wide spread means the choice matters a great deal — and that is the moment to ask which models held and why.** Either way the information is in the table and usually not in the text.

## 6. Jargon Translator

- **Renal cell carcinoma** — the commonest kidney cancer. **Radical nephrectomy** — removing the whole kidney, as opposed to **partial nephrectomy**, which removes only the tumour and spares the rest.
- **Chronic kidney disease (CKD)** — long-term loss of kidney function, graded in stages. Stage progression means moving into a worse band.
- **eGFR (estimated glomerular filtration rate)** — the standard measure of how well kidneys filter blood, in millilitres per minute per 1.73 m² of body surface. Higher is better; the CKD stages are defined by eGFR bands.
- **CKD-EPI 2021 equation** — the current recommended formula for estimating eGFR from serum creatinine, age and sex. **KDOQI** — the National Kidney Foundation initiative whose 2002 criteria defined the stages used here. **KDIGO** — the international body whose guideline recommends the CKD-EPI equation.
- **Serum creatinine** — a waste product cleared by the kidneys; higher levels mean worse filtering. **Post-to-preoperative serum creatinine ratio** — the after-surgery value divided by the before-surgery value, capturing how much the remaining kidney was knocked back.
- **Complete-case analysis** — analysing only patients with no missing values, rather than filling gaps in. Used here, with no imputation.
- **SMOTE (synthetic minority oversampling technique)** — invents extra synthetic examples of the rarer outcome so the model does not simply learn to predict the common one. Must be applied to training data only, which it was.
- **Z-score standardisation** — rescaling each variable to a common scale. The mean and spread used must come from the training data only, which they did.
- **LightGBM / XGBoost / random forest** — three ways of combining many decision rules, which carve the data into regions. **Support vector machine** finds a dividing boundary. **Logistic regression** is the classical statistical model assuming effects add up on a log-odds scale.
- **Grid search with five-fold cross-validation** — trying many settings and keeping whichever scores best across five rotating splits of the training data.
- **AUC** — the probability the model ranks a true case above a non-case. 0.5 is a coin flip, 1.0 perfect.
- **Youden index** — sensitivity plus specificity minus 1; maximising it picks a cut-off treating a missed case and a false alarm as equally bad.
- **DeLong test** — the correct paired test for comparing two AUCs measured on the same patients. Used here across all five models in both cohorts.
- **Brier score** — the average squared gap between predicted probability and what happened. Lower is better; it captures calibration and discrimination together.
- **Calibration intercept (calibration-in-the-large)** — whether predictions are systematically too high or too low overall. Zero is perfect; **positive means risk is being underestimated.**
- **Calibration slope** — whether predictions are spread too widely or too narrowly. One is perfect; below one means predictions are too extreme.
- **Decision curve analysis** — compares acting on the model against treating everyone and treating nobody, across thresholds.
- **SHAP / TreeSHAP / KernelSHAP** — methods assigning each predictor a share of the credit for a prediction; TreeSHAP is the fast version for tree-based models.
- **Prespecified predictors** — variables fixed before seeing the data, here taken from the group's earlier published study. The opposite of data-driven feature selection, and the reason much of this paper's optimism never arose.

## 7. What You Can (and Can't) Say

**Fair to say:**

- "Among 649 patients who had a kidney removed for cancer across eight Chinese hospitals, 224 (34.5%) had their chronic kidney disease stage worsen within three years."
- "A machine-learning model using ten routine variables ranked patients by that risk with an AUC of 0.755 at seven hospitals separate from the one that built it."
- "The model's ranking ability transferred to the other hospitals, but its probability estimates did not — it systematically underestimated risk, with a calibration intercept of +0.61 whose confidence interval excludes zero."
- "The reason is that the external patients were nearly twice as likely to progress — 45.6% against 23.7% — and the authors identify this themselves and call for recalibration."
- "The ten predictors were fixed in advance from a previous study rather than chosen from this data."
- "Two of the five models — support vector machine and logistic regression — fell to AUC around 0.56 externally, close to chance, while the three tree-based models held up."
- "The authors state that the external cohort informed their choice of model, and describe it as an evaluation rather than an independent validation cohort because of that."

**Not fair to say:**

- ❌ "The model performed just as well at other hospitals." Its ranking did. Its risk estimates were systematically too low, and the authors say they need recalibrating first.
- ❌ "An AUC that holds up externally means the model transfers." This paper is the counterexample: AUC moved by 0.004 while the Brier score worsened by 0.10 and the calibration intercept went from unbiased to significantly biased.
- ❌ "There was no loss of performance between development and validation." There was — AUC fell from 0.8604 in training to 0.7508 internally, a drop of 0.110. The flat step is the one after that.
- ❌ "LightGBM was significantly better than the alternatives." Better than three of them externally, but **not** better than random forest (DeLong p = 0.1119), which the authors report.
- ❌ "This can tell patients before surgery whether they will develop kidney disease." One predictor is the post-to-preoperative creatinine ratio, which requires a measurement taken after the operation.
- ❌ "About a third of patients having a kidney removed will progress to worse CKD." 34.5% is the rate among those who survived and attended for three years; roughly 30% of those screened were excluded for shorter follow-up.
- ❌ "Preoperative eGFR is the strongest driver of kidney decline." It was the top SHAP feature — for an outcome defined by crossing eGFR thresholds, which makes some of that ranking arithmetic rather than biology.
- ❌ "The results apply to patients outside Shandong." Eight centres, almost all in one Chinese province, and the paper's own finding is that moving between populations breaks the probability estimates.

## 8. Bottom Line for Your Life

If you or someone close to you is facing removal of a kidney for cancer, the useful fact here is not the model but its denominator: **in this series, about a third of patients saw their kidney function slip into a worse category within three years.** That is a real and common consequence, it is worth asking your surgeon about, and it is one of the reasons surgeons increasingly remove only the tumour rather than the whole kidney when that is possible. Your own risk depends heavily on how well your kidneys work beforehand. The model in this paper is not ready to give you a number — its own authors say the numbers need recalibrating before they are used anywhere else.

For anyone appraising research, this paper teaches one lesson exceptionally well and hands you a second for free.

**A stable AUC across hospitals does not mean the model transferred.** Here the AUC moved by four thousandths while the probabilities fell apart — systematically understating risk, because the new hospitals' patients were nearly twice as likely to decline. If a tool is going to show somebody a percentage, **ask for the calibration intercept and slope**, and read the sign. AUC is physically incapable of detecting the problem this paper found.

**And when internal and external results agree suspiciously well, look one step further back.** The training score was 0.86 and the internal score 0.75 — the loss happened there, and it was large. The internal estimate came from 100 patients with a confidence interval 0.22 wide, which could not have shown a difference even if one existed. And the predictors were fixed in advance from a previous study, which is genuinely good practice and removes much of the optimism that usually appears later. Three explanations, all visible in the paper, none of them "the model is unusually robust."

---

*This is an educational analysis of a published scientific paper, not medical advice. Nothing here is guidance about kidney surgery, kidney disease or your own care. If you have questions about a nephrectomy or your kidney function, speak to your surgeon or nephrologist.*
