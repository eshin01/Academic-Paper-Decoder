# A machine learning-based ecological momentary intervention for mental health promotion in youth: a micro-randomized trial

**Authors:** Rauschenberg C, Schirmbeck F, Fechtelpeter J, Wierzba E, Hiller S, Kahr K, Kessler A, Hornbacher L, Goetzl C, Schick A, Durstewitz D, Krumm S, Koppe G, Reininghaus U
**Journal:** Translational Psychiatry, 2026; volume 16, issue 1 (published 26 September 2026)
**Decoded:** 2026-10-11
**Analysis basis:** FULL TEXT (retrieved from PubMed Central, PMC13615972). Supplementary files (eTables, eFigures, eMethods) were not retrievable, so several numbers below are marked as "in a table or supplement not retrieved."

**Source links (all verified):**
- DOI: https://doi.org/10.1038/s41398-026-04475-8
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42800797/
- Full text (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC13615972/

---

## 1. The Gist

A German team built a phone app for young people aged 14 to 25 that pings you several times a day, asks how you are feeling, and then hands you a short mental-health exercise — a breathing practice, a reframing prompt, a moment of self-compassion. There were eight such exercises.

The question was not "does the app help?" The question was narrower and more interesting: **does letting a machine learning model choose which exercise to give you work better than picking one at random?**

To answer it they did something clever. Instead of splitting people into two groups, they flipped a coin *inside each person*, over and over — up to seven times a day for a month. At each ping, a coin decided whether that moment's exercise came from the model or from a random draw. Every participant therefore spent part of their month in the "smart" condition and part in the "random" condition, and you can compare a person against themselves.

The result: out of three things they measured, the model beat random on one — a single question about whether you feel you can handle whatever difficulties come your way. The effect was small (0.147 points on a 1-to-7 scale) and only barely cleared the usual statistical bar (p = 0.044, with the confidence interval reaching down to 0.004, essentially zero). The model did not beat random on positive mood or on negative mood.

The app was safe, people used it, and people mostly liked it. The authors are unusually straight about all of this. Their own conclusion is that this is "an initial, outcome-specific signal" — and that is exactly the right phrase for it.

---

## 2. Study Snapshot

**Design:** Within-subject micro-randomized trial (MRT). This is not a standard randomized controlled trial and the difference matters a lot — see the Statistics Spotlight.

**Where and when:** Germany, July 2022 to February 2023.

**Who:** Young people aged 14 to 25, recruited from the general population and from psychological counselling services. People were **excluded** if they had a current mental health condition, were currently using mental health services, were acutely suicidal, or could not give informed consent. So this is a mental-health-*promotion* study in a largely well population, not a treatment study.

**The funnel, step by step:**
- 80 expressed interest
- 61 gave written informed consent
- 58 completed baseline and started the 40-day programme
- 49 produced enough data to enter the repeated randomisation (average age 20.6, SD 3.4; 38 female, 78%; 10 male, 20%)
- 42 (86%) were in the main proximal analysis — 6 dropped out of it because of a server restart that corrupted the log of which condition they were in, 1 for insufficient data
- 44 (90%) were in the before-and-after analysis of the longer-term measures
- 48 of 49 (98%) completed the final assessment

**What was randomised:** Not people. *Moments.* At each eligible ping ("decision point"), a 1:1 coin flip decided between (i) the machine learning model choosing the exercise, or (ii) random choice of exercise. Up to seven decision points a day across a 30-day training phase, so up to 210 per person.

**The comparison group is the important design choice:** the control condition was **random assignment of a real exercise**, not a placebo and not nothing. So this trial does not ask "is the app better than no app?" It asks the much tighter question "is the model's choice better than a coin's choice, given that you get an exercise either way?"

**The model:** a recurrent neural network built for "dynamical systems reconstruction" — a model that tries to learn the shape of your personal emotional ups and downs over time. 30 units, 15 of which map one-to-one onto the 15 things the app asked about (mood, worry, loneliness, energy, concentration, and so on). It was **retrained from scratch every night, separately for every participant**, provided that person had at least 1.5 data points a day and at least 20 in total. At a decision point it simulated the next six time steps (roughly a day) under each of the eight candidate exercises, scored each one, turned the scores into probabilities with a softmax, and sampled from that. So it favoured the exercise it predicted would help most, but kept some chance of picking others.

**Notably, what the model did NOT use:** no phone sensor data at all — no GPS, no step counting, no sleep tracking, no screen-time features. Only the self-reported answers. And the model never chose *when* to intervene, only *which* exercise; timing was not optimised.

**Measures (proximal, i.e. a few hours later):**
- Positive affect: 3 items (good, relaxed, satisfied), internal consistency McDonald's ω = 0.87
- Negative affect: 3 items (scared, down, sad), ω = 0.84
- **Momentary resilience: one single item** — "I can handle all the difficulties that I may encounter." Internal consistency not applicable, because you cannot compute it on one question.
- All on a 1-to-7 scale.

**Measures (distal, before versus after):** K10 psychological distress, CERQ emotion regulation, CD-RISC resilience. **No follow-up assessment after the programme ended.**

**Analysis:** the `MRTAnalysis` R package (v0.1.2), using `wcls()` — weighted and centered least squares — to estimate the "marginal causal excursion effect." Before-and-after distal changes by paired t-tests with Cohen's d.

**Ethics:** approved by the Medical Ethics Review Committee II at Heidelberg University, Reference No. 2022-550. **No trial registration number appears anywhere in the text retrieved**, and none appears in the PubMed record. PubMed classifies the article type as "Randomized Controlled Trial."

**Results, plainly:**
- Momentary resilience: B = 0.147, 95% CI 0.004 to 0.290, p = 0.044
- Positive affect: B = 0.012, 95% CI −0.11 to 0.14, p = 0.839
- Negative affect: B = 0.093, 95% CI −0.02 to 0.21, p = 0.103
- Average gap between getting the exercise and being measured: 3.09 hours (SD 2.44; median 2.42; quartiles 1.48 and 4.07) — and that gap was the same in both conditions (Wilcoxon W = 114,075, p = 0.518)
- Before-and-after, uncontrolled: distress d = −0.24, resilience d = 0.55, adaptive emotion regulation d = 0.53, maladaptive emotion regulation d = −0.20
- Safety: no serious adverse events. App use averaged nearly 7 hours (SD 3.6) across the 40 days, about 10 minutes a day.
- Baseline distress (K10) averaged 23.8 (SD 7.1), with 36% in the moderate or severe range.

---

## 3. How Strong Is This Evidence? (Grade 3/5)

Three out of five. This is a well-built study reporting a thin result, and — crucially — saying so.

**What earns it marks:**

The design is genuinely strong for the question asked. Randomising inside each person at hundreds of moments removes, in one stroke, the entire category of problem where the two groups differ to begin with. You cannot be confounded by personality, income, education, or baseline distress when you are comparing a person to themselves. The control condition was active (random assignment of a real exercise), which is the hard comparison, not the easy one. The analysis method is the right one for this design rather than an off-the-shelf regression. There was an a priori power calculation. And the model was retrained person by person, nightly, from scratch — a deliberate choice to avoid getting locked into a bad early fit.

The honesty is exemplary, and I want to be specific about that rather than vague. The authors themselves write that "it is important to distinguish forecasting performance from policy value," that the resilience effect "cannot be unambiguously attributed to accurate personalization," and then they list the alternatives that would explain it just as well: the model may simply have drifted toward exercises that are better *on average for everyone* (nothing personal about it), or it may be chance, or momentary resilience may just be the one measure sensitive to brief exercises, or the effect may be an artefact of when the measurement window happened to fall. They say the before-and-after improvements "should not be interpreted as causal." They say the technical exclusion comparisons were "exploratory and underpowered and should not be interpreted as evidence of equivalence." Every one of those is a criticism I would otherwise be making here, pre-empted by the authors in their own words. That is what good scientific writing looks like.

**What holds it back:**

The headline rests on one fragile number. It is one positive result out of three proximal outcomes, with no multiplicity correction anywhere in the paper, at p = 0.044, with a confidence interval whose lower edge is 0.004 — four thousandths of a point on a seven-point scale. Correct for having looked at three outcomes and it does not survive (see Statistics Spotlight).

The one outcome that moved is the one measured with a single question. Positive and negative affect each had three items and reported internal consistency. Momentary resilience had one item, so reliability cannot even be assessed. A single-item measure is noisier, and noise usually pushes effects *toward* zero rather than inventing them — but it also means we cannot check the measure's quality at all, and it is uncomfortable that the lone positive finding sits on the lone unverifiable measure.

The study was under-recruited. The power calculation said 60 participants for about 87% power. They randomised 49 and analysed 42. My recalculation puts the realised power at roughly 73% for the effect they planned around (see Statistics Spotlight) — still respectable, but no longer what was planned.

No registration number appears in the retrieved text. For a trial with three proximal outcomes and no designated primary one, registration is what would let a reader confirm which outcome was nominated in advance. Without it, "one of three was positive" has to be read with the possibility that the ordering was settled afterwards. I am not alleging that happened — the paper's objectives list all three and its framing is consistent throughout — but the check is unavailable.

The before-and-after numbers have no control condition. The authors say so plainly and name regression to the mean, monitoring reactivity, expectancy, history and seasonality as explanations. A d of 0.55 for resilience over 40 days in a largely well population, with no comparison group, is close to uninterpretable as a treatment effect — and the authors do not try to interpret it as one.

A few small reporting slips. The abstract gives the confidence interval as 0.004 to 0.290 while the body text gives 0.01 to 0.29; rounding 0.004 to two decimals gives 0.00, not 0.01, which makes the body version read as more comfortably positive than the data are. The abstract gives the distress effect as d = −0.23 and the body as d = −0.24. And the distal funnel does not close: 49 minus 4 excluded for incomplete baseline is 45, but the paper reports 44. It reconciles only if you route through the 48 who completed the post-assessment (48 − 4 = 44), which the text does not spell out. None of these changes a conclusion. All of them are the kind of thing a careful reader notices and a copy editor should have caught.

**Where it sits on my scale:** 3/5 is where a sound method meets a preliminary result. The grade is about the strength of evidence for the claim, not the quality of the writing — and by that measure the evidence that ML-based assignment improves momentary resilience is weak. What is striking is that the paper's own self-description matches a 3/5 almost exactly. A study that tells you it is preliminary, and is, is far more useful than a study that tells you it is definitive, and isn't.

---

## 4. The Editor's Concerns

If this manuscript crossed my desk, these are the points I would raise.

**No designated primary outcome and no multiplicity handling.** Three proximal outcomes are listed as co-equal objectives. One is positive at p = 0.044. The paper notes "the proximal effect was restricted to one of three proximal outcomes" — good — but never adjusts, and never says which outcome was expected to move. I would ask for the registration record, and failing that I would ask that the resilience finding be described throughout as hypothesis-generating. (To the authors' credit, the abstract and conclusion do call it "an initial, outcome-specific signal," which is close to that.)

**The number of decision points analysed is never reported.** This is the most consequential omission. The design can deliver up to 210 decision points per person, so the natural headline is "thousands of randomisations." But MRT analyses were restricted to interactive/adaptive tasks with a measurement at both ends, and we are never told how many that left. The effective sample size of the primary analysis is therefore not stated. I was able to recover an estimate from the Wilcoxon statistic the authors do report — roughly 950 to 980 intervals, about 23 per person, around 11% of the per-person maximum (method in the Statistics Spotlight). If that is right, the analysis rests on an order of magnitude fewer observations than "210 decision points each" suggests to a casual reader. I would require this number in a table.

**A 3-hour average gap between exercise and measurement, for outcomes that are defined as momentary.** The authors raise this themselves and correctly note it cannot explain the resilience result, because the gap was the same in both conditions. But it does bear on the *negative* findings: a brief breathing exercise plausibly lifts mood for twenty minutes, and a measurement taken a median of 2.4 hours later would miss it entirely. The null results on positive and negative affect are therefore weak evidence of absence. The authors say this too.

**Six participants lost to a server restart.** That is 12% of the randomised sample lost to an infrastructure failure, not to anything about the participants. The authors compared the excluded to the included on baseline characteristics and found no marked differences, while explicitly flagging that this comparison is underpowered. This is handled about as well as it can be after the fact. The right lesson is for the next study's data pipeline, not for this paper's credibility.

**"Feasible" without a definition of feasible.** The paper states outright that "no formal a priori pass/fail thresholds were specified." So the feasibility conclusion is a narrative judgement on numbers that look good rather than a test against a bar set in advance. The numbers genuinely do look good — 98% completed the post-assessment, 10 minutes a day of use — but a feasibility study that can only pass is not really testing anything. I would ask for thresholds in the next protocol.

**Safety on 49 people establishes less than it sounds like.** Zero serious adverse events is reassuring but it is not the same as "safe." With 49 participants, zero events is statistically compatible with a true rate as high as about 6% (see Statistics Spotlight). For a wellness app in a non-clinical population that is a reasonable place to be; it is worth knowing it is the ceiling the data support.

**Generalisability, which the authors address squarely.** 78% female, mostly medium-to-high education, current mental health conditions and current service use excluded. The authors spell out that results "should not be interpreted as evidence for use in psychiatric treatment or crisis intervention contexts," and they go further in the limitations: the model "should not be assumed to identify unobserved latent states, stable patterns of psychological dynamics, deterioration trajectories, or crisis contexts that were absent from the training data." That is an important and unusually responsible thing to put in print. A model trained on your ordinary weeks has no information about your worst night. One genuine strength here: 51% of the sample reported a migration history, which is far better representation than most digital mental health trials achieve.

**Minor:** the gender counts (38 female + 10 male = 48) leave one of 49 participants unaccounted for in the retrieved text, presumably a third category not broken out. And the "36% with moderate or severe distress" does not land on a whole number of participants for a denominator of 49, so the denominator is ambiguous.

---

## 5. Statistics Spotlight

### The micro-randomized trial: randomising moments instead of people

This is the concept worth taking away, and it is new to this reading list.

In an ordinary randomized trial, the coin flip happens once per person. You are assigned to treatment or control and you stay there. The coin's job is to make the two *groups* comparable, so that any later difference between them is attributable to the treatment rather than to who ended up where.

A micro-randomized trial flips the coin at every *opportunity to intervene*. Here: up to seven times a day, for 30 days, in every participant. Each flip decided whether that one moment's exercise came from the model or from a random draw. Every person therefore contributes both conditions, interleaved through their month.

Why this is powerful: **you are comparing a person to themselves, hours apart.** Every stable thing about a participant — their personality, their income, their education, their diagnosis, their baseline gloom, their motivation for signing up — is held constant by construction, because it is the same person on both sides of the comparison. Confounding by baseline differences, the thing that wrecks most observational research and that ordinary randomisation handles only on average, is structurally impossible here. That is a real design achievement, not a technicality.

What it buys you and what it does not: an MRT answers "at a given moment, does this decision rule do better than that one?" It does not answer "should a young person install this app?" For that you need a person-level trial comparing app to no app, which this study did not do and does not claim to have done.

And the thing the design is named for creates its own trap. "Up to 210 decision points per person" sounds like an enormous amount of data, and in one sense it is. But the unit of the *analysis* is the decision point, while the unit of *recruitment* is the person — and the two do not scale together, because observations within one person are correlated. Your thousandth ping from participant 12 tells you much less than a thousandth participant would. This is the unit-of-analysis question that keeps recurring in this reading list, in a new costume: **what is the unit the effect is measured in, and is it the unit the uncertainty is driven by?** Here it is measured in decision points and driven largely by people, which is why 42 participants still leaves this study under-powered despite hundreds of randomisations. The `wcls()` method the authors used exists precisely to handle this — it is weighted and centered least squares, and the "centered" part means the treatment indicator is centered on its randomisation probability, which is what makes the resulting estimate a genuine causal quantity (the "marginal causal excursion effect") rather than an association.

### Recovering a number the paper does not report

The paper never says how many decision points went into the primary analysis. But it reports a Wilcoxon rank-sum test comparing the exercise-to-measurement interval between the two conditions: W = 114,075, p = 0.518.

That statistic is informative. In R, the Wilcoxon W counts the pairs where one group's value exceeds the other's; when the two groups do not differ, it sits near n₁ × n₂ / 2. A p-value of 0.518 means W is almost exactly at that expectation. So:

n₁ × n₂ ≈ 2 × 114,075 = 228,150

Randomisation was 1:1, so the two arms should be about equal. With n₁ = n₂, each is about √228,150 ≈ 478, for a total of about 955 intervals. The estimate is robust to the split: even at a lopsided 40/60 it only moves to about 975.

So the primary analysis rests on roughly **950 to 980 exercise-to-outcome intervals across 42 participants — about 23 per person.** Against a per-person maximum of 210, that is about 11%.

This is a worked example of a habit worth having: **reported test statistics carry information about sample sizes, and you can often back out a number an author left out.** I am flagging clearly that ~955 is my own reconstruction, not a figure the authors published, and that it assumes the standard R convention for W. But it reframes the study. "Up to 210 decision points each" and "about 23 analysed decision points each" are very different studies, and only the second one is what was actually analysed.

### A confidence interval that touches zero

The resilience result: B = 0.147, 95% CI 0.004 to 0.290, p = 0.044.

First, check the interval against itself. Its midpoint is (0.004 + 0.290) / 2 = 0.147 — exactly the point estimate, so the interval is symmetric, as a normal-approximation interval should be. Its half-width is 0.143, so the standard error is 0.143 / 1.96 ≈ 0.073. Then 0.147 / 0.073 ≈ 2.015, and a z of 2.015 corresponds to a two-sided p of 0.0439. The paper says 0.044. **The numbers reproduce exactly**, which is a good sign — the estimate, the interval and the p-value all come from the same calculation and none has been mistyped.

Now read the interval rather than the p-value. The data are consistent with the true effect being anywhere from 0.004 to 0.290 points on a 1-to-7 scale. The lower end, 0.004, is four thousandths of one point. If the truth were at that end, the model's advantage over a coin flip would be invisible to any human being and worth nothing clinically. The p-value of 0.044 tells you only that the interval does not *quite* include zero. It tells you nothing about whether the effect matters, and here the interval explicitly allows for an effect that does not.

This is why the abstract-versus-body discrepancy is worth noticing. The abstract says 0.004 to 0.290. The body says 0.01 to 0.29. But 0.004 rounded to two decimals is 0.00, not 0.01. The body's version makes the lower bound look like a real, if small, positive number. The abstract's version shows it is almost exactly zero. When two parts of a paper disagree, read the one that gives more decimal places.

### Three outcomes, one p-value, no correction

If you test three outcomes at the 0.05 level and nothing is really going on, your chance of at least one "significant" result is not 5% but about 14%. Getting one positive out of three is roughly what chance alone produces.

The standard fixes:
- **Bonferroni:** divide the threshold by the number of tests. 0.05 / 3 = 0.0167. The observed p = 0.044 is well above that. It does not survive.
- **Holm:** order the p-values (0.044, 0.103, 0.839) and compare the smallest to 0.05/3 = 0.0167. It fails at the first step, so the procedure stops and nothing is declared significant.

The paper applies neither, and does not mention multiplicity. It does state that "the proximal effect was restricted to one of three proximal outcomes," which gives a careful reader the information needed to work this out — but the arithmetic is left to the reader, and most readers will not do it.

The honest statement of this finding is: *one of three outcomes showed a small improvement that would not survive correction for having looked at three.* That is not nothing. It is the kind of result that should motivate a larger trial with one nominated primary outcome, which is precisely what the authors call for.

### What under-recruitment cost

The plan: 60 participants gives about 87% power to detect a standardised proximal effect of 0.10, at a one-sided alpha of 0.025.

You can work backwards from that. A one-sided alpha of 0.025 means a critical value of z = 1.96. 87% power means the distribution of the test statistic sits 1.126 above that. So the planned "signal-to-noise" ratio, the non-centrality, was 1.96 + 1.126 = 3.086.

Non-centrality grows with the square root of the sample size. With 42 analysed instead of 60:

3.086 × √(42/60) = 2.582, and power = Φ(2.582 − 1.96) = Φ(0.622) ≈ **73%**

So realised power for the planned effect fell from about 87% to about 73%. (At 49 randomised it would be about 80%.) The study was not hopelessly under-powered — 73% is not catastrophic — but it means roughly a one-in-four chance of missing a real effect of the planned size. That is worth holding alongside the two null findings: they are not strong evidence that the model does nothing for mood.

A caveat on this calculation: it treats the MRT power approximation as scaling with participant count in the usual way. MRT power also depends on the availability rate — how often a decision point is actually eligible — and the paper does not state the rate it assumed. So treat 73% as an approximation, not a precise figure.

### Forecasting performance versus policy value

This is the authors' own distinction and it is the sharpest idea in the paper. It deserves to be a standing question.

The model was trained to do one thing: predict your next few hours of self-reported states. Its loss function was prediction error. It was tuned by minimising prediction error on a separate earlier dataset.

But the model was *used* to do something different: choose an exercise. And what we care about is whether that choice makes you better off.

These come apart. A model can forecast your mood beautifully and still choose badly, because forecasting accuracy says nothing about whether it correctly ranks the eight *interventions* — the counterfactual question "what would happen if I gave you exercise 3 instead of exercise 7?" is not the question "what will your mood be?" Conversely, a mediocre forecaster can make good choices if its errors happen to be uninformative about the ranking.

The authors put this in writing twice, and in the paper's own words: the prediction objective "was used as a pragmatic proxy for model selection; it does not establish that the forecasting objective is optimally aligned with the causal effect of the assignment policy." So the MRT evaluated **the policy**, not the model. That is the right thing to have evaluated — the policy is what touches the user — but it means a positive result does not validate the forecasting, and a null result would not have invalidated it.

The general lesson, and it applies far beyond this paper: **when an AI system is trained on one objective and deployed to make a decision, ask which one was actually measured.** Papers that report "the model achieved AUC 0.91" have measured the first thing. Papers that report "patients assigned by the model did better" have measured the second. The gap between them is where most of the disappointment in medical AI lives.

### Uncontrolled before-and-after, and why Cohen's d does not rescue it

The distal results — distress d = −0.24, resilience d = 0.55, adaptive emotion regulation d = 0.53 — come from paired t-tests comparing each person's score after to their score before. There is no control group at all for these.

Cohen's d expresses a difference in standard deviations: 0.2 is conventionally small, 0.5 medium, 0.8 large. So d = 0.55 for resilience looks like a decent, medium improvement.

But d measures the *size* of a change, not its *cause*. In an uncontrolled before-and-after design, everything that happens over 40 days is baked into that number:

- **Regression to the mean.** People sign up for mental health studies when they are not feeling great. Feeling-not-great fluctuates. Measure them again six weeks later and some will have drifted back toward their own average regardless of what you did.
- **Monitoring reactivity.** Being asked about your mood six times a day for 40 days is itself an intervention.
- **Expectancy.** People who volunteered for a mental-wellness app expect to feel better.
- **Season and history.** July-to-February in Germany is a long run of changing daylight and changing life circumstances.

The authors name every one of these — regression to the mean, monitoring reactivity, expectancy, history, seasonal influences, spontaneous change — and conclude the analyses "were descriptive and should not be interpreted as causal intervention effects." They are right, and the discipline is worth imitating. If a paper reports a before-and-after effect size with no control group and *does not* say this, that silence is the finding.

### The rule of three: what zero adverse events means

No serious adverse events were recorded in 49 participants. What does that establish?

The rule of three: if you observe zero events in n people, the 95% upper confidence bound on the true rate is roughly 3/n. Here 3/49 ≈ 6.1%. The exact binomial calculation, 1 − 0.05^(1/49), gives 5.93%.

So "no serious adverse events in 49 young people" is fully consistent with a true serious-adverse-event rate of up to about 6%. It rules out a common harm. It does not rule out an uncommon one.

For a wellness app in a non-clinical population, that is an appropriate amount of reassurance for this stage, and the authors use the right word — "preliminary safety." The number to remember is that **a zero in a small study is a weak zero**, and the rule of three tells you exactly how weak in one division.

---

## 6. Jargon Translator

**Ecological momentary intervention (EMI)** — A short mental-health exercise delivered to your phone in the middle of ordinary life rather than in a clinic. "Ecological" means in your real environment; "momentary" means right now.

**Ecological momentary assessment (EMA)** — The measurement version of the same idea: your phone asks how you are feeling, repeatedly, during your normal day, instead of asking you to remember last month in a questionnaire.

**Just-in-time adaptive intervention (JITAI)** — The broader framework: an intervention that tries to reach you at the moment you can use it, adapting to your changing state and situation.

**Micro-randomized trial (MRT)** — A trial that randomises *moments* rather than people, over and over inside each participant, to test which decision rule works better at the moment of decision.

**Decision point** — One occasion when the app could deliver an exercise. Here, up to seven a day for 30 days.

**Proximal outcome** — What happens shortly after the intervention; in this study, a few hours later. Contrast with **distal outcome**, measured at the end of the whole programme.

**Time-lagged** — The outcome is measured at the *next* occasion, not the same one. This matters for causal ordering: the exercise came first, the measurement came after, so the measurement cannot have caused the exercise.

**Marginal causal excursion effect** — The specific causal quantity an MRT estimates: on average across people and moments, how much better off are you at the next measurement because the model chose rather than the coin? "Excursion" because you briefly depart from the comparison policy at one decision point and then return.

**Weighted and centered least squares (wcls)** — The method used to estimate that effect. "Centered" means the treatment indicator is adjusted around its known randomisation probability, which is the trick that makes the estimate causal. "Weighted" handles the repeated observations within each person.

**Recurrent neural network (RNN)** — A model with memory. Each prediction depends on an internal state carried forward from earlier inputs, which is what lets it learn patterns that unfold over time rather than treating each moment in isolation.

**Dynamical systems reconstruction (DSR)** — Fitting a model that reproduces the *shape of the motion* in a time series — the way a person's states push on each other and evolve — rather than just predicting the next value.

**Latent state** — The model's internal, unobserved summary of where you are right now. Not directly measured; inferred from your answers.

**Generalized teacher forcing** — A training technique that feeds the model some real observed values during training to stop its predictions from drifting away and destabilising learning.

**Softmax, temperature β** — A way of turning scores into probabilities that sum to 1. The temperature controls how decisive it is: low temperature means nearly always pick the top-scoring option; high temperature spreads the probability out. At β = 1 the policy favoured the predicted-best exercise while still sometimes choosing others.

**Active control condition** — A comparison group that gets something real, not nothing. Here, randomly chosen exercises. This makes the test harder and the result more meaningful.

**McDonald's ω (omega)** — A measure of whether several questions intended to capture one thing actually hang together. Above about 0.8 is good. Not computable on a single question, which is why momentary resilience has none.

**K10** — Kessler Psychological Distress Scale, 10 items, a standard screening measure of general distress.

**CERQ** — Cognitive Emotion Regulation Questionnaire, separating adaptive strategies (such as reframing) from maladaptive ones (such as rumination).

**CD-RISC** — Connor-Davidson Resilience Scale.

**MARS / MAUQ** — Mobile App Rating Scale and mHealth App Usability Questionnaire; standard instruments for app quality and usability.

**Care as usual (CAU)** — Participants kept whatever support they already had; the app was added on top, not substituted for it.

**Cohen's d** — A change expressed in standard deviations. Roughly: 0.2 small, 0.5 medium, 0.8 large.

**Bonferroni and Holm corrections** — Two ways of raising the bar when you test several outcomes, so that looking in many places does not manufacture a false positive.

**Regression to the mean** — The tendency for extreme measurements to be closer to average when you measure again, purely because part of the first extreme reading was chance.

**Rule of three** — If you see zero events in n people, the true rate could still be as high as about 3/n.

---

## 7. What You Can (and Can't) Say

**You CAN say:**
- "In a German trial of a mental-wellness app for young people, letting a machine learning model choose which exercise to deliver produced a small improvement in one measure of momentary resilience compared with choosing at random, and no improvement in mood."
- "The design randomised moments within each person rather than randomising people, which is a strong way to rule out differences between participants."
- "The comparison was against randomly chosen real exercises, not against nothing — a harder and more informative test."
- "The app was feasible and showed no serious adverse events in 49 participants."
- "The researchers themselves describe this as an initial signal needing replication in a larger, properly powered trial."
- "This was an addition to whatever support participants already had, in young people without a current mental health condition."

**You CAN'T say:**
- ❌ "AI personalisation improves youth mental health." One of three short-term measures moved, by an amount whose confidence interval reaches essentially zero, in 42 people.
- ❌ "This app reduces psychological distress." The distress improvement comes from a before-and-after comparison with no control group. The authors explicitly decline to read it causally, and so should you.
- ❌ "The AI was validated." The trial tested the *policy* — what the model chose — not the model's forecasting accuracy. The authors draw this distinction themselves.
- ❌ "The effect was statistically significant, so it's real." At p = 0.044 across three outcomes with no correction, it would not survive Bonferroni or Holm.
- ❌ "This works for people with depression or anxiety." Anyone with a current mental health condition or currently using services was excluded by design.
- ❌ "The app can detect a crisis." The authors state the opposite in print: a model trained on your observed ordinary states should not be assumed to recognise deterioration or crisis contexts that were absent from its training data.
- ❌ "Thousands of randomisations make this a large study." The design allows up to 210 decision points per person, but the analysed sample appears to be about 23 per person, and uncertainty is driven mainly by the 42 participants.
- ❌ "This generalises to young people in general." 78% female, mostly medium-to-high education, self-selected volunteers. Representation of people with a migration history was genuinely good (51%); gender and education were not.

---

## 8. Bottom Line for Your Life

If you are a young person wondering whether to install an app like this: nothing here tells you whether the app helps, because the study never compared app to no app. What it tells you is that a machine learning model choosing your exercises is, at most, slightly better than a shuffle — and possibly not better at all. If you like one of these apps and it costs you nothing, the evidence gives no reason to avoid it and no reason to expect much. Notably, when participants were asked whether they would pay for it, the ratings were "more mixed" than their other ratings.

If you are a parent or a counsellor: this is mental health *promotion* for young people who are broadly doing okay. It is not treatment, and everyone with a current condition or current service use was deliberately excluded. The authors are unusually clear that this should not be read as evidence for psychiatric treatment or crisis support, and that the model cannot be expected to spot a crisis it has never seen.

If you are reading medical AI papers: take two things from this one.

First, the distinction between **forecasting performance and policy value**, because the authors state it better than most methodologists do. A model that predicts well has not been shown to decide well. Next time you read "our model achieved AUC 0.93," ask whether anyone tested what happened to the people whose care it steered.

Second, how to read a thin positive result. The p-value said 0.044, which clears the conventional bar. The confidence interval said 0.004 to 0.290, which tells you the effect might be nothing. The outcome count said one of three with no correction, which tells you chance alone produces this about one time in seven. None of that makes the study bad. It makes the study *preliminary* — and the paper says so, repeatedly, in its own words.

That last point is the real reason this one is worth your time. The authors had a positive headline available to them and declined to oversell it. They listed the alternative explanations for their own finding before a critic could. They refused to interpret their own before-and-after improvements causally. They told the reader what their model cannot do. When you are learning to appraise papers, it helps enormously to have seen what honest reporting of a modest result looks like — so you can notice when a paper claiming far more has done far less.

---

*This is an educational analysis of a published scientific paper, not medical advice. Nothing here is a recommendation about your own mental health care. If you are a young person struggling, talk to someone — a GP, a counsellor, or a crisis line in your country.*
