# A Million People, a Perfectly Calibrated Model, and Almost Nothing to Act On

**Paper:** A Machine Learning–Derived Risk Scorecard for Pneumonia
Hospitalization in Japanese Old-Old Adults
**Authors:** Shimizu A, Kamiya H, Tanabe M, Sakamoto R, Matsui H, Momosaki R
**Venue / Year:** Geriatrics & Gerontology International, 2026;26(10):e70850
**DOI:** https://doi.org/10.1111/ggi.70850
**PubMed:** https://pubmed.ncbi.nlm.nih.gov/42781887/
**Full text used:** https://pmc.ncbi.nlm.nih.gov/articles/PMC13602450/
**Basis of this analysis:** FULL TEXT (PubMed Central open-access copy,
retrieved 2026-10-01). Figures 1–8 and the 17 supplementary tables were not
retrievable; nothing here depends on a figure value. The complete 17-feature
scorecard, including every point assignment, is reproduced in the article body
and was read in full.
**Date decoded:** 2026-10-01
**Evidence grade:** 4/5

---

# The Gist

Pneumonia puts a lot of very old people in hospital, and surviving it often
leaves them weaker than before. So it would be useful to know, at the annual
health check, which 80-year-olds are heading for a pneumonia admission — early
enough to do something about the fixable parts: dental care, vaccination,
swallowing assessment, exercise.

A Japanese team had an unusually good shot at this. Japan runs a mandatory
15-question health check for everyone aged 75 and over, and it links to national
insurance claims. That gave them **1,098,404 people** — over a million — with a
questionnaire, a medication list, a comorbidity score, and a year of follow-up.

They built two models. A heavyweight ensemble of 20 different algorithms, and a
deliberately simple scorecard: 17 questions, each worth one or two points, total
0 to 21, the kind of thing you could print on a card. The ensemble scored 0.823
on the standard discrimination measure; the scorecard 0.786. People in the
top band had a **15.9 times higher** rate of pneumonia admission than the bottom
band.

That all sounds like a success, and in one specific and genuinely impressive
sense it is: the scorecard's *calibration* is close to perfect. When it says 2%,
about 2% of those people get admitted. Most published risk models never check
this, and many that do fail it.

Here is the problem, and the authors are honest about it. Only **4,525 of
1,098,404 people — 0.41% — were hospitalised for pneumonia** in the year. At
that base rate, a 15.9-fold gradient means moving from 0.12% to 1.91%. So of
every 100 people the scorecard flags as **high risk, about 98 will not be
hospitalised for pneumonia that year.** The authors report a "scaled Brier
score" of **0.7%** — their own estimate that the scorecard explains under one
percent of the uncertainty about who gets pneumonia.

And the most sobering number in the paper: in the same population over the same
year there were **18,138 deaths from something other than pneumonia** — four
times as many as the pneumonia admissions the model was built to predict.

# Study Snapshot

- **Study type:** Retrospective cohort study developing and **internally**
  validating a clinical prediction model. No external validation, which the
  authors state repeatedly and treat as a precondition for use.
- **Data source:** The JMDC Old-Old Medical Claims Database, drawn from Japan's
  Late-Stage Medical Care System — the national insurance scheme for people aged
  75 and over. Includes the mandatory health check, inpatient and outpatient
  claims, and prescriptions.
- **Participants:** **1,098,404** community-dwelling adults aged 75 or older who
  completed the 15-item Questionnaire for Medical Checkup of Old-Old between
  April 2020 and March 2024. Mean age 80.6 years (SD 5.0), 40.3% male, mean BMI
  22.8 (SD 3.4).
- **Who was excluded:** Anyone with a previous pneumonia hospitalisation or a
  feeding tube, on the grounds that their risk is already known to be high.
  Anyone missing age, sex or BMI. For people with several health checks, only
  the first was used.
- **Outcome:** First hospitalisation for pneumonia within 365 days, identified
  by ICD-10 codes J12–J18 and J69 recorded as the **admission-triggering
  diagnosis** — not as a secondary code, specifically to avoid counting
  pneumonia caught in hospital.
