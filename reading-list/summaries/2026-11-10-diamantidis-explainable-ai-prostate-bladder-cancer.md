# Explainable artificial intelligence in prostate and bladder cancer: A review of imaging, digital pathology, molecular profiling, and clinical data

**Authors:** Diamantidis D, Tsakaldimis G, Smyrlis N, Chousein C, Kafalis C, Foutzitzi K, Deligeorgiou E, Panagiotopoulos N, Lailisidis S, Georgellis C, Giannopoulos S, Giannakopoulos S, Kalaitzis C (**thirteen authors, all from one institution** — Department of Urology, Democritus University of Thrace, Alexandroupolis, Greece, with the Endoscopy Unit and the Department of Pathology of the same university.)
**Journal:** Current Urology, 2026; 20(6): 332–348
**Decoded:** 2026-11-10

**Analysis basis:** **FULL TEXT** (retrieved from PubMed Central, PMC13719121) — the complete Introduction, Materials and Methods with both verbatim search strings, the full Conceptual Framework, all four modality sections, the Discussion, Limitations, Future Directions, Conclusions, Acknowledgments, Ethics, Conflict of Interest, Funding, Author Contributions, Data Availability and Statement of AI Use. **The five study-extraction tables did come through the extraction but flattened to one cell per line with the row structure lost** — so individual study rows are readable while a reliable tally across all 70 studies is not, and Section 4 says exactly which number I therefore refuse to report. **Figures 1 and 2 are not viewable**, though their detailed captions extracted in full and are summarised below.

**Source links (verified):**
- DOI: https://doi.org/10.1097/CU9.0000000000000367
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42960345/
- Full text used: https://pmc.ncbi.nlm.nih.gov/articles/PMC13719121/

**Basis of link verification.** Direct URL fetching is blocked from this session (`doi.org` does not resolve under the network policy here), so verification was done against the live PubMed/NLM record. According to PubMed, a query for PMID 42960345 returned this exact title, these thirteen authors with these affiliations, *Current Urology* volume 20 issue 6 pages 332–348, DOI `10.1097/CU9.0000000000000367`, publisher identifier `Curr-Urol-25-0320` and PMC ID `PMC13719121`; the full text was then retrieved from PubMed Central by that PMC ID and matches the record. Both halves of the chain were confirmed independently.

**Funding: "None."** **Conflict of interest: "The authors declare no conflicts of interest."** **Acknowledgments: "None."** Ethics: "Not applicable." Data availability: from the corresponding author on reasonable request. **All five statements are present and explicit**, which after yesterday's entry — where the whole block was missing from the extraction — is worth noting as a contrast.

**Statement of AI use: declared.** "During the preparation of this work, the authors used generative AI (**ChatGPT, GPT-5.2 and GPT-5.5, OpenAI**) and **Grammarly** to assist with language editing and wording refinement," with the authors reviewing, editing and taking full responsibility. **This is the third paper in this reading list to disclose generative-AI writing assistance**, and Section 4 records the short sequence.

**Reporting guideline: none, and the review explains why** — it is a **narrative review supported by a structured search**, chosen deliberately "because of the methodological heterogeneity of the included studies, the diversity of outcome definitions and XAI methods, and the absence of a common effect measure suitable for pooled analysis." **No risk-of-bias tool was applied**, and the review states that too.

---

## 1. The Gist

**This review is about a problem one layer up from the ones this list usually decodes: not whether a model is accurate, but whether its *explanation* can be trusted.**

The pitch for explainable AI is intuitive. A model says "this bladder tumour is muscle-invasive"; a clinician reasonably wants to know *why*. So the field bolts on tools that answer: **SHAP** ranks which variables drove a prediction, **Grad-CAM** paints a heatmap over the part of the image the network attended to. The heatmap lands on the tumour, the clinician nods, trust is established.

**This review's central argument is that the nod is doing no work.**

**The distinction that organises everything.** There are two fundamentally different things called explainability. **Post hoc** methods are applied *after* a black-box model is trained and produce an **approximation** of what it did. **Interpretable-by-design** (or "glass-box") models have transparency built into their structure, so the explanation *is* the model. In the review's words, the difference "determines whether an explanation is an auditable property of the model or an external approximation that may not faithfully represent the model's actual reasoning." **Post hoc dominates the literature; by-design is a small minority.**

**And the sentence that should change how you look at heatmaps.** "Saliency maps can appear anatomically plausible while remaining weakly coupled to the model's true decision process. These maps can also be unstable under minor input perturbations." Therefore: **"visual agreement between a heatmap and anatomical expectations should not, by itself, be considered confirmation that the model is reasoning correctly."** A heatmap over the tumour is compatible with a model that found the tumour *and* with a model that found the scanner.

**Then the number.** The review included **70 studies**. **One** of them ran a reader study — an actual test of whether clinicians behaved differently with explanations than without. **One out of seventy.** "All other studies treated XAI as a technical reporting requirement." And prospective or randomised comparisons of explainable against conventional workflows were **absent across all modalities** — zero of seventy.

**What makes that gap sting is what the single reader study found.** XAI overlays let **non-expert radiologists reach expert-level accuracy on the genuinely ambiguous PI-RADS 3 lesions, while halving reading time.** So explanation design can matter enormously. Sixty-nine studies simply never checked.

**The review's verdict on the field's workhorse is precise and worth quoting.** SHAP "values quantify associations between features and predictions **within a model's learned representation.** They do not establish causality and inherit any biases or confounders embedded in the training data." Which means that when SHAP tells you T stage mattered most, you have learned something about the model, not about cancer — and Section 5 shows why that is weaker evidence than it feels.

## 2. Study Snapshot

**Type:** a **narrative review supported by a structured literature search**, explicitly not a systematic review, with the reason given. **No meta-analysis, no pooled estimate, no risk-of-bias scoring.**

**Search, reported unusually well.** **Two parallel structured searches of PubMed/MEDLINE, one per cancer, both covering records up to 15 November 2025.** The bladder string is given verbatim: `("artificial intelligence" OR "machine learning" OR "deep learning" OR "neural network" OR "AI model" OR "radiomics" OR "radiogenomics") AND ("explainable AI" OR "explainable artificial intelligence" OR XAI OR "interpretable AI" OR "interpretability" OR "explainability" OR "saliency map" OR "Grad-CAM" OR "LIME" OR "SHAP" OR "feature importance") AND ("bladder cancer" OR "urothelial carcinoma" OR "bladder neoplasm" OR "transitional cell carcinoma")`, with an equivalent prostate string substituting the disease filter. **Reference lists of included articles and key urology-AI reviews were also screened.**

