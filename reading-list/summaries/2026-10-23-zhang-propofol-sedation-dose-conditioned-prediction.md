# Dose-conditioned machine-learning prediction of a composite target sedation state in patients undergoing propofol-sedated gastrointestinal endoscopy

**Authors:** Zhang H, Zhao L, Yang W, Li B, Lin W, Chen X, Mo L, Dai S, Chen W, Yang F, Ma H (11 authors; Department of Anaesthesiology and Perioperative Medicine and other departments, General Hospital of Ningxia Medical University, Yinchuan, China)
**Journal:** Annals of Medicine, 2026; 58(1): 2737005 (published 28 September 2026)
**Decoded:** 2026-10-23
**Analysis basis:** **FULL TEXT** (retrieved from PubMed Central, PMC13629798; 54,348 characters). Figures are described in the PMC rendering's alt-text and used where noted; the supplementary material (full model specifications, confusion matrices for the other four models, missingness summary, dose-support panels, calibration and decision-curve summary tables) was not viewable, so anything living only there is marked as not retrieved.

**Source links (verified):**
- DOI: https://doi.org/10.1080/07853890.2026.2737005
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42803764/
- Full text (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC13629798/

**Basis of link verification.** Direct URL fetching is blocked from this session (`doi.org` does not resolve under the network policy here). Verification was done against the live PubMed/NLM record: a query for PMID 42803764 returned this exact title, these eleven authors, Annals of Medicine volume 58 issue 1 article 2737005, DOI `10.1080/07853890.2026.2737005` and PMC ID `PMC13629798`; the full text was then retrieved from PubMed Central by that PMC ID and matches. Both halves of the chain were confirmed independently.

**Trial registration:** the paper states it was registered at ClinicalTrials.gov, but **the identifier is stripped from the PMC rendering**, so the registration record **could not be independently verified**.

**Funding: not reported in the text provided.** **Competing interests: not reported in the text provided.**

**Ethics:** approved by the Medical Ethics Committee of the General Hospital of Ningxia Medical University (approval No. KYLL-2023-0172), **written informed consent obtained from all participants**, conducted per the Declaration of Helsinki. Reporting followed **STROBE** (for observational studies) and **TRIPOD+AI** (for clinical prediction models) — both named explicitly.

> **Why this paper today.** A genuinely landmark paper did appear this week — Google's "The anatomy of a personal health agent" in Nature (PMID 42907512, 21 October), an open-source multi-agent LLM framework over wearables and medical records with more than 7,000 annotations and 1,350 hours of expert evaluation. It has **no PubMed Central copy**, so it joins the deferred list, which is now four deep: the BMJ review of LLM-trial reporting, the JAMA OpenEvidence usage study (PMC body still empty on day 8), the Annals of Internal Medicine Choosing Wisely benchmark, and now this Nature paper. All four re-checked this morning; all four still blocked. Today's paper was the top candidate on the restocked shelf, chosen because its own abstract volunteers three things most papers hide.

---

## 1. The Gist

When you have a camera passed into your stomach or bowel, you are usually given propofol — a drug that sends you to sleep in under a minute. The anaesthetist has to get it right in both directions at once: deep enough that you are properly asleep, but not so deep that your blood pressure drops or your oxygen falls. Those three things pull against each other, and people respond to propofol very differently.

Researchers in Ningxia, China watched 1,248 adults go through this, recording what they knew about each patient beforehand and how much propofol it took to put them under. Then they asked a machine-learning model to predict, from that information alone, whether the patient would land in the sweet spot — asleep at the right depth, blood pressure holding, oxygen fine, all three at the same moment.

Only about one patient in seven hit all three.

The models could tell apart the patients who would and would not, about four times out of five. That is a real signal. But the paper's most useful contribution is not the models — it is everything the authors say about them. They report that the probabilities the models produce are **wrong in absolute terms** even though the ranking is decent. They report that **five different models each won on a different measure**, so there is no best one. And they report that the model which looked best during development came **dead last** when tested on patients from a later period.

Most papers would have picked whichever model and whichever metric looked best and written a confident headline. This one built a table specifically to show you that you cannot do that.

## 2. Study Snapshot

**Study type:** a **prospective observational cohort study** used to develop and temporally validate a clinical prediction model. Prospective means they decided what to collect and then collected it going forward, rather than digging through old records — which rules out a whole family of biases that have affected most papers recently in this list. On the evidence ladder this sits above retrospective work and below a trial. It can tell you how well the model predicts. It cannot tell you that using it helps a patient, and the authors say so.

**Where and when:** Department of Anaesthesiology and Perioperative Medicine, General Hospital of Ningxia Medical University. **Consecutively enrolled 20 November 2024 to 30 July 2025.** The study did not change anyone's care — the anaesthetists ran their normal protocol and the investigators only collected data.

**The funnel:** **1,441** patients screened → **45** excluded for being outside 18–75 → **148** excluded for incomplete data needed to define the outcome (37 missing BIS, 32 missing blood pressure, 34 incomplete records, 45 other) → **1,248** analysed. The components sum exactly to 148, and 1,441 − 45 − 148 = 1,248.

**The split:** **the first 1,000 patients enrolled** formed the development cohort; **the next 248** formed the temporal validation cohort. A chronological split, not a random one. The paper states the validation cohort "was not used for model training, preprocessing fitting, feature selection, threshold selection, or model tuning" — naming all five things it was walled off from.

**Who they were:** adults 18–75 scheduled for painless gastrointestinal endoscopy with intravenous propofol. No restrictions on sex, body size or underlying disease. Excluded for propofol allergy, severe cardiorespiratory instability, repeat enrolment, or missing outcome data.

**The protocol, which matters for interpreting everything:** every patient got intravenous sufentanil 5 μg, then after 3 minutes propofol at a **fixed rate of 100 mg/min** until they lost consciousness (defined as a Modified Observer's Assessment of Alertness/Sedation score of 1 or less). The infusion then stopped and the cumulative amount was recorded as the initial propofol dose.

**And here is a consequence the authors flag themselves:** because the rate was fixed, the recorded dose is just a stand-in for *how long it took that patient to go under*. It was not a dose anybody chose. So this cannot tell you what would happen if you gave a patient a different dose.

**The outcome:** an **investigator-defined composite**, measured once, **1 minute after loss of consciousness and before the endoscope went in**, requiring all three of:
- **BIS 40–60** (bispectral index, a 0–100 scale from brain-wave monitoring where 40–60 is the usual general-anaesthesia range),
- **systolic blood pressure at least 80% of that patient's own baseline**,
- **oxygen saturation at least 90%.**

The authors are explicit that this "should not be interpreted as a universally accepted definition of optimal procedural sedation" and that the low event rate partly reflects needing all three at once.

**How often it happened:** **153 of 1,000 (15.3%)** in development, **33 of 248 (13.3%)** in validation.

**Predictors:** 21 candidate variables, all available **before or at** initial sedation — sex, age, height, weight, BMI, ASA physical status, smoking, drinking, hypertension, diabetes, COPD, coronary heart disease, baseline blood pressures, pulse, oxygen saturation, baseline BIS, procedure type, sufentanil dose, and the initial propofol dose.

**Leakage control, spelled out.** The paper lists exactly what was excluded from the inputs and why: the post-loss-of-consciousness BIS, blood pressure and oxygen saturation (those define the outcome), pulse after propofol, the sedation score, intra-procedural events, additional and total propofol dose, recovery variables, procedure duration, and identifiers.

**Models:** logistic regression (as an interpretable baseline), support vector machine, random forest, HistGradientBoosting, and ExtraTrees. All five used **balanced class weights**. No oversampling or synthetic sampling. **No grid search in the final analysis** — specifications were fixed after preliminary exploration on the development cohort, which the authors state plainly. Random seed 20260604; Python package versions listed.

**Thresholds — the correct procedure, with a prespecified tie-break.** For each model the classification threshold was chosen **in the development cohort** by maximising the Matthews correlation coefficient, tie-broken first by higher F1 and then by lower threshold, and then **applied unchanged** to the validation cohort. The selected thresholds were 0.811 (logistic regression), 0.429 (SVM), 0.550 (random forest), 0.177 (HistGradientBoosting) and 0.606 (ExtraTrees).

**Statistics:** 1,000 subject-level bootstrap resamples for every confidence interval. **No pairwise testing of AUCs was done, and the authors say so** — performance was "interpreted descriptively."

**And they computed their own events-per-predictor:** **153 events across 21 candidate predictors = 7.29**, which they note is *before* categorical expansion.

### The results

**In development (out-of-fold):** HistGradientBoosting had the highest AUC at **0.804**, then random forest 0.800, SVM 0.787, ExtraTrees 0.787, logistic regression 0.769.

**In temporal validation:** random forest **0.821** (95% CI 0.748–0.889), ExtraTrees **0.819** (0.728–0.897), SVM 0.802, logistic regression 0.797, and **HistGradientBoosting last at 0.780** (0.697–0.855).

**The internal winner finished last.**

**ExtraTrees at its threshold of 0.606** — the only confusion matrix given in full: **TN 198, FP 17, FN 15, TP 18.** Every reported metric recomputes from those four numbers exactly: sensitivity 0.545, specificity 0.921, PPV 0.514, NPV 0.930, accuracy 0.871, F1 0.529, MCC 0.455. It flags 35 of 248 patients — 14.1%.

**The other models at their own thresholds** behaved completely differently. Logistic regression and SVM reached specificity 0.972 but sensitivity of only 0.152 and 0.182 — catching about 5 and 6 of the 33 events. HistGradientBoosting caught 18 of 33 but raised 31 false alarms.

**Calibration was poor, and the paper explains it properly.** Brier scores: SVM best at 0.097, then HistGradientBoosting 0.111, random forest 0.127, ExtraTrees 0.150, logistic regression worst at 0.170. For ExtraTrees the **calibration intercept was −1.468 and the calibration slope 1.767**, which the authors correctly read as the model systematically overestimating the probability and the predictions being insufficiently spread out.

**Decision curve analysis** gave yet another ordering: SVM had the highest mean net benefit (0.035) across threshold probabilities 0.05–0.50, then HistGradientBoosting (0.025).

**SHAP** ranked drinking status top — and the authors immediately caution that drinking differed between cohorts (32.3% vs 39.5%, p = 0.031), that it was a crude self-reported binary, and that removing it made calibration **worse** (Brier 0.160, intercept −1.498, slope 2.397), not better.

**A sensitivity outcome** dropping the oxygen criterion gave event rates of 16.3% and 15.3% and a top AUC of 0.775 — lower than the primary.

**A dose-support analysis** confirmed the validation cohort's propofol doses sat inside the development range (40–200 mg in both, median 120 mg; 98.4% within the 1st–99th percentile range).

**And a scenario analysis** for the 148 excluded patients, because their outcomes could not be reconstructed and a proper included-versus-excluded comparison was not possible.

## 3. How Strong Is This Evidence? (Grade 4/5)

**Grade: 4/5 — a small, single-centre study that is as close to correctly reported as this reading list has seen.**

**On the scale, and why this sits with EAGLE.** This is the first 4 since the EAGLE CT screening programme, which had 12 centres, three countries, 80,612 patients, a prospective deployment and a reader study. That comparison looks odd until you remember what the grade measures: **how much you can trust what the paper actually claims.** EAGLE proved a great deal and then overstated part of it in its abstract. This paper proves much less and overstates none of it. Both land in the same place — trust the conclusions, which are appropriately bounded. A big study that overclaims and a small study that does not can be equally reliable guides to their own contents.

**What it genuinely supports.** That among adults at one Chinese hospital, routinely available pre-sedation information plus the propofol dose it took to reach unconsciousness separates patients who hit a three-part sedation target from those who do not, with an AUC around 0.80, and that this holds up on patients enrolled months later. And — the more durable finding — that model ranking, probability accuracy and clinical net benefit are three different things that pick three different winners.

**What it does not support, and does not try to.** Any dosing recommendation; any causal claim about propofol; any claim that one algorithm is best; any clinical use of the predicted probabilities. The conclusion reads: "the present models should not be used for causal dose optimization or direct clinical dosing. Independent multicenter validation, recalibration, and prospective evaluation are required before clinical implementation."

**What keeps it at 4 rather than 5 — all of them acknowledged by the authors.**

**One centre, and temporal rather than external validation.** A chronological split is a genuine test — it catches drift over time, and here it caught the internal winner failing — but every patient came from the same hospital, the same scanners, the same anaesthetists, the same protocol. That caps what can be concluded.

**Thirty-three validation events.** Every validation number rests on 33 positive cases, which is why sensitivity comes with an interval of 0.367 to 0.714. The authors state this in the abstract itself.

**Events per predictor of 7.29, below the traditional 10** — and lower still once categorical variables are expanded. They computed and published this figure, which is rare.

**Calibration is poor.** The probabilities are not usable as probabilities. The authors say so and prescribe the fix.

**The outcome is an investigator-defined construct measured at a single instant**, one minute after loss of consciousness, rather than the worst value across the procedure. Hit by only 15.3% of patients. The authors flag the definition, the timing and the low rate.

**One hundred and forty-eight patients (10.3% of those screened) were excluded with no possible comparison** against those included. They report it and model the consequences rather than ignoring it.

**No formal hyperparameter search.** Specifications were set from preliminary looks at the development cohort. Defensible, and stated.

**The registration identifier is missing** from the published record reached here, so the registration could not be checked — the one thing that would have let a reader confirm the outcome was prespecified.

**What earns the 4, and it is the longest such list in this reading list.**

Prospective and consecutive. Ethics approval with its number, **written informed consent**, and registration claimed. **STROBE and TRIPOD+AI named as the reporting standards** — and actually followed. A **complete firewall statement** naming all five things the validation cohort was kept away from. **Preprocessing fitted only within each training fold.** An **explicit list of excluded post-sedation variables** to prevent leakage. The **threshold chosen on development data with a prespecified tie-break rule and applied unchanged** — the fifth paper on this axis in a week, and the best handling of it. **Calibration intercept and slope reported and correctly interpreted.** Decision curve analysis, labelled exploratory. A sensitivity outcome. A dose-support overlap check. A scenario analysis for unreconstructable exclusions. Random seed and software versions. Bootstrap intervals on everything. Seven numbered limitations, none softened.

And two things almost nobody does. **They declined to name a best model, and built a table whose stated purpose is to show the winner changes with the metric** — its note reads: "The highest values for different performance measures were obtained from different models and should not be interpreted as indicating superiority of any single model." And they **talked themselves out of their own most interesting finding**: drinking status topped the SHAP ranking, and they explained at length why it should not be believed.

**Where 4/5 sits.** A modest result, reported so carefully that you can check almost all of it — and I did; all seven ExtraTrees metrics recompute from the published confusion matrix to three decimal places. It is not a 5 because one centre, 33 validation events and uncalibrated probabilities cap what any such study can establish, not because of anything the authors did wrong.

## 4. The Editor's Concerns

These are genuinely minor, which is itself unusual.

**Give the registration number in the text.** The paper says it was registered; the identifier does not survive into the published record reached here. Without it a reader cannot confirm the primary outcome was prespecified — which matters precisely because the outcome is investigator-defined.

**Name the class-weighting mechanism when discussing calibration.** All five models used balanced class weights, which deliberately distorts the probability scale upward — and is the most likely main reason the calibration intercept is −1.468 and logistic regression's selected threshold is 0.811 for a 13% outcome. The paper attributes the miscalibration to distribution shift and low event counts, both plausible, but does not mention the design choice that guarantees it. (This is my inference from the stated specifications, not something the paper claims.)

**Report the confusion matrices for all five models in the main text**, not just ExtraTrees. They are the clearest way to see that the five models are doing five different jobs.

**Say what the composite's three components did separately.** How many patients failed on depth, how many on blood pressure, how many on oxygen? With only 15.3% hitting all three, knowing which criterion does the excluding would tell a reader far more than the composite does.

**Consider whether the target is the right one.** A target hit by one patient in seven under the unit's own standard protocol may be describing the protocol rather than the patient. The authors raise the definitional question; the implication for the protocol is left unexplored.

**Pre-register and report the recalibration plan as an analysis, not a recommendation.** The discussion correctly prescribes logistic recalibration of intercept and slope, with isotonic regression if needed. Doing it in the development cohort and reporting the recalibrated validation performance would have cost little.

**Add funding and competing-interests statements.**

### What this study did well

- **Prospective and consecutive enrolment**, with dates, at a named department.
- Ethics approval with its number, and **written informed consent from every participant**.
- **Named and followed STROBE and TRIPOD+AI.**
- **Temporal validation** by chronological split rather than random splitting — and it mattered, because the internal winner came last.
- Stated that the validation cohort was used for **none** of training, preprocessing fitting, feature selection, threshold selection, or tuning.
- **Fitted preprocessing only inside each cross-validation fold.**
- **Listed every post-sedation variable excluded** from the inputs, with the reason.
- **Chose the classification threshold on development data, by a stated rule with a stated tie-break, and applied it unchanged.**
- **Computed and published its own events-per-predictor figure (7.29)**, and noted it is before categorical expansion.
- **Reported calibration intercept and slope and interpreted both correctly**, then said the probabilities should not be used at the bedside.
- Ran decision curve analysis and labelled it exploratory.
- Ran a sensitivity outcome, a dose-support overlap check, and a sensitivity analysis dropping the top predictor.
- **Refused to declare a best model**, and built a table to demonstrate why.
- **Argued against its own most eye-catching result** (drinking status) at length.
- Gave the random seed and every package version.
- Wrote seven numbered limitations, every one real.
- Stated in the abstract that confidence intervals were wide and comparisons uncertain.

## 5. Statistics Spotlight

### Concept 1: There is no "best model" — there is a best model *for a chosen measure*

This paper is the cleanest demonstration of this I have come across, because the authors ran nine different measures on five models and published all of it.

**Who won what, in the validation cohort:**

- Highest **AUC**: random forest (0.821)
- Highest **average precision**: ExtraTrees (0.570)
- Highest **MCC**: ExtraTrees (0.455)
- Highest **F1**: ExtraTrees (0.529)
- Highest **positive predictive value**: random forest (0.579)
- Highest **sensitivity**: HistGradientBoosting and ExtraTrees (0.545)
- Highest **specificity**: logistic regression and SVM (0.972)
- Best (lowest) **Brier score**: SVM (0.097)
- Highest **mean net benefit**: SVM (0.035)

**Nine measures, five different winners — every model in the study won something.**

**Why this happens.** Each measure asks a different question.

- **AUC** asks: if I show you one patient who hit the target and one who did not, how often do you rank them correctly? It ignores where you draw the line.
- **Average precision** asks the same ranking question but weights the top of the list, which matters when the event is rare.
- **Sensitivity** asks: of the people who hit the target, how many did you flag? **Specificity** asks the mirror.
- **PPV** asks: of those you flagged, how many really hit it?
- **F1 and MCC** are different compromises between the above. MCC is the stricter one, because it uses all four boxes of the table.
- **Brier score** ignores ranking entirely and asks: were your *probabilities* right?
- **Net benefit** asks: if I acted on this, counting a false alarm as some fraction of a missed case, would I come out ahead?

A model can be excellent at ranking and useless at probabilities. SVM here was the best probability estimator (Brier 0.097) and caught only **6 of 33** events at its own threshold.

**An everyday analogy.** Four people are judged "the best driver." One has the fewest accidents. One gets there fastest. One uses the least fuel. One is the most comfortable passenger experience. All four claims can be true of four different people, and asking "who is the best driver?" without saying what you want is not a question with an answer.

**Watch out.** When a paper says "model X performed best," find out **which single measure** that was and whether the others agreed. If the paper reports only one measure, you cannot tell whether it is the one measure where that model happened to win. The tell in this paper is Table 3, which lists seven measures and names a different model for several of them — and whose note says, in the authors' own words, that the highest values "should not be interpreted as indicating superiority of any single model." **That note is the paper's single most transferable sentence.**

### Concept 2: Calibration — what the intercept and the slope actually mean

Discrimination and calibration are two separate questions, and this paper is unusual in reporting both properly.

**The difference.** **Discrimination** is whether the model puts patients in the right order. **Calibration** is whether the number it emits means what it says: of all patients given a 30% chance, do about 30% really hit the target?

**What this paper found.** For ExtraTrees: **calibration intercept −1.468, calibration slope 1.767**, Brier score 0.150.

**How to read those two numbers, because almost nobody explains it.**

Imagine plotting predicted probability on the horizontal axis against what actually happened on the vertical. Perfect calibration is the 45-degree line. The calibration intercept and slope describe how your model's line differs from it.

**The intercept is the overall level.** Zero is perfect. The **−1.468 here means predictions sit systematically too high** — the model thinks patients are more likely to hit the sedation target than they really are.

**The slope is the spread.** One is perfect. A slope **above 1, as here at 1.767, means the predictions are bunched too close together** — the model is too timid, saying 25% and 35% when the truth is nearer 10% and 50%. (The commoner problem, a slope below 1, is the opposite: an overconfident model making extreme predictions that do not come true.)

**A worked intuition.** A weather app says 30% chance of rain. Over a hundred such days, if it rains on about 30, it is calibrated. If it rains on 12, the intercept is off — systematically too high. Now suppose the app never says anything outside 25%–40%, while real days range from near-certain downpours to cloudless skies. Its ordering may be excellent — the 40% days really are wetter than the 25% days — but it has compressed the whole world into a narrow band. That is a slope above 1, and it is what this model did.

**Why it probably happened here, and the paper does not say.** All five models used **balanced class weights** — a technique that tells the model to treat the rare outcome as if it were as common as the common one. It helps the model learn from few events and it **deliberately breaks the probability scale**, pushing predicted probabilities upward. The giveaway is in the thresholds: for an outcome occurring 13% of the time, logistic regression's chosen cut-off was **0.811**. Nothing sensible is 81% likely in a 13% world unless the probability scale has been stretched. (That mechanism is my reading of the stated specifications, not a claim the paper makes — it attributes the miscalibration to distribution shift and small numbers, which are also plausible contributors.)

**The honest consequence, which the authors draw themselves:** "although ExtraTrees separated patients relatively well, its absolute probability estimates were not reliable enough for clinical interpretation in their current form."

**Watch out.** Most prediction papers report AUC and stop. **AUC cannot detect miscalibration at all** — you can add 0.3 to every predicted probability and the AUC will not move by a thousandth, because the ordering is unchanged. If a model is going to show a patient a number, that number needs calibration evidence: an intercept, a slope, a Brier score, a calibration plot. If a paper gives you only an AUC and then talks about "individual risk estimates", it has not shown you that the estimates mean anything. And note the direction of the fix: miscalibration is usually **repairable** by recalibration, which is why this is a less damning finding than poor discrimination would be — and why the authors prescribe exactly that.

### Concept 3: Counting the events, not the patients

The headline number in this study is 1,248 patients. The number that governs how much you can conclude is much smaller, and the authors did the arithmetic for you.

**Events per predictor.** When fitting a model, what limits you is not how many people you have but **how many of them had the outcome**. The rule of thumb is at least **10 events per predictor variable**. Below that, models start fitting noise and estimates become unstable.

Here: **153 events, 21 candidate predictors — 7.29 events per predictor.** The authors computed this and printed it. They also note it is **before categorical expansion**: a variable like ASA physical status with four levels becomes three or four columns, so the real figure is lower still.

**Why the rule exists, intuitively.** Every predictor you add is another thing the model must estimate from the same limited pool of informative cases. With 153 events and 21 things to learn, each predictor gets about seven examples to pin it down. Seven examples is enough to spot a strong, consistent effect and nowhere near enough to pin down a weak one — so weak predictors get fitted to whatever happened to be in those seven cases. That is the mechanism behind unstable variable rankings, and it is exactly why the authors warn that "the stability of individual predictor rankings requires confirmation in independent datasets."

**Then the validation side, which is even tighter.** The validation cohort had **33 events**. Every number measured there — sensitivity, specificity, PPV, calibration slope — is computed from a handful of patients. Look at what that does to the intervals: ExtraTrees' sensitivity is **0.545 with a 95% interval of 0.367 to 0.714**. In plain terms, 18 of the 33 were caught, and the truth is somewhere between about 12 and 24 out of 33. You could not distinguish a mediocre model from a decent one at that precision.

**A worked example.** Suppose two models catch 18 and 20 of 33 events. That looks like a difference. But swapping the classification of just two patients produces it, and in a fresh group of 33 it could easily reverse. This is why the authors wrote, in the abstract, "With only 33 validation events, confidence intervals were wide and comparisons among models remain uncertain" — and why they ran no pairwise tests. Given 33 events, declining to test is the right call rather than a gap.

**An everyday analogy.** You want to know which of two restaurants is better. You eat at each one twice. Whatever you conclude, you have learned more about those four meals than about the restaurants. Eating at the same two restaurants fifty times each would settle it. The size of the city they are in is irrelevant — and in a prediction study, the total number of patients is the size of the city.

**Watch out.** Whenever you meet an impressive-sounding sample size, **find the event count**. A study of 10,000 patients with 40 events is a 40-event study. The quick check: divide events by the number of predictors, and look at whether the confidence intervals are narrow enough that the result would mean something different at either end. Here the paper hands you both numbers unprompted, which is how it should be done — and which is why its modest conclusions are believable in a way that louder ones from larger-sounding studies are not.

## 6. Jargon Translator

- **Propofol** — the short-acting intravenous anaesthetic used for procedural sedation; works in under a minute and wears off quickly.
- **Sufentanil** — a strong short-acting opioid painkiller; given here as a fixed 5 μg to every patient before the propofol.
- **Gastrointestinal endoscopy** — passing a camera into the stomach or bowel. "Painless endoscopy" is the term used locally for doing it under sedation.
- **BIS (bispectral index)** — a 0–100 number derived from brain-wave monitoring. 100 is fully awake, 0 is no activity; 40–60 is the usual target for general anaesthesia.
- **MOAA/S (Modified Observer's Assessment of Alertness/Sedation)** — a 0–5 scale of responsiveness. A score of 1 or less was used here to define loss of consciousness.
- **LOC (loss of consciousness)** — the moment the patient stopped responding, which is when the propofol infusion was stopped and the dose recorded.
- **SpO₂ (peripheral oxygen saturation)** — the finger-clip oxygen reading; 90% was the floor here.
- **ASA physical status** — the anaesthetist's 1-to-5 grading of how sick a patient is before an operation.
- **Composite outcome** — an outcome requiring several things at once. Here all three of depth, blood pressure and oxygen, which is why only about one patient in seven qualified.
- **Dose-conditioned model** — a model that estimates the probability of an outcome *given* the dose that was actually used, rather than recommending a dose. The distinction is the paper's central caveat.
- **Temporal validation** — testing on patients enrolled later in time rather than a random subset. Weaker than testing at a different hospital, stronger than random splitting.
- **Out-of-fold prediction** — in cross-validation, each patient's prediction made by a model that did not see them during training.
- **Balanced class weights** — telling the model to treat the rare outcome as if it were as common as the common one. Helps learning from few events; distorts the probability scale.
- **Logistic regression / SVM / random forest / HistGradientBoosting / ExtraTrees** — five modelling approaches, from a classical regression to four non-linear methods.
- **AUC** — the probability the model ranks a true positive above a true negative. Ranking only; blind to calibration.
- **Average precision (AP)** — a summary of the precision-recall curve; more informative than AUC when the outcome is rare. Compare it against the event rate: 0.570 against a 13.3% prevalence is a real signal.
- **MCC (Matthews correlation coefficient)** — a single score from −1 to 1 using all four boxes of the confusion matrix; the strictest common summary, and what the thresholds were chosen to maximise here.
- **F1 score** — the harmonic mean of precision and sensitivity.
- **Brier score** — the average squared gap between predicted probability and what happened. Lower is better; it measures calibration and discrimination together.
- **Calibration intercept / slope** — the two numbers describing how a model's probabilities differ from reality: the intercept is the overall level (0 is perfect), the slope is the spread (1 is perfect).
- **Decision curve analysis (DCA) / net benefit** — compares acting on the model against treating everyone and treating nobody, across thresholds.
- **SHAP** — assigns each predictor a share of the credit for a prediction. Describes the model, not the world.
- **Permutation importance** — scrambling one predictor and seeing how much performance falls.
- **Events per predictor (EPV)** — outcome events divided by number of predictors. Ten is the traditional minimum; this study reported 7.29.
- **Bootstrap resampling** — repeatedly resampling patients to estimate uncertainty; 1,000 resamples here.
- **STROBE / TRIPOD+AI** — the reporting checklists for observational studies and for AI-based clinical prediction models. Both named and followed.
- **Confounding by indication** — when the reason a treatment was chosen is itself related to the outcome. The authors raise it as a reason the dose findings cannot be read causally.

## 7. What You Can (and Can't) Say

**Fair to say:**

- "In 1,248 adults having sedated gastrointestinal endoscopy at one Chinese hospital, only about 15% hit a three-part target of adequate depth, stable blood pressure and preserved oxygen one minute after losing consciousness."
- "Machine-learning models using information available before sedation plus the propofol dose given predicted that target with an AUC around 0.80 in patients enrolled months later."
- "The model that performed best during development came last when tested on the later patients."
- "Five different models each won on a different performance measure, and the authors explicitly declined to name a best one."
- "The models' probabilities were poorly calibrated — the authors report a calibration intercept of −1.468 and slope of 1.767 for their lead model, and say the probabilities should not be used at the bedside."
- "The validation cohort contained only 33 events, which the authors state makes comparisons between models uncertain."
- "The study followed STROBE and TRIPOD+AI, chose its classification thresholds on the development data and applied them unchanged, and reported its own events-per-predictor figure of 7.29."

**Not fair to say:**

- ❌ "A model can now predict the right propofol dose." It cannot, and the paper repeatedly says so. The dose was never chosen — it is a record of how long each patient took to go under at a fixed infusion rate.
- ❌ "ExtraTrees was the best model." It had the highest average precision, MCC and F1; random forest had the highest AUC and PPV; SVM had the best Brier score and net benefit.
- ❌ "The model is 87% accurate." Accuracy is near-meaningless when 87% of patients do not have the outcome — predicting "no" for everyone would score 86.7%.
- ❌ "AI could make endoscopy sedation safer." Nothing about safety outcomes was tested. No patient's care was changed, and no model was deployed.
- ❌ "Drinking is the strongest predictor of sedation response." The authors spend a paragraph arguing against exactly this reading: it was a crude self-reported binary, it differed between the cohorts, and removing it made calibration worse.
- ❌ "Only 15% of patients are sedated properly." That figure reflects an investigator-defined composite measured at one instant, requiring all three criteria simultaneously — not a standard of care anybody is failing.
- ❌ "These results apply to other hospitals." One centre, one protocol, one fixed infusion rate, 33 validation events. The authors list external validation first among their limitations.
- ❌ "The model had high specificity, so a positive prediction is reliable." At the ExtraTrees threshold, 18 of 35 flagged patients hit the target — just over half.

## 8. Bottom Line for Your Life

If you are having a sedated endoscopy, nothing here changes anything. No AI was involved in anybody's care in this study, the anaesthetists followed their normal protocol throughout, and the authors are explicit that nothing they built should be used to choose a dose. The useful background fact is the one the study is built around: propofol response varies a lot between people, which is why an anaesthetist watches your depth, blood pressure and oxygen continuously rather than calculating a dose from your weight and walking away.

For anyone appraising research, read this one as a template rather than for its finding. Three checks it hands you, in order of how often they catch something:

**Find the event count, not the patient count.** 1,248 patients, 153 development events, **33 validation events**. The authors did this division themselves and printed 7.29 events per predictor. Almost nobody does.

**Ask which measure "best" refers to.** Nine measures here, five different winners, and a table note saying so outright. If a paper names a winner on one metric and does not show you the others, you have been shown the metric where that model happened to win.

**Separate ranking from probabilities.** A model can order patients well and still produce numbers that are simply wrong — this one did, and said so. If a tool is going to show somebody a percentage, ask for the calibration slope and intercept, because an AUC cannot detect that problem at all.

The deeper point is about what honest reporting looks like. This paper's conclusions are modest, hedged and a little dull — and that is precisely why you can believe them. A paper that tells you its confidence intervals are too wide to rank its own models has told you something true and useful. One that picks the winning metric and leads with it has told you something that may not survive the next hospital.

---

*This is an educational analysis of a published scientific paper, not medical advice. Nothing here is guidance about sedation, anaesthesia or endoscopy. If you have questions about an upcoming procedure, speak to your anaesthetist.*
