# Predicting Future Visual Field Status from Baseline OCT Scan in Early to Moderate Glaucoma Using Deep Learning

**Authors:** Chaurasia AK (Menzies Institute for Medical Research, University of Tasmania; **Pandani Solutions Pty Ltd**), Wang C (Monash Health), Toohey PW (**Pandani Solutions Pty Ltd**), Chen CY (Monash Health), MacGregor S (QIMR Berghofer; University of Queensland), Bennett MT (**Pandani Solutions Pty Ltd**), Verma N (University of Tasmania; Hobart Eye Surgeons), Craig JE (Flinders Medical Centre), McCartney PJ (University of Tasmania), Sarossy MG (Monash University), Hewitt AW (University of Tasmania; Hobart Eye Surgeons)
**Journal:** Ophthalmology Science, 2026; 6(12): 101419 (published 23 September 2026)
**Decoded:** 2026-11-15

**Analysis basis:** **FULL TEXT** (retrieved from PubMed Central, PMC13740841) — Introduction, all Methods sub-sections including study design, patient selection, both device scan protocols, data refinement, architecture and training, the comparator models and the evaluation metrics, and all of Results and Discussion including the Bland–Altman findings, the saliency caveats, the comparator discussion and the limitations. **All figures, tables and supplementary material are unreachable**, which costs three specific things named throughout: **the comparator table** (so the margin over a mean-reference model cannot be quantified), **the magnitude of actual visual-field change** between baseline and follow-up, and **the Footnotes and Disclosures section.**

**Source links (verified):**
- DOI: https://doi.org/10.1016/j.xops.2026.101419
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42997014/
- Full text used: https://pmc.ncbi.nlm.nih.gov/articles/PMC13740841/

**Basis of link verification.** Direct URL fetching is blocked from this session (`doi.org` does not resolve under the network policy here), so verification was done against the live PubMed/NLM record. According to PubMed, a query for PMID 42997014 returned this exact title, these eleven authors with these affiliations, *Ophthalmology Science* volume 6 issue 12 article 101419, publication date 23 September 2026, DOI `10.1016/j.xops.2026.101419`, and keywords including "Vision transformer" and "Visual Field Index"; a PMID-to-PMCID conversion returned **PMC13740841**; and the full text was then retrieved from PubMed Central by that PMC ID and matches the record. Both halves of the chain were confirmed independently.

**Ethics: fully reported, with numbers.** Data collection at Hobart Eye Surgeons was approved by the **University of Tasmania Human Research Ethics Committee (29775)**; collection at Essendon Eye Clinic and Gladstone Park Eye Clinic by the **Royal Victorian Eye and Ear Hospital Human Research Ethics Committee (24/1597HL)**. The study adhered to the Declaration of Helsinki, and **consent waivers were obtained for each of the three sites** given the retrospective design.

**Competing interests: a commercial disclosure exists and I could not read it.** The abstract carries the journal's standard flag — *"Proprietary or commercial disclosure may be found in the Footnotes and Disclosures at the end of this article"* — and that section is not in the retrieved text. What I *can* verify from the affiliations is that **three of the eleven authors, including the first author, are affiliated with Pandani Solutions Pty Ltd**, a private company, and that the paper proposes the model "could be integrated into existing OCT systems." **Funding is not reported in what I retrieved.** I am flagging the existence of the disclosure and the affiliations, not characterising a disclosure I have not seen.

**AI-assistance disclosure, which is worth noting as good practice:** the paper states that **Grammarly was used to improve readability and grammar.**

**Reporting guideline: none named.** **TRIPOD+AI** applies directly — this is a prognostic model with external validation — and is not mentioned. Section 4 places that in a now eight-entry sequence.

---

## 1. The Gist

**This is the paper this reading list has been waiting for: a deep-learning model actually validated on a different manufacturer's scanner. It degraded. The paper says it didn't. The paper's own confidence intervals say it did, and that disagreement is the most useful thing in it.**

The clinical problem is real and well framed. **Glaucoma destroys vision irreversibly**, and the only treatable risk factor is eye pressure — yet many eyes keep losing visual field despite treatment that looks clinically correct. So clinicians want to know, early, which eyes are heading downhill, because those are the ones to watch closely and treat harder. The structural scan (**OCT of the retinal nerve fibre layer**, the sheet of nerve axons at the back of the eye) is quick, objective and already taken at every visit. The visual field test is slow, tiring, and noisy. **If one OCT scan could forecast the visual field years ahead, that would be genuinely valuable.**

The team trained a **Vision Transformer** — the architecture behind modern image AI — on **1,792 eyes from 1,610 patients** at one Australian clinic, to predict three standard visual-field summary numbers at a follow-up visit **an average of 4.74 years later.** Then, and this is the part that matters, they tested it at **two other clinics**: one using the **same brand of scanner (Zeiss)**, one using a **different brand (Heidelberg)**.

**And that two-site design accidentally separates two completely different questions.** The Zeiss clinic asks: does this travel to a new hospital with new patients? The Heidelberg clinic asks: does it travel to **different hardware**? Those are not the same question, and the answers here are not the same.

**At the new Zeiss site, the model held up essentially perfectly.** Mean absolute error for mean deviation was 1.92 decibels against 1.76 internally; the systematic bias was **+0.17 dB**, which is nothing. All three confidence intervals overlapped the internal ones. **Site transportability: confirmed.**

**At the Heidelberg site, it did not.** Error on mean deviation rose from **1.76 to 2.71 dB — a 54% increase** — and on the Visual Field Index from **3.23 to 4.14, up 28%.** More decisively: **the 95% confidence intervals for those two indices do not overlap the internal intervals at all.** Internal mean deviation was 1.61 to 1.93; Heidelberg was 2.51 to 2.91. **There is a clear gap between them.** Non-overlapping confidence intervals are a *stricter* test than a p-value below 0.05, so this difference is unambiguous.

**The paper's text says the opposite.** It reports "error rates highly consistent with those observed in the model development cohort, indicating stable performance across devices," states there was **"no statistically significant difference in model performance across data sets,"** and calls the result **"surprising"** because it "contrasts with existing literature." The abstract says **"strong performance across 2 OCT devices."** Section 4 goes through this carefully, because being surprised that your model *didn't* degrade — when your own numbers show it did — is the point at which a result should have been re-checked rather than explained.

**The Bland–Altman analysis makes it concrete, and also points to the fix.** On Heidelberg the model was biased in one direction on all three measures: **+1.05 for the Visual Field Index, +1.83 dB for mean deviation, +1.13 dB for pattern standard deviation.** On Zeiss the biases were 0.05, 0.17 and 0.08 — essentially zero. **For mean deviation, that +1.83 dB offset accounts for about two-thirds of the entire 2.71 dB average error.** So the Heidelberg failure is mostly a **constant shift, not random scatter** — which is good news, because a constant shift can be corrected by recalibrating on a modest sample of Heidelberg scans. **That is a constructive finding the paper does not draw.**

**And why should anyone have expected the devices to behave the same?** The two scans are not the same picture. Zeiss acquires a **6 × 6 mm cube** of the optic disc and the RNFL image is extracted from it by the manufacturer's software. Heidelberg acquires a **circular line scan on a 3.5 mm circle.** Different geometry, different software, different quality scales. Fixing brightness and contrast — which the team sensibly did — cannot reconcile a cube-derived image with a circle scan.

