# The Paper That Tried to Prove Itself Wrong and Couldn't

**Paper:** CT radiomics showed no improvement beyond volume dynamics for early
lesion-level size response to immunotherapy in metastatic melanoma
**Authors:** Akbal S, Schepers JC, Op Gen Oorth PV, Bleymehl V, Schroth M,
Winneknecht F, Machiraju D, Holzschuh JC, Zhang KS, Wohlfeil S, Ayx I,
Schoenberg SO, Schlemmer HP, Hassel JC, Rotkopf LT
**Venue / Year:** Cancer Imaging, 2026;26(1) (published 2026-10-01)
**DOI:** https://doi.org/10.1186/s40644-026-01135-4
**PubMed:** https://pubmed.ncbi.nlm.nih.gov/42823717/
**Full text used:** https://pmc.ncbi.nlm.nih.gov/articles/PMC13632448/
**Basis of this analysis:** FULL TEXT (PubMed Central open-access copy,
retrieved 2026-10-05). The PMC rendering **stripped every table and figure
cross-reference**, leaving sentences such as "as shown in Table" and "Acquisition
and reconstruction parameters are summarized in Table" with no number attached,
and the tables and figures themselves did not render. The numbers quoted below
are those stated in the article body and abstract; **where a value lives only in
a table or supplement it is marked as not available in the text retrieved.**
That includes the sensitivity and specificity at the Youden threshold, the Brier
scores, the calibration intercepts and slopes, the precision-recall AUCs, the
numeric paired AUC differences, and every organ-specific and lesion-size
subgroup estimate.
**Date decoded:** 2026-10-05
**Evidence grade:** 5/5 — for the **conduct and reporting**. See the grading
section; the finding itself is deliberately a negative one.

All identifiers above were verified against the live PubMed and PubMed Central
records on 2026-10-05. Nothing here is based on a guessed or reconstructed link.

---

# The Gist

For about a decade, a field called **radiomics** has promised something
appealing: that an ordinary CT scan contains far more information than the
radiologist's eye extracts. Not just *how big is the tumour*, but the texture of
it — how grainy, how uniform, how the brightness is distributed inside the
outline. Run hundreds of these measurements through a machine-learning model and
you might predict which tumours will respond to treatment, from scans you
already took.

This study asked the question almost nobody in that field asks directly: **is
any of that better than simply measuring whether the tumour got bigger or
smaller?**

A German team took 158 patients with metastatic melanoma on immunotherapy and
traced **1,626 individual metastases** by hand across repeated CT scans. Then
they built five competing models to predict whether each lesion would be growing
by the second follow-up scan: one using clinical facts only, one using nothing
but **volume change**, one using radiomic texture, one using both, and one using
everything.

In the main centre, the volume-only model scored **0.84** on the standard
discrimination measure (where 0.5 is a coin flip). The radiomics model scored
**0.86**. Adding radiomics to volume produced a difference small enough to fall
inside a margin the team had **declared equivalent before looking**. Then they
sent all five models, unchanged, to a second hospital with different scanners.
There, volume scored **0.68** and radiomics scored **0.68**.

So: nothing. Hundreds of texture measurements, and the answer is the thing you
could get with a ruler.

What makes this a genuinely excellent paper is not the result. It is what they
did next. The obvious objection to a negative radiomics result is that the
texture features were just measuring size in disguise — so of course they added
nothing. The authors checked, and found the opposite: across **288** features the
median correlation with volume was only **0.37**, and when they stripped volume
out of the features mathematically, radiomics **kept** its accuracy — and
*still* added nothing to volume. Their own best excuse for the null result turned
out not to be true, and they published that.

Then they kept going. They tried a scanner-harmonisation method. They tried
filtering features for cross-centre stability. They tried higher-order textures,
spatial filters, four different binning widths, different learning algorithms,
repeated cross-validation, patient-level instead of lesion-level outcomes, and
reweighting to correct for patients who died before the second scan. Every one
of those is a lever that could have turned a null into a headline. None of them
did, and all of them are reported.

And one finding buried in the supplement is the quietest demolition in the whole
paper: **early volume change on its own, with no model fitted to it at all,
kept most of the volume model's accuracy internally and beat it at the outside
hospital.** The trivial baseline won.

The honest limit, which the authors state repeatedly rather than hide: that
outside hospital contributed **29 patients and 12 progression events.** That is
nowhere near enough to settle anything, and they say so — refusing to claim
equivalence externally even though the numbers came out identical.

