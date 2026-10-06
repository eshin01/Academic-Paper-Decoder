# The Protocol That Did the Sum the Last One Skipped

**Paper:** Development and validation of an AI-enhanced prediction model for
3-year visual decline in patients with diabetes using ophthalmic imaging:
protocol for a real-world longitudinal cohort study
**Authors:** Yu Y, Yang J, Zhang Y, Ma S, Hong J, Nan S, Sun F
**Venue / Year:** BMJ Open, 2026;16(9):e123521 (published 2026-09-30)
**DOI:** https://doi.org/10.1136/bmjopen-2026-123521
**PubMed:** https://pubmed.ncbi.nlm.nih.gov/42816089/
**Full text used:** https://pmc.ncbi.nlm.nih.gov/articles/PMC13630008/
**Registration:** **None stated.** No trial or study registry identifier appears
anywhere in the retrieved text — see the concerns section, because the paper
decoded two days ago registered voluntarily and this one does not mention it.
**Basis of this analysis:** FULL TEXT (PubMed Central open-access copy,
retrieved 2026-10-06). The PMC rendering **stripped every supplement and figure
cross-reference**, leaving dozens of sentences ending "will be prespecified
in." and "are specified in." with no target. Figure 1 and both supplemental
files did not render. That matters more here than usual: the protocol defers the
public datasets used for AI training, their label mappings and sample sizes, the
model architectures and all training hyperparameters, the AI score scales and
directions, the full predictor parameterisation table, and the completed
TRIPOD+AI checklist **entirely to those supplements.** Table 1 (the four model
groups) did render and is used below. Everything quoted here comes from the
article body or the abstract.
**Date decoded:** 2026-10-06
**Evidence grade:** 4/5 — **for the plan. A protocol has no results.** As of
September 2026 the authors state that data extraction has begun and that
"data cleaning, AI model development, AI-derived imaging-score generation,
prognostic model development, outcome analyses and external validation have not
yet been completed."

All identifiers above were verified against the live PubMed and PubMed Central
records on 2026-10-06. Nothing here is based on a guessed or reconstructed link.

---

# The Gist

Two days ago this list decoded a protocol for the first time, to learn how to
read a study before it has findings. Today's paper is a second protocol, and it
is here deliberately, because the two make a matched pair: they take the same
job — build a prediction model from routine records — and they are strong and
weak in almost exactly opposite places.

The clinical question is a good one. AI in eye care has been overwhelmingly
about **grading**: look at a retinal photograph, say how bad the diabetic
retinopathy is. That is a question about *now*. What a patient actually wants to
know is about *later*: am I going to lose vision? And the paper's central
observation is that those are not the same question — "patients with similar
baseline disease grades may experience substantially different long-term visual
outcomes."

So this team plans to predict, for each eye, **whether vision will measurably
decline within three years.** They will build a conventional clinical model from
13 things a doctor already knows — age, sex, HbA1c, blood pressure, cholesterol,
kidney function, eye pressure, glaucoma, retinopathy grade, macular oedema,
prior injections, prior laser — and then ask one clean question: **does adding an
AI score read off the retinal images make it better?** Three versions: from
fundus photographs, from OCT scans, and from both fused together.

That is a well-posed question, and the design to answer it is unusually
disciplined. The AI models will be trained on **public** datasets, never on the
study's own patients, and the scores will be generated **before** the prognostic
model is fitted. The final model will be sent to a second hospital and applied
**without refitting a single coefficient.**

And then there is the thing that made me pick this paper. Two days ago, the
other protocol cited a well-known method for working out how big a prediction
study needs to be — Riley and colleagues' framework — and then declined to
apply it, on the grounds that it was using a whole population. This one applies
it, states its three inputs, and reports a required sample of **823 eyes.** I
ran the formula with those inputs. It gives **822.7**. It reproduces to the unit.

That is what a sample-size calculation looks like when it is real rather than
decorative, and it is the single best teaching example this list has had.

Where it falls short is different, and in two places serious. It is **not
registered** anywhere, which the paper from two days ago was, voluntarily. And
its outcome — "vision got worse" — has two large competing causes in diabetic
patients over three years that the protocol barely addresses: **cataract**,
which is extremely common in diabetes and makes vision worse without the
retinopathy changing at all, and **death**, which simply stops the measurements.

# Study Snapshot

- **Study type:** **Protocol** for a retrospective, real-world **longitudinal**
  cohort study developing, internally validating and **externally** validating a
  time-to-event prognostic model. No results yet.
- **Development site:** Peking University Third Hospital. Study period 1 January
  2018 to 1 May 2026.
- **External validation site:** Ningbo Eye Hospital, Wenzhou Medical University —
  independent, with the same prespecified eligibility, predictor and outcome
  definitions.
- **Unit of analysis:** the **eye**. Both eyes of a patient may be included.
  **Splitting and resampling will be done at the patient level** so that one
  person's eyes never straddle a train/test boundary. Within-patient correlation
  handled with cluster-robust standard errors; a one-eye-per-patient sensitivity
  analysis is planned.
- **Who is eligible:** adults with diagnosed diabetes, with baseline colour
  fundus photography and/or OCT, a baseline best-corrected visual acuity
  convertible to logMAR, at least one follow-up acuity within three years, and
  reliably identifiable eye laterality.
- **Who is excluded:** ungradable images, missing baseline or follow-up acuity,
  unmatchable laterality, and major non-diabetic eye disease likely to dominate
  visual prognosis at baseline — advanced glaucoma, retinal vein occlusion,
  age-related macular degeneration, high myopic maculopathy, severe corneal
  opacity, optic neuropathy, trauma.