**Now the second finding, and the authors report it themselves with real honesty.** They built comparison models, including a **mean-reference model** — one that ignores the scan entirely and predicts the cohort average for every patient. Their own words: the comparators "showed **slightly lower** performance metrics than the ViT regression model," the improvement was **"modest, particularly for VFI and PSD,"** and the handcrafted image features "may capture **little additional prognostic signal beyond the average follow-up VF outcome.**"

**Read that again.** Predicting the same number for everybody was only *slightly* worse than the Vision Transformer. The exact margin is in a supplementary table I cannot retrieve, so **I cannot say how much better the model is than guessing the average** — and that is the single most important missing number in the paper.

**And there is a baseline they never tried at all.** Every eye in this study had a **baseline visual field test** — it was an inclusion requirement, and the baseline indices appear in their own correlation matrix. **Nobody asked how well you do by simply predicting that the future visual field will look like the current one.** For early-to-moderate glaucoma over five years, that is a formidable baseline, and it is exactly the information a clinician already has in hand. **The authors themselves name why this matters**, in a limitation that is more damaging than it looks: the model "can predict future key VF indices **without distinguishing between the impacts of baseline disease severity and true longitudinal changes.**"

**What the team deserves genuine credit for.** They did the external validation that almost nobody does, on two sites and two devices. They reported **bootstrap confidence intervals on every metric** — which is the only reason the device degradation is visible at all. They ran a **mean-reference comparator**. They produced **Bland–Altman plots and reported the biases and the wide limits of agreement**. They published two ethics approvals with numbers. And their **saliency caveat is the best in this reading list**: they note that some attention falls outside the nerve fibre layer, name the possible non-biological causes including "differences in scan quality across OCT machine vendors," and state that saliency maps are "exploratory visual explanations rather than proof." **The data needed to correct this paper's central claim is all inside this paper.**

## 2. Study Snapshot

**Study type:** retrospective multicentre cohort study developing a deep-learning regression model, **with genuine external validation at two independent sites, one using a different manufacturer's OCT device.** No prospective component, no randomisation, no patient outcome beyond the visual-field measurements themselves.

**Setting and data.** Three Australian ophthalmology clinics, data collected **2009 to 2025**. Development: **Hobart Eye Surgeons** (Zeiss OCT), patients extracted May 2009 to September 2019. External validation: **Essendon Eye Clinic** (Zeiss OCT) and **Gladstone Park Eye Clinic** (Heidelberg Spectralis OCT). Only patients already listed in the clinic database as having glaucoma or being a glaucoma suspect were extracted; classification was by an ophthalmologist on clinical examination including visual field and OCT reports.

**What is being predicted.** Three standard global summaries of a visual field test, taken at a follow-up visit: **mean deviation (MD)** in decibels, how much dimmer overall the patient's field is than a healthy age-matched eye; **pattern standard deviation (PSD)** in decibels, how uneven the field is; and the **Visual Field Index (VFI)** as a percentage, a 0–100% summary of remaining function. All from **standard automated perimetry, 24-2 SITA fast or standard, Humphrey Field Analyzer 2 or 3.**

**The input.** A **single baseline OCT scan** of the retinal nerve fibre layer at the optic nerve head, taken on the same day as the baseline visual field or within ±6 months.

**The exclusion cascade, which I traced and verified.** **4,038 eyes from 2,048 participants** had baseline and latest follow-up visual field reports. Removing **23** eyes for poor-quality or artefact-affected OCT and **791** for unreliable visual fields (reliability criteria: fixation losses, false positives and false negatives all 33% or lower) leaves **3,224** — which matches the paper exactly. Then the cohort was "curated based on follow-up intervals," restricted to **within one standard deviation of the mean (4.74 ± 2.59 years), i.e. 2.15 to 7.33 years**, leaving **1,792 eyes from 1,610 patients.** **That last step alone removed 1,432 eyes — 44.4% of the eligible pool.** The stated reason was "to minimize the influence of outliers arising from a limited data set."

**Further exclusions.** Under-18s; eyes with conditions affecting the visual field such as retinal detachment or optic neuritis; missing indices. **Advanced glaucoma was excluded** — VFI worse than 79%, MD worse than −12 dB, or PSD worse than 8 dB — on the stated and legitimate grounds that RNFL thickness shows a floor effect in advanced disease. And **"eyes showing an improvement in VF from baseline, based on the Hodapp–Parrish–Anderson criteria, were excluded to minimize the postcataract surgery effect."** The fraction removed by that last rule is **not reported.**

**Cohort characteristics.** Mean baseline age **68.81 years**; **56.7% female**. Baseline and follow-up visual field indices differed significantly (**Wilcoxon signed-rank, p < 0.001**), which the authors correctly read as evidence that glaucoma progressed over the follow-up. **The magnitude of that change is in a table I could not retrieve.**

**The two devices, and they differ in more than brand.** Zeiss: **Cirrus 6000 spectral-domain OCT**, a **6 × 6 mm optic disc cube scan, 200 A-scans per B-scan and 200 B-scans**, with the RNFL image extracted from the optic-nerve-head region using the ZEISS FORUM platform's built-in features; **signal strength 7 or higher** required. Heidelberg: **Spectralis spectral-domain OCT**, a **circular line scan centred on the optic nerve head with a 3.5 mm diameter**, extracted via Heidelberg Eye Explorer; **quality score 20 or higher out of 40** required. **Both** were exported as bitmaps at **1,356 × 904 pixels with brightness and contrast fixed at 255 and 30** to maintain consistency, then downsized to **518 × 518** for the model. Scans with artefacts, segmentation errors or movement were excluded at both.

**External set retention.** Essendon: **150 of 188 scans (79.8%)** from **92 patients**. Gladstone Park: **280 of 377 scans (74.3%)** from **166 patients**.

**Model development.** **135 configurations** were screened — I verified this is **15 base architectures × 3 loss functions × 3 optimizers** (Stochastic Gradient Descent, Adam, Ranger) — each trained for 5 epochs at batch sizes 16, 32 and 64. The data were **split at the patient level, 80% training and 20% validation.** Loss was mean squared error; monitored metrics were MAE and RMSE. Targets were **z-standardised before training and inverse-transformed to original units before reporting.** Training was two-stage: layers frozen with only the last layer fine-tuned for up to 10 epochs at learning rate 3e-3, then all layers unfrozen for up to 10 more epochs using a one-cycle policy with rates between 1e-6 and 5e-4, with **early stopping** (no improvement of at least 0.001 for 3 consecutive epochs) and **weight decay 3e-4.** Data augmentation and normalisation were applied. The winner was **ViT Small Patch14 with self-supervised DINOv2 pretraining, batch size 16.** Hardware: NVIDIA A100, 40 GB.

**Comparator models, all using OCT images only.** A **mean-reference model**, **Ridge regression**, and **Random Forest regression**, each built on a **1,166-dimensional handcrafted feature vector** from the same grayscale images — low-resolution pixel intensities, intensity histograms, horizontal and vertical projection profiles, gradient-magnitude statistics, gradient-orientation histograms and summary statistics. Ridge used standardisation, principal component analysis and cross-validated fitting. All were evaluated on the same internal validation set.

