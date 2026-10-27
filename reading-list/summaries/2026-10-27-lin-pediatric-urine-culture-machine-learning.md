# Construction and validation of a machine learning model for predicting urine culture positivity in children with suspected urinary tract infections

**Authors:** Lin S, Yao J, Fu Q, Wu Y, Deng S, Wang B (six authors; Clinical Laboratory, Fujian Children's Hospital — Fujian Branch of Shanghai Children's Medical Center, College of Clinical Medicine for Obstetrics and Gynecology and Pediatrics, Fujian Medical University, Fuzhou, China; one author at Minhou County Hospital)
**Journal:** Annals of Medicine, 2026; 58(1): 2742648 (published 7 October 2026)
**Decoded:** 2026-10-27
**Analysis basis:** **FULL TEXT** (retrieved from PubMed Central, PMC13647408; 44,395 characters). Figures are read from the PMC rendering's alt-text descriptions, which here are unusually detailed and carry real numbers. Figure 4D — the bar chart holding accuracy, precision and specificity for all seven models — is described only qualitatively, so those numbers are **not retrievable** and are marked as such throughout. The URL of the authors' web calculator was stripped by the text extraction and **could not be recovered; it is therefore not reproduced here.**

**Source links (verified):**
- DOI: https://doi.org/10.1080/07853890.2026.2742648
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42841462/
- Full text (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC13647408/

**Basis of link verification.** Direct URL fetching is blocked from this session (`doi.org` does not resolve under the network policy here). Verification was done against the live PubMed/NLM record: a query for PMID 42841462 returned this exact title, these six authors, Annals of Medicine volume 58 issue 1 article 2742648, DOI `10.1080/07853890.2026.2742648` and PMC ID `PMC13647408`; the full text was then retrieved from PubMed Central by that PMC ID and matches. Both halves of the chain were confirmed independently. According to PubMed, the record is typed "Journal Article; Validation Study".

**Funding: not reported in the text retrieved.** **Competing interests: not reported in the text retrieved.** **No reporting guideline (TRIPOD, TRIPOD+AI, STARD or otherwise) is named.**

**Ethics:** approved by the Ethics Committee of Fujian Children's Hospital (Approval No. 2026ETKLRK03021); written consent waived, with the waiver's reasoning stated — retrospective, routine data, minimal risk, de-identified before analysis.

> **Why this paper today.** The four deferred papers were re-checked this morning and all four are still blocked. Google's personal health agent (Nature, PMID 42907512), the BMJ review of LLM-trial reporting (PMID 42869550) and the Annals of Internal Medicine Choosing Wisely benchmark (PMID 42896192) returned **no PMC identifier at all** on an ID-conversion query, meaning no PubMed Central copy exists to read. The JAMA OpenEvidence study (PMID 42879271, PMC13673371) has a PMC record that **still serves a completely empty body — day 12.** This paper was spare #5, flagged four days ago because it ships something the others did not: a **live web calculator for clinicians**, built on a single hospital's data with no external validation. A deployed tool raises the bar for what the paper has to show, and the gap between what it shows and what a deployed tool needs is the whole lesson.

---

## 1. The Gist

A child arrives at hospital with a fever, or with something odd on a urine dipstick. Nobody can tell from the outside whether there are bacteria growing in the bladder. So the lab sends the urine for culture: smear it on a plate, incubate it, wait 24 to 48 hours, see what grows.

Two things are wrong with that. The wait is long enough that doctors start antibiotics on a guess. And roughly seven or eight out of every ten cultures come back empty — the lab spent two days proving nothing was there.

Six researchers at a children's hospital in Fuzhou, China, pulled the records of 581 children, aged nine days to seventeen years, whose doctors suspected a urinary tract infection between 2023 and 2025. For each one they knew what the culture eventually showed. **245 of the 581 — 42% — grew bacteria.** They then built a computer model to guess that answer in advance, from seven numbers that come back the same day: whether the child is a boy, the lymphocyte count, the CRP (an inflammation marker), two urine dipstick readings, the automated urine white-cell count, and the automated urine bacteria count.

Shown one child who would culture positive and one who would not, the best model picks the right one about **81 times in 100.** It catches **77 of every 100 children whose culture would be positive.**

They put it on the internet as a calculator doctors can use.

Here is the problem, and it is not subtle. **The paper never prints the one number its own tool depends on.** The stated purpose is to save cultures — to let a lab skip the two-day wait on specimens that were never going to grow anything. Whether you can safely do that is governed by *specificity*: of the children who would culture negative, how many does the model correctly flag as negative? Specificity appears in the methods as a metric they computed, and then appears in the results only as an unlabelled bar in a chart. There is no number for it anywhere in the text.

The model is also not calibrated — the percentage on the calculator's screen is anchored to a 50/50 background rate that no clinic has, and the paper prints the proof of this without noticing. And the headline comparison that justifies the machine learning at all turns out, on inspection, to compare two numbers computed on different groups of children.

None of which is to say the work is bad. The honesty of its limitations section is genuinely above average for this reading list. But a paper that deploys a public tool has volunteered for a stricter standard than a paper that just reports a result.

## 2. Study Snapshot

**Study type:** a **single-centre retrospective diagnostic prediction study**. Records already collected were searched backwards; no child was approached, randomised, or followed forward. On the evidence ladder this sits below a prospective cohort and well below a trial. Note it is a *diagnostic* model, not a *prognostic* one: the seven inputs and the outcome are measured from the same urine specimen at the same moment. The model does not predict the future. It predicts what a slower test, run on the same sample, will say.

**Who:** 581 children with suspected UTI at Fujian Children's Hospital, January 2023 to December 2025.

**Age:** median 7 months and 24 days; range 9 days to 17 years. The cohort is heavily weighted toward babies — **355 children (61.10%) were under 12 months**, 122 (21.00%) were 1–3 years, and only 104 (17.90%) were 4–17. **82.1% were under three.** The paper flags this itself.

**Outcome:** urine culture positivity, defined by standard colony-forming-unit thresholds from paediatric guidelines. **245 positive (42.17%), 336 negative (57.83%).** All the arithmetic in the cohort table reconciles exactly.

**Specimen collection** is described properly and this matters more than it looks: urine bags after perineal disinfection for babies not yet toilet-trained, catheterisation or suprapubic aspiration for children with voiding problems, clean midstream for older children, and everything inoculated within 1–2 hours. Collection method is the single biggest source of contamination in paediatric urine, and a model trained on contaminated specimens learns contamination. The paper handled this.

**Candidate inputs:** 15 variables — sex, age, seven blood-count measures, CRP, and four urinalysis measures (leukocyte esterase, nitrite, urine white cells, urine bacterial count).

**Final inputs:** 7 — sex, lymphocyte count, CRP, leukocyte esterase, nitrite, urine bacterial count, urine white cell count. **Age was dropped by the selection procedure**, in a cohort where 61% were infants.

**Split:** 581 children split 7:3 into a training set of 406 (171 positive, 235 negative) and a held-out internal validation set of 175 (74 positive, 101 negative), stratified by outcome. Every count reconciles, and the prevalence is preserved almost exactly across both halves (42.12% and 42.29% against 42.17% overall). That is what stratification is supposed to do and it demonstrably did it.

**Models:** seven — logistic regression, support vector machine, random forest, gradient boosting, k-nearest neighbours, XGBoost, LightGBM.

**Headline result:** random forest, validation AUC **0.814 (95% CI 0.742–0.875)**, sensitivity **0.770 (95% CI 0.662–0.865)**, Brier score 0.188.

**External validation: none.** The paper says so plainly and repeatedly.

**Secondary output:** a map of which bacteria were found and what they resist, from this hospital over three years. This part is straightforwardly useful and is discussed in Section 7.

## 3. How Strong Is This Evidence? (Grade 2/5)

**What the paper does right, and some of it is genuinely good:**

**A real leakage firewall, stated in the authors' own words.** "To prevent data leakage, all data preprocessing, feature selection algorithms (LASSO, RFE, and univariate statistical screening), and hyperparameter optimization were strictly fitted using only the training set (n = 406). The internal holdout validation set (n = 175) was kept entirely unseen until final model evaluation." That sentence is the difference between a validation number that means something and one that does not, and most papers in this reading list do not contain it.

**The hyperparameter search is fully described.** RandomizedSearchCV, 40 iterations, 5-fold stratified cross-validation, with the actual search space printed (100–1500 trees, depth 3–10 or unlimited, minimum split 2–20, feature fraction 0.2–0.5) and the winning configuration printed (1000 trees, depth 4, minimum split 10, feature fraction 0.3). You could rerun this.

**Enough events for seven predictors.** 171 positive cases in training against 7 predictors is 24 events per predictor, comfortably above the conventional floor of 10. This is one of the few papers in this list where that calculation is not a worry.

**The confidence intervals are honest.** I reconstructed the sensitivity as 57 of 74 children (0.770 × 74 = 56.98) and computed the exact Clopper–Pearson binomial interval: **0.658 to 0.860**, against the paper's bootstrap interval of 0.662 to 0.865. Those agree to within four thousandths. The bootstrap with only 500 replicates was adequate here, and I am noting that because on previous papers in this list I have criticised small-replicate bootstraps; this one checks out.

**The limitations section is unusually complete.** It names the single-centre design, the 74-positive holdout, the overfitting visible in the boosting models, the width of its own confidence interval, the age skew, the fact that age was dropped, the culture-negative-infection problem, and SHAP's inability to show causation. It uses the words "our findings should be interpreted strictly as preliminary." That is more candour than most.

**Why it still sits at 2 out of 5:**

**There is no external validation of any kind, and a temporal one was available for free.** The cohort spans three full calendar years, and the paper already breaks its resistance analysis out by year — so the year each child presented is in the dataset. Training on 2023–2024 and testing on 2025 would have cost nothing, required no new data, and produced a genuine test of whether the model survives a shift in time. They chose a random split instead. A random split asks "does this model work on more children exactly like these?" A temporal split asks "does it work next year?" Only the second question is the one a deployed tool faces.

**The headline comparison is between numbers computed on different groups of children.** The paper argues the machine learning earns its keep by comparing the random forest (AUC 0.814) to the urine bacterial count alone (AUC 0.730). But look at the confidence intervals: 0.692–0.769 for the bacterial count, half-width 0.039; 0.742–0.875 for the forest, half-width 0.067. A Hanley–McNeil calculation says an AUC of 0.730 measured on 245 positives and 336 negatives — the **full cohort** — should have a half-width of about 0.042, and an AUC of 0.814 measured on 74 positives and 101 negatives — the **holdout** — should have about 0.067. Both match almost exactly. The single-variable baseline was scored in-sample on everybody; the model was scored out-of-sample on a quarter of them. That is not a like-for-like comparison, and the paper's conclusion that nonlinearity "more successfully captures complex diagnostic signals" rests on it. This is explained in detail in Section 5.

**The model's probabilities are miscalibrated by construction, and the paper prints the receipt.** All tree models were fitted with `class_weight = "balanced"`, which tells the algorithm to treat the 171 positives as if they weighed as much as the 235 negatives. The model therefore learns a world where positives and negatives are equally common. The proof is in the SHAP waterfall plot: the base value, meaning the model's average output across the data, is **E[f(X)] = 0.499** — while the actual training prevalence is **42.1%**. The calculator is anchored to a coin flip. A clinician reading "50%" off the screen is reading a number centred on a background rate their clinic does not have.

**Specificity is never printed.** The whole clinical argument — that this saves the lab from culturing specimens that will not grow — depends on specificity or negative predictive value. Specificity is listed in the methods as a computed metric, appears in Figure 4D as a bar, and never appears as a number in the text. Sensitivity is given to three decimals with a confidence interval. The metric that governs the stated use case is the one left in the picture.

**The Brier score is described as a calibration measure, which it is not.** The figure legend says "A Brier score of 0.188 indicates a modest calibration improvement relative to the baseline prevalence." A Brier score is a combined measure; calibration is only one of its parts. Worked through in Section 5.

**An internal contradiction in the interpretability section.** The text says the random forest "was chosen to interpret the model's output," and then the very next clause says "the variables importance based on **LGBM** model is shown in [Figure 5A]." One of those is wrong, and a reader cannot tell which model the SHAP figures belong to.

**Two arithmetic problems in Table 1.** Not conclusion-changing, but they show the table was not re-derived. Detailed in Section 4.

**What would make this a 3:** either a temporal split using the data already in hand, or a second hospital. Plus the specificity number printed as a number. Either of those two, by itself, would move it.

**What would make it a 4:** both of the above, a calibration curve with an intercept and slope rather than a Brier score, a stated decision threshold, and the baseline comparison redone on the holdout so it compares like with like.

## 4. The Editor's Concerns

**The outcome is a laboratory result, not a disease — and here that makes the model look worse than it is.** This is an inversion of a problem this list usually sees from the other direction. Normally a badly chosen outcome flatters a model. Here the paper's own third limitation points out that up to 31% of febrile infants with pyelonephritis have *negative* cultures, because of antibiotics given before arrival, imperfect collection, or organisms the culture does not grow. Those children are genuinely infected, are sitting in the negative group, and the model — correctly reading their inflammation — scores them high. They are counted as the model's mistakes. The reported specificity is therefore biased **downward** by children the model got clinically right. The authors identified this. It is a point in their favour that they did.

**The control group is sicker than the case group, and that has consequences the paper does not follow through.** Fever was present in 52.2% of culture-positive children and **73.5%** of culture-negative children (p < 0.001). Median CRP was 18.53 mg/L in the positives and **24.56 mg/L** in the negatives (p = 0.02). The children whose cultures grew bacteria were, by systemic inflammatory markers, *less* unwell than the children whose cultures did not. The explanation is sampling: a feverish child with a chest infection gets a urine culture as part of a routine fever workup, and that culture comes back clean. The paper gives this explanation and it is correct. What it does not say is the consequence: **CRP enters the model with a negative weight.** The model has learned "high CRP makes a positive culture less likely." That relationship is true in this hospital's referral pattern. It is not a fact about urinary tract infections, and in a clinic that only cultures urine when a urinary source is already suspected, it could point the wrong way.

**A feature-selection rule that was overruled at the end.** The three methods — LASSO, recursive feature elimination, and univariate testing — intersected on five variables. The authors then put the urine bacterial count and urine white cell count back in "based on their established clinical indispensability." That is a defensible choice, they state it openly, and the two variables they added were the strongest univariate predictors anyway. But it means the pipeline is not purely data-driven, and the paper does not say whether the override was decided before or after anyone looked at model performance. The firewall statement covers the algorithms; it does not cover the human decision layered on top of them.

**The deployed calculator has no stated threshold.** A sensitivity of 0.770 implies that some probability cut-off was chosen to convert the model's output into a yes/no. That cut-off appears nowhere. The calculator, by the figure's description, returns a probability. A clinician looking at 47% cannot know whether that is above or below the operating point that produced the published sensitivity — and because of the calibration problem above, cannot read it as a risk either.

**Table 1 percentage errors.** Two of them. In the clinical-diagnosis block, fever is given as 128 (25.00%) in the positive group and 247 (48.24%) in the negative group. Neither percentage uses that group's size: 128/245 is 52.24% and 247/336 is 73.51%. Both reported figures correspond to a denominator of **512**, which is not 245, not 336, not 581, and not their sum. The same denominator produces the abnormal-urinalysis row. Separately, Table 1 reports 134 children with underlying disease (75 positive, 59 negative) and uses 134 as the denominator for the individual conditions — but the Results text gives vesicoureteral reflux as **81.57%** of underlying disease, which requires a denominator of **114**, the sum of the three named conditions. Against the table's own 134, reflux is 69.4%. Neither error changes a conclusion. Both indicate nobody re-derived the table from the data.

**A chi-square that does not reproduce.** The fever comparison is reported as chi-square 28.92. Computed from the group counts (128/245 versus 247/336) I get 28.00. The p-value is below 0.001 either way, so nothing turns on it — but combined with the denominator problems above, the clinical-diagnosis block of Table 1 should be treated as approximate.

**"Superior generalization" is being used to mean two different things.** XGBoost went from a training AUC of 1.000 to a validation AUC of 0.707; the random forest went from 0.845 to 0.814. The paper reads the small gap as evidence of the forest's robustness. The gap is small because the forest was *constrained* — depth 4, minimum 10 samples per split, 30% of features per split. A shallow forest cannot memorise, so it has nothing to lose. That is a fact about the hyperparameter search, not a virtue of the algorithm. The number that matters to a user is 0.814, and it would matter exactly as much if the training AUC had been 1.000.

**No reporting guideline, no funding statement, no competing-interests statement** in the text retrieved. TRIPOD+AI fits this study precisely and the paper already satisfies a good share of it.

**Where I am uncertain, stated plainly.** Figure 4D contains accuracy, precision, specificity and F1 for all seven models as bars, and the PMC alt-text describes it only in words. I cannot read those values, so I cannot reconstruct the confusion matrix, cannot compute the negative predictive value, and cannot check the F1 claim. Everything I have asserted above comes from numbers printed in the text. The web calculator's address was stripped from the extracted text and **I have not reproduced it rather than guess at it.**

## 5. Statistics Spotlight

Five things worth learning from this paper. The first one is a technique you can use on any paper, forever.

### A confidence interval tells you how big the sample was. Use that.

The paper's case for machine learning rests on one comparison: the urine bacterial count alone gets an AUC of 0.730, the random forest gets 0.814, therefore the combination and the nonlinearity are earning their keep.

Look at what is printed next to each number.

- Bacterial count alone: **0.730 (95% CI 0.692 to 0.769).** Half-width 0.0385.
- Random forest on validation: **0.814 (95% CI 0.742 to 0.875).** Half-width 0.0665.

The forest's interval is **1.7 times wider.** Intervals get wider when samples get smaller. So these two numbers were not computed on the same children.

You can check this without being told. There is a standard formula — Hanley and McNeil, 1982 — that gives the approximate standard error of an AUC from the AUC itself and the number of positives and negatives. Run it both ways:

- AUC 0.730 on 245 positives and 336 negatives — **the whole cohort** — gives a 95% half-width of **0.042**. Reported: 0.0385.
- AUC 0.814 on 74 positives and 101 negatives — **the holdout** — gives a 95% half-width of **0.067**. Reported: 0.0665.

Both land. The baseline was measured on all 581 children, in-sample, using data the selection procedure had already seen. The model was measured on the 175 children it had never seen. One is a best-case estimate, the other is an honest one, and they are being subtracted from each other.

That does not mean the forest is worthless. It means **the 0.084 gap has not been measured.** To measure it you compute both numbers on the same 175 children and run a paired DeLong test, which costs nothing and is not done here.

**The general technique: before you accept any comparison between two numbers in a paper, check whether their confidence intervals are the same width.** If they differ a lot, they came from different amounts of data, and you should find out why before you let the paper subtract them. This works on AUCs, proportions, hazard ratios, anything with an interval. It takes ten seconds and it catches mismatches the text will never mention.

### The SHAP base value tells you the model's effective prevalence

Buried in the description of the SHAP waterfall plot is this: the base value is **E[f(X)] = 0.499**, and the worked example lands at f(x) = 0.474, described as "slightly below the population baseline."

The population baseline is not 0.499. In the training set, 171 of 406 children cultured positive. **That is 0.421.**

Where did the extra 0.078 come from? From `class_weight = "balanced"`, applied to every tree model in the study. That setting multiplies each class's contribution to the loss so that the smaller class counts as much in total as the larger one. Functionally, the model is trained on a world where positives and negatives occur equally often.

The consequence is exact and predictable: **the model's average output moves to 0.5.** Which is precisely what the figure reports.

For picking out who is at higher risk, this is harmless — shifting everyone by the same amount leaves the ranking untouched, which is why the AUC is unaffected. For a calculator that displays a percentage to a doctor, it is not harmless at all. Every number it shows is pulled toward 50%. Low-risk children look riskier than they are; the whole scale is stretched around the wrong centre.

**The technique: when a paper reports a SHAP base value, compare it to the outcome rate in the training data. They should match. If the base value is near 0.5 and the prevalence is not, class weighting or resampling has moved it, and the model's probabilities are no longer probabilities.** The fix is cheap — refit the probabilities on held-out data with Platt scaling or isotonic regression, and report the calibration intercept and slope — and it is not done here.

This is the second paper this week where balanced class weights broke calibration. It is now the single most common way a clinical model ships a number nobody can use.

### A Brier score is not a calibration score

The figure legend reads: "A Brier score of 0.188 indicates a modest calibration improvement relative to the baseline prevalence."

A Brier score is the average squared distance between the predicted probability and the actual 0-or-1 outcome. Lower is better; 0 is perfect. It is a *proper scoring rule*, meaning it rewards honest probabilities — and that is precisely why it is not a calibration measure. It bundles two different virtues together:

**Brier = reliability − resolution + uncertainty.**

- *Reliability* is calibration: when you say 30%, does it happen 30% of the time? Lower is better.
- *Resolution* is discrimination: do you spread your predictions out, confidently high for some and low for others, rather than hedging at the base rate? Higher is better.
- *Uncertainty* is the irreducible part, fixed by the prevalence alone, and the model cannot touch it.

So a model can earn a good Brier score by discriminating sharply while being systematically wrong about the numbers, and a model can earn a bad one by being perfectly calibrated and useless.

Do the arithmetic on this paper. Validation prevalence is 74/175 = **0.4229**. A model that gives every single child that same number, and so has zero discrimination but perfect calibration, scores:

> 0.4229 × (1 − 0.4229) = **0.2440**

The paper's 0.188 against that no-skill floor gives a **Brier skill score of 0.230** — the model closes 23% of the gap between knowing nothing and being perfect. That is real, and it is modest. But it tells you nothing about *which* of the two components produced it, and from everything in the previous subsection we have strong reason to think reliability is the weak half.

**The technique: a Brier score alone is uninterpretable. Compute p × (1 − p) from the prevalence first and compare. Then, if you want to know about calibration specifically, ask for the calibration intercept and slope, which separate the two components and tell you the direction of the error.** The paper has the calibration plot. It reports a Brier score instead of reading its own curve.

### When the controls are sicker than the cases, a coefficient's sign belongs to the study design

Two findings in Table 1 run backwards from clinical intuition:

- Fever: **52.2%** of culture-positive children versus **73.5%** of culture-negative children.
- CRP: median **18.53** versus **24.56** mg/L, p = 0.02.

The children with bacteria in their urine were less feverish and had less inflammation than the children without.

This is not a mystery and the paper explains it correctly: the culture-negative group is not healthy children. It contains feverish children whose infection is somewhere else and who got a urine culture as part of a workup, and it contains children with genuine urinary infections that failed to grow. Both of those push fever and CRP up in the negative group.

But follow it through to the model. CRP is one of the seven inputs, and the univariate analysis confirms it has a **negative** association with culture positivity. **The model has learned that higher inflammation argues against a positive urine culture.**

Inside Fujian Children's Hospital's referral pattern during 2023–2025, that is an accurate statistical fact and it helps the model. Take the model somewhere that only cultures urine when a urinary source is already suspected — so the comparison group no longer contains all those feverish chest infections — and the relationship weakens or reverses, and the CRP input starts actively hurting.

**The technique: when a predictor's direction surprises you, do not reach for a biological story. Ask what the comparison group is made of.** A coefficient is a statement about a contrast between two specific groups of people, not a statement about the body. Change who is in the control group and the coefficient can flip sign without anything biological changing at all. This is exactly the kind of relationship an external validation would expose, and exactly why its absence matters more than the paper's limitations section implies.

### What a screening tool is for names the number that must be printed

Here is the paper's own framing of the problem, from the introduction: "approximately 70%–80% of submitted urine specimens from suspected patients turn out to be culture-negative, placing an unnecessary burden on clinical laboratories and highlighting the need for rapid screening methods."

The job is to **avoid cultures that will come back empty.**

Now ask which statistic measures success at that job. It is not sensitivity. Sensitivity asks: of the children who would culture positive, how many does the model catch? That matters for not missing infections — a real concern, but a different one. The job as stated is to safely *skip* cultures, and that is governed by **specificity** (of the children who would culture negative, how many can the model confidently identify?) and by **negative predictive value** (of the children the model calls negative, how many really are?).

Sensitivity is reported as 0.770, to three decimals, with a bootstrap confidence interval, in the abstract and twice in the text. Specificity is listed in the methods among the metrics computed, drawn as an unlabelled bar in Figure 4D, and given as a number **nowhere.** Negative predictive value is not computed at all.

So the reader cannot answer the question the paper set out to answer. If the model identifies 60% of the true negatives, it could retire a meaningful fraction of the lab's workload. If it identifies 70% of the positives and 60% of the negatives — plausible, given an AUC of 0.814 — then at this hospital's 42% prevalence, of 100 children sent through it you would skip roughly 40 cultures and miss roughly 13 infections in the process. Whether that trade is acceptable is a clinical judgement, and nobody can make it from what is printed.

**The technique: read the stated purpose, work out which metric governs it, then check whether that metric is in the paper as a number.** Papers report the metric their model scored best on far more often than the metric their use case requires. When the two diverge, the divergence is the finding. The companion habit: for any screening tool, **demand sensitivity and specificity at a single stated threshold, together**, plus the threshold itself. One without the other is half a result, and an AUC without either is a ranking exercise.

## 6. Jargon Translator

**Urine culture** — smearing urine on a nutrient plate and waiting a day or two to see whether bacteria grow, and which ones. The reference standard for diagnosing a urinary infection, and slow.

**CFU/mL (colony-forming units per millilitre)** — how many live bacteria were in the urine, counted by how many visible colonies appeared on the plate. A threshold number of these is what makes a culture "positive."

**Nitrite (NIT)** — a dipstick square. Many urinary bacteria convert nitrate, normally present in urine, into nitrite. In this cohort it was positive in 30.2% of children with positive cultures and 10.1% of those without: **specificity about 90%, sensitivity about 30%.** A positive strongly suggests infection; a negative means almost nothing.

**Leukocyte esterase (LEU)** — another dipstick square, detecting an enzyme from white blood cells. Picks up inflammation rather than bacteria. Graded − to 4+. In this cohort 57.6% of culture-positives were 3+ or 4+, against 35.1% of negatives.

**uWBC / BACT** — the automated urine analyser's counts of white cells and bacterial particles per unit volume. Much faster than culture and much less specific; the machine counts particles that look right, it does not grow anything.

**AUC / AUROC** — the probability that, shown one child who cultures positive and one who does not, the model gives the positive one the higher score. 0.5 is a coin flip, 1.0 is perfect. Says nothing about whether the scores are correct as percentages.

**PR-AUC** — the same idea read off a precision-recall curve instead. Unlike the AUC, its value depends on how common the outcome is, which makes it more informative when positives are rare — though at 42% prevalence here, they are not.

**Sensitivity / specificity** — of those who truly have the thing, how many you catch; of those who truly do not, how many you correctly clear.

**Brier score** — average squared error of the predicted probabilities. Combines calibration and discrimination; see Section 5.

**Calibration** — whether a predicted 30% actually happens 30% of the time. Entirely separate from whether the ranking is right.

**LASSO** — a regression that shrinks weak predictors' coefficients all the way to zero, so it selects variables and fits at the same time.

**Recursive feature elimination (RFE)** — fit a model, throw out the least useful variable, refit, repeat. A ranking procedure.

**Random forest** — hundreds or thousands of decision trees, each grown on a different random slice of the data and the variables, with their votes averaged. Here: 1000 trees, each at most 4 questions deep.

**class_weight = "balanced"** — an instruction to count the rarer outcome more heavily during fitting, so the model does not simply predict the common answer. Helps the ranking; wrecks the probabilities. See Section 5.

**SHAP value** — for one patient and one variable, how much that variable moved the model's output away from its average. The average it moves away from is the *base value*.

**Base value, E[f(X)]** — the model's mean output across the data. Should equal the outcome rate. Here it is 0.499 against a true rate of 0.421.

**Decision curve analysis (DCA)** — plots the net benefit of using the model against two do-nothing strategies ("treat everyone," "treat nobody") across a range of thresholds. Useful, and reported here.

**Bootstrap** — re-sample your data with replacement a few hundred times, recompute the statistic each time, and read the confidence interval off the spread. Used here with 500 replicates; I checked it against the exact binomial answer and it holds.

**Hanley–McNeil** — a 1982 formula for the standard error of an AUC given the number of positives and negatives. The tool used in Section 5 to work out which sample each number came from.

**Events per predictor (EPV)** — the number of outcome events divided by the number of variables in the model. A rough guide to whether the model has enough signal to fit. Here 171/7 = 24.4, which is fine.

**Vesicoureteral reflux (VUR)** — urine flowing backwards from bladder toward kidney, a common structural reason children get repeated urinary infections.

**Pyelonephritis** — infection that has reached the kidney itself, rather than staying in the bladder. More serious, and the kind most likely to be culture-negative after antibiotics.

## 7. What You Can (and Can't) Say

**Fair to say:**

- ✅ "In 581 children with suspected urinary infection at one Chinese children's hospital, 42% had a positive urine culture." Directly reported, arithmetic verified.
- ✅ "A random forest using seven same-day lab values scored an AUC of 0.814 on a held-out quarter of that hospital's own patients." Exactly what was measured.
- ✅ "It was never tested at another hospital, or on a later time period." The authors say so.
- ✅ "It caught about 77% of the children whose cultures came back positive." 57 of 74, confidence interval 0.66 to 0.87.
- ✅ "A urine dipstick nitrite test, on its own, missed about 70% of the positive cultures in this cohort." 74 of 245 were nitrite-positive.
- ✅ "At this hospital, *E. coli* caused about 73% of the Gram-negative infections, and the common older cephalosporins were resisted at rates between 22% and 65%." Reported, and this is the most immediately usable part of the paper.
- ✅ "Amikacin, piperacillin/tazobactam, cefoperazone/sulbactam and meropenem all held resistance below 10% here, and both *Enterococcus* species were fully susceptible to vancomycin and linezolid." Reported.
- ✅ "The children whose cultures were positive had, on average, *less* fever and *lower* CRP than those whose cultures were negative." Verified from Table 1, and the paper explains why.

**Not fair to say:**

- ❌ "Machine learning beat the single best lab test." The 0.814 was measured on 175 unseen children; the 0.730 baseline was measured on all 581, in-sample. The confidence-interval widths give it away. The comparison has not been made.
- ❌ "The model is 81% accurate." An AUC is not an accuracy. Accuracy is in Figure 4D as a bar and is not printed as a number anywhere.
- ❌ "The calculator tells you a child's risk of a positive culture." It returns a number anchored at a 50% background rate because of balanced class weighting — the paper's own SHAP base value of 0.499 against a true 42.1% is the evidence. It has not been calibrated, and no threshold is stated.
- ❌ "This safely reduces unnecessary urine cultures." That claim needs specificity or negative predictive value, and neither appears as a number in the paper.
- ❌ "A Brier score of 0.188 shows the model is well calibrated." A Brier score mixes calibration with discrimination. Against the no-skill value of 0.244 set by this cohort's prevalence, it represents a 23% improvement of unknown composition.
- ❌ "High CRP suggests a urinary infection in children." In this cohort it ran the other way, because the comparison group was full of feverish children with infections elsewhere. That is a fact about who got cultured here, not about urinary infections.
- ❌ "The model works across childhood, ages 0 to 17." 82% of the cohort was under three and 61% under one. Age was removed from the model during selection. The paper flags this itself.
- ❌ "The model predicts urinary tract infection." It predicts *culture positivity*. The paper notes that up to 31% of febrile pyelonephritis is culture-negative, and that those children are scored as the model's errors.
- ❌ "The resistance percentages apply to your hospital." They are from one children's hospital in Fuzhou, 2023–2025. Resistance is intensely local and changes year to year.
- ❌ "Random forest generalises better than XGBoost." The forest's smaller train-to-validation gap comes from being capped at depth 4. The gap measures how much a model memorised, not how useful it is.

## 8. Bottom Line for Your Life

If you are a parent: the genuinely useful fact in this paper is not the model. It is that **a urine dipstick's nitrite square missed about seven out of every ten real infections** in these children. If a child has been tested, told the dipstick was negative, and sent home still unwell, that negative is much weaker evidence than it sounds. The culture is the test that answers the question, and it takes a day or two. That is worth knowing before you accept a reassurance.

The second useful fact is more uncomfortable and the paper states it clearly: **up to a third of feverish infants with a kidney infection have a negative urine culture** — because antibiotics were started first, or the sample was imperfect, or the organism will not grow on a standard plate. A negative culture is not proof of no infection. This is why doctors sometimes keep treating a child whose culture came back clean, and it is not them ignoring the result.

For anyone appraising research, this paper hands you one technique that will pay for itself immediately and one trap that is becoming the most common failure mode in clinical machine learning.

**The technique: compare the widths of confidence intervals before you let a paper compare the numbers they sit next to.** Here, a 0.0385 half-width beside a 0.0665 half-width is the only visible sign that the baseline and the model were scored on different groups of children — one in-sample on everybody, one out-of-sample on a quarter. The text never mentions it. A ten-second check on the brackets catches it, and the same check works on any statistic that ships with an interval.

**The trap: a model that ranks well can still print numbers that mean nothing.** This one was fitted with balanced class weights, which pull its average output to 50% when the real rate is 42%. The paper prints that base value — 0.499 — in a figure legend, without noticing what it says. Then the model was published as a public calculator that shows doctors a percentage. **Discrimination and calibration are separate properties, and only one of them was measured here.** Before you trust any number a clinical calculator shows you, ask two questions: what is the background rate it was trained on, and has anyone checked that a predicted 30% happens 30% of the time? If the answer to the second is a Brier score, that is not an answer.

And the thing that would have cost these authors nothing: **they had three calendar years of data and split it at random.** Training on 2023–2024 and testing on 2025 was available for free and would have produced a real test of whether the model survives contact with a different year. When a retrospective study spans time and chooses a random split anyway, that is a decision, and it is worth asking why.

---

*This is an educational analysis of a published scientific paper, not medical advice. Nothing here is guidance about urinary tract infections, fever in children, or antibiotic choice. If your child has a fever or you are worried about an infection, speak to a doctor.*
