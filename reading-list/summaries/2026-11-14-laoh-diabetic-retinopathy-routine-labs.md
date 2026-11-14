# A Robust and Trustable Approach to Incorporate Medical Domain Knowledge in Machine Learning Models for Diabetic Retinopathy Screening Using Routine Lab Results

**Authors:** Laoh E, Ahmad OB, Liu T (all three: School of Industrial Engineering and Management, Oklahoma State University, Stillwater, OK)
**Journal:** Smart Health (Amsterdam), 2026; volume 42: article 100724 (published 28 September 2026)
**Decoded:** 2026-11-14

**Analysis basis:** **FULL TEXT** (retrieved from PubMed Central, PMC13727297) — Introduction, Literature Review, all Methods sub-sections including the dataset, the TF-RCR procedure, both algorithm listings, the experimental design and the metric definitions, and all of Results and Discussion including Model Robustness, Model Interpretability and the Conclusion. **All figures and tables are unreachable**, which costs one specific thing named throughout: **the bootstrap confidence-interval values**, whose procedure is described but whose numbers live in a table.

**Source links (verified):**
- DOI: https://doi.org/10.1016/j.smhl.2026.100724
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42974596/
- Full text used: https://pmc.ncbi.nlm.nih.gov/articles/PMC13727297/

**Basis of link verification.** Direct URL fetching is blocked from this session (`doi.org` does not resolve under the network policy here), so verification was done against the live PubMed/NLM record. According to PubMed, a query for PMID 42974596 returned this exact title, these three authors with this affiliation, *Smart Health (Amsterdam)* volume 42 article 100724, publication date 28 September 2026, DOI `10.1016/j.smhl.2026.100724`, and keywords including "Trustable AI" and "Elaborative Learning"; a PMID-to-PMCID conversion returned **PMC13727297**; and the full text was then retrieved from PubMed Central by that PMC ID and matches the record. Both halves of the chain were confirmed independently.

**Data source and ethics.** Data came from **Oracle Health Real-World Data (OHRWD)**, a de-identified multi-site United States electronic health record network. **No IRB approval, consent waiver, or data-use agreement is mentioned anywhere in the retrieved text.** For de-identified commercial EHR data this is often genuinely exempt, but the statement is normally made, and I am reporting its absence rather than assuming either way.

**Funding and competing interests: not reportable.** Neither appears in the retrieved text.

**Reporting guideline: none named.** **TRIPOD+AI** applies directly to this study — it is a multivariable diagnostic/prognostic prediction model — and is not mentioned. Section 4 places that in a now seven-entry sequence, and yesterday's entry puts a number on what it means.

---

## 1. The Gist

**Three industrial engineers built a diabetic retinopathy screening model out of eight routine lab values and got an AUROC of 0.9724. The number is real, the arithmetic behind it is flawless, and the paper's own results contain two findings that together explain where that 0.9724 comes from — neither of which the authors draw out.**

The clinical problem is genuine and well argued. **Diabetic retinopathy is the leading cause of blindness in American adults**, 9.5 million Americans had it in 2020, and the projection is 16 million by 2050. Treatment works but **vision loss cannot be reversed**, so it has to be caught early. And yet **only about 43% of diabetic patients get their recommended annual eye exam**, leaving roughly **25% of DR cases unidentified** — partly because early DR has no symptoms, partly because ophthalmologists and retinal cameras are concentrated in cities. So the idea is excellent: **if you could flag high-risk patients from blood tests they already get at primary care visits, you could tell a GP who needs to be sent to an eye clinic**, with no new equipment at all.

The method is unusual and worth describing. Rather than ask a handful of clinicians which variables matter — the authors note that clinicians are busy and that a few of them may not represent the field — they **mined 13,002 PubMed papers** to score how prominently each candidate variable appears in the DR literature, weighting each paper by its **Relative Citation Ratio**. They then capped the model at a human-sized number of inputs, invoking **Miller's 7±2**, on the reasoning that a clinician can only hold so many variables in mind at once. The result is **eight features: age, glucose, nephropathy, neuropathy, HbA1c, hemoglobin, albumin and creatinine.**

**The performance, on a 19,558-patient test set never touched during development: 95.35% accuracy, 91.17% sensitivity, 96.22% specificity, PPV 83.42%, NPV 98.12%, F1 0.8712, AUROC 0.9724, AUPRC 0.9455.** I rebuilt the entire confusion matrix from the reported sensitivity, specificity and prevalence, and **all four derived metrics reproduce to within 0.0002.** The paper's arithmetic is impeccable, including a prevalence-scenario analysis I checked at four different prevalences. **Nothing here is sloppy.**

**Now the first thing the paper's own numbers show.** The authors did something commendable and rare: they benchmarked against four other models on the **identical patients, identical preprocessing, identical threshold.** Here is what they found. **Logistic regression: AUROC 0.9713. Multilayer perceptron: 0.9635. FT-Transformer: 0.9739. XGBoost with 24 features: 0.9750. Their proposed model: 0.9724.**

**A plain logistic regression came within 0.0011 of the proposed model.** The entire spread, from the simplest linear model to an attention-based transformer, is **1.15 AUROC points.** Converting to variance explained, the whole model zoo sits between **62% and 66%** — architecture buys about **three percentage points of variance.** When every method from linear to transformer performs the same, **the information is not in the model. It is in the features and the labels**, and that should send you to look at them.

**So look at them.** DR cases were identified by **ICD diagnosis codes**. Two of the eight predictors are **nephropathy and neuropathy** — which are the **other two members of the diabetic microvascular triad**, drawn from the same records, and caused by the same thing: how long and how badly the diabetes has been uncontrolled. Three more features — **creatinine, albumin and hemoglobin** — are the standard laboratory signature of diabetic kidney disease. **So four of the eight inputs are kidney-related and one is nerve-related.** The model is substantially being asked: given that this patient is coded with the other two microvascular complications and shows their lab fingerprint, is the third one also coded?

**And the design cannot separate detecting from predicting.** The authors state it plainly in their own limitations: **"The current study is based on static, cross-sectional laboratory measurements."** There is **no index date, no requirement that the labs precede the retinopathy code, no washout period, and no distinction between newly-developed and long-established DR.** A model can only be a screening tool if it sees the patient before the diagnosis does.

**One more signal, visible in the paper's own explanation section.** The SHAP analysis reports that **higher age was associated with *reduced* predicted risk, and lower hemoglobin with *reduced* predicted risk.** Both run backwards to established DR epidemiology — retinopathy rises with age and diabetes duration, and anemia is a recognised risk factor. Section 5 works through the most likely reason, which is instructive: **diabetes duration and type are not in the model at all**, and age appears to have been recruited as a distorted stand-in for them.