**Results — internal validation.** MAE **3.23 (95% CI 2.91–3.56)** for VFI, **1.76 (1.61–1.93)** for MD, **1.14 (1.03–1.27)** for PSD. RMSE **4.42 (3.92–4.93)** for VFI and **2.29 (2.07–2.53)** for MD; RMSE **1.64** for PSD. Confidence intervals by **bootstrap resampling.**

**Results — Zeiss external (same device, new site).** MAE **3.19 (2.73–3.66)**, **1.92 (1.69–2.16)**, **1.11 (0.95–1.29)**. RMSE for MD **2.38.** **All three intervals overlap the internal intervals.**

**Results — Heidelberg external (different device, new site).** MAE **4.14 (3.82–4.46)**, **2.71 (2.51–2.91)**, **1.37 (1.21–1.55)**. **I verified that the VFI and MD intervals do not overlap the internal intervals at all** — the gaps are 3.56 to 3.82 and 1.93 to 2.51 respectively. Relative increases: **VFI +28.2%, MD +54.0%, PSD +20.2%.**

**Bland–Altman.** **Heidelberg: positive mean bias on all three** — **1.05** percentage points for VFI, **1.83 dB** for MD, **1.13 dB** for PSD. **Zeiss: near zero on all three** — **0.05, 0.17, 0.08.** The paper reports that **limits of agreement were wide across both machines, particularly for VFI and MD, "indicating clinically meaningful individual-level variability,"** and that the plots **"suggested proportional bias, with prediction errors varying across the range of VF indices."**

**Sensitivity analysis on follow-up interval.** Absolute error compared across three groups (<3 years, 3–6 years, >6 years) by **Kruskal–Wallis**, and against follow-up as a continuous variable by **Spearman correlation**, in both external sets. On Heidelberg, error was similar across groups with no correlation for any index. On Zeiss, no group-wise differences (p > 0.7); no association for VFI or MD; **PSD showed a weak negative correlation (p = 0.011)** — lower error with longer follow-up.

**Architecture screening results.** ViT with DINOv2 "consistently achieved the lowest MAEs, ranging between **5.4 and 7.6**," against DenseNets at **9.0–9.6** and ResNet/VGG at **9.8–10.3**. The best configuration "reduced the error by approximately **47% compared with the least effective model among the top ten.**" **These screening figures are on a different scale from the final reported MAEs of 1.14–3.23 and the paper does not reconcile them.**

**Saliency.** Attention weights from the final ViT layer over 14 × 14 patches, upsampled into heatmaps. Highest attention localised to **the RNFL and inner retinal layers**; the paper also states that **"the retinal pigment epithelium and outer retinal nerve layers were also highlighted."** And the caveat, which deserves quoting: "a few saliency maps highlight regions outside the RNFL, **especially in Heidelberg Spectralis OCT device-driven scans**, which may represent either the model's use of adjacent ONH or peripapillary structural features or **reflect nonbiological signals, including blood vessel shadows, image quality, differences in scan quality across OCT machine vendors, or artifacts.** Therefore, saliency maps should be viewed as exploratory visual explanations rather than proof that the model relies exclusively on biologically meaningful RNFL features."

**Comparison to the literature.** Maetschke et al estimated VFI and MD from OCT volumes with RMSE 12.0 ± 1.61 and 4.1 ± 0.44, against this paper's 4.42 and 2.29. Another neural network achieved MAE 4.0 dB (3.8–4.2) with MAE 3.3–5.9 dB on independent datasets. The paper notes **"a direct comparison between the 2 studies is not possible due to their differing data sets and model architectures."**

**Limitations the authors state themselves.** Using OCT-RNFL alone "may oversimplify the multifaceted nature" of glaucoma progression. **Clinical variables were excluded** — age, sex, baseline intraocular pressure, central corneal thickness, systemic conditions — as were genetic and lifestyle variables; the authors note these "can be easily obtained from the patient during the baseline first visit and could therefore be integrated into the model." Global indices "may overlook localized defects or regional progression patterns." Advanced glaucoma was excluded, limiting generalisability. And: the model **"can predict future key VF indices without distinguishing between the impacts of baseline disease severity and true longitudinal changes,"** with future studies needing "serial OCT and multiple longitudinal VF tests to assess whether the model can predict true structural or functional progression over time."

**Not reported or not retrievable:** the comparator table, so **the margin of the ViT over the mean-reference model cannot be quantified**; the magnitude of actual visual-field change over follow-up; **any comparator using the patient's own baseline visual field**; the fraction of eyes removed by the "excluded if improved" rule; **any R², correlation or variance-explained measure for any index**; the Footnotes and Disclosures section; funding; any reporting guideline; all figures, tables and supplementary material.

## 3. How Strong Is This Evidence? (Grade 3 out of 5)

**The design here is the best in this reading list for the question it was picked to answer, and the paper draws the wrong conclusion from its own data. Both halves of that sentence are load-bearing, and the grade sits between them.**

**What is genuinely strong, starting with the thing nobody else does.**

**Real external validation, at two sites, on two manufacturers' devices.** Yesterday's entry was held to a 2 partly for having internal validation only. This paper did the hard thing: it took a model trained on Zeiss scans at one clinic and ran it on Heidelberg scans at another. **That is the strongest form of external validation available short of a prospective trial**, and it is rare enough that it is why this paper was chosen.

**Bootstrap confidence intervals on every metric.** This matters more than it sounds. **It is the only reason the device degradation is detectable at all** — a paper reporting bare point estimates of 1.76 and 2.71 would leave a reader guessing. The authors supplied the intervals that refute their own summary, which is a strange kind of integrity but a real one.

**They ran a mean-reference comparator.** A model that ignores the image and predicts the cohort average. This is exactly the baseline this reading list called for yesterday, and it is absent from most papers of this kind. **They ran it, and they reported that it came close.**

**Bland–Altman with mean bias and limits of agreement, for both external sets.** This is a genuine agreement analysis — the closest thing to calibration available for a regression model — and yesterday's entry had nothing comparable. It is also what reveals the Heidelberg failure to be a systematic offset.

**Two ethics approvals with committee numbers, consent waivers at all three sites, Declaration of Helsinki.**

**A sensitivity analysis on follow-up interval**, by both grouping and continuous correlation, in both external sets.

**The saliency caveat is the best in this reading list.** It names the possibility of non-biological signal, lists candidate artefacts including vendor scan-quality differences, notes the effect is concentrated in Heidelberg scans, and explicitly declines to treat the maps as proof. **Entries 73, 74 and 77 of this list all turned on exactly this distinction, and this paper gets it right without being prompted.**

**And a frank limitation that identifies the paper's own central weakness** — that it cannot separate baseline severity from true longitudinal change.

**So why only 3.**

**Because the stated conclusion is contradicted by the reported numbers.** The paper claims "no statistically significant difference in model performance across data sets" and "stable performance across devices." **Its own bootstrap intervals for VFI and MD on Heidelberg do not overlap the internal intervals.** Non-overlap of 95% intervals is a conservative criterion — stricter than a significance test — so these differences are real at well under p = 0.05. A reader who takes the abstract at face value gets the wrong answer about the thing the paper is most valuable for.

**And the authors flag the result as "surprising" and contrary to the literature, then explain it rather than re-check it.** They offer three reasonable mechanisms — standardised preprocessing, attention robustness, regression being more transportable than classification — for a phenomenon that, by their own numbers, did not occur on the device that mattered. **When a result contradicts the field and your own intervals disagree with your summary, the intervals are the place to look.**

