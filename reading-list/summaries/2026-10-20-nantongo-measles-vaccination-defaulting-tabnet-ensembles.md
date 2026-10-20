# Predicting Measles Vaccination Defaulting in Uganda and Kenya: Comparative Evaluation of Custom Soft Voting and TabNet Stacked Ensemble Architectures

**Authors:** Nantongo BA, Nabukenya J, Nabende P (3 authors; Kyambogo University and Makerere University, Kampala, Uganda)
**Journal:** JMIR AI, 2026; 5: e95727 (published 13 October 2026)
**Decoded:** 2026-10-20
**Analysis basis:** **FULL TEXT** (retrieved from PubMed Central, PMC13660459; 47,799 characters). Figures and the Multimedia Appendix — which hold the immunisation schedule (Table S1), the phi-k correlation heatmap, the confusion matrices, the SHAP plots and the prototype screenshot — were not viewable, so anything living only there is marked as not retrieved.

**Source links (verified):**
- DOI: https://doi.org/10.2196/95727
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42867502/
- Full text (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC13660459/

**Basis of link verification.** Direct URL fetching is blocked from this session (`doi.org` does not resolve under the network policy here). Verification was done against the live PubMed/NLM record: a query for PMID 42867502 returned this exact title, these three authors, JMIR AI volume 5 article e95727, DOI `10.2196/95727` and PMC ID `PMC13660459`; the full text was then retrieved from PubMed Central by that PMC ID and matches the record. Both halves of the chain were confirmed independently.

**Funding and competing interests: not reported in the text provided.** The PMC rendering carries no funding, competing-interests or acknowledgements statement.

**Ethics:** the DHS Program granted use of the Ugandan and Kenyan survey datasets under its IRB-approved procedures for public-use data. No individual consent was required, as only secondary anonymised data was used.

> **A note on why this paper, and not the week's two bigger ones.** Two more prominent medical-AI papers appeared in the same week and both were checked first. A BMJ systematic review measuring how completely clinical trials of large language models are reported (PMID 42869550) has no PubMed Central copy and every other route is blocked from here. A JAMA cross-sectional study of 952,008 clinicians submitting 271 million queries to an AI clinical-information platform (PMID 42879271) has a PMC record that currently serves no body text. Both are abstract-only from this session, so both were deferred to the queue with a weekly re-check rather than decoded on an abstract. Today's paper was retrievable in full, and it turned out to contain the cleanest statistical teaching case this reading list has encountered.

---

## 1. The Gist

Measles still kills infants in Uganda and Kenya, even though the vaccine is free. A large part of the problem is children who start the vaccination schedule and then never come back for the last shot, given at nine months old. Finding those children before they drop out is hard and expensive.

Three computer scientists in Kampala tried to predict it. They took the big national household health surveys from Kenya and Uganda — about 6,400 and 6,800 eligible infants — and trained a long list of machine-learning models to guess which babies would miss the measles dose. Then they combined the best models into "ensembles", which is just a committee: several models vote, and the committee's answer is taken.

The committees did better than any single model. In Kenya the improvement was declared statistically significant. In Uganda it was not.

But here is what the numbers actually mean, and it is the reason this paper is worth your time. **In Kenya the committee correctly flagged two more children than the best single model did — two, out of 337 children who really did default.** In Uganda it flagged eight more. **The country with the smaller gain is the one called significant, and the country with the bigger gain is the one called not significant.** Both results, by the paper's own confidence intervals, are consistent with no improvement at all.

The authors report all of this openly. They are not hiding anything. It is simply an unusually clear demonstration of how far apart "statistically significant" and "actually matters" can sit.

## 2. Study Snapshot

**Study type:** a **prediction-model development study** using secondary analysis of two national household surveys. The authors describe it as a retrospective cohort, which is fair about the data, but what they built is a prediction model, and that is the honest place for it on the evidence ladder: below a cohort study designed to answer a causal question, and far below a trial. It can tell you how well a model guesses an outcome in data it was built on. It cannot tell you that acting on those guesses helps any child.

**Data source:** the **Demographic and Health Survey (DHS)** — the standardised national household survey run in many countries. Kenya: the 7th KDHS, conducted by the Kenya National Bureau of Statistics in **2022**. Uganda: the 6th UDHS, conducted by the Uganda Bureau of Statistics with the Ministry of Health, **15 June to 18 December 2016**.

**And right there is the first thing to notice.** The two datasets are **six years apart**. The authors explain why — only 10% of the 2022 Ugandan survey is publicly released, too little for national estimates — and that is a reasonable constraint honestly stated. But every "difference between Kenya and Uganda" in this paper is also a difference between 2022 and 2016, a span that includes the COVID-19 disruption to routine immunisation that the paper's own introduction describes.

**Number of infants (n):**
- **Kenya: 6,403** eligible for measles vaccination.
- **Uganda: 6,793** eligible, out of 8,928 infants in the dataset.

**Who they were:** living infants born 2020–2022 (Kenya) and 2013–2016 (Uganda), old enough to be eligible for the first measles dose, which both countries give at **nine months** — the last of the basic infant antigens.

**The outcome:** defaulting on that first measles dose. Taken from the survey: a vaccination date on the child's card, a mark on the card, or the mother's report all counted as **immunised**; **"no" or "don't know" counted as defaulting.** Note that second half — a lost card and an unsure mother produce the same label as a child who genuinely never attended.

**How common was it:** **26.3% of Kenyan infants (1,685 of 6,403)** and **22.1% of Ugandan infants (1,504 of 6,793)** were classed as defaulters. Both figures reconcile exactly.

**What was compared:** nine baseline classifiers — TabNet (a neural network built for table-shaped data, with a built-in attention mechanism that makes it partly interpretable), multilayer perceptron, random forest, gradient boosting, AdaBoost, logistic regression, support vector machine, decision tree and naive Bayes — then two kinds of committee built on top: a **custom soft-voting ensemble** (the members' probabilities are averaged) and a **TabNet stacked ensemble** (the members' outputs are fed into TabNet as a final judge).

**The pipeline:** 20 candidate predictors chosen from prior literature, cut to **11** using the phi-k correlation coefficient against the outcome plus a z-score significance threshold; missing values kept as DHS's own placeholder categories rather than imputed; RobustScaler for scaling; **SMOTE-NC** to balance the classes, applied *after* the train/test split, which the authors state explicitly was to avoid leakage; stratified 5-fold cross-validation; grid-search hyperparameter tuning; SHAP for interpretation.

**The test set:** the split size is not stated in words, but it is recoverable. Kenya's test set contained 337 defaulters out of 1,685 in total, and Uganda's 301 out of 1,504 — **20.0% in both cases**, so an 80/20 split.

**The decision threshold — and this is the central methodological issue.** From the Methods, verbatim: "The decision boundary was optimized dynamically using precision_recall_curve to maximize the localized (F1-score) harmonic mean of precision and recall **on the test set**." The cut-off that turns a probability into a yes-or-no was chosen using the same data on which performance is then reported.

**Main outcome measured:** F1 score, with accuracy, precision, recall and AUROC alongside; McNemar's test and bootstrap confidence intervals for comparing the ensembles against the best tuned single model.

**Funding / conflicts of interest:** **not reported in the text provided.**

### The results

**Single models.** Kenya: gradient boosting best at F1 **0.7034**, then support vector machine 0.7013, AdaBoost 0.6955. Uganda: random forest best at F1 **0.6520**, then gradient boosting 0.6495. Worst were naive Bayes (0.4600, Uganda) and decision tree (0.5731, Kenya). Standard deviations across the five folds were small, the largest being 0.0246. Tree-based models beat the deep-learning ones.

**Ensembles.** Kenya: TabNet+GB+RF soft voting, **F1 0.7111, AUC 0.8847**. Uganda: GB+RF+AB stacked into TabNet, **F1 0.6756**, AUC reported as **0.8862 in the abstract and 0.8867 in the Discussion** — the same quantity given two different values.

**The gain over the best tuned single model:** Kenya **+0.0054** F1 (0.7057 → 0.7111) and **+0.0018** AUC. Uganda **+0.0059** F1 (0.6697 → 0.6756) and **+0.0038** AUC.

**In children:** the ensembles correctly caught **2 more defaulters out of 337 in Kenya (0.6%)** and **8 more out of 301 in Uganda (2.7%)** than the best tuned single models did.

**Overall detection:** the final models caught **256 of 337 Kenyan defaulters (76%)** and **226 of 301 Ugandan defaulters (75%)**.

**The statistical comparison, exactly as reported.** Kenya: ΔF1 = 0.0054, **95% CI −0.0156 to +0.0260**, Cohen's g 0.1716, McNemar χ² = 7.224 (1 df), **p = .007, "Significant"**. Uganda: ΔF1 = 0.0059, **95% CI −0.0113 to +0.0222**, Cohen's g 0.0333, McNemar χ² = 0.033 (1 df), **p = .86, "Not significant"**. The authors print both confidence intervals and note in the text that Kenya's "spans zero".

**What the model thinks matters (SHAP).** Kenya: the child's current age (mean absolute SHAP 0.1795), most recent vitamin A dose (0.0747), respondent's education (0.0427), time to water source (0.0333), district previously lived in (0.0173). Uganda: vitamin A (0.0743), child's age (0.0737), inactivated polio vaccine (0.0563), Pentavalent 3 (0.0494), district (0.0317).

## 3. How Strong Is This Evidence? (Grade 2/5)

**Grade: 2/5 — weak as evidence for its conclusions, but unusually honest in its reporting, and the honesty is what makes it useful.**

The subject matter is real and important: measles kills infants in both countries, defaulting drives outbreaks, and the existing ways of finding defaulters are expensive and unreliable. The data is nationally representative, drawn from properly designed survey sampling frames. The pipeline is described in enough detail to criticise, which is more than many papers manage.

**What it genuinely supports.** That from routine national survey variables, a machine-learning model can identify roughly three-quarters of the infants who will miss their measles dose, at the cost of a substantial number of false alarms. That is a real and potentially useful finding, and it is roughly the same whichever of the nine models or two ensembles you use.

**What it does not support.** That the ensemble architectures are an advance worth the computational cost. The paper's own confidence intervals contain zero in both countries, and the practical gain is two children in Kenya and eight in Uganda. Nor does it support the country-specific policy recommendations, for two separate reasons given below.

**Five things hold it at 2.**

**The headline comparison is reported as significant while its own confidence interval contains zero.** The authors print both — ΔF1 0.0054 with a 95% interval of −0.0156 to +0.0260, and p = .007 — and then write that the result "confirms the advanced ensemble's structural advantage in Kenya." Those two statistics answer different questions, and both are correctly computed; the problem is choosing the flattering one for the conclusion. The Statistics Spotlight takes this apart, because it is the most instructive thing in the paper.

**The decision threshold was tuned on the test set, and the Methods say so.** The paper is more transparent about this than most. But it means every reported performance figure is a best case fitted to the data it is scored on, and the paper's own numbers show how much that can be worth: threshold tuning alone raised the decision tree's F1 by **0.1172** in Kenya. When a tuning step can move a model by a tenth of an F1 point, selecting the winner among twelve candidates on tuned-on-test numbers is not a neutral act.

**The Uganda recommendations come from a model the authors say had no valid advantage.** The Discussion states plainly that Uganda's result "was stochastic indicating that the ensemble architecture provided no statistically valid predictive advantage in that context." The Recommendations section then uses that same model's SHAP values to recommend specific Ugandan public-health strategies. If the model has no demonstrated advantage, its internal rankings are not a basis for policy.

**The cross-country comparison is confounded by six years.** Kenya 2022 against Uganda 2016, with the COVID-19 disruption to routine immunisation sitting between them. Any claim that a predictor "matters in Kenya but not Uganda" is equally consistent with "matters in 2022 but not 2016". The authors state the gap and its cause; they do not carry it into the interpretation.

**The strongest predictors are other vaccines from the same schedule.** In Uganda the top five include inactivated polio and Pentavalent 3; vitamin A is first in Uganda and second in Kenya. The paper's own framing is that previous work "overlooked community, demographic, and socioeconomic factors" and that this study adds them — yet what the model mostly learned is that children who missed earlier appointments miss the next one. That is a true and even useful pattern, but it is an adherence-trajectory model, not the social-determinants model the introduction promises. There is also a timing question the paper never addresses: **it is not stated whether the "most recent vitamin A" dose was recorded before the nine-month measles visit or at it.** If at it, that variable is not available at prediction time and should not be in the model.

**What pulls it up to 2 rather than 1.**

The authors reported the null. Uganda's non-significance is in the abstract, in the results, and in the discussion, stated without softening — "algorithmic complexity does not universally guarantee statistical superiority" is a sentence most authors would have cut. They printed both confidence intervals including the one that undermines their headline. They applied SMOTE after the train/test split and said why. They reported fold-level standard deviations. They used the phi-k coefficient sensibly for a mixed categorical/continuous feature set. The limitations section correctly warns that SHAP values "may reflect training correlations rather than direct epidemiological drivers". They built a working prototype with a concrete integration path into Uganda's existing DHIS2-based vaccination registry, which is more than most prediction papers attempt.

**Where 2/5 sits.** This is the same grade as yesterday's chest X-ray paper, and for a related reason: a competent study whose stated conclusions outrun what its design can carry. The difference is that this one hands you the evidence against itself, in print, in its own tables. That is a form of scientific integrity, and it is why the paper is worth reading even though the finding is not.

## 4. The Editor's Concerns

**Lead with the confidence interval, not the p-value.** The Kenya comparison should be reported as "ΔF1 0.0054, 95% CI −0.0156 to 0.0260" in the abstract, with the McNemar result as support. As written, the abstract says the ensemble "achieved significant, nonrandom performance over tuned base models" and never mentions that the interval contains zero.

**Report the gain in children in the abstract.** Two additional correctly identified defaulters out of 337 is the finding. Everything else is a way of describing those two children.

**Choose the threshold on held-out data.** With roughly 5,100 training records per country, a validation split for threshold selection costs almost nothing. Alternatively, pick the threshold inside each cross-validation fold and average, which is what a well-run pipeline does, and which one of this week's other papers did correctly.

**Reconcile the two Uganda AUC values.** 0.8862 in the abstract, 0.8867 in the Discussion.

**Withdraw the Uganda recommendations, or re-derive them from a model that works.** A model the paper describes as stochastic should not generate targeted public-health strategy. If the base gradient-boosting model is as good — and the paper says it is — then run SHAP on that and recommend from it.

**Do not read country differences off datasets six years apart.** Either restrict the comparison to the features least likely to have shifted, or frame the entire comparative section as hypothesis-generating. At minimum, the limitations should name the temporal confound, which they currently do not.

**State when the vitamin A dose was recorded relative to the measles visit.** If it was concurrent, it is not a predictor.

**Say whether SMOTE was applied inside each cross-validation fold or once before.** The text says balancing happened "after the split of training from test sets" and that experiments were run "after dataset balancing and with cross-validation", which reads as one balancing step before cross-validation. If so, synthetic samples generated from one fold's records appear in other folds' training data, and the cross-validation figures are optimistic. One sentence would settle it.

**Say whether feature selection used the full dataset.** Eleven features were kept from twenty using correlation with the outcome. If that was computed on all the data, the test set helped choose the features.

**Report calibration, not just discrimination.** A tool meant to flag individual infants for outreach needs its probabilities to mean something. There is no calibration plot and no calibration statistic.

**Add a funding and competing-interests statement.**

### What this study did well

- Took on a problem that matters, with nationally representative data rather than a convenience sample from one clinic.
- Reported the Uganda null result clearly, in the abstract and twice more in the text, and drew the correct conclusion from it about algorithmic complexity.
- Printed both confidence intervals, including the one that spans zero, rather than reporting the p-value alone.
- Applied SMOTE after the train/test split and said explicitly that this was to avoid leakage — a step many papers get wrong silently.
- Reported standard deviations across cross-validation folds, so the reader can see stability.
- Used an appropriate correlation measure for a mixed categorical and continuous feature set, with a stated redundancy rule.
- Acknowledged in the limitations that SHAP importance may reflect training correlations rather than real drivers — which is exactly the right caveat, even if the recommendations then ignore it.
- Built a working prototype and identified a real integration path into Uganda's existing DHIS2/EPIVAC registry, instead of stopping at a table of metrics.

## 5. Statistics Spotlight

### Concept 1: A significant p-value and a confidence interval that contains zero, in the same sentence

This is the heart of the paper, and it is reported in one line of Table 12 that most readers will skim past.

For Kenya, comparing the ensemble against the best tuned single model, the authors report: **ΔF1 = 0.0054, 95% CI −0.0156 to +0.0260, McNemar χ² = 7.224, p = .007.**

Read that again. The p-value says the difference is very unlikely to be chance. The confidence interval says the true difference could easily be **negative** — the ensemble could be slightly worse. Both numbers are correctly computed. They are not in conflict, because **they are answering two different questions.**

**What the confidence interval asks.** "How big is the difference in F1 score, and how precisely do we know it?" The answer: somewhere between 1.6 points worse and 2.6 points better, best guess half a point better. That range includes zero, so on this evidence the ensemble might be no better at all.

**What McNemar's test asks.** Something quite different. McNemar's test is for **paired** yes/no outcomes: the same children, classified twice, once by each model. It throws away every child both models got right and every child both got wrong, because those tell you nothing about which model is better. It looks only at the **disagreements** — the children one model got right and the other got wrong — and asks whether those disagreements are lopsided.

**A worked example with small numbers.** Suppose two models classify 100 children. They agree on 80. Of the remaining 20 disagreements, Model B is right 15 times and Model A is right 5 times. McNemar looks at 15 versus 5 and says: if the two models were equally good, you would expect about 10 and 10, and 15–5 is a fairly lopsided split, so this is unlikely to be luck. But notice the *net* gain: B is right 15 times where A was wrong, and wrong 5 times where A was right. Net, B gets 10 more children correct out of 100 — and whether that is a lot depends entirely on what you are doing with them.

Now shrink the net while keeping the lopsidedness. Suppose the disagreements are 67 for B and 33 for A. Very lopsided, very significant — yet those swaps are spread across both directions of error, and the net improvement in the summary score can be tiny. **That is what happened here.** Cohen's g of 0.1716 says roughly 67% of the disagreements favoured the ensemble. The net gain in correctly identified defaulters was **two children out of 337.**

**The everyday analogy.** Two proofreaders go over the same manuscript. Proofreader B catches 67 typos A missed; A catches 33 B missed. B is clearly doing something systematically different — that difference is real and not luck, and that is what the significance test detects. But the total error count drops by only a handful, because they are mostly catching different typos rather than B being better overall. "B behaves differently in a way that is not chance" and "the manuscript is meaningfully cleaner with B" are separate claims. The paper establishes the first and writes the second.

**Watch out.** When a paper reports both a p-value and a confidence interval for the same comparison and they point different ways, **the confidence interval is almost always the one that answers your question**, because your question is usually "how much better?" and not "is there any detectable difference at all?". And when a paper reports only one of the two, notice which one. The phrase to be alert to here is "statistically significant improvement" attached to a difference whose size is never stated in units you can picture. In this paper, the unit you can picture is children: two of them.

### Concept 2: Significance and effect size can rank two results in opposite directions

The same table contains the cleanest demonstration of this I have seen in a published paper, and it is sitting in plain sight.

**Kenya:** ΔF1 = **0.0054**, 2 extra children caught, p = **.007**, declared **significant**.
**Uganda:** ΔF1 = **0.0059**, 8 extra children caught, p = **.86**, declared **not significant**.

**Uganda's improvement is larger on both measures that matter — the F1 gain and the number of children — and it is the one declared not significant.**

**Why this happens, in plain terms.** Significance is not a measure of how big something is. It is a measure of how confidently you can rule out chance, and it depends on three things: the size of the effect, the amount of data, and — for a paired test like McNemar's — **how consistently the two models disagree in the same direction.**

In Kenya the disagreements were lopsided (Cohen's g 0.1716, roughly a two-to-one split), so even though the net gain was tiny, the *pattern* was hard to explain by luck. In Uganda the disagreements were close to an even split (Cohen's g 0.0333, roughly 53–47), so even though more children ended up correctly classified, that could easily have fallen the other way. One country had a consistent small difference; the other had an inconsistent slightly larger one.

**A tiny worked example.** Imagine two dice-based games. Game A pays you one pound, reliably, every single round — small, dull, unmistakably real. Game B pays an average of five pounds a round, but the payouts swing wildly between minus fifty and plus sixty. After a hundred rounds you can state with great confidence that Game A pays something, and you genuinely cannot tell whether Game B pays anything at all. **Game B is the better game. Game A is the more significant result.** Significance measured your certainty, not your winnings.

**Watch out.** Two traps, and they are mirror images.

The first is the one this paper falls into: treating "significant" as "worth doing". A significant result with an effect of two children and a confidence interval spanning zero is not a reason to deploy a more complicated model.

The second is the one a hasty reader falls into: treating "not significant" as "no effect". Uganda's eight additional children are not nothing. The honest statement is "we could not establish that the ensemble helps in Uganda", not "the ensemble does not help in Uganda" — and the authors, to their credit, use wording close to the first.

**The question that cuts through both.** Whenever you meet a significance claim, ask: *significant improvement of what, measured in what units, by how much?* If the answer cannot be given in something countable — children, days, pounds, deaths — the claim has not yet told you anything you can act on.

### Concept 3: Tuning the cut-off on the test set, three days running

This reading list has now met the same methodological decision three times in a row, in three different forms, and this paper supplies the plainest version.

**What happened.** From the Methods: the decision boundary "was optimized dynamically using precision_recall_curve to maximize the localized F1-score ... **on the test set**."

**Why it matters.** The test set exists to answer one question: how will this perform on data it has never seen? Using it to choose a setting means it has now been seen. Every performance figure in the paper is therefore the best case available from that particular set of children, not an estimate of what would happen in a new district next year.

**How much is it worth? The paper tells you, without meaning to.** Threshold tuning alone improved the **decision tree's** F1 by **0.1172** in Kenya and **0.0977** in Uganda — about a tenth of an F1 point, from nothing but moving the cut-off on the scored data. The better models gained less: TabNet 0.0250 and 0.0141, random forest 0.0189 and 0.0157. **A step that can move a weak model by a tenth of a point is not a formality.** And the winner among twelve candidate models was chosen using numbers every one of which had been through it.

**The one piece of good news, which is genuine.** The two final ensembles ended up with thresholds of **0.5125 and 0.5163** — barely moved from the default 0.5. So for the headline models specifically, the tuning changed very little, and the authors are right that this indicates the probability scores separated the classes cleanly. The damage is concentrated in the *comparison* between models, not in the headline numbers themselves.

**Set against the other two papers this week.** One fixed its thresholds inside cross-validation and locked them before any test data was touched — the correct procedure, and its headline numbers are the ones you can trust. One swept thresholds across the data it then reported on, and labelled them "optimised", which at least tells the reader. This one states the practice outright in the Methods, in a sentence most readers will not notice. **Three papers, three positions, and the order of trustworthiness is exactly the order of threshold discipline.**

**Watch out.** The phrase to search for is any variant of "optimal cut-point", "threshold optimisation", "Youden index was used", "best threshold was selected". Then find the answer to one question: *selected using which data?* If the paper does not say, assume it used everything. If it says "on the test set", the reported performance is an upper bound, and any ranking of models built from those numbers carries the same optimism.

## 6. Jargon Translator

- **Routine immunisation (RI)** — the standard schedule of childhood vaccines a country gives free of charge.
- **Defaulting** — starting the vaccine schedule and then not returning for a later dose. Distinct from **zero-dose**, a child who never started.
- **Vaccine-preventable disease (VPD)** — an illness a routine vaccine would have prevented.
- **Herd immunity** — the protection unvaccinated people get when enough of those around them are immune, so an outbreak cannot spread.
- **Demographic and Health Survey (DHS)** — a large standardised national household survey, run the same way in many countries, which is why the two countries can be compared at all.
- **Enumeration area** — the small geographic unit a national census is built from; in Uganda, about 130 households.
- **Pentavalent 3 / Polio 3 / inactivated polio vaccine (IPV)** — earlier doses in the same infant schedule, used here as predictors of whether the final measles dose was received.
- **Ensemble** — a committee of models. **Soft voting** averages the members' probabilities; **stacking** feeds the members' outputs into a further model that makes the final call.
- **TabNet** — a neural network designed for table-shaped data rather than images, with an attention mechanism that shows which features it used at each step.
- **Gradient boosting / AdaBoost / random forest** — three ways of combining many simple decision trees. In this paper they beat the deep-learning models, which is common with tabular data.
- **Class imbalance** — when one outcome is much rarer than the other, so a model can score well by always guessing the common one.
- **SMOTE-NC** — a method for class imbalance that invents extra synthetic examples of the rare class, handling mixed categorical and continuous features. Must be applied only to training data, which this paper did.
- **RobustScaler** — rescales features using the median and interquartile range instead of the mean and standard deviation, so extreme values do not distort it.
- **Phi-k correlation coefficient** — a correlation measure that works across categorical, ordinal and continuous variables at once, used here to drop redundant and uninformative predictors.
- **Stratified k-fold cross-validation** — splitting the training data into k parts (here 5), training on k−1 and testing on the last, rotating through, keeping the outcome proportion the same in each part.
- **Hyperparameter tuning / grid search** — trying many combinations of a model's settings and keeping the best.
- **F1 score** — the harmonic mean of precision and recall; a single number that is dragged down by whichever of the two is worse.
- **Precision-recall curve** — the trade-off between precision and recall across all possible cut-offs; used here to pick the cut-off.
- **AUROC** — the probability that the model scores a true defaulter above a non-defaulter. Measures ranking, independent of any cut-off.
- **McNemar's test** — the paired test used here to compare two models on the same children, described at length above.
- **Cohen's g** — the effect size that goes with McNemar's test: how far the split of disagreements departs from an even 50–50.
- **Bootstrap confidence interval** — a range of plausible values for a statistic, built by resampling the data many times.
- **SHAP (Shapley additive explanations)** — a method borrowed from game theory that assigns each feature a share of the credit for a prediction. **Mean absolute SHAP value** is the average size of that share across all cases, used here to rank predictors.
- **DHIS2 / EPIVAC** — the open-source health information system used across much of Africa, and Uganda's electronic immunisation registry built on it; the proposed home for the prototype tool.

## 7. What You Can (and Can't) Say

**Fair to say:**

- "Using national household survey data from Kenya and Uganda, machine-learning models identified about three-quarters of the infants who missed their nine-month measles dose — 256 of 337 in Kenya and 226 of 301 in Uganda."
- "About one in four Kenyan infants (26.3%) and one in five Ugandan infants (22.1%) in these surveys had not received the first measles dose."
- "Combining several models into an ensemble produced an improvement that was statistically significant in Kenya but amounted to two additional children correctly identified out of 337, with a confidence interval that included no improvement at all."
- "In Uganda the ensemble produced no statistically detectable advantage over a single gradient-boosting model, and the authors say so."
- "Tree-based models such as random forest and gradient boosting outperformed the deep-learning models on this tabular data."
- "The model's strongest predictors were the child's age and whether the child had received other items in the same immunisation schedule, alongside the mother's education, distance to a water source and district."
- "The decision thresholds were chosen using the test data, so the reported performance figures are a best case rather than an independent estimate."

**Not fair to say:**

- ❌ "Advanced ensemble learning significantly improves prediction of measles vaccine defaulting." Significant in one of two countries, by two children, with both confidence intervals containing zero.
- ❌ "The ensemble achieved 0.71 F1 and 0.88 AUC, so it is ready to deploy." Those figures come from thresholds fitted to the test set, with no external validation and no calibration assessment.
- ❌ "Kenya's result was stronger than Uganda's." Uganda's improvement was larger on both the F1 gain and the number of children. Kenya's was merely more consistent.
- ❌ "AI can now predict which children will miss their measles vaccine." It can rank children by risk using survey variables, in retrospective data, at about 75% recall with substantial false alarms. Nobody has tested whether acting on that ranking changes a single vaccination.
- ❌ "Distance to water predicts defaulting in Kenya but not Uganda." The Kenyan data is from 2022 and the Ugandan from 2016. That is a country difference and a six-year difference at the same time.
- ❌ "This shows Uganda should send reminders and Kenya should run outreach." Those recommendations come partly from a model the authors state had no valid predictive advantage.
- ❌ "Deep learning beat traditional methods." It did not. Gradient boosting and random forest beat TabNet and the neural network as single models, and the authors report this.
- ❌ "26% of Kenyan children are unvaccinated against measles." The outcome counted "don't know" answers and missing cards as defaulting, so the figure is an upper bound on true non-vaccination.

## 8. Bottom Line for Your Life

If you are a parent in Uganda or Kenya, nothing here changes anything: the measles vaccine is free, it is given at nine months, and this paper is about predicting who will miss it, not about whether to have it. If you work in immunisation programmes, the useful part is not the ensemble — it is the plain finding that routine survey variables can flag about three-quarters of likely defaulters, which an ordinary gradient-boosting model does about as well as the complicated committee. What is missing before anyone acts on it is an external test in a different year and district, a calibration check, and above all a study of whether flagging a child actually gets that child vaccinated. Prediction is not intervention.

For your paper-reading, take the one lesson this paper teaches better than any other in this list. **A p-value of .007 and a confidence interval running from −0.0156 to +0.0260 appear in the same sentence of the same table, describing the same comparison, and the practical difference between the two models is two children out of 337.** Nothing in that is a mistake. The p-value and the interval answer different questions, and both answers are correct. The error is only in which one became the conclusion. So when someone tells you a result is statistically significant, ask them the follow-up that does all the work: *how much better, in something I can count?* If they cannot answer, they have not told you anything yet — and quite often, as here, the answer is in the paper, in a column nobody read.

---

*This is an educational analysis of a published scientific paper, not medical advice. Nothing here is guidance about vaccinating a child. Measles vaccination is recommended by every major health authority; if you have questions about your child's immunisations, speak to a clinician.*