- **Primary outcome:** **time to first** eye-level visual decline within three
  years, defined as an increase in logMAR acuity of **≥0.2** from baseline in the
  same eye — roughly two lines on an eye chart, a doubling of the visual angle.
  Eyes without decline are censored at their last acuity within three years;
  follow-up is administratively truncated at three years.
- **Key secondary outcomes:** **sustained** decline (≥0.2 logMAR **confirmed at
  the next eligible visit**); severe decline (≥0.3 logMAR); retinopathy
  progression by at least one stage; macular oedema developing or worsening.
  Treatment-requiring oedema is exploratory.
- **The four models (Table 1 of the paper):** Model 1 is the clinical reference —
  13 prespecified predictors, **14 effective parameters** (retinopathy severity
  is three-level and so contributes two). Model 2 adds the fundus AI score,
  Model 3 the OCT score, Model 4 a single fused multimodal score. Each
  AI-enhanced model adds exactly **one** parameter, for a maximum of **15**.
  Model 4 will **not** contain the separate fundus and OCT scores at the same
  time.
- **How the AI scores are made:** deep learning models trained on **publicly
  available** fundus and OCT datasets with retinopathy-related labels, harmonised
  to no-DR / non-proliferative / proliferative where the source labels permit.
  Training, validation and test partitions at the patient level where
  identifiers exist. The scores are continuous, with higher meaning more
  AI-estimated disease burden.
- **The leakage firewall, stated four separate times:** the imaging models "will
  not be trained, selected or tuned using follow-up visual outcome data from the
  target longitudinal prognostic cohort"; "local images from the target
  prognostic cohort will not be used to train, select or tune the AI imaging
  models"; the final models are applied to the cohort "solely for score
  generation"; and the scores "will be generated before prognostic model
  fitting."
- **Primary analysis:** Cox proportional hazards regression with the **full
  prespecified predictor set and no data-driven selection.** Proportional-hazards
  assumption checked with Schoenfeld residuals. Continuous predictors linear in
  the primary model; restricted cubic splines explored for age and baseline
  acuity in secondary analyses.
- **Secondary modelling:** penalised Cox (LASSO), with the penalty chosen by
  cross-validation **separated at the patient level**, and the explicit
  statement that penalisation "will not redefine the prespecified predictor set
  or the parameter budget used for the primary sample-size calculation." Any
  LASSO-reduced set is refitted in a Cox model with cluster-robust standard
  errors.
- **Exploratory:** Random Survival Forest and gradient boosting survival models,
  with interpretation kept to the Cox models.
- **Internal validation:** bootstrap resampling **at the patient level**, with
  optimism-corrected discrimination and calibration.
- **External validation:** the final model applied "without predictor selection,
  coefficient refitting or hyperparameter retuning." Any recalibration to be
  reported separately as a secondary analysis.
- **Performance measures:** Harrell's C-index and time-dependent AUC at 1, 2 and
  3 years; Uno's C-index in sensitivity analyses if censoring is substantial;
  time-dependent Brier score; calibration plots of predicted against observed
  3-year risk; decision curve analysis.
- **Missing data:** variables above **40%** missing excluded from the primary
  model unless clinically essential; multiple imputation by chained equations
  under missing-at-random, with **at least 20** imputed datasets pooled by
  Rubin's rules; complete-case analysis as a sensitivity check. Eyes missing the
  outcome or baseline acuity are excluded.
- **Sample size:** Riley framework for time-to-event models. **15 parameters, a
  target global shrinkage factor of 0.90, an anticipated Cox-Snell R² of 0.15 →
  approximately 823 independent eye-level observations**, rounded up to **at
  least 900 eyes** for development. External validation: **at least 400 eyes**,
  with a 20–30% expected 3-year incidence giving roughly **80–120 events**. Total
  at least **1,300 eyes** and roughly **260–390 events**.
- **Sensitivity analyses:** eleven, prespecified and listed — type 2 diabetes
  only; eyes with baseline retinopathy only; newly diagnosed or treatment-naive
  retinopathy; excluding severe cataract and other major eye disease; the
  stricter ≥0.3 threshold; the sustained-decline definition; eyes with at least
  two follow-up measurements; complete cases; one random eye per patient; all
  four models within the common paired-imaging subset; and a 90-day washout for
  recent eye treatments.
- **Prespecified subgroups:** retinopathy severity, macular oedema status,
  anti-VEGF history, baseline acuity, age (cut at 65), sex, glycaemic control
  (HbA1c cut at 7.0%), kidney function (eGFR cut at 60), imaging modality.
- **Reporting standard:** TRIPOD+AI, with a completed checklist supplied as a
  supplement (which did not render).
- **Patient and public involvement:** **none.** Stated plainly: "Patients and
  the public were not directly involved in the design, conduct, reporting or
  dissemination plans of this study."
- **Ethics:** Peking University Third Hospital Ethics Committee, approval
  IRB00006761-M20260399. Consent waived for retrospective de-identified data.
  Site-specific approvals to be obtained before external validation or data
  transfer.
- **Funding and competing interests:** **Not stated in the text retrieved.**

# How Strong Is This Evidence? — Grade 4/5

Same caveat as two days ago: this paper contains no evidence about whether
imaging AI predicts visual decline. The grade is for how much the plan
constrains the authors from fooling themselves later.

**What earns the points.**

**It did the sample-size calculation, and the calculation is checkable and
correct.** Riley's shrinkage criterion for a time-to-event model is

> n = P ÷ [ (S − 1) × ln(1 − R²cs ÷ S) ]

With the protocol's stated P = 15, S = 0.90 and R²cs = 0.15, that gives
**822.7**. The protocol says "approximately 823." Nothing was fudged. The
parameter budget also reconciles: 12 single-parameter predictors plus two for
three-level retinopathy severity is 14, plus one AI score is 15, exactly as
stated.