**Eligibility.** Studies had to enrol patients with prostate or bladder cancer, develop or evaluate a machine- or deep-learning model for a defined clinical or translational task, **and include an explicit explainability component.** Explainability counted as a recognised post hoc method (SHAP, LIME, Grad-CAM, saliency maps, attention visualisations), an inherently interpretable architecture, or a described strategy rendering behaviour interpretable. **Excluded:** editorials, letters, reviews without original data, purely technical studies not applied to patient data, and — notably — **"studies in which explainability was mentioned superficially without a specific method and corresponding results."** No language restriction, though all included studies were in English.

**Data charting:** cancer type, data modality, clinical task, model family, **explainability method and scope**, primary performance metrics when reported, and **validation type**, extracted for every study into five tables. **"No risk-of-bias tool was applied because of the exploratory and heterogeneous nature of the included literature."**

**Yield: 70 studies across 4 data domains.** Imaging was the most active. **The number of records retrieved or screened is not reported**, and Section 4 treats that as a real gap.

**The conceptual framework — the most valuable part of the paper.**

*Post hoc explainability.* SHAP and LIME give feature attributions for tabular data; Grad-CAM and saliency methods highlight image regions. These "account for the vast majority of XAI implementations." Their principal limitation: **they produce approximations rather than direct readouts of model logic**, can look plausible while being weakly coupled to the real decision process, and can be **unstable under minor input perturbations.** The review names the three things required before a post hoc explanation can be used with clinical confidence: **perturbation tests, prediction–saliency coupling metrics, and concordance with expert annotations.**

*Interpretable-by-design.* Additive and generalised additive models produce per-predictor effect curves a clinician can read directly, and the review notes that **generalised additive models with selected pairwise interactions "can achieve accuracy comparable to that of fully complex black-box models while remaining fully visualizable"** — well suited to PSA, age, stage and grade. **Concept bottleneck models** force predictions through a layer of human-defined clinical concepts (PI-RADS components, grade group, lymphovascular invasion) so clinicians can inspect and intervene at concept level. **Prototype-based networks** classify by comparison with a learned library of representative patches, explaining as "this region resembles these prototypical examples of high-grade disease" — which the review observes "directly parallels visual reasoning in pathology."

*The exemplar.* The review's "most consequential urological glass-box example" is a **biologically structured deep neural network whose topology was constrained to follow known pathway–gene hierarchies in prostate cancer.** High-attribution nodes corresponded to established prostate cancer genes and pathways including androgen receptor and PTEN, **"making the structure itself the explanation"** — and it produced an experimentally identified and validated therapeutic target. The review's framing: architectural constraints can "move XAI from plausibility toward mechanism."

*Human-centred interpretability.* The review invokes **causability and the System Causability Scale**, and makes a point rarely made: **"A technically faithful but poorly framed output—for example, a high-dimensional SHAP plot containing dozens of unlabeled features—may provide less usable guidance than a simpler risk summary that maps onto established urological decision frameworks."**

*Reliability of explanations.* "Explanations themselves require validation." For imaging: perturbation tests, prediction–saliency coupling, concordance with expert annotations. For structured data: **stability across resampling and retraining.** And on transformers: **"Attention mechanisms ... should not be assumed to be faithful without dedicated reliability testing."**

**Findings by domain, as summarised in the prose.** *Imaging* is the most active domain, spanning multiparametric MRI in prostate cancer, CT and dual-energy CT in bladder cancer, and endoscopy during cystoscopy and TURBT; Grad-CAM, SHAP and attention predominate, "although their depth of integration varies and formal reliability assessment remains limited." *Digital pathology* is where explainability is "most tightly integrated into model architecture because the unit of analysis permits direct spatial correspondence between model focus and histological structure." *Molecular and liquid biopsy* spans transcriptomic/genomic architectures, biosensors and chemoinformatic pipelines, and the review's judgement is that **"the most credible XAI contributions arise when the model architecture itself encodes biological knowledge rather than when post hoc attribution is appended to a black-box output."** *Clinical and EMR* models were the largest group, using SHAP for pre-biopsy triage, treatment selection, recurrence prediction and active surveillance.

**Specific results quoted in the prose.** A post-operative erectile dysfunction model in **1,147 men across 2 centres** using XGBoost reached an **external AUC of 0.81**. A bone metastasis model derived from SEER and **externally validated in 327 patients** reported a C-index. An LLM-based bladder grading system (HuatuoGPT-derived) processing EMR narratives, imaging and pathology text through gated multi-head attention reached **AUCs of 0.8 to 0.9** for low versus high grade, with SHAP on token- and section-level embeddings identifying cystoscopy descriptions and pathology phrases as dominant — enabling interfaces that **highlight specific EMR sentences** as patient-level explanations. A complementary pipeline using **logistic regression coefficients as a transparent interpretability layer** reached AUC 0.83, "demonstrating that inherently interpretable linear models remain competitive when inputs are well selected." A digital-pathology multimodal prognostic model was **validated across four STAMPEDE phase 3 radiotherapy trials.** An NMIBC recurrence model using attention weights **outperformed EORTC risk tables.** My own descriptive summary of the 40 distinct AUC values I could locate in the text: **minimum 0.695, median 0.830, mean 0.832, maximum 0.945, with 9 of 40 at or above 0.90** — reported as a picture of what the field publishes, explicitly **not** a pooled estimate, since the review correctly refuses to pool and so do I.

**Foundation models.** The review flags an MRI–pathology foundation model for prostate grading, a multimodal prostate MRI segmentation model, and an LLM system predicting bladder grade from EMR narratives, and states the problem plainly: these "introduce qualitatively new explainability challenges," standard single-modality XAI "cannot be applied straightforwardly," and **"the fundamental question, 'Why did the model produce this output?' may currently have no satisfactory mechanistic answer."**

