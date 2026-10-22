# Predicting gallstones risk with body composition analysis and machine learning: a dual-center cohort study

**Authors:** Long HY, Wu YM, Li X, Chen BQ (4 authors; Jinqiu Hospital of Liaoning Province, Panjin Liaohe Oilfield Gem Flower Hospital, and The People's Hospital of China Medical University / The People's Hospital of Liaoning Province, Shenyang and Panjin, China)
**Journal:** Annals of Medicine, 2026; 58(1): 2742549 (published 7 October 2026)
**Decoded:** 2026-10-22
**Analysis basis:** **FULL TEXT** (retrieved from PubMed Central, PMC13647361). Figures are described in the PMC rendering's alt-text and are used where noted; the supplementary material (CT equipment parameters, formulas, the detailed fivefold cross-validation table, confusion matrices, PR curves, software versions) was not viewable, so anything living only there is marked as not retrieved.

**Source links (verified):**
- DOI: https://doi.org/10.1080/07853890.2026.2742549
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42841700/
- Full text (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC13647361/

**Basis of link verification.** Direct URL fetching is blocked from this session (`doi.org` does not resolve under the network policy here). Verification was done against the live PubMed/NLM record: a query for PMID 42841700 returned this exact title, these four authors, Annals of Medicine volume 58 issue 1 article 2742549, DOI `10.1080/07853890.2026.2742549` and PMC ID `PMC13647361`; the full text was then retrieved from PubMed Central by that PMC ID and matches. Both halves of the chain were confirmed independently.

**Funding: not reported in the text provided.** **Competing interests: not reported in the text provided.**

**Ethics:** approved by the ethics committees of all participating hospitals (approval numbers 2025K085 and LLSC-2026-KY-14); informed consent waived because the study was retrospective. Both approval numbers are given, which is good practice.

> **Why this paper today.** The three better papers from the past fortnight remain unreachable in full, all re-checked this morning: the BMJ systematic review of reporting completeness in LLM trials (PMID 42869550 — still no PubMed Central copy, and Scite still requires a paid plan), the JAMA study of 952,008 clinicians using an AI platform (PMID 42879271 — PMC record still serving an empty body), and the Annals of Internal Medicine benchmark of six commercial LLMs on Choosing Wisely scenarios (PMID 42896192 — no PMC copy). This was the last screened spare on the shelf, and it turned out to be the best-executed paper decoded in a week.

---

## 1. The Gist

Gallstones are hard lumps that form in the gallbladder. They are common, they often need surgery, and being overweight is one of the main causes.

The usual way to judge someone's risk is a tape measure and a set of scales — body mass index, waist size. The trouble is that those numbers cannot tell the difference between fat and muscle, or between the dangerous fat packed around your organs and the harmless fat under your skin.

These researchers had a different idea. Lots of people have abdominal CT scans anyway, for all sorts of unrelated reasons, and a CT scan can measure fat, muscle and bone precisely. So they took 1,944 people who had a CT scan showing **no** gallstones, used an automated tool to measure their body composition, and then waited to see who developed stones over the next three years. Three hundred and ten did.

Then they tested whether the CT measurements predicted it better than a tape measure, and whether a machine-learning model combining everything did better still.

The answers were: not really, and yes but only moderately. **No single measurement was much use** — the best one, a blood inflammation ratio, scored 0.627, where 0.5 is a coin flip. Combining everything into a model got to **0.772** at a second, separate hospital.

What makes this paper worth reading is not the number. It is that **they tested the model at a different hospital from the one that built it** — which the last four papers in this reading list did not do — and that they then went looking for their own mistakes and published what they found.

## 2. Study Snapshot

**Study type:** a **retrospective two-centre cohort study** used to develop and externally validate a prediction model. Retrospective means they looked backwards through records already collected. Cohort means they started with people free of the disease and followed them forward in time to see who got it. That forward direction matters: it lets you say the predictors came *before* the outcome, which a snapshot study cannot. On the evidence ladder this sits above cross-sectional work and below a trial — and the authors make this exact point themselves, in a table comparing their design against three previous studies.

**Number of patients (n):** **1,944** adults who had an abdominal CT between January 2017 and January 2023 with **no gallstones** on that first scan.
- **Training cohort: 1,437** from Centre 1 — 222 developed gallstones (**15.4%**).
- **Test cohort: 507** from Centre 2 — 88 developed gallstones (**17.4%**).

Both percentages reconcile exactly, the two cohorts sum to 1,944, and the 310 stone patients match the 248 gallbladder + 28 bile duct + 34 both reported separately.

**Who they were:** median age 63 in both cohorts; about half male; median waist 91.8 cm (training) and 94.3 cm (test). The two centres differed significantly on waist, weight, lymphocytes, triglycerides, cholesterol, indirect bilirubin, hypertension and diabetes — which, as it happens, is what makes the external test meaningful.

**And here is the selection to keep in mind.** To count as a **non-case**, a patient had to have **at least one abdominal CT every year for three years** with no stones. To count as a **case**, a patient needed only **one** follow-up CT showing stones within three years. These are people getting repeated abdominal CT scans — mostly, the authors report, for abdominal pain or for cancer surveillance. The authors state this plainly as a limitation: "reflecting a clinical population rather than the general population."

**The outcome:** gallstones on any follow-up abdominal CT within three years — bright, well-defined, non-enhancing spots in the gallbladder or bile ducts.

**What was measured:** three competing categories, head to head.
- **CT body composition**, extracted automatically by a deep-learning tool called **BOA** (built on nnU-Net for tissue segmentation plus TotalSegmentator to find the third lumbar vertebra). It measured visceral fat, subcutaneous fat, intermuscular fat, muscle and bone — both as a single-slice area and as a volume — plus ratios between them.
- **Anthropometric indices**: BMI, waist circumference, body roundness index, relative fat mass, A Body Shape Index (ABSI), and two triglyceride-glucose indices.
- **Laboratory indices**: the neutrophil-to-lymphocyte ratio (NLR, an inflammation marker), total and indirect bilirubin, glucose, lipids.

**Models built:** weighted logistic regression as the **baseline comparator**, plus five machine-learning models — random forest, XGBoost, CatBoost, support vector machine, and extra trees (ET). Class imbalance was handled with class weights (positive-class weight = 1,215/222 = **5.47**, which reconciles exactly to the paper's stated "≈5.47"). Hyperparameters were tuned by **nested cross-validation** — an inner stratified fivefold loop with 50 random search draws, optimising AUC.

**Funding / conflicts of interest:** **not reported in the text provided.**

### The results

**Single measurements were all weak.** NLR best at AUC **0.627** (95% CI 0.586–0.668), then ABSI **0.615**, then the subcutaneous-to-total-fat area ratio (STR_area) **0.610**. All three below 0.63. The authors say so directly: a single index "could hardly meet clinical decision-making needs."

**Logistic regression** kept six predictors by weighted forward stepwise selection: STR_area, NLR, muscle area, ABSI, total bilirubin, and weight — all significant at p < 0.01. **Using the Youden threshold taken from the training set (0.492)**, it reached test-set AUC **0.675**, sensitivity 0.716, specificity 0.628, accuracy 0.643.

**The machine-learning models, training then test:**
- Extra trees: 0.828 → **0.772** (95% CI 0.714–0.822)
- Random forest: 0.806 → 0.733 (0.675–0.786)
- SVM: 0.787 → 0.697 (0.639–0.750)
- CatBoost: 0.771 → 0.688 (0.622–0.752)
- XGBoost: 0.761 → 0.668 (0.599–0.735)
- Logistic regression: 0.690 → 0.675 (0.609–0.741)

**Stability check:** repeated fivefold cross-validation with **50 different random seeds** gave extra trees a mean AUC of **0.810 ± 0.015** on the training data.

**SHAP importance:** STR_area, age, and the intermuscular-to-total-fat volume ratio (ITR_volume) ranked top.

**Two sensitivity analyses**, both reported with intervals: restricted to patients whose CT and ultrasound agreed or who had surgical confirmation, AUC **0.756** (0.655–0.840); excluding patients with isolated bile-duct stones, AUC **0.767** (0.711–0.817). Primary was 0.772.

**And a finding they went looking for and published.** Among the 1,069 patients who happened to have ultrasound data, **77 (7.2%) were CT-negative but ultrasound-positive** — meaning they were counted as non-cases when they had stones. The authors report this, explain why they did not simply reclassify them (ultrasound was available for only about half the cohort and at inconsistent times, so using it selectively would have introduced a different bias), and test the consequence instead.

### The 2×2 for the winning model, which the paper does not print

At 88 events among 507 test patients, sensitivity 0.671 and specificity 0.816 give: **59 true positives, 29 missed, 342 correctly cleared, 77 false alarms.** The model flags **136 of 507 — 26.9%**. PPV is **43.4%**, NPV **92.2%**, accuracy 79.1% — matching the paper's reported accuracy exactly.

**Against the trivial baseline:** flagging everyone would give a PPV of 17.4%. This model flags about a quarter of patients and is right 43.4% of the time about them. That is a real improvement — unlike several recent papers in this list, this operating point is doing genuine work.

## 3. How Strong Is This Evidence? (Grade 3/5)

**Grade: 3/5 — a modestly useful model, honestly built and genuinely tested somewhere else.**

This is the first 3 in four days, and the reason is specific: **it did the one thing the last four papers did not.** It trained at one hospital and tested at another, with no mixing. The two centres differ significantly on waist, weight, lipids, bilirubin, hypertension and diabetes, so the test was not a formality. That single design choice is worth more than any amount of algorithmic sophistication, and it is why this paper's 0.772 means something that a bigger number from an internal split would not.

**What it genuinely supports.** That among patients already having repeated abdominal CT scans, body composition measured automatically from those scans, combined with routine blood tests and basic measurements, identifies future gallstone risk with moderate accuracy — about 0.77 — and that this holds up at a hospital that did not build the model. And that no single index, CT-derived or otherwise, is adequate on its own.

**What it does not support.** That extra trees is the right algorithm, that this is ready for clinical use, or that the findings extend to people who are not having regular abdominal CTs.

**Four things keep it at 3 rather than 4.**

**"Extra trees performed best" is a ranking, not a finding.** Its test interval is 0.714–0.822. Random forest's is 0.675–0.786. Logistic regression's is 0.609–0.741. **The winner's interval overlaps every other model's**, and **no paired statistical test is reported** — no DeLong test, even though all six models were evaluated on exactly the same 507 patients, which is precisely the situation a paired test exists for. The Statistics Spotlight explains why comparing two intervals is not the same as testing a difference.

**No threshold is stated for the five machine-learning models**, and the consequences are visible. On the same test set, sensitivity ranges from **0.307 (XGBoost) to 0.716 (logistic regression)** — meaning the models flag between about 14% and 43% of patients. Those are not six answers to the same question; they are six different trade-offs, and the reader cannot tell how any of them was chosen. The one model whose threshold *is* stated — logistic regression's Youden 0.492 — was taken **from the training set and applied to the test set**, which is the correct procedure and the opposite of what three papers this week did. It deserves credit, and it makes the silence about the other five more conspicuous.

**The population is narrow in a way that is hard to generalise past.** A non-case needed annual abdominal CT for three years. A case needed one positive CT. Both groups are people under repeated imaging for abdominal pain or cancer surveillance. The authors name this. But there is a subtler asymmetry they do not address: **the control definition requires sustained access to imaging; the case definition does not.** Anyone who stopped attending is excluded from the control group but could still have entered the case group, which tilts the control group toward reliable, well-insured, closely followed patients.

**No calibration is reported.** The paper evaluates discrimination (AUC), accuracy, sensitivity, specificity, precision-recall curves and confusion matrices — but there is no calibration curve and no calibration statistic, and no decision curve analysis. For a tool proposed as a risk-stratification aid giving individual probabilities, calibration is the missing piece. (Yesterday's COPD paper, graded lower overall, did report both.)

**Two smaller things.** The univariate AUCs (0.610–0.627) jump to 0.772 when combined — a gain of 0.145 from parts that are individually almost useless, which is possible through interactions but is a large leap worth a sceptical look. And there is a small arithmetic slip: 1,069 of 1,944 patients having ultrasound data is **55.0%**, not the "approximately 53.6%" stated.

**What earns the 3, and it is a long list.**

**Genuine external validation, and the right reasoning about it.** When explaining why they did not do repeated random train-test splits, the authors write that it "would compromise the independence of the external validation cohort and undermine the validity of the external validation." That is exactly right, and it is a level of methodological care rarely seen.

**Nested cross-validation** for hyperparameter tuning — the inner loop choosing hyperparameters, the outer loop estimating performance — which is the correct structure and avoids the model-selection leak.

**A classical baseline, reported honestly even though it lost.** Including weighted logistic regression and printing its numbers alongside the five machine-learning models lets the reader judge whether the complexity bought anything.

**Bootstrap confidence intervals with 2,000 resamples on every metric**, on a test set with 88 events — a sound number for the method, unlike some recent examples in this list.

**A stability check across 50 random seeds**, reporting mean ± SD rather than one lucky run.

**Two sensitivity analyses, both pre-reasoned and both reported with intervals**, testing the two things most likely to be wrong: the outcome definition and the inclusion of bile-duct stones.

**They found their own misclassification and published it.** The 7.2% of CT-negative, ultrasound-positive patients is the kind of finding most authors would never have looked for. They looked, reported it, explained why a naive fix would make things worse, and quantified the impact instead.

**They pre-empted the obvious objection about differential follow-up.** The gallstone group had fewer follow-up CTs (4.37 versus 7.46 at Centre 1; 4.16 versus 6.72 at Centre 2) — which looks alarming until you see that the median time to stone detection was about 1.1 years, so case follow-up ended early by design. The authors spell this out rather than leaving the reader to wonder.

**They tabulated their own limitations against prior work.** Table 1 compares four previous studies and this one, with a limitations column — including their own ("Retrospective design; CT may miss isodense or small stones").

**Where 3/5 sits.** A sound, modest, honestly reported prediction study whose central claim — that combining CT body composition with routine blood tests predicts gallstones moderately well, and still does at another hospital — is supported by what was done. It falls short of 4 because the model comparison is not statistically established, the operating points are unexplained, and calibration is absent.

## 4. The Editor's Concerns

**Run a paired test on the model comparison.** All six models were evaluated on the same 507 patients. A DeLong test takes minutes and would say whether extra trees genuinely beats random forest or logistic regression, rather than leaving a ranking with overlapping intervals.

**State the thresholds for the machine-learning models, and where they came from.** Sensitivity ranging from 0.307 to 0.716 across six models on one test set is an unexplained spread. The logistic-regression threshold was handled correctly; say what was done for the rest.

**Report calibration.** A calibration curve and a calibration slope, plus a decision curve analysis, for a tool intended to stratify individual risk.

**Address the asymmetry in the case and control definitions.** Controls required three years of annual CT; cases required one positive scan. Say what that does to who ends up in the control group.

**Fix the ultrasound coverage figure.** 1,069 of 1,944 is 55.0%, not 53.6%.

**Report the per-unit odds ratios on a scale readers can picture.** "Each 0.01 increase in ABSI was associated with a 59% increase in risk" is accurate and nearly impossible to interpret, because 0.01 is roughly half of ABSI's whole plausible range. Give the odds ratio per standard deviation, or across the interquartile range.

**Say which hospital was Centre 1 and which was Centre 2.** Four affiliations are listed and the mapping is never stated, which matters for anyone assessing transportability.

**Explain the jump from 0.627 to 0.772.** A combined model that far above its best single component invites the question of what interaction is doing the work. A model with and without the body-composition block would settle how much the CT measurements actually added over blood tests and a tape measure — which is, after all, the paper's stated question.

**Add funding and competing-interests statements.**

### What this study did well

- **Trained at one hospital and tested at another**, with cohorts that genuinely differ — the single most important thing a prediction paper can do, and the thing the last four papers in this list did not.
- Gave the correct reason for refusing repeated random splits: it would undermine the independence of the external validation.
- Used **nested cross-validation** for tuning, which is the right structure.
- Included **logistic regression as a baseline** and reported it fairly.
- Computed bootstrap intervals (2,000 resamples) on every metric, at an event count where the method works.
- Checked stability across **50 random seeds** and reported mean ± SD.
- Took the logistic-regression classification threshold **from the training set** and applied it to the test set — the correct direction, and the opposite of several recent papers here.
- Ran **two sensitivity analyses** on the two most fragile assumptions, and reported both with intervals.
- **Went looking for its own outcome misclassification, found 7.2%, published it**, and explained why the obvious fix would introduce a worse bias.
- Pre-empted the differential-follow-up objection with the arithmetic that resolves it.
- Compared its own design against four prior studies in a table that includes a limitations column, its own included.
- Stated plainly that the cohort is a clinical population, not a general one.
- Reported the negative finding — that no single index was clinically adequate — as a result rather than burying it.

## 5. Statistics Spotlight

### Concept 1: The gap between how a model scores at home and how it scores somewhere else

This paper gives you six measurements of the same phenomenon, and the pattern in them is the lesson.

**What the gap is.** Every model is fitted to one set of patients. On those patients it will look better than it really is, because it has partly learned their quirks — which blood test happened to run high in that hospital's lab, which scanner produced slightly different fat measurements — as if they were general truths. Statisticians call the difference **optimism**. The only way to measure it is to test the model somewhere it has never been.

**How this paper applied it.** Every one of the six models dropped from the training centre to the test centre:

- Logistic regression: 0.690 → 0.675, a drop of **0.015**
- Extra trees: 0.828 → 0.772, a drop of **0.056**
- Random forest: 0.806 → 0.733, **0.073**
- CatBoost: 0.771 → 0.688, **0.083**
- SVM: 0.787 → 0.697, **0.090**
- XGBoost: 0.761 → 0.668, **0.093**

**Look at the order.** The **simplest model has by far the smallest drop** — about a sixth of XGBoost's. Logistic regression was the worst model at home and the most honest model away. The flexible tree-based models learned more about Centre 1, and a good deal of what they learned did not travel.

**The intuition.** A flexible model is a better memoriser. Give it enough freedom and it will fit not just the real pattern but the accidents of the particular people it was shown. Those accidents do not repeat at the next hospital, so the extra fit evaporates. A simple model cannot memorise much, so it has less to lose.

**An everyday analogy.** Two students prepare for an exam. One learns the underlying principles. The other memorises every past paper, including the quirks of the examiner who wrote them. On the past papers the memoriser scores higher. Then the exam board changes examiner. The principles still work; the memorised quirks are worthless. **Both students' past-paper scores were real. Only one of them was predictive.**

**The second measurement, which is the subtler one.** The authors also ran repeated fivefold cross-validation with 50 different random seeds and got **0.810 ± 0.015** for extra trees. That is careful internal validation — far better than a single split. At the outside hospital the model scored **0.772**.

**That is 0.038 below the internal estimate, about two and a half standard deviations of it.** So even properly-run, repeated, multi-seed internal cross-validation was systematically optimistic about an outside hospital — and its own uncertainty estimate did not cover the shortfall. Cross-validation measures how well a model handles *new patients from the same place*. It cannot measure how well it handles *a different place*, because every fold comes from the same hospital, the same scanners, the same lab.

**Watch out.** When a paper reports only cross-validated performance, you are being told how the model does on patients like the ones it was built from. That is a real number and it is not the number you need. **Look for a test cohort from a different site, and when you find one, look at the gap.** A large gap is not a scandal — this paper's gaps are honest and expected — but a paper that never measures the gap has not told you whether its model travels. And beware the reverse error: dismissing a model because it dropped. Every model drops. The question is how far, and whether what is left is useful.

### Concept 2: Why "the best model" is not established by overlapping confidence intervals

The paper concludes that extra trees performed best. Here is why that is a ranking rather than a result, and why the fix is straightforward.

**What a confidence interval is.** The paper's test-set AUCs come with 95% intervals from bootstrap resampling — repeatedly drawing patients from the test set with replacement, recomputing, and taking the middle 95% of the answers. It describes how much the number would wobble if you had happened to get a different sample of 507 patients.

**The intervals here:**

- Extra trees: 0.772, interval **0.714 to 0.822**
- Random forest: 0.733, **0.675 to 0.786**
- SVM: 0.697, 0.639 to 0.750
- CatBoost: 0.688, 0.622 to 0.752
- Logistic regression: 0.675, **0.609 to 0.741**
- XGBoost: 0.668, 0.599 to 0.735

**Extra trees' interval overlaps every single one of the others.** Random forest's plausible range runs up to 0.786, above extra trees' point estimate of 0.772. On this evidence you cannot say which of the two is better.

**But here is the important part, and it cuts both ways.** Two overlapping intervals do **not** prove there is no difference either. Comparing two separate intervals is simply the wrong tool, because it ignores the single most useful fact available: **these six models were run on exactly the same 507 patients.**

**Why that matters, with a tiny worked example.** Suppose two models each get 70% of a hundred patients right. If they are right about *different* patients, the comparison is very uncertain — either could be better. But suppose they agree on 90 patients and disagree on 10, and of those 10, model A is right 9 times. That is a clear, consistent difference, visible only because you looked at the same patients twice. A separate interval for each model throws that information away.

**The right tool** is a **paired test** — for AUCs, **DeLong's test**, which compares two curves measured on the same people and accounts for the fact that they are correlated. This reading list has met it before. It is a standard function in every statistics package, it takes minutes, and its absence here is the paper's main analytical gap.

**An everyday analogy.** Two runners each run a separate race on a separate day in separate weather, and their times are close. You cannot say who is faster. Put them on the same track in the same race and you can — not because they got faster, but because you removed everything that was varying between them. The track and the weather are the patients; running them separately and comparing ranges is throwing away the race.

**Watch out.** "Model X achieved the highest AUC" is one of the most common claims in medical AI and one of the least often tested. **Two checks: do the intervals overlap, and was a paired test run?** If the intervals overlap and no paired test is reported, you have a league table, not a result. And when you see a league table of six or eight algorithms with no paired tests, remember that the winner of such a table is partly whichever model got luckiest on that particular test set — which is why rankings so often reshuffle when someone else repeats the comparison.

### Concept 3: What external validation actually is, and why these authors refused to do more splits

This is the thing this paper does right, and it is worth understanding properly because it is the single best predictor of whether a published model will work in your hospital.

**The ladder.** There are degrees of validation, roughly in order of how much they prove:

1. Performance on the training data itself. Almost meaningless.
2. A random split of one dataset into train and test. Better, but both halves share the same hospital, scanners, lab and patient mix.
3. Cross-validation, including the repeated multi-seed kind done here. Better still, and still entirely within one place.
4. **A different hospital** — what this paper did.
5. A different country or health system.
6. Prospective deployment, where the model runs on patients as they arrive.

**How this paper applied it.** Centre 1 trained, Centre 2 tested, no mixing. And the two centres genuinely differ: significantly on waist circumference, weight, lymphocyte count, triglycerides, total cholesterol, indirect bilirubin, hypertension and diabetes. **The test cohort was not a copy of the training cohort with a different label on it**, which is exactly what makes the 0.772 informative.

**The sentence that shows they understood this.** Explaining why they did not do repeated random train-test splits, the authors write that doing so "would compromise the independence of the external validation cohort and undermine the validity of the external validation."

That is subtle and correct, and it deserves spelling out. Repeated random splitting would have meant shuffling patients from both centres together and re-dividing them. It would have produced tighter, nicer-looking intervals. **And it would have destroyed the only thing that made the evaluation worth anything**, because every test set would then have contained patients from the training hospital. A great many papers do exactly this and present it as rigour, because more resampling looks like more care.

**An everyday analogy.** You develop a recipe in your own kitchen and want to know whether it works. Making it fifty more times in your own kitchen, carefully averaging the results, tells you about your kitchen: your oven's hot spot, your altitude, your tap water. Making it once in a friend's kitchen tells you something your fifty attempts could not. **Averaging more trials inside one kitchen reduces the wobble in your estimate without touching the thing you are actually unsure about.** And if you then pooled all fifty-one attempts together and resampled from the mixture, you would have thrown away the one informative test.

**The related thing they got right.** The logistic-regression classification threshold was chosen by the Youden index **on the training set** (0.492) and then applied unchanged to the test set. That is the correct direction: pick your settings where you are allowed to look, then measure where you are not. Three papers decoded in this list over the past week did the opposite, choosing thresholds on the very data they then reported. **This paper, graded lower on other grounds than one of those, got the fundamental sequence right.**

**Watch out.** "Externally validated" is now a marketing phrase and it covers all of rungs 2 through 6. **Ask one question: did the test patients come from a different institution than the training patients, and did any patient appear in both?** If a paper says "we split the data 70:30", that is rung 2 regardless of how the sentence is dressed. If it says "we validated in an independent cohort from another centre", that is rung 4 and worth considerably more. And watch for the specific failure this paper avoided: a paper that pools multiple centres and then randomly splits the pool has an impressive-sounding multi-centre dataset and a rung-2 validation.

## 6. Jargon Translator

- **Gallstones** — hard deposits that form in the gallbladder or bile ducts, often needing surgery and sometimes causing serious complications.
- **Cholecystectomy** — surgical removal of the gallbladder.
- **Abdominal CT** — a cross-sectional X-ray scan of the abdomen.
- **L3 level** — the third lumbar vertebra. A single CT slice there correlates well with whole-body fat and muscle, so it is the standard place to measure body composition.
- **Visceral adipose tissue (VAT)** — fat packed around the internal organs; metabolically active and the more harmful kind.
- **Subcutaneous adipose tissue (SAT)** — fat under the skin; metabolically quieter and, in this study, apparently protective.
- **Intermuscular adipose tissue (IMAT)** — fat deposited inside muscle; linked to insulin resistance and low-grade inflammation.
- **STR_area / VTR / ITR_volume / VSR** — ratios of subcutaneous, visceral or intermuscular fat to total fat, by area or volume. STR_area (subcutaneous as a share of total) was the top predictor here.
- **BOA (Body and Organ Analysis)** — the automated deep-learning tool that measured all of this from the scans, combining **nnU-Net** for tissue segmentation with **TotalSegmentator** for locating anatomy.
- **BMI** — weight divided by height squared. Cannot tell fat from muscle, which is this paper's starting complaint.
- **ABSI (A Body Shape Index)** — a measure of abdominal fat relative to the rest of the body, adjusted for height and weight.
- **BRI / RFM / TyG** — body roundness index, relative fat mass, and the triglyceride-glucose index; other single-number body or metabolic measures.
- **NLR (neutrophil-to-lymphocyte ratio)** — the ratio of two white blood cell types, used as a cheap marker of whole-body inflammation. The single best predictor here, at AUC 0.627.
- **Total / indirect bilirubin** — breakdown products of red blood cells, processed by the liver and excreted in bile.
- **Extra trees (extremely randomized trees)** — like a random forest but with its split points chosen at random, which makes it less prone to memorising and often better at generalising.
- **Random forest / XGBoost / CatBoost** — three other ways of combining many decision trees. **Support vector machine** separates classes by finding the best dividing boundary.
- **Weighted logistic regression** — classical regression with the rare outcome counted more heavily so the model does not simply predict "no" for everyone.
- **Class weights** — the multiplier applied to the rare group. Here 1,215 ÷ 222 = 5.47.
- **Forward stepwise selection with BIC** — adding predictors one at a time, keeping those that improve a score penalising complexity.
- **Nested cross-validation** — an inner loop for choosing settings and an outer loop for measuring performance, so the settings are never chosen using the data that scores them.
- **Youden index** — sensitivity plus specificity minus 1. The threshold maximising it treats a missed case and a false alarm as equally bad.
- **Bootstrap confidence interval** — a range of plausible values, built by resampling the data (2,000 times here).
- **Precision-recall curve / average precision (AP)** — an alternative to the ROC curve, more informative when the outcome is rare. Extra trees had the highest AP at 0.642.
- **Confusion matrix** — the four-box table of true and false positives and negatives.
- **SHAP** — assigns each feature a share of the credit for a prediction.
- **DeLong's test** — the paired test for comparing two AUCs measured on the same patients. Not used here, and should have been.
- **Calibration** — whether predicted probabilities match observed rates. Not reported here.
- **Sensitivity analysis** — repeating the analysis under a different assumption to see whether the conclusion survives. Done twice here, well.
- **Outcome misclassification** — labelling someone as not having the disease when they do. Here, the 7.2% who were CT-negative but ultrasound-positive.
- **Mendelian randomization** — a method using inherited genetic variants to probe whether an association is causal; cited in the introduction as evidence that obesity causes gallstones.

## 7. What You Can (and Can't) Say

**Fair to say:**

- "In 1,944 patients who had an abdominal CT showing no gallstones, 310 developed stones within three years, and a machine-learning model using CT body composition plus blood tests predicted this with an AUC of 0.772 at a second, independent hospital."
- "No single measurement was clinically useful on its own: the best was a blood inflammation ratio at AUC 0.627, and the best body-composition and tape-measure indices were 0.610 and 0.615."
- "The study trained its model at one hospital and tested it at another, which most prediction papers do not do."
- "The share of fat that is subcutaneous rather than visceral was the model's most important predictor, and more subcutaneous fat was associated with lower risk."
- "The authors found that 7.2% of patients with ultrasound data had stones their CT had missed, reported it, and showed the model's performance barely changed when restricted to confirmed cases (0.756 versus 0.772)."
- "Every model performed worse at the second hospital, and the simple logistic regression lost the least."
- "The winning model flags about 27% of patients and is correct about 43% of those it flags, against a background rate of 17%."

**Not fair to say:**

- ❌ "Extra trees was the best algorithm." Its confidence interval overlaps every other model's, and no paired test was run.
- ❌ "Machine learning beats logistic regression for gallstone prediction." Possibly, but not shown: 0.772 (0.714–0.822) against 0.675 (0.609–0.741), untested, and the simple model generalised far better.
- ❌ "CT body composition predicts gallstones better than BMI or waist size." The CT index scored 0.610 and the tape-measure index 0.615. They were equivalent, and both nearly useless alone. The paper never isolates how much the CT block added to the combined model.
- ❌ "A CT scan can now tell you your gallstone risk." It can contribute moderately, in a population already under repeated abdominal imaging, with no calibration reported and no test of whether acting on the prediction helps.
- ❌ "Subcutaneous fat protects against gallstones." It was associated with lower risk in one retrospective model. The paper's own limitations note that unmeasured diet, exercise, smoking and alcohol could explain it.
- ❌ "These results apply to the general population." Controls needed an abdominal CT every year for three years. The authors say explicitly that this is "a clinical population rather than the general population."
- ❌ "The model is 79% accurate." Accuracy is a poor summary when 83% of patients do not get the outcome — always saying "no" would be 82.6% accurate.
- ❌ "Inflammation causes gallstones." NLR predicted stones with an AUC of 0.627. That is an association in an observational study, and a weak one.

## 8. Bottom Line for Your Life

If you are worried about gallstones, nothing here changes anything today. The known risk factors have not moved — being overweight, rapid weight loss, female sex, older age, family history — and the one practical message is about where your risk sits, not what to do: fat around the organs looks worse than fat under the skin, which is why two people with the same BMI can carry quite different risk. No tool in this paper has been tested on whether using it helps anyone, and nobody should be having a CT scan to check their gallstone risk. If you happen to be having an abdominal CT anyway, this line of work suggests the scan already contains information nobody currently reads.

For anyone appraising research, this paper is the useful counterexample to the four before it in this list — so take the check it passes rather than one it fails.

**When a paper reports how well a model performs, find out where the test patients came from.** Same hospital, different patients, however carefully resampled, tells you about that hospital. A different hospital tells you whether the model travels. Here every model got worse at the second hospital, the sophisticated ones got worse faster than the simple one, and even 50-seed cross-validation overestimated the outside result by more than its own uncertainty allowed for. **None of that is a flaw in this study — it is the study's contribution.** The papers to distrust are not the ones that show a drop. They are the ones that never created the opportunity to see one.

---

*This is an educational analysis of a published scientific paper, not medical advice. Nothing here is guidance about gallstones, imaging or your own risk. If you have abdominal pain or concerns about your gallbladder, speak to a clinician.*