**The clinical value over predicting the average is unestablished.** Their own mean-reference model was "slightly lower," with improvement "modest, particularly for VFI and PSD." **The number that would settle this is in a supplementary table I cannot read.** I am not asserting the model is worthless — I am recording that **the paper's own comparator leaves its added value unquantified**, and that two further findings point the same way: the **proportional bias** the authors report in the Bland–Altman plots, and an outcome range **compressed from both ends** by excluding advanced glaucoma *and* excluding eyes that improved.

**The comparator that would matter most was never run.** Every eye had a baseline visual field. **Nobody reported how well "assume the future field resembles the current one" performs.** Combined with the authors' admission that the model cannot distinguish baseline severity from longitudinal change, this means **the forecasting claim — the paper's entire novelty — rests on a comparison that was available and absent.**

**The test–retest argument is the wrong yardstick and does real work in the paper.** The Discussion compares the model's MAE to the noise in measuring the same eye twice, and concludes the predictions are "statistically robust and clinically meaningful." Section 5 explains why that comparison cannot support that conclusion.

**44.4% of eligible eyes were excluded on follow-up interval alone** — 1,432 of 3,224 — for reasons of analytic convenience rather than clinical definition. And **eyes that improved were excluded**, which truncates the outcome distribution on one side only.

**There is no held-out internal test set.** 135 configurations were screened on a single 80/20 split, and that same 20% is reported as "internal validation," making those numbers selection-optimistic. **Mitigating, and only knowable because they did external validation: the Zeiss external results are very close to internal, so the optimism appears small.**

**A commercial disclosure exists that I cannot read**, with three authors including the first at a private company, and the paper proposing integration into commercial OCT systems.

**Why not 2.** Because yesterday's entry scored 2 for missing analyses — no external validation, no calibration, and an ablation that was never run. **Here the analyses were run and reported; the error is in the interpretation.** That is a materially better paper, because **a careful reader with the full text can reach the right conclusion using only the paper's own numbers.** The data corrects the discussion.

**Why not 4.** Because the headline claim about the thing that makes this paper valuable — cross-device transportability — is wrong by the paper's own evidence, and because the forecasting claim has no standard-of-care comparator.

**What would make this a 4, concretely.** **Say what the intervals say:** report the Heidelberg degradation as a finding, with the biases, rather than as consistency. **Add one comparator** — future visual field predicted from baseline visual field — and report the model's error against it. **Quantify the mean-reference margin in the main text**, not a supplement. **Report error on the change**, not only on the level. **Try the intercept recalibration** on Heidelberg, which the bias figures suggest would recover most of the loss. Four of those five use data the authors already have.

## 4. The Editor's Concerns

**1. The central claim is refuted by the paper's own confidence intervals.** The Discussion states: external validation "demonstrated error rates highly consistent with those observed in the model development cohort, indicating stable performance across devices. Importantly, **no statistically significant difference in model performance across data sets.**" The abstract says **"strong performance across 2 OCT devices."** Against that: **internal MD 1.76 (1.61–1.93) versus Heidelberg MD 2.71 (2.51–2.91)** — a clear gap between 1.93 and 2.51, with no overlap. **Internal VFI 3.23 (2.91–3.56) versus Heidelberg 4.14 (3.82–4.46)** — again no overlap. **Two of three indices show non-overlapping 95% intervals**, which is a stricter criterion than a p-value below 0.05. Only PSD overlaps, and barely (1.21 against an upper bound of 1.27). **A reader who reads the abstract learns the opposite of what the data show**, on precisely the question that makes this paper worth reading.

**2. "Surprising" was the signal to re-check, not to explain.** The authors write that the finding of stable cross-device performance "was surprising and contrasts with existing literature, which agrees that models trained on images from one OCT machine may lead to instrument-specific biases that reduce performance in a different clinical setting." They then offer three mechanisms for why their model escaped this. **The literature was right.** Their own numbers show instrument-specific bias — biases of +1.05, +1.83 and +1.13 on Heidelberg against 0.05, 0.17 and 0.08 on Zeiss — and reduced performance on two of three indices. **When your result contradicts an established consensus, and your own intervals disagree with your summary sentence, the intervals win.**

**3. The two external sets answer two different questions, and the paper pools them.** This is the design's most valuable property and it is used as though it were redundancy. **Essendon is a new site with the same device**: it tests whether the model survives new patients, new clinicians, new referral patterns. It did, essentially perfectly, with near-zero bias. **Gladstone Park is a new site with a different device**: it additionally tests whether the model survives different hardware. It did not. **Because one external set holds the device constant and the other does not, the difference between them isolates the device effect** — which is a cleaner natural experiment than most papers manage deliberately. The paper describes both as "external validation" and averages the message into "robust generalizability."

**4. And the devices differ in scan geometry, not merely in brand.** Zeiss acquires a **6 × 6 mm cube** (200 × 200 scans) from which the RNFL image is extracted by ZEISS FORUM. Heidelberg acquires a **circular line scan on a 3.5 mm circle** via Heidelberg Eye Explorer. Even the quality gates are non-equivalent: **signal strength ≥ 7 of 10 versus quality ≥ 20 of 40.** The team's standardisation — fixing brightness at 255 and contrast at 30, exporting both at 1,356 × 904 — is sensible and is credited. **It cannot make a cube-derived image and a circle scan into the same picture.** So the Heidelberg degradation is the expected result, which makes calling its absence "surprising" doubly odd.

**5. The good news the paper misses: most of the Heidelberg failure is a fixable offset.** For MD, the mean bias is **+1.83 dB** against an MAE of **2.71 dB** — so roughly **two-thirds of the average error is a constant shift**, not random scatter. For PSD the bias is **1.13** against an MAE of **1.37**, an even larger share. **A systematic offset is the most tractable kind of transportability failure**: recalibrating the intercept on a modest sample of Heidelberg scans should recover most of the loss, and the authors have 280 such scans. **This is a constructive, actionable finding sitting unused in their own Bland–Altman results** — and it is more useful than the claim they made instead.

**6. A mean-reference model came close, and the margin is unquantifiable from the main text.** The authors are commendably direct: the comparators "showed slightly lower performance metrics," the improvement was **"modest, particularly for VFI and PSD,"** and handcrafted features "may capture **little additional prognostic signal beyond the average follow-up VF outcome.**" **A mean-reference model predicts the same number for every patient.** If that is only slightly worse than a Vision Transformer, the scan is contributing little — and **the numbers that would settle it are in a supplementary table.** For a paper whose claim is that one OCT scan forecasts visual function, **the comparison against ignoring the scan belongs in the abstract.**

**7. The comparator that matters most was available and never run.** All three comparators use OCT image features. **None uses the patient's own baseline visual field** — which every eye had, which was an inclusion criterion, and which appears in the paper's own correlation matrix. For early-to-moderate glaucoma over about five years, "the future field will resemble the current field" is a strong predictor, and it is **free, standard-of-care information.** Until the model is shown to beat it, "forecasting future visual field from a single OCT scan" is not established as clinically additive. **This is yesterday's logistic-regression lesson one level up:** not "does a simpler model match it?" but "does the information the clinician already has match it?"

