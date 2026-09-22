# Automated three-dimensional radiomic body composition analysis enhances survival prediction in resectable non-small cell lung cancer

- **Authors:** Yilong Huang, Chuanpu Li, Fan Yang, Xin Chen, Xiaobo Chen, Yanqi Huang, Zhenguang Zhang, Lei Yang, Yuanming Jiang, Hanxue Cun, Zhanglin Mou, Wei Yang, Zaiyi Liu, Bo He (First Affiliated Hospital of Kunming Medical University; Guangdong Provincial People's Hospital; Southern Medical University; Guangzhou First People's Hospital; with collaborators at Zhejiang Chinese Medical University and Maastricht University Medical Centre) — 14 authors
- **Venue:** European Radiology Experimental, 2026;10(1) (published September 18, 2026)
- **DOI link:** https://doi.org/10.1186/s41747-026-00802-2
- **PubMed link:** https://pubmed.ncbi.nlm.nih.gov/42758420/ (PMID 42758420)
- **Full-text link used:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC13588999/ (PubMed Central, open access)
- **Basis:** FULL TEXT — introduction, complete Methods, all results, discussion, and stated limitations were read from the open-access PubMed Central copy. Figures and the supplementary methods, tables, and results were not retrieved, so anything living only there — including the sample size calculation, the full performance table, and the decision curve plots — is described as reported rather than quoted in detail. Ethics: approved by the institutional review boards of all three participating hospitals under named protocol numbers, following the Declaration of Helsinki. Funding and competing-interest statements were not present in the retrieved text, which is worth noting because the segmentation software used is a commercial product. Identifiers verified against the live PubMed/NLM record; direct URL browsing is blocked in this environment, so links are constructed from that verified record.
- **Decoded:** 2026-09-22
- **Note on selection:** the queue holds only entries whose full text cannot be reached here, so today's run scanned the past week. Two stronger candidates on theme were found and could not be read. Details at the end.

---

# The Gist

When someone has lung cancer surgery, doctors estimate their outlook almost entirely from the tumour: how big, how far it spread, what the cells look like. This team argued that the scan taken before surgery contains a second story nobody reads — the state of the patient's body. Muscle, fat under the skin, fat around the organs, fat threaded through the muscle, bone. They built software to measure all five automatically in three dimensions across 1,038 patients at three Chinese hospitals, then asked whether adding that information improved survival predictions beyond the tumour. It did, modestly and consistently, including at a hospital that contributed nothing to building the model. The finding that stands out: patients whose *body* readings dominated the prediction in the harmful direction had the worst survival of any group — worse than the patients flagged by their tumours.

# Study Snapshot