# Study Snapshot

- **Study type:** Retrospective, bicentric (two-centre) prognostic-model
  comparison, with internal cross-validation and a single application to an
  independent external cohort. **Deliberately framed as an equivalence test,
  not a superiority test.**
- **Patients:** 158 with histologically confirmed stage IV melanoma on immune
  checkpoint inhibitors. Internal cohort **129**; external cohort **29**.
  Consecutive patients imaged in clinical routine at both sites.
- **Lesions:** **1,626** evaluable metastases. The primary second-follow-up
  analysis used **131 patients and 1,241 lesions** — so **27 patients (17.1%)
  and 385 lesions (23.7%)** fell out of the primary analysis. About **10.3**
  lesions per patient.
- **Periods:** Internal May 2013 to October 2023 (one standardised dual-energy
  scanner, Siemens SOMATOM Definition Flash). External March 2021 to July 2024
  (multiple scanners, varying reconstruction kernels and contrast timing —
  chosen deliberately to reflect real-world heterogeneity).
- **Segmentation:** Up to the ten largest measurable lesions per site per
  patient, hand-traced by trained medical doctoral students in MintLesion, all
  reviewed by a board-certified radiologist, **all readers blinded to outcomes
  and subsequent clinical course.** An independent second reading was done for
  inter-observer agreement.
- **Outcome:** Binary lesion-level size response at the second follow-up —
  clinical benefit (complete response, partial response, or stable disease)
  versus progressive disease — using RECIST 1.1 thresholds applied to the
  individual lesion. Progressive disease required at least a 20% **and** at
  least a 5 mm increase from the reference diameter (baseline at the first
  follow-up; the lesion's own nadir at the second).
- **Features:** 72 radiomic features per lesion per timepoint — first-order
  histogram, intensity-based, and gray-level co-occurrence matrix texture —
  extracted in compliance with the **Image Biomarker Standardization
  Initiative**, after resampling to 1 mm isotropic voxels with a fixed 5
  Hounsfield-unit bin width. Delta features computed between first follow-up and
  baseline. Volumes log-transformed. Clinical features: age, sex, regimen, time
  since first and since stage IV diagnosis, number of affected organs, baseline
  LDH (cohort mean substituted for three internal patients with no LDH value).
- **The five models:** M0 clinical; **M1 volumetric** (log volumes at baseline
  and first follow-up plus the interval between them) — used as the reference;
  M2 radiomics; M3 volumetric plus radiomics; M4 comprehensive.
- **Learner:** Random Forest with recursive feature elimination down to ten
  features or fewer, with variance filtering and univariate pre-selection to 50
  features performed **inside each cross-validation fold.**
- **Internal validation:** Four-fold **patient-grouped** cross-validation
  stratified by outcome, out-of-fold predictions pooled for the final metrics.
- **External validation:** The final model of each configuration was fitted on
  the full internal cohort and applied **once, unchanged**, to the external
  cohort. **No model included a centre indicator.**
- **Thresholds:** Sensitivity and specificity reported at the Youden threshold
  derived from the **internal out-of-fold** predictions, applied unchanged
  externally. (The values themselves are in a table that did not render.)
- **Statistics:** AUC as primary metric, 95% confidence intervals from **cluster
  bootstrap resampling at the patient level**. Model comparisons as paired AUC
  differences against the volumetric reference, cluster-bootstrapped at patient
  level, with **Holm-Bonferroni correction** within each cohort.
  **Equivalence concluded only when the entire confidence interval of the paired
  difference lay within a margin of ±0.05.** Also computed: precision-recall
  AUC, Brier score, balanced accuracy, calibration intercept and slope (values
  in non-rendered tables).
- **Headline results:** Baseline-only prediction of first-follow-up response was
  near chance for every model in both cohorts. For the second follow-up,
  internal AUC was **0.84 [95% CI 0.78–0.88]** for volumetrics and **0.86
  [0.81–0.90]** for radiomics; externally **0.68 [0.50–0.85]** and **0.68
  [0.51–0.88]**, with no significant difference between any models.
- **Volume-confounding check:** Across all 288 radiomic features, median
  absolute Spearman correlation with lesion volume **0.37**; **19 of 288
  (6.6%)** above 0.7; **8 of 288 (2.8%)** above 0.9, up to **0.98**.
- **Self-assessed quality:** **Radiomics Quality Score 18 of 36**, with
  item-level detail in the supplement.
- **Analysis software:** Python 3.12.
- **Ethics:** Approved by local committees (refs 2024–809 and S-415/2024);
  written informed consent waived.
- **Funding and competing interests:** **Not stated in the text retrieved.**

# How Strong Is This Evidence? — Grade 5/5

A note on what is being graded. The *finding* here is narrow and negative:
radiomics adds nothing to volume change for predicting one lesion's future size
in melanoma. That is a useful brick, not a cathedral. The five is for how the
brick was made — and on that, this is the most carefully executed paper this list
has decoded.

**It prespecified its own defeat condition.** "Our primary hypothesis is that
radiomics-containing models are equivalent to simple volume dynamics." Stating
an equivalence hypothesis up front, with a ±0.05 margin, and labelling the
external and organ-specific comparisons **exploratory in advance**, means the
authors could not later convert a scrape past significance into a discovery.
Almost nobody in this field does this.

**It treated 1,626 lesions as what they are: 1,626 observations from 158
people.** Patient-grouped cross-validation so the same patient never appears in
both training and testing. Cluster bootstrap at the patient level for every
confidence interval and every comparison. An equal-patient-weight sensitivity
analysis on top. Getting this wrong is the most common way a lesion-level
radiomics paper inflates itself, and they got it right three separate ways.

**It applied the external model once, unchanged, with no centre indicator.** No
refitting, no tuning on the external data, no "we adjusted for scanner." One
shot. That is what external validation is supposed to mean and rarely does.

**The decision threshold came from the internal out-of-fold predictions and was
applied unchanged externally.** Third paper in a row where this check mattered,
and the third different answer: entry 36 took its cutoff from the test set
(wrong), entry 37's protocol promised to take it from validation data (right in
principle), and this paper actually did it.