**Figure captions (figures not viewable).** Figure 1 contrasts post hoc approaches — which "approximate model behavior and require validation for plausibility, fidelity, and stability" — against interpretable-by-design approaches, whose "clinical value depends on alignment with recognized clinical, anatomical, or biological concepts and validation in clinician-facing workflows." Figure 2 is a workflow from clinical question through input data and model output to XAI output, with the insistence that outputs "require clinician review and formal validation before clinical use," validation covering **model performance, explanation reliability, and clinical utility.**

**The limitations the review states itself:** most studies retrospective and single-centre, with performance "frequently declined on external datasets"; **prospective cohorts and randomised evaluations absent across all modalities**; external validation, where done, "often limited to closely related centers or datasets"; narrative rather than systematic, so **"selection bias cannot be excluded"**; **"Studies with negative or equivocal XAI findings are less likely to be published and are therefore underrepresented"**; substantial heterogeneity preventing pooled estimates; **explanations "inconsistently validated,"** with saliency maps "most often presented as qualitative overlays without assessment of stability, sensitivity to input perturbation, or localization accuracy"; no formal appraisal of XAI quality because primary studies did not report the needed inputs; and **"Standardized XAI reporting guidelines analogous to TRIPOD ... do not yet exist for AI in urological oncology."**

**Not reported or not reachable:** the post hoc versus by-design split across the 70 studies; any record or screening counts; the tables as tables; whether any included study used a reporting checklist.

## 3. How Strong Is This Evidence? (Grade 3 out of 5)

**The conceptual framework here is genuinely good — better, on its specific subject, than yesterday's 4/5 review. The reporting of its own evidence base is looser, and the grade follows the weaker half.**

**What earns credit:**

**The central distinction is correctly drawn and then actually used.** Post hoc approximation versus structural transparency is not a new idea, but most XAI papers in medicine mention it once and then treat SHAP and a glass-box model as interchangeable evidence. This review makes it the organising spine, judges each domain against it, and lands the practical consequence: **"whether an AI report stating that 'PSA density was the dominant predictor' was generated by a glass-box model or a post hoc approximation materially affects the extent to which that output should guide a clinical decision."**

**It says the thing about heatmaps that needs saying.** That a saliency map can be anatomically plausible and still weakly coupled to the model's actual reasoning, that such maps are unstable under small perturbations, and that visual agreement is therefore **not** confirmation. And it does not stop at the warning — it names the three specific validations required.

**It gets SHAP's interpretive scope exactly right**, including the hard part: when registry models repeatedly rank T stage, N stage, grade, lymphovascular invasion and carcinoma in situ at the top, those rankings "likely reflect genuine biology, data structure, and overlap between these sources of signal, **which attribution analysis cannot disentangle.**" So SHAP output is restricted "to hypothesis generation rather than mechanistic inference." That is the correct and unflattering conclusion about the field's most-used tool.

**Both search strings are printed verbatim with a cut-off date.** Anyone can re-run them. For a narrative review that is well above the norm.

**The exclusion criterion is the right one.** Ruling out "studies in which explainability was mentioned superficially without a specific method and corresponding results" is precisely the filter that stops a review of explainability from becoming a review of the word.

**It reports the number that undercuts its own field: one reader study in seventy**, and zero prospective or randomised evaluations. It would have been easy to leave that as "more research is needed."

**It names a publication bias specific to its subject** — negative or equivocal XAI findings being less publishable — which, as Section 5 argues, is a selection effect operating directly on the property under study.

**And the forward agenda is concrete rather than ritual:** prospective reader studies measuring decision quality, biopsy rates, reporting time and interobserver variability as *primary* endpoints; prespecified decision-curve analysis; a reporting checklist extending TRIPOD-AI to cover the depth and validation of explainability; and head-to-head comparisons of by-design against post hoc on the same clinical task.

**What holds it to 3:**

**It asserts frequencies throughout and supplies none.** "The vast majority," "a small minority," "the most widely used," "most often presented as qualitative overlays," "most included studies were retrospective and single-center." **Every one is a frequency claim about 70 studies, and not one carries a count** — while the review extracted explainability method *and scope* and validation type for every study into five tables. **The counts existed.** "Post hoc: 61 of 70; interpretable-by-design: 9" would have been the single most useful number in the paper and is the one thing a reader most wants. This is the same flaw as entry 71 three days ago, and unlike entry 72 yesterday — which explicitly forbade frequency inference from its own corpus — this review asserts frequencies without evidencing them.

**Seventy is a numerator with no denominator.** No record counts, no screening numbers, no exclusion tally, no PRISMA-style flow. **70 of 90 and 70 of 900 describe very different reviews**, and nothing here lets you tell which.

**PubMed/MEDLINE only.** For a field whose methodological work appears heavily at IEEE, MICCAI and on arXiv, one biomedical database plus reference tracking is a substantial coverage gap. The review lists selection bias as a limitation but **does not identify single-database search as its likely largest source** — and the omission matters most for exactly the papers it would want: the computer-science literature on whether saliency methods are faithful.

**No risk-of-bias tool, and no appraisal of XAI quality.** The second is excused honestly (primary studies did not report the inputs). The first is excused by heterogeneity, which is a weaker reason: PROBAST+AI exists, applies to prediction models, and heterogeneity of *topic* does not prevent appraisal of *bias*.

**And thirteen authors from a single department.** That concentrates clinical expertise usefully and means the appraisal reflects one institution's reading, with no methodologist or statistician identifiable on the author line for a review whose subject is methodological.

**Why not 4.** Because yesterday's review, on a similar task, published a reconstructable corpus with record counts, prespecified selection criteria, and an explicit refusal to infer frequencies — and this one does none of those three while making frequency claims. **Why not 2.** Because the framework is sound, the warnings are correct and specific, the exclusion criterion is well chosen, and the one-in-seventy finding is reported rather than buried. **A reader who takes only the post hoc/by-design distinction and the heatmap warning away from this paper has gained something durable.**

## 4. The Editor's Concerns

**1. The missing count is the review's own best finding, and it chose not to compute it.** The entire argument turns on post hoc approximation being dominant and structural transparency being rare. The review had the data — explainability method and scope, charted for all 70 studies — and reports the proportion nowhere. **I attempted the tally myself and could not complete it honestly:** the five tables extracted as flattened text with row boundaries lost, yielding 48 performance-bearing cells against an expected 70, with validation wording present in only 25 of those 48. **So I am reporting no split, because I cannot verify one.** The irony is sharp for a paper arguing that explanations must be auditable.