- **Events:** **4,525 (0.41%)** — 3,166 of 768,880 in the training set, 1,359 of
  329,524 in the test set.
- **Predictors:** 20 candidates — all 15 questionnaire items plus age, sex, BMI,
  Charlson comorbidity index, and number of distinct prescribed medications.
- **The two models:** A **Super Learner** ensemble combining 20 base learners
  (penalised regression, gradient boosting, random forests, splines, neural
  networks and others) by non-negative least squares with 10-fold
  outcome-stratified cross-validation. And, developed **independently**, a
  17-feature integer scorecard scored 0–21.
- **A notable deliberate choice:** With an event rate of 0.41% they
  **deliberately did not rebalance the classes** — no oversampling, no class
  weighting, no SMOTE — because "artificial rebalancing can inflate baseline
  risk and impair the calibration of clinical risk-prediction models."
- **Performance (test set):** Super Learner AUC **0.823** (95% CI 0.812–0.834),
  Brier 0.0041, calibration slope **1.101**, calibration-in-the-large
  **−0.002**. Scorecard AUC **0.786** (0.774–0.798), Brier 0.0041, calibration
  slope **1.017**, calibration-in-the-large **−0.001**. The ensemble beat the
  scorecard by 0.037 AUC (95% CI 0.030–0.044).
- **Risk bands (test set):** low 0–6 points, 183,340 people (55.6%), event rate
  **0.12%**; moderate 7–10, 116,631 (35.4%), **0.49%**; high ≥11, 29,553
  (9.0%), **1.91%**. A 15.9-fold gradient.
- **Operating points:** score ≥7 flags 44.4% and captures 83.8% of events,
  positive predictive value 0.78%, number needed to screen 128. Score ≥11 flags
  9.0% and captures 41.6%, positive predictive value 1.91%, number needed to
  screen 52.
- **Reporting standards:** TRIPOD and the TRIPOD+AI extension.
- **Ethics:** Review waived — the database is fully anonymised.
- **Funding:** Okasan Kato Culture Promotion Foundation (grant 2025-1-30) and
  JSPS KAKENHI (JP25K02851). The paper states the funders had no role in design,
  analysis or the decision to publish.
- **Conflicts of interest:** **"The authors declare no conflicts of interest."**

# How Strong Is This Evidence? — Grade 4/5

**What this study did well**, and the list is long:

- **It refused to rebalance a rare outcome, and said why.** This is the single
  most quietly impressive decision in the paper. Faced with 0.41% events, the
  standard move is to oversample the rare class to make the model "learn
  better." These authors declined, on the explicit grounds that rebalancing
  destroys calibration. That is correct, it is rarely done, and it is why the
  rest of the paper's numbers mean something.
- **It treated calibration as the primary concern**, stating that performance
  was evaluated "with emphasis on calibration for clinical safety," and it
  reported both calibration slope and calibration-in-the-large for every model
  and subgroup.
- **It built an interpretable model deliberately and independently**, rather than
  approximating the black box afterwards — and then reported honestly that the
  simple version loses 0.037 AUC while **improving** calibration.
- **It reported the scaled Brier score** — 1.3% for the ensemble, 0.7% for the
  scorecard — which is the number that most undercuts its own headline, and
  almost no prediction paper reports.
- **It ran a competing-risk analysis**, comparing Aalen–Johansen cumulative
  incidence against the Kaplan–Meier complement, and tested robustness by
  assigning each death to the start, middle and end of its month.
- **It re-evaluated the models in the full eligible cohort** using
  inverse-probability-of-censoring weighting, and reported that the excluded
  decedents "were markedly frailer than included individuals."
- **It reported where the model fails** — AUC falling to 0.670 and calibration
  collapsing in the over-90s, and calibration drifting in the pandemic year.
- **It declined to endorse its own thresholds:** "Neither threshold is endorsed
  for clinical use without external validation," and the cutpoints "were not
  prespecified clinical thresholds."
