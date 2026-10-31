# An interpretable machine learning model integrating mucosal and cellular immunity to predict SARS-CoV-2 reinfection: a multicenter cohort study

**Authors:** Ran J, Zhang W, Zhang W, Huang H, Gong L, Yin S, Chen Y, Wang A, Min H, Zhu L, Chu J, Qin Y, Huang R, Wu C, Chen Y (fifteen authors — Departments of Infectious Disease and Laboratory Medicine and the Center of Medical Big Data, Nanjing Drum Tower Hospital, Nanjing University; Nanjing Normal University; Nanjing Medical University; Jiangsu University; School of Computer Science, Nanjing University of Posts and Telecommunications; Jiangsu Provincial Center for Disease Control and Prevention)
**Journal:** Emerging Microbes & Infections, 2026; 15(1): 2746253 (published 21 October 2026)
**Decoded:** 2026-10-31
**Analysis basis:** **FULL TEXT** (retrieved from PubMed Central, PMC13700530). The complete body was read — introduction, cohort and sampling methods, laboratory procedures, model training, statistical analysis, all results sections, discussion and limitations. **The supplementary material is not retrievable**, which matters here more than usual: Tables S1–S7 hold the per-cohort baseline tables, the Boruta stability counts, the full six-model metric table, the nested cross-validation results and the multivariable regression, and Figures S1–S3 hold the workflow, the joint feature-space scatter plots and the calibration curves. Everything quoted below comes from the main text. **The web calculator's URL was stripped by the text extraction and is therefore not reproduced here.**