**What the authors deserve clear credit for.** This paper has visibly been through serious revision and the hedging is all in the right direction. It **repeatedly refuses to claim its model is interpretable** — "Because XGBoost is not intrinsically interpretable…" appears more than once, and interpretability is explicitly defined as the combination of a short feature list plus post-hoc attribution. It states that **clinician comprehension and trust were not evaluated**. It reports a sensitivity check showing its own headline novelty barely matters. It declares that **external validation has not been done** and says a dataset is being sought. **The ML hygiene genuinely exceeds this entry's grade**, and Section 3 says so in those words.

## 2. Study Snapshot

**Study type:** development and internal validation of a **cross-sectional** machine-learning classifier on retrospective multi-site EHR data. **No prospective component, no external validation, no clinician evaluation, no patient outcome.** The authors state each of these.

**Data.** **Oracle Health Real-World Data**, a United States multi-site de-identified EHR network. Diabetic patients **aged 18 to 65**, identified by ICD-9-CM and ICD-10-CM codes **250.x, E10.x, E11.x**. **DR cases flagged by codes 362.0x, E10.31x–E10.35x, or E11.31x–E11.35x; everyone else classified as control.** After cleaning, merging and imputation: **97,786 unique patients, 16,865 DR (17.25%) and 80,921 non-DR (82.75%).**

**Cohort composition, reported in full.** 57.06% female, 42.91% male, 0.03% unknown. 62.66% Caucasian, 19.71% African American, 7.85% Other, 3.29% Asian, 3.08% Biracial, 1.49% Hispanic, 1.07% Native American, 0.84% Middle Eastern Indian, 0.01% Pacific Islander.

**How the features were chosen.** A PubMed search in **January 2023** — `("diabetic retinopathy") AND (predict OR factor OR determine)`, clinical studies, **1990 to January 2023** — yielding **13,002 articles.** For each article and each candidate variable, a relative term frequency was computed and **multiplied by that article's Relative Citation Ratio** (a field- and time-normalised, article-level citation measure based on the co-citation network rather than the journal). Scores were aggregated across the 13,002 papers, then **z-standardised and passed through the standard normal CDF** to land on a 0-to-1 scale. **The candidate vocabulary was the 24 structured variables the authors already had** — age, glucose, nephropathy, neuropathy, HbA1c, hemoglobin, albumin, creatinine, sodium, calcium, triglyceride, bilirubin, RBC, WBC, AST, chloride, potassium, hematocrit, BUN, ALT, anion gap, MCH, MCHC, MCV.

**The cognitive constraint.** Citing **Miller's 7±2**, an interpretability score was defined as **1 when seven or fewer features are retained, and 7÷x above that.** A composite objective multiplied predictive accuracy by this score, and a modified recursive feature elimination stopped when the change in that composite fell below a preset threshold.

**Experimental design, and it is careful.** A **patient-level stratified random split, 64% / 16% / 20%**, with the test subset **held out from all development** and **the same patient unable to appear in more than one subset.** Before any balancing: **training 62,582 (10,794 DR / 51,788 non-DR), validation 15,646 (2,698 / 12,948), test 19,558 (3,373 / 16,185)** — prevalences **17.25% / 17.24% / 17.25%.** I verified these sum exactly to 97,786 and that each prevalence is correct. **Median imputation and feature scaling were fitted on the training data and applied unchanged downstream. SMOTE was applied only to the training subset, after partitioning** — stated three separate times in the paper. Validation was used for model selection and hyperparameters; **all final metrics come from the untouched test subset.**

**Uncertainty.** **1,000 bootstrap resamples of the test cohort, with replacement at patient level**, used to estimate 95% confidence intervals for accuracy, sensitivity, specificity, PPV, NPV, F1, AUROC and AUPRC. The paper states these intervals "were narrow." **The actual interval values are in a table I could not retrieve, so I cannot report a single one of them.**

**Benchmarking, on identical patients.** Logistic regression (24 variables), XGBoost (24), a multilayer perceptron (24; three hidden layers of 128/64/32, ReLU, Adam, early stopping), an **FT-Transformer** (24; 64-dimensional feature tokens, eight attention heads, three encoder layers, dropout 0.15), and the proposed eight-variable XGBoost. All used the **same training/validation/test patients, same endpoint, same preprocessing pipeline, and the same 0.50 classification threshold.** XGBoost settings: 500 estimators, learning rate 0.03, max depth 4, min child weight 2, subsample 0.85, column subsample 0.85.

**Results on the untouched test set (n = 19,558, prevalence 17.25%).** Proposed eight-feature XGBoost: **accuracy 0.9535, sensitivity 0.9117, specificity 0.9622, PPV 0.8342, NPV 0.9812, F1 0.8712, AUROC 0.9724, AUPRC 0.9455.**

**The comparators.** **XGBoost 24 features: AUROC 0.9750, AUPRC 0.9530. FT-Transformer: 0.9739 / 0.9537. Logistic regression: 0.9713 / 0.9411. MLP: 0.9635 / 0.9375.** The paper notes its model's AUROC is "only 0.0026 lower than that of the 24-feature XGBoost while using one-third as many input variables" — which I verified.

**Prevalence-scenario analysis, and this is good practice.** Holding sensitivity and specificity fixed: **PPV/NPV of 0.5597/0.9952 at 5% prevalence, 0.7285/0.9899 at 10%, and 0.8579/0.9776 at 20%.** I reproduced all six values and all six match to within 0.0003.

**Feature-selection sensitivity, reported with unusual candour.** Literature and data importance were combined as **S = 0.223·L + 0.777·D**, described explicitly as **"a sensitivity boundary, not an optimized hyperparameter"** — specifically **"the most data-dominant configuration examined at which the same eight variables remained within the top-eight selected set."** And a second check: the **RCR-weighted ranking versus the plain unweighted term-frequency ranking agreed at Spearman ρ = 0.98**, which the authors describe as RCR "refin[ing] rather than replac[ing]" the frequency signal.

**Post-hoc explanation.** SHAP. **Creatinine, HbA1c, age and hemoglobin had the largest overall contributions.** Directions as reported: **"Higher creatinine and HbA1c values were associated with increased predicted risk, whereas lower hemoglobin levels and higher age were associated with reduced predicted risk."** In the single-patient waterfall example, **"older age and lower hemoglobin levels contributed most strongly to a reduction in the predicted risk, whereas moderately elevated albumin produced a smaller increase in risk."**

