# Large-scale esophageal cancer screening through noncontrast computed tomography and artificial intelligence

**Authors:** Zhou J, Guo G, Yao J, Yu Q, Zheng C, Feng X, Ye X, Zhou Y, Yang P, Lambert L, … Zhang D, Ji J, Li N, Xie C, Cao K, Zhao Y, Zhang L, Wang Q (43 authors; DAMO Academy / Alibaba Group, Hupan Lab, Sun Yat-sen University Cancer Center, and twelve further centres in China, the Czech Republic and Australia)
**Journal:** Nature Medicine, 2026; 32(10): 3748–3759 (published 22 September 2026)
**Decoded:** 2026-10-17 (abstract only) · **REWRITTEN FROM FULL TEXT 2026-10-18**
**Analysis basis:** **FULL TEXT** (retrieved from PubMed Central, PMC13668756). Figures, Extended Data and all Supplementary material were not viewable, so anything living only there is marked as not retrieved.

> **Note on this summary's history.** This paper was the reading list's highest-priority backlog entry for 26 days. On 2026-10-17 a PMC identifier existed but served no body text, and five retrieval routes failed, so it was decoded from the abstract with a provisional grade and an explicit commitment to rewrite. On 2026-10-18 the full text became available and this summary was rewritten from it. **Section 3 records where yesterday's abstract-only reading was right and where it was wrong**, because that comparison is itself instructive.