**Source links (verified):**
- DOI: https://doi.org/10.1080/22221751.2026.2746253
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42908321/
- Full text (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC13700530/

**Basis of link verification.** Direct URL fetching is blocked from this session (`doi.org` does not resolve under the network policy here). Verification was done against the live PubMed/NLM record: a query for PMID 42908321 returned this exact title, these fifteen authors, Emerging Microbes & Infections volume 15 issue 1 article 2746253, DOI `10.1080/22221751.2026.2746253` and PMC ID `PMC13700530`; the full text was then retrieved from PubMed Central by that PMC ID and matches. Both halves of the chain were confirmed independently. According to PubMed, the record is typed "Journal Article; Multicenter Study; Validation Study."

**Funding: not reported in the text retrieved. Competing interests: no statement in the text retrieved. No reporting guideline (TRIPOD, TRIPOD+AI or otherwise) is named.**

**Ethics:** approved by the Ethics Committee of Nanjing Drum Tower Hospital. **All participants provided written informed consent prior to enrolment** — the first prospectively consented cohort in this reading list for some weeks.

> **Why this paper today.** All four deferred papers were re-checked and remain blocked; the JAMA OpenEvidence study (PMID 42879271, PMC13673371) reached **day 16** of serving an empty PMC body. This was spare #3 from the 10-28 restock, flagged for its genuine external validation across two prospective cohorts. It delivers that — and then something this list has never seen in sixty-three papers. **Every previous model lost ground when it met outside data. This one gained: internal AUC 0.835, external AUC 0.996.** That is higher than the model's performance on the data it was fitted to, and working out why is the most instructive thing available this week.

---

## 1. The Gist

COVID-19 has not gone away; it has settled into waves of reinfection. Who catches it again, and who does not, is not well understood. Blood antibodies clearly matter, but they fade, and new variants slip past them.

Fifteen researchers in Jiangsu province, China tested a different idea. Protection might depend less on antibodies circulating in the blood and more on two things measured elsewhere: **antibodies sitting in the lining of the nose** — where the virus actually lands — and a particular kind of long-lived immune memory cell. They recruited **1,186 adults** in two cities, Wuxi and Nantong, took a blood sample and a nasal swab from each at the start, and then followed them for about ten months to see who got sick again.

**128 of 1,156 people (11.1%) had a symptomatic reinfection.**

They measured 18 things about each person and let an algorithm decide which mattered. It threw out almost everything — age, sex, weight, smoking, drinking, diabetes, how many times they had been infected before, how many vaccine doses they had had, blood antibody levels, memory B cells, most T cell subsets. **Two survived:** nasal antibody (spike-specific sIgA) and one memory T cell subset (spike-specific CD4⁺ central memory T cells). The difference at baseline was stark — median nasal antibody of **4.99 in people who were later reinfected versus 66.16 in those who were not**, a thirteen-fold gap.

A two-variable model built on those markers scored **0.835** on held-back participants from Wuxi. Honest, useful, roughly what a good two-marker model looks like.

Then they tested it on the 586 people from Nantong and it scored **0.996** — essentially perfect. It caught **all 62** reinfections there, missing none.

**That is the number that will get cited, and it is the one to ignore.** A model cannot genuinely do better on strangers than on the people it learned from, and this one beat its own fitted performance (0.914) by eight points. The paper contains the explanation without connecting it: the two cohorts' marker values **differ significantly**, and in Nantong the two groups separate far more cleanly. A cohort where the sick and the well sit further apart is simply an easier sorting problem. Section 5 works through why that inflates the score without the model having improved at all.

The trustworthy figure is elsewhere in the paper, and the authors computed it properly: a cross-validated **0.834 ± 0.084**. That is a decent result for two biological markers, and it is the one worth remembering.

## 2. Study Snapshot

**Study type:** development and external validation of a clinical prediction model using **two prospective community-based cohorts**. Prospective matters: the markers were measured before anyone was reinfected, so the predictors genuinely precede the outcome. This is real prediction, not the same-day identification several papers in this list have offered.

**Where and when:** Wuxi and Nantong, Jiangsu province, China. Enrolment May 2024 to February 2025, median follow-up **10 months**.

**Flow:** **1,186 enrolled** → 30 lost to follow-up (2.5%: 14 uncontactable, 7 relocated, 4 died of unrelated conditions, 5 withdrew) → **1,156 analysed**. The paper compared the 30 lost against those retained and found no significant differences in baseline demographic, clinical or immunological characteristics. Every number reconciles.

**Outcome:** symptomatic SARS-CoV-2 reinfection — COVID-19 symptoms plus a positive antigen or nucleic-acid test after enrolment. Ascertainment was by **symptom-triggered self-testing**, with free test kits and monthly follow-up calls. **128 events (11.1%).**

**Cohort split:** Wuxi (n = 570) divided 7:3 stratified by outcome into a **training cohort of 400** and an **internal validation cohort of 170**. Nantong (n = 586) held as the **external validation cohort** — a genuinely separate site, not a random slice.

**Reconstructed event counts** (derived in Section 5 from the published metrics): the external cohort contained **62 reinfections** among 586 (10.58%), so Wuxi held the other **66** among 570 (11.58%). After the 7:3 split the training cohort had roughly **46 events** and the internal validation cohort about **20**.

**What was measured:** 18 candidate variables — age, sex, smoking, drinking, BMI, diabetes, number of prior infections, number of vaccine doses, plus ten antigen-specific immune measures (nasal spike-specific sIgA, serum spike-specific IgG, spike-specific memory B cells, spike-specific circulating T follicular helper cells, and six spike-specific CD4⁺ and CD8⁺ T cell memory subsets). The JN.1 spike protein was used as both stimulating and coating antigen, because JN.1 was the circulating strain.

**How the nasal samples were taken** — described with unusual care: a polyvinyl alcohol sponge expanded in 50 mL saline, compressed in a syringe to a 4 mL mark to standardise residual volume, cut into six equal segments, one segment held in the right nostril for five minutes, transferred within four hours into transport medium, centrifuged, stored at −80 °C. Standardising the sponge's residual volume is the step that makes nasal antibody concentrations comparable between people, and most studies skip it.

**Feature selection:** the **Boruta** algorithm, run on the training cohort only — random forest base, 500 trees, 100 maximum iterations, significance threshold 0.01. Then a **stability analysis**: Boruta re-run on 100 random 80% subsamples. **Nasal sIgA and CD4⁺ central memory T cells were confirmed in 100% of the 100 runs.** BMI was confirmed in 10% and tentative in 47%. Vaccination status was rejected in 87%, sex in 97%, drinking in 99%, and smoking, diabetes and prior infection history in **100%**.

**Models:** six — adaptive boosting, Gaussian naive Bayes, k-nearest neighbours, logistic regression, random forest, extreme gradient boosting (XGB).

**The validation framework, which is the best in this reading list:** a **nested 5-fold cross-validation** in which "Boruta feature selection and hyperparameter tuning were strictly restricted to the training folds of each loop." Centring and scaling parameters were estimated on the training cohort and applied to the validation cohorts. AUC was the primary optimisation metric.

**Results:**
- Training apparent AUCs across the six models: **0.783 to 0.957**; XGB apparent **0.914**
- **Nested cross-validated, optimism-corrected AUC for XGB: 0.834 ± 0.084**
- Internal validation AUC: **0.835**
- **External validation AUC: 0.996**
- External cohort metrics: accuracy **0.974**, sensitivity **1.000**, specificity **0.971**, PPV **0.805**, NPV **1.000**, F1 **0.892**

**A confounding check the paper ran unprompted:** multivariable logistic regression adjusting for age, sex, infection history, vaccination history, alcohol, smoking, BMI and diabetes. Nasal sIgA remained associated with reduced reinfection (**OR 0.995 per unit, 95% CI 0.993–0.997, p < 0.001**); CD4⁺ central memory T cells showed a protective trend that did not reach significance (**OR 0.427, 95% CI 0.167–1.093, p = 0.076**).

**Baseline differences in the whole cohort:** nasal sIgA **4.99 vs 66.16** (p < 0.001), serum IgG **113.42 vs 166.52 AU/mL** (p = 0.001), CD4⁺ central memory T cells **0.01% vs 0.05%** (p < 0.001), all lower in those later reinfected. Median age 55 versus 62 (p = 0.059, not significant). No differences in sex, BMI, smoking, drinking, diabetes, number of prior infections or number of vaccine doses.

**Calibration curves and decision curve analysis** were performed in all three cohorts; both reported as favourable for XGB.

## 3. How Strong Is This Evidence? (Grade 3/5)

**The methodology here is 4-grade work. The headline external result is 2-grade reporting. The net is 3, and the split is worth being explicit about.**

**What this paper does better than anything else in this reading list:**

**A nested cross-validation with the feature selection inside the loop.** This is the single most-skipped step in applied machine learning and the paper does it, says it did it, and quotes the resulting number: apparent AUC 0.914 falling to a corrected **0.834 ± 0.084**. Two days ago this list criticised a paper for selecting its model and tuning its prompt on the evaluation data; this paper is the counterexample. **The 0.834 is the honest estimate of what this model does, and the authors produced it themselves.**

**A Boruta stability analysis over 100 subsamples, reported per variable.** Not just "Boruta selected these two" but *how often* — 100% for both survivors, 10% confirmed and 47% tentative for BMI, 87% to 100% rejection for the clinical covariates. That is far more informative than a p-value, because it tells you whether the selection would survive a different sample. It usually would not. Here it would.

**Prospective design with written informed consent**, markers measured before any outcome occurred.

**External validation at a genuinely separate site** — 586 participants from another city, not a held-out slice.

**Loss to follow-up of 2.5%, enumerated by reason, with the lost compared against the retained.** Almost nobody does the comparison.

**A multivariable confounding check on the selected markers**, adjusted for eight covariates, with the non-significant result (p = 0.076) reported rather than buried.

**Sample collection standardised at the step that matters** — the sponge's residual volume — which is what makes nasal antibody levels comparable across people.

**They chose their final model on generalisation, not on apparent performance.** The text notes that KNN and random forest had higher training AUCs and XGB was preferred for consistent discrimination across validation analyses. That is the right basis.

**A limitations section that names seven real problems**, including the one that undercuts their own strongest claim: both cohorts were "recruited within the same province and during a similar epidemic period."

**Why it is not a 4:**

**The external AUC of 0.996 is not interrogated.** It is higher than the internal validation (0.835), higher than the cross-validated estimate (0.834 ± 0.084, putting 0.996 about **1.9 between-fold standard deviations** above the mean), and higher than the **apparent in-sample** training AUC of **0.914** — the model performed better on 586 strangers than on the 400 people it was fitted to. The paper reports this as the model's best result and selects XGB partly on the strength of it. Section 5 explains what is almost certainly going on.

**The paper contains the diagnosis and does not use it.** Two sentences, in two different sections: the cohorts differ significantly on nasal sIgA, serum IgG, memory B cells, cTfh cells and two CD4⁺ subsets (all p < 0.05); and in the joint feature space "the Wuxi cohort showed moderate overlap between groups… the Nantong cohort demonstrated greater separation." Those are the explanation. Neither is connected to the AUC.

**The deliverable cannot be deployed.** The final model needs two inputs: a nasal spike-specific sIgA titre from an **in-house ELISA**, and a spike-specific CD4⁺ central memory T cell percentage from **flow cytometry on freshly isolated PBMCs with activation-induced marker assays**. Neither is a test any ordinary clinic can order. The paper built a public web calculator that asks the user to type in both.

**Three paragraphs of immunological mechanism are built on a SHAP curve from ~46 events.** The U-shaped relationship for CD4⁺ central memory T cells — moderate good, very low and relatively high both bad — appears nowhere else in the paper. The univariate comparison is monotone (0.01% vs 0.05%) and so is the adjusted odds ratio (0.427, p = 0.076). Section 4 takes this up.

**No funding statement, no competing-interests statement, and no reporting guideline** in the retrieved text. TRIPOD+AI fits this design and most of its items are already satisfied.

**What would make it a 4:** investigate the external result rather than celebrate it — compare the marker distributions between cohorts quantitatively, check for assay batch differences, and recalibrate; report a version of the model using markers a clinic can measure, or drop the calculator; and name a reporting guideline.

## 4. The Editor's Concerns

**An external result that beats the training result is a measurement question, not a modelling triumph.** Taking the paper's own numbers at face value, the model's discrimination improved by 0.161 when it moved to a city it had never seen, and by 0.082 relative to the data it was fitted to. There is no mechanism by which a frozen model gets better at a task. What changes is the task. The honest reading is that **Nantong posed an easier sorting problem than Wuxi**, which the paper's Figure S2 describes in words, and the reason the problem is easier is exactly what Table S3 reports: the marker distributions differ between the cohorts, significantly, including for both of the model's two inputs.

**The candidate explanations are all worth ruling out, and none is.** Assay batch effects, if the two sites' samples were processed in separate runs with different calibration. Differences in when samples were taken relative to each city's epidemic wave, which would shift nasal antibody levels systematically. Differences in how reinfections were detected between sites, since ascertainment was self-triggered. Or genuine population differences. These have very different implications — a batch effect would mean the 0.996 is an artefact, while a case-mix difference would mean it is real but not transportable — and the paper does not distinguish them.

**The outcome definition is linked to the top predictor through symptom severity, and this is not noted.** Reinfection was counted only when symptoms prompted a test. Nasal sIgA is a mucosal antibody whose job is to blunt infection at the point of entry. A person with high nasal sIgA who does get infected plausibly has a milder course — and so is less likely to feel ill enough to test. **High sIgA may therefore reduce the chance of being *recorded* as reinfected, separately from reducing the chance of being infected.** The paper names the ascertainment bias and says the model applies to symptomatic reinfections only; it does not note that the under-detection is likely to be strongest in exactly the people the model scores as low-risk, which would inflate the apparent protective effect.

**The non-linear CD4⁺ T cell story rests on one SHAP plot and nothing else.** The paper devotes a long passage to why moderate levels might be protective while high levels are not — contraction of the naive T cell pool, constrained TCR repertoire diversity, repeated antigenic stimulation, memory quality versus quantity. It is a coherent and interesting hypothesis. But the evidence for the U-shape is a SHAP dependence plot from a gradient-boosted tree fitted to roughly **46 outcome events with two input variables**. Boosted trees produce step functions, and with that few events a step in the upper tail can be a handful of individuals. Meanwhile the paper's own two conventional analyses — the univariate medians and the adjusted logistic regression — are both **monotone**, and the adjusted one is not significant. **A shape that only the machine-learning model sees, in the sparsest region of the data, is a model artefact until something else confirms it.**

**The CD4⁺ measurement sits very close to the floor of what flow cytometry can resolve.** The reported medians are **0.01% and 0.05%** of CD4⁺ T cells. If 500,000 CD4⁺ T cells were acquired, 0.01% is about 50 events with a counting coefficient of variation near 14%; at 50,000 cells it is five events and a CV near 45%. The number of cells acquired is in the Supplementary Methods, which were not retrievable, so this cannot be checked — but the difference between 0.01% and 0.05% being a reliable biological signal versus counting noise depends entirely on it, and a paper resting a two-variable model on this measure should state it in the main text.

**The odds ratio for nasal sIgA cannot be interpreted as printed.** OR 0.995 per unit sounds like nothing. Across the gap between the two groups' medians (61.17 units) it compounds to 0.736, a 36% higher odds of reinfection at the low end — modest. But if some individuals have sIgA in the hundreds, the same coefficient across 500 units is 0.082, a twelve-fold effect. **The range and spread of sIgA are never reported**, so the clinical magnitude of the paper's strongest and most significant finding is unreadable from the paper. Section 5 shows the arithmetic.

**Eighteen candidates were screened against about 46 training events.** By the usual accounting the final model has 23 events per variable, which is comfortable. Against the 18 variables the outcome was consulted about, it is **2.6** — and Boruta is itself an outcome-driven procedure. The saving grace, and it is a real one, is that the stability analysis shows the two survivors would have been selected from any 80% subsample.

**The abstract reports the internal number and describes the external one in words.** "The prediction model achieved an AUC of 0.835 in the internal validation cohort and demonstrated strong discrimination in the external validation cohort." The 0.996 appears only in the body. Whether that is restraint or avoidance is not something the text settles, but a reader of the abstract alone gets the more defensible figure.

**Where I am uncertain, stated plainly.** The supplementary material was not retrievable, and it holds material that would settle several of the above: Table S3 (the per-cohort baseline comparison, which would show how far the marker distributions differ), Table S6 (the full six-model metric table), Table S7 (the nested cross-validation results per model), Table S4 (the Boruta stability counts in full) and Figure S2 (the joint feature-space plots). The confusion matrix reconstructed in Section 5 is derived, not printed. **The web calculator's URL was stripped by the text extraction and I have not guessed at it.** No funding or competing-interests statement appears in the retrieved text.

## 5. Statistics Spotlight

Three things. The first has never come up in this list because no previous paper produced the phenomenon.

### When external validation beats internal validation, something about the data changed

Every model-development paper decoded here so far has lost ground on new data. Entry 54 dropped from 0.86 to 0.77. Entry 58 held its ranking but destroyed its calibration. Entry 61's winner fell from first of five to fourth. Losing ground is the normal, expected thing: a model fits some real signal and some noise peculiar to its own sample, and only the real signal travels.

This paper went the other way. Line the numbers up:

- Apparent AUC on the training cohort (the data it was fitted to): **0.914**
- Nested cross-validated AUC, optimism corrected: **0.834 ± 0.084**
- Internal validation cohort (170 people, ~20 events): **0.835**
- **External validation cohort (586 people, 62 events): 0.996**

Approximate confidence intervals make the gap concrete. Using the Hanley–McNeil formula, the internal AUC of 0.835 on about 20 events and 150 non-events has a standard error near 0.057, so a 95% interval of roughly **0.72 to 0.95**. The external AUC of 0.996 on 62 events and 524 non-events has a standard error near 0.006, so an interval of roughly **0.985 to 1.000**. **Those two intervals barely touch.** They are not two noisy estimates of one number.

**Here is the thing that makes it unambiguous: 0.996 is higher than 0.914, the model's score on the very people it was trained on.** A frozen model cannot improve. Whatever produced the difference is a property of the data, not of the algorithm.

**And the explanation is a fundamental property of AUC that almost nobody internalises: AUC depends on the case mix, not just on the model.**

Recall what an AUC is: take every pairing of one person who had the outcome with one who did not, and ask how often the model scores the first higher. Now imagine two cohorts with the identical model:

- **Cohort A:** the sick have nasal antibody around 20, the well around 50. Lots of overlap. Many pairs are close together, and a model with any noise will get some of them the wrong way round. AUC maybe 0.83.
- **Cohort B:** the sick cluster near 3, the well near 80. Almost no overlap. Nearly every pair is easy. AUC 0.99.

**Same model. Same biology. Different question.** Cohort B is not testing the model harder; it is testing it on a population where the answer is more obvious.

The paper tells us which cohort is which, in a sentence it does not revisit: "the Wuxi cohort showed moderate overlap between groups… the Nantong cohort demonstrated greater separation between participants with and without reinfection, with reinfected participants tending to cluster in the lower-left region of the joint feature space." That is Cohort A and Cohort B. And the per-cohort baseline table reports that nasal sIgA and CD4⁺ central memory T cells both **differ significantly across the three cohorts** (p < 0.05).

**The technique, and it is general: before comparing two AUCs from two cohorts, compare the cohorts' predictor distributions.** If they differ, the two AUCs answer different questions and their difference is not a statement about the model. The things that would settle it here are cheap: plot the two cohorts' marker histograms side by side, check for assay batch effects, and — crucially — **report calibration separately for each cohort**, because calibration is far less forgiving of this than discrimination is. Entry 58 taught the reverse case: AUC that travelled while the probabilities collapsed. This paper is the mirror, and the same tool — look at calibration, not just ranking — resolves both.

**The watch-out:** an unexpectedly *high* external result should trigger the same scepticism as an unexpectedly low one. Readers are trained to doubt a drop and to celebrate a rise. Both are deviations that need explaining, and a rise above in-sample performance is the more impossible of the two.

### Reconstructing the external confusion matrix — and what sensitivity 1.000 is worth

The paper reports six numbers for the external cohort and no counts. From n = 586, accuracy 0.974, sensitivity 1.000, specificity 0.971, PPV 0.805, NPV 1.000 and F1 0.892, exactly one whole-number table fits:

> **TP = 62 · FN = 0 · FP = 15 · TN = 509**

Check every one: accuracy 571/586 = 0.9744 ✓. Sensitivity 62/62 = 1.000 ✓. Specificity 509/524 = 0.9714 ✓. PPV 62/77 = 0.8052 ✓. NPV 509/509 = 1.000 ✓. F1 = 124/139 = 0.8921 ✓. Six for six.

This tells us three things the paper does not print.

**First, the external event count: 62.** That matters because "sensitivity 1.000" is worth wildly different amounts depending on the denominator. Two days ago this list flagged a paper reporting 100% sensitivity on **one** patient — exact confidence interval 2.5% to 100%, which is to say no information at all. Here it is **62 out of 62**, and the exact Clopper–Pearson interval is **94.2% to 100%**. That is a genuine result. The model really did flag every reinfection in Nantong.

**Second, where the errors are.** Fifteen false positives, zero false negatives. The model was operating at a threshold that catches everything and over-calls 15 of 524 healthy people. The PPV of 0.805 (exact interval 69.9% to 88.7%) is the consequence: **of 77 people it flagged, 62 were right.** For a risk-stratification tool meant to target preventive measures, that is a reasonable trade.

**Third, the arithmetic for Wuxi by subtraction.** 128 total events minus 62 external leaves **66** among the 570 Wuxi participants, so roughly 46 in the training cohort and 20 in the internal validation cohort after the 7:3 split. The internal AUC of 0.835 rests on about 20 events, which is why its confidence interval is so wide.

**The technique, now used three times in four days:** when a paper publishes several percentages from one table, recover the counts. It takes a minute, it is usually unique, and it converts uninterpretable percentages into the thing you actually need — how many people, and which way the mistakes went.

### A per-unit odds ratio is meaningless without the variable's spread

The strongest and most statistically significant finding in this paper is the adjusted association between nasal sIgA and reinfection:

> **OR 0.995 per unit (95% CI 0.993 to 0.997), p < 0.001**

Read literally, that says one extra unit of nasal antibody cuts the odds of reinfection by half a percent. It sounds like nothing. The p-value says it is one of the most certain findings in the study. Both are true, and the apparent contradiction is the lesson.

**An odds ratio is always "per one unit of whatever this was measured in," and that unit is an arbitrary choice.** The quantity that matters is how much the odds change across the range people actually span. Compound it:

- Across **10** units: 0.995¹⁰ = 0.951 — a 5% difference in odds. Trivial.
- Across **61.17** units (the gap between the two groups' medians, 66.16 − 4.99): 0.995^61.17 = **0.736** — about 36% higher odds of reinfection at the low end. Modest but real.
- Across **100** units: 0.606 — 65% higher odds.
- Across **500** units: 0.082 — a **twelve-fold** difference.

**Same coefficient. Four different stories.** Which one is true depends on the spread of sIgA in the population — and the paper reports the two group medians and never the range, the interquartile range or the standard deviation. So the clinical magnitude of its headline immunological finding **cannot be read from the paper at all.**

**An everyday analogy.** Suppose a study says each extra metre of daily walking cuts your risk of something by 0.01%. Useless-sounding. But people walk thousands of metres a day, so across the real spread between a sedentary person and an active one the effect is large. Report it per kilometre and the same number reads as meaningful. **The unit is a presentation choice; the range is the fact.**

**The convention that fixes this** is to report the odds ratio **per standard deviation** or **per interquartile range** of the predictor, which makes it automatically interpretable and comparable with other predictors. The paper's other odds ratio shows why this matters for comparison too: CD4⁺ central memory T cells come in at **OR 0.427 (0.167–1.093)** — per one percentage point, on a variable whose medians are 0.01% and 0.05%. Nobody in this study moves by one percentage point on that scale, so the number describes an increment that does not exist in the data. The two odds ratios in this paper, 0.995 and 0.427, look as though they describe effects of completely different size. On a per-standard-deviation basis they might be very similar. **As printed, they cannot be compared with each other.**

**The watch-out:** whenever you see an odds ratio or hazard ratio close to 1.000 with a very small p-value, do not conclude the effect is negligible — find the units and the spread, and compound. And whenever you see one far from 1, check whether its unit is a step anybody actually takes.

## 6. Jargon Translator

**SARS-CoV-2 reinfection** — catching COVID-19 again after a previous infection. Here it counted only if symptoms appeared *and* a test was positive.

**Secretory IgA (sIgA)** — the antibody that works on wet surfaces: nose, airway, gut. It sits where the virus lands rather than in the bloodstream, and its job is to stop the virus attaching in the first place. Measured here from a nasal sponge.

**Spike protein** — the knob on the virus's surface that lets it into cells, and the target of vaccines and most antibody tests. "Spike-specific" means the immune measure counts only the antibodies or cells that recognise spike.

**JN.1** — the SARS-CoV-2 variant circulating during this study. The assays used JN.1 spike, which is why the authors caution that results may not transfer to very different future variants.

**Serum IgG** — the main antibody in blood. Systemic protection. It was significantly lower in the reinfected group (113 vs 167 AU/mL) but Boruta rejected it as a predictor.

**Central memory T cell (Tcm)** — a long-lived immune memory cell that waits in lymph nodes and can multiply fast when it meets the virus again. Distinguished from effector memory cells, which patrol tissues.

**CD4⁺ / CD8⁺ T cells** — helper and killer T cells respectively.

**cTfh cells (circulating T follicular helper)** — T cells that help B cells make better antibodies.

**Memory B cells** — cells that remember how to make a particular antibody and can restart production quickly.

**PBMCs (peripheral blood mononuclear cells)** — the white cells separated out of a blood sample for immune testing.

**Flow cytometry** — a machine that fires cells past lasers one at a time and counts how many carry particular markers. How the T cell percentages here were measured. At frequencies like 0.01% it is counting a handful of cells, which is why precision matters.

**ELISA** — a plate-based antibody test. "In-house" means the lab built it themselves rather than buying a standardised kit, which is normal in research and makes cross-study comparison harder.

**Boruta** — a feature-selection algorithm. It creates randomly shuffled "shadow" copies of every variable and keeps only the real variables that consistently beat their own shadows. Variables end up Confirmed, Tentative or Rejected.

**Stability analysis (by subsampling)** — re-running the selection on many random portions of the data to see whether the same variables keep winning. Here 100 runs on 80% subsamples; the two survivors won **all 100**.

**XGBoost (XGB)** — a model that builds many small decision trees in sequence, each correcting the last. Strong on tabular data, and it produces step-shaped rather than smooth relationships.

**Nested cross-validation** — the careful version. An outer loop holds data back for scoring; an inner loop does all the selecting and tuning on the remaining data only. It is the right way to get a performance estimate that is not inflated by the choices you made along the way.

**Apparent performance** — the score on the same data the model was fitted to. Always flattering.

**Optimism correction** — the gap between apparent and honest performance, estimated and subtracted. Here 0.914 apparent became **0.834 ± 0.084**.

**AUC / AUROC** — the share of (sick person, well person) pairs the model ranks the right way round. **Depends on the case mix as well as the model.** See Section 5.

**Calibration** — whether a predicted 20% risk happens 20% of the time. Separate from ranking, and far more sensitive to differences between cohorts.

**Sensitivity / specificity / PPV / NPV** — of those who truly had it, how many you caught; of those who truly did not, how many you cleared; of those you flagged, how many really had it; of those you cleared, how many really did not.

**F1 score** — the harmonic mean of PPV and sensitivity, as a single balance number.

**Odds ratio (OR)** — how much the odds of the outcome multiply per one unit of the predictor. Below 1 is protective. **Uninterpretable without the predictor's spread** — see Section 5.

**SHAP value** — how much a particular variable pushed the model's output for a particular person away from its average. Shows what the model learned, which is not the same as what is true.

**Decision curve analysis (DCA)** — plots the net benefit of using the model against "treat everyone" and "treat nobody" across a range of risk thresholds.

**Ascertainment bias** — systematic error in *detecting* the outcome, as opposed to in causing it. Here, symptom-triggered testing means mild and silent reinfections were missed.

## 7. What You Can (and Can't) Say

**Fair to say:**

- ✅ "In 1,156 adults followed for about ten months in two Chinese cities, 11.1% had a symptomatic COVID-19 reinfection." Verified; 128 of 1,156.
- ✅ "People who were later reinfected had much lower nasal antibody at the start — median 4.99 against 66.16." Reported, p < 0.001.
- ✅ "An algorithm screening 18 variables kept only two: nasal spike-specific sIgA and spike-specific CD4⁺ central memory T cells." And they were selected in **100 of 100** stability subsamples.
- ✅ "Number of vaccine doses and number of prior infections were not useful predictors here." Rejected in 87% and 100% of subsamples respectively, and not significantly different between groups.
- ✅ "A properly cross-validated estimate of the model's discrimination is about 0.834." The authors' own nested cross-validation, 0.834 ± 0.084. **This is the number to cite.**
- ✅ "In the second city the model flagged all 62 reinfections, at the cost of 15 false alarms out of 524." Reconstructed and verified against all six reported metrics.
- ✅ "Nasal antibody remained associated with lower reinfection risk after adjusting for eight clinical factors." OR 0.995 per unit, 95% CI 0.993–0.997.
- ✅ "The authors report that their cohorts came from one province and one epidemic period." Stated as a limitation.

**Not fair to say:**

- ❌ "The model predicts reinfection with 99.6% accuracy." An AUC is not an accuracy, and the 0.996 is higher than the model's score on its own training data — a difference between cohorts, not a property of the model.
- ❌ "External validation confirmed the model." External validation produced a *different and better* result than internal validation, which needs explaining before it can confirm anything. The paper's own text reports that the cohorts' marker distributions differ significantly and that class separation was greater in the second city.
- ❌ "The model is better than its internal results suggested." A frozen model cannot improve. The task got easier.
- ❌ "Moderate levels of CD4⁺ central memory T cells are protective while high levels are not." That U-shape comes from one SHAP plot on a boosted tree with roughly 46 events. The paper's univariate and adjusted analyses are both monotone, and the adjusted one is not significant (p = 0.076).
- ❌ "Nasal antibody cuts reinfection risk by 0.5% per unit, so it barely matters." The per-unit odds ratio compounds — about 36% higher odds across the gap between the two groups' medians — and the range of the variable is never reported, so the real magnitude is unreadable.
- ❌ "Clinicians can use the web calculator to estimate a patient's reinfection risk." Its two inputs are an in-house nasal ELISA and a flow-cytometry rare-event assay on fresh blood cells. Neither is orderable in routine care.
- ❌ "Vaccination does not protect against reinfection." The study found vaccine *dose count* unhelpful for ranking individuals in an already heavily vaccinated and previously infected population. That is not a statement about whether vaccination works.
- ❌ "This applies to future variants." Every assay used JN.1 spike, and the authors say performance may not transfer to antigenically distant strains.
- ❌ "11.1% is the reinfection rate." It is the rate of **symptomatic, test-confirmed** reinfection under symptom-triggered self-testing. The true infection rate was higher, and the people most likely to be missed are plausibly those with the highest nasal antibody.

## 8. Bottom Line for Your Life

The genuinely interesting biology here is worth knowing even though the model is not ready for anyone to use. Among over a thousand adults who had all been infected and vaccinated before, **what best separated those who got COVID again from those who did not was not their blood antibody level, their vaccine dose count, or how many times they had been infected.** It was how much antibody was sitting in the lining of their nose. Those later reinfected had roughly a thirteenth as much.

That fits a simple picture — the nose is where the virus arrives, and defences stationed there matter — and it is part of why a lot of current vaccine research is aimed at nasal delivery. Nothing in this paper is actionable for you today: you cannot get your nasal antibody measured, and there is nothing you could do about the number if you could. But it is a reason to take the idea of nasal vaccines seriously as they appear.

For anyone appraising research, this paper teaches the most counterintuitive lesson in the list so far.

**An external validation result that is too good is as much of a warning as one that is too bad.** Readers are trained to be suspicious when performance drops on new data, and to relax when it holds up. This paper's model scored **0.996** on a new city after scoring **0.835** on held-back participants from its own — and, decisively, after scoring **0.914** on the people it was actually fitted to. **A frozen model cannot get better at a task.** When it appears to, the task changed. Here the paper itself reports both halves of the explanation, in two sentences it never puts together: the two cohorts' marker levels differ significantly, and in the second city the sick and the well sat much further apart. **An AUC describes a model and a population jointly.** Hand the same model an easier population and the number rises without anything improving.

And the most portable habit of the week: **when a paper reports an odds ratio close to 1 alongside a tiny p-value, do not conclude the effect is small.** Find the units, find the spread of the variable, and compound. Here 0.995 per unit becomes 0.74 across the observed gap between groups — and would become 0.08 if the variable spans 500 units, which the paper never tells you. **Ask for odds ratios per standard deviation or per interquartile range.** It is the difference between a number you can use and a number you can only recite.

Finally, credit where this paper is better than anything else here: it ran a **nested cross-validation with its feature selection inside the loop**, reported that its apparent AUC of 0.914 fell to **0.834 ± 0.084** once that optimism was removed, and showed through **100 subsampling runs** that its two chosen markers would have been picked from any portion of the data. That is the right way to find out what a model is worth. **The paper did the careful work and then put the uncareful number in the headline.** The careful one is still in there.

---

## Appendix — deferred-paper status, 2026-10-31

- **Google, "The anatomy of a personal health agent"** (Nature, PMID 42907512): no PubMed Central copy. Unchanged.
- **BMJ, LLM-trial reporting completeness review** (PMID 42869550): no PMC copy; Scite paywalled. Unchanged.
- **Annals of Internal Medicine, Choosing Wisely benchmark** (PMID 42896192): no PMC copy. Unchanged. Standing note: the overuse rate of 5.4% with a 95% CI of 0.6–12.2% is a clustering signature — that interval is almost certainly computed across the 15 recommendations rather than the 4,050 responses.
- **JAMA, "Clinician Use of an AI-Enabled Clinical Information Platform"** (PMID 42879271, PMC13673371): PMC record exists and serves an **empty body for the sixteenth consecutive day.** Standing instruction unchanged — **if still empty on 2026-11-05 (day 21), decode abstract-only and say so explicitly.**

---

*This is an educational analysis of a published scientific paper, not medical advice. Nothing here is guidance about COVID-19, vaccination or your own risk. If you have questions about reinfection or vaccination, speak to a doctor.*