**It computed the budget on the right thing.** The calculation is based "on the
total number of prespecified predictor parameters in the largest primary
prognostic model rather than on the number of predictors retained after
penalisation or variable selection." That is the correct and commonly-dodged
choice: you pay for the parameters you *considered*, not the ones that survived.

**The leakage firewall is unusually thorough.** The AI scores come from public
datasets, the study's own images never train anything, the scores are frozen
before the prognostic model is fitted, AI training partitions are at patient
level, and LASSO cross-validation is separated at patient level so one person's
two eyes cannot leak into each other. There is a dedicated "Data leakage"
subsection. Four independent statements of the same firewall is not redundancy,
it is a team that knows this is where these studies die.

**External validation is specified strictly enough to be meaningful.** "Without
predictor selection, coefficient refitting or hyperparameter retuning," and any
recalibration reported separately as secondary. That is the same standard
yesterday's radiomics paper actually met — apply once, unchanged — written down
in advance.

**It picked the right outcome type.** A **time-to-event** outcome rather than a
yes/no at three years. That is the correct choice for irregular real-world
follow-up and it is rarer than it should be; this is the first time-to-event
primary outcome in this list.

**The performance measures are complete.** Discrimination (Harrell's C **and**
time-dependent AUC at three horizons, with Uno's C held in reserve for heavy
censoring), overall error (time-dependent Brier), **calibration plots**, and
**decision curve analysis.** Most prediction papers report one of these four.

**Missing data is handled properly:** multiple imputation by chained equations
with at least 20 datasets and Rubin's rules, a 40% exclusion rule, and
complete-case as a sensitivity analysis — not the mean-substitution seen earlier
this week.

**The prespecification is granular and auditable.** Eleven numbered sensitivity
analyses. Nine named subgroups with their cut-points stated. Baseline windows
pinned to 180 days. The ±180-day widening for slow-moving labs flagged in
advance as a sensitivity analysis rather than used quietly. Index-date rules that
explicitly prevent a linked complementary-modality image from shifting the
baseline. Four models with one clean comparison each against the same reference.

**It is honest about what it is.** The limitations name selection bias, missing
data, irregular follow-up, imaging heterogeneity across devices, and treatment
exposure during follow-up — and the closing sentence insists the model "should be
interpreted as a prognostic risk stratification tool rather than a causal
model."

**What costs the points.**

**One: no registration.** There is no registry identifier anywhere in the
retrieved text. Compare entry 37 two days ago, which registered an observational
study on ClinicalTrials.gov when nobody required it, explicitly "to ensure
transparency and public accountability." A published protocol is a strong
commitment; a registered one is a verifiable commitment, with a timestamped
record outside the journal. This protocol has done the harder intellectual work
and skipped the cheaper governance step.

**Two: two big competing causes of the outcome go largely unaddressed.** The
outcome is "visual acuity got worse." In a diabetic cohort over three years, two
things cause that without retinopathy changing at all.

**Cataract.** It is markedly more common and earlier in diabetes, it progresses
over exactly this timescale, and it produces precisely this measurement.
Baseline exclusions cover "severe corneal opacity" and major non-diabetic
disease, and one of the eleven sensitivity analyses excludes "eyes with severe
cataract" — but **incident** cataract during follow-up is not addressed, and it
is the common case. Worse, cataract **surgery** during follow-up typically
*improves* acuity, which would erase an outcome that had already occurred. The
protocol's only provision is that "major ocular treatments during follow-up will
be summarised descriptively and considered in sensitivity analyses." For the
single largest competing cause of the primary endpoint, descriptive
summarisation is not enough.

**Death.** Not mentioned anywhere. Diabetic patients, many with reduced kidney
function (eGFR is a predictor), have meaningful three-year mortality. A patient
who dies is censored at their last acuity — and that censoring is **informative**,
because the same things that predict dying predict worse eyes. Standard Cox
censoring assumes the censored are like those who remain; here they are
systematically sicker. The list covered competing risks before (entry 34,
Shimizu, where non-pneumonia deaths outnumbered the predicted events four to
one). Here it is a design gap rather than a reporting one.

**Three: the 9.4% uplift for two eyes per patient is probably not enough.** 823
is a requirement for **independent** observations. Both eyes of a patient are not
independent — diabetic retinopathy is a bilateral systemic disease and the two
eyes share duration, HbA1c and blood pressure. With two eyes per patient and
inter-eye correlation ρ, you need 823 × (1 + ρ) eyes to carry the same
information:

> ρ = 0.1 → **905** eyes. ρ = 0.3 → **1,070.** ρ = 0.5 → **1,234.** ρ = 0.7 →
> **1,399.**

The target is 900. At ρ = 0.5, those 900 eyes carry the information of about
**600** independent eyes, well short of 823. The protocol is honest that ρ
"cannot be estimated reliably before completion of data acquisition," and it
leans on cluster-robust standard errors, patient-level bootstrap and a one-eye
sensitivity analysis. Those are the right tools — but they fix the **inference**,
not the **information content**. Correcting a standard error does not recover
power; it correctly tells you that you have less of it. More on this in the
Spotlight, because it is the subtler half of a lesson this list has now met
three times.

**Four: the multimodal comparison has no sample size of its own.** Model 4 needs
paired fundus **and** OCT at baseline, and the protocol also plans to compare all
four models within that common subset to equalise case mix — a good idea. But no
target is given for how many eyes will have both. If 60% do, that is 540 eyes and
108–162 events against 15 parameters — about **7 to 11** events per parameter,
at or below the conventional floor. If 40% do, it falls to **5 to 7**. The
headline secondary objective is a comparison of fundus-only against OCT-only
against fused, and that comparison runs on the smallest cohort in the study with
no stated budget.