**Limitations the authors state themselves.** **External validation "remains necessary"** and an additional dataset "is currently being pursued." The study is **"based on static, cross-sectional laboratory measurements, which may not fully capture the progression dynamics"** of DR. **XGBoost "is not intrinsically interpretable"** and interpretability here means a concise feature set plus post-hoc attribution, **not transparency of the decision mechanism.** **"Formal clinician-comprehension or trust study was [not] conducted."** The TF-RCR procedure "quantified the prominence of a candidate variable in the literature rather than the direction of an association; therefore, a separate negation-detection step was not applied."

**Not reported:** any calibration assessment — no calibration plot, slope, intercept or Brier score; any temporal separation between the laboratory measurements and the DR diagnosis code (no index date, no washout, no incident-versus-prevalent distinction); how much data was median-imputed and for which variables; whether the nephropathy and neuropathy variables were themselves ICD-coded; diabetes duration or type; IRB or data-use approval; funding; competing interests; any reporting guideline.

## 3. How Strong Is This Evidence? (Grade 2 out of 5)

**This is the most uncomfortable grade in this reading list so far, because the machine-learning hygiene here is better than that of several papers graded higher — and the clinical design has a hole the paper never tests, through which the headline number may largely be flowing.**

**Let me start with what is genuinely well done, because there is a lot of it.**

**The data-handling discipline is close to exemplary.** The split is **patient-level and stratified**, with an explicit guarantee that no patient appears in two subsets. **Imputation and scaling were fitted on training data only.** The test set was **held out from development entirely** and the validation set carried model selection. And **SMOTE was applied only to the training subset after partitioning** — stated three times, with the observed prevalence deliberately preserved in validation and test. That is precisely the error that wrecks a large fraction of imbalanced-data papers, and these authors did not make it.

**Uncertainty was quantified.** 1,000 patient-level bootstrap resamples across eight metrics.

**The benchmarking is better than most papers in this field attempt**, and it is the reason this entry has a clear answer to its own central question. Four comparators — linear, boosted, neural and attention-based — on **identical patients, pipeline and threshold.** The paper even explicitly retired its earlier external comparisons, stating it would avoid "conflating differences in cohort composition, prevalence, preprocessing, and outcome definition across published studies." **That is the right instinct and rarely acted on.**

**The right metrics for an imbalanced problem.** AUPRC alongside AUROC, PPV and NPV, and then a **prevalence-scenario analysis** showing how predictive values move at 5%, 10% and 20%. Every number I checked was correct.

**And the claims are hedged correctly, repeatedly.** The paper refuses to call XGBoost interpretable, defines what it does and does not mean by interpretability, states that clinician trust was never tested, publishes a sensitivity check that undercuts its own named novelty, and declares the absence of external validation. **A team optimising for citations does not write "formal evaluation with clinicians remains necessary" four times.**

**So why 2.**

**Because the study cannot distinguish predicting diabetic retinopathy from detecting that it has already been coded — and the entire clinical case for the paper depends on that distinction.** The stated goal is to "empower primary care physicians to evaluate the risk of DR in their patients, recommend necessary eye exams, and establish tailored screening intervals." That requires seeing a patient **before** the diagnosis. But the design is **cross-sectional by the authors' own description**, with **no index date, no requirement that the laboratory values precede the retinopathy code, no washout, and no separation of incident from prevalent disease.** A patient whose retinopathy was diagnosed in 2019 and whose creatinine was drawn in 2023 is, as far as anything in this paper shows, a "correct prediction."

**And two of the eight predictors are the other two diabetic microvascular complications.** Nephropathy and neuropathy are not independent risk factors in the way a lipid level is. They are **the same disease process in different tissues**, caused by the same duration and severity of hyperglycemia that causes retinopathy, and in this dataset they are **drawn from the same ICD coding in the same records as the label.** Add creatinine, albumin and hemoglobin — the standard laboratory picture of diabetic kidney disease — and **four of the eight features are kidney-related.** A patient coded with diabetic nephropathy and diabetic neuropathy is, almost by construction, someone with long-standing poorly-controlled diabetes who has already been worked up by specialists. **That is not a prediction from routine labs. It is a strong clue that the chart already contains the answer.**

**The flat model comparison is the evidence that something like this is happening.** When logistic regression, gradient boosting, a neural network and an attention transformer all land within **1.15 AUROC points** of each other, the task has almost no non-linear structure left to exploit. **That is the signature of a problem where the label is substantially recoverable from a few inputs by any method** — and it is the single most diagnostic result in the paper. The authors present it as evidence that their compact model is competitive, which is true and is not the most important thing it shows.

**No calibration, anywhere.** Discrimination start to finish, plus PPV and NPV at a fixed 0.50 threshold. This matters more than usual **because SMOTE guarantees miscalibration**: training on an artificially balanced set calibrates the model's probabilities to a 50% prevalence world and then it is deployed in a 17.25% one. Section 5 shows that **a predicted probability of 0.90 from this model corresponds to a true risk of roughly 65%.** The classification still works — the 0.50 cut happens to land near a sensible screening operating point — but **not one predicted probability from this model can be told to a patient**, and nothing in the paper says so.

**Internal validation only**, which the authors state. Multi-site data helps and is not a substitute: the split is random within one data vendor's extract, sharing its coding conventions, its lab platforms and its referral patterns.

**The explanation points the wrong way in two places and the paper does not notice.** Higher age reducing predicted risk, and lower hemoglobin reducing predicted risk, both contradict established DR epidemiology. **Entry 74 of this list established that a stable, biologically correct explanation can sit on a useless model. This is the mirror image: a suspicious explanation sitting on an apparently excellent one** — and the mirror image is the more dangerous of the two, because the performance invites you to trust the explanation.

**No reporting guideline.** TRIPOD+AI covers exactly this study type and would have forced the two things most missing: a calibration assessment and an explicit statement of the prediction horizon.

**Why not 1.** Because nothing here is incompetent or evasive. The pipeline is clean, the arithmetic is flawless, the benchmarking is honest, the comparators are real, and the limitations section names the cross-sectional design, the absent external validation and the absent clinician evaluation. **A grade of 1 in this list is for work whose numbers cannot be trusted at all. These numbers are trustworthy; it is their meaning that is unestablished.**