- **Study type:** Retrospective multicentre modelling study with genuine external validation. Nobody was treated differently, nothing was deployed, and no clinical outcome was changed by any prediction.
- **What is automated and what is not.** The body composition measurement is fully automatic. **The tumours were outlined by hand** by two radiologists with 6 and 10 years of experience, blinded to clinical data, with a senior radiologist reviewing and adjusting. So the pipeline still needs an expert for half its inputs.
- **Patients:** 2,880 screened, 1,038 included, all having surgery with curative intent for confirmed non-small cell lung cancer between January 2013 and December 2017. Mean age 61.81, and 608 of them (58.7%) male.
- **How the three hospitals were used.** Two centres were pooled and randomly split 7 to 3 into a training set and an internal validation set. A third centre was held back entirely as an external validation set — the genuinely hard test.
- **Deaths and follow-up:** 293 patients (28.2%) died. Median follow-up was 3.31 years overall, but it differs sharply by site: 2.86 years at one centre, 2.43 at another, and 7.16 at the external centre. That difference matters for one of the paper's claims.
- **The centres were not alike.** They differed significantly on age, sex, body mass index, prior cancer, family history, tumour type, stage, and whether patients had chemotherapy.
- **What the software measured:** it first located the spine, using the vertebrae as anatomical landmarks, then segmented five tissue types in three dimensions — skeletal muscle, fat under the skin, fat around the organs, fat within muscle, and bone.
- **The measurement was checked against humans, carefully.** Spine localisation was correct in 97.5% of cases (194 out of 200). Overlap with manual outlines exceeded 0.98 for muscle, subcutaneous fat, visceral fat, and bone on a scale where 1.0 is perfect. The hardest tissue, fat inside muscle, reached 0.895. Agreement with manual measurements exceeded 0.99 on two separate statistics across all compartments.
- **How features became scores:** thousands of numerical descriptors were extracted from the tumour and from each tissue compartment, then narrowed by three successive filters — keep only those individually related to survival, drop any that duplicated another, then apply a method that shrinks weak predictors to zero. Ten features survived for the tumour and ten for body composition, combined into a tumour score and a body composition score.
- **A step worth noticing:** the images came from different scanners at different hospitals, so the team checked for and corrected systematic differences between sites before analysis.
- **The core result.** In the training cohort, both scores independently predicted survival: hazard ratio 2.72 for the tumour score and 2.03 for the body composition score, both strongly significant.
- **Adding the body improved the tumour-only model.** The ranking score rose from 0.695 to 0.749 in internal validation and from 0.692 to 0.742 in external validation, both statistically significant.
- **The full model, adding clinical facts, did better still.** 0.780 against 0.725 internally, and 0.779 against 0.726 externally. Predictions of survival at 1, 2, 3, and 5 years all exceeded 0.80.
- **They checked whether using it would help, not just whether it scored well.** Decision curve analysis showed the full model gave better net clinical benefit than the clinical or tumour-only models across all three cohorts. Only 3 of 29 studies in the delirium review decoded two days ago did this.
- **The cut-off points were fixed in the training data and applied unchanged to validation.** A small sentence that matters, for reasons below.
- **Four patient types emerged.** By asking which score dominated each individual prediction and in which direction, patients sorted into four groups. Those dominated by tumour in the protective direction did best. **Those dominated by body composition in the harmful direction did worst — consistently across all three cohorts, worse even than the tumour-harmful group.**
- **One subgroup analysis failed, and they reported it.** In patients with limited lymph node involvement in the internal validation cohort, the model did not separate high from low risk, which the authors attribute to too few patients and events in that slice.
- **Funding / conflicts:** not present in the retrieved text.

# How Strong Is This Evidence?

**Grade: 4/5 — unusually disciplined methodology for a radiomics study, with a real external validation cohort and several checks most papers in this genre skip, reporting a modest and consistent improvement that has not been tested on anyone prospectively.**

Read enough of these and you develop a list of things that separate a careful imaging study from a hopeful one. This paper does most of them. There is a third hospital held completely out of model building. The cut-off values were chosen in the training data and applied to the validation cohorts **unchanged** — compare the kidney cancer study decoded on 17 September, where cut-offs were chosen by an algorithm hunting for the best split in the same patients it then described, a practice those authors flagged as a limitation. The segmentation was validated against blinded manual work with overlap and agreement statistics reported per tissue. Systematic differences between scanners were detected and corrected. Secondary comparisons were corrected for multiple testing. A subgroup analysis that failed is in the paper rather than the drawer. And they ran decision curve analysis, which asks whether acting on the model beats the alternatives — the check that the delirium review found in only 10% of a whole literature.

What holds it at 4 is partly design and partly arithmetic. It is retrospective, so the associations reflect whatever was and was not recorded. The "fully automated" framing applies to body composition only; a radiologist still outlines every tumour by hand, which is the slow part. Overall survival is shaped by adjuvant treatment, other illnesses, and tumour genetics, none of which entered the model — the authors say this plainly and describe their scores as complementary rather than standalone. And the 5-year predictions rest on thinner ground than they appear to, for a reason the paper does not discuss.

# The Editor's Concerns

