# Reading a Study Before It Has Any Findings

**Paper:** trIAje project: protocol for a retrospective cohort study to optimise
AI-assisted telephone triage of time-sensitive conditions in emergency medical
services
**Authors:** Luque-Hernández MJ, Romero-Olóriz C, Ritoré-Hidalgo Á, Serrano
Alarcón Á, López López C, Caballero-García A, Armengol de La Hoz MÁ
**Venue / Year:** BMJ Open, 2026;16(9):e113242 (published 2026-09-28)
**DOI:** https://doi.org/10.1136/bmjopen-2025-113242
**PubMed:** https://pubmed.ncbi.nlm.nih.gov/42805668/
**Full text used:** https://pmc.ncbi.nlm.nih.gov/articles/PMC13630096/
**Registration:** ClinicalTrials.gov **NCT07247669**
**Basis of this analysis:** FULL TEXT (PubMed Central open-access copy,
retrieved 2026-10-04). Two things did not render in the PMC copy and are named
where they matter: Figure 1 (the triage workflow diagram) and the two
supplemental files (the completed STROBE-RECORD and TRIPOD+AI checklists).
The PMC rendering also **silently dropped the registration number** — the text
reads "registered at ClinicalTrials.gov (identifier)" with the identifier
missing, and "Trial registration number ." with nothing after it. NCT07247669
above comes from the live PubMed record for this article, not from the rendered
full text, and is flagged as such.
**Date decoded:** 2026-10-04
**Evidence grade:** 4/5 — **and this grade is for the plan, not for results.
This paper has no results.** See the grading section for what that means.

All identifiers above were verified against the live PubMed and PubMed Central
records on 2026-10-04. Nothing here is based on a guessed or reconstructed link.

---

# The Gist

Every paper this list has decoded so far had already happened. Somebody ran a
study, got numbers, and wrote them up — and the job was to work out how much to
trust the numbers.

Today's paper has no numbers. It is a **protocol**: a public, dated, ethics-
approved description of what a team is *about to* do, published before they do
it. And reading one is a distinct skill worth having, because a protocol is in
one specific way the most honest document in science. Nobody has seen the
results yet, so nobody can tilt the plan to flatter them.

The plan itself: emergency call centres across Andalusia, Spain — eight
physician-led coordination centres serving about **8.6 million people** and
taking **more than 1.5 million calls a year** — want to build an AI model that
listens to what the caller says and flags, during the call, whether this is a
genuine time-critical emergency: cardiac arrest, severe breathlessness, chest
pain, or stroke.

The reason is that the current system is not good at this, and the paper is
blunt about it. Across 31 studies, the sensitivity of medical dispatch systems
for critical illness ranged from **14% to 96%**. Over-triage — sending the
emergency response when it wasn't needed — runs **at or above 30%**. Under-
triage — failing to send it when it was needed — runs **up to 23%**. Cardiac
arrest is recognised on the phone somewhere between **14% and 96%** of the
time; stroke between **18% and 83%**. And in Australian and Swiss data, **fewer
than one in ten** of the missions dispatched at top priority truly needed
immediate life-saving intervention.

Crucially, the failures are not evenly spread. The paper states that
under-triage is more common in older patients, when the caller is not the
patient, and — this is the one that drives the study's design — **in women with
acute coronary syndrome, who more often present atypically and get missed.**

So the team will take five years of calls (2020–2024), link them to what
actually happened to each patient in hospital, and train models on both the
tick-box answers and the **free text** of what the call-taker typed while
listening. Then they will check, in advance of looking, whether the model works
as well for women as for men.

What makes this worth a careful read is not the ambition. It is that the plan
contains several things I have spent the last ten days asking other papers for —
and two problems serious enough that, if they are not fixed before the data are
analysed, the results will not mean what the team thinks they mean.

# Study Snapshot

- **Study type:** **Protocol** for a retrospective cohort study developing and
  **internally** validating a multivariable clinical prediction model. No
  results exist yet. Not a clinical trial, and the authors say so.
- **Setting:** All eight physician-led Emergency Coordination Centres
  (CCUE-061) in Andalusia, Spain. Catchment ≈8.6 million.
- **Period of data:** 2020–2024, five years.
- **Who is included:** Every eligible call — no sampling. Calls initially coded
  as chief complaint A36/A58 (unconsciousness / cardiorespiratory arrest), A16
  (breathing difficulty), A23 (non-traumatic chest pain), or A54 (suspected
  stroke).
