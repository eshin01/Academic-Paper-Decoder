# Machine Learning Classification of Bipolar Disorder Across Mood States Using Natural Language Processing and Speech Analysis: Observational Study

**Authors:** Yamaguchi Y, Kano Y, Sugihara G, Takemura R, Nakamura H, Shimizu M, Iizuka M, Kitazawa M, Sento A, Takahashi H, Kishimoto T (eleven authors — Department of Psychiatry and Behavioral Sciences, Institute of Science Tokyo; Center for the Promotion of Interdisciplinary Research in Medicine and Life Science, Keio University School of Medicine; Department of Neuropsychiatry, Keio University; Clinical and Translational Research Center, Keio University Hospital; Faculty of Informatics, Shizuoka University; Center for Brain Integration Research, Institute of Science Tokyo. **No commercial affiliations appear on the author line.**)
**Journal:** Journal of Medical Internet Research, 2026; 28: e98094 (published 1 November 2026)
**Decoded:** 2026-11-07

**Analysis basis:** **FULL TEXT** (retrieved from PubMed Central, PMC13723951) — the complete Introduction, Methods, Results, Discussion, Limitations and Conclusion, plus **Tables 1–4 in full**. **Figures 1–3 and the whole of Multimedia Appendix 1 (supplementary sections 1–15, Tables S1–S18) are not retrievable**, along with the audio samples in Appendix 2 and the STROBE checklist. Section 4 names the three specific places where that gap changes what I can conclude — most importantly supplementary section 7, which defines how the multiple-testing threshold was built.

**Source links (verified):**
- DOI: https://doi.org/10.2196/98094
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42967232/
- Full text used: https://pmc.ncbi.nlm.nih.gov/articles/PMC13723951/

**Basis of link verification.** Direct URL fetching is blocked from this session (`doi.org` does not resolve under the network policy here), so verification was done against the live PubMed/NLM record. According to PubMed, a query for PMID 42967232 returned this exact title, these eleven authors with these affiliations, *Journal of Medical Internet Research* volume 28 article e98094, a publication date of 1 November 2026, DOI `10.2196/98094` and PMC ID `PMC13723951`; the full text was then retrieved from PubMed Central by that PMC ID and matches the record. Both halves of the chain were confirmed independently.

**Funding, competing interests and data availability: none of the three appears anywhere in the retrieved text.** I am not reporting them, because I have not seen them. JMIR requires all three, so they are very likely present in the published article and were simply not captured by the full-text extraction — **this is an extraction gap, not an allegation that the statements are missing.** Readers should go to the article for them.

**Reporting guideline: STROBE, named in the Methods, with a completed checklist deposited.** Section 4 notes that STROBE is the checklist for observational studies and that a prediction-model paper would normally also be held to TRIPOD+AI, which is not named.

**Ethics:** approved by the Institutional Review Board of Keio University School of Medicine (**approval 20170388; protocol 2017-0388-23**), per the Declaration of Helsinki. **Written informed consent from every participant**, with the right to withdraw at any time. Data deidentified; audio stored on encrypted servers. Recruitment ran 2017–2024.

---

## 1. The Gist

**This is the most self-critical paper in this reading list, and the criticism lands on its own headline.**

Bipolar disorder is misdiagnosed as ordinary depression in **76.8%** of patients at first presentation, with an average delay of about **six years** before the right diagnosis. That delay is not academic: treating bipolar depression with an antidepressant alone can tip a patient into mania. So an objective test would matter enormously.

This study recorded **61 patients with bipolar disorder and 99 healthy volunteers** across ten sites in Japan over seven years, interviewed them for 30–60 minutes each, and extracted **6,373 acoustic measurements** from the audio plus **211 linguistic measurements** from the transcripts. Then it asked three questions.

**Can voice tell bipolar patients from healthy people? Yes, apparently very well — AUC 0.916.** Sensitivity 0.933, specificity 0.859. That is better than the 0.77 pooled accuracy from previous meta-analyses.

**Is it the words or the sound? The sound, decisively.** Acoustic features alone reached **AUC 0.910**; the words alone managed **0.651**; and putting them together gave **0.911** — meaning the language content added essentially nothing. How you say it, not what you say.

**Can voice tell which mood episode someone is in? Essentially no — and this is the finding that matters.** Depression versus euthymia scraped past chance (AUC 0.760, p=.03). But **mania/mixed versus euthymia (0.601, p=.20) and depression versus mania/mixed (0.569, p=.30) did not.** On that last comparison the model's sensitivity was **0.467 — worse than a coin flip.** The paper's own introduction says treatment "differ[s] markedly between depressive and manic or hypomanic phases." So the decision that actually changes prescribing is the one the method cannot make.