- **It refused a causal reading of its own predictors:** they "are prognostic
  markers rather than causal or modifiable intervention targets," and medication
  count "may reflect comorbidity and health care utilization rather than
  biological risk."
- **It followed TRIPOD+AI and declared funding and conflicts.**

**Why it is a 4 and not a 5:** there is no external validation, which the
authors name as essential. And the abstract leads with a 15.9-fold gradient
without the absolute risks beside it — a relative figure that will travel far
better than the 1.91% it is built from. Everything else in this paper argues
against reading it that way; the abstract does not.

# The Editor's Concerns

Almost every concern below is one the authors raise themselves. What follows is
mostly arithmetic they invite the reader to do.

**Ninety-eight of every hundred "high-risk" people will be fine.** *Deriving*
from the paper's own figures: at a score of 11 or more, 29,553 test-set people
are flagged, and the positive predictive value is 1.91%. So roughly **564 of
them are hospitalised for pneumonia and roughly 28,989 are not.** The paper
states this as a number needed to screen of 52 — you must flag 52 people to find
one who will be admitted. Whether that is worth doing depends entirely on how
cheap and harmless the resulting intervention is. For a dental check or a
vaccination reminder, 52 is plausibly fine. For anything invasive, frightening,
or expensive, it is not.

**The broad threshold is worse on this measure, and better on another.** At a
score of 7 or more the model flags **44.4% of the entire population** — about
146,000 of 329,524 test-set people — to capture 83.8% of events. *Deriving*: at
a positive predictive value of 0.78%, that is roughly 1,141 true cases against
roughly **145,167 false alarms**, and a number needed to screen of 128. You can
have sensitivity or you can have precision. At a 0.41% base rate you cannot have
both, and no amount of modelling changes that.

**Even the high-risk flag misses most of the cases.** *Deriving*: a score of 11
or more captures 41.6% of events, which means roughly **794 of the 1,359
pneumonia admissions happen in people the scorecard did not call high risk.**
A screening tool that misses 58% of events is not a safety net.

**The 15.9-fold gradient is a relative number hiding tiny absolute ones.** It is
the ratio of 1.91% to 0.12%. *Deriving*: the absolute gap is **1.79 percentage
points**, and 99.88% of the low-risk group and 98.09% of the high-risk group
have no event. "Sixteen times the risk" and "under two percent either way" are
the same fact. The first is what gets quoted.

**The authors' own scaled Brier score is the most honest number in the paper,
and it is buried in the limitations.** They report "small positive scaled Brier
scores (1.3% ensemble; 0.7% integer score)." A scaled Brier score measures how
much of the outcome's uncertainty the model removes compared with just
predicting the average risk for everybody. **0.7% means the scorecard removes
under one percent of it.** Set that beside an AUC of 0.786 and you have the
clearest demonstration in this reading list of how differently those two
measures behave when an outcome is rare.

**The model works worst exactly where the risk is highest.** AUC by age:
0.752 for 75–79, 0.743 for 80–84, 0.723 for 85–89, and **0.670 for 90 and over**
— and that oldest group has an event rate of 1.52%, *deriving*, **3.7 times the
overall rate**. Worse, calibration in the over-90s falls apart: slope **0.452**
against an ideal of 1.0, and calibration-in-the-large **+0.586**, meaning the
model systematically under-predicts their risk. The authors state plainly that
"independent validation with age-specific recalibration remains necessary before
clinical use in people aged ≥ 90 years."

**The thing most likely to happen to these people is not pneumonia.** In the
full eligible cohort of 1,286,990, there were 4,525 pneumonia hospitalisations
and **18,138 deaths from something else** — *deriving*, **4.0 times as many**.
Cumulative incidence: 1.53% for death versus 0.38% for pneumonia. The paper
handles this properly with a competing-risk analysis and finds the incidence
estimate barely moves. But it reframes the clinical question: a tool that
stratifies 80-year-olds by pneumonia risk is sorting them on the fourth-most-
likely thing to happen to them.