- **Expected size:** Stated only as "on the order of tens of thousands of
  eligible calls and several thousand confirmed high-acuity (Priority 1)
  events." **No exact number, and no sample-size calculation.** More on this
  below — it is the single biggest gap.
- **Exclusions:** "Cases with missing essential data," which the authors say
  will be minimised.
- **Architecture:** Four separate chief-complaint submodels (A: unconscious,
  B: dyspnoea, C: chest pain, D: suspected stroke), whose outputs feed one
  clinical decision-support system producing a single priority recommendation.
- **Predictors:** Everything available at call time — time of day, day of week,
  province, urban/rural, age, sex, medical history (pulled live from the
  regional health record when the caller gives an ID number), caller's
  relationship to the patient, the structured questionnaire answers, the
  current system's own dispatch code and priority level, repeat calls for the
  same incident, and the free-text call-taker notes.
- **How the text is handled:** Spanish-language BERT models for sentence
  embeddings, plus evaluation of instruction-tuned open-weight large language
  models (LLaMA 3.3 is named), plus a curated keyword list for phrases like
  "not breathing," "turning blue," "sudden onset chest pain radiating to the
  arm."
- **Primary outcome:** A binary label — was this call a true Priority 1
  emergency? Positive if **any** of: found in cardiac arrest by responders;
  diagnosed with a time-sensitive condition (STEMI, stroke, severe respiratory
  failure) in prehospital or hospital records; required advanced life-support
  intervention on scene (intubation, defibrillation); or admitted to intensive
  care. Hospital discharge diagnosis is the gold standard when available,
  supplemented by prehospital diagnosis for patients not transported.
- **Secondary outcome:** Under-triage and over-triage rates, computed for both
  the current protocol and the AI system, for direct comparison.
- **Models planned:** Logistic regression, random forests, XGBoost, support
  vector machines, deep neural networks with LSTM or transformer text encoders,
  and stacking/voting ensembles.
- **Validation:** 80/20 split stratified by outcome; k-fold cross-validation
  inside the training set for tuning; **hold-out test set explicitly described
  as untouched during development.** No external validation — acknowledged.
- **Thresholds:** "Optimal probability thresholds will be derived from
  validation data... then applied to test predictions."
- **Fairness analysis:** Prespecified sex-disaggregated comparison of
  sensitivity, specificity and **false-negative rates**, with planned
  mitigation (re-weighting, loss-function penalties) and a gender-health
  advisory group.
- **Reporting standards followed:** STROBE, its **RECORD** extension for
  routinely collected health data, and **TRIPOD+AI** for the prediction model.
  Completed checklists supplied as supplements (not rendered in the copy read).
- **Registration:** ClinicalTrials.gov NCT07247669 — registered voluntarily, for
  transparency, despite being observational.
- **Ethics:** Andalusian Biomedical Research Ethics Committee, reference
  SICEIA-2025-001391, protocol version 5.0 dated 24/04/2025. Individual consent
  waived for anonymised retrospective data under Spanish Law 14/2007, GDPR and
  Organic Law 3/2018.
- **Deliverable:** A prototype decision-support tool that reads from, but never
  writes to, live dispatch systems. Code to be released publicly.
- **What is explicitly NOT in this study:** the shadow-mode prospective pilot.
  It is scoped out, made contingent on prespecified performance thresholds, and
  requires its own ethics approval and prospective registration.
- **Timeline:** 36 months, in six six-month stages.
- **Funding and competing interests:** **Not stated in the text retrieved.**

# How Strong Is This Evidence? — Grade 4/5

A word about what this grade means, because it is not the usual thing.

This paper contains **no evidence at all** about whether AI can triage
emergency calls. It cannot be graded on its findings, because it has none. What
can be graded is the **quality of the promise** — how much the plan, as
written and dated and publicly registered, constrains the team from fooling
themselves later. Four out of five means: this is a well-prespecified plan that
will be hard to spin, with two design problems that could still undermine the
answer and ought to be fixed before the analysis runs.

**What earns the points.**

**It commits in public, in advance, to things that are easy to abandon
quietly.** TRIPOD+AI is the right reporting standard for an AI prediction
model, STROBE-RECORD is the right one for routinely collected data, and using
both with completed checklists is more than most published *results* papers
manage. Registering an observational study on ClinicalTrials.gov when nobody
requires it is a deliberate act of self-binding.

