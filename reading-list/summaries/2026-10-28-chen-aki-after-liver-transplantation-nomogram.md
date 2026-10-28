# Machine learning-based nomogram for acute kidney injury after liver transplantation

**Authors:** Chen X, Luo W, Cheng M, Xu L (four authors, all Department of Hepatobiliary Surgery, The Second Affiliated Hospital of Chongqing Medical University, Chongqing, China)
**Journal:** Renal Failure, 2026; 48(1): 2698148 (published 27 September 2026)
**Decoded:** 2026-10-28
**Analysis basis:** **FULL TEXT** (retrieved from PubMed Central, PMC13618104; 54,873 characters). Table 1 (62 variables compared across both cohorts), Table 2 (the logistic model) and Table 3 (all 30 pairwise DeLong comparisons) were read in full as text. Figures 1–3 are described in the PMC rendering's alt-text; values quoted from them are only those the alt-text or the body text states numerically.

**Source links (verified):**
- DOI: https://doi.org/10.1080/0886022X.2026.2698148
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42802088/
- Full text (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC13618104/

**Basis of link verification.** Direct URL fetching is blocked from this session (`doi.org` does not resolve under the network policy here). Verification was done against the live PubMed/NLM record: a query for PMID 42802088 returned this exact title, these four authors, Renal Failure volume 48 issue 1 article 2698148, DOI `10.1080/0886022X.2026.2698148` and PMC ID `PMC13618104`; the full text was then retrieved from PubMed Central by that PMC ID and matches. Both halves of the chain were confirmed independently. According to PubMed, publication date 27 September 2026.

**Funding: not reported in the text retrieved.** **Competing interests: not reported in the text retrieved.** **Reporting guideline: TRIPOD and TRIPOD+AI are explicitly named and cited as the framework for model development and reporting** — the first paper in this reading list to name TRIPOD+AI without also needing to be told.

**Ethics:** approved by the Ethics Committee of the Second Affiliated Hospital of Chongqing Medical University, Scientific Ethics Pre-Review No. [2025] 361. The paper states that organs came from controlled brain-dead donors allocated through the China Organ Transplant Response System and that **no organs from executed prisoners were used** — a disclosure that belongs in every Chinese transplant paper and is frequently missing.

> **Why this paper today.** All four deferred papers were re-checked this morning and all four remain blocked. Google's personal health agent (Nature, PMID 42907512), the BMJ review of LLM-trial reporting (PMID 42869550) and the Annals of Internal Medicine Choosing Wisely benchmark (PMID 42896192) returned PubMed records with **no PMC identifier**, meaning no PubMed Central copy exists; a Scite full-text fallback was attempted and the server is still behind a paywall. JAMA OpenEvidence (PMID 42879271, PMC13673371) reached **day 13** of serving an empty PMC body. This paper was the last spare on the shelf, flagged a week ago for one specific reason: **n = 127**, the smallest cohort this list has decoded, and therefore the right place to teach events-per-variable properly. It turned out to teach something better. This is the most honestly reported study in the reading list, and it is still only worth 2 out of 5 — and the gap between those two facts is the most useful thing here.

---

## 1. The Gist

When someone receives a new liver, their kidneys often take the hit. Roughly four in ten transplant recipients develop acute kidney injury — a sudden drop in kidney function — in the days afterwards, and it is linked to worse recovery, longer-term kidney disease, and worse survival. Knowing early who is heading that way would let the team watch those patients harder, keep their blood pressure and fluid balance right, and avoid drugs that are hard on kidneys.

Four surgeons in Chongqing, China pulled the records of every adult who received a liver at their hospital between June 2023 and January 2026. After exclusions, **127 patients.** **61 of them — 48% — developed acute kidney injury.**

They measured 62 things about each patient: who they were, their blood tests before surgery, what happened during the operation, and their blood tests from the first urgent sample drawn afterwards, **usually within an hour of leaving theatre.** A statistical procedure narrowed those 62 down to four that mattered: kidney function on that first post-operative blood test, how long the operation spent in the "anhepatic phase" (the window with the old liver out and the new one not yet connected), a clotting marker called D-dimer, and a liver enzyme called ALT.

They built five different models from those four inputs and compared them.

Now, here is what makes this paper unusual, and it is not the result. **The authors spend most of the paper explaining why you should not take their result too seriously.** They report that their best-performing model won by a margin their own statistical test says is meaningless. They report that a different validation method reverses the ranking entirely. They point out, unprompted, that their strongest predictor is derived from the same blood measurement that defines the disease they are predicting. They state that they could not do external validation and explain exactly why. They publish the comparison that undercuts their own headline.

The model itself is weak evidence. 127 patients at one hospital, tested only on themselves, with a top predictor that partly overlaps the outcome. That is a 2 out of 5.

But you can *tell* that it is a 2 out of 5 — from the paper, without doing any detective work. That is rarer than a good result, and the difference between "honest" and "strong" is the lesson this reading list exists to teach.

## 2. Study Snapshot

**Study type:** a **single-centre retrospective cohort study** used to develop and internally validate a clinical prediction model. The design is prognostic in shape — predictors measured, then the outcome observed over the following week — but with a timing problem discussed below.

**Where and when:** The Second Affiliated Hospital of Chongqing Medical University, adults transplanted June 2023 to January 2026. The authors note their centre only recently started a liver transplant programme, which is why the numbers are small.

**Flow:** 146 recipients screened → 19 excluded (15 with pre-existing kidney impairment, 1 combined liver-kidney transplant, 3 with active post-operative bleeding) → **127 analysed.** Every number reconciles.

**Split:** randomly divided 3:1 into **94 training** (45 with kidney injury, 49 without) and **33 validation** (16 with, 17 without). Event rates 47.9% and 48.5%.

**Outcome:** acute kidney injury by the 2012 KDIGO definition — a creatinine rise of at least 26.5 µmol/L within 48 hours, **or** creatinine reaching 1.5 times baseline within 7 days, **or** urine output under 0.5 mL/kg/h for 6 straight hours. Baseline creatinine was the most recent stable value in the 24 hours before surgery.

**Candidate predictors: 62**, across four domains — 12 demographic and clinical, 20 pre-operative laboratory, 8 intra-operative, 22 early post-operative laboratory. Every one of them appears in Table 1 with a p-value, in both cohorts.

**Final predictors: 4**, chosen by LASSO regression fitted on the training cohort — post-operative eGFR, anhepatic phase time, post-operative ln(D-dimer), post-operative ALT. All three laboratory values come from **the first urgent blood test after surgery, generally within one hour.**

**The logistic model (Table 2), training cohort:**
- Post-operative eGFR: OR **0.9507** per 1 mL/min/1.73 m² (95% CI 0.9276–0.9745), p < 0.001
- Anhepatic phase time: OR **1.0372** per minute (95% CI 1.0027–1.0729), p = 0.034
- Post-operative ln(D-dimer): OR 1.4933 (95% CI 0.8878–2.5119), p = 0.131 — **not significant**
- Post-operative ALT: OR 1.0002 (95% CI 0.9996–1.0008), p = 0.425 — **not significant**

So two of the four predictors in the published nomogram have confidence intervals comfortably spanning 1.

**Group differences that drove selection:** anhepatic phase 70 min (IQR 58–84) with injury vs 59 min (48–69) without, p = 0.004. Post-operative eGFR 79.09 ± 25.48 vs 110.27 ± 22.70 mL/min, p < 0.001. ln(D-dimer) 8.05 vs 7.54, p = 0.024. ALT 834 U/L vs 682, p = 0.044. Nothing before surgery differed — not age, sex, BMI, diabetes, hypertension, Child-Pugh grade, MELD score, pre-operative creatinine or pre-operative eGFR.

**Five models compared:** logistic regression (converted into the nomogram), LightGBM, random forest, support vector machine, XGBoost.

**Validation-cohort AUCs:** SVM 0.846 (0.711–0.980), XGBoost 0.842 (0.700–0.984), random forest 0.816 (0.661–0.971), LightGBM 0.811 (0.652–0.970), logistic regression 0.761 (0.581–0.941).

**Five-fold cross-validation on all 127, the same five models:** random forest 0.807, XGBoost 0.792, LightGBM 0.788, **SVM 0.704**, logistic 0.703.

**External validation: none.** Stated plainly, four times, with the reason given.

## 3. How Strong Is This Evidence? (Grade 2/5)

**Read this section carefully, because the grade and the quality of the paper point in different directions.**

The grade in these summaries answers one question: *how much should a reader update their beliefs about the world?* It is not a mark for effort or for honesty. On that question this study scores low, and nothing the authors did wrong caused it:

**127 patients, one hospital, one recently-established programme.** The validation cohort is 33 people containing 16 events. An AUC measured on 33 people has a confidence interval roughly a quarter of the whole scale wide — SVM's runs from 0.711 to 0.980. You cannot learn much from an interval that includes both "modest" and "near-perfect."

**No external validation.** The authors explain precisely why — no data-sharing access to other centres, no public liver-transplant database holding the perioperative variables they need. The explanation is credible and it does not change what the absence costs. Every paper in this list that *has* had external validation found something the internal numbers hid.

**The strongest predictor shares a measurement with the outcome.** Post-operative eGFR is calculated from serum creatinine. Acute kidney injury is defined by a rise in serum creatinine within 48 hours. The post-operative blood test is drawn within one hour — **inside that 48-hour window.** The authors disclose the overlap and are careful about it. Section 5 explains why the disclosure, though honest, is slightly less complete than the problem.

**Two of the four published predictors are not statistically significant** in the multivariable model, with confidence intervals spanning 1. They stay in the nomogram because LASSO selected them.

**62 variables were screened on 94 patients with 45 events.** The paper's own events-per-variable figure of 11.25 counts the four survivors. Against the 62 that the outcome was consulted about, it is 0.73. Section 5 works this through.

**Now what the paper does right — and it is the longest such list in this reading list:**

**It names TRIPOD and TRIPOD+AI** as the framework for development and reporting, and cites them. First in this list to do so unprompted.

**It computes and publishes its own events-per-variable**, states the ≥10 rule, and says in the same paragraph that the small validation cohort still limits what the number is worth.

**It runs pairwise DeLong tests between all five models, corrects for multiple comparisons with Benjamini-Hochberg, and prints all 30 comparisons** — including the ones that destroy its headline. In the validation cohort **no comparison reaches significance; the smallest adjusted p-value is 0.609.**

**It runs bootstrap internal validation** and reports optimism-corrected AUCs alongside apparent ones, with the optimism quantified (0.025 to 0.059).

**It runs 5-fold cross-validation on the whole dataset** as a check on the single small split — and publishes the result even though it reverses the model ranking.

**It states three separate times that the SVM was chosen for the SHAP analysis only because its validation AUC was numerically highest, and that this choice should be treated cautiously** because DeLong showed no significance and the cross-validation disagreed.

**Its abstract leads with its own weakest number.** The title is "Machine learning-based nomogram"; the nomogram is the logistic model; the logistic model's validation AUC of **0.761 is the lowest of the five**, and the abstract reports it before mentioning the SVM's 0.846. Papers do not usually do this.

**It discloses the predictor-outcome overlap unprompted**, and tells the reader what the model therefore is not: "the model should not be interpreted as a preoperative prediction tool or as a model based entirely on predictors independent of the outcome definition."

**It names the variables it could not get** — donor characteristics, cold ischaemia time, intraoperative blood pressure trajectories, vasopressor dose, immunosuppression, nephrotoxic drug exposure, kidney injury biomarkers.

**It states that no organs from executed prisoners were used** and names the allocation system.

**So: 2 out of 5 for the strength of the evidence, and the best-reported 2 out of 5 in this list.** It is better reported than yesterday's paper, better reported than the two 3/5 papers decoded last week, and on transparency about its own limitations it is competitive with the 4/5 papers. The thing it lacks is not candour. It is patients.

**What would make it a 3:** external validation anywhere — a second Chinese centre, a public registry, even a temporal split across its own 32 months.

**What would make it a 4:** that, plus a version of the model restricted to variables measured *before* the outcome window opens, so that the eGFR overlap stops being a caveat.

## 4. The Editor's Concerns

**The timing problem is slightly worse than the paper's own description of it.** The authors write that post-operative eGFR "is closely linked to serum creatinine, which forms part of the AKI diagnostic framework" and acknowledge "the possibility of partial overlap." That frames it as two variables sharing an ingredient. The sharper statement is about *when*: the KDIGO criterion is a creatinine rise within **48 hours** after transplant, and the predictor is a creatinine drawn within **1 hour** after transplant. The predictor measurement falls inside the outcome's ascertainment window. For a patient whose creatinine has already climbed 26.5 µmol/L by that first draw, the measurement used to predict the outcome is a measurement that can *satisfy* the outcome. The paper never says how many patients that applied to, and the data to check it are not published.

**The model ranking depends entirely on which validation you look at.** Four estimates exist for each model, and they disagree:

- Training apparent: random forest 0.959 > LightGBM 0.886 > XGBoost 0.873 > logistic 0.861 > SVM 0.851
- Validation (n = 33): **SVM 0.846** > XGBoost 0.842 > RF 0.816 > LightGBM 0.811 > logistic 0.761
- Five-fold cross-validation (n = 127): RF 0.807 > XGBoost 0.792 > LightGBM 0.788 > **SVM 0.704** > logistic 0.703
- Apparent on the whole dataset: RF 0.941 > LightGBM 0.888 > XGBoost 0.881 > SVM 0.731 > logistic 0.729

The SVM is first on one list and fourth on another, and the drop from its validation figure to its cross-validation figure is **0.142 — the largest fall of any model.** The SHAP analysis, the paper's interpretability centrepiece, explains the SVM. The authors flag the fragility of that choice repeatedly, which is the right thing to do; it does not make the SHAP figure less dependent on it.

**"Significant" differences in apparent performance are not differences in skill.** The Benjamini-Hochberg-adjusted DeLong table reports, on the apparent whole-dataset numbers, random forest 0.941 vs XGBoost 0.881, ΔAUC 0.060, **adjusted p < 0.001**. Highly significant — and computed on data both models were fitted to. The random forest's apparent 0.941 against its own cross-validated 0.807 is a gap of **0.134**, larger than the maximum bootstrap optimism the paper itself estimated (0.059). A significant difference between two resubstitution AUCs tells you which model memorised harder.

**The same model, the same method, two in-sample estimates, 0.132 apart.** Logistic regression scores an apparent AUC of **0.861** when fitted and scored on 94 patients and **0.729** when fitted and scored on all 127. Nothing changed but which patients were in the fit. That spread — from a model with no tuning, no randomness, and no algorithmic choices — is the noise floor of this dataset, and it is larger than every between-model difference reported in the validation cohort.

**The nomogram contains two predictors the model says do nothing.** ln(D-dimer) (p = 0.131) and ALT (p = 0.425) are drawn on the published nomogram with their own point scales. A clinician using it will move a slider for ALT and watch the predicted risk change, when the paper's own regression says that movement is indistinguishable from noise. The SHAP analysis agrees: ALT's mean absolute SHAP value is 0.014, against 0.191 for eGFR — **fourteen times smaller.**

**62 variables, 45 events, no correction in Table 1.** Each of the 62 candidate variables is tested in both cohorts, giving about 124 p-values. At the conventional 5% threshold, roughly 3 of 62 would cross it by chance alone even if nothing were associated with anything. The authors applied Benjamini-Hochberg to the 30 DeLong comparisons — so they know the problem exists — and did not apply it to the screening table whose p-values informed which variables went into LASSO.

**ICU stay was measured and excluded from the predictors**, correctly, as a post-outcome consequence rather than a cause. Worth crediting: that is the kind of variable that quietly leaks into models.

**Where I am uncertain, stated plainly.** Calibration is described in words ("acceptable overall agreement in the training cohort but greater fluctuation in the validation cohort") and drawn in Figure 2, panels C, F and I. **No calibration intercept, slope, or Brier score is printed anywhere**, so I cannot say in which direction the predictions err or by how much. Figure 2's bootstrap panels (J, K, L) give optimism-corrected AUCs as a density plot and a bar chart; the body text gives only the range of the optimism (0.025 to 0.059), so I cannot quote a corrected AUC per model. No funding or competing-interests statement appears in the text retrieved.

## 5. Statistics Spotlight

Four things, and the first is a tool you can carry to any paper reporting an AUC.

### The AUC grid: with small samples, the score can only move in jumps

An AUC has a concrete meaning that is easy to lose sight of. Take every possible pairing of one patient who had the outcome with one patient who did not. For each pair, ask: did the model give the higher score to the one who had it? The AUC is the fraction of pairs it got the right way round.

That makes it a **counting statistic**, and counting statistics live on a grid.

The validation cohort here has **16 patients with kidney injury and 17 without.** So the number of pairs is:

> 16 × 17 = **272 pairs**

Which means the AUC can only take values that are multiples of **1/272 = 0.00368**. There is nothing between them. The score cannot be 0.8440 or 0.8450; it can be 229/272 = 0.8419, or 230/272 = 0.8456, and nothing in the gap.

Now look at the reported validation AUCs, converted into pairs:

- SVM 0.846 → **230** pairs out of 272
- XGBoost 0.842 → **229** pairs
- Random forest 0.816 → 222 pairs
- LightGBM 0.811 → 220.5 pairs (the half comes from a tie, which scores half credit)
- Logistic 0.761 → 207 pairs

Every single one lands on the grid. That confirms the arithmetic — and it tells you what the paper's model selection actually rested on:

> **The winning model beat the runner-up by one pair out of 272.**

One patient, somewhere in a cohort of 33, ranked one place differently. That is the entire basis on which the SVM was declared the numerically best model and chosen for the SHAP analysis. The paper's own DeLong test agrees: ΔAUC = 0.004, adjusted p = 0.926.

**The technique:** when you see an AUC comparison, find the number of positives and negatives, multiply them, and take the reciprocal. That is the smallest difference the data can even express. Then ask whether the reported difference is more than a couple of grid steps. At n₁ = 16 and n₂ = 17 the grid is coarse — 0.0037 per step — and a difference of 0.004 is one step. At n₁ = 500 and n₂ = 500 the grid is 0.000004 per step and this check never fires. **It is a small-sample tool, and small samples are exactly where model-ranking claims get made.**

### Count the variables you looked at, not the ones that survived

The paper reports its events-per-variable figure honestly:

> "In the training cohort, 45 AKI events were available, corresponding to an events-per-variable value of 11.25."

45 events ÷ 4 predictors = 11.25. Above the conventional floor of 10. Correct arithmetic, and the authors deserve credit for computing it at all — most papers in this list did not.

But the denominator is the wrong one, and this is a mistake almost everybody makes.

The rule of thumb exists because a regression fitted with too few events per predictor will fit noise. The amount of noise-fitting depends on **how many chances the procedure had to find a spurious pattern** — which is the number of variables the outcome was consulted about, not the number that came out the other end. Here, 62 variables went into Table 1, each tested against the outcome in both cohorts. LASSO then searched among them, also using the outcome. By the time four emerged, the outcome had been looked at 62 times.

> 45 events ÷ **62 candidates** = **0.73 events per variable**

To support 62 candidates at an events-per-variable of 10 you would need about 620 events — roughly 1,290 transplant recipients at this AKI rate, against the 127 available.

**The everyday version:** suppose you want to know whether a coin is biased. Flip it 20 times, see 14 heads, and that is weak evidence. Now suppose you had 62 coins, flipped each 20 times, picked the one with the most heads, and reported *that* coin's result. The number 14 has not changed. What it means has changed completely, and nothing in the final report tells you which situation you are in unless somebody says how many coins there were.

**The watch-out:** papers report events-per-variable against the final model because that is what the model contains. It is not a dishonest number; it is an incomplete one. **Find the sentence that says how many candidate variables were screened, and divide by that instead.** If the paper does not say, count the rows of Table 1.

### Four estimates of the same thing, and the spread between them is the answer

This paper gives five models and four performance estimates apiece. Most papers give one. The spread is more informative than any single number in it.

Watch what happens to plain logistic regression — a model with no tuning, no randomness, no architecture choices, nothing that could vary:

- Fitted on 94 patients, scored on those same 94: **AUC 0.861**
- Fitted on all 127, scored on those same 127: **AUC 0.729**

Both are apparent, in-sample estimates of the same method. The only difference is which patients were in the pot. **The gap is 0.132.**

That number is the dataset's noise amplitude — how much the answer moves when nothing meaningful changes. And now compare it with every difference the paper found between models in the validation cohort:

> SVM vs XGBoost 0.004. RF vs SVM 0.029. LightGBM vs RF 0.006. Logistic vs SVM 0.085.

Every one is smaller than the noise floor. The largest, 0.085, is less than two-thirds of it.

**The theory:** every performance number is a sample from a distribution. With 127 patients that distribution is wide, and you cannot see its width from a single estimate. When a paper gives you several estimates produced under conditions that *should not* matter — a different split, a different resampling scheme, a different subset — **the spread across them is a free measurement of how much any one of them can be trusted.**

**The watch-out:** readers treat a second validation method as confirmation when it agrees and as a puzzle when it disagrees. It is neither. It is a measurement of variability, and disagreement is the informative case. Here the cross-validation moved the SVM by 0.142 and the random forest by 0.009, which says the SVM's validation figure was the fluke, not the random forest's.

### Reading a Benjamini-Hochberg table without being fooled by it

The authors ran DeLong tests on all pairs of models in each dataset and adjusted the p-values with the Benjamini-Hochberg procedure. This is good practice and almost nobody does it. But the adjusted numbers need reading correctly.

Here is the validation-cohort column, all ten comparisons:

> 0.609, 0.609, 0.609, 0.609, 0.609, 0.609, 0.609, 0.609, 0.926, 0.926

**Ten comparisons, two distinct values.** That is not ten separate measurements of uncertainty that happened to coincide. It is the procedure's machinery showing through.

Benjamini-Hochberg works by sorting the raw p-values smallest to largest, scaling each by the number of tests divided by its rank, and then — the step that causes this — **enforcing that the adjusted values never decrease as you walk down the list.** Where the raw values are close together and none is small, that enforcement flattens a whole run of them onto the same ceiling. Eight genuinely different raw p-values collapse to one printed number.

**What to take from it:** the correct reading of that column is *"nothing here is significant, and the procedure stopped distinguishing between the comparisons."* The incorrect reading is that eight comparisons are equally uncertain and two are more so. Identical repeated BH values are a signature of the method, not a finding.

**The wider watch-out:** Benjamini-Hochberg controls the **false discovery rate** — the expected fraction of your *declared* discoveries that are wrong. It does not control the chance of any single error, and it does nothing at all when you declare no discoveries, as here. The authors used it in exactly the right place and reported the uncomfortable answer. The place they did not use it was Table 1, where 62 variables × 2 cohorts generate about 124 uncorrected p-values and roughly three would cross 0.05 by chance with nothing going on.

## 6. Jargon Translator

**Acute kidney injury (AKI)** — a sudden fall in kidney function over hours to days. Not the same as chronic kidney disease, though it raises the risk of it.

**KDIGO criteria** — the international standard definition of AKI: creatinine up by ≥26.5 µmol/L within 48 hours, or creatinine at ≥1.5× baseline within 7 days, or urine output under 0.5 mL/kg/h for 6 hours. Meeting any one is enough.

**Serum creatinine** — a waste product the kidneys clear. When they slow down, it builds up. The standard bedside measure of kidney function, and the quantity underneath both the outcome definition and the top predictor here.

**eGFR (estimated glomerular filtration rate)** — how fast the kidneys are filtering, estimated from creatinine using a formula (here the CKD-EPI equation). Higher is better. Since it is computed *from* creatinine, it carries the same information in a more clinically readable form.

**Anhepatic phase** — the stretch of a liver transplant when the old liver is out and the new one is not yet connected to the blood supply. Major vessels are clamped; blood pressure and kidney perfusion are under stress. Longer is worse. Median 70 minutes in patients who developed AKI, 59 in those who did not.

**D-dimer** — a fragment released when blood clots are broken down. Rises with clotting activation and inflammation. Used here as ln(D-dimer), the natural logarithm, which compresses a very skewed measurement into a workable scale.

**ALT (alanine aminotransferase)** — a liver enzyme. Spikes when liver cells are damaged, as happens when a transplanted liver gets its blood supply back.

**MELD score** — a standard severity score for end-stage liver disease, used for transplant prioritisation. It did not differ between groups here.

**Child-Pugh grade** — another liver disease severity classification, A through C. Also did not differ.

**LASSO regression** — a fitting method that shrinks weak predictors' coefficients to exactly zero, so it selects and fits in one step. Used here to go from 62 candidates to 4.

**Nomogram** — a printed chart that turns a regression model into something you can read by hand: mark each predictor on its scale, read off points, total them, read off a risk. A logistic regression wearing a paper interface.

**Odds ratio (OR)** — how much the odds of the outcome multiply per one-unit increase in a predictor. Above 1 means more risk, below 1 means less. An OR whose confidence interval includes 1 is not distinguishable from no effect.

**AUC / AUROC** — the share of positive-negative patient pairs the model ranks the right way round. See Section 5 for why that definition matters.

**DeLong test** — a statistical test for whether two AUCs computed on the *same patients* differ. The correct test for comparing models, and this paper runs all 30 of them.

**Benjamini-Hochberg correction** — an adjustment for running many tests at once, controlling the share of your declared findings that are false. See Section 5.

**Bootstrap internal validation** — resample your patients with replacement hundreds of times, refit, and measure how much better the model looks on data it saw than on data it did not. The difference is the **optimism**, and subtracting it gives a corrected estimate.

**Five-fold cross-validation** — split the data into five parts; train on four, test on the fifth; rotate. Every patient gets tested on exactly once by a model that never saw them.

**Apparent performance** — performance measured on the same data the model was fitted to. Always flattering. Also called resubstitution performance.

**SHAP value** — for one patient and one variable, how much that variable pushed the model's output away from its average. Mean absolute SHAP ranks overall influence.

**Support vector machine (SVM)** — a classifier that finds the boundary best separating two groups, allowing curved boundaries via a kernel.

**Decision curve analysis (DCA)** — plots the net clinical benefit of using a model against "treat everyone" and "treat nobody," across a range of risk thresholds.

**Events per variable (EPV)** — outcome events divided by predictors. A rough adequacy check. See Section 5 for which denominator to use.

## 7. What You Can (and Can't) Say

**Fair to say:**

- ✅ "Among 127 adults receiving a liver transplant at one Chinese hospital, 48% developed acute kidney injury within a week." 61 of 127, and consistent with the ~41% from the meta-analysis the paper cites.
- ✅ "A longer anhepatic phase was associated with more kidney injury." 70 vs 59 minutes, p = 0.004, and it stayed significant in the multivariable model (OR 1.0372 per minute, CI 1.0027–1.0729).
- ✅ "Nothing measured before surgery distinguished the two groups." Not age, sex, BMI, diabetes, hypertension, Child-Pugh grade, MELD score, pre-operative creatinine or pre-operative eGFR.
- ✅ "Kidney function on the first blood test after surgery was by far the strongest signal." SHAP 0.191, more than double the next variable, and the only predictor with p < 0.001.
- ✅ "None of the five models was statistically better than any other in validation." The paper's own DeLong tests with Benjamini-Hochberg correction; smallest adjusted p = 0.609.
- ✅ "The authors say external validation is required before clinical use." They say it four times.

**Not fair to say:**

- ❌ "A support vector machine was the best model for predicting AKI after liver transplant." It led by **one correctly-ranked pair out of 272**, its advantage was not significant on the paper's own test, and five-fold cross-validation put it fourth of five with a score 0.142 lower.
- ❌ "Machine learning outperformed logistic regression here." In validation the gap was 0.085 with overlapping intervals and an adjusted p of 0.609. In cross-validation the SVM and logistic regression finished 0.704 and 0.703 — a single thousandth apart.
- ❌ "The model predicts kidney injury before it happens." The dominant predictor is a creatinine-derived value measured within one hour of surgery, and the outcome definition counts a creatinine rise within 48 hours. The measurement windows overlap, and the authors say the model is not a preoperative prediction tool.
- ❌ "D-dimer and ALT are risk factors for AKI after transplant." Both appear in the nomogram; neither is significant in the multivariable model (p = 0.131 and p = 0.425), and ALT's SHAP contribution is fourteen times smaller than eGFR's.
- ❌ "Random forest was significantly better than XGBoost." That comparison (p < 0.001) was run on **apparent, in-sample** AUCs. The random forest's apparent 0.941 falls to 0.807 under cross-validation.
- ❌ "The model has an AUC of about 0.85." Pick a model and a validation scheme and you can get 0.959, 0.846, 0.807, 0.761, 0.729 or 0.703 — all from this paper, all for models built on the same four variables.
- ❌ "Events per variable was adequate at 11.25." That counts four surviving predictors. Sixty-two were screened; against those, it is 0.73.
- ❌ "This applies to transplant recipients generally." Patients with pre-existing kidney impairment or hepatorenal syndrome were deliberately excluded — 15 of 19 exclusions — which is a defensible design choice the authors explain, and which removes exactly the group at highest baseline risk.

## 8. Bottom Line for Your Life

If someone close to you is facing a liver transplant, the useful fact here is the denominator, not the model: **roughly four to five in every ten recipients develop some degree of acute kidney injury in the first week.** It is common, it is largely expected, and it is one of the main things the intensive care team is watching for. This paper's most clinically interesting finding is also its simplest — **nothing measurable before the operation predicted it.** Not age, not diabetes, not MELD score, not baseline kidney function. What predicted it was how the operation went: specifically, how long the surgery spent in the anhepatic phase, with the old liver out and the new one not yet plumbed in. That points at surgical and anaesthetic technique rather than patient selection, which is a more hopeful place for a risk factor to live.

For anyone appraising research, this paper is worth keeping for a reason that has nothing to do with livers.

**It separates two things that usually get confused: how strong a study is, and how honestly it is reported.** This one is weak and honest. The evidence is 127 patients at one hospital with no external test and a predictor whose measurement window overlaps the outcome — a 2 out of 5, and it would be a 2 out of 5 no matter how it was written up. But the authors told you all of that themselves. They published the test that killed their own headline, ran a second validation that reversed their ranking and printed it, flagged the overlap between their best predictor and their outcome before anyone asked, computed their own events-per-variable, named TRIPOD+AI, and led their abstract with the worst of their five numbers.

The opposite combination — strong-looking and badly reported — is far more common and far more dangerous. A paper with 10,000 patients that hides its calibration, picks its baseline comparison from a different sample, and reports only the metric it won on will *look* like better evidence and leave you less able to judge it. **Honesty is not strength, but it is the thing that lets you measure strength.** When you cannot tell what a study is worth, assume it is worth less than it claims.

And the portable tool from today: **when a paper ranks models on a small test set, multiply the positives by the negatives.** 16 × 17 = 272. One in 272 is 0.0037, and that is the smallest difference the data can express. A winner that led by 0.004 led by one patient. Check the grid before you believe the ranking.

---

*This is an educational analysis of a published scientific paper, not medical advice. Nothing here is guidance about liver transplantation, kidney function, or your own care. If you or someone you know is facing a transplant, speak to the transplant team.*