- **The five-year claim outruns the follow-up at two of three centres.** Median follow-up was 2.86 years at one contributing centre and 2.43 at the other. A median of 2.43 years means half those patients were followed for less than that. A 5-year prediction estimated in the internal validation cohort therefore rests on a minority who reached five years — and people with long follow-up are not a random sample of patients, they are disproportionately the ones who lived. The external centre, with 7.16 years median follow-up, is the only one comfortably able to support a 5-year figure.
- **The four "phenotypes" are derived from the model's own outputs.** Patients were sorted by which score contributed more to their individual prediction and in which direction, then those groups were shown to have different survival. But the model was built to predict survival, so groups defined by its internal reasoning separating on survival is close to guaranteed. The BC-harmful group doing worst is a striking observation and it is a description of how the model behaves, not an independent discovery about patients.
- **"Fully automated" describes half the pipeline.** Body composition is automatic. Tumours were segmented manually by two radiologists and reviewed by a third. Any hospital adopting this still needs expert time for every case.
- **The segmentation tool is a commercial product and no conflict statement could be retrieved.** The framework is named with a version number and a company. That may be entirely fine, and the retrieved text simply does not contain the declaration that would let a reader check.
- **The three hospitals differ on nearly every baseline variable.** Age, sex, body mass index, prior malignancy, family history, tumour type, stage, chemotherapy — all significantly different. The team corrected the *images* for scanner differences, which is good practice, but no correction addresses three genuinely different patient populations. That the model still worked at the external centre is reassuring; it also means the external test involved a different kind of patient, not just a different scanner.
- **The improvement is real and modest.** Going from 0.725 to 0.780 is a gain of 0.055 on a scale where 0.5 is a coin flip. That is a meaningful step and it is not a transformation, and the difference matters when deciding whether a hospital should add a processing step to every scan.
- **Overall survival includes deaths from anything.** A patient who dies of a heart attack counts the same as one who dies of lung cancer. Body composition plausibly predicts general frailty, so part of what the body score captures may be "this person was unwell in a broad sense" rather than anything specific about their cancer.
- **The biological explanations are speculative, and labelled as such.** The discussion offers mechanisms for why fat inside muscle or bone texture might matter, then states these "remain hypothesis-generating and warrant further biological validation."
- **All three centres are in China, and nothing was tested prospectively.** The authors note the workflow's real-world implementation and clinical utility have not been evaluated.
- **What this study did well:** held one hospital entirely out of model development; fixed cut-off values in training data and applied them unchanged to validation; validated the automatic segmentation against blinded manual outlining with per-tissue overlap and agreement statistics; detected and corrected systematic differences between scanners before analysis; used a three-stage feature filter to avoid keeping redundant predictors; corrected secondary analyses for multiple testing; built a ladder of models so the contribution of each addition could be seen separately; ran decision curve analysis rather than stopping at discrimination; reported a subgroup where the model failed; estimated required sample size in advance; obtained ethics approval at all three sites with protocol numbers; and wrote limitations that concede residual confounding and describe the scores as complementary biomarkers rather than determinants.

# Statistics Spotlight

**1. The concordance index — what AUC becomes when you are predicting *when*, not *whether*.**
- *What it is:* You have met AUC repeatedly on this list: given one patient who has the outcome and one who does not, how often does the model score the first higher? Survival data breaks that setup, because the question is not whether someone dies but when, and because many patients are still alive when the study ends. The concordance index, or C-index, adapts the idea: take every pair of patients where you can tell who died first, and ask how often the model ranked that person as higher risk. Like AUC, 0.5 is a coin flip and 1.0 is perfect.
- *How this paper used it:* It is the main yardstick throughout. The tumour-only model scored 0.695 internally and 0.692 externally. Adding body composition raised those to 0.749 and 0.742. The full model with clinical facts reached 0.780 and 0.779. Comparisons between models used bootstrap resampling, which repeatedly redraws the patients to see how much each number would wobble.
- *The theory, with a worked example:* Picture 100 patients and imagine lining them up in the true order they died. A C-index of 0.78 means that if you pull any two patients out of the hat where you know who went first, the model gets their order right about 78 times in 100. Read the other half of that sentence: it gets the order wrong 22 times in 100. And note what "you can tell who died first" quietly excludes — two patients both still alive at the end of the study contribute nothing, because their order is unknown. The C-index is computed only on the pairs where the answer is knowable.
- *Watch out:* A C-index above 0.7 is often described as "good discrimination," and the phrase does a lot of work. It is a ranking measure only: it says nothing about whether a predicted 30% five-year risk corresponds to a real 30%, which is calibration and is a separate report card. It also cannot tell you whether the ranking is useful for any decision. This paper's decision curve analysis is the step that addresses the second gap, and it is the step most radiomics papers omit.