**Why not 3.** Because the grade tracks what a reader may safely conclude, and the headline invites a conclusion the design cannot support. **"AUROC 0.97 for DR screening from eight routine labs" would, if true, be a significant public-health finding** — and the two things that would establish it are both missing: a temporal design in which the labs precede the diagnosis, and a model that does not use the other two microvascular complications as inputs.

**What would make this a 4, concretely.** Define an **index date** and require every laboratory value to precede it. **Exclude patients with any DR code before the index date** so the outcome is incident. **Drop nephropathy and neuropathy**, or report performance with and without them — that single ablation would answer the central question and the authors already have everything needed to run it. **Add diabetes duration and type**, which would likely fix the inverted age effect. **Report calibration** after a prevalence correction for SMOTE. **Validate externally.** My expectation is that the AUROC would fall substantially — and the resulting paper would be far more valuable, because its number would mean what it says.

## 4. The Editor's Concerns

**1. Nephropathy and neuropathy are not risk factors for retinopathy. They are its siblings.** The three microvascular complications of diabetes — retinopathy, nephropathy, neuropathy — share one cause: cumulative exposure to high blood glucose. They co-occur because of that shared cause, not because one predicts another. Here, **the label and two of the eight features all come from ICD codes in the same patient records**, and three further features (creatinine, albumin, hemoglobin) are the laboratory signature of the nephropathy already included as a code. **The question the model is actually answering is closer to "is the third complication also in this chart?" than to "will this patient develop retinopathy?"** The fix is a one-line ablation the authors can run today: **report AUROC with nephropathy and neuropathy removed.** Until that exists, the contribution of co-coding to 0.9724 is unknown — and it is the first thing any reader should want.

**2. Cross-sectional data cannot support a screening claim, and the paper's framing is a screening claim.** The title says "Screening." The introduction promises to let primary-care physicians "establish tailored screening intervals." The limitations say the study is **"based on static, cross-sectional laboratory measurements."** Those cannot all be right. **There is no index date, no requirement that labs precede the DR code, no washout, and no incident-versus-prevalent distinction** anywhere in the retrieved text. A screening tool is defined by temporal order: it must see the patient before the diagnosis does. **This study demonstrates association between concurrent records, which is a real finding and a different one.**

**3. A plain logistic regression got 0.9713, and that is the most informative number in the paper.** Against the proposed model's 0.9724, the difference is **0.0011.** Across all five models — linear, boosted, neural, attention — the full spread is **1.15 AUROC points**, or about **three percentage points of explained variance.** The authors present this as showing their eight-feature model is competitive. **It also shows that the modelling contributes almost nothing**, which in turn says the task as posed is nearly linearly separable from a handful of inputs. Section 5 teaches this as a general leakage detector. **The honest headline for this paper is not "our framework achieves 0.9724"; it is "eight routine variables recover concurrent DR coding at 0.97 by any method you like, including logistic regression" — and the interesting question is then why.**

**4. No calibration, in a paper that used SMOTE.** The two facts belong together. Balancing the training data to 50/50 and then deploying at 17.25% prevalence **systematically inflates every predicted probability**, by a prior-odds factor I compute as **0.2084**: a model output of 0.90 corresponds to a true risk of about **65%**, and 0.70 to about **33%.** No calibration plot, slope, intercept or Brier score is reported, so **none of this is visible to a reader, and the paper never warns that its probabilities are not risks.** The classification is unaffected, because the 0.50 cut lands near a true risk of 17% — a defensible screening threshold, arrived at by accident. For a tool whose stated purpose is to help a GP decide whom to refer, **the probability is the output that matters**, and it is the one output not validated.

**5. The SHAP directions contradict the epidemiology in two of the four leading features, unremarked.** The paper reports that **higher age lowers predicted risk** and **lower hemoglobin lowers predicted risk.** Retinopathy prevalence rises with age and with diabetes duration; anemia is an established DR risk factor and a marker of diabetic kidney disease. **Both directions are backwards.** The most likely explanation is in the paper's own introduction: nearly all type 1 diabetics develop DR after 20 years, and the cohort is capped at **18–65.** So a 28-year-old carrying DR codes is plausibly long-duration type 1 disease, while a 60-year-old in a primary-care extract is more often recently-diagnosed type 2 without retinopathy. **Diabetes duration and type are not in the model**, and age appears to have been pressed into service as an inverted proxy for them. **That is a classic omitted-variable signature, and it is a finding rather than a footnote** — it says the model has learned a cohort artefact, which is exactly what an external validation would expose.

**6. The explanation is being offered for a model whose correctness is unestablished — and this list settled that question three weeks ago.** Entry 73 argued that explanation plausibility is not validation; **entry 74 demonstrated it**, with a rectal-dose feature that ranked first in all 25 repeats, with the right sign and established biology, on a model with an AUROC of 0.587. **Entry 77 is the inverse case and the more hazardous one.** Here the performance is superb and two of the four leading explanations are implausible. **A reader who trusts the SHAP plot because the AUROC is 0.97 has the inference exactly backwards:** the implausible explanation is evidence against the model's construct validity, not a curiosity to be explained away by the performance.

**7. The named novelty barely does anything, and the authors say so.** TF-RCR's distinguishing ingredient is the Relative Citation Ratio weighting. Their own sensitivity check: **the RCR-weighted ranking and the plain unweighted term-frequency ranking agree at Spearman ρ = 0.98.** They describe this as RCR "refin[ing] rather than replac[ing]" the frequency signal, which is a fair gloss on ρ = 0.98 and also means **the citation weighting is close to decorative.** **Reporting it anyway is a genuine credit** — most authors would have left this check out — and a reader should know that "TF-RCR" is, operationally, counting how often a variable is mentioned.

**8. The literature procedure ranked a list the authors already had.** The candidate vocabulary for TF-RCR **was the 24 structured variables already in the dataset.** So the 13,002-article corpus did not discover a variable, propose one the authors lacked, or rule one out; it **ordered a predetermined shortlist.** That is a legitimate use and much weaker than "incorporating medical domain knowledge" suggests. Compounding it, the authors note that TF-RCR measures **prominence, not direction, with no negation detection** — so a variable repeatedly reported as **not** associated with DR scores highly. Stated honestly, and it means the literature signal is "how much is this discussed," not "how much does this matter."

**9. The weighting that makes the framework work was chosen as the boundary where the answer survives.** The literature/data blend is **22.3% / 77.7%**, described as **"the most data-dominant configuration examined at which the same eight variables remained within the top-eight selected set."** Read carefully, that says: **push past 77.7% data weighting and the feature set changes.** So at least 22.3% literature weight is *required* to retain these eight features — which is a weaker claim than "literature and data agree," and is close to the opposite of how the stability result reads at first pass. **The authors reported the boundary rather than hiding it, which is to their credit**, and a reader needs to notice which direction it points.