**2. Seventy studies, and no idea out of how many.** Both search strings are printed, which is excellent, and then the screening is invisible. Not a count of records returned, not a count screened, not a count excluded by reason. **A reader cannot distinguish a tightly-screened review from a loosely-assembled one**, and for a narrative review — where selection *is* the method — that is the number that most governs how much weight the synthesis carries.

**3. One database, in a field whose methods literature lives elsewhere.** The warnings this review most relies on — that saliency maps can be plausible and unfaithful, that attention is not explanation, that attributions are unstable under perturbation — come overwhelmingly from the machine-learning literature, which PubMed indexes thinly. **The review cites these findings and searched the one database least likely to contain the primary work establishing them.** That does not make the warnings wrong; it means the review's own evidence base for its strongest claims is thinner than its evidence base for the clinical applications.

**4. Heterogeneity is a reason not to pool, not a reason not to appraise bias.** The review declines a risk-of-bias tool "because of the exploratory and heterogeneous nature of the included literature." But **PROBAST+AI exists precisely for prediction models** and asks about participants, predictors, outcome and analysis — questions that do not require a common effect measure. Entry 72 yesterday made the same choice and was equally explicit, so this is a convention rather than an oversight; it still means **nobody has graded whether these 70 studies are at high risk of bias**, which the review's own remark that "performance frequently declined on external datasets" rather suggests.

**5. The circularity the review walks up to and does not name.** It observes that "in many studies, explainability functions as a post hoc illustration that confirms expected findings," and separately that when SHAP ranks T stage and grade highest, biology and data structure cannot be disentangled. **Put together, those yield a conclusion the review does not state: an explanation that recovers what you already believed provides no new information about the model.** If T stage tops the SHAP ranking, that is equally consistent with a model that learned oncology and a model that learned one registry's coding habits. **Confirmation by explanation is the weakest available evidence precisely because it was the expected outcome** — and only an out-of-distribution test can separate the two. Section 5 develops this.

**6. One reader study in seventy, and it found that explanation *design* was decisive.** The single reader study showed "the explanation method and visual design—not merely the presence of XAI—determine whether clinicians trust and act on AI outputs," and elsewhere the review records that XAI overlays let **non-expert radiologists reach expert-level accuracy on PI-RADS 3 lesions while halving reading time.** **So the one study that looked found a large effect that depended on how the explanation was presented.** That makes the 69 non-studies a measurement gap rather than a null result — and it means the field has been shipping explanations for years without testing the variable that the only test identified as decisive.

**7. The review's own best idea is relegated to a sub-section.** Section 3.3, on causability, contains the observation that "a high-dimensional SHAP plot containing dozens of unlabeled features may provide less usable guidance than a simpler risk summary that maps onto established urological decision frameworks." **That is the practical upshot of the entire paper** — an explanation is an interface, and an unusable interface explains nothing — and it sits in one paragraph of a conceptual section rather than in the conclusions.

**8. A small inconsistency about what glass-box models cost.** The review states that generalised additive models with pairwise interactions "can achieve accuracy comparable to that of fully complex black-box models while remaining fully visualizable," and that logistic-regression coefficients served as a transparent interpretability layer at **AUC 0.83**, "competitive when inputs are well selected." **If transparency is roughly free on structured clinical data, the dominance of post hoc explanation on structured clinical data is not a trade-off but a habit** — a stronger claim than the review makes, and one its own two examples support. It instead calls for head-to-head comparisons, which is more cautious than its evidence requires.

**9. Foundation models are correctly identified as breaking the whole apparatus.** "The fundamental question, 'Why did the model produce this output?' may currently have no satisfactory mechanistic answer," and the gap between capability and explanation granularity "may become a greater barrier to clinical trust than predictive performance itself." **Credit for stating that plainly.** The uncomfortable corollary the review notes but does not press: regulatory frameworks for software as a medical device "are currently advancing faster than the XAI methodology needed to support them."

**10. Reporting and disclosure are complete, which is worth recording.** Funding "None," no conflicts, acknowledgments "None," ethics not applicable, data availability on request — **all five present**, after yesterday's entry where the entire block was absent from the extraction. And the **Statement of AI use** names ChatGPT GPT-5.2 and GPT-5.5 plus Grammarly for language editing. **That makes three papers in this list disclosing generative-AI writing assistance:** entry 67 (ChatGPT, language editing), entry 71 (OpenEvidence for literature review plus Claude Sonnet 3.5 for proofreading), and this one. Three different disclosure wordings, all appropriate, in a fortnight.

## 5. Statistics Spotlight

Ten techniques, numbered from 234 in the running list in `queue.md`. This list has accumulated SHAP lessons across entries 96, 106, 143 and 164; the first three techniques here are what that accumulation adds up to.

**Post hoc explanation and interpretable-by-design are different kinds of evidence, not different styles of the same thing.**

An **interpretable-by-design** model has its reasoning in its structure. A generalised additive model fits a smooth curve for each predictor, so "PSA density mattered most" is **read directly off the fitted model** — it is a fact about the model, auditable, reproducible, and as reliable as the model's own arithmetic.

A **post hoc** explanation is a second procedure run against a finished black box. SHAP perturbs inputs and watches outputs to **estimate** each feature's contribution; Grad-CAM reads gradients to **estimate** which pixels mattered. Both produce an **approximation** of the model's behaviour, with its own error, its own assumptions, and its own failure modes.

The review's statement of the consequence is the cleanest available: the distinction "determines whether an explanation is an auditable property of the model or an external approximation that may not faithfully represent the model's actual reasoning." And in practical terms: whether a report saying "PSA density was the dominant predictor" came from a glass-box or a post hoc method **"materially affects the extent to which that output should guide a clinical decision."**

**The everyday version.** You want to know why a bakery's bread is good. **Glass-box:** they hand you the recipe. You can read it, check it, argue with it, and bake from it. **Post hoc:** you are not allowed in the kitchen, so you buy a hundred loaves, vary the weather and the time of day, and infer that humidity matters most. Your inference may well be right. It is an **estimate about a process you never observed**, and it could be entirely wrong while fitting every loaf you bought.