**2. Time-dependent AUC — and why follow-up length quietly limits it.**
- *What it is:* "Will this patient die" is not a question until you add "by when." Time-dependent AUC answers the question separately at each horizon: how well does the model separate the patients who died within one year from those who did not, then the same at two years, three, and five.
- *How this paper used it:* The full model produced AUCs above 0.80 at 1, 2, 3, and 5 years, and beat the tumour-only model at every one of those points in both validation cohorts, with the improvement statistically significant at every point in the internal cohort.
- *The theory, with a worked example:* Imagine judging a weather forecaster. Their skill at predicting tomorrow and their skill at predicting next month are different abilities and deserve different scores. Same here: predicting who dies within a year draws mostly on obvious severity, while predicting who is gone in five years is a subtler question about slow processes. Now the catch specific to this study. To score a 5-year prediction you need patients whose 5-year outcome is actually known. Median follow-up at the two model-building centres was 2.86 and 2.43 years. **Half the patients at one of those centres were followed for under two and a half years.** So the internal 5-year AUC is computed on the minority who were enrolled early enough to reach that mark — and those are disproportionately the earliest patients, treated with the oldest protocols, and disproportionately the survivors.
- *Watch out:* Whenever you see a five-year or ten-year prediction, find the median follow-up before believing it. If the follow-up is shorter than the horizon, the long-horizon numbers are estimated from a shrinking and non-random slice of the study. This is not fraud and it is rarely mentioned. Here the external cohort's 7.16-year median follow-up is what makes the 5-year claim defensible at all, and that is a detail buried in the results rather than stated as a caveat.

**3. Incremental value — the only question that matters for a new test.**
- *What it is:* A new measurement is never judged on whether it predicts something. Almost anything predicts something. It is judged on whether it predicts better than what you already have, for free, in the chart.
- *How this paper used it:* Properly, and visibly. They built a ladder: a clinical-facts-only model, a tumour-only model, a body-composition-only model, a combined imaging model, then clinical plus tumour, then clinical plus tumour plus body composition. Each rung shows what the next addition bought. The critical comparison is the last one: 0.780 against 0.725 internally, 0.779 against 0.726 externally. Then decision curve analysis asked the further question of whether acting on the better model produces net benefit across a range of decision thresholds. It did, in all three cohorts.
- *The theory, with an analogy:* Suppose someone markets a blood test that predicts heart attacks. Impressive on its own — until you notice it predicts them no better than asking the patient's age and whether they smoke. The test is not wrong. It is redundant. The only defence against being impressed by redundancy is to force the new thing to compete against the cheap old thing, in the same patients, and report the gap. Note what makes this study's version credible: the gap held up at a hospital that contributed nothing to building the model. A gain that appears only in the data used for fitting is usually the model remembering rather than knowing.
- *Watch out:* Two traps. First, any model with more variables fits its own training data better — always. Improvement means nothing unless it survives into data the model never saw, which is exactly why the external cohort's 0.726 to 0.779 is the number to quote and the training figures are not. Second, a higher C-index does not by itself mean anyone benefits. Decision curve analysis exists to bridge that gap, which is why its presence here is worth noting and its absence elsewhere is worth holding against a paper.

# Jargon Translator

- **Non-small cell lung cancer (NSCLC):** the most common category of lung cancer.
- **Resectable:** the tumour can be removed by surgery.
- **Overall survival (OS):** time from surgery until death from any cause, not just cancer.
- **Radiomics:** extracting large numbers of numerical descriptors — shape, brightness patterns, texture — from a medical image, on the theory that patterns invisible to the eye carry information.
- **Body composition:** the make-up of the body in tissue terms. Here five compartments: skeletal muscle, fat under the skin, fat around the organs, fat within muscle, and bone.
- **Segmentation:** outlining a structure on a scan so it can be measured.
- **Dice coefficient:** how much an automatic outline overlaps a human one, from 0 to 1.
- **Intraclass correlation coefficient:** how closely two methods agree on a measurement.
- **TNM stage:** the standard cancer staging system, describing tumour size, lymph node spread, and distant spread.
- **Hazard ratio (HR):** how much faster an event happens in one group than another at any moment. 2.72 means roughly 2.72 times the rate.
- **Concordance index (C-index):** the survival version of AUC. 0.5 is chance, 1.0 is perfect ordering.
- **Time-dependent AUC:** the same idea evaluated separately at each time horizon.
- **Kaplan-Meier curve:** the stepped graph showing what share of a group remains alive over time.
- **Log-rank test:** the standard test for whether two survival curves genuinely differ.
- **LASSO:** a method that shrinks weak predictors to exactly zero, used here to cut thousands of features down to ten.
- **XGBoost:** a widely used machine learning method for tabular data.
- **SHAP values:** a technique for attributing a model's prediction to its individual inputs, patient by patient.
- **ComBat:** a statistical correction for systematic differences between data sources, used here to reduce scanner effects.
- **Bootstrap resampling:** re-drawing the patients at random many times to see how much a result wobbles.
- **Bonferroni correction:** a strict adjustment for having run many statistical tests.
- **Decision curve analysis:** a method for asking whether acting on a model's predictions produces net benefit, rather than only whether it ranks well.
- **External validation:** testing on patients from an institution that contributed nothing to building the model.