**10. The final model fails the interpretability criterion the paper built.** The score is **1 for seven or fewer features and 7÷x above that**, derived from Miller's 7±2. The final model uses **eight**, scoring **0.875** — a self-imposed 12.5% penalty. Minor, and worth noting because the cognitive-limit argument is load-bearing in the paper's framing: the entire case for eight features rather than 24 rests on a threshold the model then exceeds by one. **Nothing turns on it numerically**, but a criterion that the preferred model does not meet is doing rhetorical rather than analytic work.

**11. Three authors, all from industrial engineering, and no clinical co-author is apparent.** This is not a criticism of competence — the ML engineering is better than that in several clinically-authored papers in this list. But **concerns 1, 2 and 5 are all clinical-domain errors rather than statistical ones**: that the microvascular complications are one disease, that screening requires temporal order, that anemia and age point the other way in DR. A retinopathy specialist or diabetologist reading a draft would likely have flagged all three. **The paper's own stated motivation for mining PubMed was that clinicians are too busy to consult** — and this entry is a demonstration of what consulting one buys that a literature corpus does not.

**12. No reporting guideline, now the seventh consecutive entry.** Entry 69 named TRIPOD+AI and deposited the checklist. Entry 70 named STROBE. Entry 71 named none. Entry 73 named none and called for a checklist that does not exist. Entry 74 named none while doing more of what TRIPOD+AI asks than any of them. Entry 75 named none while running the best multiplicity treatment in this list. Entry 76 measured the whole phenomenon and put a number on it: **40% mean completeness against the instrument written for the job.** **Entry 77 names none, and is the first entry in weeks where naming one would have changed the paper** — TRIPOD+AI requires a calibration assessment and an explicit prediction horizon, the two gaps that drive this grade from a 4 to a 2. **So the sequence now has both halves: six entries showing the checklist does not predict quality, and one showing where it would have helped.** Read the methods — and when something is missing, the checklist tells you what to look for.

## 5. Statistics Spotlight

Three concepts, numbered from 273 in the running list in `queue.md`. The first is the load-bearing one and this paper is an unusually clean example of it.

**When every model from logistic regression to a transformer performs the same, the information is in the data, not the method — and that is a leakage detector.**

The authors did the right thing and benchmarked five models on identical patients, identical preprocessing and an identical threshold. Here is the whole result:

- **Logistic regression (24 variables): AUROC 0.9713**
- **Multilayer perceptron (24): 0.9635**
- **FT-Transformer, attention-based (24): 0.9739**
- **XGBoost (24): 0.9750**
- **Proposed XGBoost (8): 0.9724**

**The total spread is 1.15 AUROC points.** A linear model with no interactions is **0.0011** from the proposed model and **0.0037** from the best one.

**Why this is so informative.** Different model families succeed by exploiting different structure. Logistic regression can only add up weighted inputs. Gradient boosting finds thresholds and interactions. A neural network finds smooth non-linear combinations. An attention transformer learns which features to look at depending on the others. **If all four land in the same place, there is almost no interaction structure and almost no non-linearity to find** — the outcome is close to a weighted sum of a few inputs.

**Converting to something more intuitive.** Using the variance conversion from technique 224 (turn AUROC into an equivalent separation, then into a correlation, then square it), the five models explain between **about 62% and 66% of the variance** in the outcome. **The entire contribution of model architecture — from a linear equation to a transformer — is roughly three percentage points of variance.** Everything else, the other sixty-odd points, comes from the features and the labels.

**And that is when you go and look at the features and the labels.** Here: the outcome is an **ICD code for diabetic retinopathy**, and two of the eight inputs are **ICD codes for diabetic nephropathy and diabetic neuropathy** — the other two members of the same microvascular triad — plus three laboratory markers of the kidney disease already coded. **Four of eight features are kidney-related.** A problem that is trivially easy for every method is usually easy for a reason, and "the answer is partly already in the inputs" is the most common reason.

**The worked contrast, because this reading list has the perfect comparison.** Three days ago, **entry 74** predicted late radiotherapy toxicity and got **AUROC 0.587 — about 2.4% of variance.** This paper gets **64.8%**, **twenty-seven times more.** The tempting conclusion is that this is twenty-seven times the study. **The real difference is the question.** Entry 74 predicted an event that had not yet happened, from data recorded before treatment, with a permutation test that re-ran its entire pipeline a thousand times. Entry 77 identifies a diagnosis code from records that may have been written at the same time, using two closely related diagnosis codes as inputs. **One is prediction. The other may be recognition. The AUROC cannot tell them apart, which is exactly why the number alone is not the finding.**

**The everyday version.** You build a model to predict whether someone owns an umbrella. Simple version: a logistic regression on two inputs — does the person own a raincoat, and do they own wellington boots. It scores 97%. You then try gradient boosting, a neural network and a transformer. **They all score 97%.** At that point the right reaction is not "my simple model is impressively competitive." It is: **raincoats, wellingtons and umbrellas are all bought by people who live somewhere rainy.** You have not learned to predict umbrella ownership. You have learned that wet-weather gear comes in sets.

**Watch out for:** a model-comparison table where everything from the simplest baseline to the fanciest architecture lands within a point or two, presented as evidence that the chosen model is efficient. **It is that, and it is also a signal to audit the inputs.** Two questions: **could the label have been produced by the same process that produced any input** — the same coder, the same visit, the same chart? And **is any input downstream of, or a sibling of, the outcome** rather than upstream of it? A flat model zoo on a hard-sounding clinical problem is one of the cheapest leakage tests available, and it needs no extra analysis — just a table most papers already have.

**SMOTE calibrates your probabilities to a prevalence that does not exist.**

This paper did the hard part of SMOTE correctly, and it is worth saying first. **SMOTE — Synthetic Minority Over-sampling Technique — creates artificial examples of the rare class** so a model is not overwhelmed by the common one. The catastrophic mistake is applying it *before* splitting the data, which copies minority patients across the train/test boundary and inflates everything. **These authors applied SMOTE only to the training subset, after partitioning, and preserved the real 17.25% prevalence in validation and test.** They say so three times. That is correct and many papers get it wrong.