**It attacked its own result.** The standard rescue for a negative radiomics
finding is "our features were just proxies for size." They tested that four
ways — direct correlation, residualising features on volume, excluding
volume-correlated features, and redundancy filtering — and found radiomics
retained its discrimination through all of them while still adding nothing. The
excuse was available and they demolished it.

**It reported every lever it pulled.** ComBat harmonisation: no external
improvement. Cross-centre distribution filtering: a numerically higher external
radiomics AUC, not significant — and they volunteer that this filter "may
therefore reflect case mix as well as acquisition," undercutting their own most
favourable sensitivity analysis. An extended feature set with higher-order
texture families, spatial filters and four bin widths: no gain after adjustment.
Alternative learners, repeated cross-validation: unchanged. A
distribution-filtered comprehensive model that *was* significant internally
after Holm correction **and did not replicate externally** — reported anyway.

**It corrected for the dead.** Second-follow-up analysis only includes patients
who survived to a second scan, and survival correlates with response.
Inverse-probability weighting left the comparison unchanged — and they checked
rather than hand-waving.

**It states the alternative explanation that would rescue radiomics, and does
not dismiss it.** The largest lesions — where texture is most stably computed —
showed a numerical gain that did not survive correction, so "noise-limited
texture in small lesions cannot be excluded as a contributor to the negative
result." That is a sentence written by people trying to be right rather than to
win.

**It scored itself with a published instrument and reported a mediocre score.**
Radiomics Quality Score **18 of 36 — exactly 50%** — with item-level detail. Most
papers that cite the RQS use it on other people's work.

**And the honesty that matters most:** the external numbers came out *identical*
(0.68 versus 0.68), which would have been trivially spinnable as "equivalent in
external validation." They refused, because the confidence intervals were too
wide, and said so: "the estimates were too imprecise to establish equivalence or
a deficit." Getting the answer you predicted and declining to claim it is the
rarest thing in this list.

**What keeps the result modest rather than the grade low.** The external cohort
is tiny — 29 patients, 12 progression events — and the authors lead their own
limitations with it. The internal cohort spans more than ten years on one
scanner, over which melanoma treatment changed profoundly, and no within-cohort
temporal analysis is reported. Centre and treatment regimen are confounded, which
they state and say cannot be separated. The endpoint is a future *size
measurement*, not survival or symptoms. And the paper's own conclusion is
appropriately bounded: it "regards only incremental value over volume dynamics
for a size-based lesion-level endpoint and does not invalidate associations
reported for other endpoints."

# The Editor's Concerns

Short list, because most of what I would normally ask for is already in the
paper.