**It gets the threshold question right** — and this is worth pausing on,
because yesterday's paper got it wrong. Entry 36 in this list, Ye et al., chose
its referral cutoff on the same hold-out set it used to report its headline
sensitivity, which makes that sensitivity an upper bound rather than an
estimate. This protocol says the opposite: thresholds come from **validation**
data and are **then applied to** test predictions, with the test set "untouched
during model development." That is exactly the fix. The habit of checking where
a threshold came from, which I wrote into the queue notes yesterday, found a
paper that passes on its first outing.

**It states the limits of explainability correctly, twice.** "SHAP and LIME
identify variables associated with the predicted outcome and support model
transparency, but they do not establish causal relationships." And then again,
in the design of the operator-facing screen: the contributing factors will be
labelled "as contributing associated factors, not causes." This is the single
cleanest handling of this point in anything decoded here — and again a direct
contrast with yesterday's paper, which narrated its SHAP plots as biology.

**It plans to report explanation fidelity and stability,** and prefers
inherently interpretable models "where predictive performance permits." Almost
nobody reports whether their explanations are *stable*. It is the right
question and it is rarely asked.

**The fairness analysis is prespecified, motivated, and has a mitigation
plan.** Not "we will check for bias" as a gesture, but a named metric
(false-negative rate), disaggregated by sex, with stated remedies
(re-weighting, loss penalties), a gender-health advisory group, and a clear
reason drawn from the literature — women with ACS are missed more often. Deciding
this before seeing the numbers is what makes it credible.

**It refuses to overclaim deployment.** The shadow-mode pilot — running live
without showing dispatchers the output — is the obvious next step, and the
protocol explicitly puts it outside this study, behind performance thresholds
and a fresh ethics approval. Most AI papers promise the clinic in their
abstract. This one declines.

**It admits what was missing.** Patient and public involvement was absent at
the grant-writing stage; the paper says so rather than backdating it.

**What costs the points.**

**One: the outcome label is partly caused by the decision being studied.** Two
of the four ways a call gets labelled "true emergency" are *consequences of
triage*. "Required advanced life-support intervention on scene" can only be
recorded if an advanced life-support unit was **dispatched** — which depends on
the original triage call. "Admitted to intensive care" requires having been
transported. So a call that the current system under-triaged, sending a basic
unit or no unit, is less likely to generate the evidence that would have marked
it critical. The label therefore **agrees with the existing protocol more often
than the truth does, and systematically hides under-triage** — the exact error
the study exists to measure. Compounding it, the gold standard (hospital
discharge diagnosis) is only available "for transported patients," with
prehospital diagnosis substituted for the rest: a weaker reference standard
applied to a group selected by the very decision under study. This is
differential and partial verification bias, and the protocol does not address
it.

**Two: a random split across a data window containing the COVID-19 pandemic.**
The data run 2020–2024. "Breathing difficulty" calls in 2020 and 2021 — their
volume, their callers, their outcomes, the whole dispatch protocol around them
— were not like 2024. An 80/20 split taken at random lets the model learn from
2024 and be tested on 2020, and vice versa, which flatters it: a real deployment
only ever predicts forward. The protocol includes year as a feature and promises
sensitivity analyses on "temporal protocol shifts," which is not the same thing.
The honest design for a tool meant to run next year is a **temporal split** —
train on the earlier years, test on the most recent — reported alongside the
random one.

**Three: it feeds the current system's own answer into the model, then compares
the two.** Predictors explicitly include "dispatch code and priority level,
allowing models to learn adjustments from baseline system performance." That is
a reasonable engineering decision and probably improves accuracy. But the
headline comparison is AI *versus* the current protocol — and the AI gets to see
the protocol's answer first. If it wins, you cannot tell how much of the win is
"AI beats protocol" versus "protocol plus extra information beats protocol
alone." A variant trained without the dispatch code would separate those, and
the protocol does not plan one.

**Four: no sample-size calculation, and the one place it is discussed gets the
question backwards.** Detailed below, because it is the best teaching material
in the paper.

**Five: calibration is mentioned but not specified.** "We will monitor
probability calibration" names no metric — no calibration slope, no
calibration-in-the-large, no Brier score. TRIPOD+AI asks for calibration
measures explicitly. For a tool whose whole function is to act at a threshold,
this needs pinning down.