**Watch out for:** papers that present SHAP output in the same register as a regression coefficient table. A coefficient is a parameter of the fitted model; a SHAP value is the output of a separate estimation procedure applied to it. **When a paper says "the model used feature X," check whether that is a readout or an inference**, and then ask the next question, which is technique 235.

**A plausible saliency map is not a correct one — and the three tests that distinguish them.**

This is the single most useful warning in the review, and it is counterintuitive, because the heatmap landing on the tumour feels like proof.

The review: **"saliency maps can appear anatomically plausible while remaining weakly coupled to the model's true decision process. These maps can also be unstable under minor input perturbations."** Hence: **"visual agreement between a heatmap and anatomical expectations should not, by itself, be considered confirmation that the model is reasoning correctly."**

**Why plausibility is so weak.** A saliency map highlights where the image is *locally sensitive* — change these pixels and the output moves. The tumour is the highest-contrast, most unusual structure in the picture, so it is where almost any image model is locally sensitive, **whether or not the tumour is what drove the classification.** A model that actually keyed on the scanner's noise signature, or on the fact that cancer cases at this hospital were scanned on the older machine, can still produce a heatmap centred on the lesion. **The map is compatible with the right reasoning and with the wrong reasoning, so observing it discriminates between them hardly at all.**

**The three tests the review names, and what each catches.**
**Perturbation tests** — change the input slightly and see whether the explanation changes a lot. A faithful explanation should be about as stable as the prediction. **If a one-pixel-shift rewrites your heatmap, the heatmap was not describing the model.**
**Prediction–saliency coupling** — remove or occlude the region the map highlighted. If the prediction barely moves, the highlighted region was not what the model used. **This is the direct test and it is rarely run.**
**Concordance with expert annotations** — compare the map against lesion contours drawn by a radiologist, quantitatively. Overlap can be measured; "looks right" cannot.

And for structured data the analogue is **stability across resampling and retraining** — which is exactly what entry 70's Jaccard and Nogueira indices measured, four days ago, on a model where the selected feature set changed substantially between resamples.

**The everyday version.** A detective says the butler did it and points at the butler. The butler is the most suspicious-looking person in the room, so pointing at him is what *any* detective would do, competent or not. **You have learned almost nothing about the detective's reasoning.** To learn something you have to remove the butler and see whether the accusation changes — which is the occlusion test.

**Watch out for:** a figure of heatmaps with a caption saying they "confirm the model focuses on clinically relevant regions," and no quantitative fidelity measure anywhere. The review reports that this is how saliency was **most often** presented across its 70 studies. **Treat such a figure as decoration until a coupling or perturbation measure appears.**

**SHAP attributes association within the model's learned representation — not causation, and not biology.**

The review's formulation is precise enough to memorise: SHAP "values quantify associations between features and predictions **within a model's learned representation.** They do not establish causality and inherit any biases or confounders embedded in the training data."

Unpack the three layers of distance from biology. SHAP measures **how the model's output changes** with a feature. The model's output depends on **what the model learned.** What the model learned depends on **the training data, including its confounders, coding conventions and collection artefacts.** So a SHAP ranking is at three removes from the disease.

**The review's own example makes this concrete and uncomfortable.** Across bladder cancer registry models, SHAP consistently ranks T stage, N stage, grade, lymphovascular invasion and carcinoma in situ at the top. Those "likely reflect genuine biology, data structure, and overlap between these sources of signal, **which attribution analysis cannot disentangle.**" Three explanations fit identically: these features genuinely drive outcome; these features are the most reliably *coded* fields in the registry; or these features are correlated with each other and with everything else so attribution smears across them arbitrarily. **SHAP cannot choose between the three**, which is why the review restricts its scope "to hypothesis generation rather than mechanistic inference."

**A tiny worked example of the correlation problem.** Suppose tumour size and T stage are nearly perfectly correlated, and the outcome truly depends on size. Train a model; it can use either, or split the credit arbitrarily. SHAP will report whatever split the fitted model happened to land on — which depends on initialisation, regularisation and the random seed. **Retrain and the ranking can flip, with the biology unchanged.** That is not a SHAP defect; SHAP is faithfully reporting a model that genuinely has two interchangeable paths. **It is a defect in reading a SHAP ranking as a statement about disease.**

**The everyday version.** You ask which ingredient makes a cake rise, and you are only allowed to vary ingredients in a recipe that always uses self-raising flour and baking powder together. Remove either and the cake flops, so both look essential. **The attribution is correct about your recipe and tells you nothing about baking.**

**Watch out for:** SHAP rankings presented as discovery — "the model revealed that X drives outcome." The review's standard is the right one: **report them as hypotheses, and validate with perturbation tests, localisation metrics, or independent biological endpoints before treating them as findings.**

**237. Confirmation by explanation is not validation.** The review notes that explainability often "functions as a post hoc illustration that confirms expected findings." **The consequence, which it leaves implicit: an explanation that recovers your prior carries almost no information.** Information is surprise. If you expected the heatmap on the tumour and the SHAP ranking to start with T stage, then observing both has barely updated you — those observations were nearly certain under a correct model *and* under several incorrect ones. **A genuinely informative explanation is one that could have come out wrong**, which is why the three fidelity tests in technique 235 are worth more than any number of plausible figures. **And the corollary for designers: an explanation that cannot surprise you is not an audit, it is a reassurance.**

**238. Explanation utility and explanation existence are different claims, and only one has been tested here.** Of 70 studies, **1 (1.4%)** ran a reader study; **0** ran a prospective or randomised comparison of explainable against conventional workflows. The one that looked found that explanation **design** — not its presence — determined whether clinicians acted, and that overlays let non-expert radiologists reach expert-level accuracy on ambiguous lesions while **halving reading time.** **So the gap is a measurement gap, not a null result.** The distinction generalises: *does an explanation exist* is an engineering property; *does it change a decision for the better* is a clinical outcome needing a comparative design. **This is technique 229 from yesterday, applied to explanations rather than predictions — what you deploy is an explanation plus a clinician plus an interface, and only the assembly can be tested.**