**8. Predicting a level is not predicting change, and the authors say so.** Their limitation: the model "can predict future key VF indices **without distinguishing between the impacts of baseline disease severity and true longitudinal changes.**" This is the most important sentence in the paper. Future MD is baseline MD plus change. In a cohort restricted to early-to-moderate disease, the change over five years is small relative to the spread between patients — so **a model that merely reads current severity off the scan will score well on the future level while carrying no prognostic information whatsoever.** The paper's own introduction concedes that cross-sectional structure–function mapping from OCT is already established. **The novelty claimed is forecasting; the design cannot separate forecasting from the mapping that was already known.** Reporting error on the *change* would settle it, and is not done.

**9. Test–retest variability is the wrong comparison and it carries the clinical-significance argument.** The Discussion cites Swanson et al — repeat Humphrey testing gives MD variation of +2.5 to −1.4 dB (SD 0.9) and PSD of 0.9 to 2.1 (SD 0.3) — then notes the model's MAEs of 1.76 and 1.14 are "comparable to or lower than the inherent test–retest variability," concluding the predictions are "statistically robust and clinically meaningful" and that this "enables the identification of eyes requiring treatment escalation from the baseline visit." **Test–retest variability is the noise in measuring the same state twice. The model's MAE is the error in predicting a different state 4.74 years later.** Section 5 works through why beating measurement noise can be a symptom rather than an achievement when the quantity barely moves — and the right denominator, the magnitude of actual change, is in a table I cannot read.

**10. 44.4% of eligible eyes were excluded because their follow-up interval was inconvenient.** From 3,224 eyes down to **1,792**, dropping **1,432**, to keep only those within one standard deviation of the mean follow-up (2.15–7.33 years), "to minimize the influence of outliers." **Follow-up duration is not a clinical criterion and it is not random.** Patients with very short intervals may have been lost to follow-up, moved, or died; those with very long intervals may be stable enough to be seen rarely. **Selecting on follow-up duration selects on everything correlated with it.** It also bounds the model: **its validated horizon is 2.15 to 7.33 years and no wider**, which the paper does not state as a deployment constraint.

**11. Excluding eyes that improved truncates the outcome on one side only.** "Eyes showing an improvement in VF from baseline... were excluded to minimize the postcataract surgery effect." The motive is legitimate — cataract surgery brightens the whole field and would masquerade as glaucoma improvement. **The cost is that the upper tail of change is removed**, so the cohort is enriched for progression and the outcome range is compressed further on top of the advanced-glaucoma exclusion at the other end. **The fraction of eyes removed by this rule is not reported**, so the size of the effect cannot be assessed. Any exclusion defined by the outcome reshapes the outcome distribution, and that deserves a number.

**12. No held-out internal test set.** 135 configurations were screened — 15 architectures × 3 loss functions × 3 optimizers, which I verified — on a single patient-level 80/20 split, and **the same 20% is reported as "internal validation."** Selecting the winner among 135 candidates on a set and then reporting performance on that set is optimistic by construction. **The mitigation is real and worth stating: the Zeiss external results (1.92 versus 1.76 for MD) are close enough to internal that the optimism appears small** — and that reassurance exists only because external validation was done. Separately, the screening MAEs quoted as **5.4–7.6** for ViT and **9.0–10.3** for CNNs are on a visibly different scale from the final reported **1.14–3.23**, and the paper does not reconcile them; the "47% error reduction" also compares the best model to the tenth-best rather than to any baseline.

**13. Two saliency observations that belong in the same paragraph.** The paper reports that attention fell partly on **the retinal pigment epithelium and outer retinal layers** — and the RPE is not where glaucoma acts; glaucoma destroys retinal ganglion cells and their axons, which are the RNFL and inner retina. Separately, it reports that off-RNFL attention occurred **"especially in Heidelberg Spectralis OCT device-driven scans."** **That is the same device on which performance degraded.** The two facts appear in different parts of the Results and are never joined. **An explanation anomaly and a performance drop pointing at the same subgroup is corroboration, not coincidence** — and together they suggest the model is reading something device-specific rather than something glaucomatous. **Full credit to the authors for reporting both honestly**, including naming "blood vessel shadows, image quality, differences in scan quality across OCT machine vendors, or artifacts" as candidates; the connection is the only thing missing.

**14. A commercial disclosure exists and is unreadable, which matters here.** The abstract carries the journal's flag that proprietary or commercial disclosure appears in the Footnotes, and that section is not in the retrieved text. **What is verifiable from the affiliations: three of eleven authors, including the first author, are at Pandani Solutions Pty Ltd**, and the paper states the model "could be integrated into existing OCT systems." Funding is not reported in what I retrieved. **I am not alleging anything undisclosed** — the journal flagged a disclosure, which is the system working. A reader should go and read it, because the overclaim in concern 1 runs in the direction of commercial interest.

**15. No reporting guideline, now eight consecutive entries — and the second in a row where it would have helped.** The sequence: entry 69 named TRIPOD+AI with the checklist; 70 named STROBE; 71 none; 73 none, while calling for a checklist that does not exist; 74 none, while doing more of what TRIPOD+AI asks than any of them; 75 none, while running the best multiplicity treatment in this list; 76 *measured the phenomenon* at **40% mean completeness**; 77 none, where TRIPOD+AI would have forced calibration and a prediction horizon. **Entry 78 names none, and TRIPOD+AI requires reporting against a simple baseline model — which is concern 7 exactly.** The rule holds and keeps earning its clause: **the checklist is not the quality signal; read the methods — and when something is missing, the checklist tells you what to look for.**

## 5. Statistics Spotlight

Three concepts, numbered from 283 in the running list in `queue.md`. The first is the load-bearing one and this paper is an unusually clean case of it.

**Non-overlapping confidence intervals refute "no significant difference" — read the intervals, not the adjective.**

This paper reports that there was **"no statistically significant difference in model performance across data sets."** It also reports these numbers:

- **Internal mean deviation: MAE 1.76, 95% CI 1.61 to 1.93**
- **Heidelberg mean deviation: MAE 2.71, 95% CI 2.51 to 2.91**

**Those two intervals do not touch.** The internal one stops at 1.93; the Heidelberg one starts at 2.51. There is a gap of more than half a decibel between them. The same is true for the Visual Field Index: internal 2.91–3.56, Heidelberg 3.82–4.46. **Two of the three headline comparisons show no overlap at all.**

**What a confidence interval means, and why non-overlap is strong evidence.** A 95% confidence interval is the range of values consistent with the data — roughly, if you repeated the study many times, intervals built this way would contain the true value about 95 times in 100. Here they were built by **bootstrap resampling**: repeatedly drawing a sample of the test set with replacement, recomputing the error, and seeing how much it moves.

**Now the key logical point, and it is often got backwards.** When two 95% intervals **do not overlap**, the difference between the two quantities is statistically significant — and **significant at a level stricter than 0.05.** The intuition: each interval already stretches about two standard errors either side of its estimate, so for them to clear each other entirely the estimates must be more than about four standard errors apart, where a conventional test needs only about two. **Non-overlap is a conservative test. If the intervals miss each other, the difference is real by any standard you like.**

**And the converse trap, which is the more common error.** **Overlapping intervals do *not* prove there is no difference.** Two intervals can overlap substantially while a proper paired test still finds a clear difference. "The intervals overlap, so performance is the same" is not a valid inference — it is the absence of evidence being reported as evidence of absence.

