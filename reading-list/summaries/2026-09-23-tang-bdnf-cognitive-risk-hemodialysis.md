# Serum BDNF and cognitive risk in maintenance hemodialysis: a machine learning study

- **Authors:** Qiong Tang, Jiakun Tian, Xinyu Ying, Yanyun Zhang, Yanqiao Huo, Daiyao Liu, Yongping Zhang (The First People's Hospital of Lianyungang, Jiangsu, China; with one author at Lianyungang Center for Disease Control and Prevention) — 7 authors
- **Venue:** Renal Failure, 2026;48(1):2732422 (published September 20, 2026)
- **DOI link:** https://doi.org/10.1080/0886022X.2026.2732422
- **PubMed link:** https://pubmed.ncbi.nlm.nih.gov/42764337/ (PMID 42764337)
- **Full-text link used:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC13592005/ (PubMed Central, open access)
- **Basis:** FULL TEXT — introduction, complete Methods, all results including both performance tables with confidence intervals, the nested cross-validation figures, discussion, and the full limitations section were read from the open-access PubMed Central copy. Figures and supplementary material were not retrieved, so anything living only there is described as reported rather than quoted. Reporting followed the TRIPOD+AI recommendations, with risk of bias considered under PROBAST+AI. Software versions are named in the paper; analytic code is stated to be available from the corresponding author on request. Ethics approval and funding and competing-interest statements were not present in the retrieved text. Identifiers verified against the live PubMed/NLM record; direct URL browsing is blocked in this environment, so links are constructed from that verified record.
- **Decoded:** 2026-09-23
- **Note on selection:** the queue holds only entries whose full text cannot be reached here, so today's run scanned the past week. Details at the end.

---

# The Gist

People on long-term dialysis often develop thinking problems, and there is no good way to tell in advance who will. This team measured a brain protein called BDNF in the blood of 130 dialysis patients who had normal cognitive screening scores, then retested everyone a year later. Over half had slipped below the threshold. Patients who started with more of the protein were considerably less likely to be among them — a clear, statistically strong association. Then the researchers did something most papers avoid: they asked whether knowing the protein level actually improved their ability to *predict* who would slip, on top of what the chart already said. It barely did, and the improvement was not statistically significant. Both findings are in the same paper, reported with equal prominence. That gap — between a real association and a useful prediction — is the thing worth taking from this one, and it explains a great deal of disappointing medical research.

# Study Snapshot

- **Study type:** A single-centre prospective observational cohort with an internally validated prediction model. Prospective matters here: people were enrolled, measured, and then followed forward, rather than the researchers digging through old records.
- **Who:** 253 dialysis patients screened. 103 excluded because they already had low cognitive scores, 19 because they did not complete the baseline assessment. 131 entered follow-up, 1 died before reassessment, leaving **130 analysed**. Nobody was lost to follow-up.
- **The outcome:** a standard 30-point cognitive screening test at baseline and again one year later. Everyone started at 26 or above. The outcome was scoring below 26 at one year. **70 of 130 patients (53.8%) met it.**
- **The measurement:** a blood protein involved in the survival of nerve cells, measured once at baseline from a fasting sample taken before dialysis, in duplicate, using a standard laboratory kit. All samples were collected and assayed within one week under one protocol, and — a detail worth noticing — the laboratory staff could not have known who would develop the outcome, because the outcomes did not exist yet.
- **What went into the models:** 14 baseline variables. Age, sex, education, high blood pressure, diabetes, stroke history, haemoglobin, inflammation marker, albumin, a kidney function estimate, a parathyroid hormone measure, a cardiovascular burden stage, the baseline cognitive score, and the protein. Only baseline information was used, deliberately, so nothing from the future could leak in.
- **Who differed at baseline.** Patients who later declined were older (median 54 against 43 years) and had fewer years of education (9 against 11). Almost nothing else separated the groups: blood pressure, diabetes, haemoglobin, inflammation, albumin, kidney function, and parathyroid hormone all showed no significant difference. Stroke history was more common in the decline group but not significantly so.
- **The association, which is strong.** Each one standard deviation higher level of the protein was linked to **roughly half the odds** of developing the outcome, after adjusting for age, sex, education, diabetes, kidney function, and baseline score. The odds ratio was 0.52, with a confidence interval from 0.34 to 0.80.
- **Five different model types were compared,** using cross-validation repeated ten times: two tree-based methods, a support vector machine, a penalised regression, and ordinary logistic regression.
- **The results of that comparison:** random forest scored 0.798 and extreme gradient boosting 0.797, against 0.757 for penalised regression, 0.743 for the support vector machine, and **0.711 for plain logistic regression**.
- **Calibration was reported, not just ranking.** One model, the penalised regression, produced a calibration slope of **25.792** where 1.0 is ideal, because its predicted probabilities were squeezed into a narrow band. The authors flag this and warn against reading it at face value. That single number is the most instructive thing in the paper's tables.
- **The central test.** They built one model with the protein and one identical model without it, using the same data splits and the same settings, and compared them. Adding the protein moved the ranking score from 0.770 to 0.797, moved a second measure from 0.746 to 0.779, and improved a prediction-error score slightly. **The difference in ranking was not statistically significant, at p = 0.236.**
- **A more stringent check, rarely performed.** They re-ran everything with an extra layer of validation designed to strip out optimism from tuning the models. Every number got slightly worse: the best model fell from 0.797 to 0.782, and the model without the protein from 0.770 to 0.761.
- **Sensitivity analyses in several directions.** Removing the baseline cognitive score, excluding patients who started right at the threshold, and requiring a drop of at least 2 or at least 3 points all preserved the direction of the association.
- **The authors state their own key weakness in plain terms:** with 70 events and about 14 candidate predictors, the ratio of events to variables was about 5, against a conventional minimum of 10, and they write that "overfitting cannot be excluded."
- **Funding / conflicts:** not present in the retrieved text.

# How Strong Is This Evidence?

**Grade: 3/5 — a small single-centre study conducted and reported with more care than many far larger ones, whose main claim its own authors describe as small and statistically uncertain.**

Start with what is genuinely good, because there is a lot of it. This is prospective: people were enrolled, measured, and followed, so the protein was measured before anyone knew the answer. Follow-up was complete, with no losses. Predictors were chosen in advance and restricted to baseline information to prevent future data leaking backwards. Five different model families were compared rather than one favourite being presented. Calibration was reported alongside ranking, with both the intercept and the slope. Prediction error, precision-recall performance, decision curves, and per-patient explanations were all included. There were sensitivity analyses in four directions. The reporting followed the current standards for AI prediction models. Software versions are named to the decimal point.

And the central finding is a null that the authors could easily have buried. Their headline biomarker produced a strong association and then failed to meaningfully improve prediction, and both results sit in the abstract with equal weight. The conclusion says the biomarker warrants further evaluation "rather than routine clinical implementation at this stage."

What holds the grade at 3 is scale and scope. One hospital, 130 people, no external validation of any kind. The events-per-variable ratio of about 5 means the models had more freedom than the data could really discipline, and the authors say so. The outcome is a screening test, not a diagnosis, and the 53.8% one-year event rate is difficult to interpret as real cognitive decline. Those are limits of the study's size and design, not of its conduct.

# The Editor's Concerns

- **More than half the cohort "developed cognitive impairment" in one year, which is not plausible as clinical disease.** Everyone started at 26 or above on a 30-point screen, and 70 of 130 fell below 26 within twelve months. A screening threshold plus the ordinary wobble in retaking a test will generate a large share of that. The authors address it directly — excluding people who started right at 26 barely changed the rate, and requiring a drop of 2 or 3 points preserved the association — but the headline number still describes crossing a line on a screening test, not developing a diagnosed condition, and the paper says so repeatedly.
- **The machine learning advantage over logistic regression is suspiciously large.** Logistic regression scored 0.711 while the tree-based models scored 0.797 and 0.798, a gap of nearly 0.09. In well-powered studies, simple regression is usually competitive — the delirium review decoded three days ago found exactly that across 29 studies. In a 130-patient dataset with an events-per-variable ratio of 5, a large advantage for flexible models is more likely to reflect those models fitting noise than discovering real curvature. The nested validation shrank the gap but did not eliminate it.
- **About 5 events per variable, stated by the authors.** The conventional floor is 10. Below it, coefficients become unstable and performance estimates optimistic. Giving that number in your own limitations section is admirable and does not fix it.
- **No external validation.** Everything is internal. Every performance figure comes from the same 130 people, resampled.
- **The protein was measured once.** A single blood draw captures a moment. The authors note that peripheral levels vary biologically and that one measurement cannot describe change over time.
- **Dialysis-specific factors are missing.** How long someone has been on dialysis, how adequate their sessions are, the access type, weight gain between sessions, and blood pressure drops during treatment were not fully captured — and several of those are plausible drivers of both brain injury and frailty.
- **The one clinical variable that reached significance did so marginally.** The cardiovascular burden stage differed between groups at p = 0.048, and the authors are careful that this comparison was unadjusted and not intended to estimate an independent effect. Removing it changed the model's score by 0.005.
- **Code is "available on request."** The software versions are admirably specific, and a repository would let someone actually check.
- **Ethics approval details were not in the retrieved text.** For a prospective study drawing blood and administering cognitive tests, the approving body and protocol number would normally be stated; the retrieved text does not contain them.
- **What this study did well:** ran prospectively with complete follow-up; measured the biomarker before any outcome existed, so the laboratory could not be influenced; pre-specified the predictor set and restricted it to baseline values to prevent leakage; compared five model families rather than showcasing one; reported calibration intercept and slope, prediction error, precision-recall performance, and decision curves rather than stopping at a ranking score; flagged one model's absurd calibration slope instead of quietly reporting it; ran a stricter nested validation and published the resulting worse numbers; tested the outcome definition four different ways; named software versions; followed current AI prediction-model reporting standards; disclosed its own events-per-variable problem; and concluded against clinical use.

# Statistics Spotlight

**1. Association versus prediction — why a strong link can be a useless test.**
- *What they are:* An **association** answers a question about groups: on average, do people with more of this have less of that? A **prediction** answers a question about an individual: can I tell, in advance, which specific person this will happen to? These feel like the same question. They are not, and confusing them is probably the single most common error in how medical findings get reported.
- *How this paper used it:* Both, side by side. The association was strong: each standard deviation higher protein level was linked to about half the odds of the outcome, odds ratio 0.52 with a confidence interval of 0.34 to 0.80, comfortably significant. The prediction test was the honest follow-up: build the model without the protein, build it with, compare. The ranking score went from 0.770 to 0.797, and the formal test of that difference gave **p = 0.236** — no significant improvement.
- *The theory, with a worked example:* Imagine two overlapping bell curves, one for people who will decline and one for people who will not. An association says the curves' centres are meaningfully apart. Prediction depends on something different: how much the curves *overlap*. Two groups can have clearly different averages and still overlap across most of their range, and it is the overlap that decides whether you can classify an individual. Height differs strongly and significantly between men and women, and you still cannot reliably determine someone's sex from height alone, because plenty of women are taller than plenty of men. That is exactly the shape of this result. The protein genuinely differs between the groups. It does not separate them.
- *Watch out:* This is the trap behind an enormous amount of biomarker research and almost every "scientists discover marker linked to X" headline. A significant odds ratio tells you a difference exists. It tells you nothing about whether a test based on it would work. **The question that separates them is: does adding this to what we already know improve the prediction, and by how much?** Most papers never ask. This one asked, got an inconvenient answer, and printed it.

**2. Nested cross-validation — the optimism hiding inside ordinary validation.**
- *What it is:* Cross-validation splits your data into folds, trains on most, tests on the rest, and rotates. Standard practice. The hidden problem is that modern models have settings that must be tuned, and if you tune them using the same folds you then report performance on, you have quietly let the test data influence the model. Nested cross-validation fixes this by putting a second loop *inside* each training fold to do the tuning, so the outer test data stays genuinely untouched.
- *How this paper used it:* As a sensitivity analysis, which is unusual and to their credit. The ordinary version gave the best model a score of 0.797. The nested version gave 0.782. The model without the protein went from 0.770 to 0.761. Every number got slightly worse.
- *The theory, with an analogy:* Picture a student sitting practice exams to decide which revision method works best, then sitting the real exam — and the real exam turns out to contain some of the practice questions. Their score is inflated, not by cheating, but by the practice and the test overlapping. Nested validation is the examiner insisting the practice questions come from a sealed set that never appears on the paper. The size of the inflation here, about 0.015, is small. It is small because the authors also averaged over ten repeats, which stabilises things. In studies that tune aggressively on small data, the gap can be far larger.
- *Watch out:* Almost no clinical prediction paper does this, so when you read "we used cross-validation," assume the reported figure carries some unmeasured optimism. The practical version of the question: **were the model's settings chosen using the same data the performance was measured on?** If a paper does not say, it probably was. And note the deeper point, which the authors make themselves: nested validation reduces optimism from tuning. It does nothing about the optimism that comes from being tested only on the hospital that produced the data.

**3. Calibration slope — and the model that scored 25.792.**
- *What it is:* Ranking and honesty are different skills. A model can order patients correctly and still produce probability numbers that mean nothing. The calibration slope measures whether a model's predicted risks are appropriately spread out. **1.0 is ideal.** Below 1.0 means the predictions are too extreme — the model says 5% and 95% when it should say 25% and 70%. Above 1.0 means they are too timid, bunched near the average.
- *How this paper used it:* They reported it for all five models, which is rare. The best-behaved was the boosting model at 0.867, close to ideal. Random forest came in at 1.430, the support vector machine at 1.115, logistic regression at 0.512 — meaning its probabilities were roughly twice as spread out as they should be. And then **the penalised regression produced a calibration slope of 25.792**, which is not a near miss but a different order of thing entirely. The authors explain exactly why: that model's predicted probabilities were crammed into a narrow band around the overall event rate, so it barely varied its answer at all.
- *The theory, with a worked example:* Picture a weather forecaster who says "50% chance of rain" every single day, nudging to 49% or 51%. Over a year where it rains half the time, they are beautifully accurate on average, and completely useless for deciding whether to take an umbrella. If you rank days by their tiny nudges, they might even do respectably — and that is the crucial detail here. **That model scored 0.757 on ranking, better than the support vector machine and much better than logistic regression.** By the measure most papers report, it looked fine. Only the calibration slope revealed it was barely making predictions at all.
- *Watch out:* This is why "we report AUC" is not enough, and why the delirium review three days ago found calibration assessed in only about half of 29 studies. A ranking score cannot see this failure mode. If a model's output will ever be shown to a patient or used to pick a treatment threshold, the probabilities have to mean something, and only calibration tells you whether they do. Ask for the calibration slope. If a paper does not report one, it has not checked whether its numbers are honest — it has only checked whether they are in the right order.

# Jargon Translator

- **Maintenance hemodialysis:** ongoing dialysis treatment, usually three times a week, for people whose kidneys have failed.
- **BDNF (brain-derived neurotrophic factor):** a protein involved in the survival of nerve cells and the formation of connections between them.
- **MoCA (Montreal Cognitive Assessment):** a 30-point screening test of thinking and memory. Below 26 is the conventional cutoff for possible impairment. A screening test, not a diagnosis.
- **Incident:** newly developing. Everyone here started without the outcome.
- **Screening-defined outcome:** an outcome defined by crossing a threshold on a screening test rather than by clinical diagnosis. The paper is careful to use this phrasing throughout.
- **ELISA:** the standard laboratory method for measuring a specific protein in blood.
- **Odds ratio (OR):** how the odds of an outcome change per unit of a predictor. 0.52 means roughly half the odds.
- **Per 1 standard deviation:** the predictor is expressed in units of its own spread, so the number is comparable across differently scaled measurements.
- **Confidence interval:** the range of values consistent with the data. If it crosses 1.0 for an odds ratio, no effect cannot be ruled out.
- **AUC / AUROC:** a ranking score from 0.5 (coin flip) to 1.0 (perfect).
- **PR-AUC:** a companion measure that responds more strongly to how common the outcome is.
- **Brier score:** average prediction error. Lower is better.
- **Calibration intercept and slope:** whether predicted risks are right on average, and whether they are appropriately spread. Slope 1.0 is ideal.
- **Cross-validation:** repeatedly splitting data into training and testing portions to estimate performance without a separate test set.
- **Nested cross-validation:** a stricter version with an inner loop for tuning, so the outer test data stays untouched.
- **DeLong's test:** the standard statistical test for whether two ranking scores genuinely differ.
- **Events per variable (EPV):** the number of outcomes divided by the number of predictors. Ten is the conventional minimum. This study had about 5.
- **Overfitting:** a model learning the quirks of its training data rather than the real pattern.
- **SHAP values:** a technique for attributing each prediction to its individual inputs.
- **Decision curve analysis:** asking whether acting on a model's predictions produces net benefit.
- **TRIPOD+AI / PROBAST+AI:** current standards for reporting and appraising AI-based prediction models.
- **Elastic net:** a form of regression that penalises complexity. The model with the runaway calibration slope here.

# What You Can (and Can't) Say

**Fair to say:**
- "In a prospective study of 130 dialysis patients, each standard deviation higher baseline BDNF was associated with about half the odds of falling below the cognitive screening threshold within a year, with an odds ratio of 0.52."
- "Adding BDNF to a model built from routine clinical information raised the ranking score from 0.770 to 0.797, a difference that was not statistically significant at p = 0.236."
- "Tree-based models scored around 0.80, while logistic regression scored 0.711, in a dataset of 130 patients with roughly five events per predictor."
- "The authors conclude that BDNF warrants further evaluation as an adjunctive marker rather than routine clinical use, and that external validation is needed first."
- "The study reports its own events-per-variable ratio as about 5, against a conventional minimum of 10, and states that overfitting cannot be excluded."

**Not fair to say:**
- "A blood test predicts cognitive decline in dialysis patients" — the association is real and the prediction test came back not significant. Those are different claims and this paper made both.
- "Low BDNF causes cognitive decline" — this is an observational association in 130 people, with a single measurement and no mechanism tested.
- "Machine learning outperforms traditional statistics here" — the gap is large in a dataset far too small to support that conclusion confidently, and the paper's own stricter validation narrowed it.
- "More than half of dialysis patients develop cognitive impairment within a year" — 53.8% crossed a screening threshold. The authors state explicitly this is not the incidence of diagnosed impairment.
- "The model is ready to help identify at-risk patients" — there is no external validation, and the conclusion argues against clinical implementation at this stage.

# Bottom Line for Your Life

This is a small study about a niche question, and it is on the list for one reason: it does, cleanly and in public, the thing almost no paper does.

Somebody found a biomarker with a strong association. Odds ratio 0.52, confidence interval well clear of 1, p = 0.003. That result alone would have made a perfectly publishable paper and a confident press release. Instead they asked the follow-up question — does knowing this actually improve our ability to predict who declines, beyond what the chart already tells us — and the answer was barely, with p = 0.236. Both appear in the abstract.

Carry that pair of questions. When you meet any claim of the form "scientists find marker linked to disease," the association is usually the easy part. The question that decides whether it becomes a test you could ever be given is whether it adds anything to what a doctor already knows about you. Age and education did most of the work in this study. The new protein added a sliver.

The second thing to take is narrower and very practical. When a model produces probabilities, someone has to check that the probabilities mean something. One model in this paper ranked patients respectably and had a calibration slope of 25.792 — it was essentially predicting the average for everybody. A ranking score cannot detect that. If you are ever told a tool estimates your risk at some percentage, the question underneath is whether anyone has verified that its 30% happens 30% of the time.

Nothing here changes anyone's care. The authors are explicit that external validation is needed before this approach is considered for clinical use, and that their outcome was a screening threshold rather than a diagnosis. One study is one data point. This is an educational breakdown, not medical advice.

---

**Sources** (based on articles retrieved from PubMed and PubMed Central; identifiers verified against the live PubMed/NLM record — URL browsing is blocked in this environment, so links are constructed from that verified record):
- DOI: https://doi.org/10.1080/0886022X.2026.2732422
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42764337/ (PMID 42764337)
- Full text (PMC, open access): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC13592005/

**Why this paper.** The queue's remaining entries all lack reachable full text, including the two candidates added yesterday, which still have no PubMed Central copy. Scanning the past week produced a stronger thematic match that also could not be read and has now been queued:
- Vladika J, et al. "Improving Reliability and Explainability of Medical Question Answering Through Atomic Fact-Checking in Retrieval-Augmented Large Language Models." *Journal of Medical Internet Research* 2026;28:e92090 — https://doi.org/10.2196/92090 (PMID 42770666). Breaks model answers into individual factual claims and checks each against clinical guidelines, reporting up to 50% answer improvement and an 80% hallucination detection rate, with expert multireader assessment and real tumour board cases. It follows directly from the data-poisoning and trust entries already on this list.