**Six: the primary outcome is not fully defined.** "Final labelling criteria
will be defined jointly with senior emergency physicians from the coordination
centre." Involving clinicians is good; leaving the primary outcome open after
publishing the protocol is a prespecification gap, however well-intentioned,
because the definition can then move once the data are in view.

# The Editor's Concerns

These are the queries I would send back, and a protocol is the one kind of paper
where sending them back actually changes the science rather than just the
write-up.

**Break the circularity in the label, or bound it.** At minimum: report how many
positives were established by each of the four criteria separately, and how many
cases had hospital diagnosis versus prehospital diagnosis only. Then run the
analysis restricted to the criteria that do not depend on dispatch — a diagnosis
in the records, cardiac arrest found by responders — and show that the
conclusions hold. Without this, measured "under-triage" is an underestimate of
unknown size.

**Add a temporal split, and pre-register which one is primary.** Train on
2020–2023, test on 2024. Given the pandemic sits inside the window, also report
performance by year. If the random split and the temporal split disagree, the
temporal one is the one that tells you what happens at deployment.

**Train a model without the existing dispatch code** and report it alongside.
This is the only way the AI-versus-protocol comparison means what the abstract
says it means.

**Do the sample-size calculation, per submodel.** The protocol cites Riley and
colleagues on minimum sample size for prediction models, then declines to apply
their criteria on the grounds that the whole population is used. Those are
different questions (see the Spotlight). Working from the protocol's own
numbers: Spanish BERT sentence embeddings are 768-dimensional, and adding the
structured fields and keyword flags gives roughly **800+ candidate predictors**.
At the conventional 10 events per predictor that implies about **8,000 events**;
at 20, about **16,000**. The protocol anticipates "several thousand" Priority 1
events **across the whole cohort** — and then divides them among **four
submodels**. At 3,000 cohort events that is roughly 750 per submodel, an
events-per-variable ratio of about **0.9**. Regularisation and feature selection
change this calculation; they do not remove it. State the expected N per
submodel and the effective dimensionality after selection.

**Pin down the expected N, because two statements in the paper do not fit
together.** The protocol says CCUE-061 handles "more than 1.5 million assistance
requests per year" — about **7.5 million** over five years — that the four
target complaints "represent a substantial proportion" of these, and that the
team anticipates "tens of thousands" of eligible calls. Tens of thousands is
**0.13% to 1.3%** of 7.5 million. "Substantial proportion" and "tens of
thousands" cannot both be right, and every power claim in the paper depends on
which it is. The data already exist; count them.

**State the power of the fairness analysis.** This is the concern I would press
hardest, because the sex-disaggregated analysis is the best thing in the
protocol and it is the one most likely to come back inconclusive. Splitting by
submodel and then by sex divides the events twice. Suppose the true
false-negative rate is 15% in men and 25% in women — a ten-point gap, the order
the ACS literature the protocol itself cites would predict. Power to detect it
at the 5% level is about **24% with 50 test events per sex, 42% at 100, 58% at
150, and only reaches 80% at about 250.** A prespecified fairness analysis that
is underpowered will return "no significant difference," and that will be
reported as equity. Say in advance how many events are expected per sex per
submodel, and what will be concluded if the interval is wide.

**Reconsider F1 and balanced accuracy as the threshold-selection metrics.** Both
treat a false negative and a false positive as equally bad. In dispatch they are
not remotely equal: a missed cardiac arrest and an unnecessary ambulance differ
by orders of magnitude in cost. Use an explicit cost ratio, an Fβ with β stated
and justified, or decision-curve analysis. The protocol does promise sensitivity
analyses across thresholds so end-users can pick their own trade-off, which is
genuinely good — but the *primary* selection metric still embeds a value
judgement silently.

**Match the operating point when comparing to the current protocol.** A tunable
model and a fixed rule-based system cannot be compared at arbitrary thresholds.
Report AI sensitivity at the protocol's specificity, and AI specificity at the
protocol's sensitivity. Otherwise the comparison can be won by choosing a
threshold.

**Replace median imputation with multiple imputation,** and state that
imputation models will be fitted on the training set only. Also: the exclusion
of "cases with missing essential data" needs a missingness analysis before it is
applied. Missing dispatch fields are unlikely to be missing at random — the most
chaotic calls, where the caller is panicking and the patient is in arrest,
plausibly have both the least complete structured data **and** the highest
acuity. Excluding them could remove precisely the cases the model exists to
catch. Report the exclusions' outcome rate.

**State funding and competing interests.** Not present in the text retrieved.