**But there is a second consequence, and it is not addressed.** After SMOTE, the training set is roughly **50% DR / 50% non-DR.** The model learns probabilities appropriate to a world where retinopathy affects half of diabetics. **It is then deployed in a world where 17.25% do.** Every predicted probability comes out too high.

**The correction is simple arithmetic.** Convert to odds, multiply by the ratio of the true prior odds to the training prior odds, convert back. True prior odds are 0.1725 ÷ 0.8275 = 0.2085; training prior odds are 1.0; so the correction factor is **0.2084**. Applying it:

- the model says **0.50** → true risk about **17%**
- the model says **0.70** → true risk about **33%**
- the model says **0.90** → true risk about **65%**

**So a patient the model scores at 90% has roughly a two-in-three chance, not a nine-in-ten chance.**

**Two things follow, and they pull in opposite directions.** The **classification is fine** — in fact the 0.50 threshold corresponds to a true risk of about 17%, which is a perfectly sensible place to set a screening cut-off, so the reported sensitivity and specificity stand. But **the probabilities are unusable as risks**, and the paper's stated purpose — helping a physician "evaluate the risk" and set "tailored screening intervals" — is precisely a use of the probability rather than the label. **No calibration plot, calibration slope, intercept or Brier score appears anywhere**, so a reader has no way to see this.

**The everyday version.** You learn to judge whether it will rain by training in Scotland in November, where it rains half the time. You move to Arizona. Your sense of "it's about even money today" is still perfectly ordered — the days you call wettest really are the wettest — **but every single one of your probabilities is far too high**, and you will pack an umbrella constantly. Your *ranking* transferred. Your *numbers* did not.

**Watch out for:** any paper that uses SMOTE, class weighting, undersampling or any rebalancing, then reports probabilities or a risk score **without reporting calibration.** Discrimination (AUROC, AUPRC) is untouched by rebalancing because it only depends on ranking. **Calibration is destroyed by it.** Two questions: was the balancing applied after the split, and was the output recalibrated to the real prevalence? **The first question is the one everyone asks. The second is the one that matters once the first is answered correctly** — and the clue is that the paper reports eight discrimination and classification metrics and not one calibration metric.

**Positive predictive value is not a property of a model; it is a property of a model plus a population — and these authors showed it properly.**

This is the practice worth copying from this paper. Sensitivity and specificity describe the test. **PPV and NPV describe what a result means for a patient, and they move with how common the disease is**, even when the test itself has not changed at all.

The authors held their sensitivity (0.9117) and specificity (0.9622) fixed and recalculated across prevalences. I reproduced all six values; every one matches:

- **At 5% prevalence: PPV 0.5597, NPV 0.9952**
- **At 10%: PPV 0.7285, NPV 0.9899**
- **At 17.25% (their cohort): PPV 0.8342, NPV 0.9812**
- **At 20%: PPV 0.8579, NPV 0.9776**

**Read the first line again.** In a population where 5% of diabetics have retinopathy, **a positive result from this model is wrong about 44% of the time** — nearly half the people flagged for an eye referral would not have DR. The model has not changed. The AUROC is still 0.9724. **Only the population changed.**

**Why it happens, in one sentence.** As disease gets rarer, there are more and more healthy people available to generate false positives, and fewer sick people to generate true ones — so the false positives come to dominate the "positive" column.

**A tiny worked example.** Take 1,000 diabetic patients at 5% prevalence: **50 with DR, 950 without.** This model catches 91.17% of the 50 → **46 true positives.** It wrongly flags 3.78% of the 950 → **36 false positives.** So 82 people are flagged and **46 of them have DR: 46 ÷ 82 = 56%.** Now run it at 20% prevalence: **200 with DR, 800 without** → 182 true positives and 30 false positives → **182 ÷ 212 = 86%.** **The same test, the same numbers, two very different letters to send a patient.**

**Why it matters specifically here.** The authors' own motivating statistic is that **only 43% of diabetics get their annual eye exam**, and the cohort prevalence of 17.25% comes from a diagnosed, coded hospital-network population. **A primary-care screening population — the intended deployment — would plausibly have a lower prevalence of recognised DR**, which pushes PPV toward the 56% end. For a referral tool that is still potentially useful, but "we flag the right patient 83% of the time" and "we flag the right patient 56% of the time" are different products.

**Watch out for:** PPV, NPV or "precision" quoted as though they were fixed properties of a model, especially from a study whose cohort prevalence differs from the deployment setting. **Ask two things: what was the prevalence in the test set, and what will it be where this is used?** Then recompute — the formula needs only sensitivity, specificity and prevalence, and takes thirty seconds. **And give this paper credit: it did the recomputation itself, unprompted, which almost nothing in this reading list has done.**

## 6. Jargon Translator

**Diabetic retinopathy (DR)** — damage to the small blood vessels at the back of the eye caused by diabetes. The leading cause of blindness in American adults. **Treatable, but vision already lost does not come back**, which is why early detection is the whole game.

**The diabetic microvascular triad** — retinopathy (eye), nephropathy (kidney) and neuropathy (nerve). **Three expressions of one underlying process**: cumulative damage to small blood vessels from high blood glucose. They tend to appear together because they share a cause — central to concern 1.

**ICD-9-CM / ICD-10-CM codes** — the standard system for recording diagnoses in medical records, used for billing and statistics. Both the outcome and two predictors here are ICD codes.

**Cross-sectional** — everything measured at one point in time, with no before-and-after. **The opposite of what a prediction study needs**, and the authors state their study is cross-sectional.

**Index date** — in a properly designed prediction study, the moment from which you predict. Everything used as input must come before it; the outcome must come after. **Not defined in this paper.**

**Incident vs prevalent disease** — newly developed versus already present. A screening tool must find incident cases; a model trained on prevalent ones may only be recognising what is already known.

**HbA1c** — a blood test reflecting average blood glucose over roughly the previous three months. The standard measure of diabetes control.

**Creatinine / albumin / BUN** — blood markers of kidney function. Together with hemoglobin (anemia is common in kidney disease), **the standard laboratory picture of diabetic nephropathy.**

**XGBoost** — "extreme gradient boosting," a method that builds many small decision trees in sequence, each correcting the last. Usually the strongest performer on tabular data. **Not interpretable by itself**, as this paper repeatedly says.

**Logistic regression** — the simplest respectable approach: multiply each input by a weight and add them up. **Here it scored 0.9713 against the proposed model's 0.9724** — technique 273.

**Multilayer perceptron (MLP)** — a basic neural network; here three hidden layers of 128, 64 and 32 units.