**So the asymmetry is useful and worth memorising.** **Intervals that miss each other: difference established. Intervals that overlap: undetermined, go and do the test.** This paper is in the first case and reports the conclusion of neither.

**The everyday version.** Two bakeries claim identical delivery times. The first says "between 20 and 24 minutes." The second says "between 31 and 36 minutes." You do not need a statistician to tell you these are different, and you do not need to know anything about their methods. **The ranges do not touch.** If instead the second had said "between 23 and 28 minutes," the ranges would overlap and you genuinely would not know — that is when you need the formal comparison. **This paper is the first bakery pair, described in the language of the second.**

**Watch out for:** a paper that asserts "no significant difference," "comparable performance," "consistent across sites" or "stable" **next to a table of confidence intervals it does not compare.** Do the comparison yourself; it takes ten seconds per row. **Two specific red flags:** an author who calls a non-degradation result "surprising" or "contrary to the literature" — that is the moment to check the intervals, because the literature is usually right and the summary sentence is usually where the error lives — and a paper that reports intervals but performs no test between groups, leaving the reader to assume one was done.

**Site transportability and device transportability are different questions — and this design separates them.**

This is the most valuable thing in the paper and it arrives almost by accident. There were **two** external validation sets, and they differ in exactly one respect:

- **Essendon Eye Clinic: new site, new patients, new clinicians — same scanner brand (Zeiss).**
- **Gladstone Park Eye Clinic: new site, new patients, new clinicians — AND a different scanner brand (Heidelberg).**

Because one holds the device constant and the other does not, **the difference between the two results isolates the effect of changing the hardware.** That is a controlled comparison, and it gives a clear answer:

- **Zeiss site: MD error 1.92 against 1.76 internally. Mean bias +0.17 dB. All intervals overlap.** The model travelled.
- **Heidelberg site: MD error 2.71. Mean bias +1.83 dB. Intervals do not overlap.** It did not.

**This list has a technique for the distinction** (number 194, from entry 68): **reproducibility** of a pipeline, **portability** of a workflow and **transportability** of a fitted model are three different properties. This paper demonstrates a fourth split inside the last one. **A model can be transportable across institutions and not across instruments**, and most papers that claim "external validation" only ever test the first.

**Why devices break models when sites do not.** A new site changes the *patients* — different ages, severities, referral patterns. A model that learned real biology survives that. A new device changes the *measurement itself*: here, a 6 × 6 mm cube scan versus a 3.5 mm circle scan, different segmentation software, different quality scales. **Anything the model learned about how the image was made, rather than about the eye, breaks.** And the bias pattern shows exactly that: near-zero offset at the new Zeiss site, a one-directional offset on all three measures at Heidelberg.

**The everyday version.** You train yourself to judge a room's temperature by reading a particular wall thermometer. Move to another building with **the same model of thermometer** and you are fine — different room, same instrument. Move to a building with **a different brand**, mounted differently and calibrated differently, and every reading is off by a couple of degrees in the same direction. **Your skill at judging temperature did not change. Your skill at reading that one instrument did not transfer.** The giveaway is that the errors all lean the same way.

**Watch out for:** "externally validated" used without saying what changed. **Ask three questions: new patients? new institution? new equipment or assay?** A model validated across hospitals that all use the same scanner, analyser or assay platform has shown much less than one validated across platforms. **And when a paper does test across devices, look for the bias, not just the error** — an error that grows with a consistent directional offset is an instrument problem, and that is the single most informative pattern you can find in an external validation.

**When degradation is mostly systematic bias, it is fixable — so measure the bias separately from the scatter.**

The Bland–Altman analysis is where this paper's most actionable finding sits, unused. A **Bland–Altman plot** charts the error between predicted and actual values and reports two separate things: the **mean bias** (how far off you are on average, and in which direction) and the **limits of agreement** (how much individual predictions scatter around that). **These are different problems with different fixes**, and lumping them into a single error number hides which one you have.

Here is what this paper found:

- **Heidelberg mean bias: +1.05 for VFI, +1.83 dB for MD, +1.13 dB for PSD** — all positive, all three measures.
- **Zeiss mean bias: +0.05, +0.17, +0.08** — essentially zero.

Now put the bias next to the total error. **Heidelberg MD: mean bias 1.83 dB, total MAE 2.71 dB.** So about **two-thirds of the average error is a constant shift in one direction.** For PSD it is a larger share still: bias 1.13 against MAE 1.37.

**Why that distinction changes what you do about it.** A **constant offset** means the model's readings are systematically displaced — like a scale that reads two kilograms heavy. **You fix that by subtracting two kilograms**, and you can work out how much to subtract from a modest sample. **Random scatter** means the model is unreliable patient by patient, and no single correction helps; you need a better model. **Bias is cheap to fix. Scatter is not.**

So the constructive reading of the Heidelberg result, which the paper does not state: **recalibrating the intercept on a sample of Heidelberg scans should recover most of the lost accuracy.** The authors have 280 such scans. **That is a far more useful conclusion than "performance was stable."**

**One caution the paper does report, honestly, and it cuts the other way.** The limits of agreement were **"wide across the OCT machines, particularly for VFI and MD, indicating clinically meaningful individual-level variability,"** and the plots **"suggested proportional bias, with prediction errors varying across the range of VF indices."** So there is also real scatter, and the bias is not perfectly constant — it changes across the range. **Proportional bias is the fingerprint of predictions being pulled toward the middle of the distribution**, which is what minimising average error does when the outcome has been compressed. Here it was compressed from both ends: advanced glaucoma excluded at one end, improving eyes excluded at the other. **That is the same mechanism as the mean-reference model coming close** — three independent signs of one phenomenon.

**The everyday version.** Two archers both miss the target by six inches on average. The first puts every arrow six inches high, tightly grouped. **The second scatters arrows all around the bullseye, six inches out in random directions.** Same average error, completely different problems. **The first archer adjusts their sight once and is excellent. The second needs to learn to shoot.** If you only report "six inches," nobody can tell which archer they hired.

**Watch out for:** external validation reported as a single error number with no bias and no limits of agreement. **Ask for a Bland–Altman plot or its two numbers**, because "MAE rose from 1.76 to 2.71" and "MAE rose from 1.76 to 2.71, of which 1.83 is a constant offset" call for completely different responses — the first says start again, the second says recalibrate. **And treat proportional bias as a warning**, not a footnote: it means the model's errors depend on the true value, which usually means predictions are being shrunk toward the average.

## 6. Jargon Translator

**Glaucoma** — a progressive disease of the optic nerve in which retinal ganglion cells and their axons die, causing permanent visual-field loss. Eye pressure is the only treatable risk factor, and lowering it does not always stop progression.

**Visual field (VF) test / standard automated perimetry** — you stare at a central point and press a button when you see faint flashes in your peripheral vision. Slow, tiring, and noticeably noisy from one sitting to the next.

**Mean deviation (MD)** — in decibels, how much dimmer the patient's whole visual field is than a healthy age-matched eye. **0 is normal; more negative is worse.** Here anything worse than −12 dB was excluded.

**Pattern standard deviation (PSD)** — in decibels, how *uneven* the field is. Glaucoma typically damages patches, so unevenness is informative; higher is generally worse.