**Calibration drifted badly in one pandemic year.** Event rates by fiscal year
ran 0.37%, 0.39%, **0.66%**, 0.39%, and the 2022 calibration-in-the-large was
**+0.796** — substantial under-prediction. Discrimination held up (AUCs 0.803,
0.787, 0.810, 0.779) while calibration did not, which is itself the lesson: the
two can come apart, and the one that breaks first is the one that matters for
telling a patient a number.

**The people screened are the healthier ones.** This is a voluntary annual
health check. The authors note that "health checkup attendees may be healthier
than non-attendees, limiting generalizability to frailer or homebound
populations" — and their own sensitivity analysis confirms the excluded
decedents "were markedly frailer." The frailest people, who most need this, are
least likely to be in the data.

**The predictors are self-reported and the obvious ones are missing.** Chewing
difficulty, swallowing difficulty, memory complaints and going-out frequency all
come from a questionnaire the person fills in. And the paper notes that
"vaccination status, oral hygiene, and nutritional intake were unavailable" —
meaning the three things you would most want to act on are the three things not
measured.

**One outcome code is weaker than the others.** The authors flag that "the lower
PPV of ICD-10 code J69 than J12–J18 may have caused outcome misclassification."
J69 is pneumonitis from inhaling food or liquid — aspiration pneumonia — which
is precisely the mechanism the chewing and swallowing questions are meant to
capture. Noise in that code is noise in the most mechanistically interesting
part of the model.

**And a detail that complicates the denominator.** Among people *without* the
primary outcome, 119,378 (10.9%) had a different all-cause hospitalisation. So
the model is separating "admitted for pneumonia" from a background in which one
person in nine is admitted for something else.

# Statistics Spotlight

## Concept 1 — Calibration: the measure that decides whether a number means anything

This reading list has mentioned calibration once in passing. This paper is the
right place to teach it properly, because it is one of the few that treats it as
the main event.

**The distinction.** Discrimination and calibration are different things, and a
model can have one without the other.

**Discrimination** asks: can the model put people in the right *order*? That is
what AUC measures — the chance that a randomly chosen person who gets pneumonia
scored higher than a randomly chosen person who doesn't. It cares only about
ranking.

**Calibration** asks: are the model's *numbers* true? If it tells a thousand
people "your risk is 2%," do about twenty of them get pneumonia?

You can rank perfectly and be numerically absurd. A model that assigns everyone
exactly ten times their real risk has the identical AUC to the correct model —
the ordering is untouched — while telling every patient something false. For
ranking a waiting list, discrimination is enough. For saying a number out loud
to a person, calibration is the whole thing.

**The two numbers this paper reports, and what they mean.**

**Calibration slope.** Plot predicted risk against observed risk and fit a line.
Perfect is **1.0**. Below 1 means predictions are too spread out — the model is
overconfident, calling high risks too high and low risks too low, the classic
signature of overfitting. Above 1 means predictions are too bunched together.

- Scorecard: slope **1.017**. Almost exactly 1. Excellent.
- Super Learner: slope **1.101**. Slightly bunched, still good.
- **Over-90s: slope 0.452.** Less than half. The model's predictions for the
  oldest group are wildly over-spread — it is confidently sorting people whose
  real risks are much closer together than it claims.

**Calibration-in-the-large.** Is the model's *average* prediction right? Perfect
is **0**. Negative means it over-predicts overall; positive means it
under-predicts.

- Scorecard: **−0.001**. Essentially perfect.
- **Over-90s: +0.586.** Systematically under-predicting the risk of the group
  whose risk is highest.
- **Pandemic year 2022: +0.796.** Under-predicting during the year when events
  actually rose to 0.66%.

**An everyday version.** Two weather forecasters. The first says 70% chance of
rain on days it rains and 30% on days it doesn't — but when she says 70%, it
rains 95% of the time. Her ranking is flawless; her numbers are useless for
deciding whether to carry an umbrella. The second's days-it-rains and
days-it-doesn't predictions overlap more, but when he says 70%, it rains about
70% of the time. For planning, you want the second. Calibration is whether the
number on the label matches what is in the tin.