**Finalise the primary outcome before the data are opened,** and publish the
amendment if it changes.

# Statistics Spotlight

Five ideas. The first is about protocols as a genre; the rest are the
load-bearing statistics in this one.

## 1. Why a protocol is the most honest document in science

Here is the problem a protocol solves. After you have seen your data, there are
hundreds of small, individually defensible choices still open: which outcome is
"primary," where to put the threshold, which subgroup to highlight, whether to
adjust for that variable. Each can be argued for. And the ones that make the
result look better are *easier* to argue for, because you can see that they do.
Nobody has to be dishonest for this to go wrong. It is enough to be human and
to be looking.

A protocol removes the choices from the room before the data arrive. It is
dated, it is public, it is registered, and anyone can later ask: did you do what
you said?

**What to look for when you read one:**

- **Is the primary outcome one thing, defined exactly?** Here: mostly yes, with
  one gap — final labelling criteria are still to be agreed.
- **Is the analysis specified, or just gestured at?** Here: specified in unusual
  detail, down to the libraries.
- **Is the hold-out set protected in writing?** Here: yes, explicitly.
- **Where do the thresholds come from?** Here: validation data, then applied to
  test. Correct.
- **Are the subgroup analyses named in advance?** Here: yes — sex, with
  false-negative rate as the metric.
- **Is there a registration number?** Here: yes, NCT07247669, voluntarily.
- **What is promised but out of scope?** Here: the shadow-mode pilot, gated
  behind performance thresholds and separate approval.

And the matching test for later: when the results paper appears, read it next to
the protocol. Anything that moved — and did not say it moved — is the thing to
ask about.

## 2. "We used everyone, so we don't need a sample size" — half right

This is the most instructive sentence in the paper: *"Because the study uses the
entire eligible population rather than a sample, no formal a priori sample-size
calculation is required."*

There are really two different questions that both get called "sample size," and
using the whole population answers one of them and not the other.

**Question one: how uncertain am I about this population?** If you want to know
the average height of everyone in a city and you measure *everyone*, there is no
sampling error — you have the answer. Using the complete population genuinely
does retire this question. The protocol is right about that.

**Question two: how many examples does my model need before it starts
memorising instead of learning?** This one has nothing to do with sampling. It
is about the ratio between **how much the model has to estimate** and **how much
information it has to estimate it from** — and for a yes/no outcome, the
information is carried almost entirely by the **rarer** class. Not the number of
calls. The number of *true emergencies*.

The usual shorthand is **events per variable (EPV)**: the number of outcome
events divided by the number of candidate predictors. The old rule of thumb is
10; more careful modern work (Riley and colleagues, whom this protocol cites)
replaces the rule of thumb with a calculation based on how much the model is
expected to explain.

Now put the protocol's own plans through it. Spanish BERT sentence embeddings
are **768 numbers per call**. Add age, sex, province, urban/rural, time, weekday,
medical history, caller relationship, the dispatch code, the priority level, the
questionnaire answers and the keyword flags, and you have on the order of **800
candidate predictors**.

> At 10 events per variable: about **8,000** events needed.
> At 20: about **16,000**.

The protocol expects "several thousand" Priority 1 events across the whole
cohort — short of the 10-EPV figure before anything else happens. And then the
design **splits into four submodels**, one per chief complaint, so the events
split four ways too:

> 3,000 cohort events ÷ 4 submodels ≈ **750 events each** → EPV ≈ **0.9**
> 6,000 ÷ 4 ≈ 1,500 each → EPV ≈ **1.9**
> 10,000 ÷ 4 ≈ 2,500 each → EPV ≈ **3.1**

**An everyday version.** Suppose you want to learn what makes a good restaurant
and you are allowed 800 yes/no facts about each one — cuisine, street, hour,
lighting, how many forks. If you have visited 750 restaurants, you can find a
combination of facts that perfectly separates the ones you liked from the ones
you didn't. You will also have learned nothing: with that many facts and that
few meals, a perfect-looking rule exists **by arithmetic**, whatever the truth
is. It will fail on restaurant 751.

The protocol's mitigation — "automated feature selection and regularisation
methods prevent overfitting" — is the right tool, and it genuinely helps.
Regularisation shrinks the model's effective number of parameters, which is what
the EPV calculation really cares about. But it transforms the question rather
than deleting it: the honest version becomes "what is my effective
dimensionality after shrinkage, and is it small enough for my event count?" That
calculation is not in the paper.