**239. Publication bias specific to explainability, and why its direction is known.** The review: **"Studies with negative or equivocal XAI findings are less likely to be published and are therefore underrepresented."** Consider what that selects on. A team generates saliency maps, looks at them, and if they look wrong, investigates further or abandons the figure. **So every heatmap in the published literature has passed an informal visual screen on the exact property under study — plausibility.** The published distribution of "explanations that look sensible" is therefore biased upward by construction, and **unlike the opinion-strength selection in entry 71, which inflated praise and complaint alike, this one biases in a single known direction.** The remedy is the same as for any publication bias: weight unvalidated plausible-looking explanations near zero, and look for the studies that ran a fidelity test and reported the number whichever way it came out.

**240. A review's numerator needs a denominator.** This review reports **70 included studies** and no record counts, no screening numbers and no exclusion tally. **70 of 90 is a near-census of a small field; 70 of 900 is a selection, and selection is the method of a narrative review.** Whenever a review gives you an included count with no flow, you cannot calibrate how much the synthesis depended on choices you cannot see. **Ask for the flow; if it is absent, read the conclusions as the authors' considered opinion informed by 70 studies, which is a different and weaker object than a synthesis of a field.**

**241. Frequency language without counts, in a review that charted the counts.** "The vast majority," "a small minority," "most often," "most included studies." Five frequency claims about 70 studies, zero numbers — from a review that extracted explainability method *and scope* and validation type for every one into five tables. **The data existed; the arithmetic was one column-count away.** Compare the three consecutive reviews and qualitative studies in this list: entry 71 made frequency claims from a 10.4% sample, entry 72 **explicitly forbade** frequency inference from its own corpus, and entry 73 asserts frequencies it charted but does not report. **The best of the three is the one that refused.** When a review asserts a proportion without a count, treat it as the authors' impression — which may well be right, and is not evidence.

**242. A single-database search in a field whose methods literature sits elsewhere.** This review searched **PubMed/MEDLINE only**, plus reference tracking. Its strongest and most load-bearing claims — saliency unfaithfulness, attention not being explanation, attribution instability under perturbation — originate in the machine-learning literature indexed by IEEE Xplore, the ACM Digital Library, MICCAI proceedings and arXiv. **So the review's clinical-application evidence is well covered and its methodological evidence is covered by citation rather than by search.** The general rule: **match your databases to where the evidence for each of your claims actually lives**, and when you cannot, say which claims rest on a thinner search.

**243. Foundation models break post hoc explanation, and the review says so.** When a model integrates imaging, text and genomics through cross-modal attention trained at scale, "tracing that output through cross-modal attention layers ... is categorically different from attributing a gradient-boosted tree prediction to its input features," and token- or patch-level attribution "cannot verify whether the model has learned clinically valid reasoning or merely statistical co-occurrence in the training data." **So for the newest and most capable models, the honest answer to "why did it say that?" is currently that nobody knows.** Two consequences worth holding. **The gap is widening**, because capability is scaling faster than explanation methods. And **regulation is moving faster than the methodology meant to support it** — the review's own observation — which means "explainable" may become a box ticked on a submission before anyone can tick it truthfully.

## 6. Jargon Translator

**Explainable AI (XAI)** — methods that link a model's prediction to something a human can inspect: which variables mattered, or which part of an image. An umbrella term covering two quite different things, which is the review's main point.

**Post hoc explanation** — produced *after* a model is trained, by probing it from outside. An estimate of what the model did.

**Interpretable-by-design / glass-box** — the model's structure *is* the explanation, so you read its reasoning off the model rather than inferring it.

**SHAP (SHapley Additive exPlanations)** — assigns each input variable a share of the credit for a prediction, using a fairness idea borrowed from game theory. Consistent and widely used; still an estimate about the model, not a statement about biology.

**LIME** — fits a simple model around one prediction to approximate the complex model locally. Model-agnostic, and the review notes it "can produce inconsistent explanations depending on the perturbation scheme."

**Grad-CAM / saliency map** — a heatmap over an image showing which regions most influenced the output. Intuitive, and the thing technique 235 is about.

**Attention** — a mechanism letting a network weight some inputs more than others. Often shown as if it were an explanation; the review warns attention "should not be assumed to be faithful without dedicated reliability testing."

**Fidelity** — whether an explanation actually reflects what the model did, as opposed to looking reasonable. The property almost never measured.

**Perturbation test** — nudge the input and see whether the explanation changes more than the prediction does. A stability check.

**Prediction–saliency coupling** — occlude the region a heatmap highlighted and see whether the prediction moves. The direct test of whether the model used that region.

**Concept bottleneck model** — forces predictions through a layer of named clinical concepts (PI-RADS components, grade group), so a clinician can inspect and correct at concept level.

**Prototype-based network** — classifies by resemblance to a library of example patches: "this looks like these known high-grade examples." Close to how pathologists actually reason.

**Generalised additive model** — fits a separate readable curve for each predictor, optionally with a few interactions. The review notes these can match black-box accuracy on structured clinical data while staying fully visualisable.

**Pathway-constrained network** — a network whose wiring is forced to follow known biological pathways, so high-weight nodes correspond to real genes and processes. The review's exemplar of explanation as structure.

**Causability / System Causability Scale** — how well a *human* can form a correct and actionable understanding from an explanation. Explanation quality judged from the user's side rather than the model's.

**PI-RADS** — the 1-to-5 scale for reporting prostate MRI suspicion. **PI-RADS 3 is the genuinely equivocal middle**, which is why the one reader study used it.

**NMIBC / MIBC** — non-muscle-invasive versus muscle-invasive bladder cancer. The distinction drives management, from bladder-sparing surveillance to cystectomy.

**TURBT** — transurethral resection of bladder tumour: the scope-and-resect procedure that both diagnoses and treats bladder tumours.

**Decision-curve analysis** — weighs true against false positives across the thresholds a clinician might actually use. Answers "would acting on this help?" rather than "does it rank well?"

**Software as a medical device** — the regulatory category clinical AI falls into. Relevant because, as the review notes, it is advancing faster than the explanation methods meant to support it.

## 7. What You Can (and Can't) Say

**You can say:**

"A 2026 review of 70 studies of explainable AI in prostate and bladder cancer found that post hoc explanation methods such as SHAP and Grad-CAM dominate, while models with transparency built into their structure remain a small minority."

"The review states that saliency maps can appear anatomically plausible while being weakly coupled to the model's actual reasoning, and can be unstable under small changes to the input — so visual agreement with anatomy is not confirmation that a model is reasoning correctly."