**Why it is usually missing.** Calibration is unglamorous — it produces no
single impressive figure and it can only make a model look worse. Rebalancing
the data to help a model "learn" a rare outcome destroys it outright, which is
why these authors' refusal to rebalance is the reason their calibration numbers
exist at all.

**Watch out for:** any risk calculator that gives you a percentage without a
calibration statistic anywhere in its paper. An uncalibrated model's percentage
is a ranking in disguise, and rankings do not belong in sentences that start
"your risk is." And watch for calibration reported only overall: here the
headline slope of 1.017 conceals a slope of 0.452 in the group the tool would
most often be pointed at.

## Concept 2 — Why a good AUC and a useless model are compatible when the outcome is rare

AUC 0.786 is conventionally "good." The scaled Brier score is 0.7%. Both are
correct. Understanding why is the most practically valuable thing in this paper.

**AUC does not know the base rate.** It is computed by pairing up every case
with every non-case and asking how often the case scored higher. That question
has nothing to do with how many cases there are. Make the disease a hundred
times rarer and the AUC does not budge — but the usefulness of the model
collapses.

**Where the usefulness goes.** Positive predictive value — of the people you
flag, how many actually have the outcome — depends brutally on prevalence.

Work it with this paper's numbers. Among the 29,553 highest-scoring people,
1.91% are hospitalised for pneumonia. That means for every person the model
correctly identifies, it also flags **about 51 who will be fine**. The model has
ranked them correctly; the trouble is that even the top 9% of a very-low-risk
population is still a very-low-risk population.

**A tiny worked example.** Imagine a disease affecting 1 person in 1,000, and a
test so good it flags 90% of cases while wrongly flagging only 5% of healthy
people. Test 10,000 people: 10 have the disease and 9 are flagged; 9,990 are
healthy and about 500 are flagged anyway. So 509 people get a positive result
and 9 of them have the disease — under **2%**. That test has excellent
sensitivity, excellent specificity, and a positive result that is wrong 98% of
the time. Nothing is broken. The base rate is simply doing the work.

**The scaled Brier score is the honest summary.** The plain Brier score is the
average squared error of the predicted probabilities — here 0.0041, which looks
tiny until you realise that always predicting 0.41% for everyone would also
score about 0.0041. The *scaled* version expresses the improvement over that
do-nothing baseline as a percentage, and the authors report **0.7%** for the
scorecard. That is the model's actual contribution to knowing who gets
pneumonia: under one part in a hundred.

**Watch out for:** AUC quoted alone for anything rare — rare diseases, suicide,
violence, fraud, readmission, equipment failure. Always ask three further
questions: *what is the base rate?*, *of the people flagged, what fraction
actually have the outcome?*, and *how much better is this than predicting the
average for everyone?* If a paper reports only AUC, those answers are being
withheld, usually not deliberately. This paper supplies all three, which is why
it earns a 4 despite them being unflattering.

## Concept 3 — Competing risks: when something else happens first

This one changes how you read the whole paper, and it is new to this list.

**The problem.** You are predicting who gets pneumonia within a year. But some
people die of a heart attack in month three. They cannot get pneumonia any more
— the opportunity is gone. They are not "still at risk but unobserved." They are
permanently out.

**Why ordinary methods get this wrong.** The standard Kaplan–Meier approach
treats people who leave the study as **censored**, which quietly assumes they
would have carried the same risk had they stayed. That assumption is fine for
someone who moves to another city. It is false for someone who has died. Treat
death as censoring and you **overestimate** how much pneumonia the surviving
population would have had.

**The right tool** is the **Aalen–Johansen estimator**, which counts each
competing event explicitly and asks: of everyone who started, what fraction
actually experienced pneumonia — as opposed to dying first, or neither.

**What this paper found.** In the full eligible cohort of 1,286,990 there were
4,525 pneumonia hospitalisations and **18,138 non-pneumonia deaths** within the
year. Cumulative incidence: **1.53% for death, 0.38% for pneumonia.** Then:

- Aalen–Johansen pneumonia incidence: **0.378%** (95% CI 0.367–0.389)
- Kaplan–Meier complement (death treated as censoring): **0.381%**
  (0.370–0.392)

