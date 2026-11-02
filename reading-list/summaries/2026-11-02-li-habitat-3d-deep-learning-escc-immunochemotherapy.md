# Habitat informed 3D deep learning predicts immunochemotherapy response in esophageal squamous cell carcinoma

**Authors:** Li T, Zou T, Li Z, Liu Z, Chen J, Xiong Y, Li M, Zhang X, He P, Guo W, He Y, Wu T, Wu W, Wu Y (fourteen authors — Department of Digital Medicine, College of Biomedical Engineering and Medical Imaging, Army Medical University (Third Military Medical University), Chongqing; Yu-Yue Pathology Research Center, Jinfeng Laboratory; and the thoracic/cardiothoracic surgery departments of The First Affiliated Hospital, Southwest Hospital and Daping Hospital, Army Medical University, Chongqing, China)
**Journal:** iScience, 2026; 29(11): 117782 (published 15 October 2026)
**Decoded:** 2026-11-02
**Analysis basis:** **FULL TEXT** (retrieved from PubMed Central, PMC13691255). The complete body was read, including the STAR★Methods — participant details, treatment regimens, annotation and preprocessing, habitat clustering, feature selection, network architecture and training, and the quantification and statistical analysis section. **The figures and supplementary tables are not retrievable**, so per-model sensitivity/specificity, the calibration curves, the decision curves, the SHAP plots and the backbone comparison table are described from the text only. The GitHub repository URL and the grant numbers were stripped by the text extraction and are therefore **not reproduced here**.

