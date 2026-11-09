# Artificial Intelligence-driven Biomarker Discovery for Precision Psychiatry

**Author:** Serretti A (**a single author** — Department of Medicine and Surgery, Kore University of Enna, Italy; Oasi Research Institute–IRCCS, Troina, Italy.)
**Journal:** Clinical Psychopharmacology and Neuroscience, 2026; 24(4): 675–691 (published 30 October 2026)
**Decoded:** 2026-11-09

**Analysis basis:** **FULL TEXT** (retrieved from PubMed Central, PMC13720497) — the complete Introduction, Search Strategy and Evidence Selection, all five body sections, Limitations, What Changes Next and Conclusions. **Every table and figure is unreachable**, and for this paper that is a serious gap rather than a cosmetic one: **the full specification of the six-stage framework — the review's central contribution — lives in a table.** I have the six stages only *in brief*, as the Introduction summarises them, and not the per-stage scientific question, minimum evidence, required reporting or characteristic failure mode. Also unreachable: the table of eight method and workflow families, the per-study table giving sample, performance and stage demonstrated, and the tabulated failure-mode catalogue (which is however described at length in prose).

**Source links (verified):**
- DOI: https://doi.org/10.9758/cpn.26.1519
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42947584/
- Full text used: https://pmc.ncbi.nlm.nih.gov/articles/PMC13720497/

**Basis of link verification.** Direct URL fetching is blocked from this session (`doi.org` does not resolve under the network policy here), so verification was done against the live PubMed/NLM record. According to PubMed, a query for PMID 42947584 returned this exact title, this single author with these two affiliations, *Clinical Psychopharmacology and Neuroscience* volume 24 issue 4 pages 675–691, publication date 30 October 2026, DOI `10.9758/cpn.26.1519`, publisher identifier `cpn.26.1519` and PMC ID `PMC13720497`; the full text was then retrieved from PubMed Central by that PMC ID and matches the record. Both halves of the chain were confirmed independently.

**Funding, competing interests, acknowledgements and data availability: none of the four appears anywhere in the retrieved text**, which ends at CONCLUSIONS. **I am not reporting them, because I have not seen them.** Most journals require a competing-interest statement, so this is very likely an **extraction gap rather than an omission** — but for a review that discusses commercial pharmacogenomic tests and named drug-development programmes, a reader should go to the article for it rather than take silence here as absence.

**Reporting guideline: none claimed, and the review is explicit about why** — it declares itself **narrative rather than systematic**, so PRISMA does not apply. It does, however, **name and correctly distinguish TRIPOD+AI, PROBAST+AI and DECIDE-AI** as standards for the studies it reviews, which Section 5 treats as a technique in its own right.

**Nature of this entry:** a **narrative review**, the first in this reading list to be decoded. It is also, more than any previous entry, **a paper about the same problem this reading list exists to address** — how to tell a strong study from a weak one — and Section 3 says plainly where it is better at that than this list has been.

---

## 1. The Gist

**This review's central observation is one sentence long, and it reframes the whole field: "Producing candidates is becoming cheap while qualifying them is not."**

Precision psychiatry has been promising for two decades to replace clinical guesswork with measurement — a blood test, a brain scan, a voice sample that tells you which antidepressant will work. AI has made the *finding* of such candidates dramatically easier. Language models can read a hundred thousand clinical notes and turn them into variables. Self-supervised models can learn from the oceans of unlabelled signal psychiatry already collects. Research agents have proposed drug candidates and had them confirmed in a laboratory — though, importantly, **not yet in psychiatry.**

**What has not got easier is proving any of it works.** And the review's verdict is unusually direct: **"None of the artificial intelligence capabilities reviewed here yet reaches the stages at which a candidate becomes a clinical test."**

**Three findings in it are worth your time whatever field you work in.**

**The two substitutions.** Over and over, reported performance answers an easier question than the clinical one. **Diagnosis stands in for differential diagnosis** — and the review's example is brutal. A schizophrenia classifier kept a respectable external sensitivity of 0.75, but **misclassified 59% of bipolar cases and 55% of depression cases.** Telling schizophrenia from healthy people is easy. Telling it from bipolar disorder is the actual job. **Prognosis stands in for differential treatment benefit** — identifying who will get better, rather than who will get better *on this drug rather than that one.* Of 19 comparative antidepressant studies in one systematic review, **only one directly ranked treatments.**

**Nonspecific prediction, with the perfect example.** Anterior cingulate theta activity is, in the review's words, **among the most replicated** markers in psychiatry. It predicts response to antidepressants. It also predicts response to repetitive transcranial magnetic stimulation, to electroconvulsive therapy — **and to placebo.** A marker that predicts recovery under everything is not a treatment-selection marker; it identifies patients who recover. And the reason is structural: most treatment-response markers in psychiatry were **defined in open-label single-arm data and never tested against a control arm**, so their specificity to a treatment was never knowable.

**And the finding that ought to be on a poster in every hospital procuring AI.** In a preregistered randomised study of 1,298 people, **language models alone identified the relevant condition in 94.9% of cases — and the participants who were given the model to help them did no better than the participants who were not.** A 94.9% standalone score bought nothing once a human was in the loop.

**What the review offers in return is a ladder.** Six stages, from "name the decision this marker informs" to "monitored deployment with drift surveillance." Its practical instruction to a clinician is five questions long, and Section 5 turns them into arithmetic you can run yourself.

## 2. Study Snapshot

**Type:** a **narrative review**, declared as such repeatedly and deliberately. **Not a systematic review**, no meta-analysis, no pooled estimate, no formal risk-of-bias scoring of included studies.

**Search and selection, reported in a dedicated section — which is better practice than most narrative reviews manage.** Structured PubMed searches **run to July 2026**, limited to work **published from 2015 onward**, covering AI methods, data modalities, treatment prediction, validation standards, digital phenotyping and autonomous discovery, with a focused top-up search for recent large language and foundation models. **The query strings, retrieval dates and returned records were retained, "so the corpus can be reconstructed."** Selection criteria were **set before screening**: syntheses and reporting standards from 2022 onward; large, multicentre, longitudinal, randomised or externally evaluated studies; models addressing a clinically consequential task; and studies reporting calibration, external evaluation, decision-curve analysis or failed replication. **Diagnosis-only case-control classifiers and single-centre pilots without held-out evaluation were given low priority.** **Fifty-three records form the core evidence set**, each held with extracted values and an assessment of contribution; not all are cited.

