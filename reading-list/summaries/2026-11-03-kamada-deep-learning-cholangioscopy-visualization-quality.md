# Feasibility of a Deep-Learning Model for Objective Visualization-Quality Assessment During Cholangioscopy-Guided Lithotripsy: A Proof-of-Concept Study

**Authors:** Kamada H, Kobayashi K, Yamana H, Fujita N, Namima D, Yamada M, Fujita S, Suto H, Okano K, Kobara H (ten authors — Department of Gastroenterology and Neurology, and Department of Gastroenterological Surgery, Faculty of Medicine, Kagawa University, Japan)
**Journal:** DEN Open, 2026; 7(1): e70454 (published 18 October 2026)
**Decoded:** 2026-11-03
**Analysis basis:** **FULL TEXT** (retrieved from PubMed Central, PMC13678035). The complete body was read, including Tables 1–3 in full, all nine numbered limitations, the ethics and consent statements and the funding and conflicts declarations. **The supporting information is not retrievable** — it holds the 5-point scale's reference images, the per-case time-course plots, the patient-flow figure, the device settings, the image pre-processing and augmentation details, the validation-frame selection procedure and the full verification-bias correction. Everything quoted below is from the main text.

**Source links (verified):**
- DOI: https://doi.org/10.1002/deo2.70454
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42898633/
- Full text (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC13678035/

**Basis of link verification.** Direct URL fetching is blocked from this session (`doi.org` does not resolve under the network policy here). Verification was done against the live PubMed/NLM record: a query for PMID 42898633 returned this exact title, these ten authors, DEN Open volume 7 issue 1 article e70454, DOI `10.1002/deo2.70454` and PMC ID `PMC13678035`; the full text was then retrieved from PubMed Central by that PMC ID and matches. Both halves of the chain were confirmed independently.

**Funding: "The authors have nothing to report."** **Conflicts of interest: "The authors declare no conflicts of interest."** **Reporting: "Reporting follows applicable CLAIM and TRIPOD+AI items; unmet items are listed in the Limitations"** — and they are: sample-size justification, calibration, and a large independent development cohort.

**Ethics:** approved by the institutional review board (No. 2025–238), conducted per the Declaration of Helsinki. Written or opt-out consent obtained, **including explanation of the off-label use of the gel in the bile duct** — a disclosure most papers would leave out.

> **Why this paper today.** All four deferred papers were re-checked and remain blocked; the JAMA OpenEvidence study (PMID 42879271, PMC13673371) reached **day 19** of serving an empty PMC body. This was the last spare on the shelf, flagged a week ago as "tiny but remarkable." It is tiny: **twelve patients in the comparison, three in the development set.** It is also, after sixty-five papers, **the most honestly reported study in this reading list** — by a clear margin, and not because its result is good. Its result is largely negative, and the authors did more work to establish that than most papers do to establish a positive one. It is the first paper here to identify its own verification bias, name the correction, apply it, and publish both the flattering and the corrected numbers side by side.

---

## 1. The Gist

Some gallstones get stuck in the bile duct and will not come out. One way to deal with them is to thread a tiny camera up into the duct and shatter the stone with electrical shockwaves. The problem is immediate: the shattering fills the duct with dust, sludge and bubbles, and the camera goes blind. Endoscopists call it the **snowstorm effect**. You then have to stop and flush with saline — which takes time, and pushing fluid into a bile duct raises the pressure and can cause infection. Or you keep going half-blind, and risk tearing the duct wall.

Someone had an idea: instead of watery saline, fill the duct with a **clear thick gel**, which should resist being churned up.

Testing that needs a way to measure "how clearly can you see," and until now that has meant a doctor eyeballing it and giving a score out of five. So ten researchers at Kagawa University in Japan tried to build software to do the scoring objectively — and then used it to compare gel against saline.

Here is what makes this paper worth a full day despite its size.

**The model does not work very well, and they proved it on themselves.** Two expert endoscopists, blinded, scored the same frames and agreed with each other almost perfectly — **weighted kappa 0.98**. The model agreed with them only **moderately, 0.60**. And when the authors corrected for a sampling quirk in their own validation, the model's **sensitivity fell from 60.7% to 29.8%** — it misses roughly seven out of ten clear views.

**They found that quirk themselves and fixed it.** Nobody made them. Their validation frames had been picked by cycling through the model's own predictions, which over-represented frames the model thought were usable. That is called **verification bias**, it flatters a test, and the authors spotted it, named the standard correction, applied it, and printed both sets of numbers.

**And their headline comparison came out non-significant — which they say, in the abstract.** Gel looked better than saline on the main measure (22.7% of frames clear versus 8.4%), but with five patients against seven that difference gave **p = 0.15**. A different measure, computed afterwards, did reach p = 0.005 — and they label it post hoc every single time they mention it.

So: a small study, a model that is not good enough yet, a comparison that does not prove its point. And the authors say all three things themselves, repeatedly, before anyone else can.

## 2. Study Snapshot

**Study type:** a **single-centre retrospective pilot**, described by its own title as a proof-of-concept and feasibility study. Two things are being done at once: building a measuring instrument, and using that instrument for an exploratory comparison.

**Where and when:** Kagawa University, records and video archives of peroral cholangioscopy-guided electrohydraulic lithotripsy for difficult bile duct stones, November 2021 to June 2025.

**Patients: 15 in total.**
- **3 development cases** — used only for model training and a convergence check. These were "the first three consecutive procedures in which both viscous gel and saline were used within the same procedure, **selected before the comparison cohort was assembled and solely on this mixed-medium criterion**."
- **12 comparison cases** — the test set, with **no overlap**. Viscous gel **n = 5**, saline **n = 7**, each irrigated with one medium throughout.

**Equipment:** the same cholangioscope (SpyGlass DS II) and lithotripsy system (Autolith Touch) throughout, with the generator and probe models named. The gel is a dedicated endoscopic product (VISCOCLEAR), injected manually through the accessory channel.

**Disclosed honestly and unprompted:** "Owing to the retrospective design, generator settings, irrigation flow/pressure, and injected gel volume were not recorded, and injection and irrigation were not protocolized across operators."

**The scoring scale:** 5 points — 0 Unusable, 1 Poor, 2 Fair, 3 Good, 4 Excellent.

**How the labels were made, and the distinction the paper draws:** one board-certified expert (Reader A) assigned **all** training labels. Two additional endoscopists blindly scored a **disjoint** subset to assess the scale, giving weighted kappa 0.60–0.79 — and the paper states that this "**validates the scale rather than the training labels**." The kappa subset, the hold-out set and the accuracy-evaluation set were **mutually disjoint**.

**The model:** ResNet-18 initialised from ImageNet weights (torchvision IMAGENET1K_V1), 5-unit classifier, cross-entropy loss, Adam optimiser, batch size 8, 20 epochs, best-validation checkpoint. **Class imbalance is printed exactly** — Score 0/1/2/3/4 = **45/964/465/202/56 frames** (1,732 total; the commonest class is 55.7% of the data and the rarest 2.6%, a ratio of 21 to 1) — and handled with an inverse-frequency weighted random sampler, "**not augmentation**."

**The convergence check the paper disowns.** On a 100-frame hold-out drawn from the same development cases: accuracy **99.0%**, sensitivity 100% (16/16), specificity 98.8% (83/84) — against a best training-validation accuracy of **79.5%**. The paper's own verdict: "the higher hold-out figures arise because those frames overlap the training videos and do not establish generalizability."

**The independent validation:** 120 frames (10 per case) from the 12 unseen comparison cases, scored by **two board-certified endoscopists blinded to group, medium and model output**, with their per-frame consensus as the reference.

**The flaw they caught in their own design:** frames were "drawn at random while cycling through the model's predicted classes so that each class was represented, which **enriched the sample for predicted-usable frames (39% versus 13.8% of all 1950 analyzed frames)**." Because selection depended on model output, the raw metrics are subject to **verification bias** — stated in those words, with the correction named (**Begg–Greenes-type**), applied, and bootstrap confidence intervals attached.

**Results, raw (enriched sample):** accuracy **70.8%** (Wilson 62.2–78.2), sensitivity **60.7%** (34/56; 47.6–72.4), specificity **79.7%** (51/64; 68.3–87.7).

**Results, corrected to the natural frame distribution:** accuracy **73.6%** (bootstrap 63.2–83.0), sensitivity **29.8%** (21.2–43.2), specificity **93.5%** (90.4–96.3), with estimated true-usable prevalence **31.3%** against **13.8%** predicted. The paper's own reading: "under real-world conditions the model is specific but markedly under-sensitive, so HQVR underestimates usable time in both groups."

**Agreement, all four numbers:** reader vs reader 5-class weighted kappa **0.98**; model vs consensus 5-class weighted **0.60**. Binary (Usable 3–4 vs Unusable 0–2): reader vs reader **0.95**; model vs consensus **0.41**.

**By medium:** gel frames (n = 50) kappa 0.45, accuracy 72.0%; saline frames (n = 70) kappa 0.69, accuracy 70.0%; overlapping intervals. Mean signed error −0.40 for gel and −0.19 for saline, **permutation p = 0.34** — no significant medium-specific bias, and, as the paper notes, "if anything the model scored gel more conservatively, which **biases against** the observed gel advantage."

**The comparison.** From each case's lithotripsy clip, 150–220 frames were sampled at equal intervals (1,950 in total) — the sampling interval was lengthened from 0.2 s to 1.1–10.9 s **specifically "to reduce temporal autocorrelation."** The primary measure, High-Quality View Rate (HQVR), is the proportion of frames the model scores Good or Excellent.

- **HQVR: gel median 22.7% (IQR 19.3–24.0) vs saline 8.4% (6.7–10.1). Exact Mann–Whitney U = 27, p = 0.15 — not significant.**
- **Post hoc** mean predicted quality score: gel 1.65 (1.61–1.66) vs saline 1.35 (1.23–1.37), U = 34, **p = 0.005**.
- **Post hoc** longest continuous usable interval: gel 24.4 s (20.6–26.8) vs saline 5.2 s (4.4–14.4).

**Baseline, and the sentence most papers never write:** "No formal statistical testing was performed for baseline characteristics owing to the small sample and varying stone burden; **non-significance must not be read as group comparability**." Gel had larger stones (16.2 vs 13.3 mm) and longer procedures (median 928 vs 455 s) — which the paper identifies as "a confounder that **biases against, rather than toward**, the efficiency rationale for gel." Mild cholangitis occurred in 4/7 saline and 1/5 gel patients; all resolved, no severe adverse events.

## 3. How Strong Is This Evidence? (Grade 3/5)

**The grade is capped by arithmetic, not by candour. On reporting alone this would be the highest-graded paper in this list.**

Twelve patients cannot produce strong evidence about anything. Five versus seven cannot establish that a gel works. A model trained on three cases cannot be a validated instrument. Those are facts about sample size and no amount of careful writing changes them.

But the grade in these summaries asks how much a reader should update their beliefs, and that depends on what is being claimed. **This paper claims: it is feasible to train such a model; the model is not yet good enough; and the gel signal is hypothesis-generating only.** All three claims are established — the third by a non-significant primary test the authors report as non-significant. **The evidence and the claim are the same size, and the paper spent most of its effort proving its own negative.**

**What it does that nothing else in sixty-five papers has done:**

**It identified its own verification bias, named the correction, applied it, and published both sets of numbers.** The raw sensitivity of 60.7% is the number a less careful paper would have printed alone. The corrected 29.8% is the number that is true. Both are in the abstract. Section 5 works the correction through.

**It disowned its own 99% hold-out accuracy.** "Those frames overlap the training videos and do not establish generalizability." A 99% figure sitting unused in a results section, explicitly labelled as not meaning anything, is a thing this list has never seen.

**It refused to run baseline significance tests and explained why.** "Non-significance must not be read as group comparability." That is methodologically correct — baseline p-values conflate chance imbalance with real imbalance and are actively misleading in a non-randomised comparison — and almost nobody declines to produce them.

**It worked out which direction each of its confounders pushes.** The gel group had harder cases, which **biases against** gel. The model scored gel more conservatively, which also **biases against** gel. The saline cases were earlier, allowing a learning curve, which biases **toward** gel. All three are stated.

**It labelled its primary comparison non-significant and its significant result post hoc — in the abstract.** Both p-values appear with their labels attached.

**It listed the reporting-guideline items it fails.** "Several CLAIM/TRIPOD+AI items (sample-size justification, calibration, a large independent development cohort) remain unmet."

**It distinguished validating the scale from validating the labels.** The 0.60–0.79 kappa among extra readers "validates the scale rather than the training labels" — a distinction that matters because all training labels came from one person, which the paper also lists as a limitation.

**It printed the exact class-imbalance counts and said how imbalance was handled**, including that augmentation was *not* used.

**It changed its own sampling scheme to reduce temporal autocorrelation**, said so, and kept all comparisons at the patient level because frames within a video are not independent.

**It measured human-versus-human agreement first**, establishing that the task has a high ceiling (0.98) before showing the model falls well short of it.

**Why it is not a 4:**

**Twelve patients, five versus seven.** The primary comparison could not have reached significance without near-perfect separation — Section 5 shows the smallest achievable two-sided p here is **0.0025**. That is a design fact, knowable before the study ran, and it is the one thing a sample-size justification would have surfaced. The paper lists its absence as an unmet CLAIM item.

**Three development cases, one labelling expert.** The model's whole notion of "Good" comes from one person's judgement on three procedures. The paper lists both.

**The instrument and the comparison are entangled.** The gel-versus-saline result is measured with an instrument the same paper shows to be 30% sensitive. The authors address this directly — the instrument was applied equally to both groups, and the per-medium check found no significant differential bias (permutation p = 0.34) — which is the right defence, but it rests on 50 gel and 70 saline frames.

**Unmeasured procedural variables.** Generator settings, irrigation pressure and gel volume were not recorded. Disclosed, and still missing.

**No link to any clinical outcome.** HQVR has no validated threshold and is not tied to procedure time, irrigation volume, or complications. The paper says so: "our data do not show that higher HQVR translates into greater efficiency, less irrigation, or fewer adverse events."

**What would make it a 4:** a prospective study with a prespecified sample size, a development set of tens of cases labelled by more than one reader, and HQVR tied to something that happens to a patient.

## 4. The Editor's Concerns

Most of this section's usual contents are, unusually, in the paper already. What follows is what remains.

**The cholangitis numbers invite a conclusion the design cannot support.** Mild cholangitis occurred in **4 of 7 saline patients (57.1%) and 1 of 5 gel patients (20.0%)**. That looks like a safety signal in gel's favour and will be read as one. It rests on five events in twelve patients, no test was run (correctly), and the mechanism would have to run through reduced irrigation volume — which was not recorded. The paper reports the counts in Table 1 and the results text and makes no claim about them, which is the right handling; a reader skimming will still take the impression.

**The gel is used off-label in the bile duct.** Stated in the consent section, and worth carrying forward: the comparison is not between two approved options but between the standard and an off-label application of a product developed for a different purpose. The paper's disclosure of this in the consent process is to its credit and is the kind of detail that usually disappears.

**The per-class results show the model is weakest exactly where the scale matters most.** Table 2's per-class precision and recall: Score 0 (0.59/0.56), Score 1 (0.25/0.47), Score 2 (0.29/0.24), Score 3 (0.36/0.39), Score 4 (0.43/0.24). **Every single class sits below 0.60 precision**, and the middle of the scale — Fair and Good, the frames where a human most needs help deciding whether to keep going — is the worst. The binary collapse to Usable/Unusable hides this; the paper prints the full table anyway.

**Weighted kappa 0.60 and binary kappa 0.41 are the same model on the same data.** Collapsing the ordered 5-point scale to a binary removes the partial credit that weighted kappa gives for near-misses, and the number falls by 0.19. Both are reported, which is the right answer to the problem flagged two days ago — that "weighted kappa" without its weighting scheme is not a reported statistic. Here you can see exactly what the weighting was worth.

**The two post hoc measures are not independent of each other or of the primary.** HQVR, the mean predicted score and the longest usable interval are three summaries of the same 1,950 model outputs. When the primary threshold-based measure missed significance and a threshold-independent version of the same quantity reached it, the natural question is how many summaries were tried. The paper names two post hoc measures and labels them, which bounds the problem; it does not say whether others were computed and discarded.

**A note in the paper's favour that is easy to miss.** The three development cases were chosen as "the first three consecutive procedures" meeting a **single prespecified criterion** (both media used), "selected before the comparison cohort was assembled." That is a prespecified, non-cherry-picked development set, described precisely enough to check — in a paper that could easily have written "three representative cases."

**Where I am uncertain, stated plainly.** The supporting information was not retrievable, which here means I cannot see the 5-point scale's reference images, the per-case time courses, the patient-flow figure, the device settings, the pre-processing and augmentation detail, the exact validation-frame selection procedure, or the full verification-bias correction with its per-medium statistics. My own re-derivation of the correction in Section 5 is a **binary** version and gives a slightly different answer from the paper's (36.0% versus 31.3% estimated prevalence; sensitivity 27.8% versus 29.8%), consistent with the authors having re-weighted across all five predicted classes rather than the binary collapse — so the method reproduces, the arithmetic differs in the expected direction, and **the paper's numbers are the ones to use.**

## 5. Statistics Spotlight

Three things. The first has never appeared in this list and is one of the most important biases in diagnostic research.

### Verification bias: when the test decides who gets checked

Suppose you want to know how good a test is. You need the truth for each case — the **reference standard** — and getting it costs something. So you check some cases and not others. **If which cases you check depends on what the test said, every accuracy figure you compute is biased.** This is called verification bias, or work-up bias, and it is everywhere in diagnostic research.

Here is the mechanism in this paper, which is unusually clean. The authors needed expert labels for validation frames, and expert time is scarce, so they could only label 120 of 1,950 frames. To make sure every score band was represented they sampled "while cycling through the model's predicted classes." The consequence, which they state: predicted-usable frames made up **39% of the validation sample** but only **13.8% of all 1,950 frames** — an enrichment of about **2.8 times**.

Why does that flatter the model? Reconstruct the 2×2 from the reported numbers. Sensitivity 60.7% = **34/56**; specificity 79.7% = **51/64**; so:

> **TP = 34 · FN = 22 · FP = 13 · TN = 51** (total 120, accuracy 85/120 = 70.8% ✓)

Predicted-usable frames are TP + FP = **47**, which is 39.2% of the sample — matching the paper's 39%. Over-sampling predicted-usable frames means over-filling the **TP** cell relative to **FN**, which inflates sensitivity, and over-filling **FP** relative to **TN**, which deflates specificity.

**The fix rests on one insight the paper states precisely: "per-predicted-class positive predictive values are unbiased."** Within each predicted class the sampling *was* random, so the proportion of truly-usable frames inside that class is an honest estimate. You then re-weight those classes back to how often they actually occur.

Worked through in the simple binary form:

> among predicted-**usable** frames, truly usable = 34/47 = **0.723**
> among predicted-**unusable** frames, truly usable = 22/73 = **0.301**
> natural mix: 13.8% predicted-usable, 86.2% predicted-unusable
> estimated true prevalence = 0.138 × 0.723 + 0.862 × 0.301 = **0.360**

and from there, corrected sensitivity ≈ 27.8% and specificity ≈ 94.0%. The paper, re-weighting across all five predicted classes rather than collapsing to two, gets **29.8%** and **93.5%** with an estimated prevalence of **31.3%**. Same method, same direction, same magnitude.

**What the correction reveals:**

> sensitivity **60.7% → 29.8%** (roughly halved)
> specificity **79.7% → 93.5%** (rose)

The model predicts "usable" 13.8% of the time; the truth is about 31.3%. It is **specific but markedly under-sensitive** — it rarely cries wolf, and it misses most of the clear views that exist. Which has a direct consequence the authors spell out: **HQVR underestimates usable time in both groups**, so the gel-versus-saline gap is measured with a ruler that is too short for everyone.

**The everyday version.** A school nurse screens children for a condition and sends only the ones who look ill for a blood test. Among those sent, the screen looks excellent — most really are ill. But the children who looked fine were never tested, so the screen's misses were never counted. **Sensitivity measured only among the people you chose to check is not sensitivity.**

**The watch-out:** verification bias is usually invisible, because papers describe their sampling in a methods sentence and report the metrics as though the sample were random. **Ask one question of every diagnostic study: how were the cases chosen that got the reference standard, and could the test's own output have influenced that choice?** If yes, the raw sensitivity is too high and the raw specificity too low. The corrections have names — Begg and Greenes published theirs in 1983 — and the fact that this paper applies one is the single most unusual thing about it.

### Reporting the human ceiling before measuring the machine against it

Four agreement numbers appear in this paper, and the way they are arranged is the model for how to do this:

> reader vs reader, 5-class weighted kappa: **0.98**
> model vs consensus, 5-class weighted kappa: **0.60**
> reader vs reader, binary Cohen's kappa: **0.95**
> model vs consensus, binary Cohen's kappa: **0.41**

Kappa, as this list covered last week, is agreement after subtracting what chance would produce: (observed − chance) / (1 − chance).

**The first number is the one most papers skip, and it does the most work.** Before you can say a model is bad at a task, you have to know the task is doable. A model scoring 0.60 against humans could mean the model is weak, *or* it could mean the task is inherently subjective and the humans do not agree either. **Here the two blinded experts agreed at 0.98** — near-perfect. So the target is real and well-defined, the ceiling is high, and the model's 0.60 is squarely the model's problem. Without the human-human number you could not tell those two situations apart.

Note also what happens when the scale collapses. The **same model on the same frames** scores **0.60 weighted** and **0.41 binary**. Weighted kappa on an ordered scale gives partial credit for being one step off; the binary version throws that away. Two days ago this list flagged a paper for reporting "weighted kappa 0.96" without naming its weighting scheme. This paper reports both versions, so you can see exactly what the weighting was worth: **0.19 of kappa.**

**The watch-out:** a model's agreement score is meaningless without a human benchmark on the same data, and benchmarks from other studies will not do — kappa depends on the case mix, so it is not comparable across settings. **Demand the human-human number from the same frames, scored blind.** If a paper gives you only the model's kappa, you cannot tell a weak model from an impossible task.

### With tiny samples, work out which p-values are even reachable

The primary comparison was gel (5 patients) against saline (7), by exact Mann–Whitney U test. Before looking at the result, ask what results were *possible*.

A Mann–Whitney test on 5 versus 7 works by counting arrangements. There are

> C(12,5) = **792**

ways to choose which five of the twelve patients belong to the gel group. If the gel group's five values were all higher than every saline value — **perfect separation** — exactly one of those 792 arrangements is that extreme, so the one-sided p is 1/792 = 0.00126 and the two-sided p is:

> **0.0025**

**That is the floor.** With five against seven, no result however dramatic can produce a p below 0.0025, and reaching anywhere near it requires near-perfect separation of twelve numbers.

Now the reported results:

- **HQVR (primary): U = 27, p = 0.15.** Exact calculation gives 0.1490 — matches.
- **Mean predicted score (post hoc): U = 34, p = 0.005.** Exact calculation gives 0.0051 — matches.

And U = 34 is one step from U = 35, the perfect-separation maximum. So **p = 0.005 here means: all but one of the five gel values exceeded all seven saline values.** It is not a statement about effect size in the usual sense; it is a statement that twelve numbers lined up almost perfectly. The reported interquartile ranges agree — they do not overlap for any of the three measures.

That cuts both ways, and both ways are worth holding. **It is a strong ordering**, far more striking than a p-value near 0.05 would be. **And it rests on twelve observations**, so one differently-behaving patient moves it substantially — which is exactly why the authors call it hypothesis-generating.

**The watch-out, and it is a design lesson rather than a reading one:** with groups this small, compute the minimum achievable p **before** running the study. Here it was knowable in advance that the primary analysis would need near-perfect separation to reach significance — so a non-significant HQVR was always the likely outcome, whatever the gel does. **A non-significant result from a study that could barely have produced a significant one is not evidence of no effect.** The paper reaches the same conclusion by a different route, calling the comparison exploratory throughout.

## 6. Jargon Translator

**Peroral cholangioscopy (POCS)** — passing a very thin camera down through the mouth and into the bile duct to look directly inside it.

**Bile duct** — the tube carrying bile from the liver and gallbladder to the intestine. Stones can lodge in it.

**Electrohydraulic lithotripsy (EHL)** — breaking a stone apart with electrical shockwaves delivered through a probe. Effective, and it makes a mess of the view.

**Snowstorm effect** — the instant whiteout as stone dust, sludge and bubbles fill the field. Borrowed from laser lithotripsy in urology.

**Viscous gel immersion** — filling the duct with a clear thick gel instead of saline, so debris does not swirl. Here an off-label use of a gel developed for gastrointestinal bleeding.

**Cholangitis** — infection of the bile duct. One reason to avoid vigorous irrigation, which raises pressure inside the duct.

**ResNet-18** — a small, standard image-classification neural network. "18" is its number of layers.

**ImageNet-pretrained** — started from weights learned on a large collection of everyday photographs, then adapted. Standard when medical training data are scarce, as here.

**Class imbalance** — some score categories being far commoner than others. Here Score 1 had 964 training frames and Score 0 only 45, a 21-to-1 ratio.

**Inverse-frequency weighted sampler** — showing the model rare categories more often during training so it does not simply learn to predict the common one.

**Hold-out set** — data kept back from training to test on. **Only useful if it is genuinely separate** — here it came from the same three videos, which the authors say makes it worthless for judging generalisation.

**Reference standard** — the answer treated as correct. Here, two blinded experts' consensus.

**Verification bias (work-up bias)** — the distortion that arises when which cases get the reference standard depends on the test result. See Section 5.

**Begg–Greenes correction** — the standard method for undoing verification bias by re-weighting predicted classes back to their natural frequencies.

**Cohen's kappa / weighted kappa** — agreement between two raters after subtracting chance agreement. The weighted version, for ordered categories, gives partial credit for near-misses.

**Sensitivity / specificity** — of the frames that truly were usable, the share the model caught; of the frames that truly were not, the share it correctly rejected.

**Wilson confidence interval** — a method for a proportion's interval that behaves well near 0 and 1, unlike the symmetric Wald interval this list criticised last week.

**Bootstrap confidence interval** — resampling the data many times and reading the interval off the spread. Used here for the corrected metrics, where no simple formula applies.

**HQVR (High-Quality View Rate)** — the paper's primary measure: the share of sampled frames the model scores Good or Excellent. **No validated clinical threshold exists for it.**

**MPQS (mean predicted quality score)** — a threshold-free alternative: the probability-weighted average predicted score, 0 to 4. Computed **post hoc**.

**Exact Mann–Whitney U test** — a rank test that counts arrangements rather than assuming a distribution. The right choice for tiny samples, and its floor on achievable p-values is a design constraint. See Section 5.

**Temporal autocorrelation** — consecutive video frames look almost identical, so treating them as independent observations inflates your effective sample size. The authors lengthened their sampling interval to reduce it and analysed at the patient level.

**Post hoc** — decided after seeing the data. A p-value from a post hoc analysis does not carry the same weight as one from a prespecified analysis.

**CLAIM / TRIPOD+AI** — reporting checklists for medical AI and for prediction models. This paper names both and lists the items it fails.

## 7. What You Can (and Can't) Say

**Fair to say:**

- ✅ "Two blinded expert endoscopists scoring the same frames agreed almost perfectly (weighted kappa 0.98), while the model agreed with them only moderately (0.60)." Reported.
- ✅ "After correcting for how the validation frames were chosen, the model's sensitivity was 29.8% and its specificity 93.5%." Reported, and the correction is the authors' own.
- ✅ "The authors say their model is not yet a validated measurement tool." Their words, in the abstract and the conclusion.
- ✅ "On the primary measure, gel was not significantly better than saline (22.7% vs 8.4%, p = 0.15)." Reported, including in the abstract.
- ✅ "A post hoc measure did favour gel (1.65 vs 1.35, p = 0.005), and the authors label it exploratory." Also in the abstract.
- ✅ "The gel group had larger stones and longer procedures — harder cases — which works against the gel hypothesis rather than for it." The paper's own analysis.
- ✅ "A 99% accuracy figure from a hold-out drawn from the training videos tells you nothing, and the authors say so about their own." Stated.
- ✅ "The gel was used off-label in the bile duct, and patients were told so." In the consent statement.

**Not fair to say:**

- ❌ "Gel immersion gives a clearer view than saline during lithotripsy." The primary comparison was **not significant** (p = 0.15); the significant result was post hoc; the groups differed at baseline; and the measuring instrument misses about 70% of clear views.
- ❌ "An AI can now objectively measure visualization quality." It agrees with experts moderately (kappa 0.60), every per-class precision is below 0.60, and the authors call it "an early feasibility demonstration rather than a validated measurement tool."
- ❌ "The model is 70.8% accurate." That figure comes from a sample enriched for frames the model called usable. Corrected to the real frame mix, sensitivity is **29.8%**.
- ❌ "Gel reduced cholangitis." Four of 7 saline versus 1 of 5 gel patients, no test performed, and the mechanism would run through irrigation volume, which was **not recorded**.
- ❌ "The groups were comparable at baseline." The paper explicitly refuses this inference: "non-significance must not be read as group comparability" — and no tests were run.
- ❌ "p = 0.005 is strong evidence here." With 5 versus 7, the smallest possible two-sided p is **0.0025**, and p = 0.005 corresponds to all but one gel value exceeding every saline value. It is a near-perfect ordering of twelve numbers, not a large-sample result.
- ❌ "A higher High-Quality View Rate means safer or faster procedures." HQVR has no validated threshold and is not linked to any outcome. The authors state this directly.
- ❌ "The model works equally well for both media, so the comparison is fair." Agreement differed numerically (kappa 0.45 gel vs 0.69 saline) with overlapping intervals and a permutation p of 0.34 on 50 and 70 frames — the authors' defence is reasonable and it is not the same as demonstrated equivalence.

## 8. Bottom Line for Your Life

If you are facing a procedure for a difficult bile duct stone, nothing here changes your care. The gel is an off-label experiment in twelve patients. What the paper does illustrate, usefully, is a real constraint your endoscopist works under: once the shockwaves start, **the camera goes blind within seconds** — the saline group's view collapsed almost immediately, with a median longest-clear-stretch of about **five seconds**. That is the reason these procedures sometimes take two attempts, and why "we could not see well enough to continue safely" is a reasonable thing for a doctor to say.

For anyone appraising research, this paper is the best teaching case in the list so far, and the reason has nothing to do with its findings.

**The technique: ask how the cases that got the reference standard were chosen.** If the test's own output influenced that choice — screening positives sent for biopsy, flagged records sent for review, frames sampled by predicted class — then the reported sensitivity is too high and the specificity too low. Here that single design detail, which the authors caught themselves, took sensitivity from **60.7% down to 29.8%**. **Verification bias is invisible unless you look for it, and the only place to look is the sampling sentence in the Methods.**

**And the habit: demand the human-versus-human number before you believe the human-versus-machine one.** A model agreeing with experts at kappa 0.60 could be a weak model or an impossible task. Only the readers' 0.98 against each other tells you which — and it tells you unambiguously.

**Last, the thing worth taking from this paper as a reader of papers generally.** It is the smallest study in this collection and the most honestly reported, and those two facts are connected. **The authors let the design dictate the claim instead of the other way round.** They had a non-significant primary result and said so in the abstract. They had a 99% accuracy figure and explained why it was meaningless. They found a flaw in their own validation and published the corrected, worse numbers next to the flattering ones. They worked out that two of their confounders argued against their own hypothesis and wrote it down.

Sixty-five papers in, the pattern is clear enough to state: **the papers that tell you the most are rarely the ones with the best results.** They are the ones whose authors went looking for reasons to doubt themselves first.

---

## Appendix — deferred-paper status, 2026-11-03

- **Google, "The anatomy of a personal health agent"** (Nature, PMID 42907512): no PubMed Central copy. Unchanged.
- **BMJ, LLM-trial reporting completeness review** (PMID 42869550): no PMC copy; Scite paywalled. Unchanged.
- **Annals of Internal Medicine, Choosing Wisely benchmark** (PMID 42896192): no PMC copy. Unchanged. Standing note: the overuse rate of 5.4% with a 95% CI of 0.6–12.2% is a clustering signature — that interval is almost certainly computed across the 15 recommendations rather than the 4,050 responses.
- **JAMA, "Clinician Use of an AI-Enabled Clinical Information Platform"** (PMID 42879271, PMC13673371): PMC record exists and serves an **empty body for the nineteenth consecutive day.** Standing instruction unchanged — **if still empty on 2026-11-05 (day 21), decode abstract-only and say so explicitly.**

---

*This is an educational analysis of a published scientific paper, not medical advice. Nothing here is guidance about gallstones, bile duct procedures or your own care. If you are facing treatment for bile duct stones, discuss it with your gastroenterologist.*