**FT-Transformer** — a transformer (the attention-based architecture behind modern language models) adapted to spreadsheet-style data, learning which features to attend to depending on the others. Scored 0.9739.

**AUROC** — the chance the model scores a randomly chosen patient with DR above a randomly chosen patient without it. 0.5 is a coin flip, 1.0 is perfect. **Measures ranking only; says nothing about whether the predicted probabilities are right.**

**AUPRC** — area under the precision-recall curve. More informative than AUROC when the outcome is rare, because its baseline is the prevalence (here 17.25%), not 0.5. Reported at 0.9455.

**Sensitivity / specificity** — the share of DR cases correctly flagged (0.9117) and the share of non-DR correctly cleared (0.9622). **Properties of the test.**

**PPV / NPV** — given a positive or negative result, the chance it is right. **Properties of the test *and* the population** — technique 275.

**F1-score** — the harmonic mean of PPV and sensitivity, used as a single summary when the classes are imbalanced. Here 0.8712.

**Calibration** — whether a predicted 70% risk corresponds to 70% of such patients having the disease. **Separate from discrimination, and not reported here** — technique 274.

**SMOTE** — Synthetic Minority Over-sampling Technique: manufactures artificial examples of the rare class to balance the training data. **Applied correctly here (training only, after the split), and it still distorts the output probabilities** — technique 274.

**Bootstrap confidence interval** — resample the test set with replacement many times (1,000 here) and see how much the metric moves. A way to express uncertainty without new patients.

**SHAP (SHapley Additive exPlanations)** — a method that assigns each feature a credit or blame for an individual prediction. **A description of what the model did, not evidence that the model is right** — entry 74, technique 249.

**Post-hoc explanation** — an explanation produced after the fact by a separate tool, as opposed to a model that is transparent in itself. **This paper is admirably insistent on the distinction.**

**Relative Citation Ratio (RCR)** — an article-level citation measure normalised for field and publication year using the paper's co-citation network. Used here to weight literature mentions; **agreed with unweighted counting at Spearman ρ = 0.98.**

**Spearman ρ** — correlation between two rankings rather than two values. 0.98 means the two orderings are nearly identical.

**Recursive feature elimination (RFE)** — repeatedly drop the least useful feature and retrain, until a stopping rule fires.

**Miller's 7±2** — a 1956 finding that people can hold about seven items in working memory. Used here as a design cap on the number of model inputs.

## 7. What You Can (and Can't) Say

**You can say:**

"In a 97,786-patient multi-site US EHR cohort, eight routinely collected variables — age, glucose, nephropathy, neuropathy, HbA1c, hemoglobin, albumin and creatinine — identified patients coded with diabetic retinopathy with an AUROC of 0.9724 on a held-out test set of 19,558 patients at the observed 17.25% prevalence."

"The study's data handling was careful: a patient-level stratified split with no patient in two subsets, imputation and scaling fitted on training data only, SMOTE applied only to the training subset after partitioning, the observed prevalence preserved in validation and test, and 1,000 patient-level bootstrap resamples for uncertainty."

"Benchmarked on identical patients, an eight-feature model performed comparably to a 24-feature XGBoost (0.9750), an FT-Transformer (0.9739), a logistic regression (0.9713) and an MLP (0.9635)."

"The authors reported PPV and NPV across prevalence scenarios, showing PPV falls from 0.8579 at 20% prevalence to 0.5597 at 5%."

"The authors state that external validation has not been performed, that the study is cross-sectional, that XGBoost is not intrinsically interpretable, and that no clinician comprehension or trust evaluation was conducted."

**You cannot say:**

"Routine blood tests can screen for diabetic retinopathy at 97% accuracy." **The study is cross-sectional with no index date**, so nothing establishes that the laboratory values preceded the diagnosis. This is a statement about concurrent association, not screening.

"This model predicts who will develop diabetic retinopathy." **No prediction horizon exists.** No washout, no incident-case definition, no requirement of temporal order.

"Eight routine labs are enough to find retinopathy." **Two of the eight are diagnosis codes for the other two diabetic microvascular complications**, drawn from the same records as the outcome, and three more are the laboratory signature of the kidney disease already coded. The ablation that would separate these contributions was not run.

"The gradient-boosting approach outperformed simpler methods." **A logistic regression scored 0.9713 against 0.9724** — a difference of 0.0011. Across all five models the spread is 1.15 AUROC points.

"The model can tell a patient their risk is 90%." **SMOTE-trained probabilities are calibrated to a 50% prevalence world and deployed at 17.25%**; a model output of 0.90 corresponds to a true risk of roughly 65%. **No calibration was assessed.**

"SHAP showed the model uses clinically sensible features." **Two of the four leading features point the wrong way** — higher age and lower hemoglobin both *reduced* predicted risk, against established DR epidemiology.

"Medical domain knowledge was incorporated from the literature." **The 13,002-article corpus ranked the 24 variables the authors already had**; it discovered none, and the procedure measured how often a variable is discussed, not whether the association was positive, negative or null.

"Citation-weighted literature mining improved feature selection." **The authors' own check puts the RCR-weighted and unweighted rankings at Spearman ρ = 0.98.**

"The model is interpretable." **The paper explicitly declines to claim this**, more than once, and the claim should not be made on its behalf.

"This generalises across institutions." **Internal validation only**, within one data vendor's extract. The authors say external validation "remains necessary."

**The honest one-sentence version:** *a careful, well-engineered, arithmetically flawless study showing that eight variables recover a concurrent diabetic-retinopathy diagnosis code at AUROC 0.97 by any modelling method you care to use including plain logistic regression — which, together with the fact that two of those variables are diagnosis codes for the other two diabetic microvascular complications and the design never requires the labs to precede the diagnosis, means the number is solid and its interpretation as a screening result is not yet established.*

## 8. Bottom Line for Your Life

**If you have diabetes:** the underlying clinical message in this paper's introduction is the part worth keeping, and it does not depend on the model. **Only about 43% of diabetic patients get their recommended annual eye exam, early retinopathy has no symptoms, and vision already lost cannot be recovered.** If you have diabetes and have not had a dilated eye exam in the past year, **that is the actionable item here** — not anything about blood tests. No model in this paper replaces looking at the retina.

**If you are a primary care physician:** this is not yet a tool, and the authors agree — they state that external validation and clinician evaluation both remain to be done. **What the paper does usefully confirm is clinical common sense: a diabetic patient who already carries nephropathy and neuropathy codes, with a rising creatinine and a high HbA1c, is at high risk for retinopathy and should be in an eye clinic.** You did not need a transformer to know that, which is rather the point of technique 273.