A difference of **0.003 percentage points**. They then stress-tested it by
assigning each death to the beginning, middle and end of its month, and got
0.354% to 0.378%. So here, handling competing risk properly changed essentially
nothing — and we only know that *because they checked*.

**Why it matters anyway, and this is the part worth keeping.** The competing-risk
analysis barely moved the incidence estimate, but it revealed something more
important: for this population, **death from something else is four times more
likely than the outcome being predicted.** A tool that sorts 80-year-olds by
pneumonia risk is sorting them on a relatively unlikely event, and the people it
scores highest are also the people most likely to die of something else first.
That is not a statistical artefact to be adjusted away. It is a fact about what
matters to these patients, and it is an argument for predicting a composite
outcome — death, hospitalisation, functional decline — rather than one named
disease.

**An everyday version.** You want to know what fraction of a fleet of 20-year-old
cars will need a new gearbox this year. Some will be written off in crashes
first. Count the write-offs as "we lost track of them" and you will overstate
gearbox failures among the ones still on the road. And if four times as many get
written off as need gearboxes, a gearbox-failure predictor is answering a
narrower question than the fleet manager is asking.

**Watch out for:** any survival or time-to-event analysis in an elderly or
seriously ill population that does not mention competing risks. The tell is a
paper reporting Kaplan–Meier curves for a non-fatal outcome in people with high
mortality. Ask: *what else could have happened to these people first, and how
often did it?* And then ask the harder question these authors' own numbers
raise: *is the outcome being predicted the one that matters most?*

# Jargon Translator

- **Super Learner:** A method that fits many different models — here 20,
  including penalised regressions, gradient boosting, random forests, splines
  and neural networks — and finds the best weighted blend of them, rather than
  picking a single winner.
- **Risk scorecard:** A points table. Each risk factor is worth a fixed number of
  points, you add them up, and the total maps to a risk. Old-fashioned,
  transparent, needs no software.
- **AUC:** The chance the model scores a person who gets the outcome above one
  who doesn't. 0.5 is a coin flip. Measures ranking only, and is blind to how
  rare the outcome is.
- **Calibration slope:** Whether predicted risks are appropriately spread out.
  1.0 is perfect; below 1 means overconfident.
- **Calibration-in-the-large:** Whether the average prediction is right. 0 is
  perfect; positive means under-predicting.
- **Brier score:** Average squared error of the predicted probabilities. Looks
  impressively small whenever the outcome is rare, which is why the scaled
  version matters more.
- **Scaled Brier score:** How much better the model is than simply predicting the
  average risk for everyone, as a percentage. **0.7% here.**
- **Platt scaling:** A method for correcting a model's raw output so the numbers
  behave like real probabilities.
- **Positive predictive value:** Of the people flagged, the fraction who actually
  have the outcome. 1.91% in the high-risk band.
- **Number needed to screen:** How many people you must flag to find one true
  case. 52 at the high threshold, 128 at the broad one.
- **Competing risk:** Another event — here, death from another cause — that
  removes someone from being able to have the outcome at all.
- **Aalen–Johansen estimator:** The correct way to estimate cumulative incidence
  when competing events exist.
- **Inverse-probability-of-censoring weighting:** Re-weighting the people you
  still have to stand in for those you lost, so the analysis reflects the
  original population.
- **Charlson comorbidity index:** A standard score summing up how many serious
  chronic conditions someone has.
- **Decision curve analysis:** A way of asking whether acting on a model beats
  treating everyone or treating nobody, across the range of thresholds a
  clinician might plausibly use.
- **TRIPOD / TRIPOD+AI:** The reporting checklists for clinical prediction
  models. Following them is why this paper's weaknesses are visible.

# What You Can (and Can't) Say

**Fair to say:**

- In 1,098,404 Japanese adults aged 75 and over, 4,525 (0.41%) were hospitalised
  for pneumonia within a year.
- A 20-learner ensemble reached AUC 0.823 (95% CI 0.812–0.834) and a 17-item
  points scorecard 0.786 (0.774–0.798) on a held-out 30% test set.