**The review's own stated guard against over-reading, quoted verbatim because it is rare:** *"It compares method families and evaluation designs across studies too heterogeneous to pool, so it reports no field-wide frequencies and none should be inferred from the examples cited."* And: *"The published evidence is itself concentrated in depression and psychosis, and conclusions for other disorders therefore rest on fewer studies."*

**The six-stage framework, in the brief form the Introduction gives** (the full specification is in an unreachable table):
- **Stage 1** — name the decision the marker is meant to inform, the population it applies to, and the comparator it is judged against
- **Stage 2** — validity of the measurement, and of the label the model is trained against
- **Stage 3** — internal evaluation of the complete modelling pipeline **against a simple baseline**
- **Stage 4** — evaluation of a **locked** model under a shift in site, time, device or population
- **Stage 5** — **prospective** testing of whether model-guided use improves decisions or outcomes
- **Stage 6** — monitored deployment, with governance, fairness and drift surveillance

**A "readiness" value reported as a stage number records the highest stage demonstrated among the studies cited.** And the headline result of that mapping: among the psychiatric biomarker examples selected, **every method family occupies the pre-deployment stages and none occupies the two beyond them.**

**Method families, as the review separates them** (with the framing that "method family is not a stage of clinical qualification, and greater complexity does not imply stronger evidence"): conventional supervised methods (penalised regression, support vector machines, random forests, gradient boosting — *"they provide important baselines against which more complex models should be compared"*); unsupervised methods and, distinctly, **normative models** that estimate a reference distribution and quantify individual deviation; neural networks; transformers; self-supervision as a *training strategy*; foundation models as *large reusable models*; LLMs as *language-oriented foundation models*; **causal machine learning** for treatment-effect heterogeneity; and autonomous or multi-agent systems, which *"coordinate literature searches, analyses and laboratory iteration rather than directly defining a biomarker."*

**Selected findings by data source, with the numbers as reported.**

*Electronic health records.* A dynamic transdiagnostic psychosis-risk model used **158,139 patients with 5,007 events**, reaching a concordance index of **0.79 against 0.76 for a static model**, with internal-external evaluation examining **calibration and decision-curve net benefit, not discrimination alone.** A multisite bipolar risk model used **3,529,569 records containing 12,533 cases**, AUC **0.82 to 0.87**, calibration assessed — but **positive predictive values were concentrated in the highest-risk quantiles and local retraining was required.** And the one that matters most: in **73,601 primary-care patients**, an antidepressant-selection model reached AUC **0.65** while **baseline severity alone reached 0.61**, and the estimated data-driven policy **improved little over routine practice.** The review labels it correctly: *"a retrospective policy evaluation, not a prospective test of model-guided prescribing."*

*Genomics.* A trans-ancestry depression meta-analysis of **688,808 cases and 4,364,225 controls from 29 countries** found **697 associations at 635 loci**, while polygenic scores explained **at most 5.8% of liability** in the best-powered ancestry and less elsewhere. A meta-analysis of **6 prospective studies and 3,532 adults** with at least one treatment failure evaluated **one** weighted multigene test: response relative risk **1.3 (1.16–1.47)**, remission relative risk **1.41 (1.19–1.66)** — and the review immediately notes this **"did not evaluate an AI-guided intervention"** and that *"absolute benefit, comparator and sponsorship remain important to interpretation."*

*Molecular and multiomic.* A systematic review of machine learning on immune markers covered **43 studies and 11,556 participants**, diagnostic AUCs **0.65 to 0.99** — and the review adds that *"this range is descriptive and is not itself an estimate of heterogeneity or transportability."* In **7,945 depression cases**, unsupervised analysis found three metabolic subtypes with subtype-specific discrimination of **0.942 against 0.644** for the pooled model.

*Neuroimaging.* An umbrella review of treatment-response imaging covered **14 reviews and 17,855 patients**: **evidence quality low to very low, and most high-performing models lacked external evaluation.** A reproducibility analysis of roughly **50,000 participants** showed brain-wide associations **smaller than previously assumed**, requiring samples in the thousands. And a clean negative: resting-state functional imaging **did not predict psychotherapy outcome above chance or beyond clinical variables** in two independent samples of **220 and 190** participants.

*Electroencephalography.* A machine-learning meta-analysis of **15 treatment-response studies and 758 patients**: pooled accuracy **83.9%**, pooled AUC **0.85 (0.747–0.89)** — with the review's own caution that *"many contributing studies were small, open-label, or lacked independent train-test separation"* and the pooled estimates *"therefore probably overstate performance."*

*Speech and wearables.* A multicentre speech model used **23,608 samples from 1,816 participants**: internal evaluation on 333 participants gave AUC **0.932**, external on 160 gave **0.879** — *"a comparatively strong result among the examples reviewed"* — but the task was **supported diagnosis, not treatment choice.** A systematic review of passive sensing covered **52 studies and 4,814 participants**, relapse AUCs **0.7 to 0.88** up to four weeks ahead, with **most studies at high risk of bias.** And the most instructive single example in the review: a wearable study followed **144 people across 90,281 person-days**, week-ahead prediction of depressive episodes reaching AUC **0.772 (0.75–0.794)** — at a base rate of **5.3%**, a positive predictive value of **16.7%** and a review burden of **20 per 100 patient-days.** The review notes that *"the repeated person-days do not constitute independent participants."*

*Multimodal.* Randomised schizophrenia trial cohorts: **2,307 discovery participants** gave AUC **0.874 (0.867–0.881)** for antipsychotic response, and **1,379 external-evaluation participants** gave **0.851 (0.841–0.861)**. The review's assessment is careful: randomisation strengthened the source data and external testing strengthened evaluation, but **"neither feature demonstrates that using the model prospectively improves treatment selection,"** and the model **"did not directly estimate each patient's differential benefit across antipsychotics."**

**Language models: two bounded uses supported, one not.** Phenotyping from clinical text — one study drew from **111,563 adults** but **development and evaluation used 3,996 manually reviewed note sets**, best AUC **0.84** with positive predictive value **0.8 at specificity 0.87**; the review warns that *"the larger source population should not be read as the evaluation sample."* A preprint tested open-source generative models on **109 psychiatric phenotypes**, macro-F1 **0.75 to 0.86** after fine-tuning, with either a fine-tuned model or a traditional pipeline reliably detecting **100** phenotypes. Structuring evidence — a locally run pipeline for abstract screening benchmarked against three published reference reviews, where *"a false exclusion could remove a record from every downstream analysis."* **Autonomous clinical decision-making is not supported**, and the key evidence is the human-factors study: **1,298 members of the public, general medical scenarios, models alone identifying the relevant condition in 94.9%, and assisted participants doing no better than controls.**