**Source links (verified):**
- DOI: https://doi.org/10.1016/j.isci.2026.117782
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42920785/
- Full text (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC13691255/

**Basis of link verification.** Direct URL fetching is blocked from this session (`doi.org` does not resolve under the network policy here). Verification was done against the live PubMed/NLM record: a query for PMID 42920785 returned this exact title, these fourteen authors, iScience volume 29 issue 11 article 117782, DOI `10.1016/j.isci.2026.117782` and PMC ID `PMC13691255`; the full text was then retrieved from PubMed Central by that PMC ID and matches. Both halves of the chain were confirmed independently.

**Funding: acknowledged, but the funder names and grant numbers were stripped by the text extraction and are not reproduced here.** **Competing interests: declared — "The authors declare no competing interests related to this study."** **Code: deposited on GitHub and stated to be publicly available** (URL stripped by the extraction). **Data: not public; available from the lead contact on request, subject to ethics and privacy restrictions.** **No reporting guideline (TRIPOD, TRIPOD+AI, CLAIM or otherwise) is named.**

**Ethics:** approved by three committees with ID numbers given — First Affiliated Hospital of Army Medical University (KY2025056), Chongqing Banan District People's Hospital (BNLLKY-2025–050) and Daping Hospital (2020MSXM014). Informed consent waived as retrospective. Declaration of Helsinki cited.

> **Why this paper today.** All four deferred papers were re-checked and remain blocked; the JAMA OpenEvidence study (PMID 42879271, PMC13673371) reached **day 18** of serving an empty PMC body. This was spare #5, flagged a week ago for one oddity: an external AUC of **0.927 with a 95% confidence interval of 0.850–0.951**, which sits 0.077 below the estimate and only 0.024 above it. Chasing that down turned out to be worth the day — it is the only asymmetric interval in a paper of nine, and it is almost exactly symmetric around a *different number*. The paper also contains a post hoc power calculation that is the clearest example of a common and circular error this list has seen, and an honest non-significant headline the authors state five separate times.

---

## 1. The Gist

Oesophageal cancer is usually found late. The modern treatment for locally advanced disease combines chemotherapy with immunotherapy before surgery, and it works well — for some people. **About 30% get nothing from it.** Those months of toxicity and cost buy nothing, and may cost the window in which surgery would have helped. So knowing in advance who will respond is worth a great deal, and current markers like PD-L1 are not good enough to decide with.

Fourteen researchers in Chongqing tried something clever with the CT scan everyone already gets before treatment. Instead of averaging measurements across the whole tumour — which is what conventional "radiomics" does — they looked at it voxel by voxel and used clustering to split each tumour into **three "habitats"**: zones that look texturally different from each other and may correspond to healthy tumour tissue, dead or oxygen-starved tissue, and the rim where tumour meets the body's immune cells.

They then fed the scan, the tumour outline and the habitat map into a 3D neural network as **three separate channels**, so the network could see the heterogeneity map alongside the anatomy rather than having the two stitched together afterwards.

**277 patients from three hospitals.** 217 to build on, and **60 from a third hospital, held back entirely, as the test.** On those 60 the network scored an AUC of **0.927**.

Three things make this paper worth reading carefully.

**The simple version nearly matched it, and the paper says so — repeatedly.** A plain gradient-boosted model using nine hand-crafted habitat measurements scored **0.869**, and the formal test of the difference came back **p = 0.343**. The authors state that the deep learning model was only "numerically higher" and not statistically better in the abstract, the results, and twice in the discussion. That restraint is rare and it is the right call.

**The clinical variables were worthless.** Age, sex, BMI, performance status, smoking, drinking and tumour stage, combined in a model, gave an AUC of **0.496** — a coin flip, with a confidence interval straddling 0.5. That one number is the whole justification for the imaging work, and the paper reports it almost in passing.

**And the headline confidence interval does not belong to the headline number.** 0.850 to 0.951 has a midpoint of **0.9005**, not 0.927. Every other interval in the paper is centred on its own estimate. Section 5 works through what that means.

## 2. Study Snapshot

**Study type:** multicentre **retrospective** development and external validation of an imaging-based prediction model.

**Patients:** 277 with locally advanced oesophageal squamous cell carcinoma.
- **Training cohort: 217** — Centre A (First Affiliated Hospital of Army Medical University, January 2020 to August 2022) and Centre B (Chongqing Banan District People's Hospital, January 2020 to December 2022). **156 responders, 61 non-responders.**
- **External test cohort: 60** — Centre C (Army Specialty Medical Center, **September 2022 to August 2024**), "held out from model training and validation and was used only for external testing." **40 responders, 20 non-responders.**

**Worth noticing, and the paper does not say it:** Centre C is not only a different hospital, it covers a **later and non-overlapping time window**. That makes the external test simultaneously geographic and temporal, which is a stronger design than either split alone.

**Response rates by centre:** 71.7%, 73.1% and 66.7% — close enough that the external cohort is not a different population in the way entry 58's was (23.7% versus 45.6%).

**Treatment:** at least two three-weekly cycles of paclitaxel (175 mg/m²) plus cisplatin or carboplatin (70–75 mg/m²), with sintilimab, pembrolizumab or camrelizumab at a fixed 200 mg every three weeks.

**Outcome:** response by **iRECIST**, assessed four weeks after treatment on contrast CT by two senior thoracic surgeons independently, with a chief physician arbitrating disagreements. Dichotomised into responders (complete or partial response) versus non-responders (stable, unconfirmed or confirmed progression). **The paper is explicit that pathological complete response was unavailable** — all patients had definitive non-surgical treatment — **and that survival follow-up was not mature enough to analyse.**

**Imaging harmonisation**, applied identically to all 277 scans: fixed window width/level (300/30 HU), isotropic 1 × 1 × 1 mm resampling by bicubic spline, and background suppression below −150 HU — stated to remove scanner differences in dynamic range, resolution and background intensity.

**Segmentation:** manual, slice by slice, in ITK-SNAP 3.6.0 by two thoracic surgeons with over five years' experience, **blinded to clinical information**, reviewed by a chief surgeon with over ten years' experience, with consensus for discrepancies.

**Reproducibility, quantified** — a first in this reading list. Thirty patients were randomly chosen and independently re-delineated by both surgeons: **intraclass correlation for tumour volume 0.95 (95% CI 0.92–0.97)** and **Dice similarity coefficient for voxel overlap 0.88 (0.85–0.91)**.

**Habitat construction:** a 3 × 3 × 3 sliding window moved voxel by voxel through the tumour, computing **19** local features per voxel across first-order, GLCM, GLRLM, GLSZM and NGTDM families. Vectors were z-scored and clustered by K-means (Euclidean, k-means++ initialisation, 10 restarts, 300 iterations). **The number of clusters was chosen by an objective criterion:** the Calinski–Harabasz index was evaluated from K = 2 to K = 9, peaked at **K = 3**, and decreased monotonically thereafter.

**Feature selection:** **321** habitat radiomics features → univariate testing at **p < 0.05, explicitly "without multiple hypothesis testing correction"** → **41** → Spearman correlation filtering at |ρ| ≥ 0.9 → **24** → LASSO → **9** final features.

**Classical models on those nine features (training / external test AUC):** XGBoost **0.944 / 0.869**, RandomForest 0.854 / 0.775, SVM 0.827 / 0.740, ExtraTrees 0.803 / 0.704.

**The deep learning model:** 3D ResNet-50, ImageNet-pretrained, input tensor 3 × 96 × 96 × 96 (image, binarised mask, habitat map), Adam, learning rate 0.001, batch size 32, 48 epochs. ResNet-18, ResNet-34, ResNet-101 and DenseNet were also compared.

**Headline results on the 60-patient external cohort:**
- Three-channel ResNet-50: **AUC 0.927 (95% CI 0.850–0.951)**; apparent training AUC **0.997 (0.995–0.999)**
- Habitat-radiomics XGBoost: **0.869 (0.773–0.966)** — **DeLong p = 0.343**, not significant
- Two-channel ablation (habitat channel removed, everything else identical): **0.749 (0.617–0.872)** — p = 0.028
- Whole-tumour radiomics XGBoost (no habitat decomposition): **0.719 (0.576–0.833)** — p = 0.008
- Clinical-only L2 logistic regression on eight variables: **0.496 (0.356–0.648)** — p < 0.001
- ResNet-18 external 0.833; ResNet-34 external 0.805

**Calibration curves and decision curve analysis** were performed and reported as favourable; the numerical calibration metrics are in figures that were not retrievable.

**No sample-size calculation was done at the design stage.** A **post hoc power** estimate by Hanley–McNeil approximation reports ">99.9%" power against a null AUC of 0.5 and ">99.9%" against a threshold of 0.75. Section 5 takes this apart.

## 3. How Strong Is This Evidence? (Grade 3/5)

**What this paper does well, and the list is long:**

**Genuine external validation at a third hospital that is also a later time period.** Centre C contributed no training or validation data. Few papers in this list manage one of those; this manages both at once.

**It states its own non-significant headline five times.** The deep learning model beat the simple habitat-radiomics model by 0.058 with **p = 0.343**, and the paper says "numerically higher… not statistically significant" in the abstract, in the results, at the opening of the discussion, and again in the discussion body. After two months of papers that round a null result up to a win, this is worth saying plainly: **the authors declined to claim their own headline.**

**It admits overfitting in its own voice.** "The near-perfect AUC in the training cohort (0.997…) represents an apparent in-sample estimate obtained on data used for model fitting and is therefore likely optimistic. The decrease to an AUC of 0.927… indicates a generalization gap and suggests potential overfitting."

**Three baselines, including a proper ablation, each with a formal test.** Clinical-only, whole-tumour radiomics, and a two-channel version with the habitat map removed and *everything else held identical* — same architecture, same pretrained weights, same ROI size, same optimiser, same learning rate, same batch size, same 48 epochs. That is how an ablation should be specified.

**The ablation's limits are stated explicitly:** "this comparison supports an incremental contribution of habitat information; however, it does not establish that the AUC difference is attributable exclusively to that channel." Almost nobody writes that sentence.

**The number of habitats was chosen by a stated objective criterion** — Calinski–Harabasz peaking at K = 3 with monotone decline after — rather than picked because three looked good.

**Segmentation reproducibility was measured, not asserted.** ICC 0.95 and Dice 0.88 on 30 blinded re-delineations. Since every feature in the paper is computed inside those outlines, this is the foundation, and it is the first time this list has seen it quantified.

**A described and justified harmonisation protocol** applied identically across all three centres' scanners.

**Competing interests declared. Code deposited publicly. Three ethics IDs given.** Entry 64 managed none of those three.

**The absence of pathological complete response and survival endpoints is explained rather than ignored**, with the reason (non-surgical cohort, immature follow-up) and a stated plan.

**Why it is not a 4:**

**The headline confidence interval is not centred on the headline estimate.** 0.850–0.951 has a midpoint of 0.9005 and a half-width of 0.0505. The other eight intervals in the paper have below-to-above ratios between 0.92 and 1.25 — essentially symmetric. This one is **3.21**. Section 5 shows that the lower bound is consistent with a standard interval around 0.927 and the upper bound is not, and **the method used to compute the AUC intervals is never named.** Something is wrong with either the point estimate or its interval, and a reader cannot tell which.

**321 univariate tests at p < 0.05 with no correction, feeding the comparator model.** By chance alone about **16 of the 321** would clear that threshold, against **41 actually retained** — so up to roughly two-fifths of that step's output could be noise before Spearman and LASSO run. The paper states the absence of correction honestly, twice, which does not fix it.

**The post hoc power calculation is circular, and tests the wrong null.** It reports >99.9% power against AUC 0.5 and 0.75 for a model whose own interval starts at 0.850 — while the comparison the paper actually cared about returned p = 0.343. Working backwards from that p-value, **the study had about 16% power for its own headline comparison.** Detail in Section 5.

**The external cohort appears to have informed architecture choice.** Five backbones were compared, and the only basis the text gives for preferring ResNet-50 is that "its external-test AUC was higher than those of ResNet-18 (0.833) and ResNet-34 (0.805)." If the held-out cohort chose the architecture, it is no longer purely held out. Entry 58 faced exactly this and **renamed its cohort** to disclose it; this paper does not raise it.

**Only three of the five backbones' external results appear in the text.** ResNet-101 and DenseNet are named in the Methods and absent from the Results prose.

**The outcome is radiological, not clinical.** iRECIST response at four weeks, from a baseline CT — imaging predicting imaging. Legitimate and clearly stated, but the thing patients care about is unmeasured here.

**No reporting guideline is named.** TRIPOD+AI or CLAIM would fit.

**What would make it a 4:** resolve the interval and name the CI method; report the expected false-positive count for the uncorrected screen, or correct it; compute power for the comparison that matters rather than against a null of 0.5; and prespecify the architecture before touching Centre C.

## 4. The Editor's Concerns

**The interval anomaly is specific and narrow, which is what makes it diagnosable.** It is not that AUC intervals near the ceiling are asymmetric — they should be, with a longer tail downward. It is that **this paper's eight other intervals are not asymmetric at all**, and this one is asymmetric in a way that makes its midpoint 0.9005. A Hanley–McNeil standard error at AUC 0.927 on 40 responders and 20 non-responders is about 0.033, giving roughly 0.863–0.991; the reported lower bound of 0.850 is in that neighbourhood and the reported upper bound of 0.951 is nowhere near it. **The same interval appears in the published abstract, so this is not an artefact of the PubMed Central rendering.** Without the method named, the most a reader can say is that one of the two numbers does not belong to the other — and since the point estimate is what gets cited, that matters.

**A clinical-only AUC of 0.496 is the most important number in the paper and gets one clause.** Eight routine pretreatment variables, combined in a regularised regression, discriminate responders from non-responders **no better than chance**, with an interval of 0.356 to 0.648 that comfortably contains 0.5. That is not a boring control result. It is the finding that establishes there is currently no clinical way to select patients for this treatment — which is precisely why an imaging biomarker would be valuable, and precisely what makes the 0.869 from nine hand-crafted features interesting even without the neural network. The paper reports it inside a list of baselines and never returns to it.

**The simpler model is the practical story and the paper half-tells it.** Nine radiomics features in an XGBoost model reached **0.869**; a 3D ResNet-50 with ImageNet pretraining reached 0.927; the difference was not significant. One of those is reproducible on a laptop from a published feature list; the other needs a GPU, a pretrained backbone and 48 epochs. The authors are scrupulous about the statistics and still frame the deep learning model as the proposal, with the radiomics model as the comparator. On this evidence the ordering could reasonably be reversed.

**The habitat interpretation is a hypothesis presented as an anatomy.** The discussion assigns the three clusters to "viable, perfused tumour," "hypoxic or necrotic regions," and "peripheral interface zones where stromal-immune interactions occur," and reads the SHAP prominence of habitat 3 texture as consistent with that. The paper does flag that "point-to-point pathological validation was unavailable" and that "their biological meaning requires further pathological validation." Credit for that — but K-means on 19 texture features produces three clusters whether or not they correspond to biology, and the assignment of which cluster is which is unconstrained by any measurement here.

**The SHAP analysis explains the model that was not chosen.** SHAP was computed "for the optimal habitat-radiomics model" — the XGBoost — not for the three-channel ResNet-50 the paper proposes. So the interpretability section describes the comparator, and the headline model remains uninterpreted. That is a defensible practical choice (SHAP on a 3D CNN is hard) and it should be said more clearly than it is, because a reader skimming will take the habitat-3 texture story as an explanation of the 0.927.

**The non-responder count is the real sample size.** Sixty external patients sounds reasonable; **20 non-responders** is the number that governs every interval on that cohort. Against the nine final features that is 6.8 events per feature; against the 321 screened it is 0.19.

**Where I am uncertain, stated plainly.** The figures and supplementary tables were not retrievable, so I cannot report sensitivity, specificity, accuracy, PPV or NPV for any model; cannot read the calibration intercept or slope, or any calibration metric beyond the text's assertion of "high concordance"; cannot see the decision curves; cannot see the SHAP plots beyond the two feature names given; and cannot see the backbone comparison table. The CI anomaly is an observation about the published numbers, **not a claim about what the correct interval is** — I have not asserted a typo. The GitHub URL and grant numbers were stripped by the extraction and **I have not guessed at them**.

## 5. Statistics Spotlight

Three things. The second one is an error common enough that spotting it is worth more than most of what this list has taught.

### Check whether a confidence interval is centred on its own point estimate

A confidence interval and the estimate it belongs to are computed from the same data, so they have to fit together. When they don't, something has gone wrong in the reporting, and you can often see it with arithmetic alone.

The paper's headline: **AUC 0.927 (95% CI 0.850–0.951)**.

Measure the two arms:

> below the estimate: 0.927 − 0.850 = **0.077**
> above the estimate: 0.951 − 0.927 = **0.024**

A ratio of **3.2 to 1**. Now check whether that is just how this paper reports intervals, by measuring all nine:

- habitat XGBoost 0.869 (0.773–0.966) → ratio **0.99**
- clinical-only 0.496 (0.356–0.648) → **0.92**
- whole-tumour radiomics 0.719 (0.576–0.833) → **1.25**
- two-channel CNN 0.749 (0.617–0.872) → **1.07**
- ExtraTrees 0.704 (0.558–0.851) → **0.99**
- RandomForest 0.775 (0.646–0.904) → **1.00**
- SVM 0.740 (0.588–0.892) → **1.00**
- ResNet-50 training 0.997 (0.995–0.999) → **1.00**
- **ResNet-50 external 0.927 (0.850–0.951) → 3.21**

Eight symmetric, one not. And the odd one out has a revealing midpoint:

> (0.850 + 0.951) / 2 = **0.9005**, half-width **0.0505**

**It is a symmetric interval around 0.9005.** So either the interval was computed for an AUC of about 0.900 and paired with a point estimate of 0.927, or the upper bound is wrong, or something else happened — but the two numbers as printed do not describe one estimate.

Sanity-check it with the standard formula. Hanley and McNeil's approximation for the standard error of an AUC, at 40 responders and 20 non-responders:

- at AUC 0.927: SE ≈ 0.033, so a symmetric 95% interval is about **0.863 to 0.991**
- at AUC 0.900: SE ≈ 0.039, so about **0.823 to 0.977**

The reported **lower** bound of 0.850 is in the right region for a 0.927-centred interval. The reported **upper** bound of 0.951 is far too low for one. And the method used to compute the AUC intervals is never stated anywhere in the paper.

**The technique, and it takes ten seconds:** subtract the lower bound from the estimate, subtract the estimate from the upper bound, and compare. For most statistics the two should be similar. For a bounded quantity near its ceiling — an AUC near 1, a proportion near 100% — expect the lower arm to be longer, and expect it **consistently across the paper**. A single interval whose asymmetry is wildly out of line with its neighbours is a reporting error, not a feature of the statistic.

**The watch-out:** readers quote point estimates and ignore intervals, so an interval that contradicts its estimate propagates silently. This one is already in the published abstract. **If an interval and its estimate disagree, trust neither until the method is named.**

### Post hoc power is circular — and the tell is which null it is tested against

The paper states:

> "Because this was a retrospective multi-center study, no sample-size calculation was performed at the design stage. A post hoc statistical power was estimated by Hanley–McNeil variance approximation. On the external test cohort… the observed AUC of 0.927 yielded power >99.9% against a null AUC of 0.5 and >99.9% against a clinically meaningful threshold of 0.75."

Two problems, and the second is the useful one.

**First, power computed from the result you got is circular.** Power asks: *if* the true effect were some size, how often would a study of this size detect it? It is a question you ask **before** collecting data, using an effect size you hypothesise. Feed in the effect you actually observed and the answer becomes a deterministic re-expression of your p-value: a significant result always yields high "observed power," a non-significant one always yields low. It adds no information. The confidence interval already tells you everything post hoc power pretends to, and this paper reports those.

**Second, and more telling: the nulls tested are not the ones in dispute.** Nobody doubted that this model beats a coin flip. The claim at stake is that the three-channel network beats the simple habitat-radiomics model — 0.927 versus 0.869 — and that comparison returned **p = 0.343**.

You can recover the power for *that* comparison from the p-value itself. A two-sided p of 0.343 corresponds to **z = 0.948**. The observed difference was 0.058. So:

> standard error of the difference = 0.058 / 0.948 = **0.0612**

And the power to detect a true difference of 0.058 at the conventional 5% level is:

> Φ(0.058 / 0.0612 − 1.96) = Φ(0.948 − 1.96) = Φ(−1.012) = **about 16%**

**The study had roughly a one-in-six chance of detecting its own headline difference, in a paper reporting >99.9% power.** Both figures are correctly computed; they answer different questions, and only one of them matters.

How many patients would the comparison need? The standard error scales with 1/√n, and 80% power requires SE ≈ 0.058 / (1.96 + 0.84) = 0.0207:

> n ≈ 60 × (0.0612 / 0.0207)² ≈ **524 patients**

That is a far more useful sentence than ">99.9% power," and it is computable from numbers the paper already prints.

**The everyday version.** Suppose you want to know whether a coin is biased, flip it ten times, get six heads, and then announce "I had enormous power to detect a two-headed coin." True, and irrelevant — nobody suspected a two-headed coin. The question was whether the bias is 50/50 or 55/45, and ten flips cannot tell. **Power against an absurd alternative is always high; it is reassurance about nothing.**

**The watch-out:** when you see post hoc or "observed" power, especially against a null of chance performance, read it as a flag rather than a reassurance. Then find the comparison the paper actually rests on and check whether its p-value was anywhere near significance. If it was not, the study was underpowered for its own claim regardless of what the power section says.

### Two agreement numbers on the same data, and why one is kinder than the other

This paper does something this list has been waiting for: it measures whether the human step everything depends on — drawing the tumour outline — is reproducible. Thirty patients were re-delineated independently by both surgeons, blinded, and two numbers are reported:

> **Intraclass correlation coefficient (ICC) for tumour volume: 0.95 (95% CI 0.92–0.97)**
> **Dice similarity coefficient (DSC) for voxel overlap: 0.88 (0.85–0.91)**

These are not two measurements of the same thing, and the gap between them is instructive.

**ICC** is the continuous cousin of Cohen's kappa, which this list covered twice last week. It compares the variation *between patients* with the total variation:

> ICC ≈ between-subject variance ÷ (between-subject variance + measurement error)

So it answers: **do the two readers put the tumours in the same order, relative to how different the tumours are from each other?** And like kappa, it inherits a dependency on the spread of the subjects. Tumour volumes vary enormously — a small lesion and a bulky one differ by an order of magnitude — so the between-subject variance in the numerator is huge, and a reader disagreement of a few cubic centimetres barely dents the ratio. **A wide case mix makes a high ICC easy.**

**Dice** has no such escape hatch. For two outlines A and B:

> DSC = 2 × (voxels in both) ÷ (voxels in A + voxels in B)

It asks whether the readers agree **voxel by voxel**, within each tumour, with no reference to how different the tumours are from each other. Two surgeons can produce volumes within 2% of each other — excellent ICC — while their outlines sit in measurably different places, because one traced slightly wider at the top and slightly narrower at the bottom. Dice sees that; ICC cannot.

A Dice of 0.88 is good for manual tumour segmentation on CT. It also means roughly **12% of the delineated volume is not agreed**, and every habitat cluster, every one of the 321 radiomics features, and the network's entire input were computed inside outlines carrying that much disagreement.

**The technique:** when a paper reports agreement on a derived summary (volume, a score, a total), ask whether it also reports agreement on the underlying thing (the outline, the individual items). **A high coefficient on a summary can conceal disagreement that a direct overlap measure exposes**, because summaries let errors cancel. Here both are reported, which is why the comparison is available at all — and the honest number is the lower one.

## 6. Jargon Translator

**ESCC (oesophageal squamous cell carcinoma)** — the commoner form of oesophageal cancer in China, over 90% of cases there. Arises from the flat lining cells.

**Locally advanced** — grown beyond the earliest stage and possibly into nearby lymph nodes, but not spread to distant organs.

**Immunochemotherapy (ICT) / neoadjuvant** — chemotherapy plus an immune checkpoint inhibitor, given *before* definitive treatment. "Neoadjuvant" means before surgery; here treatment was definitive and non-surgical.

**Immune checkpoint inhibitor** — a drug that releases a brake the tumour uses to switch off immune cells. Here sintilimab, pembrolizumab or camrelizumab.

**PD-L1** — the standard protein marker used to guess who will respond. The paper notes it is limited by varying within one tumour, varying over time, and inconsistent testing.

**pCR (pathological complete response)** — no viable tumour left in the surgically removed specimen. The strongest response endpoint, and **unavailable here** because nobody had surgery.

**iRECIST** — standard rules for scoring tumour response on imaging, adapted for immunotherapy (which can make tumours briefly look bigger before they shrink). The outcome used here.

**Radiomics** — extracting large numbers of quantitative texture and shape measurements from a medical image.

**Habitat analysis** — instead of averaging features over the whole tumour, computing them for each voxel's neighbourhood and clustering voxels into sub-regions that look alike. Those sub-regions are "habitats."

**Voxel** — a 3D pixel; one small cube of the scan.

**K-means clustering** — an algorithm that sorts items into K groups, each item joining the group whose centre it is closest to. Used here to create the habitats.

**Calinski–Harabasz index** — a score for how well-separated a clustering is, used here to pick K = 3 rather than guessing.

**GLCM, GLRLM, GLSZM, GLDM, NGTDM** — families of texture measurement. GLCM, the one that dominates the SHAP ranking, describes how often pairs of grey levels occur next to each other; "GLCM correlation" measures how linearly predictable a voxel's brightness is from its neighbour's.

**ROI (region of interest)** — the outlined tumour.

**Dice similarity coefficient (DSC)** — voxel overlap between two outlines, 0 to 1. See Section 5.

**ICC (intraclass correlation coefficient)** — a reliability coefficient for continuous measurements. See Section 5.

**LASSO** — a regression that shrinks weak predictors' coefficients to exactly zero, selecting variables while fitting. Took 24 features to 9.

**XGBoost / RandomForest / ExtraTrees / SVM** — four standard classifiers. XGBoost builds trees in sequence, each correcting the last.

**3D ResNet-50 / ImageNet-pretrained** — a 50-layer convolutional network adapted to work on volumes rather than flat images, started from weights learned on a large general photograph dataset.

**Three-channel input** — feeding the network the scan, the tumour mask and the habitat map as three stacked layers, so it sees them together. The paper's central idea.

**Ablation** — rerunning the model with one component removed and everything else identical, to see what that component contributed.

**Apparent performance** — performance measured on the data the model was fitted to. Always flattering; here 0.997.

**AUC** — the share of (responder, non-responder) pairs the model ranks the right way round.

**DeLong test** — the correct test for whether two AUCs computed on the *same* patients differ. Here it returned p = 0.343 for the comparison that mattered.

**Power** — the probability a study would detect an effect of a given size if it were real. Must be specified in advance against a hypothesised effect; computed afterwards from the observed effect it is circular. See Section 5.

**SHAP value** — how much a variable pushed a model's output for one patient away from its average. Here computed for the XGBoost model, not the neural network.

**Decision curve analysis (DCA)** — plots net clinical benefit against "treat everyone" and "treat nobody" across risk thresholds.

## 7. What You Can (and Can't) Say

**Fair to say:**

- ✅ "In 277 patients across three Chinese hospitals, about 30% of people got no response from immunochemotherapy." Consistent with the paper's framing and its centre response rates of 71.7%, 73.1% and 66.7%.
- ✅ "Eight routine clinical variables predicted response no better than chance — AUC 0.496, interval 0.356 to 0.648." Reported, and arguably the paper's most important result.
- ✅ "A model using nine texture measurements from CT sub-regions reached an AUC of 0.869 on 60 patients from a hospital that contributed no training data." Reported.
- ✅ "The deep learning version scored higher, 0.927, but the difference was not statistically significant (p = 0.343)." Stated by the authors five times.
- ✅ "Splitting the tumour into sub-regions beat treating it as one lump: 0.869 versus 0.719 for whole-tumour radiomics." DeLong p = 0.008 against the three-channel model; the habitat-versus-whole-tumour contrast is the substantive finding.
- ✅ "Removing the habitat map from the network dropped its external AUC from 0.927 to 0.749." A properly specified ablation, p = 0.028.
- ✅ "Two surgeons re-outlining 30 tumours agreed with an ICC of 0.95 on volume and a Dice of 0.88 on overlap." Reported, and rarely measured.
- ✅ "The authors say the training AUC of 0.997 is optimistic and indicates possible overfitting." Their words.

**Not fair to say:**

- ❌ "Deep learning outperformed radiomics for predicting immunotherapy response." The difference was 0.058 with **p = 0.343**, and the study had roughly **16% power** to detect it. The paper itself declines this claim.
- ❌ "The model achieves an AUC of 0.927 (95% CI 0.850–0.951)." You can quote the estimate or the interval, but they are not consistent with each other: the interval is symmetric around **0.9005**, every other interval in the paper is symmetric around its own estimate, and the CI method is never named.
- ❌ "The study was well powered." It had >99.9% power against a null of 0.5, which nobody disputed, and about 16% power for the comparison it was built to make. Around **524 patients** would be needed for 80%.
- ❌ "Nine habitat features were robustly selected." They came through a screen of **321 features at p < 0.05 with no multiple-comparison correction**, where about 16 false positives are expected by chance against 41 retained.
- ❌ "The three habitats correspond to viable tumour, necrosis, and the immune interface." That is the paper's hypothesis. It states that pathological validation was unavailable and the biology requires confirmation.
- ❌ "SHAP explains why the deep learning model works." SHAP was computed for the **habitat-radiomics XGBoost model**, not for the three-channel network.
- ❌ "ResNet-50 was the best architecture." Five backbones were compared and the only stated basis for preferring it is its performance on the supposedly held-out external cohort.
- ❌ "The model predicts whether patients will benefit from treatment." It predicts a **radiological response category at four weeks**. Pathological complete response was unavailable and survival follow-up was too immature to analyse — so whether responders live longer is not addressed.
- ❌ "This is ready for clinical use." Retrospective, 60 external patients of whom **20 were non-responders**, no prespecified locked model. The authors call for "prospective multicenter evaluation of a prespecified locked model."

## 8. Bottom Line for Your Life

If you or someone close to you is facing treatment for locally advanced oesophageal cancer, the fact worth taking from this paper is uncomfortable and useful: **roughly three in ten people get no benefit from immunochemotherapy, and at present there is no reliable way to know in advance who they are.** This study's own clinical model — age, sex, BMI, performance status, smoking, drinking, tumour stage — performed **exactly at chance**. That is why oncologists cannot answer "will this work for me" with anything better than population averages, and why so much effort is going into reading the pretreatment scan for clues. The approach here is promising and not yet ready; nothing in it changes a treatment decision today.

For anyone appraising research, this paper hands you two tools, and the second is one of the most broadly useful things in this whole reading list.

**Check that a confidence interval is centred on its own point estimate.** Subtract the lower bound from the estimate; subtract the estimate from the upper bound; compare. Here the headline interval sits 0.077 below and 0.024 above — a 3.2-to-1 asymmetry in a paper where the other eight intervals run between 0.92 and 1.25. And the midpoint of 0.850 and 0.951 is **0.9005**, not 0.927. One of those two numbers does not belong to the other, the method is never named, and the interval is already in the published abstract. **When an estimate and its interval disagree, trust neither until you know how the interval was made.**

**Treat post hoc power as a warning sign, and always ask which null it was tested against.** This paper reports >99.9% power — against an AUC of 0.5, which nobody questioned. The comparison it actually rests on came back **p = 0.343**, and from that single number you can recover the truth: a standard error of 0.061 on a difference of 0.058, meaning about **16% power** for its own headline, and roughly **524 patients** needed for a real test. Power calculated after the fact from the effect you found is a restatement of your p-value in flattering clothes. **The confidence interval already told you what power pretends to, and it does not need a hypothesis to do it.**

And one piece of credit, because it is rarer than any of the above: **these authors had a result that looked like a win and refused to call it one.** Five separate times they wrote that their deep learning model was only "numerically higher" and that the difference was not significant — in the abstract, where almost nobody would have checked. A paper that argues against its own headline is telling you it wants to be understood rather than believed, and that is worth more than the 0.927.

---

## Appendix — deferred-paper status, 2026-11-02

- **Google, "The anatomy of a personal health agent"** (Nature, PMID 42907512): no PubMed Central copy. Unchanged.
- **BMJ, LLM-trial reporting completeness review** (PMID 42869550): no PMC copy; Scite paywalled. Unchanged.
- **Annals of Internal Medicine, Choosing Wisely benchmark** (PMID 42896192): no PMC copy. Unchanged. Standing note: the overuse rate of 5.4% with a 95% CI of 0.6–12.2% is a clustering signature — that interval is almost certainly computed across the 15 recommendations rather than the 4,050 responses.
- **JAMA, "Clinician Use of an AI-Enabled Clinical Information Platform"** (PMID 42879271, PMC13673371): PMC record exists and serves an **empty body for the eighteenth consecutive day.** Standing instruction unchanged — **if still empty on 2026-11-05 (day 21), decode abstract-only and say so explicitly.**

---

*This is an educational analysis of a published scientific paper, not medical advice. Nothing here is guidance about cancer treatment or immunotherapy. If you are facing treatment decisions for oesophageal cancer, discuss them with your oncologist.*