**And then the part that makes this paper remarkable.** Its most exciting claim is that bipolar disorder leaves a permanent acoustic fingerprint — detectable even in **euthymia**, when symptoms are minimal. The euthymic group scored the *highest* state AUC of all, 0.874. The paper then reports, in its own conclusion, that euthymic diagnostic probability was **substantially higher in patients taking antipsychotics (Cohen's d = 1.17, p=.005)**, and concludes that these patterns "cannot presently be attributed to the disorder rather than to its treatment." **Seventy-two percent of the patients were on antipsychotics. None of the controls were.** The authors found the most parsimonious rival explanation for their best result and printed it.

## 2. Study Snapshot

**Study type:** a **cross-sectional machine-learning classification analysis** nested inside a seven-year prospective observational cohort — the UNDERPIN project (Understanding Psychiatric Illness through Natural Language Processing). Prospective collection, cross-sectional analysis: the paper is explicit and repeats the distinction three times.

**Setting:** Keio University Hospital and collaborating institutions — **seven hospitals and three outpatient clinics across Japan.** Data collected 2017–2024.

**Participants: 61 patients with bipolar disorder, 99 healthy controls.** Patients: aged ≥20, DSM-5 or ICD-11 bipolar diagnosis, referred by treating psychiatrists; **18 inpatients, 43 outpatients.** Excluded for comorbid major depressive disorder, schizophrenia, anxiety disorders or dementia. Controls: aged ≥20, no psychiatric history, screened with the MINI and the MMSE, **excluded if MMSE below 27.** All fluent in Japanese, all gave written consent. **No patient changed diagnostic category during the study**, and across the whole UNDERPIN source dataset nobody moved into or out of a bipolar diagnosis — a check worth noticing, because diagnostic migration would invalidate the labels.

**Groups were well matched.** Age **48.3 (SD 15.4)** versus **51.7 (SD 18.0)** years, p=.21. Female **54.1%** versus **55.6%**, p=.98. Symptom scores differed as they should: HAMD-17 **11.1 (SD 7.4)** versus **1.2 (SD 1.6)**, YMRS **5.5 (SD 7.0)** versus **0.2 (SD 0.6)**, both p<.001.

**Visits:** 1 to 5 per participant (bipolar median 3 [IQR 1–5]; controls median 2 [IQR 2–2]), consecutive visits a median of **51 days apart** for patients and 35 for controls, follow-up extending to 37 months. **42 of the 61 patients were recorded in a single mood state; 19 in two or more.**

**The interview, standardised across everyone**, 30–60 minutes, three tasks: **free conversation** (illness history, daily life, sleep, hobbies, work — intentionally unstructured, with interviewers instructed to use neutral words, avoid emotional terms, and follow the participant's account); **picture description** (three images from the Visual Perception Test for Agnosia, COGNISTAT and the Western Aphasia Battery); and **storytelling** (Cinderella or a Japanese folktale). Free conversation was 60–80% of each interview. **Recorded in soundproof booths or quiet rooms, two microphones, interviewer on the left channel and participant on the right so participant speech could be separated afterwards**, 16 kHz, 16-bit. All three tasks merged into one dataset per data point.

**Mood states, defined by score thresholds:** depressive state (**DS**: HAMD-17 ≥8 and YMRS ≤7), state with manic or mixed symptoms (**MS/MX**: YMRS ≥8), euthymic state (**ES**: HAMD-17 ≤7 and YMRS ≤7). The 61 patients produced **78 distinct mood-state labels**: DS 32, MS/MX 20, ES 26 — which sums exactly to 78. Of the 20 in MS/MX, **8 were predominantly manic and 12 had mixed features**; they were merged because of sample size. State characteristics: HAMD-17 **14.9 / 11.2 / 4.0** and YMRS **2.6 / 14.3 / 1.3** for DS / MS/MX / ES. Most patients had **mild to moderate** severity.

**Features. 6,373 acoustic features** from openSMILE 3.0 with the ComParE 2016 set, **minus 2,900 volume-dependent features** deliberately discarded because microphone-to-mouth distance could not be standardised (four openSMILE families: pcm_RMSenergy, audspec_lengthL1norm, audspecRasta_lengthL1norm, audSpec_Rfilt), **leaving 3,473 acoustic candidates** — an exact subtraction, and a genuinely thoughtful exclusion. Plus **211 linguistic features** from three NLP routes: sentiment analysis over Plutchik's eight primary emotions, morphological analysis, and syntactic analysis via GiNZA. Acoustic features were grouped as prosodic, spectral and voice quality, with **MFCCs separated out as their own category** because they are the most consistently reported markers in this literature. **Total candidate pool: 3,684 features.**

**The paper is careful about what its linguistic features are:** they "quantify linguistic patterns… rather than directly assessing clinical symptoms," and syntactic complexity "may hypothetically reflect cognitive processes such as rapid thinking, but these features represent quantifiable linguistic patterns rather than symptom assessments."

**An a priori power analysis — rare enough in this list to name.** Three steps: prior speech/NLP bipolar studies' AUCs of **0.71–0.76** taken as the expected effect; converted to Cohen's d of **0.78–1.0** by the Rice and Harris area-to-d formula; entered into a two-sample t-test power analysis in G*Power (two-tailed α=.05, power=0.8), requiring **17 per group at d=1 and 27 per group at d=0.78.** The paper then reports honestly which comparisons met it: BP vs HC and DS vs HC met both; ES vs HC and MS/MX vs HC met only the d=1 threshold; and among the interstate subgroups (n=15–27) **all but one fell below 27, and the smallest (n=15) fell below 17 as well.**

**Analysis.** One data point per participant, to guarantee independence. For BP vs HC, features **averaged across all of a participant's visits**. For each mood state vs HC, **one qualifying visit chosen at random**. For interstate comparisons, one qualifying visit per state — **and participants meeting criteria for more than one state were excluded from both groups**, leaving DS vs ES (23 vs 17), MS/MX vs ES (15 vs 21, 5 excluded) and MS/MX vs DS (15 vs 27). All features standardised first. **LASSO-regularised logistic regression** throughout.

**Nested cross-validation**, with the outer fold count tied to the smallest group: **10-fold for BP vs HC, 5-fold for everything else.** Inside each outer training fold, **age- and sex-matched undersampling repeated 10 times**, then an inner loop for hyperparameter tuning — yielding **100 models for BP vs HC and 50 for each other task.** Predicted probabilities averaged across the 10 undersampling iterations to give each participant one probability. Metrics computed from participant-level out-of-fold probabilities, **at the Youden-index cut-point for the HC comparisons and at a fixed 0.5 for the interstate comparisons.**

**Statistical validation at two levels.** Feature level: importance based on **selection frequency** across resamples, with significance set at the **95th percentile of a permutation-based null distribution**. Model level: **100 label-shuffling permutations, shuffled at the participant level**, testing whether the observed AUC beat chance. Correlations FDR-corrected (Benjamini-Hochberg, q<0.05) **within analysis batches** (m=203 for the acoustic correlations). And **feature-selection stability explicitly quantified** — the distribution of the number of features selected, per-feature selection frequency, coefficient-sign consistency, pairwise Jaccard overlap, and the chance-corrected **Nogueira index**.

**Results — and all 21 cells of Table 4 reconcile exactly**, which I checked:
- **BP vs HC (60 vs 99): AUC 0.916 (95% CI 0.854–0.958)**, sensitivity 0.933 (56/60), specificity 0.859 (85/99), accuracy 0.887 (141/159)
- **DS vs HC (32 vs 97): AUC 0.805 (0.730–0.905)**, sensitivity 0.750 (24/32), specificity 0.814 (79/97)
- **MS/MX vs HC (20 vs 97): AUC 0.848 (0.814–0.950)**, sensitivity 0.800 (16/20), specificity 0.856 (83/97)
- **ES vs HC (26 vs 97): AUC 0.874 (0.833–0.949)**, sensitivity 0.962 (25/26), **specificity 0.711 (69/97)** — the lowest specificity of the four
- **DS vs ES (23 vs 17): AUC 0.760 (0.685–0.936), permutation p=.03**
- **MS/MX vs ES (15 vs 21): AUC 0.601 (0.457–0.819), p=.20**
- **MS/MX vs DS (15 vs 27): AUC 0.569 (0.412–0.759), p=.30**, sensitivity **0.467 (7/15)**
- Median AUCs across resampled models: BP 0.933, MS/MX 0.908, ES 0.885, DS 0.846
- **Modality-specific: acoustic-only 0.910, linguistic-only 0.651, combined 0.911**, each above chance at model-level permutation p≤.02. Combining modalities changed mood-state AUCs by **at most 0.012**.
- **No individual feature exceeded the permutation threshold in any interstate comparison.**

**Significant features.** Across the four HC comparisons, acoustic features were **97.8% (174/178), 97.5% (118/121), 96.3% (104/108) and 98.4% (123/125)** of those reaching significance; 2–4 linguistic features per comparison also reached it, including the ratio of the case particle "to" (recurring in three comparisons) and sentiment variability — though the paper says these "were selected less stably… and should be interpreted with caution." Trait markers (the ES vs HC set) were **lower-order MFCCs (1, 4, 6)**, harmonics-to-noise ratio and spectral skewness; DS features were **higher-order MFCCs (8, 9, 12)**; MS/MX features were mainly spectral variability measures, **with correlations inconsistent in direction**.

**Severity correlations, a category the paper carefully keeps separate from classification predictors:** HAMD-17 inversely correlated with MFCC 8 variability (**ρ=−0.51**, q<0.001); YMRS inversely with MFCC 6 flatness (**ρ=−0.37**, q=0.008); and anger-related linguistic parameters correlated with mania severity (ρ=0.32 and 0.36, q=0.048 and 0.042) **despite not being significant classification predictors.**

**Medication: all 61 patients were medicated.** Mood stabilisers **77.0% (47/61)**, antipsychotics **72.1% (44/61)**, anxiolytics **49.2% (30/61)**, antidepressants **32.8% (20/61)**, others 85.2%. The six mutually exclusive psychotropic combination patterns **sum exactly to 61**. The sensitivity analysis found **no medication association** for the BP, DS and MS/MX models — but for **ES**, diagnostic probability was higher in antipsychotic users (**Cohen's d = 1.17, p=.005**) and the marker stayed correlated with total medication burden after adjusting for HAMD-17 (**partial ρ = −0.45, p=.02**).

**Stability:** a mean of **168 (SD 119)** features selected per resample for BP vs HC, **116 selected in at least half** of resamples, median coefficient-sign consistency **1**, mean pairwise **Jaccard 0.48** (Nogueira 0.56) — falling to **0.18–0.29** for the mood-state comparisons.

**Not reported, or explicitly absent:** any external validation (none, and stated); any comparison against major depressive disorder or schizophrenia (excluded by design); any unmedicated bipolar group (none existed); within-person longitudinal modelling (deliberately not done, with reasons given); dose-response medication analysis beyond exploratory (daily doses extractable for only a minority of prescriptions).

## 3. How Strong Is This Evidence? (Grade 3 out of 5)

**This is the first paper in this list where the quality of the reporting clearly exceeds the quality of the evidence, and the grade has to track the second.** The conduct and the candour are at a level I would grade 5. The evidence base — 61 patients, 3,684 candidate features, no external validation, and a headline finding the authors themselves flag as possibly a drug effect — is thin. The grade reflects **what a reader can conclude**, not how well the authors behaved. The authors behaved extremely well.

**What a 5-level reporting job looks like, since it is worth cataloguing:**

**An a priori power analysis, with the comparisons that failed it named.** Almost nothing in this list has one. And the paper does not use it as decoration — it states that the interstate subgroups fell below the requirement, which is precisely the information needed to read the three null results correctly.

**Permutation testing at two separate levels** — feature selection *and* model performance — with model-level labels shuffled **at the participant level**, which is the correct unit when a participant contributes one aggregated point.

**Nested cross-validation with the fold count chosen by the smallest group**, so no fold is left with too few training cases.

**Feature-selection stability actually quantified**, with Jaccard overlap and the chance-corrected Nogueira index, and the honest conclusion drawn: feature-level results must be read as selection frequency and direction, "rather than as a fixed feature list." Papers in this field routinely print a top-ten feature table from one model fit. This one explains why that would be misleading.

**A deliberate, well-reasoned exclusion of 2,900 features** because microphone distance could not be standardised — throwing away 45% of the available measurements to avoid a recording artefact masquerading as a biomarker.

**The modality comparison done two ways, with the invalid one flagged by the authors.** They note that acoustic-only versus linguistic-only "cannot be fully separated from the larger search space available to the acoustic models," while combined-versus-acoustic "is a nested comparison and is unaffected by this asymmetry." That is a genuinely sophisticated distinction and Section 5 teaches it.

**The Youden-index optimism flagged, with 0.5-threshold metrics supplied in the supplement.**

**The non-independence of the four HC comparisons flagged** — same controls, 19 patients in multiple state groups.

**"Nonsignificant results indicate that an effect was undetected rather than absent."** That sentence, in the paper's own limitations, is the thing most papers in this list get wrong.

**And the ES/antipsychotic confound placed in the conclusion**, undercutting the paper's most publishable claim.

**Why it is nonetheless a 3:**

**3,684 candidate features and 61 patients.** That is **60 candidate features for every patient in the study**, and for the interstate comparisons the ratio reaches **87 to 102 features per participant**. LASSO narrows this, but the search space is enormous and the paper says so — labelling its own analyses "exploratory and hypothesis-generating" with "provisional" performance estimates.

**No external validation, in a single cohort, in one language.** The paper states that internally validated models "typically show optimism" elsewhere and that **AUC 0.916 should be read as an internal estimate, not transportable accuracy.** Take it at its word.

**The headline trait finding may be measuring medication.** 72.1% of patients on antipsychotics, no controls on anything, and the ES model's probability shifts with antipsychotic use at d=1.17.

**BP-specificity is unknown by construction.** Major depressive disorder and schizophrenia were *exclusion criteria*. So nobody knows whether this detects bipolar disorder or detects "being psychiatrically unwell and medicated" — and the paper's own discussion notes the markers overlap with ones reported for geriatric depression, "suggesting that shared acoustic features may reflect common psychomotor effects rather than disorder-specific signatures." Since the clinical problem is *bipolar misdiagnosed as unipolar depression*, the comparison that would matter most is the one not made.

**The one comparison with direct clinical consequence returns a null from an underpowered test.** Section 5 computes what those nulls could have detected.

**Why not 2.** Because the design is strong where it counts: real psychiatrist-made DSM-5/ICD-11 diagnoses, trained raters, a standardised interview in acoustically controlled rooms, channel-separated audio, ten sites, seven years, consent from everyone, and no diagnostic migration. The measurement is good. The inference is just preliminary, exactly as the authors say.

## 4. The Editor's Concerns

**1. The three null interstate results cannot bear the weight anyone will put on them — and Section 5 shows by how much.** Inverting the paper's own power framework: with n=15 versus 21, and n=15 versus 27, **these comparisons could only reliably detect AUCs of about 0.748 and 0.738 respectively.** The observed values were 0.601 and 0.569 — below the floor. So a *genuinely useful* ability to tell mania from depression, say a true AUC of 0.70, **would have been missed most of the time.** The honest summary is not "voice cannot distinguish mood states" but "this study could not have found out." To the paper's credit it says exactly this. Everyone citing it will get it wrong anyway.

**2. The "96–98% of significant features were acoustic" claim is mostly an artefact of the candidate pool, and the paper's better argument sits right next to it.** Acoustic features were **94.27% of the 3,684 candidates before any analysis ran.** So "97.8% of significant features were acoustic" is a small step up from the base rate, not a dramatic finding. My binomial test on the enrichment: BP vs HC z=+2.00 (p=0.046), DS z=+1.54 (p=0.124), MS/MX z=+0.91 (p=0.365), ES z=+1.99 (p=0.047). **Two of four are marginal and two are not significant at all.** The paper does not compute this. But it independently reaches the same conclusion by the valid route — **the nested comparison**: combined 0.911 versus acoustic-only 0.910 means the linguistic features add nothing, and that comparison is immune to the search-space asymmetry because one feature set contains the other. **Credit the nested argument; discard the feature-count argument.** The conclusion survives; one of the two routes to it does not.

**3. The number of "significant" features is not itself evidence, and the threshold's definition is in a supplement I cannot read.** If the permutation threshold is the 95th percentile of a **per-feature** null, the per-feature false-positive rate is 5%, so under a complete null you would expect about **184 of 3,684 features** to clear it. The paper reports **178, 121, 108 and 125** significant features in its four comparisons — **at or below the chance expectation.** That does *not* mean there is no signal: the model-level permutation tests are significant, so real discrimination exists. It means **the count of significant features carries no information**, and sentences built on that count should be read as descriptive. The paper calls this "family-wise error correction" in one place and "permutation-based thresholding… to account for multiple testing" in another. If the null is a **max-statistic** null, it genuinely is family-wise and my calculation does not apply. **Supplementary section 7 settles this and I cannot reach it.** For a paper this careful, I expect the max-statistic — but I cannot verify it, and the distinction decides how to read every feature-level sentence.

**4. The euthymic paradox is the most interesting thing here, and the most likely explanation is the drugs.** The model separates **asymptomatic** bipolar patients from controls (AUC 0.874) *better* than it separates depressed ones (0.805). Framed as stable trait markers, that is exciting. But: **72.1% of patients were on antipsychotics and no control was on anything**; the ES model's diagnostic probability is higher in antipsychotic users at **Cohen's d = 1.17**; and the marker tracks total medication burden even after adjusting for severity (**partial ρ = −0.45**). Antipsychotics affect arousal, psychomotor activity and articulation — exactly what MFCCs measure. **The paper puts this in its conclusion.** Note also the specificity cost: at the chosen operating point the ES model flags **28 of 97 healthy controls** as bipolar to achieve sensitivity 0.962.

**5. Excluding depression and schizophrenia makes the result unusable for the problem that motivated it.** The introduction's case is that **76.8% of bipolar patients are first misdiagnosed with unipolar depression.** The relevant test is therefore bipolar-versus-unipolar-depression. But major depressive disorder was an *exclusion criterion* — reasonably, since UNDERPIN enrolls those patients separately and comorbidity would confound the signal. The consequence stands: a classifier that separates bipolar patients from *healthy* people does not address the misdiagnosis it was motivated by, because nobody confuses bipolar disorder with health. The paper names BP-versus-MDD as "a critical next step."

**6. "Trait marker" is doing more work than the design supports, and the paper concedes it.** Trait markers are *operationally defined* as features significant in ES vs HC. That is a cross-sectional definition of a longitudinal concept. The paper: "definitive establishment of 'trait' status would require longitudinal within-person confirmation, which our cross-sectional analytical design does not provide." It also explains why it did not model within-person change — irregular, sparse visits (1–5) and small subgroups would be underpowered. Both honest. But **19 patients were recorded in two or more states**, which is the beginning of the within-person data that would settle it, and that analysis is deferred.

**7. The averaging strategy differs between the headline comparison and every other one, which makes them not quite comparable.** BP vs HC averages each participant's features **across all visits**; mood-state comparisons use **one randomly selected visit**. Averaging several visits reduces measurement noise, so the headline AUC of 0.916 benefits from a noise-reduction the state comparisons do not get. Some of the gap between 0.916 and the 0.805–0.874 state AUCs is therefore **method, not biology**. The paper explains its reasoning (a stable occasion-independent estimate for the trait-level comparison) and does not note this side-effect.

**8. Random visit selection with no reported seed or repetition.** Where one qualifying visit was "randomly selected" per participant, a different draw would give different data and so a different AUC. The paper reports fixing a seed for the *modality-specific* reruns — noting seed-to-seed SD ≤0.01 and that 0.911 versus 0.916 is within it — which is exactly the right observation. **It does not report repeating the random visit selection itself** across draws. With n=20 in MS/MX, which visit you pick could matter more than 0.01.

**9. STROBE is named; TRIPOD+AI is not.** STROBE is the right checklist for an observational study and the completed one is deposited. But this paper develops and evaluates a diagnostic prediction model, which is TRIPOD+AI's exact scope. Yesterday's entry 69 named TRIPOD+AI and deposited its checklist; **this paper is in most respects the more rigorous of the two and is held to the less relevant standard.** That is a comment on reporting conventions, not on the work.

**10. A 0.467 sensitivity deserves to be stated as plainly as the 0.916.** On depression versus mania/mixed, at the 0.5 threshold, the model correctly identified **7 of 15** manic/mixed patients. Below a coin flip. Accuracy 0.548. The paper reports it in Table 4 without softening, and concludes that "the overall limited ability to distinguish between mood states within BP represents a significant limitation for clinical monitoring applications." Correct — and worth repeating, because the AUC of 0.916 is what will be quoted.

**11. Credit where it is unusual: feature counts, cohort counts and medication counts all reconcile exactly.** 6,373 − 2,900 = 3,473. 32+20+26 = 78 mood-state labels. 42 single-state + 19 multi-state = 61. The six combination patterns sum to 61. All five medication percentages reproduce to the first decimal. **All 21 cells of Table 4** — seven comparisons × sensitivity, specificity, accuracy, each with its underlying counts — reconcile to the fourth decimal. I found **no arithmetic discrepancy anywhere in this paper.**

## 5. Statistics Spotlight

Ten techniques, numbered from 204. The first three are the load-bearing ones.

**A null result means nothing until you compute what it could have found. Here is that computation.**

The three interstate comparisons returned p-values of .03, .20 and .30. The two non-significant ones will be cited as "voice cannot distinguish manic from depressive states." That is not what they show.

**The idea: minimum detectable effect.** Before you believe a null, ask how big an effect your study could have caught 80% of the time. Anything smaller than that, your study was blind to — so finding nothing tells you nothing about effects below the floor.

The paper hands us the machinery, since its own power analysis converts an AUC into Cohen's d (a standardised difference between two groups' means) and runs a two-sample t-test. Run it backwards.

For 80% power at two-sided α=.05, the noncentrality parameter needs to be about **δ = 2.80**. And

$$\delta = d \times \sqrt{\frac{n_1 n_2}{n_1 + n_2}}$$

so the smallest detectable d is **d_min = 2.80 ÷ √(n₁n₂/N)**. Convert back to an AUC with the relation the paper itself uses, **AUC = Φ(d/√2)**, where Φ is the normal cumulative distribution.

Doing that for each comparison:

- **DS vs ES**, n=23 vs 17: √(391/40) = 3.126, so d_min = 0.896 and **AUC_min = 0.737.** Observed **0.760** — just clears the floor, consistent with p=.03.
- **MS/MX vs ES**, n=15 vs 21: √(315/36) = 2.958, d_min = 0.947, **AUC_min = 0.748.** Observed **0.601** — well below.
- **MS/MX vs DS**, n=15 vs 27: √(405/42) = 3.105, d_min = 0.902, **AUC_min = 0.738.** Observed **0.569** — well below.

**So all three comparisons were blind to anything under roughly AUC 0.74.** An AUC of 0.70 — not spectacular, but clinically interesting for a voice test — would have been missed most of the time in all three. The two nulls are **uninformative**, not negative.

**The everyday version.** You weigh yourself on a bathroom scale marked only in 5-kilogram increments, before and after a diet, and the needle doesn't move. You have not learned that you lost no weight. You have learned you lost less than 5 kilograms. **The instrument's resolution bounds the conclusion**, and a sample size is an instrument's resolution.

**Watch out for:** "no significant difference" presented as equivalence. The two are different claims and the second requires a different design — an equivalence or non-inferiority test with a prespecified margin. The honest form of a small-sample null is "we could not detect a difference smaller than X, and we did not detect one." **The paper writes its own version of this: "nonsignificant results indicate that an effect was undetected rather than absent."** Hold every paper to that sentence.

**Permutation testing as a multiple-comparisons correction: why it beats Bonferroni when your features are correlated.**

The problem: **3,684 candidate features, 61 patients.** Test every feature at p<.05 and you would expect about 184 "discoveries" from pure noise. Something must correct for that.

**Why not Bonferroni.** Dividing α by the number of tests gives .05/3,684 = **0.0000136** — a brutally strict threshold. Bonferroni assumes the tests are independent. **These features are nothing like independent:** MFCC 8's mean, variance, flatness and rising-slope are four views of the same signal, and openSMILE's 6,373 features are built by applying a few dozen summary functions to a few dozen base signals. With heavily correlated tests, Bonferroni is far too conservative — you throw away real findings to control an error rate that was never that high.

**What permutation does instead.** Shuffle the diagnostic labels at random, so any real association is destroyed but **the correlation structure among the features is left completely intact.** Re-run the entire selection procedure on the shuffled data. Record how often each feature gets selected. Repeat many times. You now have an empirical distribution of "how often does this feature get picked when the labels are meaningless?" — and you can set your threshold from that distribution rather than from a formula. **The null distribution inherits your data's real dependence structure for free.**

**A tiny worked example.** Twenty coins, and you want to know whether any is biased. Flip each 10 times; the best performer gets 9 heads. Is that impressive? Bonferroni says compute p for 9-of-10 and divide α by 20. Permutation says: simulate 20 fair coins flipped 10 times each, record the *best* result, repeat 1,000 times, and see how often the best of 20 fair coins reaches 9. (It happens often — about 1 in 6 runs.) So 9-of-10 as the winner of 20 is unremarkable. **The permutation answered the question you actually asked — "is the best of my set surprising?" — rather than a question about one coin in isolation.**

**The paper does this twice over**, which is better practice than most: once for **feature selection** (significance set at the 95th percentile of the permutation null of selection frequency) and once for **model performance** (100 label shuffles, testing whether the observed AUC beats chance). That second test is what makes the interstate p-values of .03, .20 and .30 meaningful at all, and the labels were shuffled **at the participant level** — the right unit, since each participant contributes one aggregated data point. Shuffling at the observation level would have leaked information and produced an over-optimistic null.

**Watch out for the gap between "per-feature" and "family-wise."** If the threshold is the 95th percentile of each feature's *own* null, you have controlled the per-feature error rate at 5% — and across 3,684 features you still expect **about 184 false positives.** To get family-wise control you take the 95th percentile of the **maximum** statistic across all features in each shuffle, which is a much higher bar. **This matters here concretely:** the paper reports 178, 121, 108 and 125 significant features, and ~184 is the per-feature chance expectation. If the null were per-feature, those counts would be entirely consistent with noise at the feature level, even though the model-level test proves real signal exists. The paper calls it "family-wise error correction" in one sentence, which implies the max-statistic; the definition is in supplementary section 7, which I could not retrieve. **When you read a permutation correction, find out which null it is.**

**Comparing two feature modalities fairly: why the search space must match, and why a nested comparison escapes the problem.**

The paper wants to know whether sound or words carry the diagnostic signal. It ran three models: **acoustic-only (3,473 features) AUC 0.910; linguistic-only (211 features) AUC 0.651; combined (3,684) AUC 0.911.**

**The trap.** The acoustic model was allowed to search a feature set **16 times larger.** With a bigger search space you get more chances to find something that fits — some of it real, some of it the noise that happens to look like signal in your sample. So part of the 0.910-versus-0.651 gap could be search space rather than information content. **You cannot cleanly attribute the difference to the modality.** The paper flags this itself: the gap "cannot be fully separated from the larger search space available to the acoustic models."

**The escape.** Compare **combined (0.911) against acoustic-only (0.910).** The combined set *contains* the acoustic set — it is the acoustic features **plus** the 211 linguistic ones. A nested comparison. Adding features can only expand what the model is able to fit, so if adding all 211 linguistic features moves the AUC by **0.001**, those features genuinely carry no additional information beyond what the acoustic features already supply. **That conclusion is airtight and does not depend on dimensionality at all.** The paper says so: the combined-versus-acoustic comparison "is a nested comparison and is unaffected by this asymmetry."

**The everyday version.** Two job candidates, one interviewed for three hours and one for ten minutes, and the first seems better. You have not learned they are better — you have learned you had more chances to find something good. **That is the unmatched comparison.** Now instead: you have already hired the first candidate, and you ask whether adding the second to the team improves output. If output doesn't move, the second adds nothing *given* the first. **That is the nested comparison, and it answers a question you can actually answer.**

**How to fix the unmatched version if you need it.** Give each modality the same number of candidate features — by random subsampling the larger set to 211, repeated many times — or compare each against its own permutation null, which the paper does report (both modalities beat chance at p≤.02). Either restores the comparison.

**Watch out for:** any claim that modality A beats modality B when A was given more features, more preprocessing, or more model-selection attempts. **Ask what each side was allowed to search.** And when the comparison is unfixable, look for a nested version of the question — it is usually the more useful one anyway, because "does adding B help?" is what a practitioner actually needs to know.

**207. When an asymptomatic group classifies better than a symptomatic one, suspect the treatment.** ES (minimal symptoms) hit AUC **0.874** against DS's **0.805**. Read charitably that is a stable trait marker. But check the obvious rival: **72.1% of patients on antipsychotics, zero controls**, and the ES model's probability shifted with antipsychotic use at **Cohen's d = 1.17**. **Whenever a model performs best in the group with the least disease activity, ask what else is uniform in that group but absent from the controls** — medication, care setting, time in the clinic, the recording environment. The paper ran this check and reported the answer against its own interest.

**208. Feature-selection stability, and what a Jaccard index of 0.48 actually means.** The paper reports a mean of **168 (SD 119)** features selected per resample, with mean pairwise **Jaccard 0.48**. Jaccard is intersection over union, so for two sets of ~168 with J=0.48: |A∩B| = 0.48 × (336 − |A∩B|), giving **|A∩B| ≈ 109.** So two resamples agree on about **109 of 168** features and each picks ~59 the other missed — consistent with the paper's "116 selected in at least half of resamples." For the mood-state comparisons Jaccard falls to **0.18–0.29**, meaning the selected sets barely overlap. **The right response is the one the paper takes:** base inference on selection frequency and coefficient-sign direction, not on any single model's feature list. **An SD of 119 on a mean of 168 is itself a warning** — report that spread, and never print a top-ten feature table from one fit.

**209. A sensitivity below 0.5 is a specific and reportable finding.** MS/MX vs DS: sensitivity **0.467 (7/15)**, accuracy 0.548, AUC 0.569. A sensitivity under a half means that for the positive class the model does worse than a coin. It is not an error; it is what weak discrimination plus an unlucky threshold produces, and with n=15 the confidence interval is enormous. **Report it plainly rather than retreating to the AUC** — which the paper does.

**210. Converting an AUC to Cohen's d for an a priori power analysis: useful, with two caveats.** The paper's three-step chain — prior AUCs 0.71–0.76 → Rice and Harris conversion → d = 0.78–1.0 → G*Power t-test → 17–27 per group — is good practice and rare. Two caveats. **The conversion assumes both groups' scores are normal with equal variance**; if the distributions are skewed, the implied d is off. **And a t-test power analysis is an approximation to AUC power** — the proper tools are the Obuchowski or Hanley–McNeil variance formulas for the AUC itself, which account for its particular sampling behaviour. Neither caveat undermines the exercise; both mean the numbers are approximate, and here that is plenty, because the conclusion (interstate subgroups are underpowered) is not close to the line.

**211. Several comparisons sharing a control group are not independent results.** The four HC comparisons all drew on the same ~97 controls, and **19 patients appear in more than one mood-state group.** So the four AUCs are correlated, and you cannot treat "four out of four beat chance" as four independent confirmations. **Observations are independent *within* each comparison — which is what the model needs — but the comparisons are not independent of *each other*, which is what a reader counting successes needs.** The paper flags this explicitly.

**212. A threshold chosen on the data you report is optimistic.** Sensitivity and specificity here come from the **Youden-index cut-point** (the point maximising sensitivity + specificity − 1), selected on the pooled out-of-fold probabilities — so the operating point was tuned on the same numbers used to report performance. The **AUC is unaffected** (it averages over all thresholds), but the sensitivity/specificity pairs are. **The paper flags this and supplies 0.5-threshold metrics in the supplement**, which is the correct remedy. When a paper reports only Youden-point metrics with no prespecified-threshold alternative, treat the pair as a best case.

**213. "Not significant" and "no effect" are different claims.** Technique 204 gives the arithmetic. This is the principle, and the paper's own sentence is the best phrasing of it in this list: **"nonsignificant results indicate that an effect was undetected rather than absent."** It appears in the medication analysis, where small subgroups (20–60 patients) returned nulls. A null from an underpowered test is an absence of evidence, and the distinction is the single most common error in reading clinical research.

## 6. Jargon Translator

**Bipolar disorder** — a condition with episodes of depression and episodes of mania or hypomania (abnormally elevated, expansive or irritable mood with increased energy). The crucial clinical point: antidepressants alone can trigger a manic episode, so getting the diagnosis right changes the treatment.

**Euthymia** — the periods between episodes, when mood is in the normal range. Not "cured"; the diagnosis persists.

**Mixed features** — depressive and manic symptoms at the same time. Harder to treat and harder to classify, which is why this study merged manic and mixed into one group.

**HAMD-17 / YMRS** — clinician-administered rating scales for depression (17 items) and mania severity. Here they define the mood-state labels by threshold.

**MINI / MMSE** — a structured psychiatric interview used to screen controls for any diagnosis, and a cognitive screen (controls needed 27 or above).

**openSMILE / ComParE 2016** — standard open-source software and a standard feature set for speech analysis. The feature set deliberately extracts everything measurable — 6,373 numbers — rather than a chosen few.

**MFCC (mel-frequency cepstral coefficient)** — a compact numerical description of a voice's *timbre*: its tonal colour, independent of pitch and loudness. Built by measuring energy across frequency bands spaced the way human hearing spaces them, then compressing that into about 13 numbers. **Low-order coefficients describe the broad shape of the sound; high-order ones describe fine detail.** They are what makes two people saying the same word at the same pitch sound different.

**Prosodic / spectral / voice quality features** — the rhythm and melody of speech (pitch, pace, pauses); how energy is spread across frequencies; and the mechanical regularity of the vocal folds (jitter, shimmer, harmonics-to-noise ratio).

**Harmonics-to-noise ratio** — how much of a voice is clean tone versus breathy or rough noise. Lower means less regular vocal fold vibration.

**LASSO** — a regression method that shrinks unhelpful predictors' coefficients all the way to zero, so it fits and selects features at once. Essential when you have far more features than people.

**Nested cross-validation** — two loops. The inner one picks model settings; the outer one measures performance on data the inner loop never saw. Without the nesting, tuning on the same data you evaluate on inflates the result.

**Undersampling with age and sex matching** — when one group is much larger, randomly drop members of the larger group so the two match on age and sex. Repeated 10 times here so the result does not hinge on one lucky draw.

**Permutation test** — shuffle the labels, redo the whole analysis, repeat. Builds a "what would chance look like?" distribution that keeps your data's real structure intact. Section 5 explains why this beats Bonferroni for correlated features.

**AUC** — the probability that the model scores a randomly chosen patient higher than a randomly chosen control. 0.5 is a coin flip, 1.0 is perfect.

**Youden index** — sensitivity + specificity − 1. Picking the threshold that maximises it gives the "best balance" point, at the cost of having chosen it using your own results.

**Jaccard index / Nogueira index** — how much two selected feature sets overlap (intersection over union), and a version of that corrected for the overlap you would get by chance.

**False discovery rate (Benjamini-Hochberg)** — a multiple-testing correction that controls the *proportion of your discoveries that are false*, rather than the chance of any false positive at all. Less strict than Bonferroni and usually more useful.

**Trait marker versus state marker** — a feature of the disorder that is always present versus one that comes and goes with episodes. Distinguishing them properly needs following the same person over time, which this paper says it could not do.

**STROBE / TRIPOD+AI** — the reporting checklist for observational studies, and the one for machine-learning prediction models. This paper names and deposits the first.

## 7. What You Can (and Can't) Say

**You can say:**

"In 61 Japanese patients with bipolar disorder and 99 healthy volunteers, a machine-learning model using voice and language features separated the two groups with an AUC of 0.916 in internal cross-validation."

"The signal was almost entirely acoustic. Adding 211 linguistic features to the acoustic model changed the AUC by 0.001."

"Acoustic differences were still detectable when patients were in remission — but the authors report that this particular finding could not be separated from antipsychotic use."

"The model could not reliably distinguish depressive from manic or mixed states (AUC 0.569, not significant), and the authors state this limits its use for monitoring."

"The authors describe their own results as exploratory and hypothesis-generating, and say external validation is required before any claim of clinical utility."

**You cannot say:**

"AI can diagnose bipolar disorder from your voice." Internal cross-validation in one cohort of 61 patients, in one language, with no external validation. The paper says the AUC "should therefore be read as internal estimate[s] rather than as evidence of transportable diagnostic accuracy."

"Bipolar disorder has a permanent acoustic signature." That is the trait-marker claim, and 72.1% of these patients were on antipsychotics while no control was on anything. The paper's own conclusion says these patterns "cannot presently be attributed to the disorder rather than to its treatment."

"Voice analysis cannot distinguish manic from depressive episodes." The study could not have detected an AUC below about 0.74 in that comparison. The null is uninformative, not negative — and the paper says so.

"This could catch the bipolar patients who are misdiagnosed as having depression." Major depressive disorder was an **exclusion criterion**. The comparison that would answer this was not made, and the authors call it a critical next step.

"96 to 98% of the important features were acoustic, so sound matters far more than words." 94.27% of the *candidate* features were acoustic to begin with. The valid version of this claim rests on the nested model comparison, not the feature counts.

"The model is 93% sensitive." At a threshold chosen to maximise the Youden index on the same data being reported. The paper flags this and provides fixed-threshold numbers in its supplement.

"Mood states were tracked over time." They were not. Prospective collection, cross-sectional analysis — one data point per participant, stated three separate times in the paper.

**The honest one-sentence version:** *an unusually careful exploratory study showing that something in the voices of 61 medicated Japanese bipolar patients separates them sharply from healthy volunteers, that it is the sound rather than the words, that nobody yet knows whether it is the illness or the medication, and that it cannot tell which episode a patient is in — which is the question a clinician would actually ask.*

## 8. Bottom Line for Your Life

**If you have bipolar disorder, or love someone who does:** there is no test here you can ask for. What is worth knowing is the direction of travel — researchers are looking for something objective to shorten that six-year diagnostic delay, and this is a careful early step. What this study cannot yet do is the thing that would help most day to day: tell which episode you are heading into. On that question it performed at roughly chance, and the authors say so.

**If you are a clinician:** nothing to change. If a vendor shows you an AUC above 0.9 for voice-based psychiatric diagnosis, the questions this paper answers honestly are the ones to ask them: **was it validated outside the cohort it was built in** (here, no), **were the patients medicated and the controls not** (here, yes — all 61 versus none), **and was it ever compared against the condition you would actually confuse it with** (here, no — unipolar depression was excluded). Most vendors will not answer as straightforwardly as these authors did.

**If you are a researcher in digital phenotyping:** this is the methods paper to copy. The a priori power analysis, the two-level permutation testing, the quantified selection stability, the deliberate exclusion of volume-dependent features, the nested modality comparison, and above all the limitations section. Two things to add. **Report the minimum detectable effect next to every null** — Section 5 shows it takes four lines of arithmetic and it is what stops your null being miscited. And **compute whether your significant-feature count exceeds chance expectation** before building an argument on its composition.

**If you are designing a study in this area:** the binding constraint is not the algorithm, it is the control group. An unmedicated patient group, or a psychiatric comparison group, would be worth more than ten times the sample size of healthy volunteers — because with medicated patients and unmedicated controls, **a model that detects antipsychotics will look exactly like a model that detects bipolar disorder**, and no amount of cross-validation can separate them.

**If you are reading the coverage:** expect "AI spots bipolar disorder from the voice with 92% accuracy." The 0.916 is real as an internal number. The two findings that will not make the headlines are the ones the authors were most careful about: the remission signal may be the medication, and the model cannot tell mania from depression.

**This is education, not medical advice.** Nothing here should change anyone's treatment or medication. If something in this paper bears on your own care, that is a conversation with your psychiatrist.

---

## Appendix: deferred papers and shelf, status on 2026-11-07

**Landmark check for the past week, per the trigger's step 2.** According to PubMed, a search of JAMA, Lancet, NEJM, Nature, Nature Medicine, BMJ and *Annals of Internal Medicine* for AI, machine-learning, deep-learning, LLM or foundation-model titles entered between 2026-10-31 and 2026-11-07 returned **three records, none a primary clinical study**: the NEJM AI-scribe case report already noted yesterday (PMID 42981576, [DOI](https://doi.org/10.1056/NEJMclde2600746)); **a Nature structure-guided RNA foundation model, structRFM** (PMID 42983082, [DOI](https://doi.org/10.1038/s41586-026-11210-2), 21 million RNA sequence-structure pairs, with dataset, weights and code openly released) — genuinely significant work, but computational structural biology with no patients and no clinical decision, so outside this list's scope; and an *Annals* **Annals On Call** commentary on AI risk and accountability (PMID 42970802, [DOI](https://doi.org/10.7326/ANNALS-26-04494-OC)). **None displaces the queue pick.**

**Deferred papers — all three re-checked today; none has a PMC copy.**

**1. "The anatomy of a personal health agent" — Nature (PMID 42907512, [DOI](https://doi.org/10.1038/s41586-026-11161-8), 659(8139):197-207).** **Deferred, day 18.** Weekly re-check, next 2026-11-12.

**2. BMJ review of LLM-trial reporting completeness (PMID 42869550, [DOI](https://doi.org/10.1136/bmj-2026-100855), 395:e100855).** **Deferred, day 25 — reaches its own twenty-one-day threshold on 2026-11-12, when the abstract-only rule fires.** Today's entry sharpens its relevance again: this paper names and deposits **STROBE** but not **TRIPOD-LLM or TRIPOD+AI**, while being methodologically stronger than most papers that do — exactly the mismatch between reporting-checklist adherence and actual rigour that the BMJ review is built to quantify (it found mean TRIPOD-LLM completeness of **40%**).

**3. *Annals of Internal Medicine*, overuse and false restraint in LLM *Choosing Wisely* recommendations (PMID 42896192, [DOI](https://doi.org/10.7326/ANNALS-26-01667)).** **Deferred, day 18.** Weekly re-check, next 2026-11-12; abstract-only date 2026-11-19. Standing note unchanged: its **5.4% (95% CI 0.6%–12.2%)** overuse rate has an interval computed across the **15 recommendations**, not the 4,050 responses — the correct choice for clustered data, and a clustering signature visible from the interval width alone.

**Shelf status: three spares remain** — (4) NOTIFY-DISCUSS qualitative study of a deployed AI screening tool (PMID 42965008); (5) precision-psychiatry six-stage framework review (42947584); (6) explainable-AI urology review of 70 studies (42960345). **Next run takes spare (4)**, which will be the **first qualitative study in this list** — patient and clinician perceptions of an AI tool actually in clinical use. After sixty-nine quantitative entries that is a deliberate change of instrument, and the natural place to teach what qualitative evidence can and cannot establish, and why "n=20" means something entirely different in a qualitative design than it did in today's interstate comparisons.

**Watch item:** PM Heart trial results (protocol PMID 42893738), quarterly.
