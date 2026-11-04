# Deep learning based detection of active pulmonary tuberculosis from chest radiographs in a retrospective prospective multicenter study

**Authors:** Tuersun A, Abudoubari S, Xu J, Ma J, Nijiati P, Warisi X, Chen X, Li Y, Zou X, Huang C, Nijiati M (eleven authors — Department of Radiology and Clinical Medical Research Center, The First People's Hospital of Kashi Prefecture; Xinjiang Key Laboratory of Artificial Intelligence Assisted Imaging Diagnosis, Kashi; Xinjiang Academy of Medical Sciences, Urumqi; The Fourth Affiliated Hospital of Xinjiang Medical University. **Four authors — Xu J, Chen X, Li Y and Huang C — are at Beijing Deepwise & League of PHD Technology Co., Ltd**, a commercial medical-AI company.)
**Journal:** iScience, 2026; 29(11): 117960 (published 20 October 2026)
**Decoded:** 2026-11-04
**Analysis basis:** **FULL TEXT** (retrieved from PubMed Central, PMC13697335), including the complete STAR★Methods — participant details, reference-standard definitions, preprocessing, architecture, training configuration, the ablation and benchmarking protocols, the reader-study design and the statistical analysis section. **The figures and supplementary tables are not retrievable**, so the ROC curves, calibration curves, confusion matrices other than the prospective one, Grad-CAM images, the full ablation table, the per-architecture metric table and the subgroup table are described from the text only. The paper's stated code repository address appears in the retrieved text and is reported below as the paper gives it; **I could not fetch it to confirm its contents.**

**Source links (verified):**
- DOI: https://doi.org/10.1016/j.isci.2026.117960
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42936410/
- Full text (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC13697335/

**Basis of link verification.** Direct URL fetching is blocked from this session (`doi.org` does not resolve under the network policy here). Verification was done against the live PubMed/NLM record: a query for PMID 42936410 returned this exact title, these eleven authors, iScience volume 29 issue 11 article 117960, DOI `10.1016/j.isci.2026.117960` and PMC ID `PMC13697335`; the full text was then retrieved from PubMed Central by that PMC ID and matches. Both halves of the chain were confirmed independently.

**Funding: acknowledged, but every funder name and grant number was stripped by the text extraction and is not reproduced here.** **Competing interests: "The authors declare no competing interests"** — recorded alongside the commercial affiliations above, which are disclosed on the author line. **Generative AI: declared** — "the authors used ChatGPT (OpenAI) for language-editing and document-formatting assistance," with the authors taking full responsibility for the content. The first such declaration in this reading list. **Code: the paper states that public research scripts and a README are available at `https://github.com/xujingxu/DL_APT`** (as printed in the paper; not fetched or verified here). **Data: not public**, available on request subject to institutional review and a data-use agreement. **No reporting guideline (TRIPOD+AI, CLAIM, STARD) is named.**

**Ethics:** approved by the Institutional Review Board of the First People's Hospital of Kashi (Approval No. 202243), per the Declaration of Helsinki. **Consent waived for the retrospective cohorts; written informed consent obtained from all participants in the prospective cohort** — the correct handling, stated separately for each.

> **Why this paper today.** All four deferred papers were re-checked and remain blocked; the JAMA OpenEvidence study (PMID 42879271, PMC13673371) reached **day 20** of serving an empty PMC body — **one day short of the 21-day threshold at which the standing instruction says to decode it abstract-only.** Today's paper was the top pick from yesterday's restock, chosen for two things this list had never decoded: a **genuine prospective validation cohort** and a **human-versus-AI reader study**. It has both, 6,491 patients across five hospitals, and it does something rarer still — it works out its own positive predictive value, names the harms a false positive would cause, diagnoses its own calibration failure and identifies the right cause. It is the first **4 out of 5** in nine days.

---

## 1. The Gist

Tuberculosis killed about **1.23 million people in 2024** and 10.7 million developed it. The single most consequential question in TB care is whether a given patient's disease is **active** — replicating, symptomatic, and highly contagious — or **non-active**, meaning old scarring that is neither infectious nor in need of treatment. Active TB needs isolation and months of multi-drug therapy. Non-active TB needs nothing but occasional checking.

Telling them apart is hard and slow. The gold standards are sputum microscopy, which catches only about **half to three-fifths** of real cases, and bacterial culture, which takes **two to eight weeks**. In the places where TB is commonest, there are few radiologists and fewer labs.

So eleven researchers in Kashi Prefecture, Xinjiang — a high-burden region — trained a deliberately small neural network on **4,613 chest X-rays** from two hospitals, then tested it in two ways that almost no paper in this collection has managed together:

- **Retrospectively at two further hospitals** (1,318 patients): **AUC 0.917**
- **Prospectively at a fifth hospital** (560 patients, consented in advance): **AUC 0.896**

Then they had **nine radiologists** read the same 560 prospective X-rays. Every one of them scored below the model — juniors around **0.65 to 0.70**, seniors around **0.79 to 0.81**, against the model's **0.896**. With the model's output on screen, three readers re-read the set and scored **0.897, 0.902 and 0.937**.

And here is what lifts this paper above the pile. It does not stop at the AUC.

**It works out what happens when you actually use it.** In the prospective cohort the model flagged 205 patients as active. **68 of them were not** — a third of its positives were wrong. The paper computes that, names the consequences (needless isolation, extra tests, distress, wasted resources, possibly months of unnecessary multi-drug therapy), and concludes the model must be a triage tool only. That sentence is in the abstract: *positive predictions should not be used alone to initiate treatment.*

**And it catches its own calibration failure.** The model ranks patients well but its percentages are wrong in the prospective setting — and the authors identify exactly why: active TB was **44.8%** of the training data and only **28.4%** of the prospective cohort, so a model that learned the first background rate overestimates risk in the second. Section 5 computes the correction: a predicted 50% should read about **31%**.

## 2. Study Snapshot

**Study type:** a **multicentre model development study with both retrospective external validation and a prospective validation cohort**, plus a reader study. The prospective arm is what puts this near the top of this list's designs.

**Where:** five hospitals in Kashi Prefecture, Xinjiang, China.
- **Training:** Kashi Chest Hospital (n = 2,872) and Jiashi County Hospital (n = 1,741) → **4,613**
- **Retrospective external validation:** Shufu County Hospital (n = 1,011) and Yecheng County Hospital (n = 307) → **1,318**
- **Prospective validation:** Maigaiti County Hospital → **560**

**Patients: 6,491 total**, mean age 60.73 ± 16.32 years, 3,209 men and 3,282 women. **Every single breakdown in this paper reconciles exactly** — by cohort, by activity status, by sex, by centre. That is rarer than it should be and worth saying.

- Training: **2,067 active / 2,546 non-active** — prevalence **44.81%**
- Retrospective external: **688 active / 630 non-active** — prevalence **52.20%**
- Prospective: **159 active / 401 non-active** — prevalence **28.39%**

**Exclusions:** incomplete records, and conditions that would confound the chest film — lung cancer, pacemaker or defibrillator, prior cardiac or pulmonary surgery, extensive pleural effusion.

**The reference standard.** Active TB required (i) positive microbiological confirmation of *Mycobacterium tuberculosis*, (ii) symptoms (cough, weight loss, fever, night sweats, dyspnoea or chest pain), **and (iii) imaging findings** such as consolidation, nodules, cavities, ground-glass opacity or tree-in-bud. Non-active required negative microbiological confirmation **and imaging features** such as calcified or sclerotic lesions, clean cavities, pleural thickening or calcification. Section 4 discusses what that third criterion does to the study.

**The model:** **ShuffleNetV2** — chosen for size, not accuracy. 224 × 224-pixel input, ImageNet-pretrained, four stages of shuffle units, global average pooling, fully connected layer, softmax. Adam optimiser, cross-entropy loss, initial learning rate 0.0001, weight decay 0.001, momentum 0.9, batch size 64, with a learning-rate scheduler. **Training took about 57 hours** on two NVIDIA TITAN Xp GPUs; Python 3.8, PyTorch 1.8, CUDA 11.1.

**Augmentation:** random horizontal and vertical flips, described as having "effectively quadrupled the training dataset from 4,613 to approximately 18,452 images (4,613 original images × 4 augmentation variants: original, horizontal flip, vertical flip, and both flips)." Section 4 returns to this.

**Headline performance:**
- Training: AUC **0.926** (95% CI 0.918–0.933), sensitivity **0.847** (0.831–0.862), specificity **0.851** (0.837–0.864)
- Retrospective external: AUC **0.917** (0.902–0.932), sensitivity **0.854** (0.826–0.879), specificity **0.818** (0.786–0.846)
- Prospective: AUC **0.896** (0.860–0.932), sensitivity **0.862** (0.799–0.907), specificity **0.830** (0.791–0.864)

**The prospective confusion matrix, printed in full in the paper:** **137 true positives, 22 false negatives, 68 false positives, 333 true negatives.** From which: PPV **0.668**, NPV **0.938**, accuracy **0.839**. All reproduce exactly.

**Calibration.** The paper reports that the prospective calibration curve "deviated from the ideal calibration line, particularly in the low-to-intermediate predicted-probability ranges," and concludes: "although discrimination remained favorable, the probability estimates were not optimally calibrated in the prospective cohort." Brier scores are listed among the planned metrics; their values are in figures that were not retrievable.

**Ablation**, one factor changed at a time with everything else fixed: input resolution 384 × 384, width multipliers 0.5 and 2.0, no augmentation, **no ImageNet pretraining**, and focal loss in place of cross-entropy. **Removing pretraining produced the largest performance drop**; the other factors produced "smaller but measurable" changes.

**Architecture benchmarking** against ResNet50, DenseNet121, EfficientNet-B0 and ViT-Base/16 under identical splits, preprocessing, augmentation, optimisation, batch size and stopping criteria:
- Prospective AUC: ShuffleNetV2 **0.896**, ViT-Base/16 **0.895**, ResNet50 **0.882**, DenseNet121 **0.848**, EfficientNet-B0 **0.687**
- Retrospective external AUC: ResNet50 **0.930**, DenseNet121 **0.927**, ViT-Base/16 **0.927**, ShuffleNetV2 **0.917**, EfficientNet-B0 **0.817** — **ShuffleNetV2 ranks fourth of five here**
- Parameters: **2.3 M** vs 25.6 M, 8.0 M, 5.3 M and **86 M**
- Inference: **0.9 s** per case vs 2.4, 3.1, 2.8 and **6.7 s**

**The reader study.** Nine radiologists — three senior (≥10 years), three intermediate (5–10), three junior (<5) — read the 560 prospective radiographs unassisted. Then **one randomly selected radiologist per tier re-read the same images** with the model's real-time output available.
- Unassisted: range given as **0.648** (Junior_3, 95% CI 0.607–0.689) to **0.786** (Senior_3, 0.746–0.824); juniors clustered 0.648–0.700, seniors described as 0.786–0.811. **All nine fell below the model's 0.896.**
- Assisted: Senior_A **0.937** (0.915–0.960), Intermediate_A **0.902** (0.872–0.931), Junior_A **0.897** (0.869–0.923)
- **Time per case:** model 0.9 s; seniors 16.9 s; intermediates 35.3 s; juniors **87.1 s**

**Subgroup analyses** across age, gender, occupation, residence and scanner type, compared by DeLong test, **all p > 0.05** — described in the abstract as prespecified.

**Interpretability:** Grad-CAM, with attention co-localising to pathology in active cases and to right mid-to-upper-lobe scarring in non-active cases, "despite the absence of manual annotations." **Two misclassifications are analysed by name**: an active case called non-active where the right clavicle overlapped an apical abnormality, and a non-active case called active where pleural calcification and chronic post-TB change were read as active disease.

## 3. How Strong Is This Evidence? (Grade 4/5)

**This is the first 4 out of 5 in nine days, and it earns it on design rather than on reporting polish.**

**What earns it:**

**A genuine prospective validation cohort at a fifth hospital, with written informed consent.** 560 patients recruited forward in time at a centre that contributed nothing to training. This list has decoded sixty-six papers and this is the first with a true prospective validation arm. It is the single most informative thing a model-development paper can do, and it is almost never done.

**Retrospective external validation at two further hospitals on top of that.** So there are two independent tests, not one, and they agree: 0.917 and 0.896.

**The paper computes its own positive predictive value and tells you what it means.** "Of the 205 patients predicted to have active TB, 68 were actually non-active cases, meaning that 33.2% of positive predictions were false positives." Then the harms, enumerated: "unnecessary patient isolation, additional diagnostic procedures, psychological distress, increased use of healthcare resources, and potentially inappropriate multidrug therapy." Then the conclusion: triage only, confirm with microbiology, **and adjust the threshold for the local prevalence.** This list spent three days last week teaching that a PPV must be read against what a false positive triggers (entry 64). Here the authors do it themselves, and put it in the abstract.

**It diagnoses its own calibration failure and gets the mechanism right.** "A model may rank active and non-active cases effectively, as reflected by an AUC of 0.896, while still producing probability estimates that do not accurately represent absolute risk. One likely explanation is the marked prevalence shift between cohorts" — 44.8%, 52.2%, 28.4% — "a model trained on the higher-prevalence retrospective population may overestimate the probability of active TB in the prospective setting." And the remedy: "site-specific recalibration using representative local data, followed by prospective monitoring of calibration and operating thresholds." That is entry 58's lesson, derived independently by the authors, with the correct cause and the correct fix.

**A proper one-factor-at-a-time ablation**, with the largest effect identified (removing pretraining) rather than just asserted.

**Architecture benchmarking that admits competitors won.** Under identical conditions, ResNet50, DenseNet121 and ViT-Base/16 all beat ShuffleNetV2 on retrospective external validation. The paper says so: "while deeper architectures such as ResNet50 and ViT-Base/16 achieved marginally higher AUCs on retrospective external validation…" and justifies its choice on **efficiency** — 2.3 M parameters against 86 M, 0.9 s against 6.7 s. That is the right argument for a tool meant for resource-limited settings, and making it openly is better than pretending the small model simply won.

**A reader study with all nine radiologists stratified by experience, plus timing.** The unassisted spread — juniors at 0.648–0.700 against seniors at 0.786–0.811 — is itself a useful finding about how much this diagnosis depends on who is reading.

**Error analysis with named anatomical causes.** Two misclassifications explained by clavicle overlap and by pleural calcification. Not "the model sometimes errs," but *why*.

**Every arithmetic breakdown reconciles**, across five cohorts, three activity splits, sex, and five centres.

**Consent handled correctly and separately** for the retrospective and prospective arms, with an IRB number. **Commercial affiliations disclosed on the author line. Generative-AI use in manuscript preparation declared** — the first such declaration in this list. **Code address published.**

**Why it is not a 5:**

**The reference standard includes imaging findings, and the model's input is the image.** Active TB required microbiological confirmation *and* characteristic radiographic findings; non-active required negative microbiology *and* characteristic radiographic findings. So part of what the model is learning to reproduce is a radiographic criterion rather than a microbiological one. The microbiology anchors it, which keeps this from being full circularity — but the paper never raises the issue, and it is the single most important unaddressed threat. Section 4 has the detail.

**The reference-standard definition is internally ambiguous.** The Methods say "patients with microbiologically confirmed TB were included" and also that non-active cases were "defined by negative pathogenetic confirmation." Both cannot be true as written. The likely resolution — a history of confirmed TB, with current activity judged on current microbiology plus imaging — is not stated, and it determines what the model predicts.

**The AI-assisted reader result rests on three readers.** Nine read unassisted; **one per tier** re-read with assistance, on **the same images**, with **AI always second** and **no washout period stated**. The improvement may well be real, but the design cannot separate it from a second-reading effect, and the limitations section does not mention the reader study at all.

**No DeLong test between architectures.** ShuffleNetV2's prospective 0.896 against ViT's 0.895 is a difference of **0.001**, which Section 5 shows is **0.06 standard errors**. The paper's phrase "superior or equivalent" is doing a lot of work; the honest word is equivalent.

**Augmentation includes vertical flips of chest radiographs**, which produce images that cannot occur in a human body, and four copies of a dataset are described as "quadrupling" it.

**Two internal inconsistencies.** The Results give the prospective cohort's mean age as 60.73 ± 16.32 — the figure for all 6,491 patients — while the participant-details section gives 61.51 ± 17.40. And the reader paragraph says the unassisted range ran "to 0.786 for Senior_3" and then that seniors reached 0.786–0.811.

**No reporting guideline named**, and **all five centres are in one prefecture** (the latter acknowledged).

**What would make it a 5:** a reference standard independent of the imaging modality, or a sensitivity analysis restricted to microbiologically-defined activity alone; the reader study with all nine readers, randomised order and a washout; and a DeLong test on the architecture comparison.

## 4. The Editor's Concerns

**The circularity is the one that matters, and it is specific.** The model takes a chest radiograph and outputs "active" or "non-active." The label it is trained against was assigned partly *by looking at the chest radiograph* — consolidation, nodules, cavities, ground-glass and tree-in-bud for active; calcification, cord-like and sclerotic lesions, clean cavities and pleural change for non-active. So a microbiologically positive patient whose film looked quiescent would not have been labelled active, and a microbiologically negative patient with a calcified granuloma would have been labelled non-active. **The model is therefore being trained, in part, to agree with a radiologist's reading of the same image** — which is a much easier task than predicting bacteriology, and a much less useful one. The microbiological criterion keeps this from being wholly circular, and the right analysis would be to re-derive performance against microbiology alone. The paper does not do it, or mention the issue.

**The reference-standard statements contradict each other.** "In this multicenter cohort study, patients with microbiologically confirmed TB were included" and "This multicenter study included patients with microbiologically confirmed pulmonary tuberculosis" sit alongside "Non-active TB cases were defined by negative pathogenetic confirmation of Mycobacterium tuberculosis." If everyone had confirmed TB, nobody can be defined by negative confirmation. The sensible reading is that all patients had a documented history of TB and current activity was adjudicated afresh — which would also explain the exclusion of lung cancer and post-surgical chests. But that is my inference, not the paper's statement, and **the population the model applies to depends on which reading is right**: all-comers with a suspicious film, or people already known to have had TB.

**The reader study's design cannot support the claim made from it.** Three readers, same 560 images, AI always on the second pass, no washout mentioned, no order randomisation. Three mechanisms could produce the improvement and the design separates none of them: the AI genuinely helped; the readers remembered the cases; or those particular three readers were the stronger ones in their tiers (we are not told which of the three per tier was selected, so the assisted figures cannot be matched to their own unassisted baselines). The honest version of this finding is *suggestive*, and the paper's limitations section — which covers international cohorts, clinical parameters, immunocompetent atypical cases and the architecture benchmark — never mentions it.

**One number in the reader study is quietly interesting.** Junior_A's assisted AUC was **0.897**; the model's was **0.896**. A difference of one thousandth. Senior_A's assisted AUC was **0.937** — **0.041 above** the model. The most natural reading is that the junior reader adopted the model's call more or less wholesale, while the senior reader combined it with their own judgement and beat it. That is the difference between **automation bias** and genuine synergy, and it has direct implications for who should be given such a tool and with what training. The paper reports both numbers and does not comment.

**"Stable across prespecified subgroups, all p > 0.05" is weaker than it sounds.** Five subgroup dimensions (age, gender, occupation, residence, scanner) compared by DeLong test in a cohort with **159 active cases**. Splitting 159 events across age bands or scanner types leaves very few per cell, so a non-significant DeLong is close to guaranteed whether or not real differences exist. Absence of a detected difference is not demonstrated invariance, and the abstract's "performance was stable" reads as the latter.

**The augmentation includes an impossible transformation.** A **vertically flipped** chest radiograph places the diaphragm above the lung apices. No such image exists in medicine. Horizontal flipping at least produces a mirror image resembling situs inversus. Flips of this kind can still act as useful regularisation noise — the network learns not to rely on absolute position — but they are not realistic variation, and describing four copies as having "effectively quadrupled the training dataset from 4,613 to approximately 18,452 images" overstates what was gained: augmented copies are not independent patients, and the effective sample size is still 4,613.

**A "no competing interests" declaration alongside four authors at a commercial medical-AI company.** Beijing Deepwise & League of PHD Technology Co., Ltd appears in four author affiliations, including the author credited with formal analysis and interpretation. The affiliations are disclosed, which is what matters most; the formal declaration saying there are no competing interests is in tension with them, and a reader should know both facts.

**Deserved credit on something this list usually has to criticise.** The paper's comparison with prior CXR-TB studies is unusually careful. It notes that studies reporting 96–99% accuracy were distinguishing **TB from normal or from other lung disease** — a different and easier task — and that "latent tuberculosis is not directly equivalent to the non-active pulmonary tuberculosis category used in our study." It then warns that "numerical performance across studies should be interpreted cautiously because of differences in classification endpoints, disease prevalence, reference standards, dataset composition, and validation design." That is exactly the right handling of a literature full of inflated headline accuracies.

**Where I am uncertain, stated plainly.** The figures and supplementary tables were not retrievable. I therefore cannot read the **Brier scores** (listed as a planned metric), the calibration intercept or slope, the training and retrospective-external confusion matrices, the full ablation table with its per-variant metrics, the per-architecture sensitivity and specificity, the subgroup table, or the Grad-CAM images. The **prospective confusion matrix is printed in the body text** and is the one quantitative table I could fully verify. Funder names and grant numbers were stripped by the extraction and **were not guessed at**; the stated code URL is reported as the paper prints it and **was not fetched**.

## 5. Statistics Spotlight

Three things. The second is a calculation this list has described for weeks and never actually performed.

### Positive predictive value moves with the base rate while sensitivity and specificity sit still

The paper gives its prospective confusion matrix outright: **137 true positives, 22 false negatives, 68 false positives, 333 true negatives.** From those four numbers:

> sensitivity = 137/159 = **86.2%** · specificity = 333/401 = **83.0%**
> **PPV = 137/205 = 66.8%** · NPV = 333/355 = 93.8%

Sensitivity and specificity are properties of the model. **PPV is not** — it depends on how common the disease is in the people you point the model at. Freeze this model's sensitivity at 86.2% and specificity at 83.0%, and vary only the prevalence:

- prevalence **52.2%** (the retrospective external cohort) → PPV **84.7%**
- prevalence **46.5%** (the four retrospective centres pooled) → PPV **81.5%**
- prevalence **28.4%** (the prospective cohort, where it was actually used) → PPV **66.8%**
- prevalence **10%** (a lower-burden clinic) → PPV **36.1%**
- prevalence **2%** (general-population screening) → PPV **9.4%**

**The same model, unchanged, has a PPV of 81.5% in the population it was built from and 66.8% in the population it was tested in — a 15-point drop from nothing but the base rate.** Take it somewhere TB is uncommon and two-thirds of its alarms would be false; at screening prevalence, nine in ten.

**Why this happens.** False positives come out of the *healthy* pool, and the healthy pool grows as prevalence falls. At 28.4% prevalence there are 401 non-active patients, and 17% of them — 68 people — get wrongly flagged. That 68 is the same order of magnitude as the 137 real cases, so a third of positives are wrong. At 2% prevalence the healthy pool is fifty times the sick one, and the false positives swamp everything.

**What the paper does with this is the part worth copying.** It computes the PPV, states that 33.2% of positives were false, lists the specific harms — isolation, extra procedures, distress, resources, inappropriate multi-drug therapy — concludes that the model "should be used only as a triage or clinical decision-support tool," and adds that "because positive predictive value depends strongly on disease prevalence, the model's operating threshold should be evaluated and, where necessary, adjusted for the intended clinical population." Then it puts the operative sentence in the abstract: **positive predictions should not be used alone to initiate treatment.**

**The watch-out:** a reported PPV belongs to one prevalence and travels nowhere. Whenever you see one, find the prevalence it was computed at, then recompute for yours. The formula is short:

> PPV = (Se × prev) ÷ (Se × prev + (1 − Sp) × (1 − prev))

### Computing the recalibration factor from the prevalence shift

The paper reports that discrimination held up prospectively (AUC 0.896) while calibration did not, and attributes it to the prevalence shift. You can take that further and work out **how wrong the probabilities are, and in which direction**, from the prevalences alone.

The model learned on data where active TB ran at about **46.5%** (the pooled retrospective centres). It was deployed where it ran at **28.4%**. Convert both to **odds** — probability divided by its complement:

> training prior odds = 0.465 / 0.535 = **0.869**
> deployment prior odds = 0.284 / 0.716 = **0.397**

A classifier's output carries its training prior baked in. To move it to a new prior you multiply the **odds** by the ratio of the two:

> correction factor = 0.397 / 0.869 = **0.456**

So every predicted odds should be multiplied by about 0.46 — **roughly halved.** Worked through:

- model says **20%** → recalibrated **10.2%**
- model says **30%** → recalibrated **16.4%**
- model says **50%** → recalibrated **31.3%**
- model says **70%** → recalibrated **51.6%**
- model says **90%** → recalibrated **80.4%**

**Every number comes down, and the middle of the range moves most** — which is precisely where the paper says its calibration curve deviated: "particularly in the low-to-intermediate predicted-probability ranges." The arithmetic and the observation agree.

**The intuition.** Imagine a doctor who trained in a hospital where half the coughing patients had TB. Move them to a clinic where a quarter do, and they will keep over-calling TB — not because their judgement of *which* patients look worse is wrong, but because their sense of how common it is was formed somewhere else. **Ranking survives the move; the baseline does not.** That is exactly the difference between discrimination and calibration.

**The watch-out, and it is the most consequential one in clinical AI:** this correction uses a single number, the prevalence ratio, and assumes nothing else changed between the two settings. Real shifts also involve different case mixes, severities and imaging equipment, so a prior adjustment is a first approximation rather than a fix. The real remedy is the one the paper prescribes — **site-specific recalibration on local data, then ongoing monitoring** — and it requires outcome data from the new site, which is why so few deployed models have it.

### When a tiny AUC difference decides which model gets built, check the noise

ShuffleNetV2 was selected over four alternatives. On the prospective cohort its AUC was **0.896**; ViT-Base/16's was **0.895**. A difference of **0.001**.

How big is the noise around a number like that? The Hanley–McNeil formula gives the standard error of an AUC from the AUC and the class counts. At 159 active and 401 non-active patients:

> standard error ≈ **0.0173**

which implies a 95% interval of roughly **0.862 to 0.930** — and the paper reports 0.860 to 0.932, so its intervals are sound. Now put the difference against that noise:

> 0.001 ÷ 0.0173 = **0.06 standard errors**

That is indistinguishable from zero by any measure. And no DeLong test between architectures is reported — the paper runs DeLong tests on the subgroup analyses but not on the comparison that determined the whole design.

**But the paper's actual argument is a good one, and it is not about accuracy.** ShuffleNetV2 uses **2.3 million** parameters against ViT's **86 million** — a 37-fold difference — and runs in **0.9 seconds** per case against 6.7, a 7.4-fold speed-up. For a tool intended for county hospitals in a high-burden region with few radiologists, "equally accurate and runs on modest hardware" is the right reason to choose a model. The paper states it in those terms.

**What it should not claim is superiority.** Its own phrase — "superior or equivalent performance on the prospective cohort" — blends an untested 0.001 lead with the honest word. And on retrospective external validation ShuffleNetV2 was **fourth of five**: 0.917 against 0.930, 0.927 and 0.927.

**The watch-out:** when a paper compares many models and the winner leads by a margin smaller than one standard error, the ranking is noise and the paper has effectively chosen arbitrarily — which is fine if the stated reason is something else (size, speed, cost), and misleading if the stated reason is performance. **Find the standard error before you accept a ranking.** Here, usefully, the comparison also reveals how little the extra 84 million parameters bought.

## 6. Jargon Translator

**Active vs non-active pulmonary TB** — active means the bacteria are replicating, the person is symptomatic and contagious, and needs isolation plus months of multi-drug therapy. Non-active means old, healed damage: not infectious, no treatment needed, just periodic checking. Telling them apart is the whole point of this paper.

**Latent TB infection** — bacteria present but dormant; the person is not ill and not infectious, but may progress later. The paper correctly notes this is **not** the same category as its "non-active."

**Sputum smear microscopy** — looking for bacteria in coughed-up phlegm under a microscope. Fast and cheap, with sensitivity typically only **50–60%**.

**Mycobacterial culture** — growing the bacteria to confirm them. The reference standard, and it takes **2–8 weeks**.

**NAAT (nucleic acid amplification test)** — a molecular test, highly specific and fast, but too expensive for routine use in many high-burden settings.

**Chest radiograph (CXR) / chest X-ray** — one flat image, cheap, low radiation, available almost everywhere. The reason a CXR-based tool is practical where a CT-based one is not.

**Tree-in-bud sign, cavitary lesion, ground-glass opacity** — radiological patterns suggesting *active* disease.
**Calcified lesion, sclerotic lesion, clean cavity, pleural thickening** — patterns suggesting *healed, non-active* disease.

**ShuffleNetV2** — a deliberately small neural network built for phones and low-power devices. "Channel shuffle" mixes information between groups of features so that heavily grouped convolutions, which are cheap, still share information.

**Width multiplier** — a dial that scales how many channels a network has. 0.5 makes it smaller and faster, 2.0 larger and slower. One of the ablation factors here.

**ImageNet-pretrained** — started from weights learned on millions of everyday photographs. **Removing this caused the largest performance drop in the ablation**, which is the usual finding with medical datasets of this size.

**Ablation study** — rerunning with one ingredient changed at a time, everything else fixed, to see what each contributes.

**Data augmentation** — making altered copies of training images so the model sees more variety. Here horizontal and vertical flips. See Section 4 on why vertical flips of chest films are odd.

**AUC / AUROC** — the share of (active patient, non-active patient) pairs the model ranks the right way round.

**Sensitivity / specificity** — of those truly active, the share caught; of those truly non-active, the share correctly cleared. **Properties of the model.**

**PPV / NPV** — of those the model flags, the share truly active; of those it clears, the share truly non-active. **Depend on prevalence.** See Section 5.

**Calibration** — whether a predicted 30% risk corresponds to 30% of such patients actually having active TB. Separate from ranking, and the thing that broke here.

**Brier score** — average squared error of predicted probabilities, combining calibration and discrimination. Listed as a planned metric; its values are in figures not retrievable here.

**Prevalence shift** — the disease being commoner or rarer in the deployment setting than in training. **44.8% → 28.4%** here, and the stated cause of the calibration failure.

**Recalibration** — adjusting a model's output probabilities to a new setting's base rate. Section 5 computes the factor.

**DeLong test** — the correct test for whether two AUCs computed on the *same* patients differ. Used here for the subgroups, not for the architecture comparison.

**Grad-CAM** — a heatmap showing which parts of the image drove the model's answer. Not a guarantee the reasoning is right, but it catches gross failures.

**Automation bias** — a human deferring to a machine's answer rather than combining it with their own judgement. See Section 4 on Junior_A.

**Crossover reader study** — the same readers reading the same cases under two conditions. Needs randomised order and a washout period to work properly; see Section 4.

## 7. What You Can (and Can't) Say

**Fair to say:**

- ✅ "A small neural network distinguished active from non-active TB on chest X-rays with an AUC of 0.917 at two external hospitals and 0.896 in a prospective cohort at a fifth hospital." Reported; the prospective arm is the rare part.
- ✅ "In the prospective cohort it caught 137 of 159 active cases and wrongly flagged 68 of 401 non-active patients." The paper prints the confusion matrix.
- ✅ "A third of its positive predictions were wrong, and the authors say it must not be used alone to start treatment." 68 of 205; the sentence is in the abstract.
- ✅ "Its probability estimates were poorly calibrated prospectively, and the authors attribute this to prevalence falling from about 45% in training to 28% in the prospective cohort." Their own diagnosis.
- ✅ "All nine radiologists scored below the model when reading unassisted — juniors around 0.65–0.70, seniors around 0.79–0.81." Reported.
- ✅ "The model read each X-ray in about 0.9 seconds; junior radiologists took about 87 seconds." Reported.
- ✅ "Removing ImageNet pretraining hurt performance more than any other change tested." Reported in the ablation.
- ✅ "ShuffleNetV2 was chosen for being small and fast, not for being the most accurate — three other architectures beat it on retrospective external validation." Reported, and the paper says so.

**Not fair to say:**

- ❌ "AI beats radiologists at diagnosing active TB." It scored higher than all nine on this one task in one prefecture, against a reference standard that itself used the chest X-ray. The task is activity classification among people with TB, not diagnosis from scratch.
- ❌ "AI assistance improves radiologist accuracy." Three readers, one per tier, re-read **the same images** with AI **always second** and **no washout** — the design cannot separate AI benefit from a second-reading effect, and the paper does not list this among its limitations.
- ❌ "ShuffleNetV2 outperformed ViT-Base/16." The prospective difference was **0.001**, about **0.06 standard errors**, with no DeLong test between architectures. And ViT beat it externally, 0.927 to 0.917.
- ❌ "A PPV of 66.8% is what you would get in practice." That belongs to a 28.4% prevalence. At 10% prevalence the same model's PPV is **36%**; at 2%, **9%**.
- ❌ "The model is ready to deploy." Its own authors call for site-specific recalibration, prospective monitoring of thresholds, international validation, and confirmatory microbiology before treatment.
- ❌ "Performance was proven equal across demographic groups and scanners." Five subgroup dimensions tested in a cohort with 159 active cases, all DeLong p > 0.05. That is absence of a detected difference, not demonstrated invariance.
- ❌ "Augmentation quadrupled the training data." Four flipped copies of 4,613 images are not 18,452 independent patients, and vertically flipped chest radiographs depict anatomy that cannot exist.
- ❌ "The model predicts bacteriological activity from the image alone." The reference standard required characteristic imaging findings as well as microbiology, so part of what it learned is a radiologist's reading of the same film.
- ❌ "These results apply to TB screening in the general population." Everyone included had microbiologically investigated TB, patients with confounding chest findings were excluded, and all five centres are in one Chinese prefecture.

## 8. Bottom Line for Your Life

If you or someone close to you has had tuberculosis, the clinically important thing here is the distinction itself, which is easy to misunderstand and matters enormously. **A chest X-ray showing TB damage does not mean active TB.** Old, healed scarring and calcification show up on films for life, are not infectious, and need no treatment. Active disease needs isolation and months of drugs. Being told "your X-ray shows tuberculosis" is not the same as being told you are ill or contagious — and this paper exists because even radiologists find that distinction hard, scoring between 0.65 and 0.81 on it. If you are ever in that conversation, the question to ask is whether the *sputum* tests confirm active disease, because the film alone cannot settle it.

For anyone appraising research, this paper hands you one calculation and one habit.

**The calculation: a predictive value belongs to one prevalence and travels nowhere.** This model's PPV is **66.8%** where it was tested, **81.5%** where it was built, **36%** in a clinic at 10% prevalence and **9%** at screening prevalence — with sensitivity and specificity completely unchanged throughout. The formula is one line and you should run it for your own setting every time: PPV = (Se × prev) ÷ (Se × prev + (1 − Sp) × (1 − prev)). **And then ask the question the authors asked themselves: what does a false positive actually do to a person?** Here they answered it — isolation, extra procedures, distress, possibly months of unnecessary drugs — and concluded their own tool must never be used alone to start treatment. That paragraph is the best thing in the paper.

**The habit: when discrimination survives a move and calibration does not, compute the prevalence ratio.** Trained at **46.5%**, deployed at **28.4%** — convert both to odds, divide, and you get **0.46**. Every predicted probability needs its odds roughly halved: a reported 50% is really about **31%**. The direction is predictable from nothing but the two base rates, and it matches exactly where the authors said their calibration curve went wrong. **Ranking travels; baselines do not.** It is the most common way a working model becomes a misleading one, and it is also the most fixable — which is why "site-specific recalibration and ongoing monitoring," the thing this paper asks for and almost no deployed model has, is the sentence to look for in any paper proposing to put a model into use.

---

## Appendix — deferred-paper status, 2026-11-04

- **Google, "The anatomy of a personal health agent"** (Nature, PMID 42907512): no PubMed Central copy. Unchanged.
- **BMJ, LLM-trial reporting completeness review** (PMID 42869550): no PMC copy; Scite paywalled. Unchanged.
- **Annals of Internal Medicine, Choosing Wisely benchmark** (PMID 42896192): no PMC copy. Unchanged. Standing note: the overuse rate of 5.4% with a 95% CI of 0.6–12.2% is a clustering signature — that interval is almost certainly computed across the 15 recommendations rather than the 4,050 responses.
- **JAMA, "Clinician Use of an AI-Enabled Clinical Information Platform"** (PMID 42879271, PMC13673371): PMC record exists and serves an **empty body for the twentieth consecutive day — one short of the threshold.** Standing instruction: **if still empty on 2026-11-05 (day 21), decode abstract-only and say so explicitly.**

---

*This is an educational analysis of a published scientific paper, not medical advice. Nothing here is guidance about tuberculosis or your own care. If you have questions about a TB diagnosis or a chest X-ray result, speak to your doctor.*