**Research agents.** Robin proposed enhancing retinal pigment epithelium phagocytosis in dry age-related macular degeneration and identified **ripasudil**, a clinically used Rho kinase inhibitor, with confirmed activity. Co-scientist generated, critiqued and ranked hypotheses through an internal tournament. A benchmark of AI scientists used **15 single-cell datasets and 193 discovery questions drawn from 41 published studies**, finding current systems **below the standard required for autonomous discovery.** The review's framing is exact: *"Humans framed the problems, ran the physical experiments and checked the outputs… The systems were therefore semi-autonomous,"* and *"workflow completion is an engineering result."*

**Stage 4 failure, stated as starkly as it deserves:** machine-learning models trained on one randomised antipsychotic trial **predicted outcomes well within that trial and no better than chance in independent trials, and pooling the trials did not repair the loss.**

**The failure-mode catalogue, in prose** (the table is unreachable): leakage; shortcut learning (distinguishing scanner, site or documentation style instead of the construct); pretraining–evaluation overlap; **modality dominance** (one information-rich channel carrying a multimodal result while the others add cost); **version drift** (a hosted model's output changing under an unchanged prompt); **human-use failure**; **error propagation in agents**; **nonspecific prediction**; and **misattributed failure** — *"a negative biomarker-guided trial can fail because the drug did not engage its target or because the selection rule was wrong, and the two call for different corrections."*

**Fairness as part of evaluation, with a concrete example:** aggression prediction in acute psychiatric care, **17,703 patients and 42,719 observation-days**, overall AUC **0.81** — while **error rates differed by race or ethnicity, gender, admission mode, citizenship and housing.** *"Overall discrimination can conceal subgroup errors with different clinical consequences."*

**A calibration point for the whole field:** *"Reproducible treatment-response prediction in independent data typically explains about 5 to 15% of outcome variance… A much larger figure, reported in the data used to develop the model, usually reflects optimism."*

**Regulatory grounding:** the **2019 US FDA enrichment guidance**, and the crucial consequence that **a trial conducted only in marker-positive participants can establish efficacy in that group but cannot show the marker is predictive rather than prognostic.** Two illustrations: **zuranolone**, approved for postpartum depression on a rationale resting on parturition-related falls in allopregnanolone, with inconsistent phase III results in broader major depression — a subgroup defined by **clinical context rather than a measured marker**; and a polymorphism in **ANK3** reported to predict response to **liafensine**, with placebo-controlled efficacy shown in carriers but **no result reported in non-carriers**, where *"the unusually large variance attributed to one common variant also raises a plausibility concern."*

**Limitations the review states itself:** narrative and PubMed-based with purposive selection; **no formal risk-of-bias assessment of every cited study**; **the six-stage assignments are "qualitative author judgements"**; selection favours recent, large, externally evaluated or clinically consequential studies, so it **cannot estimate how often any problem occurs**; evidence concentrated in depression and psychosis; and the rapid publication cycle means the assessment will need updating.

**Not reported or not reachable:** all tables and figures, including the full six-stage specification; the query strings and record counts (retained but not printed); any funding or competing-interest statement.

## 3. How Strong Is This Evidence? (Grade 4 out of 5)

**The third 4 out of 5 in this list, the first for a review, and it earns it on epistemic hygiene rather than on new data.** A review produces no data; it can only be graded on whether its claims are supported by what it assembles, and whether it tells you honestly what it is. On both counts this is the best-behaved paper decoded here.

**What earns it:**

**It forbids the misreading it would most benefit from.** *"It reports no field-wide frequencies and none should be inferred from the examples cited."* A narrative review's standard failure mode is to let a handful of selected examples imply a pattern across a field. This one blocks that in its own Methods, and repeats the block twice more in the body — *"these observations describe the studies selected for this narrative review rather than the frequency of these problems across the entire field."* **Yesterday's entry 71 made frequency claims from a 10.4% response rate. This one declines to make them from 53 purposively selected records.** That contrast is the clearest illustration of epistemic discipline across two consecutive entries that this list has produced.

**It publishes a reconstructable search.** Query strings, retrieval dates and returned records retained; selection criteria **set before screening**; the explicit deprioritisation of diagnosis-only case-control classifiers and single-centre pilots. For a narrative review that is far above the norm, and it is what distinguishes a purposive review from an arbitrary one.

**It separates three things the field routinely conflates** — the measured characteristic, the prediction model, and the intended clinical use — and then separates a fourth: **method family from evidential stage.** *"Method family is not a stage of clinical qualification, and greater complexity does not imply stronger evidence."* That sentence does more work than most review abstracts.

**It gets the reporting-standards taxonomy exactly right**, which almost nothing does: TRIPOD+AI *"specifies how studies… should be reported; it does not prescribe model development or establish low risk of bias,"* PROBAST+AI *"assesses model quality, risk of bias and applicability,"* and DECIDE-AI addresses early-stage live clinical evaluation. **Three standards, three distinct jobs, correctly distinguished** — and then the conclusion that matters: *"Complete reporting enables appraisal, but does not by itself establish validity or utility."* This list spent three consecutive days (entries 69, 70, 71) demonstrating that checklist adherence and methodological care run in nearly opposite directions. Here is a paper that states the principle outright.

**It reports negative results and uses them.** The resting-state fMRI study that failed in 220 and 190 participants. The cross-trial antipsychotic models that dropped to chance. The antidepressant-selection model that barely beat baseline severity. **A review that only cites successes cannot teach you anything about failure modes**, and this one is built around them.

**It names the hardest problem in the field correctly.** The two substitutions, and the structural reason for the second: most treatment-response markers were defined in open-label single-arm data, so **their specificity to a treatment was never knowable.** The anterior cingulate theta example — a marker predicting response to drugs, rTMS, ECT and placebo — is the single best-chosen illustration in any paper decoded here.

**Its limitations section is accurate rather than ritual**, including the admission that the stage assignments are one person's qualitative judgements.

**What keeps it from 5:**

**It is a single author.** No second screener, no inter-rater agreement for study selection, and the framework — the review's central product — is **one person's construction, with its stage assignments explicitly one person's judgement.** For a paper proposing an appraisal instrument that others are invited to use, that is a real limit. PROBAST+AI and TRIPOD+AI were built by large consensus panels precisely because appraisal criteria built by one mind inherit that mind's blind spots.

**Fifty-three records, purposively selected.** The criteria were prespecified and the selection is defensible, and the review disclaims frequency inference — which handles the problem honestly rather than solving it. The framework is nonetheless calibrated against a corpus chosen partly for being externally evaluated or clinically consequential, which is a non-random slice of the field.

**The framework is proposed, not validated.** Nobody has yet shown that two readers applying these six stages to the same paper agree, or that a stage assignment predicts anything. It is a reasoning aid offered in good faith, and it should be used as one.

**And I could not read it.** The full six-stage specification is in a table I cannot reach. **I am grading the review's reasoning, which I have in full, while its central deliverable is partly invisible to me** — and I would rather say so than imply otherwise.

**One unreconciled internal tension**, which Section 5 computes: the review's own 5–15%-of-variance benchmark for reproducible treatment-response prediction sits far below several AUCs it reports approvingly.

**Why not 3.** Because a 3 in this list means "the findings are real but their reach is unknown and the paper sometimes implies it knows." This review consistently does the opposite — it states what it does not know, in the places where overstating would have helped it most.

## 4. The Editor's Concerns

**1. The review's own variance benchmark contradicts several of the AUCs it reports approvingly, and it does not reconcile them.** The review states that reproducible treatment-response prediction in independent data **typically explains about 5 to 15% of outcome variance**, and that a much larger figure in development data **"usually reflects optimism."** Section 5 does the conversion. That band corresponds to roughly **AUC 0.63 to 0.73**. Now take the review's own treatment-response examples: the antidepressant-selection model at AUC 0.65 implies about **6.9% of variance — squarely inside the band.** But the EEG treatment-response meta-analysis at pooled AUC 0.85 implies about **34.9%**, and the schizophrenia multimodal model's **external** AUC of 0.851 implies about **35.1%** — more than double the top of the band. **The review flags the EEG estimate itself** as probably overstating performance, which is consistent. **It does not flag the multimodal result**, which it presents as *"one informative example"* with external validation. So either that study is genuinely exceptional, or the 5–15% band is too conservative, or its external cohort was easier than the band's reference class. **Both numbers are the review's own and both concern treatment response.** Reconciling them would have strengthened the framework considerably, because the band is the single most useful calibration figure in the paper.

**2. A single author proposing an appraisal framework.** The review is candid that the stage assignments are *"qualitative author judgements."* The deeper issue is that the six stages themselves are one person's architecture. The instruments the review correctly praises — TRIPOD+AI, PROBAST+AI, DECIDE-AI — were each produced by multi-disciplinary consensus panels with published Delphi processes, because an appraisal criterion that one expert finds obvious may be one another would reject. **Nothing here is wrong; the framework is sensible and I expect to use it.** But it has not been through the process that makes an appraisal instrument citable as a standard, and it should not be cited as one yet.

**3. The framework is unvalidated in the specific sense that matters.** For any appraisal instrument the first question is **inter-rater reliability**: do two readers applying it to the same paper reach the same stage? That has not been assessed, and with a single author it could not have been. The second question is whether the assignment **predicts** anything — whether stage-4 markers go on to succeed at stage 5 more often than stage-3 markers do. Also unassessed. **Those are the studies that would turn this from a good idea into an instrument**, and the review does not claim otherwise.

**4. Purposive selection with prespecified criteria is better than arbitrary selection, and still shapes the conclusions.** The criteria favour *"large, multicentre, longitudinal, randomised or externally evaluated studies"* and deprioritise *"diagnosis-only case-control classifiers and single-centre pilots."* So the 53-record corpus is **enriched for the better end of the literature** — which means the review's central finding (frequent internal evaluation, fewer independent tests, little prospective evidence) is, if anything, **an optimistic picture of the field.** The review's disclaimer covers this honestly. It is worth saying out loud which direction the bias runs.

**5. The wearable example is the most useful thing in the review and deserves more than a paragraph.** AUC 0.772, base rate **5.3%**, positive predictive value **16.7%**, review burden **20 per 100 patient-days.** I verified those three figures are mutually consistent — they reproduce at a sensitivity near 0.65 and a specificity near 0.82. What they mean: **five of every six alerts are false**, and a service carrying 100 patients receives about 20 alerts a day of which roughly 3 are real. That is the whole argument about whether predictive monitoring is deployable, in four numbers, and the review has it. **It is in a sentence in the middle of a paragraph about speech and sensors.** For a review organised around the gap between performance and utility, this example *is* the thesis.

**6. The review quietly contains the strongest available argument against its own field's optimism, and does not foreground it.** Five million participants, 635 loci, **5.8% of liability explained** — which Section 5 converts to AUC **0.637**. The largest study in the review produces, by a wide margin, the weakest predictor. **Sample size bought discovery of real biology; it did not buy a clinical test.** The review reports this correctly and moves on. It is arguably the most important single data point for anyone deciding whether to fund the next large cohort versus the next validation study.

**7. "Readiness" as a single stage number invites the misuse the review warns about elsewhere.** A readiness value *"records the highest stage demonstrated among the studies cited here."* But the highest stage demonstrated by **any** study of a method family tells you little about a **specific** marker — and a single ordinal number is exactly the kind of summary that gets extracted into a slide and compared across rows. The review is careful that *"development may return to earlier stages when the population, assay or model changes,"* which is right. **A stage number is a property of a claim, not of a method.** I would expect this to be misquoted within a year.

**8. The agent evidence is honestly labelled and still load-bearing in a way worth noting.** Every autonomous-discovery example — Robin and ripasudil, Co-scientist, the ML research workflow — comes from **outside psychiatry**, and the review says so each time and states plainly that *"no direct evidence yet shows that an autonomous agent can discover and qualify a psychiatric biomarker."* Good. But the review's forward-looking claim, that agents shift the bottleneck from proposing candidates to qualifying them, rests entirely on these out-of-field examples. **That is a reasonable extrapolation and it is an extrapolation**, and the asymmetry at the heart of the paper — cheap to produce, expensive to qualify — is therefore partly argued from analogy.

**9. No funding or competing-interest statement in what I retrieved**, in a review that assesses a commercial pharmacogenomic test (reporting response relative risk 1.3 and remission 1.41 for *"one weighted multigene test"*) and discusses two named drug-development programmes. **The review itself flags that for the pharmacogenomic evidence** *"absolute benefit, comparator and sponsorship remain important to interpretation"* — good practice applied to others' work. Almost certainly an extraction gap; a reader should confirm it at the article.

**10. A small but real gap: the review recommends comparison against a simple baseline and does not always supply one.** Stage 3 is defined as internal evaluation *"against a simple baseline,"* and the review's sharpest critique is of a model that *"improved little over baseline severity"* — AUC 0.65 against 0.61. **That is exactly right, and it is the only example where the baseline is given.** For the psychosis-risk C-index of 0.79, the static model at 0.76 serves as one. But for the bipolar model at 0.82–0.87, the speech model at 0.879, the EEG pooled 0.85 and the multimodal 0.851, **no baseline is reported** — so by the review's own Stage 3 criterion, the reader cannot judge incremental value for four of its headline examples. The underlying studies may not have reported them, which would itself be worth stating.

**11. Credit for a distinction almost everyone misses.** *"These models estimate associations unless the design and estimand support a causal interpretation."* And on causal machine learning: it can estimate treatment-effect heterogeneity **"when the study design, causal assumptions and measured covariates support that estimand,"** with estimated policies requiring *"prospective comparison with usual care before they can establish benefit."* **Naming the estimand, rather than the algorithm, as what licenses a causal reading is the correct move**, and it is rare.

## 5. Statistics Spotlight

Ten techniques, numbered from 224 in the running list in `queue.md`. The first three are the load-bearing ones, and the first is a piece of arithmetic worth memorising.

**Converting explained variance to AUC — and using it as an optimism detector.**

The review hands you a calibration figure and does not fully exploit it: **reproducible treatment-response prediction in independent data typically explains about 5 to 15% of outcome variance**, and more than that in development data *"usually reflects optimism."*

To use that, you need to translate between variance explained and the AUC that papers actually report. The chain is three steps:

$$r = \sqrt{R^2}, \qquad d = \frac{2r}{\sqrt{1-r^2}}, \qquad \text{AUC} = \Phi\!\left(\frac{d}{\sqrt{2}}\right)$$

where $\Phi$ is the normal cumulative distribution. Running it forwards:

- **5% of variance → AUC 0.627**
- **10% → AUC 0.681**
- **15% → AUC 0.724**
- 20% → AUC 0.760
- 30% → AUC 0.823
- **40% → AUC 0.876**

**So the review's "reproducible" band is roughly AUC 0.63 to 0.73.** Now run it backwards on numbers the review itself reports for treatment response:

- Antidepressant selection, **AUC 0.65 → about 6.9% of variance.** Inside the band.
- EEG treatment response, pooled **AUC 0.85 → about 34.9%.** The review says this probably overstates performance; the arithmetic says the same.
- Schizophrenia multimodal, **external AUC 0.851 → about 35.1%**; discovery **0.874 → 39.6%.**
- Metabolic subtype-specific discrimination, **AUC 0.942 → about 55.3%.**

**That last one is the technique's whole value.** An AUC of 0.94 for a psychiatric outcome means a model claiming to explain **over half the variance** in who gets better. Stated that way it is implausible on its face — and you reached that judgement from the reported number alone, without reading the methods.

**The everyday version.** Someone tells you their model predicts height with an AUC of 0.95 from shoe size. Shoe size and height genuinely correlate, maybe r = 0.7, which is about 50% of variance — so 0.95 is in the right neighbourhood and you believe it. Now someone claims AUC 0.95 for predicting which of two antidepressants will work better. **That implies a correlation with outcome stronger than shoe size with height, for a decision that expert psychiatrists make barely better than chance.** The number is the claim, and the claim is extraordinary.

**Watch out for two things.** First, **this conversion assumes roughly normal, equal-variance distributions**, so treat the numbers as approximate — they are a smell test, not an estimator. Second, **the 5–15% band is specifically for treatment-response prediction.** Diagnosis against healthy controls can legitimately reach much higher, because that is an easier problem. Applying a treatment-response benchmark to a diagnostic AUC would be the mistake the review spends its whole paper warning about. **So the first question is always: variance in *what*?**

**The two substitutions — and what they cost in positive predictive value.**

The review's central methodological finding is that reported metrics routinely answer an easier question than the clinical one, in two specific ways.

**Substitution one: diagnosis in place of differential diagnosis.** The review's example, which I will now put a number on. A schizophrenia classifier kept external **sensitivity 0.75** but **misclassified 59% of bipolar cases and 55% of depression cases.** So against the conditions that actually walk into a psychiatric clinic, its specificity is **0.41** and **0.45** — barely better than a coin.

Now compute what that does. Take an illustrative clinic mix — **my assumption, not the paper's** — of 20% schizophrenia, 20% bipolar, 40% depression, 20% other:

- true positives: 0.20 × 0.75 = **0.150**
- false positives from bipolar: 0.20 × 0.59 = 0.118
- false positives from depression: 0.40 × 0.55 = 0.220
- false positives from other (assume 0.20 rate): 0.20 × 0.20 = 0.040

$$\text{PPV} = \frac{0.150}{0.150 + 0.378} = 28.4\%$$

**About seven in ten positive calls would be wrong.** For contrast, the same sensitivity against *healthy* controls at an assumed specificity of 0.85 and the same 20% prevalence gives **PPV 55.6%.** **The substitution roughly halves the positive predictive value** — and the published headline was measured on the easy comparison while the clinic supplies the hard one.

**Substitution two: prognosis in place of differential treatment benefit.** The review: *"General outcome prediction identifies who is likely to improve. Treatment selection requires an estimate of how outcomes differ between options for the same patient."* Of **19** comparative antidepressant studies in one systematic review, only **7 (37%)** used external evaluation and **only 1 (5%)** directly ranked treatments.

**The everyday version.** You want to know which of two routes to work is faster for you. A model that predicts "you will arrive on time today" is a *prognosis* — it is mostly reading the weather and the hour. It may be highly accurate and still tell you nothing about which route to take. **For that you need the difference between two predictions for the same person on the same day**, and no amount of accuracy on the first question delivers the second.

**Watch out for:** any reported AUC where the comparison group is healthy controls, when the clinical decision involves distinguishing two diseases. **Ask what the model was asked to separate, and whether that is what you would need separated.** The answer is often in one line of the methods and rarely in the abstract.

**Nonspecific prediction: a marker built without a control arm predicts recovery, not benefit.**

This is the structural version of substitution two, and the review's example is as clean as the literature offers.

**Anterior cingulate theta activity** is described as **among the most replicated** markers in psychiatry. It predicts response to antidepressants. It also predicts response to repetitive transcranial magnetic stimulation. And to electroconvulsive therapy. **And to placebo.**

A marker that predicts improvement under *everything*, placebo included, is measuring **a property of the patient's prognosis**, not a property of the match between patient and treatment. It identifies people who are going to get better. That is useful for enriching a trial and useless for choosing a drug.

**And the review names why this keeps happening:** *"Most treatment-response markers in psychiatry were defined in open-label single-arm data and never tested against a control arm, so their specificity to a treatment is unknown."* If everyone in your development set received drug A, then a marker that correlates with improvement cannot be distinguished from a marker that correlates with improving anyway. **The design makes the two indistinguishable, no matter how large the sample or how sophisticated the model.**

**The everyday version.** You notice that students who sit at the front of the class get better grades, and you conclude front-row seating helps. But you only ever observed one class. You cannot tell whether the seat helps, or whether the kind of student who sits at the front would have done better anywhere. **To find out, you have to assign seats** — which is what a control arm is.

**The fix, and the regulatory logic behind it.** The review connects this to the **2019 FDA enrichment guidance** and draws out the consequence precisely: **a trial conducted only in marker-positive participants can establish efficacy in that group, but it cannot show the marker is predictive rather than prognostic.** You need **marker-negative participants** to establish that outcome differences are attributable to marker status. Which is exactly the flaw in the review's ANK3/liafensine example — placebo-controlled efficacy shown in carriers, **no result reported in non-carriers.**

**Watch out for:** the phrase "treatment-response biomarker" attached to a marker developed in a single-arm or open-label study. **The term asserts specificity that the design could not have tested.**

**227. Positive predictive value and alert burden at a realistic base rate.** The wearable example is the review's best. AUC **0.772**, base rate **5.3%**, PPV **16.7%**, burden **20 alerts per 100 patient-days.** I checked those three are mutually consistent: solving PPV for the false-positive rate gives $(1-\text{spec}) = \text{sens} \times \frac{\text{prev}(1-\text{PPV})}{\text{PPV}(1-\text{prev})}$, and at **sensitivity 0.65 with specificity 0.82** the implied burden is **20.6 per 100 patient-days** — reproducing the reported figure almost exactly. **What it means: PPV 16.7% is about one in six, so five of every six alerts are false.** A service carrying 100 patients gets roughly 20 alerts a day, of which about **3 are real and 17 are not.** **An AUC in the high 0.7s sounds deployable and this is what it looks like in a clinic.** Always convert to alerts-per-day and true-alerts-per-day before believing a monitoring tool is usable. And note the review catches the denominator trap itself: **144 people, not 90,281 person-days** — *"the repeated person-days do not constitute independent participants."*

**228. Predictive versus prognostic markers, and why you need marker-negative participants.** A **prognostic** marker tells you what will happen. A **predictive** marker tells you what will happen *differently* under one treatment versus another. They are different claims requiring different designs, and **only a trial that includes marker-negative participants can distinguish them** — because the evidence for prediction is an *interaction* between marker status and treatment, and you cannot estimate an interaction from one level of a factor. **Technique 226 is the mechanism; this is the design consequence.**

**229. Standalone model performance versus the model–user pair.** The review's most striking relayed finding: **1,298 people, models alone identifying the relevant condition in 94.9%, assisted participants doing no better than controls.** **A 94.9% standalone score produced zero measured benefit once a human was in the loop.** The review's conclusion is the right one: *"performance must be evaluated in the intended model-user pair."* This is the same lesson entry 70's technique 194 taught about fitted models versus pipelines, in a different register: **what you deploy is not a model, it is a model plus a person plus a workflow**, and the only valid test is of the whole assembly. Caveat, which the review states: the public rather than psychiatrists, general medical rather than psychiatric scenarios. Indirect, and still the most actionable number in the paper.

**230. The six stages as a reading checklist.** Reduced to questions you can ask of any paper in about two minutes: **(1)** Which decision does this inform, in which population, against which comparator? **(2)** Is the measurement reliable and does the label represent the clinical state? **(3)** Was the whole pipeline evaluated internally **against a simple baseline**? **(4)** Was a **locked** model tested under a shift in site, time, device or population? **(5)** Has **prospective** testing shown model-guided use improves decisions or outcomes? **(6)** Is deployment monitored for drift and subgroup fairness? The review's own shortcut is two questions: **what was the model compared against, and does the reported metric answer the clinical question.** **Those two catch most weak studies.** One caution the review supplies: *"development may return to earlier stages when the population, assay or model changes"* — a stage is a property of a claim, not a permanent rank.

**231. Reporting standards, appraisal instruments and early-evaluation standards do three different jobs.** The review gets this right where almost nothing does. **TRIPOD+AI** says how a prediction-model study should be *reported* — it *"does not prescribe model development or establish low risk of bias."* **PROBAST+AI** *assesses* model quality, risk of bias and applicability. **DECIDE-AI** covers reporting of early-stage *live clinical* evaluation. So: **a paper can follow TRIPOD+AI perfectly and still be a bad study, because complete reporting enables appraisal rather than substituting for it.** Entries 69, 70 and 71 of this list demonstrated exactly that across three consecutive days, with checklist adherence running in close to the opposite order from methodological care. **Never read a named checklist as a quality signal.**

**232. Overall discrimination conceals subgroup error rates.** Aggression prediction in **17,703 patients over 42,719 observation-days**: overall AUC **0.81**, while error rates **differed by race or ethnicity, gender, admission mode, citizenship and housing.** A single AUC is an average over everyone, and averages hide the groups where the errors concentrate — and in a model whose false positives trigger restriction or restraint, **which group absorbs the false positives is the whole ethical question.** **Demand subgroup performance, subgroup calibration, and a statement of what a false decision costs in each group.** This is the same demand technique 202 made of entry 69's use of race as a predictor.

**233. A narrative review that refuses to report frequencies is stronger, not weaker, for refusing.** *"It reports no field-wide frequencies and none should be inferred from the examples cited."* The temptation in any selective review is to let examples imply a rate — "most studies lack external validation" — which a purposive sample cannot support. **By declining, the review keeps its claims inside what its method can carry**, and what remains is a set of existence proofs about failure modes plus a framework for organising them. That is the correct product of a narrative review. **When a narrative review does quote a percentage of the literature, check whether its search was systematic enough to produce one.**

## 6. Jargon Translator

**Biomarker** — a measured characteristic indicating a normal biological process, a disease process, or a response to treatment. The review's definition, and note it says *measured*: a questionnaire score can qualify, and a model's output on its own does not.

**AI-derived biomarker** — such a characteristic whose discovery or interpretation uses an AI method. The review insists on separating this from **the prediction model** that uses it and from **the intended clinical use.**

**Precision psychiatry** — using measured features of a patient, not just clinical judgement, to guide treatment.

**Predictive versus prognostic marker** — predictive tells you which *treatment* will work better for this person; prognostic tells you how they will do in general. Section 5 covers why distinguishing them needs marker-negative participants.

**Differential diagnosis** — telling apart the conditions that could plausibly explain a presentation, rather than telling a condition apart from health. The clinically real task.

**Differential treatment benefit** — how much better this patient would do on drug A than drug B. Not the same as how well they will do.

**Enrichment marker / companion diagnostic** — a marker used to pack a trial with likely responders, versus a test considered essential for a drug's safe and effective use, which may determine eligibility. Different claims, different evidence.

**Polygenic score** — a single number summing many small genetic effects. The review's example explains **at most 5.8% of liability** for depression, from five million participants.

**Normative model** — estimates what a reference population looks like, then measures how far an individual deviates. Distinct from supervised prediction: no outcome label needed.

**Self-supervised learning** — a *training strategy* that learns structure from unlabelled data, so scarce labels can be spent on the final task.

**Foundation model** — a large reusable model, often self-supervised, adapted to several tasks afterwards. **LLMs are language-oriented foundation models.** The review stresses these categories overlap and none of them is a level of clinical evidence.

**Causal machine learning** — methods for estimating how treatment effects differ between people, valid *only* when design, assumptions and measured covariates support that target quantity.

**Estimand** — the quantity you are actually trying to estimate. **Naming it is what licenses a causal reading, not the choice of algorithm.**

**Concordance index (C-index)** — the AUC's sibling for time-to-event data: the probability the model ranks a person who has the event sooner as higher risk.

**Calibration** — whether predicted probabilities match observed rates. A model can rank perfectly and still have badly wrong percentages.

**Decision-curve analysis / net benefit** — weighs true against false positives across the thresholds a clinician might actually use. Answers "would acting on this help?" rather than "does it rank well?"

**Leakage** — when preprocessing, feature selection or tuning sees evaluation data, inflating performance. Prevented by resampling the *whole* pipeline and locking a held-out set.

**Shortcut learning** — the model distinguishes scanner, site or documentation style instead of the disease. Caught by testing across sites, not by another internal accuracy estimate.

**Modality dominance** — one data channel carries a multimodal model's whole result while the others add cost. Caught by testing against the best single-modality model.

**Version drift** — a hosted model's output changes under an unchanged prompt. A reproducibility problem unique to models you do not control.

**Locked model** — weights and preprocessing frozen before evaluation. Stage 4 requires it; retraining at the new site tests something different.

**TRIPOD+AI / PROBAST+AI / DECIDE-AI** — how to report a prediction-model study; how to appraise its bias and applicability; how to report early live clinical evaluation. Section 5 on why the three are not interchangeable.

## 7. What You Can (and Can't) Say

**You can say:**

"A 2026 narrative review of AI in psychiatric biomarker discovery concludes that producing candidate markers is becoming cheap while qualifying them is not, and that none of the AI capabilities it reviewed has yet reached the stage at which a candidate becomes a clinical test."

"Across the studies it selected, discrimination was stronger in development data than in independent evaluation, and prospective evidence that model-guided care improves outcomes was scarce."

"Reported metrics frequently answer an easier question than the clinical one — diagnosis against healthy controls instead of differential diagnosis, and general prognosis instead of differential treatment benefit."

"One of psychiatry's most replicated response markers, anterior cingulate theta activity, predicts response to antidepressants, rTMS, ECT and placebo — so it identifies patients who recover rather than patients who benefit from a specific treatment."

"In one randomised study of 1,298 people, language models alone identified the relevant condition in 94.9% of general medical scenarios, while participants given the model to assist them did no better than controls."

"The review proposes a six-stage framework from intended use through monitored deployment, and offers two screening questions: what was the model compared against, and does the reported metric answer the clinical question."

**You cannot say:**

"Most AI psychiatry studies lack external validation," or any percentage of the field. **The review explicitly forbids this inference** — *"it reports no field-wide frequencies and none should be inferred from the examples cited"* — because its 53 records were purposively selected.

"This is the standard framework for appraising AI biomarkers." It is a **single author's proposal**, published once, with stage assignments the author describes as qualitative judgements, and with no inter-rater reliability assessed. TRIPOD+AI and PROBAST+AI are consensus instruments; this is not yet one.

"AI biomarkers don't work." The review's claim is about **evidential stage**, not about biology. Several examples show real signal with real external validation; what is missing is prospective evidence that *using* them improves care.

"Polygenic scores are useless for depression." They explain **at most 5.8% of liability** in the best-powered ancestry — too little for an individual clinical test, which is a different statement from useless, and the 635 loci are real biology.

"Language models can diagnose psychiatric illness." The review supports **two bounded research uses** — extracting phenotypes from clinical text and structuring literature — and states that evidence for autonomous clinical decision-making is insufficient.

"AI agents can discover biomarkers." Every autonomous-discovery example in the review is **from outside psychiatry**, humans framed the problems and ran the experiments, and a formal benchmark found current systems **below the standard required for autonomous discovery.**

"The pharmacogenomic test works, so gene-guided prescribing is established." That evidence concerns **one specific weighted multigene test**, did not evaluate an AI-guided intervention, and the review itself flags that absolute benefit, comparator and sponsorship matter to interpretation.

"A readiness stage of 4 means the marker is nearly ready." A stage number records **the highest stage demonstrated among the cited studies for that capability**, not the status of any particular marker — and the review notes development can return to earlier stages when anything changes.

**The honest one-sentence version:** *one author read 53 deliberately chosen studies and concluded that AI has made psychiatric biomarker candidates cheap to generate and no cheaper to prove, that the metrics the field reports routinely answer an easier question than the clinical decision they are offered for, and that nothing reviewed has yet been shown to improve a patient's care — then proposed a six-step ladder for telling those situations apart, which is useful, sensible and so far entirely untested as an instrument.*

## 8. Bottom Line for Your Life

**If you are a patient or a family member:** nobody can currently offer you a blood test, brain scan or voice recording that reliably tells you which psychiatric medication will work for you. **That is this review's central finding and it is worth knowing plainly**, because the marketing around precision psychiatry has run well ahead of it. If a clinic offers you a genetic test to guide prescribing, the honest state of play is that **one specific multigene test has prospective evidence** — a response relative risk of 1.3 in people who had already failed a treatment — and that this is a real but modest effect for one product, not a general validation of the category.

**If you are a clinician:** the review's two questions take about two minutes and catch most weak studies. **What was the model compared against?** If a paper reports an AUC with no simple baseline, it has not shown incremental value — and note that the review's own best example is a model reaching 0.65 where **baseline symptom severity alone reached 0.61.** **Does the metric answer the clinical question?** An AUC against healthy controls says nothing about telling schizophrenia from bipolar disorder; Section 5 shows the positive predictive value roughly halving when you move from the easy comparison to the real one.

**If you are offered a predictive monitoring tool:** make the vendor convert their AUC into alerts. The review's wearable example — **AUC 0.772, 5.3% base rate, 16.7% positive predictive value, 20 alerts per 100 patient-days** — means **five of every six alerts are false** and a 100-patient service absorbs around 20 alerts a day to catch about 3 real events. That may still be worth it, depending on what an alert triggers and what a missed episode costs. **It is a staffing decision disguised as a statistic, and you cannot make it from the AUC alone.**

**If you are a researcher in this area:** the review's most actionable sentence is about study design, not analysis. **Most treatment-response markers in psychiatry were defined in open-label single-arm data, so their specificity to a treatment was never knowable.** If you want a predictive marker rather than a prognostic one, **you need a control arm and marker-negative participants** — and no amount of modelling sophistication substitutes. Also worth internalising the variance benchmark: reproducible treatment-response prediction explains about **5 to 15%** of outcome variance, which is **AUC 0.63 to 0.73.** If your development AUC is 0.9, Section 5's arithmetic says you are claiming to explain over 40% of the variance in who gets better, and you should go looking for the leak before you go looking for a journal.

**If you are deciding where to spend money:** the review contains the argument in one comparison. **Five million participants and 635 genetic loci produced a predictor explaining 5.8% of liability — AUC about 0.637.** Meanwhile the review's recurring complaint is the absence of prospective studies, which are comparatively cheap. **Sample size has been buying discovery; it has not been buying clinical tests.**

**If you are reading the coverage of any AI-in-psychiatry paper:** the question that most reliably separates signal from noise is the simplest one in the review. **Not "how accurate is it?" but "accurate at what, compared to what, and has anyone checked whether using it helps?"**

**This is education, not medical advice.** Nothing here should change anyone's medication or treatment. If something in this review bears on your own care, that is a conversation with your psychiatrist.

---

## Appendix: deferred papers and shelf, status on 2026-11-09

**Today's pick, and why it is not the gait paper.** Yesterday's plan was to decode the *Nature Medicine* gait foundation model **if a full text was reachable.** It is not. According to PubMed, converting PMID 42995231 returns **no PMC identifier**, so no PubMed Central copy exists; and Scite's indexed text returned its usual paid-plan error. **Two routes, both closed, three days after publication** — so it joins the deferred list with its clock started today rather than being decoded abstract-only, consistent with this list's standing practice of attempting full text for twenty-one days first. The planned fallback, shelf spare (5), was taken.

**Landmark check for the past week.** According to PubMed, the same four records as yesterday, all previously assessed: the gait model (PMID 42995231), the NEJM AI-scribe case report (42981576), the Nature structRFM RNA model (42983082) and the *Annals* commentary (42970802). **No new candidates, and none displaces the queue.**

**Deferred papers — four now, all re-checked today.**

**1. Gait foundation model — *Nature Medicine* (PMID 42995231, [DOI](https://doi.org/10.1038/s41591-026-04724-9)). NEW to the deferred list, day 1.** No PMC copy; Scite paywalled. **Abstract-only date set at 2026-11-30** under the twenty-one-day rule. It remains the highest-value item outstanding: **1,887 of 3,210 tested phenotypes called significant** is the largest multiplicity problem this list will have faced, and today's entry sharpens the first question to ask of it — the review's 5–15%-of-variance benchmark converts to AUC 0.63–0.73, so a reported **r = 0.91 for BMI** implies about 83% of variance, which for a *learned embedding predicting a physical measurement* is plausible, whereas the same arithmetic applied to its clinical-diagnosis and medication-use predictions is where the scrutiny belongs.

**2. "The anatomy of a personal health agent" — Nature (PMID 42907512, [DOI](https://doi.org/10.1038/s41586-026-11161-8), 659(8139):197-207). Deferred, day 20.** Weekly re-check, next 2026-11-12.

**3. BMJ review of LLM-trial reporting completeness (PMID 42869550, [DOI](https://doi.org/10.1136/bmj-2026-100855), 395:e100855). Deferred, day 27 — its twenty-one-day threshold fires on 2026-11-12, in three days.** Today's entry makes it more relevant again, and from the opposite direction: entries 69, 70 and 71 showed checklist adherence running counter to methodological care, and **today's review states the principle outright** — *"Complete reporting enables appraisal, but does not by itself establish validity or utility"* — while correctly distinguishing TRIPOD+AI from PROBAST+AI from DECIDE-AI. The BMJ review measures completeness at **40% mean TRIPOD-LLM**; today's entry explains why that number is necessary and insufficient.

**4. *Annals of Internal Medicine*, overuse and false restraint in LLM *Choosing Wisely* recommendations (PMID 42896192, [DOI](https://doi.org/10.7326/ANNALS-26-01667)). Deferred, day 20.** Weekly re-check, next 2026-11-12; abstract-only date 2026-11-19.

**Shelf status: one spare remains** — (6) explainable-AI review of 70 prostate and bladder cancer studies (PMID 42960345). **The shelf needs restocking**, and the method that has worked twice before is a `pubmed pmc[sb]` date-window search, which went six-for-six on 2026-10-28 and again on 2026-11-03. **Next run: restock the shelf first, then decode.** If the BMJ review's PMC body is still empty on 2026-11-12 it takes priority that day under the standing rule.

**Watch item:** PM Heart trial results (protocol PMID 42893738), quarterly.