# What You Can (and Can't) Say

**Fair to say:**
- "A 2026 multicentre study of 1,038 lung cancer surgery patients found that automatically measured body composition from the pre-surgery CT improved survival prediction beyond the tumour alone, with the ranking score rising from 0.692 to 0.742 at an independent hospital."
- "Adding clinical factors as well brought the score to 0.779 externally, against 0.726 for the model without body composition."
- "The automatic segmentation agreed closely with expert manual outlining, with overlap above 0.98 for four of five tissue types."
- "Patients whose predictions were driven mainly by body composition in the harmful direction had the worst survival in all three cohorts."
- "The authors state the workflow has not been prospectively evaluated and describe their scores as complementary biomarkers rather than standalone determinants of survival."

**Not fair to say:**
- "AI predicts lung cancer survival with over 80% accuracy" — the figures above 0.80 are time-dependent AUCs, which are ranking measures, not accuracy, and the 5-year figure rests on limited follow-up at two of the three centres.
- "Body composition causes worse lung cancer outcomes" — this is a retrospective association, and overall survival includes deaths from any cause, so some of the signal may be general frailty rather than anything cancer-specific.
- "The process is fully automated" — body composition is. Every tumour was outlined by hand by radiologists.
- "The study identified four patient types" — the four groups are defined by which score dominated each prediction in the model. They describe the model's behaviour, not an independently discovered biological classification.
- "This should change how lung cancer patients are followed up" — nothing was deployed, no decision was made using the model, and no patient outcome was compared.

# Bottom Line for Your Life

There is an idea worth keeping here that has nothing to do with lung cancer. Every scan taken of anyone contains far more than the thing it was ordered for. A chest CT taken to look at a tumour also photographs the patient's muscle, fat, and bone, and that information is discarded every day in every hospital in the world. This study is a demonstration that some of it is worth reading.

That said, read the size of the claim accurately. Adding all that body information moved the ranking score from 0.726 to 0.779 at the independent hospital. Real, repeated at a site that contributed nothing to building the model, and modest. Not a new era. A better estimate.

Two habits to take from how this was done. First, the authors fixed their cut-off points in the training data and applied them to the validation cohorts unchanged. Five days ago you read a study that let an algorithm find the best-separating cut-off in the same patients it then described, which reliably makes results look stronger than they are. The difference is one sentence in a methods section and it changes how much a survival curve is worth. Second, this team asked whether acting on the model would help, not only whether it scored well — the check that a systematic review found in 3 studies out of 29. When you next meet a prediction model, those are two specific, checkable things to look for.

And the concrete caveat worth carrying generally: when you see a five-year or ten-year prediction, find the median follow-up. Here it was 2.43 years at one of the three centres. A long-range forecast validated on people who have not yet been followed that long is estimated from whoever happened to enrol early, which is not a random group.

Nothing here changes anyone's care today. This is a retrospective study of software, and the authors say clearly that clinical utility has not been evaluated. One study is one data point. This is an educational breakdown, not medical advice.

---

**Sources** (based on articles retrieved from PubMed and PubMed Central; identifiers verified against the live PubMed/NLM record — URL browsing is blocked in this environment, so links are constructed from that verified record):
- DOI: https://doi.org/10.1186/s41747-026-00802-2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42758420/ (PMID 42758420)
- Full text (PMC, open access): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC13588999/

**Two stronger candidates from the past week that could not be read.** Both are recorded in the queue with verified identifiers, to retry once open-access copies appear:
- Berger J, et al. "Human learning is an understudied but promising lever for boosting human-AI synergy." *PNAS* 2026;123(39):e2536100123 — https://doi.org/10.1073/pnas.2536100123 (PMID 42766752). A reanalysis of all 74 studies from an earlier meta-analysis which had found that human-AI combinations do not, on average, outperform the better of the two alone. Directly extends yesterday's decode on trust and dependency.
- Feng Y, et al. "Accuracy of Deep Learning in Detecting Cerebral Microbleeds: Systematic Review and Meta-Analysis." *Journal of Medical Internet Research* 2026;28:e95041 — https://doi.org/10.2196/95041 (PMID 42767630). Prospectively registered in PROSPERO, with QUADAS-2 appraisal and pooled sensitivity, specificity, and likelihood ratios — statistics this reading list has not yet covered.