**If you build or buy clinical prediction models, this entry is a checklist of four questions.** **Does every input predate the outcome, with a defined index date?** **Is any input a sibling or a consequence of the outcome rather than a cause or precursor** — another complication of the same disease, a treatment for it, a referral generated by it? **If the data were rebalanced, was calibration reported afterwards?** And **does a logistic regression do just as well?** That last one costs an hour and tells you more about your problem than another month of architecture search. **If the answer is yes, you have learned something important about your data, not a disappointment about your model.**

**If someone shows you an AUROC above 0.95 on a clinical problem:** treat it as a question rather than a result. Genuine clinical prediction is hard — **three days before this entry, this reading list analysed a methodologically exemplary study that predicted radiotherapy toxicity at AUROC 0.587, about 2.4% of the variance.** An AUROC of 0.97 is **twenty-seven times more variance explained**, and the usual explanation is not twenty-seven times the insight. **It is that the question has quietly changed** — from predicting the future to recognising the present, or from finding disease to finding the paperwork that disease generates. **Ask what the model would have known at the moment it was supposed to be useful.**

**If you are reading the coverage:** expect "AI spots diabetic eye disease from a routine blood test." The study is real, the engineering is sound, and the number is correctly computed. The three things that will not be in the headline are that **a plain logistic regression matched it**, that **two of the eight inputs are diagnosis codes for the other two complications of the same disease**, and that **nothing in the design requires the blood test to have come before the diagnosis.**

**This is education, not medical advice.** Nothing here should change anyone's diabetes care or eye-screening schedule. **If you have diabetes, the recommendation that matters is the one your own clinician will give you: get the annual dilated eye exam.**

---

## Appendix: verification, deferred papers, and shelf status on 2026-11-14

**Pre-registered questions, both answered.** This pick was set on 2026-11-11 as the deliberate contrast with entry 74 and carried two questions written down **before** the paper was read. **(1) "Could the label be inside the inputs?"** — the abstract confirmed the premise immediately (nephropathy and neuropathy are two of the eight features) and the full text sharpened it: **the DR label is an ICD code, the two comorbidities are comorbidity variables from the same records, and three further features are the laboratory signature of the nephropathy already coded — four of eight features kidney-related.** The design is **cross-sectional by the authors' own statement**, with no index date, no washout and no incident-case definition. **(2) "Against what baseline is 0.972 being called good?"** — answered decisively by the paper's own §4.4: **logistic regression 0.9713**, within **0.0011** of the proposed model, with the full five-model spread at **1.15 AUROC points**. Recording that both questions were posed in advance and both were answered from the paper's own numbers.

**Arithmetic verified today, every check passing.** Cohort and split counts close exactly (**62,582 + 15,646 + 19,558 = 97,786**; **3,373 + 16,185 = 19,558**), with prevalences 17.25% / 17.24% / 17.25% as stated. **The entire confusion matrix rebuilt from sensitivity, specificity and prevalence alone reproduces all four derived metrics** — accuracy 0.95349 vs 0.9535, PPV 0.83407 vs 0.8342, NPV 0.98123 vs 0.9812, F1 0.87116 vs 0.8712. **All six prevalence-scenario PPV/NPV values reproduce** to within 0.0003. The stated 0.0026 gap to the 24-feature XGBoost confirmed. Variance conversions via technique 224: the five models span **61.6%–65.8%**, against entry 74's **2.4%** — a **27-fold** ratio. SMOTE prior-odds correction factor **0.2084**, giving true risks of ~17% / ~33% / ~65% for model outputs of 0.50 / 0.70 / 0.90. HCCL at eight features **0.875**. **No arithmetic error of any kind was found in this paper** — its internal consistency is the best in recent entries, which is precisely why the grade turns on design rather than on execution.

**What could not be verified.** **All figures and tables**, which costs the **bootstrap 95% confidence-interval values** specifically — the procedure is described (1,000 patient-level resamples, eight metrics) and the paper says the intervals "were narrow," but **not one interval value is reportable.** Also absent from the retrieved text: any calibration assessment; any temporal separation between labs and diagnosis; the extent of median imputation; whether nephropathy and neuropathy were themselves ICD-coded (stated only as "comorbidity variables"); diabetes duration and type; IRB or data-use approval; funding; competing interests; any reporting guideline. **Nothing was reproduced that was not seen.**

**Deferred status, 2026-11-14.** ***Annals* *Choosing Wisely* (42896192) — day 25**, weekly re-check due 2026-11-19, **abstract-only date 2026-11-19** — five days out, and the next scheduled fallback; standing note that its 5.4% / 0.6–12.2% CI is a clustering signature computed across 15 recommendations rather than 4,050 responses. **Gait foundation model (42995231) — day 6**, abstract-only date **2026-11-30**; it carries the largest multiplicity problem this list will have faced (**1,887 of 3,210 tested phenotypes called significant**) and the first question for it is what false-discovery-rate procedure ran across those 3,210 tests. Both were re-checked on 2026-11-13 with no PMC copy; **re-checks resume on schedule rather than daily, since neither is near its threshold.**

**Landmark check, 2026-11-07 → 11-14.** Three records, all previously assessed: the NEJM mass-surveillance Perspective (43001754), the *Nature Medicine* gait commentary (43003904), and the gait foundation model itself (42995231). **No new candidates; none displaces the queue.**

**Plan set on 2026-11-14.** **Next run takes shelf item (D)**, the glaucoma visual-field prediction model with **external validation on two separate OCT devices** (PMID 42997014, PMC13740841), **because today's entry makes it the sharpest available follow-up.** Entry 77's two decisive weaknesses are **internal validation only** and **a feature set that may contain its own label**; item (D) is the one paper on the shelf that was **validated on data from different hardware**, which is the strongest form of external validation in imaging-adjacent work and directly tests what entry 77 could not. **The first question for (D):** did performance drop between the two devices, and by how much — because **a model that holds up across two acquisition platforms has answered the question entry 77 left open**, and one that collapses has shown why entry 77's 0.9724 should not be assumed to travel. **Carry forward technique 275 as well:** check what prevalence (D) reports and what its PPV would be in a screening population. **Shelf after today: four spares — (B) bone-tumour reference-standard review, (D) next, (E) MIBC pCR with 102 models screened, (F) bitewing mannequin-only.**

**Standing watch item:** PM Heart trial results (protocol PMID 42893738), quarterly.