**Visual Field Index (VFI)** — a 0–100% summary of remaining visual function, weighted toward the centre. 100% is full function.

**Decibel (dB), in perimetry** — a measure of light sensitivity on a logarithmic scale, not a sound measure. A few decibels of MD is a clinically meaningful amount.

**OCT (optical coherence tomography)** — a quick, non-contact scan that builds a cross-sectional picture of the retina using light. Standard in eye clinics.

**Retinal nerve fibre layer (RNFL)** — the layer of nerve axons carrying signals from the retina to the brain. **It thins as glaucoma progresses**, which is why it is imaged.

**Optic nerve head (ONH)** — where the nerve fibres exit the eye. The scans here were centred on it.

**Retinal pigment epithelium (RPE)** — a layer *underneath* the retina with a supporting role. **Not where glaucoma does its damage**, which is why attention falling there is a flag — concern 13.

**Floor effect** — the point where a measurement stops being able to get worse. RNFL thickness hits one in advanced glaucoma because non-nerve tissue remains, which is why advanced cases were excluded.

**Vision Transformer (ViT)** — an image model that cuts the picture into small patches (14 × 14 pixels here) and uses attention to decide which patches matter in light of the others, rather than scanning with small local filters as a CNN does.

**Convolutional neural network (CNN)** — the older dominant approach: layers of small filters detecting local patterns like edges, built up into abstract features.

**DINOv2 / self-supervised pretraining** — a way of pretraining an image model on unlabelled pictures so it learns general visual structure before being fine-tuned on a small labelled dataset. Used by the winning configuration here.

**Regression (versus classification)** — predicting a number (a future MD of −4.2 dB) rather than a category (progressing or stable). This paper predicts numbers.

**MAE (mean absolute error)** — the average size of the mistake, in the outcome's own units. Easy to read and **it rewards predicting the middle of the distribution** when the outcome is compressed — technique 285.

**RMSE (root mean squared error)** — like MAE but punishes large individual mistakes more heavily. Always at least as large as MAE; the gap between them indicates how much big errors contribute.

**Bootstrap confidence interval** — resample the test set with replacement many times, recompute the metric each time, and read off the range. How the intervals here were built, and **the reason the device degradation is visible** — technique 283.

**Bland–Altman plot** — a plot of prediction error that separates **mean bias** (average offset, and its direction) from **limits of agreement** (individual scatter). **Two different problems with two different fixes** — technique 285.

**Proportional bias** — when the error depends on the true value rather than being constant. **The fingerprint of predictions being shrunk toward the average.**

**Test–retest variability** — how much a measurement changes when you repeat it on the same unchanged patient. **Pure measurement noise, and the wrong yardstick for prediction error** — concern 9.

**Saliency / attention map** — a heatmap of which image regions most influenced the output. **A description of what the model did, not evidence it is right** — entry 74.

**Kruskal–Wallis test / Spearman correlation** — distribution-free tests, used here to check whether error varied with follow-up length across groups and continuously.

**Wilcoxon signed-rank test** — a paired distribution-free test, used here to confirm baseline and follow-up visual fields genuinely differed.

**Hodapp–Parrish–Anderson criteria** — a standard staging system for glaucoma severity by visual-field damage, used here for the −12 dB cutoff and for identifying improved eyes.

## 7. What You Can (and Can't) Say

**You can say:**

"A Vision Transformer trained on single baseline OCT nerve-fibre-layer scans from 1,792 eyes of 1,610 patients predicted visual-field indices a mean of 4.74 years later with mean absolute errors of 3.23 for the Visual Field Index, 1.76 dB for mean deviation and 1.14 dB for pattern standard deviation on internal validation."

"The model was externally validated at two independent clinics, which is unusual and valuable: performance held at a second site using the same scanner brand, with near-zero mean bias (0.05, 0.17 dB and 0.08 dB)."

"At a third clinic using a different manufacturer's scanner, error rose on all three indices — mean deviation from 1.76 to 2.71 dB and the Visual Field Index from 3.23 to 4.14 — with 95% confidence intervals that do not overlap the internal intervals for those two indices."

"On that different device the model showed a one-directional mean bias on all three measures (+1.05, +1.83 dB, +1.13 dB), so most of the added error on mean deviation and pattern standard deviation is a systematic offset rather than random scatter."

"The authors report that limits of agreement were wide for the Visual Field Index and mean deviation, indicating clinically meaningful individual-level variability, and that the plots suggested proportional bias."

"The authors state the model cannot distinguish the contribution of baseline disease severity from true longitudinal change, and that their image-only comparator models — including a mean-reference model — were only slightly worse than the Vision Transformer."

**You cannot say:**

"The model performs equally well across OCT devices." **Its own confidence intervals for the Visual Field Index and mean deviation on the Heidelberg device do not overlap the internal intervals.** Non-overlapping 95% intervals indicate a difference at a stricter level than p = 0.05.

"There was no statistically significant difference in performance across datasets." **This is the paper's sentence and the reported intervals contradict it** for two of three indices.

"One OCT scan can forecast a patient's visual field." **Not established as better than the information already available.** No comparator used the patient's own baseline visual field, and the authors state the model cannot separate baseline severity from longitudinal change.

"The model beats simply predicting the average." **Possibly, and the margin is unquantifiable from the main text.** The authors describe the improvement over image-only comparators including a mean-reference model as "modest, particularly for VFI and PSD."

"Prediction error is within test–retest variability, so the predictions are clinically meaningful." **Test–retest variability is the noise in measuring the same state twice; this is error in predicting a different state years later.** The relevant comparison is with the magnitude of actual change, which is not in the retrievable text.

"Saliency maps confirm the model uses glaucoma-relevant anatomy." **The paper explicitly declines to claim this**, notes that attention also fell on the retinal pigment epithelium and outer retina, and that off-RNFL attention occurred especially in Heidelberg scans — the device where performance dropped.

"This works for any follow-up interval." **Validated for 2.15 to 7.33 years only**; 44.4% of otherwise eligible eyes were excluded for falling outside that window.

"This applies to glaucoma generally." **Early-to-moderate only** — eyes worse than −12 dB mean deviation were excluded, and so were eyes whose fields improved.

"The Vision Transformer architecture is what makes this work." **Not shown.** The architecture comparison was a 135-configuration screen on the same split later reported as internal validation, and the decisive comparison — against standard clinical information — was not run.

**The honest one-sentence version:** *a well-designed study that did the rare and valuable thing of testing its model on a second manufacturer's scanner, found that it degraded there — by 54% on mean deviation, with non-overlapping confidence intervals and a systematic one-directional bias — reported the degradation in its numbers while describing it as stability in its text, and separately disclosed that a model which ignores the scan entirely and predicts the cohort average was only slightly worse.*

## 8. Bottom Line for Your Life

**If you have glaucoma or are being monitored as a suspect:** nothing here changes your care, and this is not a tool you can be offered yet — the authors say it needs further work and should be "a complementary risk-stratification tool rather than a replacement for standard VF-based progression assessment." **The durable message from the paper's own framing is that visual-field loss in glaucoma is irreversible and that many eyes keep progressing on apparently adequate treatment.** That is the case for keeping your monitoring appointments, not for a new scan.