**Watch out for:** any paper that justifies skipping a power or sample-size
calculation by pointing at a large total N. Ask how many **events** there were,
and how many **parameters** were fitted, and whether the analysis was split into
subgroups — because every split divides the events while leaving the parameters
alone.

## 3. When the outcome is caused by the thing you are studying

A prediction study needs a **reference standard** — the thing you treat as the
truth. The whole exercise rests on that truth being established *independently*
of the decision being evaluated.

Here it isn't, in two of four cases. A call counts as a true emergency if the
patient "required advanced life-support interventions (intubation,
defibrillation) on scene" or "was admitted to an intensive care unit." Both
require that someone was **sent** — which is the triage decision. Run it
forward:

- A call correctly triaged high → advanced unit dispatched → intubation
  performed and recorded → labelled critical. Correct.
- A call **under-triaged** → basic unit, or none → no advanced intervention
  possible, no ICU admission via that route → the evidence that would have
  labelled it critical was never generated.

So the label is **more likely to agree with the current protocol than the truth
is**, and it is biased in the single most consequential direction: it hides
exactly the under-triage the study was built to find. Measured under-triage will
be an underestimate, and the AI model — trained on these labels — will learn to
reproduce the existing system's blind spots and be scored as correct for doing
so.

There is a second, related problem: the gold standard (hospital discharge
diagnosis) exists only "for transported patients," with prehospital diagnosis
substituted otherwise. Being transported is itself downstream of triage. When
different patients get reference standards of different quality, and which one
you get depends on the thing under study, that is **differential verification
bias**; when some get no gold standard at all, **partial verification bias**.
QUADAS-2, the standard appraisal tool for diagnostic accuracy studies, has a
whole domain for this.

**An everyday version.** You want to know whether a shop's security guard is any
good at spotting shoplifters. You define "was a shoplifter" as "was caught with
stolen goods by the guard." The guard now scores 100%, and every thief who
walked past unchallenged has been defined out of existence.

**Watch out for:** in any diagnostic or triage study, ask *who decided which
patients got the definitive test, and did the thing being evaluated influence
that decision?* If yes, sensitivity is overstated and misses are undercounted.

## 4. Random splits versus time splits

Splitting data into training and test sets at random is the default, and for
most problems it is fine. It stops being fine the moment the world changes
inside your data window — because a random split quietly lets the model learn
from the future.

This protocol's data run **2020 to 2024**, and one of its four chief complaints
is **breathing difficulty**. The COVID-19 pandemic sits in the middle of that
window. In 2020 and 2021, the volume of dyspnoea calls, who was calling, what
the dispatch protocols said, and what happened in hospital were all different
from 2024.

Under a random 80/20 split, a model can train on 2024 calls and be tested on
2020 calls, and vice versa. It gets to absorb the pandemic's patterns and then
be scored on predicting them. Deployment is never like that: a tool switched on
next year has only the past to learn from.

The fix is a **temporal split** — train on 2020–2023, test on 2024 — reported
next to the random one. If the two agree, the random number was trustworthy. If
the temporal number is worse, that gap *is* the finding: it tells you how fast
the model goes stale, which is exactly what an emergency service needs to know
before committing to one.

Including year as a predictor, which the protocol does, is not a substitute. It
lets the model adjust for which year a call came from — it does not stop the
model from having seen the future.

**Watch out for:** any model meant to run forward in time, validated on a random
split of historical data, especially data spanning a disruption. Look for the
words "temporal," "chronological," or a date-based split. If they are absent,
the reported performance is the optimistic case.

## 5. F1 quietly assumes a miss costs the same as a false alarm

To turn a model's probability into a decision you pick a threshold, and to pick
a threshold you need a score to maximise. This protocol names **F1** and
**balanced accuracy**.

**F1** is the harmonic mean of precision (of those flagged, how many were real)
and recall (of those real, how many were flagged). It has two properties worth
knowing. It **ignores true negatives entirely** — the enormous pool of
correctly-not-dispatched calls does not appear. And it weights precision and
recall **equally**, which is a statement that a missed emergency and an
unnecessary ambulance are equally bad.

In emergency dispatch they are not close. A missed cardiac arrest is a death. An
unnecessary ambulance is expense and a slower response to the next call —
serious, but not the same order of thing.

The honest tool is **Fβ**, where β says how many times worse a miss is:

> Fβ weights recall **β²** times as heavily as precision.
> β=1 → equal. β=2 → recall counts **4×**. β=3 → **9×**. β=5 → **25×**.

Choosing β forces you to say out loud what you think the exchange rate is. With
F1 you have said it too — you have said 1 — just without noticing.

Better still for this problem is **decision-curve analysis**, which sweeps the
threshold and plots net benefit, letting a service read off the answer for its
own cost ratio. Credit where due: the protocol does promise threshold
sensitivity analyses "enabling end-users to select trade-offs appropriate to
local priorities," which is the right instinct. The gap is that the *primary*
selection metric is still symmetric.

**Watch out for:** F1 or accuracy as the headline metric in any setting where
the two kinds of error have very different costs. Ask what exchange rate the
metric implies, and whether anyone chose it on purpose.

# Jargon Translator

- **Protocol** — a published, dated description of a study written *before* it
  is run, so that later deviations are visible.
- **Prespecification** — committing to decisions in advance, so results cannot
  shape the analysis.
- **Retrospective cohort** — a study of records of things that already happened.
- **Time-sensitive condition (TSC)** — an emergency where minutes change the
  outcome: cardiac arrest, heart attack, stroke, respiratory failure.
- **Under-triage** — treating a real emergency as low priority. The dangerous
  error.
- **Over-triage** — treating a non-emergency as top priority. The expensive
  error.
- **OHCA** — out-of-hospital cardiac arrest.
- **ACS / STEMI** — acute coronary syndrome; ST-elevation myocardial
  infarction, the kind of heart attack needing immediate reopening of an artery.
- **Reference standard / gold standard** — the thing treated as the truth when
  scoring predictions.
- **Differential verification bias** — some patients' truth is established by a
  better test than others', and which you get depends on the thing being
  studied.
- **Partial verification bias** — some patients never get the definitive test at
  all.
- **Sensitivity / recall** — of the real emergencies, the share correctly
  flagged.
- **Specificity** — of the non-emergencies, the share correctly left alone.
- **Precision / PPV** — of those flagged, the share that were real.
- **AUC-ROC** — chance the model scores a random real emergency above a random
  non-emergency. 0.5 is a coin flip.
- **AUC-PR** — area under the precision-recall curve; more informative than
  AUC-ROC when the outcome is rare. Its no-skill baseline is the prevalence.
- **F1 / Fβ** — combined precision-and-recall scores; β sets how much more a
  miss costs than a false alarm.
- **Calibration** — whether "20%" actually happens 20% of the time.
- **Events per variable (EPV)** — outcome events divided by candidate
  predictors; a rough guard against overfitting.
- **Overfitting** — learning the noise in your data, so performance collapses on
  new data.
- **Regularisation** — penalising complexity so a model cannot chase noise;
  shrinks the effective number of parameters.
- **Hold-out test set** — data deliberately untouched until the very end.
- **k-fold cross-validation** — rotating which slice of the training data is
  used for checking, to tune choices without touching the test set.
- **Temporal split** — training on earlier data and testing on later, to mimic
  real deployment.
- **NLP (natural language processing)** — turning free text into numbers a model
  can use.
- **BERT / embeddings** — a language model that converts a sentence into a list
  of numbers (here, 768 of them) capturing its meaning.
- **LLaMA 3.3** — an open-weight large language model, named here as a candidate
  text encoder.
- **LSTM** — an older neural network design for sequences, such as text.
- **SHAP / LIME** — methods that attribute a single prediction to its input
  features. They describe the model, not the body.
- **Clinical decision-support system (CDSS)** — software that offers a
  recommendation to a clinician, who decides.
- **Shadow mode** — running a system live on real cases while hiding its output,
  so it can be measured without affecting care.
- **STROBE / RECORD / TRIPOD+AI** — reporting checklists: observational studies,
  routinely collected data, and AI prediction models respectively.
- **GDPR** — the EU data-protection regulation.
- **Consent waiver** — ethics-committee permission to use existing anonymised
  records without asking each person, when asking is impracticable.

# What You Can (and Can't) Say

**You can say:** a Spanish team has published a registered, ethics-approved
protocol to build and internally validate an AI model for emergency telephone
triage, using all 2020–2024 calls for four time-critical complaints across
Andalusia, with prespecified sex-disaggregated fairness analysis.

**You can say:** the existing evidence they cite shows dispatch triage performs
poorly and inconsistently — sensitivity for critical illness ranging from 14% to
96% across 31 studies, over-triage at or above 30%, under-triage up to 23%.
Those numbers are from prior literature, not from this study.