**The external cohort cannot support the word "equivalent," and to the authors'
credit it is never used there.** It is worth making the arithmetic explicit,
because it governs how the paper should be cited. With 12 progression events at
roughly the internal 1:4 event ratio, the approximate 95% confidence half-width
on a single AUC near 0.68 is about **0.18**. To get that half-width down to the
**0.05** equivalence margin takes on the order of **200 progression events** —
and that is before accounting for the within-patient clustering the authors
correctly handle, which pushes the requirement higher still. Twelve events is
roughly a sixteenth of the way there. Say this in the abstract, not only the
limitations.

**Add a temporal analysis within the internal cohort.** May 2013 to October 2023
is a decade in which combination checkpoint immunotherapy went from
investigational to standard, and the paper itself notes that regimens were
"balanced across therapies" internally but combination-dominant externally. Split
the internal cohort by era and report whether the volumetric model's AUC holds.
If performance drifts across treatment eras, that is more clinically important
than the radiomics question.

**Try to separate centre from regimen, even if underpowered.** Restrict both
cohorts to combination-immunotherapy patients and repeat the external
comparison. The result will be imprecise, and reporting that it is imprecise is
itself informative — right now "treatment-related differences in response
patterns cannot be separated from acquisition differences" leaves the external
null genuinely ambiguous between two very different causes.