**If you are an ophthalmologist being shown this kind of tool by a vendor:** ask the question this paper accidentally answers beautifully. **"Was it validated on my scanner, or on a scanner of the same brand as the one it was trained on?"** Here the answer mattered enormously: near-zero bias at a new clinic with the same brand, and a +1.83 dB systematic offset on a different brand. **And ask for the bias, not just the average error** — because a one-directional offset can be recalibrated on a few hundred of your own scans, while random scatter cannot be fixed at all.

**If you buy, commission or regulate medical AI, this entry is a three-question test.** **What changed between development and validation — patients, institution, or equipment?** **Is the reported degradation tested, or asserted to be absent?** (Compare the confidence intervals yourself; it takes seconds, and here it reverses the conclusion.) And **what does the model beat?** Not another model of the same data — **the information the clinician already has.** In this case that is the patient's own previous visual field test, and it was never tried.

**If you read papers for a living, the transferable skill from this entry is ten seconds long.** When a paper says "comparable," "consistent," "stable" or "no significant difference," **find the two confidence intervals and see whether they touch.** If they do not, the difference is real regardless of the adjective. If they do overlap, you have learned nothing either way and the paper owes you a test. **That single habit would have caught the central error here, and it requires no statistics beyond reading two pairs of numbers.**

**If you are reading the coverage:** expect "AI predicts glaucoma vision loss years in advance from a single scan." The study is real, the external validation is better than most, and the errors are honestly reported. The three things that will not make the headline are that **performance dropped significantly on the other manufacturer's scanner**, that **a model which ignores the scan and predicts the average was only slightly worse**, and that **nobody checked whether the patient's own previous visual field test would have done just as well.**

**This is education, not medical advice.** Nothing here should change anyone's glaucoma treatment or monitoring schedule. If you have glaucoma, the schedule that matters is the one your own ophthalmologist sets.

---

## Appendix: the pre-registered question, verification, and status on 2026-11-15

**The pre-registered question, and its answer.** This pick was set yesterday with one question written down in advance: **"did performance drop between the two devices, and by how much?"** — on the reasoning that entry 77's two decisive weaknesses were internal validation only and a feature set that might contain its own label, and that item (D) was the one paper on the shelf validated on different hardware. **The answer: yes, substantially, and the paper says otherwise.** Relative increases in MAE on the Heidelberg device were **VFI +28.2%, MD +54.0%, PSD +20.2%**, with **non-overlapping 95% confidence intervals for VFI and MD**, and a **one-directional mean bias on all three indices** (+1.05, +1.83, +1.13) against near-zero bias (+0.05, +0.17, +0.08) at the same-device external site. **The second carried-forward instruction — check the reported prevalence and what PPV would be in a screening population (technique 275) — does not apply**, because this is a regression model predicting continuous indices rather than a classifier, so there is no prevalence and no PPV. Recording that explicitly rather than silently dropping it.

**Arithmetic verified today, every check passing.** The exclusion cascade closes exactly: **4,038 − 23 poor-quality OCT − 791 unreliable VF = 3,224**, as stated; then **3,224 − 1,792 = 1,432 eyes dropped on follow-up interval alone, 44.4% of the eligible pool.** The follow-up window **4.74 ± 2.59 → 2.15–7.33 years** reproduces exactly. **1,792 eyes / 1,610 patients = 1.11 eyes per patient.** The architecture screen **15 × 3 × 3 = 135** confirms the stated count. External retention: **150/188 (79.8%)** Zeiss, **280/377 (74.3%)** Heidelberg. CI overlap tested for all six internal-versus-external comparisons: **all three Zeiss comparisons overlap; Heidelberg VFI and MD do not** (gaps 3.56→3.82 and 1.93→2.51), Heidelberg PSD overlaps narrowly (1.21 against 1.27). Bias as a share of MAE on Heidelberg: **VFI 25%, MD 68%, PSD 82%.** **No arithmetic error was found in the paper** — the numbers are all correct; the error is that the prose does not describe them.

**What could not be verified.** All figures, tables and supplementary material, which costs four specific things: **the comparator table**, so the margin of the Vision Transformer over the **mean-reference model cannot be quantified** — the single most important missing number; **the magnitude of actual visual-field change** between baseline and follow-up, so the ratio of model error to real change cannot be computed; **the fraction of eyes removed by the "excluded if improved" rule**; and **the Footnotes and Disclosures section**, which the abstract flags as carrying a proprietary or commercial disclosure. Also absent from the retrieved text: any **R², correlation or variance-explained** measure; **funding**; any **reporting guideline**. Verifiable from affiliations and reported here as such: **three of eleven authors, including the first author, are at Pandani Solutions Pty Ltd.** **Nothing was reproduced that was not seen, and no comparator result was estimated.**

**Positive practice worth carrying forward.** External validation at two sites on two devices; **bootstrap CIs on every metric**, which is the only reason the degradation is detectable; a **mean-reference comparator**, run and honestly reported; **Bland–Altman with mean bias and limits of agreement** for both external sets; two HREC approvals with numbers and consent waivers; a follow-up-interval sensitivity analysis by two methods; **the best saliency caveat in this reading list**, naming non-biological candidates and declining to treat the maps as proof; a frank limitation identifying the paper's own central weakness; and an **AI-writing-tool disclosure** (Grammarly, for readability and grammar).

**Deferred status, 2026-11-15.** ***Annals* *Choosing Wisely* (42896192) — day 26**, weekly re-check and **abstract-only date both 2026-11-19**, four days out and the next scheduled fallback; standing note that its 5.4% / 0.6–12.2% CI is a clustering signature computed across 15 recommendations rather than 4,050 responses. **Gait foundation model (42995231) — day 7**, abstract-only date **2026-11-30**; largest multiplicity problem this list will have faced (**1,887 of 3,210 tested phenotypes called significant**), first question being what false-discovery-rate procedure ran across those 3,210 tests. Both were last re-checked 2026-11-13 with no PMC copy; **neither is near threshold, so re-checks stay on schedule rather than daily.**

**Landmark check, 2026-11-08 → 11-15.** Three records, all previously assessed: the NEJM mass-surveillance Perspective (43001754), the *Nature Medicine* gait commentary (43003904), and the gait foundation model itself (42995231). **No new candidates; none displaces the queue.**

**Plan set on 2026-11-15.** **Next run takes shelf item (B)**, the bone-tumour review arguing that **reference-standard instability is the binding constraint** on diagnostic AI (PMID 42997475, PMC13742044), **because the last three entries have converged on it from three directions and (B) is the paper that addresses it head-on.** Entry 76 found harms and methods reporting incomplete at 40% against the instrument written for the job; entry 77's label was an ICD code that may have been co-written with two of its own predictors; **entry 78's outcome is a visual-field test whose own test–retest noise the paper had to invoke as a yardstick — and whose measurement changed when the device changed.** All three are failures of the *reference standard*, not of the model. **First question for (B): does it quantify reference-standard disagreement, or only argue for it?** — because technique 265 says a claim about a binding constraint needs a measured one. **Carry technique 283 forward too:** a review of this kind will report pooled estimates with intervals, and the habit of checking whether intervals touch applies to every forest plot in it. **Shelf after today: three spares — (B) next, (E) MIBC pCR with 102 models screened, (F) bitewing mannequin-only.**

**Standing watch item:** PM Heart trial results (protocol PMID 42893738), quarterly.