**You can say:** the protocol follows TRIPOD+AI and STROBE-RECORD, protects its
hold-out set in writing, derives thresholds from validation rather than test
data, states that SHAP and LIME show association and not causation, and places
the live pilot outside the study behind performance thresholds and separate
ethics approval. As a piece of prespecification it is better than most results
papers.

**You cannot say** anything whatsoever about how well this model works. There is
no model yet and there are no results. Not "promising," not "shows potential" —
nothing. The timeline is 36 months.

**You cannot say** AI improves emergency dispatch. One prior Spanish study is
cited as raising F1 by 17% over a regional protocol; that is somebody else's
result, one study, on a different system.

**You cannot say** this study will show whether the model is fair to women. It
will report the comparison, which is to its credit — but on the event counts the
protocol anticipates, a real ten-point gap in false-negative rate might be
detected only about a quarter to a half of the time. An inconclusive answer is a
likely outcome and should not be read as equity.

**You cannot treat** the study's eventual under-triage figure as the true rate.
Two of the four label criteria depend on an advanced unit having been
dispatched, so missed emergencies are structurally undercounted.

**You cannot assume** the eventual performance numbers transfer to another
country's dispatch system, or even forward in time within Andalusia. There is no
external validation planned, and the validation split is random rather than
temporal across a window containing the pandemic.

**You should note,** if you ever cite this protocol, that its registration
number was dropped from the PubMed Central rendering and had to be recovered
from the PubMed record.

# Bottom Line for Your Life

The useful thing in this paper is not the model that does not exist yet. It is
what the published literature it cites tells you about **what happens when you
phone for an ambulance** — and what you can do in those ninety seconds to make
the system work better.

Dispatch triage is genuinely hard and it genuinely fails. Over-triage at or
above 30%, under-triage up to 23%, cardiac arrest recognised somewhere between
14% and 96% of the time depending on the system. The person taking your call is
following a script and cannot see the patient. What they get right depends
heavily on what you tell them.

So: **say the worst thing first.** Not the history, not the context — the
single most alarming observation. "He is not breathing." "She is grey." "The
pain is in his chest and going down his left arm." "Her face has dropped on one
side and she can't speak." The paper lists exactly these as the phrases the
model will be trained to catch, because they are the phrases that move a
dispatcher. Lead with them.

**Answer the questions, even when they feel like a delay.** The script exists
because it works more often than improvisation. And **stay on the line** —
dispatchers talk callers through CPR, and bystander CPR before the ambulance
arrives is one of the largest survival effects in all of emergency medicine.

Two specific things worth carrying. First: **under-triage is more common when
the caller is not the patient.** If you are calling for someone else, be
concrete about what you can see rather than what you assume. Second, and the
reason this study is designed the way it is: **women having heart attacks are
missed more often**, because the presentation is more often not the classic
crushing central chest pain — it can be nausea, breathlessness, jaw or back
pain, overwhelming fatigue. If that is you, or someone you are calling for, say
the words "I think this could be a heart attack." Do not wait to be asked the
question that fits the textbook.

**This is education about how to read a study, not medical advice. In an
emergency, call your local emergency number and follow the dispatcher's
instructions.**

---

*Decoded 2026-10-04. Source: PubMed and PubMed Central, accessed 2026-10-04.
Full text read from PMC13630096. Figure 1 and the two supplemental checklist
files were not retrievable; the ClinicalTrials.gov identifier was dropped by the
PMC rendering and was recovered from the live PubMed record (NCT07247669).
Derived figures — the ~800 candidate-predictor count and its 8,000/16,000-event
implications, the ~0.9 to 3.1 events-per-variable range per submodel, the
0.13%–1.3% mismatch between "tens of thousands" and 7.5 million calls, the
Wilson confidence-interval widths for sensitivity, and the 24%/42%/58%/80% power
figures for detecting a ten-point sex gap in false-negative rate — were computed
from the protocol's own stated numbers and standard dimensionalities, and are
labelled as derived wherever they appear. Funding and competing interests were
not stated in the text retrieved.*

**Verified source links**
- DOI: https://doi.org/10.1136/bmjopen-2025-113242
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42805668/
- Full text used: https://pmc.ncbi.nlm.nih.gov/articles/PMC13630096/
- Registration: ClinicalTrials.gov NCT07247669 (from the PubMed record)