**Source links (all verified):**
- DOI: https://doi.org/10.1038/s41591-026-04656-4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42773211/
- Full text (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC13668756/
- Trial registration: stated as Chinese Clinical Trial Registry **ChiCTR2300074806** (the identifier is stripped from the PMC rendering of the Methods but appears in the abstract). The registry was not reachable from this session, so the record itself **could not be independently verified**.
- **Funding and competing interests: not retrievable.** Nature Medicine places these in the online-only end matter, which the PMC rendering does not include. Note that a substantial share of the authorship is employed by DAMO Academy / Alibaba Group and Hupan Lab, who built the model.

---

## 1. The Gist

Oesophageal cancer kills most of the people who get it, because by the time it causes symptoms it is usually too late. Caught early it is often curable. There has been no practical way to catch it early: the reliable test is endoscopy, a camera down the throat, which is invasive and which nobody will do on a whole population.

Meanwhile, millions of people get an ordinary chest CT every year for unrelated reasons. The oesophagus is in every one of those scans. Nobody looks at it, because it is a floppy, collapsed tube that moves with the heartbeat and an early tumour in it is essentially invisible. Radiologists do not even try.

This group built an AI to try anyway, and then — unusually — spent most of the paper stress-testing it rather than celebrating it.

The headline is that on chest CTs from eight hospitals in China, the Czech Republic and Australia, it cleared 98.5% of people without cancer while catching 90.0% of cancers. But the most valuable number in the paper is a different one. When they ran the same model on 20,758 consecutive real patients — people coming through outpatients, emergency and inpatient wards rather than a curated research cohort — **specificity fell from 98.5% to 95.5%.** They report that drop, explain it, then go away and fix it: they retrained on the hard cases, cut false positives by 72.7%, and ran the improved model prospectively on 17,446 people. In that prospective deployment, 90 people were flagged, 38 genuinely had disease, and one cancer was found that the hospital's normal process had missed.

Three things to carry away, two of them warnings.

The threshold discipline is exemplary. The cut-off was fixed in cross-validation *before* any test cohort was touched, using a stated rule — 99% specificity for hospital screening, 98% sensitivity for population screening. Having spent this week on two papers that tuned thresholds on the data they then reported, the contrast is stark.

**First warning: it still misses about half of pre-cancer.** 90.0% for cancer, 52.5% for high-grade dysplasia. Screening exists to catch disease *before* it becomes cancer. That gap is the paper's real limitation and it survives full-text reading.

**Second warning: the most quotable claim in the paper — that triaging people to endoscopy by AI would triple the detection rate — comes from a simulation.** The prospective screening cohort of 530 people contained six precancerous lesions and **zero invasive cancers**. To do the analysis, the authors added three cancers by resampling from a different, retrospective cohort. They say so plainly in the Methods. The abstract does not.

## 2. Study Snapshot

**Design:** development and multi-cohort validation of a two-stage deep learning model, EAGLE, detecting oesophageal malignancy — high-grade intraepithelial neoplasia (HGIN) and oesophageal cancer (EC) — on non-contrast chest CT. Retrospective internal and external testing, real-world calibration, prospective hospital deployment, a reader study, and a prospective endoscopic-screening cohort.

**Ethics:** individual institutional review board approval obtained from twelve named institutions. Registered at ChiCTR.

**Reference standard — the question I could not answer yesterday, now answered.** Positive cases were confirmed by **surgical or biopsy histopathology** and staged by the AJCC 8th edition. Negative controls were defined as **free of malignant oesophageal lesions by at least 2 years of clinical follow-up, or a negative endoscopy within 1 year.** The authors add, unprompted: "It remains possible that a minor fraction of indolent lesions remained undetected during the follow-up period, thereby introducing potential label noise."

**Training:** 6,813 scans from two centres — 264 HGIN, 548 stage I, 2,932 stages II–IV, and 3,069 negative controls. Lesions were annotated on paired **contrast-enhanced** CT (where boundaries are visible) by two radiologists with ≥3 years' oesophageal experience, agreement measured by Dice coefficient, masks with Dice >0.6 merged and lower-agreement cases adjudicated by a radiologist with >8 years' experience; annotations were then transferred to the non-contrast scan by image registration. Cases that could not be confidently delineated were excluded from training.

**All validation cohorts, and the arithmetic now closes.** The abstract named six cohorts summing to 77,582 against a stated 80,612 — a gap of 3,030 I flagged yesterday. The full text supplies both missing pieces: an **internal test cohort of 2,500** never mentioned in the abstract, and the **530-patient prospective endoscopic cohort**. 77,582 + 2,500 + 530 = 80,612 exactly.

- **Internal test** — 2,500 patients (18 HGIN, 181 stage I, 948 stages II–IV, 134 positives without staging, 1,219 negatives). AUC 0.991 (0.989–0.994), sensitivity 89.4% (87.7–91.1), specificity 99.3% (98.8–99.8).
- **External multicentre test** — eight centres in China, the Czech Republic and Australia; 11,466 patients (40 HGIN, 363 stage I, 2,404 stages II–IV, 8,654 negatives). AUC 0.976 (0.972–0.980), sensitivity 89.5% (88.3–90.6), specificity 98.5% (98.2–98.8). Czech cohort sensitivity 94.4%, Australian 90.2%.
- **LDCT test** — 147 malignant and 1,460 negative, 1,607 total. With low-dose simulation training, sensitivity 88.4% versus 83.0% without (p = 0.024) at the 99% specificity threshold.
- **Real-world calibration and validation** — 35,402 patients across three centres, split into two continuous series: **RW1 (20,758)** for calibration and **RW2 (14,644)** for testing.
- **Prospective hospital validation** — 17,446 patients, enrolled January–April 2025, follow-up to 31 July 2026.
- **Real-world LDCT screening** — 10,959 consecutive participants aged 45–75, July–December 2024.
- **Endoscopic-screening external test** — 702 patients (552 malignant, 150 negative) who had both CT and endoscopy; 68.6% of the malignancies were HGIN or stage I–II.
- **Prospective endoscopic-screening cohort** — 530 participants enrolled over 20 days in July 2023.

**Subgroup sensitivity, which is where the real story is:** HGIN 50.0% internal, 52.5% external, 42.9% on LDCT, 65.0% in the endoscopic-screening cohort. Stage I EC 65.7% internal, 60.1% external, 78.4% in the endoscopic-screening cohort. Sensitivity rose with stage; it was higher in the middle oesophagus than at the gastro-oesophageal junction, higher in men than women, and higher at body mass index ≤22. At a matched specificity of 91.0% — chosen to match a liquid-biopsy comparator — stage I sensitivity rose to 73.4%.

**Threshold selection — prespecified and fixed.** "Thresholds were determined during fivefold cross-validation and were fixed after training… the final threshold was fixed as the mean value across the five folds." The rule was declared in advance: **99% specificity** for opportunistic screening, **98% sensitivity** for population screening. Final fixed values: 0.93 for EAGLE, 0.88 for EAGLE-Plus.

**What happened in the real world.** In RW1 (20,758 consecutive patients, 285 malignancies, prevalence 1.37%), sensitivity held at 89.6% but **specificity fell from 98.5% to 95.5%**, which the authors attribute to including outpatient, inpatient and emergency populations "whose clinical profiles differed substantially from the curated cohorts used for model development." EAGLE also found three cancers the standard pathway had missed, one of them 21 months before clinical diagnosis.

**The fix.** Hard cases from RW1 — all false positives, all false negatives, plus borderline true positives to keep a roughly 1:1 ratio — were re-annotated and merged into training for 200 further epochs, producing EAGLE-Plus. On RW2 (14,644 patients, 163 malignancies), false positives fell **from 432 to 118 (−72.7%)**, PPV rose **from 25.3% to 55.0%** (p < 0.001), and sensitivity was essentially unchanged (89.8% → 88.3%, p = 0.62).

**Prospective deployment.** 17,446 patients; 47 malignancies confirmed (41 EC, 6 HGIN); 90 AI-positive predictions (a 0.52% positive rate); 38 true positives. **PPV 42.2% (31.8–52.1), sensitivity 80.9% (69.2–91.3) for malignancy and 87.8% for EC.** Of the 90 flagged, 48 were already being managed by the normal pathway; of the remaining 42, the multidisciplinary team referred 16 for endoscopy (an AI-triggered referral rate of 0.09%), **3 actually attended**, and one T3N0M0 cancer was found and treated. The primary endpoint was prespecified as PPV. Among patients negative on both AI and standard care, about **1%** were randomly audited.

**Real-world LDCT.** 10,959 participants, **8 positive predictions** (0.07%), specificity 99.94% (99.88–99.97), **PPV 12.5%** — which on 8 predictions means exactly one confirmed cancer. Five of the eight did not attend the recommended endoscopy.

**Reader study — not mentioned in the abstract at all.** 300 scans (200 malignant, 100 negative) from four centres, read by **17 radiologists** (3 oesophageal subspecialists, 6 general radiologists, 8 residents; mean 7.6 years' experience), twice, with a **≥3-month washout** and randomised order. EAGLE beat the reader average by 19.1 points of sensitivity and 18.4 of specificity (p < 0.001). With AI assistance, reader sensitivity rose 71.9% → 85.7% and specificity 79.6% → 91.7% (both p < 0.001), with HGIN sensitivity up 16.6 points and stage I up 22.7.

**The triage claim.** The 530-person prospective cohort yielded **six HGIN and no invasive cancers**. The authors constructed a hybrid cohort by resampling three EC cases from a separate retrospective cohort, repeated 1,000 times, giving 9 malignancies in 533. In that simulated cohort, triaging only AI-positive people to endoscopy raised the detection rate from 1.7% to 5.2%, cut the number needed to screen from 59.2 to 19.2, and avoided a stated 67.6% of endoscopies.

**Statistics:** bootstrap resampling with 1,000 iterations for all 95% confidence intervals; DeLong's test for paired AUCs; permutation tests (≥1,000) for sensitivity, specificity and balanced accuracy; McNemar's test for paired binary outcomes. Fixed random seed. **"No adjustment was made for multiple comparisons"** — stated openly.

## 3. How Strong Is This Evidence? (Grade 4/5)

Four out of five. The grade is the same as yesterday's provisional one, but the basis is entirely different: yesterday I was grading a design as described, and said so. Now it is graded on verification, and it holds up.

**Where yesterday's abstract-only reading was right, and where it was wrong.** This comparison is worth recording, because it is a measurement of how much an abstract can and cannot tell you.

*Right:* that the validation programme was exceptionally broad; that precancer sensitivity was the real limitation; that the cohort arithmetic left 3,030 patients unexplained (it was an unnamed internal test cohort plus the prospective endoscopic cohort, exactly as guessed); and that different operating points were in play.

*Wrong, or half-wrong:* I suspected the multiple operating points might invite cherry-picking. They do invite misquotation, but they were **prespecified in cross-validation and fixed before testing** — the opposite of cherry-picking, and the single best thing about the paper's method. I could not see that from the abstract.

*Right answer, wrong road:* I reconstructed the calibration as taking specificity to 99.59% at a prevalence of 0.33%, predicting a PPV of 42.1% against the paper's reported 42.2%. The full text shows the prospective cohort had prevalence 0.269% and sensitivity 80.9%, not the 90% I assumed, with implied specificity 99.70%. Two errors cancelled. The method was sound; the agreement was partly luck. I would not have known that without the full text, which is the point.

**What the full text shows that earns the grade.**

**The threshold discipline.** Fixed in cross-validation, averaged across five folds, locked before testing, with the operating criterion stated in advance and differing by clinical use. This is the practice two of this week's other papers lacked.

**They ran it against reality and published the damage.** The drop from 98.5% to 95.5% specificity when the model met consecutive unselected patients is the most useful number in the paper, and most teams would have buried it. Instead it became the motivation for the next experiment.

**The calibration is a real engineering cycle, not a reanalysis.** Hard cases were identified in one continuous series, re-annotated, merged into training, and the improved model tested on a *different* continuous series from the same centres. Every number checks: 432 → 118 false positives is a 72.7% reduction; the implied true positives reproduce the reported PPVs of 25.3% and 55.0% exactly.

**Prospective deployment with a prespecified primary endpoint**, integrated into a live system, with the standard-of-care radiologists blinded to AI output and no feedback loop. One cancer was found that would otherwise have been missed.

**A proper reader study** — 17 readers, two rounds, three-month washout, randomised order — that the abstract never mentions. And the authors report the uncomfortable result: AI alone (an implied 91.0% sensitivity in that cohort) **outperformed AI-assisted humans (85.7%)**, and they discuss why rather than hiding it.

**Honest limitations**, including follow-up shorter than two years, poor compliance with recommended endoscopy, label noise in the negative controls, sex imbalance in training, and the simulation-based nature of the triage evidence.

**What holds it at 4 rather than 5.**

**The headline cohort is not a screening population.** The external test cohort is 2,812 malignant against 8,654 negative — **24.5% prevalence**. That is a case-control-like design. Real screening populations in this paper run 0.27% to 1.37%. The 98.5% specificity was measured where a quarter of patients had cancer, and the authors' own RW1 result shows what happens when it meets 1.37% prevalence. Not a flaw so much as a reason the headline figures should never be quoted as screening performance.

**The triage headline rests on synthetic cancers.** Six HGIN, zero invasive cancers, three cancers injected by resampling from a different cohort. The Methods are transparent; the abstract's "exploratory analyses of a prospectively enrolled cohort" is not. And I could not reconcile the stated 67.6% of endoscopies avoided with the 75.5% implied by the numbers in the text — the difference may sit in an Extended Data figure I could not view.

**The real-world LDCT result rests on one confirmed cancer.** Eight positive predictions, PPV 12.5%, so exactly one true positive — and five of the eight never had the recommended endoscopy. Worse, the reported 95% interval for that PPV is **7.1–25.0%**, which cannot be right: an exact binomial interval for 1 of 8 runs from roughly 0.3% to 52.7%, and a bootstrap over eight observations can only produce PPVs at multiples of 1/8. The point estimate is what it is; the interval is an artefact of applying a bootstrap below the sample size where it works.

**An unexplained count.** The LDCT test cohort is stated as 147 malignant. The Methods describe 4 malignant from one centre and 85 additionally retrieved from another — 89. Fifty-eight positives are unaccounted for in the retrieved text.

**A small internal inconsistency in the reader study:** readers are described as having interpreted "an average of 1,141 esophageal CT scans (range = 100–1,000)". A mean cannot lie outside its own range.

**Model selection used the external cohort.** The ResEnc backbone was chosen partly because "in the eight-center external validation cohort… it achieved the highest sensitivity (89.5%) and specificity (98.5%), outperforming other models." That is selecting on the test set — a milder version of the problem, since the differences were small and the AUC actually favoured another backbone, but it means the external figures carry some selection optimism.

**No multiplicity adjustment**, stated openly, across a paper with a great many comparisons.

**Precancer sensitivity is still about half.** 52.5% externally, 42.9% on low-dose CT. The authors show the trade-off honestly — at 91% specificity, stage I sensitivity rises to 73.4% — but at the operating point they propose for hospital screening, half of precancer is missed.

**Where 4/5 sits.** This is the most thoroughly validated medical-AI paper decoded in this list: twelve centres, three countries, a validation set twelve times the training set, a real-world failure honestly reported and then engineered against, a prospective deployment, and a reader study. It falls short of 5/5 because the screening case it most wants to make — that this should triage people to endoscopy — rests on a simulation with synthetic cancers, and because the thing screening most needs, precancer detection, is where it is weakest.

## 4. The Editor's Concerns

**Say in the abstract that the triage analysis used simulated cancers.** My main request. "Exploratory analyses of a prospectively enrolled cohort suggest that referring high-risk individuals for endoscopy could improve screening efficiency" is the sentence that will be cited, and it describes an analysis in which the cancers were resampled from a different cohort because the prospective one contained none. The Methods are scrupulous about this. The abstract should be too.

**Report the real-world specificity in the abstract alongside the 98.5%.** The drop to 95.5% in consecutive unselected patients is the paper's most transferable finding and appears nowhere in the summary.

**Give the external cohort's prevalence where the 98.5% is quoted.** A reader cannot otherwise know that the headline figures come from a cohort that is 24.5% cancer.

**Withdraw or recompute the LDCT PPV interval.** A 95% CI of 7.1–25.0% on one true positive out of eight is not attainable by any valid method. An exact binomial interval would be roughly 0.3–52.7%, which is honest and tells the reader the result is a single case.

**Reconcile 147 with 89 in the LDCT test cohort**, and reconcile the 67.6% of endoscopies avoided with the 75.5% the stated numbers imply.

**Fix the reader-experience range.** A mean of 1,141 cannot sit inside a range of 100–1,000.

**Put funding and competing interests where readers see them.** They are in Nature's online-only end matter, which means they are absent from the PMC rendering most readers will reach. With roughly a quarter of the authorship at the model's developer, this matters.

**Audit more than 1% of the double negatives.** Sensitivity in the prospective and LDCT cohorts depends on who later presented plus a 1% sample. The authors acknowledge the follow-up is under two years; a larger audit would firm up the one number a screening programme cannot do without.

**Report the interval-cancer rate when follow-up matures.** It is the real measure of what a screening programme missed, and it is the obvious next publication.

**Note the backbone selection.** Choosing ResEnc partly on external-cohort sensitivity and specificity should be flagged, since the external figures are then not entirely out-of-sample.

**One thing I would not change.** The decision to report RW1's specificity collapse, investigate it, fix it, and test the fix on a separate series. That sequence is what the rest of the field should copy.

## 5. Statistics Spotlight

### Concept 1: Why the headline cohort flatters, and what happened when the model met reality

Yesterday, working from the abstract, I taught the screening arithmetic in the abstract: how 98.5% specificity turns into five false alarms per cancer at low prevalence. The full text contains something better — **the authors ran that experiment themselves.**

**The setup.** The external test cohort has 2,812 cancers among 11,466 patients: **24.5% prevalence**. That is not a screening population; it is closer to a case-control study, assembled by taking known cancers and known non-cancers. Nothing wrong with it for measuring whether a model can tell the two apart — but it is not where the model will be used.

**What happened next.** They ran the same model on **20,758 consecutive patients** from outpatients, emergency and inpatient wards — prevalence **1.37%**. The result:

- sensitivity held: 89.5% → 89.6%
- **specificity fell: 98.5% → 95.5%**

Sensitivity is a property of the diseased; it travels. Specificity is measured on the well, and the "well" in a curated cohort are not the "well" of a real hospital. A real hospital's negatives include pneumonias, hiatus hernias, oesophagitis, post-radiation change and a hundred other things that look abnormal. The authors say exactly this: the drop came from patients "whose clinical profiles differed substantially from the curated cohorts used for model development."

**Why three percentage points is a lot.** At 1.37% prevalence in 20,758 people, roughly 285 have cancer and 20,473 do not.

- At 98.5% specificity: about 307 false positives.
- At 95.5% specificity: about 921 false positives.

Three points of specificity tripled the false-alarm workload. That is the difference between a tool a radiology department will tolerate and one it will switch off.

**An analogy.** A spell-checker tested on a textbook looks superb. Run it over real correspondence — names, jargon, addresses, abbreviations — and it underlines everything. The checker did not get worse. The "normal" text got more varied.

**Watch out.** When a diagnostic AI paper reports a test-cohort prevalence anywhere near the prevalence of its positives, check whether that cohort was assembled by *collecting cases and controls* rather than by *taking consecutive patients*. If so, the specificity is an upper bound. The tell is a prevalence far above the disease's real frequency: 24.5% for a cancer that affects well under 1% of a hospital population.

### Concept 2: What a calibration cycle looks like, and how to check one

The second half of this paper is an engineering loop, and it is worth understanding as a template.

**The problem.** After RW1, the model was generating 432 false positives per 14,644-ish patients. Too many.

**The loop.** They took the hard cases from RW1 — every false positive, every false negative, plus borderline true positives to keep hard negatives and hard positives at roughly 1:1 — had them re-annotated by the same expert radiologist, merged them into the training data, and fine-tuned for 200 more epochs. They then tested the result on **RW2, a different continuous series from the same centres**.

That last detail is what makes it legitimate. Calibrating on one slice and testing on another slice collected at a different time is a weak form of external validation, but it is a genuine out-of-sample test. Calibrating and reporting on the same data would have been worthless.

**The result, and how to verify it.** RW2 had 14,644 patients with 163 malignancies.

- EAGLE: sensitivity 89.8% → about 146 true positives; 432 false positives; PPV = 146/(146+432) = **25.3%** ✓ matches the reported figure.
- EAGLE-Plus: sensitivity 88.3% → about 144 true positives; 118 false positives; PPV = 144/(144+118) = **55.0%** ✓ matches.
- False-positive reduction: (432−118)/432 = **72.7%** ✓ matches.

Everything reconciles, which is reassuring about the rest.

**The thing to notice.** Sensitivity went from 89.8% to 88.3% — a drop of 1.5 points, and the paper reports the comparison as non-significant (p = 0.62). Cutting false positives almost always costs sensitivity. Here it cost very little, which is the achievement. **Whenever a paper reports a reduction in false positives, look immediately for what happened to sensitivity.** If it is not reported, assume it fell.

**Watch out.** "We reduced false positives by X%" is meaningless without three things: the sensitivity before and after, the cohort it was measured on, and whether that cohort is the one used to do the reducing. This paper supplies all three. Most do not.

### Concept 3: When a confidence interval is an artefact — and when a result is one case

Two related failures of small numbers, both visible in this paper's real-world LDCT cohort.

**The result.** 10,959 participants. Eight positive predictions. PPV 12.5%.

A PPV of 12.5% from eight predictions means exactly **one true positive**. The entire real-world low-dose screening result — the one that produced the striking 99.94% specificity — rests on a single confirmed cancer. Five of the eight flagged people never had the recommended endoscopy.

**Now the interval.** The paper reports that PPV as 12.5% with a 95% confidence interval of **7.1–25.0%**.

That interval cannot be right, and you can see why without any software. The study used bootstrap resampling: repeatedly draw 8 observations with replacement and recompute. But with eight predictions of which one is a true positive, a resampled PPV can only ever be 0/8, 1/8, 2/8 and so on — a handful of discrete values. The bootstrap distribution is lumpy and does not approximate anything.

The right tool is an exact binomial (Clopper–Pearson) interval, and for 1 out of 8 it runs from roughly **0.3% to 52.7%**. That is the honest statement: with one case, you know almost nothing about the true PPV.

**A worked intuition.** You flip an unfamiliar coin eight times and get one head. What is the chance of heads? Your best guess is 1 in 8. But would you bet that the truth lies between 7% and 25%? Of course not — eight flips is consistent with almost any coin that is not two-tailed. The data permit a huge range, and a method that returns a narrow one is not measuring uncertainty, it is hiding it.

**Why this matters beyond this paper.** Bootstrapping is the default in modern medical AI because it is easy and assumption-free. It is excellent with hundreds of events — and this paper uses it entirely appropriately for its large cohorts, where the intervals are credible. It fails silently when events are few, which is precisely the situation in rare-disease screening. **The signal to watch for: a suspiciously tight interval around a proportion with a tiny denominator.** When you see one, count the events. If there are fewer than about ten, the interval should be wide, and if it is not, it is an artefact.

**And the broader point about one-case results.** Even with a correct interval, "one cancer found among 10,959 people" is a demonstration that the pipeline runs end-to-end, not a measurement of how well it works. The authors are reasonably careful about this in the Discussion, listing limited positive cases in the real-world LDCT cohort among their limitations. The abstract's "99.94% specificity" is the part that will travel, and it is the figure from the same eight-prediction cohort.

## 6. Jargon Translator

**Oesophageal cancer (EC)** — Cancer of the food pipe. Deadly largely because it is found late. **ESCC** (squamous cell carcinoma) and **EAC** (adenocarcinoma) are the two main types.

**HGIN (high-grade intraepithelial neoplasia)** — Precancerous change: abnormal cells confined to the lining, not yet invasive. Usually removable endoscopically. The prize of screening.

**LGIN** — The lower-grade version; not malignant, but needs watching.

**Stage I / stages II–IV** — How far a cancer has spread. Stage I is confined and usually curable.

**Non-contrast CT (NC CT)** — A standard CT with no injected dye. Done constantly for unrelated reasons.

**Low-dose CT (LDCT)** — A CT using much less radiation, already used for lung cancer screening.

**Endoscopy / Lugol's chromoendoscopy** — Camera down the throat; the iodine stain makes abnormal areas stand out.

**Opportunistic screening** — Looking for one disease in scans done for something else.

**Standard of care (SOC)** — What the hospital does normally, here double reading by radiologists blinded to the AI.

**Sensitivity** — Of those with the disease, the share caught. **Specificity** — of those without, the share correctly cleared.

**Positive predictive value (PPV)** — Of those flagged, the share who really have it. Depends heavily on prevalence.

**Prevalence** — How common the disease is in the group tested.

**Operating point / threshold** — The score above which the model says positive. Here fixed in advance at 0.93 and 0.88.

**Calibration (as used here)** — Retraining on hard cases to cut false positives, then testing on fresh data.

**Hard-case mining** — Feeding a model its own mistakes as extra training data.

**nnU-Net / ResEnc / Swin-UNETR / Mamba** — Standard architectures for medical image segmentation. ResEnc is a conventional convolutional design; the others are newer transformer- and state-space-based alternatives.

**Dice similarity coefficient (DSC)** — Overlap between two outlines, 0 to 1. Used here both to measure agreement between annotators and to score the model's lesion outlines.

**Class activation mapping** — A heatmap showing which image regions drove the decision.

**Bootstrap resampling** — Estimating uncertainty by repeatedly resampling the data. Reliable with many events; unreliable with few.

**Clopper–Pearson (exact binomial) interval** — The conservative, always-valid interval for a proportion. The right tool when events are few.

**DeLong's test** — For comparing two AUCs measured on the same patients.

**Permutation test** — Shuffling labels many times to see how often chance reproduces the result.

**McNemar's test** — For comparing paired yes/no outcomes, such as two pathways applied to the same people.

**Multidisciplinary team (MDT)** — Radiologists, endoscopists and surgeons reviewing cases together.

**Washout period** — Time between a reader's two sessions so they cannot remember their earlier answers. Three months here.

**Interval cancer** — A cancer appearing between screening rounds after a negative result. Not yet reported.

## 7. What You Can (and Can't) Say

**You CAN say:**
- "An AI model detected oesophageal cancer and precancer on ordinary non-contrast chest CT, validated across twelve centres in three countries on more than 80,000 patients."
- "At eight external centres it achieved 89.5% sensitivity and 98.5% specificity, with an AUC of 0.976."
- "When run on 20,758 consecutive real patients, sensitivity held but specificity fell from 98.5% to 95.5% — and the team reported that, retrained on the hard cases, and cut false positives by 72.7% without losing sensitivity."
- "In a prospective deployment on 17,446 patients, 42.2% of those it flagged had confirmed disease, and it found one cancer the hospital's normal pathway had missed."
- "In a reader study with 17 radiologists, AI assistance raised sensitivity from 71.9% to 85.7% and specificity from 79.6% to 91.7%."
- "Decision thresholds were fixed in cross-validation before any test cohort was examined, using rules stated in advance."
- "Sensitivity for precancerous lesions was 52.5% externally — about half."

**You CAN'T say:**
- ❌ "It detects oesophageal cancer with 90% sensitivity and 99.94% specificity." Those come from different cohorts at different operating points. The 99.94% is from a cohort that produced eight positive predictions.
- ❌ "98.5% specificity is what you would see in practice." It was measured where 24.5% of patients had cancer. In consecutive real patients it was 95.5%.
- ❌ "AI triage would triple endoscopic detection rates." That comes from a simulation in which three cancers were resampled from a different cohort, because the prospective cohort contained none.
- ❌ "It catches oesophageal cancer early." It catches 90.0% of cancers and 52.5% of precancerous lesions at the hospital-screening threshold.
- ❌ "The low-dose screening result shows it works at population scale." That result is one confirmed cancer among eight predictions, with five flagged people never examined, and its reported confidence interval is not attainable by any valid method.
- ❌ "AI assistance makes radiologists as good as the AI." In this study the model alone (about 91% sensitivity in that cohort) outperformed AI-assisted readers (85.7%), and the authors say so.
- ❌ "This is ready for population screening." No interval-cancer rate, follow-up under two years, poor compliance with recommended endoscopy, and the triage case unproven on real cancers.

## 8. Bottom Line for Your Life

If you are at raised risk of oesophageal cancer — long-standing reflux, Barrett's oesophagus, a family history, or you live somewhere this cancer is common — nothing changes today. The accurate test is still endoscopy. What this paper makes plausible is that within a few years a chest CT you have for some entirely different reason might also get checked for this, at no extra scan, radiation or cost. On the evidence here that is a reasonable thing to hope for and not yet a thing to rely on.

If you work in radiology, gastroenterology or screening policy: the number to take seriously is not 98.5%. It is 95.5% — what the specificity became when the model met consecutive unselected patients — and then 72.7%, the false-positive reduction the team achieved by retraining on its own mistakes and testing on a fresh series. That loop is the transferable contribution. The open questions are the interval-cancer rate, precancer sensitivity, and whether the triage case survives contact with real cancers rather than resampled ones.

For your paper-reading, take two things.

**First: check the prevalence of the cohort that produced the headline.** A specificity measured where a quarter of patients have the disease is an upper bound, and this paper is unusually useful because the authors went and measured the real number themselves. Three points of specificity — 98.5% to 95.5% — tripled the false alarms. When a diagnostic AI paper reports a test cohort whose prevalence is wildly above the disease's real frequency, you are reading a laboratory result, not a deployment result.

**Second: count the events behind any proportion before you trust its confidence interval.** A PPV of 12.5% with an interval of 7.1–25.0% looks precise. It came from eight predictions and one true positive, where the honest interval runs from under 1% to over 50%. Bootstrapping is the default in this field and it is silently wrong when events are few — which is exactly the situation in rare-disease screening. Counting events takes a second, and it is the difference between a result and an artefact.

A last note on how this summary came to exist. Yesterday I published an analysis of this paper's abstract, clearly labelled, after twenty-six days of failed retrieval, with a provisional grade and a promise to rewrite. Today the full text opened and I rewrote it. The grade did not move. But I was wrong about one substantive thing — I suspected the multiple operating points might be opportunistic, and they turn out to have been prespecified and locked, which is the best feature of the paper's method. And I was right about the headline numbers by a route that contained two cancelling errors. Both of those are arguments for reading the methods, and neither would have been visible from a summary that did not say what it was based on.

---

*This is an educational analysis of a published scientific paper, not medical advice. Nothing here is guidance about cancer screening or your own risk. If you are worried about oesophageal cancer, talk to your doctor.*