- The scorecard was **very well calibrated** — slope 1.017,
  calibration-in-the-large −0.001 — and was better calibrated than the ensemble
  despite scoring lower on discrimination.
- The authors deliberately did not rebalance the rare outcome, specifically to
  protect calibration.
- Risk bands ran 0.12%, 0.49% and 1.91%, a 15.9-fold gradient between lowest and
  highest.
- At the high threshold, 9.0% of people are flagged, 41.6% of events are
  captured, the positive predictive value is 1.91%, and the number needed to
  screen is 52.
- Performance degraded with age, reaching AUC 0.670 in the over-90s, where
  calibration also broke down (slope 0.452, calibration-in-the-large +0.586).
- Non-pneumonia death was four times more common than the predicted outcome
  (18,138 versus 4,525), though handling it as a competing risk changed the
  incidence estimate by 0.003 percentage points.
- The authors report a scaled Brier score of 0.7% for the scorecard.
- **The model has not been externally validated**, and the authors state that
  neither threshold is endorsed for clinical use without it.

**Not fair to say:**

- ~~"AI predicts pneumonia in the elderly with 82% accuracy."~~ AUC is not
  accuracy, and at a 0.41% event rate it does not describe usefulness.
- ~~"High-risk patients are 16 times more likely to get pneumonia."~~ True, and
  it means 1.91% versus 0.12%. Both are small.
- ~~"The scorecard identifies elderly people at risk of pneumonia."~~ It flags
  groups in which roughly 1 in 52 will be admitted, and it misses about 58% of
  cases.
- ~~"This tool is ready for use in health checkups."~~ Internal validation only.
  The authors say prospective validation and clinical-impact assessment are
  needed first.
- ~~"It works especially well in the very old."~~ It works **worst** there —
  AUC 0.670 with badly broken calibration — and the authors say it should not be
  used in the over-90s without recalibration.
- ~~"The simple scorecard is as good as the AI."~~ It is 0.037 AUC worse (95% CI
  0.030–0.044) and better calibrated. Different trade-off, not equivalence.
- ~~"Chewing and swallowing problems cause pneumonia admissions."~~ The authors
  explicitly call their predictors "prognostic markers rather than causal or
  modifiable intervention targets."

# Bottom Line for Your Life

**If you are ever given a risk percentage — by a doctor, an app, an insurer —
the question that matters is whether anyone checked that the number is true.**
That check is calibration, and this paper is the rare one that leads with it. A
model can sort people into the right order while every number it prints is
wrong, and the ordering is what AUC measures. "Your ten-year risk is 12%" is
only a meaningful sentence if, among people told 12%, about 12 in 100 had the
event. Ask whether the calculator's paper reports a calibration slope. Most
don't.

**The second habit is to convert every relative risk into an absolute one before
you react to it.** "Sixteen times the risk" is the sentence that will be quoted
from this study. "1.91% versus 0.12%" is the same finding. The ratio is designed
to be alarming and the percentages are designed to be ignored, and the
percentages are what tell you whether to change anything. The arithmetic takes
ten seconds and it almost always deflates the headline.

**And notice the question this paper quietly asks about itself.** Its authors
built a careful, honest, well-calibrated model on a million people — and their
own numbers show it removes under 1% of the uncertainty about who gets
pneumonia, while four times as many people in the same population die of
something else entirely. That is not a failure of the modelling. It is what
happens when you aim very good methods at a rare outcome in a population where
many things are happening at once. The useful lesson is not "prediction doesn't
work." It is that **the hardest part of a prediction problem is choosing what to
predict**, and that a model can be technically excellent and still be pointed at
the wrong question.

---

*Education, not medical advice. Decoded 2026-10-01 from the PubMed Central
open-access full text. Derived calculations — the false-alarm counts at each
threshold, the number of events missed by the high-risk flag, the absolute gap
behind the 15.9-fold gradient, the ratio of competing deaths to pneumonia
events, and the comparison of the over-90s event rate against the overall rate —
are labelled as derived and were computed from the paper's own reported values.*