**Five: the anticipated R² of 0.15 is unsourced, and everything rests on it.**
The sample size is highly sensitive to it:

> R² = 0.20 → 597 eyes. **R² = 0.15 → 823.** R² = 0.10 → **1,274.** R² = 0.075 →
> **1,724.**

Halving the assumption roughly doubles the requirement. No citation or
derivation is given for 0.15. A prior study's value, or a stated range with the
corresponding sample sizes, would make the budget defensible rather than merely
arithmetically correct.

**Six: the primary outcome is a single unconfirmed measurement.** The more robust
definition — **sustained** decline, confirmed at the next visit — is specified,
and is relegated to secondary. Visual acuity has test-retest variability around
0.1 logMAR, so the 0.2 threshold sits at roughly twice the noise floor. One bad
measurement on one bad day will enter the primary analysis as an event. The
protocol clearly knows this (it says the sustained outcome exists "to assess the
potential influence of transient visual acuity variation") — which makes the
choice of the weaker definition as primary harder to explain.

**Seven: almost every verifiable detail is deferred to supplements.** Which
public datasets, with what labels, mapped how, at what sample sizes; the model
architectures; every training hyperparameter; the score scales and directions;
the full predictor parameterisation; the TRIPOD+AI checklist. A protocol's whole
function is to be checkable in advance, and a reader of the article body —
which is what the open-access rendering served — can check none of it.

**Eight: no patient or public involvement.** Stated plainly, which is better than
pretending, but this is a study whose entire clinical purpose is to change how
often patients are asked to attend appointments. That is a question patients
have views about.

# The Editor's Concerns

**Register the study, now, before the analysis runs.** ClinicalTrials.gov takes
observational studies, as the protocol decoded two days ago demonstrates. The
intellectual commitment here is already strong; registration makes it verifiable
by someone who does not have the journal in front of them.

**Add a competing-risks analysis for death, and say how incident cataract and
cataract surgery will be handled.** For death: report the Fine-Gray
subdistribution hazard or an Aalen–Johansen cumulative-incidence estimate
alongside the Cox model, so that three-year *absolute* risk is not overstated by
treating death as ordinary censoring. For cataract: at minimum, prespecify that
lens status will be extracted at baseline and follow-up, report how many
outcome events coincide with documented cataract progression, run the primary
analysis censoring at cataract surgery, and report what fraction of eyes have
surgery during follow-up. If a meaningful share of "visual decline" turns out to
be lens rather than retina, the incremental value of a *retinal* AI score is
attenuated for a reason that has nothing to do with the AI.

**Raise the development target, or state the contingency.** Either plan for
roughly 1,100 to 1,250 eyes, or state in advance: "if the observed inter-eye
correlation exceeds X, we will recruit further eyes / restrict to one eye per
patient / report the primary analysis on the one-eye subset." A prespecified
contingency costs nothing now and protects the result later. And note that
restricting to one eye per patient — currently a sensitivity analysis — is the
clean design: it would need about 823 patients and have no clustering problem at
all.

**Give a sample size for the paired-imaging subset,** since the comparison of
fundus against OCT against fused is a headline objective. State the expected
proportion with both modalities from the extraction already under way, and the
resulting events per parameter. If it is below 10, say what will be done — fewer
parameters in that comparison, or a penalised model reported as primary there.

**Source the 0.15.** Cite the study it comes from, or present the sample size
across a range of plausible values and commit to the conservative end.

**Swap the primary and secondary outcome definitions,** or at minimum
pre-commit to reporting both with equal prominence. Sustained decline confirmed
at a subsequent visit is the clinically meaningful event; a single reading
crossing a threshold two noise-widths wide is partly a measurement artefact.

**Say how visit frequency will be handled, not just summarised.** Follow-up
comes from routine care, so sicker eyes are seen more often and therefore have
more opportunities to be caught crossing the threshold. Visit frequency is
itself predicted by the baseline predictors, so this is not merely noise — it
biases the model toward predictors that drive clinic attendance. Summarising
intervals and restricting to eyes with at least two measurements (both planned)
help but do not solve it. Consider interval-censored methods, or including visit
count as a sensitivity covariate, and prespecify which.

**Measure whether the AI score transfers.** The scores come from public datasets
and are applied to a Beijing hospital cohort and then a Ningbo one. Public
retinopathy datasets differ in camera, population and label definition.
Prespecify a check: the distribution of each AI score in each cohort, and its
agreement with locally graded retinopathy severity. Without it, a null
incremental value is ambiguous between "imaging adds nothing beyond clinical
variables" and "our score did not transfer" — and yesterday's radiomics paper is
the cautionary example, where one centre's 0.86 became an uninterpretable 0.68
the moment the scanner changed.

**Check proportional hazards for the AI score specifically.** Schoenfeld
residuals are planned globally, which is right. But an imaging severity score
plausibly has a *front-loaded* effect — predicting early decline better than
decline at year three. If its hazard ratio is not constant, a single Cox
coefficient understates its early value and overstates its late value. Prespecify
a time-varying-effect check for the score, and report the time-dependent AUCs at
1, 2 and 3 years separately for it.

**Put the supplements' substance in the body, or at least name what is in
them.** Which public datasets, and the architecture family, belong in the
methods.

**State funding and competing interests.**

# Statistics Spotlight

Five ideas. The first is new to this list, and the second is the best worked
example of a sample-size calculation it has encountered.

## 1. Time-to-event analysis: why "when" beats "whether"

Every prediction paper decoded here so far asked a yes/no question: does this
person have a polyp, will this lesion grow, is this call a real emergency. This
protocol asks a **when** question, and that changes the statistics.

The naive approach would be: look at each eye three years later and record
whether vision declined. Two things go wrong. First, people turn up when they
turn up — real clinics do not run on three-year schedules, so some eyes have four
years of data and some have eight months. Second, "declined at some point in
three years" throws away the difference between declining in month two and
month thirty-four, which matters enormously to a patient.

**Survival analysis** fixes both. Instead of a yes/no, each eye contributes
**how long it was watched** and **whether the event happened by then**.

- An eye that crosses the ≥0.2 logMAR threshold at month 14 contributes: event,
  at 14 months.
- An eye last seen at month 20 with no decline contributes: **censored** at 20
  months. That is not a "no" — it is "no, *so far*, and we stopped looking."

Censoring is the whole idea. It lets you use partial information honestly. An eye
watched for 20 clean months tells you something real, and a yes/no analysis
either discards it or lies about it.

The standard tool is **Cox proportional hazards regression**. It models the
**hazard** — the instantaneous risk of declining right now, given you haven't yet
— and its central assumption is in the name: that a predictor multiplies the
hazard by the **same factor at all times**. If retinopathy grade doubles the
hazard, it doubles it in month 3 and in month 30.

That assumption is often wrong, and this protocol checks it, with **Schoenfeld
residuals** — essentially, do the predictor's effects drift as time passes? If
the residuals trend with time, proportional hazards has failed and a single
hazard ratio is a blur of a changing effect.

**Measuring discrimination is also different.** For a yes/no outcome you use AUC.
For survival data the equivalent is **Harrell's C-index**: of all the pairs of
eyes where you can tell who declined first, in what fraction did the model rank
that one as higher risk? Same 0.5-is-a-coin-flip scale, same interpretation, but
it handles censored pairs by simply not counting the ones where the order is
unknowable. The protocol adds **time-dependent AUC at 1, 2 and 3 years** — because
a model can be good at predicting early decline and poor at late decline, and a
single C-index averages that away. And it holds **Uno's C-index** in reserve for
heavy censoring, where Harrell's version is known to be biased by how much
censoring there is.

**An everyday version.** You want to know how long light bulbs last. You install
100 and check back after a year. Thirty have failed, at known dates. Sixty are
still burning — those are censored at one year, and "still working at 12 months"
is real information. Ten were removed when the room was redecorated at month
four — censored at four months, and you had better hope the redecoration had
nothing to do with which bulbs were failing. If it did, your censoring is
**informative** and your estimates are wrong. Which is exactly the problem with
death in this cohort.

**Watch out for:** a hazard ratio quoted with no mention of whether proportional
hazards was checked. And the common misreading — a hazard ratio of 2 does **not**
mean twice as many people get the outcome. It means twice the rate at any instant
among those still at risk, which can translate into a modest absolute difference
over three years. Always ask for the **absolute** three-year risk alongside it,
which is why this protocol's plan to report predicted 3-year risk and calibration
plots matters.

## 2. A sample-size calculation you can check yourself

This is the part worth copying. Two days ago, entry 37's protocol cited Riley and
colleagues and then skipped the calculation. This one runs it, and the number
comes out right.

For a prediction model, "how many do I need" is not about sampling error. It is
about **overfitting**: with too few outcome events relative to the number of
things you are estimating, the model fits noise, looks brilliant in development
and collapses elsewhere. The modern framework asks how much your model's
coefficients will have to be **shrunk** to stop that happening, and chooses a
sample size that keeps the shrinkage small.

The criterion for a time-to-event model:

> n = P ÷ [ (S − 1) × ln(1 − R²cs ÷ S) ]

Three inputs, and all three are judgements you can argue with:

- **P — the number of parameters.** Here 15. Note it is *parameters*, not
  predictors: 13 predictors, but three-level retinopathy severity needs two, so
  14, plus one AI score makes 15.
- **S — the target global shrinkage factor.** Here 0.90, meaning you accept that
  coefficients will need shrinking by about 10%. Closer to 1 is stricter and
  needs more data.
- **R²cs — the anticipated Cox-Snell R².** Here 0.15 — roughly, how much of the
  variation in outcome you expect the model to explain. A guess about the
  future.

Plug in P = 15, S = 0.90, R²cs = 0.15:

> ln(1 − 0.15 ÷ 0.90) = ln(0.8333) = −0.1823
> (0.90 − 1) × (−0.1823) = 0.01823
> n = 15 ÷ 0.01823 = **822.7**

The protocol says "approximately 823 independent eye-level observations." It
reproduces to the unit.

**And this is why the third input deserves a source.** The answer is very
sensitive to R²cs:

> R² = 0.20 → 597 eyes. **R² = 0.15 → 823.** R² = 0.125 → 1,003. R² = 0.10 →
> 1,274. R² = 0.075 → **1,724.**

Halve the assumed R² and the requirement roughly doubles. The protocol gives no
citation for 0.15, so the entire 900-eye target rests on one unsourced
optimistic-ish number. The calculation is right; the input is a hope.

**One more thing done correctly.** The budget is computed on the parameters in
the **largest** model, "rather than on the number of predictors retained after
penalisation or variable selection," and the protocol states that penalisation
"will not redefine the prespecified predictor set or the parameter budget." You
pay for the parameters you **considered**, not the survivors. Choosing which
variables to keep by looking at the data is itself a use of the data, and
pretending afterwards that you only ever fitted the winners is how studies claim
sample sizes they never had.

**Watch out for:** the phrase "events per variable" used as the only
justification, and worse, any sample-size section whose logic is "we used all
available data." Check whether the parameter count includes categorical
expansions and interactions, and whether it was counted before or after variable
selection.

## 3. The clustering you cannot fix with better standard errors

This list has now met clustering three times — pooling across studies (entry 30),
splitting lesions within patients (entry 38), and now two eyes per patient. The
new wrinkle here is the sharpest one.

The protocol does the two things that are usually missing. It splits at the
**patient** level so one person's eyes cannot appear on both sides of a
train/test boundary. And it uses **cluster-robust standard errors** plus
**patient-level bootstrap** so the uncertainty reflects the real structure.

Both are correct. Neither gives you back the information you don't have.

Here is the distinction, and it is worth getting straight. Two eyes from one
diabetic patient are highly alike — same disease duration, same blood sugar, same
blood pressure, same person. So 900 eyes from 450 people do **not** carry 900
eyes' worth of information. With m observations per cluster and intracluster
correlation ρ, the **effective** sample size is n ÷ (1 + (m−1)ρ). With m = 2:

> ρ = 0.1 → 900 eyes behave like **818.** ρ = 0.3 → **692.** ρ = 0.5 → **600.**
> ρ = 0.7 → **529.**

Against a requirement of 823. Turned round, to *carry* 823 independent
observations you need 823 × (1 + ρ) eyes: **905** at ρ = 0.1, **1,070** at 0.3,
**1,234** at 0.5. The protocol's uplift from 823 to 900 is **9.4%**, which covers
ρ ≈ 0.1 and nothing more. Inter-eye correlation in a bilateral systemic disease
is plausibly far higher.

So: **cluster-robust standard errors tell you the truth about your precision.
They do not improve it.** They are a thermometer, not a heater. If clustering has
eaten a third of your information, honest standard errors will correctly come out
wider — and your model will still be overfitted, because the shrinkage problem
is about how many events the coefficients were estimated from, not about how the
uncertainty is reported.

**An everyday version.** You want to know what the country thinks, so you survey
900 people. But you got them by knocking on 450 doors and interviewing both
people in each household. Households agree internally. You do not have 900
opinions; you have maybe 600. Weighting the answers properly and widening your
error bars is honest — it does not conjure 300 more households.

**Watch out for:** "we accounted for clustering with robust standard errors"
offered as if it resolved the matter. Ask two separate questions. *Was the
uncertainty computed correctly?* (robust SEs, cluster bootstrap — yes here.) And
*was the sample big enough once clustering is accounted for?* (a design
question, answered before collection — probably not here.) The second is the one
that gets skipped. And note the clean escape hatch: **one eye per patient** has no
clustering at all, and is currently only a sensitivity analysis.

## 4. When something else causes your outcome, or stops you seeing it

Two specific threats here, both about the outcome rather than the predictors.

**A competing cause of the same measurement: cataract.** The endpoint is
"best-corrected visual acuity got two lines worse." Diabetic retinopathy does
that. So does a cataract — a clouding of the lens — which is substantially more
common and earlier in diabetes and progresses over exactly three years. A model
built on *retinal* images and *retinal* severity grades is being scored partly on
an outcome caused by the lens in front of the retina. The effect is to **dilute**
the apparent value of every retinal predictor, including the AI score. If the
study reports that imaging AI adds little, one perfectly good explanation is
that a chunk of the endpoint was never retinal.

Worse, the direction reverses: **cataract surgery** usually *improves* acuity. An
eye that declined at month 10 and had surgery at month 16 may look fine at month
20. The protocol plans to summarise follow-up treatments descriptively, which is
not a plan for handling them.

**Informative censoring: death.** Not mentioned in the protocol. Standard Cox
censoring assumes that an eye censored at month 20 is representative of eyes
still being followed at month 20. If the patient died, that assumption fails in a
specific direction: whatever killed them — kidney disease, vascular disease, poor
glycaemic control — also damages retinas. So the eyes that vanish are
systematically worse than the eyes that remain, and treating them as ordinary
censoring **understates** true risk.

The right tools are **competing-risks** methods: a **Fine-Gray**
subdistribution-hazard model, or an **Aalen–Johansen** cumulative-incidence
estimator, which ask "what is the chance of visual decline by three years, given
that death can get there first" rather than the counterfactual "what if nobody
died."

**An everyday version.** You want to know how long students take to graduate.
Students who drop out are "censored." But dropping out is not random with
respect to graduating — the struggling ones leave. Treat them as merely
unobserved and you will conclude the course is easier than it is.

**Watch out for:** any three-year or five-year risk model in an older or sicker
population that never mentions death. Entry 34 in this list is the benchmark: a
pneumonia model where **18,138** people died of something other than pneumonia
against **4,525** pneumonia admissions — four competing events for every
predicted one.

## 5. Your threshold should clear your measurement noise

The primary outcome is a **single** reading showing ≥0.2 logMAR worsening. One
line on an eye chart is 0.1 logMAR, so 0.2 is two lines, a doubling of the
visual angle — a real, noticeable change.

But visual acuity is a **behavioural test**. The same eye on the same day gives
different answers depending on the chart, the lighting, the examiner, the
refraction, whether the patient is tired or has just had their pupils dilated.
Published test-retest variability for best-corrected acuity sits around **0.1
logMAR**. So the threshold is roughly **twice the noise floor** — not comfortably
clear of it.

That means some eyes will be recorded as having "declined" because of one bad
measurement on one bad day. And because the trigger is the **first** crossing
among all follow-up readings, the more times you measure an eye, the more chances
noise has to trip it. Noise is not symmetric when you take the minimum.

The protocol knows this — it defines **sustained decline** (≥0.2 confirmed at the
next eligible visit) explicitly "to assess the potential influence of transient
visual acuity variation," and it also offers a stricter ≥0.3 threshold. Both are
secondary.

This connects to something the list has already covered: **regression to the
mean.** An eye recorded at an unusually bad value is likely to read better next
time, for no clinical reason. Requiring confirmation at the next visit kills most
of that. Not requiring it means some fraction of your events are the statistical
equivalent of a bad hair day.

**An everyday version.** Your bathroom scale varies by about half a kilo
day to day. If you define "gained weight" as any single reading one kilo above
your starting point, you will have gained weight many times without eating
differently. Weighing twice and requiring both to agree fixes it.

**Watch out for:** a threshold-based outcome where the threshold is within about
two standard deviations of the measurement's own repeatability, and no
confirmation is required. Ask: what is the test-retest variability of this
measurement, and does the study require the change to be seen twice? If the
answer is no and the threshold is tight, some of the reported events are
measurement error — and a model trained to predict them is partly being trained
to predict noise.

# Jargon Translator

- **Protocol** — a published, dated description of a study written before it is
  run, so later deviations are visible.
- **Prognostic model** — predicts a future outcome. Distinct from a *diagnostic*
  model, which identifies a current state. The whole point of this paper.
- **Retrospective cohort** — a study of records of things that already happened.
- **Diabetic retinopathy (DR)** — damage to the retina's blood vessels from
  diabetes. **Non-proliferative (NPDR)** is earlier; **proliferative (PDR)**
  involves new fragile vessels growing and is more dangerous.
- **Diabetic macular oedema (DME)** — fluid swelling the central retina, a common
  cause of vision loss in diabetes.
- **Colour fundus photography (CFP)** — a photograph of the back of the eye.
- **Optical coherence tomography (OCT)** — a cross-sectional scan showing the
  retina's layers and any fluid. Complementary to a photograph.
- **Best-corrected visual acuity (BCVA)** — how well you see with the best
  possible glasses.
- **logMAR** — the acuity scale used in research. **Higher is worse.** One chart
  line is 0.1; a 0.2 increase is two lines, a doubling of the visual angle.
- **Anti-VEGF injection** — a drug injected into the eye to reduce leaking
  vessels and swelling.
- **Panretinal photocoagulation** — laser treatment for proliferative
  retinopathy.
- **eGFR** — estimated glomerular filtration rate; a kidney-function measure.
  Below 60 is considered reduced.
- **HbA1c** — average blood sugar over about three months. 7.0% is a common
  control target.
- **Time-to-event / survival analysis** — modelling *when* something happens, not
  just whether.
- **Censoring** — knowing only that the event hadn't happened by the time you
  stopped looking. **Informative censoring** is when the reason you stopped
  looking is related to the outcome, which breaks the analysis.
- **Competing risk** — a different event that prevents the one you care about
  from being observed (death, here).
- **Fine-Gray model / Aalen–Johansen estimator** — methods for estimating
  absolute risk when competing events exist.
- **Cox proportional hazards regression** — the standard survival model. Assumes
  each predictor multiplies risk by a constant factor at all times.
- **Hazard** — the instantaneous rate of the event among those who haven't had it
  yet. A **hazard ratio** compares two hazards; it is not a ratio of totals.
- **Schoenfeld residuals** — a diagnostic for whether the proportional-hazards
  assumption holds.
- **Harrell's C-index** — survival analysis's version of AUC. Of the pairs whose
  order is knowable, how often does the model rank them correctly? 0.5 is chance.
- **Time-dependent AUC** — discrimination measured separately at specific
  horizons (1, 2, 3 years here), rather than averaged.
- **Uno's C-index** — a C-index variant less sensitive to how much censoring
  there is.
- **Brier score** — average squared error of a probability forecast.
  **Time-dependent** means computed at specific horizons.
- **Calibration plot** — predicted risk against observed risk. Checks whether
  "30%" means 30%.
- **Decision curve analysis** — net benefit across the thresholds at which a
  clinician might act; compares the model to "treat everyone" and "treat nobody."
- **Cox-Snell R²** — a measure of how much variation a survival model explains.
  An input to the sample-size formula, and here a guess.
- **Global shrinkage factor** — how much coefficients must be pulled toward zero
  to stop a model overfitting. 0.9 means about 10% shrinkage is accepted.
- **LASSO / penalised regression** — shrinks weak predictors' coefficients toward
  (or to) zero, trading a little bias for much less overfitting.
- **Restricted cubic splines** — a way of letting a predictor's effect bend
  rather than forcing a straight line.
- **Random Survival Forest / gradient boosting survival** — machine-learning
  alternatives to Cox regression for time-to-event data.
- **Cluster-robust standard errors** — uncertainty estimates that account for
  correlated observations within a group. They report precision honestly; they do
  not increase it.
- **Intracluster correlation (ρ) / design effect** — how alike observations within
  a cluster are, and how much that shrinks your effective sample size.
- **Bootstrap resampling** — repeatedly re-drawing your sample to estimate
  uncertainty and correct over-optimism. **At the patient level** here, so both
  eyes travel together.
- **Optimism correction** — adjusting a development-cohort performance estimate
  downward to account for the model having been fitted on that same data.
- **Multiple imputation by chained equations (MICE)** — filling in missing values
  many times over to reflect the uncertainty, rather than once.
- **Missing at random (MAR)** — the assumption that what's missing can be
  predicted from what you observed. MICE needs it.
- **Rubin's rules** — how to combine estimates across imputed datasets.
- **Data leakage** — any route by which information about the outcome, or about
  the test set, reaches the model during training.
- **Standardised mean difference** — a scale-free measure of how different two
  groups are on a variable.
- **TRIPOD+AI** — the reporting checklist for AI-based prediction models.
- **Index date** — the baseline moment from which follow-up and predictors are
  defined.
- **Administrative truncation** — deliberately stopping follow-up at a fixed
  horizon (three years here) for everyone.
- **Washout window** — excluding a period after a treatment so its short-term
  effect doesn't contaminate the baseline.

# What You Can (and Can't) Say

**You can say:** a Chinese team has published a detailed protocol to build and
validate a model predicting three-year visual decline in diabetic eyes, testing
whether AI scores read from retinal photographs, OCT scans, or both fused add
anything to 13 routine clinical variables, with development at Peking University
Third Hospital and independent external validation planned at Ningbo Eye
Hospital.

**You can say:** the prespecification is strong. It computes its sample size with
the Riley framework on the parameters of the largest model (823 eyes, rounded to
900, with the calculation reproducing exactly from its stated inputs); it keeps
the AI models entirely away from the study's own images and from follow-up
outcomes; it specifies external validation with no refitting of any kind; and it
names eleven sensitivity analyses and nine subgroups with their cut-points in
advance.

**You can say** that this and the protocol decoded two days ago are a matched
pair: this one does the quantitative work the other skipped, and skips the
registration the other did voluntarily.

**You cannot say** anything about whether imaging AI predicts visual decline.
There is no model and no result. The authors state that as of September 2026,
data extraction has begun and nothing downstream is complete.

**You cannot say** the study is adequately powered. The 823-eye requirement is
for *independent* observations, and the 9.4% uplift to 900 covers an inter-eye
correlation of about 0.1 — likely an underestimate for a bilateral systemic
disease. The multimodal comparison, which is a headline objective, has no sample
size at all.

**You cannot treat** whatever three-year risk this model eventually reports as a
patient's absolute chance of losing vision. Death is not handled as a competing
risk, and treating it as ordinary censoring understates true risk in a cohort
with reduced kidney function among its predictors.

**You cannot assume** the outcome is purely retinal. Cataract is a common,
competing cause of exactly this measurement in diabetes, incident cataract
during follow-up is not addressed, and cataract surgery would reverse an outcome
already recorded.

**You cannot read** a null result on the AI scores as "retinal imaging carries no
prognostic information." It would be ambiguous between that and "a score trained
on public datasets did not transfer to these hospitals" — a distinction the
protocol does not currently plan to test.

**You should note** that the open-access rendering strips every supplement
reference, so the datasets, architectures, hyperparameters, score definitions and
TRIPOD+AI checklist cannot be checked from the article body.

# Bottom Line for Your Life

If you have diabetes, the useful part of this paper is its premise, which is
correct and under-appreciated: **your retinopathy grade is not your prognosis.**
Two people with the same grade today can have very different vision in three
years, and what separates them is largely the things in this protocol's clinical
model — how long you have had diabetes, your blood sugar, your blood pressure,
your cholesterol, your kidney function.

That list is mostly actionable, and it is the real message. The eye findings are
downstream of systemic control. The appointment where your HbA1c and blood
pressure get sorted out is doing more for your sight than the one where
photographs get graded.

**Get the screening.** Diabetic retinopathy is painless and silent until it is
advanced, which is the entire reason screening programmes exist. The treatments
— injections and laser — work far better early, and most vision loss from
diabetes is preventable with timely treatment. If you have been putting off a
retinal screening appointment, that is the single highest-value thing in this
summary.

**Two practical things from the detail of this protocol.** First, if your vision
seems worse at one appointment, that single measurement may not mean much —
acuity testing varies by about a line day to day, which is why this study's own
more rigorous outcome requires the change to be confirmed at a second visit. Ask
whether a recheck is worthwhile before anything drastic is decided. Second, not
all visual decline in diabetes is retinopathy: **cataract is very common in
diabetes and happens earlier**, and it is treatable with surgery that usually
restores the lost acuity. If your sight is getting hazier, that is a specific
thing to ask about, and it has a good answer.

And on what this protocol is actually for: it is trying to work out who needs to
be seen more often and who could safely be seen less. If a tool like this ever
reaches your clinic, the question to ask is the one the authors ask themselves —
was it validated on patients at a different hospital, with different cameras,
without being retuned? That is what this protocol promises to do, and the promise
is the reason it was worth reading before it has any answers.

**This is education about how to read a study, not medical advice. Decisions
about diabetes and eye care belong with you and your doctors.**

---

*Decoded 2026-10-06. Source: PubMed and PubMed Central, accessed 2026-10-06.
Full text read from PMC13630008. The PMC rendering stripped all supplement and
figure cross-references and served neither Figure 1 nor the two supplemental
files, so the public training datasets, label mappings, model architectures,
training hyperparameters, AI score scales, full predictor parameterisation and
the completed TRIPOD+AI checklist could not be examined; Table 1 did render.
Derived figures — the reproduction of the Riley sample size as 822.7 against the
protocol's stated 823, the sensitivity of that requirement to the anticipated
Cox-Snell R² (597 eyes at 0.20 up to 1,724 at 0.075), the parameter-budget
reconciliation to 14 and 15, the 9.4% uplift from 823 to 900, the inter-eye
correlation table (905 eyes needed at rho 0.1 up to 1,399 at 0.7, and 900 eyes
carrying 600 independent eyes' worth at rho 0.5), the events-per-parameter range
of roughly 5 to 14 for the paired-imaging subset, the expected event counts, and
the Hanley-McNeil precision of the external C-index at 80-120 events — were
computed from the protocol's own stated numbers and are labelled as derived
wherever they appear. No study registration identifier appears in the retrieved
text. Funding and competing interests were not stated in the text retrieved.*

**Verified source links**
- DOI: https://doi.org/10.1136/bmjopen-2026-123521
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42816089/
- Full text used: https://pmc.ncbi.nlm.nih.gov/articles/PMC13630008/