**Name the near-tautology in the endpoint and bound it.** The strongest
predictor is volume change from baseline to first follow-up; the outcome is a
size change from the lesion's nadir to the second follow-up. The volumetric
model's internal AUC of 0.84 is partly a measure of **how autocorrelated tumour
growth is over consecutive scans** — which is a real and useful fact, but not the
same as predicting treatment benefit. The paper handles this better than most by
stating the endpoint's limits explicitly; it would be stronger still to report
the simplest possible benchmark head-on (the supplement's "early volume change
alone, without a fitted model" result) in the main text, since that comparison
is the one a clinician would actually make.

**Report the non-rendered numbers in the abstract.** Sensitivity, specificity,
calibration slope and precision-recall AUC all exist in tables. A reader who
only reaches the article body — which is what the open-access rendering served
me — cannot see any of them. Calibration in particular matters: the body says
calibration "decreased externally for all models," and the magnitude of that is
the difference between a usable tool and an uninterpretable one.

**Reconsider mean-substituting LDH,** even for three patients. It only affects
the clinical model, which lost anyway, so nothing turns on it — but it is the one
place in an otherwise careful paper where a quick fix was used instead of
multiple imputation.

**State funding and competing interests.** Not present in the text retrieved.

**And one point of praise that is also a request:** the Radiomics Quality Score
of 18 of 36 should be in the abstract. A field with a reproducibility problem
benefits more from authors publishing their own 50% than from anyone else's
commentary.

# Statistics Spotlight

Five ideas. The first is the paper's own primary method and is new to this list.

## 1. "No significant difference" is not "the same." Equivalence testing is.

This is the most useful statistical idea in the paper, and the one most often
got wrong in print.

Ordinary significance testing asks: *can I rule out that these two things are
identical?* If the answer is no — p is above 0.05 — people routinely write "there
was no difference between the groups." That is not what was shown. What was shown
is that **the study could not detect a difference**, which happens both when
there isn't one and when the study was too small to see one. Those two situations
look identical on paper and mean opposite things.

**Equivalence testing flips the question.** Instead of trying to rule out "no
difference," you first state **how big a difference would have to be before you
would care** — the *equivalence margin* — and then ask whether you can rule out
differences that large. You have shown equivalence only when **the entire
confidence interval of the difference fits inside the margin.**

This paper did exactly that, and prespecified the margin: **±0.05 of AUC.**
Their rule, quoted: "Equivalence was concluded only when the entire confidence
interval of the paired difference lay within a margin of ±0.05."

Now watch the same p-value mean two completely different things in the same
paper:

- **Internally**, adding radiomics to volume gave a paired difference whose
  whole interval sat inside ±0.05. Not just "not significant" — **positively
  demonstrated to be too small to matter.** Meanwhile, the clinical-only model
  was the one configuration that *exceeded* the margin, in the bad direction:
  demonstrably worse.
- **Externally**, no model differed significantly from volume either — and the
  authors drew **no conclusion at all**, because the intervals were far too wide
  to fit inside ±0.05. Same "not significant," no information.

**An everyday version.** Two bathroom scales. You weigh yourself on both and get
70.0 kg and 70.4 kg. Does that prove the scales agree? Only if you first decide
how close is close enough. If you need them within 0.1 kg for a medication dose,
a single pair of readings proves nothing — you need many weighings until you can
be confident the true gap is under 0.1 kg. If being within 2 kg is fine, one
reading might already settle it. **The margin has to come first, and from the
decision you are trying to make, not from the data.**

**Watch out for:** the phrase "no significant difference" standing in for "the
same." Ask two questions: was a margin stated in advance, and does the whole
confidence interval fit inside it? If no margin was named, the study has not
shown equivalence no matter how similar the numbers look. This is also why
"non-inferiority" trials — the drug-approval version of the same logic — live or
die on whether their margin was chosen honestly before the data arrived.

## 2. 1,626 lesions from 158 patients are not 1,626 observations

This is the single most common way a lesion-level imaging paper inflates itself,
and this paper is a clinic in avoiding it.

Measurements from the same patient are **not independent**. The same tumour
biology, the same drug, the same immune system, the same scanner, the same day.
If one liver metastasis is shrinking, its neighbour probably is too. So you do
not have 1,626 independent facts; you have something between 158 and 1,626,
depending on how alike one patient's lesions are.

The standard way to express this is the **design effect**. With *m* observations
per cluster and an intracluster correlation *ρ*, your **effective** sample size
is n ÷ (1 + (m−1)ρ). Here m ≈ **10.3** lesions per patient:

> ρ = 0 → effective n ≈ **1,626**
> ρ = 0.1 → effective n ≈ **843**
> ρ = 0.3 → effective n ≈ **429**
> ρ = 0.5 → effective n ≈ **288**

A modest correlation of 0.3 between a patient's own lesions would cut the real
information content by nearly four. If you ignore that, your confidence
intervals come out roughly half as wide as they should be, and small differences
look significant when they aren't.

Three things break if you ignore clustering, and this paper fixes all three:

**The split.** If you shuffle 1,626 lesions and put 80% in training, the same
patient's lesions land on both sides. The model can recognise the *patient* —
their scanner settings, their tumour burden, their anatomy — and get credit for
predicting lesions it has effectively already seen. The fix is
**patient-grouped cross-validation**: whole patients go into a fold, never split.
They used four-fold patient-grouped CV stratified by outcome.

**The confidence interval.** Ordinary bootstrapping resamples individual
lesions, which quietly assumes independence. **Cluster bootstrap** resamples
whole patients, preserving the within-patient structure. Every interval and
every comparison in this paper is cluster-bootstrapped at the patient level.

**The weighting.** A patient with 30 lesions counts thirty times as much as a
patient with one. They ran an **equal-patient-weight** sensitivity analysis and
report the AUCs changed "only slightly" — which is consistent with their finding
that within-patient response concordance was **low**, i.e. ρ here is genuinely
small and the effective sample size really is near the top of that table. Note
what happened: they did not *assume* the favourable case, they measured it.

**Watch out for:** any imaging, pathology or genomics paper that reports a large
N of *things* (lesions, slides, cells, teeth, eyes, images) drawn from a much
smaller number of *people*. Find the sentence about how the split and the
confidence intervals were done. If you cannot find the words "grouped,"
"clustered," "by patient," or "mixed effects," assume the intervals are too
narrow. Two eyes from one person is the classic case — and it is why this list's
earlier lesson on clustering and random intercepts (entry 30, the free-flap
meta-analysis) and this one are the same idea applied at opposite ends: there to
*pooling* results, here to *splitting* data.

## 3. What 12 events can and cannot settle

The external cohort is where this paper's result would have become a general
claim, and it is too small. Here is how to see that for yourself, which is a
transferable skill.

The precision of an AUC is driven mostly by the number of observations in the
**rarer** class. The external cohort had **12 progression events** across 20
patients. Using the standard approximation (Hanley and McNeil) at an AUC of 0.68
and the internal cohort's roughly 1:4 event-to-non-event ratio:

> **12 events** → 95% CI half-width ≈ **0.18**
> 25 events → ≈ 0.13
> 50 events → ≈ 0.09
> 100 events → ≈ 0.06
> **200 events** → ≈ **0.04** — finally inside the ±0.05 margin

And that matches what the paper actually reports: **external volumetric AUC 0.68
[0.50–0.85]**, an interval **0.35 wide** — three and a half times wider than the
internal one, and **wider than the entire range from "useless" to "excellent."**
Its lower bound is **exactly 0.50**: a coin flip is inside the confidence
interval.

So the external result is compatible with radiomics being worthless, and
compatible with it being a dramatic improvement. It distinguishes nothing. The
authors say precisely this, and it is why their conclusion rests on the internal
comparison and asks for "larger multicenter studies."

**An everyday version.** You want to know if a coin is fair. You flip it 12
times and get 7 heads. The honest answer is not "the coin is fair"; it is "12
flips cannot tell you." You'd need hundreds.

**Watch out for:** external validation sections with wide intervals presented as
confirmation. The giveaway is a confidence interval wider than about 0.15 of
AUC, or an interval whose lower bound is at or below 0.5. And watch for the
inverse of this paper's honesty: a study whose external numbers come out equal
and which calls that "validated." Equal point estimates with huge intervals is
not validation; it is a shrug.

## 4. "Independent predictor" is a claim about correlation, and it can be checked

The natural suspicion about a negative radiomics result is that the texture
features were secretly measuring size, so of course they added nothing to size.
Many radiomic features *do* track volume — bigger objects have more voxels,
smoother histograms, different texture statistics.

The authors tested it on all **288** features (72 features at four
timepoints/deltas) and reported the whole distribution rather than a summary
verdict:

- median absolute Spearman correlation with volume: **0.37**
- above 0.7: **19 of 288 (6.6%)**
- above 0.9: **8 of 288 (2.8%)**, up to **0.98**

Squaring a correlation tells you the **shared variance** — how much of one thing
is explained by the other:

> |ρ| = 0.37 → **14%** shared with volume
> |ρ| = 0.70 → **49%**
> |ρ| = 0.90 → **81%**
> |ρ| = 0.98 → **96%** — this feature *is* volume, wearing a texture name

So the typical feature overlaps volume by about a seventh, and only a handful are
near-duplicates. That alone does not settle it, so they went further:
**residualising** every feature on volume (mathematically removing the part that
volume explains), **excluding** the volume-correlated features entirely, and
**redundancy filtering**. In all three, radiomics "retained their discrimination"
and still "none improved on volume dynamics."

That is the interesting shape of this result. Radiomics is **not** a disguised
ruler — it carries real, volume-independent signal. It is just that the signal
it carries is not *additional* signal for this particular prediction.

**Watch out for:** the phrase "independent predictor." It almost always means
"survived a regression that included some other variables," not "uncorrelated
with them." Ask what the correlation actually was. And the reverse trap: when a
new expensive measurement correlates 0.9 with a cheap old one, a model containing
both will often credit the new one, because with that much overlap the two are
nearly interchangeable and which one the model picks is close to arbitrary.

## 5. The trivial baseline — and this time it won

This list has been running one check on every prediction paper: **what does the
simplest possible rule get?** Two days ago it was "refer every man." Here the
authors ran it on themselves, and the result is in the supplement:

> "Early volume change alone, without a fitted model, retained most of the
> discrimination of the volumetric model internally **and exceeded it
> externally**."

Read that again. Not "radiomics added nothing to the model." **The model added
nothing to a single number you can compute with a ruler and a calculator** — and
out of sample, at the hospital with different scanners, the raw number did
*better* than the Random Forest trained to use it.

This is the most important sentence in the paper and it is in a supplement.

Why would a fitted model lose to its own raw input? Because fitting costs
something. A Random Forest trained on 129 patients at one centre learns the
particular relationship between volume change and outcome **as it appeared at
that centre** — including the parts that were noise, and the parts that were
specific to one scanner and one era of treatment. Raw volume change has nothing
to overfit. It cannot learn the wrong lesson because it cannot learn. When the
setting changes, the thing that learned nothing travels better.

**An everyday version.** You want to predict whether a restaurant is good.
"Number of people inside at 8pm" is a crude rule that works roughly everywhere.
A model tuned on 129 restaurants in one city might beat it in that city and lose
to it in the next, because half of what it learned was about that city.

**Watch out for:** any paper where a complex model is compared only against other
complex models. The comparison that matters is against the simplest thing a
clinician could do unaided — one measurement, one threshold, no software. If the
paper does not report that comparison, compute it yourself from the baseline
table. If it does report it and loses, as here, that is the finding.

# Jargon Translator

- **Radiomics** — extracting many quantitative measurements (texture, shape,
  brightness distribution) from a medical image and feeding them to a model.
- **Texture feature / GLCM** — numbers describing how grainy or uniform a region
  looks. A gray-level co-occurrence matrix counts how often particular
  brightness pairs sit next to each other.
- **First-order / histogram feature** — a statistic of the brightness values
  alone, ignoring where they sit (mean, spread, skew).
- **Hounsfield unit (HU)** — the CT brightness scale. Water is 0, air is −1000.
- **Bin width** — how coarsely brightness values are grouped before texture is
  computed. Changing it changes the features, which is why a fixed value (5 HU
  here) must be stated.
- **IBSI** — Image Biomarker Standardization Initiative; the reference
  definitions that make radiomic features comparable between papers.
- **Delta (Δ) feature** — the change in a feature between two scans.
- **Volume dynamics** — how the lesion's volume changed between scans. The cheap
  comparator in this study.
- **RECIST 1.1 / iRECIST** — the standard rules for calling tumour response from
  size changes on imaging; iRECIST adapts them for immunotherapy's odd patterns.
- **Pseudoprogression** — a tumour appearing to grow on immunotherapy because of
  immune cells flooding in, then shrinking.
- **Lesion-level endpoint** — scoring each metastasis separately rather than the
  patient as a whole. Relevant because one patient's lesions often behave
  differently.
- **Oligoprogression** — a few lesions growing while the rest respond; the
  situation this lesion-level framing is meant to inform.
- **AUC** — pick one lesion that progressed and one that didn't; the AUC is the
  chance the model scores the progressing one higher. 0.5 is a coin flip.
- **Precision-recall AUC** — a companion to AUC that is more informative when the
  outcome is uncommon. Its no-skill baseline is the event rate.
- **Brier score** — average squared error of a probability forecast; only
  meaningful against the no-information value p(1−p).
- **Calibration intercept and slope** — whether predicted probabilities are
  systematically too high or too low (intercept) and whether they are too
  extreme or too timid (slope). A slope of 1 and intercept of 0 is perfect.
- **Youden threshold** — the cutoff maximising sensitivity plus specificity
  minus one.
- **Random Forest** — many decision trees averaged together.
- **Recursive feature elimination (RFE)** — repeatedly dropping the least useful
  predictor until few remain. Must happen **inside** each cross-validation fold,
  as it does here, or it leaks.
- **Nested model sets** — comparing models where each contains the previous
  one's variables plus more, so the added value of the extra information is
  isolated.
- **Patient-grouped cross-validation** — folds built from whole patients, so no
  patient appears in both training and testing.
- **Cluster bootstrap** — resampling whole patients rather than individual
  lesions when computing confidence intervals.
- **Intracluster correlation / design effect** — how alike observations within
  one patient are, and how much that shrinks your effective sample size.
- **Equivalence margin** — the largest difference you would consider
  unimportant, chosen before seeing data.
- **Holm-Bonferroni correction** — a way of tightening thresholds when several
  comparisons are made, so that testing five models does not manufacture a
  false positive.
- **ComBat harmonisation** — a statistical method for removing scanner- or
  site-specific shifts from feature values.
- **Residualisation** — removing the part of one variable that another explains,
  leaving the remainder.
- **Inverse-probability weighting (IPW)** — reweighting the people who remained
  in the analysis to stand in for those who dropped out, when dropout is related
  to outcome.
- **Spearman correlation (ρ)** — correlation based on ranks rather than raw
  values; robust to skew. Squaring it gives shared variance.
- **Radiomics Quality Score (RQS)** — a 36-point published checklist for
  radiomics study quality. This study scored its own work at 18.
- **LDH (lactate dehydrogenase)** — a blood marker; in melanoma a well-known
  prognostic factor.
- **Stage IV** — cancer that has spread to distant organs.
- **Immune checkpoint inhibitor** — a drug that releases the brakes on the
  immune system so it attacks the tumour.

# What You Can (and Can't) Say

**You can say:** in 158 melanoma patients on immunotherapy with 1,626 hand-traced
metastases, CT texture radiomics showed no conclusive improvement over simple
volume change for predicting whether an individual lesion would be growing at
the second follow-up scan — internal AUC 0.84 for volume versus 0.86 for
radiomics, with the combined model's difference falling inside a prespecified
±0.05 equivalence margin.

**You can say:** this held up against a deliberate attempt to overturn it —
scanner harmonisation, cross-centre feature filtering, higher-order texture
families, four bin widths, alternative learners, repeated cross-validation,
volume residualisation, patient-level endpoints, and reweighting for patients
who did not survive to the second scan.

**You can say:** radiomic features here were **not** just volume in disguise —
the median feature shared only about 14% of its variance with volume, and
radiomics kept its accuracy after volume was mathematically removed. The signal
is real; it is simply not *additional*.

**You can say** — and this is the sharpest finding — that early volume change
**with no model fitted at all** retained most of the fitted model's internal
accuracy and **beat it** at the external hospital.

**You cannot say** radiomics has been shown not to work. The claim is bounded
three ways by the authors themselves: one cancer, one imaging modality, and one
**size-based lesion-level endpoint**. Associations with survival, with
progression-free survival, or with patient-level best response are different
questions this study did not test.

**You cannot say** the external cohort confirmed anything. Twelve progression
events gave an AUC interval of 0.50 to 0.85 — a coin flip is inside it. The
authors explicitly decline to claim equivalence there, and a citation that
reports the matching 0.68s as confirmation misrepresents the paper.

**You cannot say** this rules out deep learning on the same images. The authors
say the opposite — their closing line calls for exactly that study. What was
tested is handcrafted texture features, not learned representations.

**You cannot separate** the external drop in performance from the fact that the
external centre used different scanners **and** different drug regimens. The
paper states that these cannot be disentangled.

**You cannot treat** the internal AUC of 0.84 as "we can predict who benefits
from immunotherapy." It predicts whether one lesion's diameter will have grown by
the next scan, using how much it changed by the last one — which is partly a
measure of how consistent tumour growth is across consecutive scans.

**You should note** that the open-access rendering of this paper stripped all
table and figure references, so the sensitivity, specificity, calibration and
subgroup numbers are not readable from the article body alone.

# Bottom Line for Your Life

If you or someone close to you has metastatic melanoma on immunotherapy, the
useful thing here is not the radiomics question. It is three facts sitting in
the background of this paper.

**First, the treatment genuinely works for many people.** The paper's opening
line, citing the trial literature: combination checkpoint immunotherapy now
achieves median overall survival beyond five years, with durable responses in
roughly half of treated patients. That is a transformation, and it is the reason
anyone cares about predicting response at all.

**Second, your lesions may not behave the same way as each other.** This is why
the study was done lesion by lesion: "lesions of the same patient frequently
respond differently under checkpoint inhibition." The authors found within-patient
response concordance was **low**. So a scan report saying one spot has grown
while others shrank is a known pattern with a name — **oligoprogression** — and
it does not automatically mean the treatment has failed. It is a specific
situation with specific options, sometimes including treating the one growing
spot directly while continuing the drug. Worth asking about by name.

**Third, and most practically: a scan that shows growth at one visit is not the
end of the story.** Immunotherapy produces **pseudoprogression** — tumours that
look bigger because immune cells have flooded into them, then shrink. This is
exactly why the response rules used for immunotherapy (iRECIST) require
confirmation rather than acting on a single measurement. If you are told a scan
looks worse, the right question is "are we confirming this before changing
treatment?"

And one thing **not** to take from this paper, if you are ever offered an
AI-imaging-biomarker test: the fact that a radiomic signature was published with
good numbers from one hospital is not evidence it works at yours. This study is
what it looks like when somebody checks — one centre's 0.86 became an
uninterpretable 0.68 the moment the scanner changed. Ask whether the test has
been validated at a different site, on different machines, without being
refitted. That is the question, and it is the one this field has mostly not
answered yet.

**This is education about how to read a study, not medical advice. Decisions
about cancer treatment belong with you and your oncology team.**

---

*Decoded 2026-10-05. Source: PubMed and PubMed Central, accessed 2026-10-05.
Full text read from PMC13632448. The PMC rendering stripped all table and figure
cross-references and did not serve the tables, figures or supplement; values
living only there are marked as not available in the text retrieved —
specifically the Youden-threshold sensitivity and specificity, Brier scores,
calibration intercepts and slopes, precision-recall AUCs, the numeric paired AUC
differences, and all organ-specific and lesion-size subgroup estimates. Derived
figures — the 17.1% patient and 23.7% lesion attrition into the primary
analysis, the 10.3 lesions per patient, the 72 × 4 = 288 feature accounting, the
shared-variance conversions of the reported correlations, the 3.5× ratio of
external to internal confidence-interval width, the Hanley-McNeil event counts
(≈0.18 half-width at 12 events, ≈200 events needed to reach the ±0.05 margin),
the design-effect table, and the RQS as 50% — were computed from the paper's own
reported numbers and are labelled as derived wherever they appear. Funding and
competing interests were not stated in the text retrieved.*

**Verified source links**
- DOI: https://doi.org/10.1186/s40644-026-01135-4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42823717/
- Full text used: https://pmc.ncbi.nlm.nih.gov/articles/PMC13632448/