"Of the 70 included studies, one ran a reader study, and no study prospectively or randomly compared explainable against conventional workflows."

"That single reader study found that the design of the explanation, not merely its presence, determined whether clinicians trusted and acted on the output — and that overlays let non-expert radiologists reach expert-level accuracy on equivocal PI-RADS 3 lesions while halving reading time."

"SHAP values describe associations within a model's learned representation; the review concludes they support hypothesis generation rather than mechanistic inference."

"The review's strongest examples are models whose architecture encodes the explanation — including a network constrained to known prostate cancer pathways that produced an experimentally validated therapeutic target."

**You cannot say:**

"Most XAI studies use post hoc methods," with any specific proportion. **The review asserts this without a count**, and I could not verify one from the flattened tables. The direction is probably right; the magnitude is unevidenced.

"Explainable AI doesn't work," or "doesn't help clinicians." **One study tested it and found a substantial benefit.** Sixty-nine did not test it. That is a measurement gap, and the one measurement available was positive.

"These 70 studies represent the field." Single-database search (PubMed/MEDLINE), no record or screening counts, and the review itself says selection bias cannot be excluded and that negative XAI findings are underrepresented.

"The heatmaps show the model is looking at the tumour." They show the model's output is locally sensitive to that region. **Establishing that the model used it requires occluding it and watching the prediction** — a test the review reports was rarely run.

"SHAP revealed that T stage drives bladder cancer outcome." SHAP revealed that *the model's output* depends on the T stage field. Biology, registry coding practice and correlation among the predictors are all consistent with that, and the review says attribution cannot separate them.

"Interpretable models sacrifice accuracy." The review reports the opposite on structured clinical data: generalised additive models with pairwise interactions can match black-box accuracy while staying visualisable, and a logistic-regression layer reached AUC 0.83.

"Foundation models are explainable with the usual tools." The review says standard single-modality methods cannot be applied straightforwardly, and that "why did the model produce this output?" may currently have no satisfactory mechanistic answer.

"This review graded the quality of the studies it included." It applied **no risk-of-bias tool** and no formal appraisal of XAI quality, and says so.

**The honest one-sentence version:** *thirteen urologists read 70 studies and concluded that the field's dominant form of explanation is an after-the-fact approximation that is almost never checked for faithfulness, that a convincing heatmap is evidence of very little, that the handful of models with explanation built into their structure are the ones worth copying, and that in seventy studies exactly one asked whether any of it changed what a clinician did — a review whose framework is sharper than its own accounting, since it asserts proportions it charted and never reports.*

## 8. Bottom Line for Your Life

**If you are a patient:** nothing here changes your care. What it is worth knowing is that when an AI tool is described as "explainable," that word currently covers two very different things — a model whose reasoning can genuinely be inspected, and a black box with a plausible-looking picture attached. **Your clinician's judgement about whether an AI output makes sense for you is doing more work than the explanation is**, and this review's conclusion is that it should.

**If you are a clinician:** the practical instruction is one question. When a vendor shows you a heatmap, ask **"what happens to the prediction if you cover that region?"** If the answer is "we haven't measured that," you are looking at a picture, not an audit — and the review reports that this is how most of the literature presents saliency. For structured-data tools, the equivalent question is **"does the feature ranking stay the same if you retrain on a different split?"** Entry 70 in this list, four days ago, showed a model whose selected features changed substantially between resamples while its performance held steady.

**If you procure or deploy clinical AI:** two things from this review are directly actionable. **On structured clinical data, transparency appears to be roughly free** — generalised additive models matched black-box accuracy here, and a logistic-regression layer reached AUC 0.83 — so for PSA, age, stage and grade, **ask why the tool is a black box at all.** And **the one reader study found that explanation design determined whether clinicians acted.** A SHAP plot with forty unlabelled features is not an explanation to a working urologist; the review's own words are that it "may provide less usable guidance than a simpler risk summary that maps onto established urological decision frameworks." **Specify the interface, not just the algorithm.**

**If you are a researcher:** the gap is embarrassingly specific and cheap to close. **One reader study in seventy.** The review's proposed endpoints are the right ones — decision quality, biopsy rates, reporting time, interobserver variability as *primary* outcomes, with decision-curve analysis prespecified. And if you publish a saliency figure, **publish a fidelity number beside it**: an occlusion effect, a perturbation-stability measure, or an overlap statistic against expert contours. The review reports that this is almost never done, which means doing it is currently a cheap way to produce the most informative paper in your subfield.

**If you build or buy foundation models for clinical use:** the review's warning is the one to carry. For cross-modal architectures, **"why did the model produce this output?" may currently have no satisfactory mechanistic answer**, and regulation is advancing faster than the methods that would answer it. Plan validation around **outcomes and monitored deployment** rather than around an explanation you will not be able to supply.

**If you are reading AI coverage generally:** the reflex this review should install is a small one. **A picture of a model's reasoning is not a measurement of its reasoning.** The heatmap on the tumour, the SHAP bar chart topped by the variable you expected — both are what a correct model and several incorrect models would produce. **Ask what would have looked different if the model were wrong.** If the answer is "nothing," the explanation has told you nothing.

**This is education, not medical advice.** Nothing here should change anyone's treatment or any decision about prostate or bladder cancer care. Those are conversations with your own clinician.

---

## Appendix: shelf restocked, deferred papers, status on 2026-11-10

**Shelf restocked, as planned yesterday**, using the `pubmed pmc[sb]` date-window method that went six-for-six on 2026-10-28 and again on 2026-11-03. The search — AI/ML/DL/LLM in the title AND validation, external, prospective, multicenter or calibration in the title/abstract, restricted to PMC-indexed records entered 2026-11-01 to 2026-11-10 — returned **189 records**, of which I screened 10 and kept **6**, rejecting a tea-metabolite study, a livestock-genetics review, and a remote-sensing parasite-risk model as outside clinical medicine. **All six have confirmed PMC IDs.** In priority order:

**(A) Exploratory machine-learning evaluation of clinical and dosimetric features in late prostate radiotherapy toxicity** — PMID 42999685, PMC13744349, *Clin Transl Radiat Oncol* 2026;62:101305, Jordan K et al. **229 men** from the REQUITE cohort. **This is the most valuable item on the shelf, because it is a near-null study reported properly**: GI toxicity AUCs of **0.573, 0.571 and 0.587** with permutation p-values of **0.036, 0.047 and 0.022** — statistically significant discrimination that is clinically almost worthless, which is the cleanest possible teaching case for "significant is not useful." And **GU discrimination was below chance with no evidence beyond the null distribution.** Repeated nested stratified cross-validation, bootstrap CIs, outcome-label permutation testing, and SHAP stability assessed across repeats. **This list has almost no honestly reported negative studies.**

**(B) Multimodal imaging and artificial intelligence for bone tumor diagnosis** — PMID 42997475, PMC13742044, *J Bone Oncol* 2026;61:100808, Liu X & Liu L. A review advancing **one specific argument**: that the binding constraint on AI in musculoskeletal oncology is **the stability of the reference standard, not algorithmic capability** — with numbers. Biopsy-versus-resection grade agreement in central chondrosarcoma falls from **weighted kappa 0.63 in long bones to 0.12 in the pelvis**; interobserver kappa for grading cartilaginous tumours is **0.44 among musculoskeletal pathologists and 0.35 among radiologists**; molecular criteria have redefined entities so older datasets "contain classes that no longer exist as defined." And the inference that inverts this list's technique 194: **"apparent failure on external validation may reflect label divergence between institutions rather than model deficiency."** Genuinely new territory here.

**(C) A Robust and Trustable Approach to Incorporate Medical Domain Knowledge in Machine Learning Models for Diabetic Retinopathy Screening** — PMID 42974596, PMC13727297, *Smart Health* 2026;42:100724, Laoh E et al. **97,786 patients, 16,865 cases (17.25%)**, an eight-variable XGBoost reporting **AUROC 97.24%, sensitivity 91.17%, specificity 96.22%** on a 19,558-patient untouched test set, with SMOTE applied to training only. **Shelved for a sceptical reading**: technique 224 converts AUROC 0.972 to roughly 80% of outcome variance, and two of the eight predictors are **nephropathy and neuropathy** — the other two microvascular complications of diabetes, routinely coded alongside retinopathy. A near-textbook label-leakage candidate, and the authors' own framing is about trustworthiness.

**(D) Predicting Future Visual Field Status from Baseline OCT Scan in Early to Moderate Glaucoma Using Deep Learning** — PMID 42997014, PMC13740841, *Ophthalmol Sci* 2026;6(12):101419, Chaurasia AK et al. **1,792 eyes from 1,610 patients** for development, with **genuine external validation at two further centres on two different OCT devices** (Zeiss Cirrus, 150 eyes; Heidelberg Spectralis, 280 eyes), MAE reported with 95% CIs throughout, follow-up 4.74 ± 2.59 years. **Multi-device external validation is rare** and this list has decoded almost none.

**(E) Machine learning models to predict pathological complete response after chemoradiotherapy in muscle-invasive bladder cancer** — PMID 42997524, PMC13741961, *Clin Transl Radiat Oncol* 2026;62:101320, Fujiwara M et al. **285 patients**, with **102 machine-learning models evaluated in the training cohort** and the best-in-training taken forward — a textbook winner's-curse setup — reaching test AUC **0.829 (0.706–0.932)**. And the authors report a **calibration slope of 0.856 with a 95% CI of 0.469 to 1.639**, stating themselves that "the wide CI indicated uncertainty in calibration." Honest, and a good vehicle for calibration-slope teaching.

**(F) Automated Detection of Positioning Errors in Bitewing Radiographs Using Deep Learning** — PMID 42981213, PMC13734376, *Clin Exp Dent Res* 2026;12(6), Rabelo KA et al. **403 radiographs, acquired entirely from dental mannequins**, with accuracies from 99.0% (side) down to **73.2% (incorrect receptor placement)**, and the authors stating that "a validation study using patient-acquired bitewing radiographs from clinical settings is required before clinical deployment." A clean, low-stakes case for teaching distribution shift: **a mannequin is not a patient.**

**Landmark check for the past week.** According to PubMed, four records, three previously assessed. The new one is **"Mass Surveillance with Artificial Intelligence — A New Determinant of Health?"** (PMID 43001754, [DOI](https://doi.org/10.1056/NEJMp2611224), *NEJM*, 7 November 2026, Peoples N, Hoops K, Fleegler EW). **A Perspective piece with no abstract, so not a primary study and it does not displace the queue** — but noted because it is adjacent to entry 71's finding three days ago that patients spontaneously raised **insurance eligibility, employment and assisted-living admission** as harms of an incidental AI finding. If a primary study on surveillance-derived health data appears, it goes straight to the shelf.

**Deferred papers — four, all re-checked today.** **Gait foundation model**, *Nature Medicine* (PMID 42995231, [DOI](https://doi.org/10.1038/s41591-026-04724-9)) — **day 2**, no PMC copy, abstract-only date **2026-11-30**. **Nature personal health agent** (PMID 42907512, [DOI](https://doi.org/10.1038/s41586-026-11161-8)) — **day 21**, weekly re-check. **BMJ review of LLM-trial reporting completeness** (PMID 42869550, [DOI](https://doi.org/10.1136/bmj-2026-100855)) — **day 28, and its twenty-one-day threshold fires in two days, on 2026-11-12.** Today's entry makes it sharper again: this review states that **"standardized XAI reporting guidelines analogous to TRIPOD do not yet exist"** and calls for a checklist extending TRIPOD-AI to cover the depth and validation of explainability — which is precisely the kind of gap the BMJ review quantifies at 40% mean TRIPOD-LLM completeness. ***Annals* *Choosing Wisely*** (PMID 42896192, [DOI](https://doi.org/10.7326/ANNALS-26-01667)) — **day 21**, weekly re-check, abstract-only date 2026-11-19.

**Next run takes shelf item (A)**, the REQUITE radiotherapy toxicity study — a near-null result reported with permutation testing, bootstrap CIs and SHAP stability analysis, and the natural home for teaching why an AUC of 0.587 can be statistically significant and clinically useless. **On 2026-11-12 the BMJ review takes priority** under the standing rule if its PMC body is still empty.

**Watch item:** PM Heart trial results (protocol PMID 42893738), quarterly.
