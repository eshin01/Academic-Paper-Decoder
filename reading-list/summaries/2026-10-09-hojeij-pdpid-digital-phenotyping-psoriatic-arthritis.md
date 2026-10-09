# The Measurement Question Almost Nobody Asks

**Paper:** Psoriatic arthritis digital phenotyping and inflammation drivers
(PDPID) study: protocol for an international multicentre prospective cohort
**Authors:** Hojeij B, Tchetverikov I, Vasileiou E, Apostolidis G, Dimitroulas T,
Mytilinaiou M, Gonçalves C, Rodrigues AM, Coates L, Konstantinidis D,
Dimitropoulos K, Melanitis N, Foolen J, Wagenaar W, Charisis V, Hadjileontiadis
LJ, Luime JJ
**Venue / Year:** BMJ Open, 2026;16(9):e115903 (published 2026-09-28)
**DOI:** https://doi.org/10.1136/bmjopen-2025-115903
**PubMed:** https://pubmed.ncbi.nlm.nih.gov/42805667/
**Full text used:** https://pmc.ncbi.nlm.nih.gov/articles/PMC13629932/
**Registration:** ClinicalTrials.gov **NCT06347237**
**Basis of this analysis:** FULL TEXT (PubMed Central open-access copy,
retrieved 2026-10-09). Tables 1, 2 and 3 — the study objectives, the clinical
measures and the digital measures — all rendered in full and are used throughout.
Figures 1 and 2 (the study-procedure diagram and the app screenshots) did not
render. As with two earlier protocols in this list, **the PMC rendering silently
dropped the registration number** — the abstract ends "Trial registration number
." with nothing after it. NCT06347237 above comes from the live PubMed record for
this article, not from the rendered full text, and is flagged as such.
**Date decoded:** 2026-10-09
**Evidence grade:** 4/5 — **for the plan. A protocol has no results.**

All identifiers were verified against the live PubMed and PubMed Central records
on 2026-10-09. Nothing here rests on a guessed or reconstructed link.

Chosen today as the next reachable queue entry. Three entries ahead of it were
checked and remain unreachable — details at the end, including one that has now
failed twice in the same specific way.

---

# The Gist

**Psoriatic arthritis** is an inflammatory arthritis that comes with psoriasis.
It affects about 0.1% of adults and roughly one in five people who have
psoriasis. Its defining practical problem is that it comes in waves: periods of
relative calm punctuated by **flares** — joints swelling, pain, fatigue,
stiffness — and the flares are unpredictable.

The clinical gap is almost absurdly simple when you say it plainly. Disease
activity is assessed at clinic visits, and patients get a few visits a year. So
for roughly 360 days out of 365, nobody knows what is happening. The paper puts
it as "limited information into disease activity changes between visits."

The obvious fix is to ask patients more often. The obvious problem with the
obvious fix is that questionnaires suffer "recall bias and survey fatigue," and
asking someone to rate their pain every day for a year is itself a burden.

So this team is trying something else: let the phone and the watch do the
noticing. A smartphone already measures how you move, how you type, how much you
use it; a smartwatch adds heart rate, sleep and activity. If a flare changes how
you walk, how fast you type, how you sleep — and it plausibly does — those
changes should be visible without anyone filling in a form. That is a **digital
biomarker**.

The plan: 554 patients with psoriatic arthritis, recruited across **30 sites in
four European countries**, followed for **12 months**, with a study app on their
own phone and a Garmin watch on their wrist. Alongside the sensors they collect
clinical examinations, nine kinds of questionnaire, stool samples for gut
microbiome, saliva for DNA, hair for cortisol, blood CRP, and — unusually —
weather and air pollution looked up from each participant's postcode.

Two things make this worth decoding rather than skimming.

The first is that **the sample size is computed twice, by two different routes,
and both reproduce exactly.** 554 patients. I ran the arithmetic: to pin down a
sensitivity of 90% to within ±5 percentage points you need about **138 flare
cases**, and at an assumed 25% flare rate that means **553** patients. Separately,
a 13-parameter prediction model at ten events per parameter needs 130 events, and
554 patients yields **139**. Two independent calculations landing on the same
number is what a real sample-size section looks like.

The second is rarer and better. Almost every digital-health paper reports an AUC
and stops. This protocol commits in advance to asking the questions that actually
determine whether a monitoring tool is usable: **how reliable is this score when
nothing has changed** (test-retest, by intraclass correlation), **what size of
change would a patient actually care about** (minimal important change, by two
independent methods), and **what is the smallest change we can detect above our
own measurement noise** (minimal detectable difference). If the second number is
smaller than the third, the instrument cannot see changes that matter — and
nobody finds that out unless they measure both.

The problem is structural and the protocol does not address it. The app sends
daily questionnaires **while a flare is registered** and a single control
questionnaire **every two weeks otherwise**. Photos and videos are taken every
six weeks **and whenever a flare is registered**. So the amount of data in
existence is **fourteen times higher during a flare than outside one** — which
means "lots of recent data exists" is caused by the outcome, and would work as a
near-perfect predictor of it in any model allowed to see it. No train/test split
fixes that, because the leak is in the sampling design, not the analysis.

# Study Snapshot

- **Study type:** **Protocol** for an international, multicentre, **prospective**
  observational cohort study developing and **internally** validating digital
  biomarkers and machine-learning models. No results yet.
- **Registration:** ClinicalTrials.gov NCT06347237.
- **Sites:** 30 sites across **four countries** — the Netherlands, UK, Portugal
  and Greece — within the EU-funded iPROLEPSIS project, chosen to represent
  North-Western and Southern Europe.
- **Initiated:** **September 2024.** The protocol was published 2026-09-28 — see
  the concerns section.
- **Target:** **554 patients** with diagnosed psoriatic arthritis.
- **Follow-up:** 12 months, with visits at baseline and 3, 6, 9 and 12 months,
  **plus patient-initiated visits** when someone seeks care for a flare.
- **Inclusion:** 18 or over and able to consent; diagnosed psoriatic arthritis;
  **uses a smartphone**; agrees to wear a smartwatch; good command of the local
  language.
- **Primary objective 1:** develop and internally validate a model detecting
  flare from **accelerometer data, keystroke dynamics and screen time** —
  benchmarked against flare as defined clinically by the rheumatologist.
- **Primary objective 2:** develop and internally validate models **predicting**
  flare from sleep, fatigue, pain, stress, mechanical stress, gut microbiome,
  genetic predisposition and environmental exposure.
- **Nine secondary objectives,** including construct validity against composite
  disease-activity scores; a video and photo model of joint and skin appearance;
  **intraperson reliability**; **clinically relevant change**; **minimal
  detectable difference**; cost-effectiveness; and user compliance and
  satisfaction.
- **The reference standard:** "The physician-reported flare will serve as the
  gold standard for flare identification" — with self-registered app flare,
  patient-reported questionnaire flare, and the biomarker's own output also
  explored. The authors state plainly that **"there is currently no standard
  definition of a PsA flare."**
- **Devices:** the **miPROLEPSIS** app on the participant's **own** phone
  (iOS and Android, four languages), plus a provided **Garmin Vivoactive 5**.
- **Passive digital measures:** smartphone accelerometer and gyroscope, keystroke
  dynamics from the virtual keyboard, screen time; smartwatch accelerometer,
  physical activity intensity and category, motion intensity, steps, distance,
  body battery, stress, heart rate, beat-to-beat intervals, and sleep metrics
  and staging. All continuous.
- **Active digital measures:** a **flare toggle button**; daily in-app
  questionnaires (sleep, stiffness, pain, fatigue, function, skin, mood, plus a
  joint manikin) for the first 14 days and whenever the flare button is on; a
  control questionnaire every 2 weeks otherwise; photos of hands and feet and
  videos of hand, gesture and posture at baseline, **every 6 weeks, and on
  registered flare**.
- **Privacy design:** for the videos, "only the derived time series of hand and
  body landmarks are stored (raw video footage is not saved)," and "all data
  collected by the miPROLEPSIS app is available to study participants."
- **Biological samples:** saliva for DNA at baseline; stool for gut microbiome at
  baseline, on flare, and additionally at 6 and 12 months in the Netherlands;
  hair for cortisol at 3 months (optional at baseline, 6, 9, 12); CRP from
  routine records at every visit.
- **Environmental data:** weather and air pollution at **residential and
  occupational** postcodes, from open-source monitoring-station databases.
- **Clinical measures (Table 2):** roughly 45 measures including swollen and
  tender joint counts, enthesitis, dactylitis, psoriasis, CASPAR criteria,
  PASDAS, DAPSA, minimal disease activity, PSAID, HAQ, SF-36, EQ-5D, PHQ-9 and
  WPAI.
- **Sample size — route 1 (detection):** targeting sensitivity 90% and
  specificity 80% with a 25% assumed flare rate and "10% width around the
  estimate" → **554**.
- **Sample size — route 2 (prediction):** ten events per parameter at 25%
  prevalence → **554**, giving **139 expected flares** and room for **12
  variables plus the intercept**.
- **Planned analysis:** descriptive statistics; linear and logistic regression;
  **mixed-effects models for repeated measures**; **Cox models for time-to-event**;
  machine learning on engineered keystroke and inertial feature vectors;
  **MediaPipe** landmark extraction for video range-of-motion; image processing
  for nail and joint metrics **adjusted for skin tone using the Fitzpatrick
  classification**; and **deep learning with few-shot learning on foundation
  models** fusing all modalities at various levels.
- **Measurement properties:** test-retest reliability by **intraclass
  correlation coefficient**; construct validity against app, physician and
  patient flare and against PSAID with AUC at different precision-recall
  cut-offs; **minimal important change by anchor-based and distribution-based
  methods**, the latter via Cohen's effect-size benchmark; **minimal detectable
  difference**.
- **Validation:** internal only — "data will be randomly split into training,
  validation and test sets," with bootstrap and cross-validation. The authors
  state external validation "will be required."
- **Patient and public involvement:** substantial and genuine. Patient partners
  helped develop the flare-detection methods, **tested the app features during
  study design**, and are consulted throughout on objectives, procedures and
  progress; participants complete usability questionnaires.
- **Ethics:** approved in all four countries (Erasmus MC MEC-2023-0470; HRA and
  Health and Care Research Wales 332916; NOVA Medical School CEFCM
  124/2023/CEFCM; Hipokrateion Hospital Thessaloniki 5549/31.01.24), with local
  institutional approvals.
- **Funding:** EU-funded via the iPROLEPSIS project; findings to be reported to
  the European Union funding body. **No competing-interest statement in the text
  retrieved.**

# How Strong Is This Evidence? — Grade 4/5

The third protocol this list has decoded, and the grade is again for the plan,
not for findings. Four out of five: the best measurement-science planning of the
three, with one structural flaw in the data-collection design and one
prespecification problem that is about timing rather than content.

**What earns the points.**

**It asks the measurement question almost nobody asks.** Secondary objectives 3,
4 and 5 are, in plain terms: *is this score stable when nothing changes? how big
a change do patients care about? and how big a change can we actually detect?*
The analysis plan names the tools — intraclass correlation for test-retest,
anchor-based **and** distribution-based estimation of minimal important change,
minimal detectable difference. A monitoring tool whose noise is larger than the
change it is meant to spot is useless, and the only way to discover that is to
measure both quantities. Almost every digital-biomarker paper reports
discrimination and skips this entirely. More in the Spotlight, because this is
the most transferable idea in the paper.

**The sample size is real, computed two ways, and both reproduce.** The precision
route needs ~138 flare cases to pin a 90% sensitivity to ±5 points, which at 25%
prevalence gives 553; the events-per-parameter route gives 139 events and room
for 13 parameters. I checked both and they land on the stated 554. Compare entry
37 in this list, which cited the relevant framework and declined to apply it.

**It declares a gold standard, and admits the gold standard does not exist.**
"The physician-reported flare will serve as the gold standard" — while also
stating that "there is currently no standard definition of a PsA flare," and
collecting four separate flare signals (physician, patient questionnaire, app
button, biomarker) rather than quietly conflating them. Naming the primary
reference and keeping the others visible is the right way to handle a soft
outcome.

**Patient and public involvement is the best of the three protocols decoded.**
Patient partners helped develop the methods, **tested the app during design**, and
are consulted on an ongoing basis, with usability measured in-study. Entry 37
added involvement after the grant stage and said so; entry 39 had none and said
so; this one built it in.

**A prespecified fairness measure in the image analysis.** Nail and joint metrics
will be "adjusted for skin tone bias using the Fitzpatrick Skin Tone
classification." Entry 39, also an imaging protocol, had no fairness analysis at
all. See the concerns for how to make this stronger.

**Privacy engineered rather than promised.** Raw video is not stored — only
derived landmark coordinates. Participants can access all their own app data.

**The statistical plan matches the data structure.** Mixed-effects models for
repeated measures and Cox models for time-to-event are the right families for
intensive longitudinal data from the same people, and naming them in advance
rules out the common error of treating each day's observation as independent.

**Honest, specific limitations.** Dropout and loss to follow-up; **missingness in
high-frequency sensor data**; recall bias and social desirability in
questionnaires, with objective counterweights named (hair cortisol for stress,
physician assessment for activity); smartphone ownership as a selection
restriction; and internal validation only, with external validation explicitly
flagged as still required.

**What costs the points.**

**One: the amount of data collected depends on the outcome.** This is the
substantive flaw. Daily questionnaires run for 14 days at the start, then
**only while the flare button is on**; otherwise one control questionnaire a
fortnight. Photos and videos come every six weeks **and on registered flare**. So
within any two-week window a flare period generates about **14** questionnaire
observations against **1** outside it, and an off-schedule photo exists
*because* a flare was registered. Any model that can see the existence or density
of these observations has access to a near-perfect proxy for the outcome, and no
train/test split repairs it, because the leak is in how the data came to exist.

To be precise about the exposure: the **passive** streams — accelerometer,
gyroscope, heart rate, keystrokes, screen time, sleep — are continuous and
**not** outcome-dependent, so **Primary objective 1 is clean on this axis.** The
risk sits in Secondary objective 2, the photo and video model, and in the
deep-learning fusion model for flare prediction, which is explicitly described as
combining "active video and photo tests" with the passive streams.

**Two: the protocol was published roughly 24 months after recruitment began.**
"Initiated in September 2024"; published September 2026. No enrolment figure is
reported — not how many of the 554 are in, not the observed flare rate against
the assumed 25%. A protocol's value is that it is dated before the data. Two
years of accumulating data weakens that, and the omission of any progress figure
is conspicuous when the key design assumption (25% flare rate) could by now be
checked. Compare the other two protocols in this list, both of which stated
exactly where they had got to.

**Three: the sample-size budget and the analysis plan are an order of magnitude
apart.** The budget justifies **13 parameters** against **139 events** — 10.7
events per parameter. The analysis plan then proposes deep learning, few-shot
learning on foundation models, and "various levels of modality fusion" across
smartphone and smartwatch inertial streams, keystroke features, screen time,
sleep, heart rate, video landmarks, photo metrics, microbiome, genetics and
weather. A crude count of just the **named** feature families comes to around
**79** before any time-windowing, which is about **1.8 events per feature**.
Regularisation and pretrained foundation models change that calculation; they do
not erase it. The fix is one sentence: name the 13-parameter model as primary and
label the deep-learning work exploratory.

**Four: the gold standard is only measured when the patient decides to attend.**
Physician-reported flare — the declared reference — is recorded at scheduled
visits or at a patient-initiated visit when someone "seeks help from the
rheumatologist due to a flare." A patient who flares and does not come in has no
physician-confirmed flare. So the reference standard is applied selectively, to
the subset who present, and absence of a confirmed flare conflates *no flare*
with *flare that did not trigger a visit*. Worse, the app itself may influence
presenting: activating the flare button restarts daily questionnaires, which may
make a patient more likely to recognise and act on a flare. If so, the
measuring instrument partly causes the outcome it is measuring.

**Five: missing sensor data will not be missing at random, and no method is
named.** The limitation is acknowledged — "missingness in high-frequency data
from smartphone and smartwatch" — with the remedy given only as "appropriate
missing data handling and imputation methods will be applied." But people stop
wearing a watch when they are in pain, in hospital, or too unwell to bother. So a
gap in the data is itself a flare signal. Imputing it either destroys that signal
or manufactures a spurious one, depending on how. This needs a named, prespecified
approach, and it deserves a planned analysis of whether missingness predicts
flare.

**Six: Table 1 and Table 2 disagree about what is primary.** Table 1 makes flare
detection Primary objective 1. Table 2 labels "Flare" as a **Secondary**
parameter, while "Remission," "Low disease activity" and "Patient acceptable
symptom state" are labelled **Primary**. One of the two tables is mislabelled,
and in a protocol the identity of the primary outcome is the thing that most
needs to be unambiguous.

**Seven: participants use their own phones.** Good for realism and adherence,
awkward for measurement. Keystroke dynamics in particular — key hold time, flight
time, typing speed, "normalised pressure" — depend on the keyboard software, the
screen, the sampling rate and the operating system. Accelerometer sampling rates
differ across devices too. No harmonisation or device-effect analysis is
described, and with four languages and both iOS and Android the heterogeneity is
large. At minimum, device make and OS should be covariates, and the protocol
should say whether features are standardised within person.

**Eight: adjusting for skin tone is not the same as showing it works across skin
tones.** Two refinements. The Fitzpatrick scale was designed to classify sunburn
propensity rather than pigmentation and is widely criticised as a skin-tone
measure, particularly at the darker end. And "adjusting for" a bias removes it
from a coefficient; it does not demonstrate equal performance. Report accuracy
**stratified** by skin tone, as entry 37's protocol planned to do for sex.

**Nine: no multiplicity plan.** Nine secondary objectives and roughly 45 clinical
measures across six time points, with no statement of which analyses are
confirmatory, which exploratory, or how the resulting number of tests will be
handled.

# The Editor's Concerns

**Separate the outcome-triggered data streams from the continuous ones, in
writing.** State that Primary objective 1 uses only continuously collected
passive signals, and that any model including questionnaire density, photo
timing or video timing is exploratory. Better still, prespecify that the fusion
model will be fitted on fixed-schedule data only, with the flare-triggered
observations held out and reported separately. Without this, a strong result from
the fusion model will be uninterpretable.

**Report enrolment, and check the 25% assumption.** The study has been running
for two years. Say how many of the 554 are enrolled, how many have completed 12
months, and what the observed flare rate is. If it is materially below 25%, the
whole sample-size argument needs revisiting, and better to know now. Publishing a
protocol two years into recruitment without this is a missed opportunity rather
than a flaw in the design.

**Name the primary prediction model and label the rest exploratory.** The 13
parameters that the sample size was computed for should be listed explicitly —
the text names age, sex, initial disease activity state, sleep, stress,
keystroke-derived features, accelerometer activity features and screen time,
which is fewer than 12 distinct items as written. Pin down the list.

**Prespecify the missing-data method, and analyse missingness as a signal.**
Name the approach (multiple imputation under what assumption? a model for
not-at-random missingness? a wear-time threshold for including a day?), and add a
planned analysis of whether non-wear predicts flare. That analysis may itself be
one of the study's more useful outputs.

**Address the verification problem in the gold standard.** Options: define a
confirmed-flare and a possible-flare category; collect a flare questionnaire from
every participant at every scheduled visit covering the interval since the last
one, which the design partly does; or report the detection model's performance
restricted to the windows where a physician assessment exists, and separately
describe what it flagged outside them. Also state whether app use is expected to
change care-seeking, and consider a comparison against patients who have the
sensors but not the flare button.

**Reconcile Tables 1 and 2** on which parameter is primary.

**Add device and OS as covariates** and describe how keystroke and inertial
features will be harmonised or within-person standardised across heterogeneous
phones.

**Report image-analysis performance stratified by Fitzpatrick category** rather
than only adjusting for it, and acknowledge the scale's known limitations as a
pigmentation measure.

**State which analyses are confirmatory,** and how multiplicity across nine
secondary objectives will be handled.

**State competing interests.**

**And one point of praise that should be made louder.** The reliability and
minimal-change work is the most valuable thing in this protocol and it is buried
in secondary objectives 3 to 5. It should be in the abstract. A digital biomarker
with a published intraclass correlation, a minimal detectable change and a
minimal important change is a usable clinical instrument; one with only an AUC is
a research curiosity. If this study delivers nothing else, those three numbers
would be a real contribution.

# Statistics Spotlight

Five ideas. The second is new to this list and is the one most worth carrying
away.

## 1. When how much data you have depends on what happened

Normally you decide in advance when to measure something, and then the
measurements are just measurements. This protocol does something different, for
entirely sensible practical reasons, and it creates a subtle trap.

The rules, as written:

- Daily in-app questionnaires for the **first 14 days** after joining.
- After that, daily questionnaires **resume and continue "for as long as the
  flare button is activated."**
- When no flare is registered, **one** control questionnaire **every two weeks**.
- Photos and videos at baseline, **every six weeks**, **and whenever a flare is
  registered.**

Count the observations in any two-week stretch:

> during a flare: about **14** questionnaire observations
> outside a flare: **1**

**Fourteen times more data exists during the outcome than outside it.** And an
off-schedule photo exists *because* someone pressed the flare button.

Now imagine a model trying to predict flare that is allowed to see these data.
"How many questionnaires were completed in the last fortnight" is not a symptom
of psoriatic arthritis. It is a consequence of the flare button having been
pressed, which is nearly the outcome itself. A model would learn it instantly,
score beautifully, and be worthless — because at deployment the button press
comes *with* the flare, not before it.

The important part: **a train/test split does not fix this.** Splitting data
protects you when information leaks from the test set into training. Here nothing
leaks between sets; the *existence* of each observation is caused by the outcome,
identically in both. The leak is in how the data came to exist, and the only
repairs are at the design or feature level — use fixed-schedule data only, or
exclude any feature that encodes observation timing or density.

The protocol's **passive** streams are clean on this: accelerometer, gyroscope,
heart rate, keystrokes, screen time and sleep run continuously regardless of
flare status. That is why Primary objective 1, which uses exactly those, is
sound. The exposure is in the photo and video work and in the all-modality fusion
model.

**An everyday version.** You want to predict which days a child will be ill, and
you note that you take their temperature far more often on ill days. "Number of
thermometer readings today" will predict illness almost perfectly, and tells you
nothing you did not already know. The thermometer readings themselves are useful;
the *count* of them is a shadow of the answer.

**Watch out for:** any study where measurement is triggered by symptoms,
complaints, or clinician concern — which describes most routine-care data. Ask:
was this observation collected on a fixed schedule, or because something
happened? If the latter, the *fact* of the observation carries outcome
information, and any feature built on timing, frequency or completeness is
suspect. This is the design-level cousin of the ascertainment problem in entry
39, where sicker eyes were seen more often and so had more chances to be caught
crossing a threshold.

## 2. Can the instrument see a change worth seeing?

This is the best idea in the protocol and it is almost absent from the
digital-health literature. It also has a satisfying structure: two numbers, and
all that matters is which is bigger.

Suppose you build a score that tracks arthritis activity. Before using it to
monitor anyone, you need two things.

**How much does the score wobble when nothing has changed?** Measure the same
stable person twice and see how much the number moves. Summarised by the
**intraclass correlation coefficient (ICC)** — roughly, the share of the score's
variation that reflects real differences between people rather than measurement
noise. From it you get the **standard error of measurement**, and from that the
**minimal detectable change (MDC)** — the smallest change you can be confident is
not just noise. The usual form is:

> standard error of measurement = between-person SD × √(1 − ICC)
> minimal detectable change (95%) = 1.96 × √2 × standard error of measurement

**How much change would a patient actually care about?** That is the **minimal
important change (MIC)**, and it cannot be computed from the score alone — it
needs an external anchor, such as asking patients whether they feel better. The
protocol plans both approaches: **anchor-based** (tie score changes to patients'
own global rating of change, which Table 2 collects at every visit) and
**distribution-based** (a rule of thumb from the spread, here using Cohen's
effect-size benchmark). Using both and triangulating, as the protocol says it
will, is best practice.

Now the punchline. Take a score from 0 to 100 with a between-person standard
deviation of 15, and watch what reliability does to the detectable change:

> ICC 0.70 → measurement error 8.2 → **minimal detectable change 22.8 points**
> ICC 0.80 → 6.7 → **18.6**
> ICC 0.90 → 4.7 → **13.2**
> ICC 0.95 → 3.4 → **9.3**

Suppose the minimal important change turns out to be **8 points**. At ICC 0.70
the instrument cannot reliably detect anything smaller than 22.8 points — so
**every change patients care about is invisible inside its own noise.** The score
is not slightly weak; it is unusable for monitoring, no matter how good its AUC
for distinguishing flare from non-flare across people. Only at ICC around 0.95
does the detectable change approach what matters.

**MDC larger than MIC is a fatal property of a monitoring tool, and the only way
to find out is to measure both.** This protocol commits to doing exactly that, in
advance.

**An everyday version.** You want to track whether a diet is working, using
bathroom scales that read ±2 kg at random. A 1 kg loss matters to you. The scales
cannot see it — any single reading could be 2 kg out either way. The scales are
not broken and they are fine for telling a 60 kg person from a 90 kg person. They
are simply the wrong instrument for the question, and you only learn that by
measuring their wobble and comparing it to the change you care about.

**Watch out for:** any wearable, app or score offered for *monitoring* — tracking
change within a person over time — that reports only discrimination (AUC,
sensitivity, specificity). Those describe telling people apart, which is a
different job. Ask for the test-retest reliability, the minimal detectable
change, and the minimal important change. If they are not reported, the tool has
not been shown capable of the thing it is being sold for.

## 3. Two ways to size a study, and why they agreed here

This protocol computes its sample size twice, for its two primary objectives, and
the two routes are worth knowing because they ask different questions.

**Route 1 — precision.** The question is *how tightly do I want to pin down a
number?* They want a sensitivity of 90% estimated to within a 10-percentage-point
total width, i.e. ±5 points. The standard formula for a proportion:

> n = z² × p(1 − p) ÷ d²

With z = 1.96, p = 0.90, d = 0.05: n = 3.8416 × 0.09 ÷ 0.0025 = **138.3**. But
that is 138 **flare cases**, and only an assumed 25% of patients flare. So:

> 138.3 ÷ 0.25 = **553** patients

The protocol says 554. It reproduces. And notice which arm binds: specificity of
80% to the same precision needs 246 controls, and 554 patients supply 416 — more
than enough. **The entire cohort size is set by needing about 138 flares to
measure sensitivity precisely.** That is a useful thing to see: in a
diagnostic-accuracy study, the rarer group almost always drives the sample size.

**Route 2 — overfitting.** The question is *how many things can I estimate before
my model starts memorising?* The protocol uses events per parameter: 554 patients
× 25% = **139 events**, divided by **12 variables plus an intercept** = 13
parameters, giving **10.7 events per parameter** — clearing the conventional
floor of about 10. (The text says "10 patients per event," which is garbled; the
rule is events per variable, and the arithmetic they performed is the right one.)

The two routes agree at 554, and the precision route is marginally the stricter.
When two independent calculations land on the same number, the number is probably
not reverse-engineered from a feasible recruitment target — which is the usual
failure mode of sample-size sections.

**An everyday version.** Two reasons to taste more soup. One: you want to be
confident about how salty it is, which needs enough spoonfuls to average out.
Two: you want to judge six different seasonings separately, which needs enough
spoonfuls that each judgement rests on something. Different questions, both
answered in spoonfuls, and you take whichever number is larger.

**Watch out for:** a sample size justified by one route when the paper's main
claim needs the other. A study sized for precision on a single proportion will be
too small for a multi-variable model, and vice versa. And check which group is
rare: if the sample size does not mention the number of **events**, it probably
was not computed for the analysis being reported.

## 4. A gap in the data is data

The protocol names its risk honestly — "missingness in high-frequency data from
smartphone and smartwatch" — and then proposes "appropriate missing data handling
and imputation methods," without naming them. That gap matters more than it looks
in a sensor study.

Most imputation methods assume data are **missing at random**: that what is
absent can be predicted from what is present. For a wearable in an arthritis
study, that assumption fails in a specific and inconvenient direction. People
stop wearing a watch when they are in too much pain to care, when they are in
hospital, when a flare has wrecked their routine. So **non-wear is itself a flare
signal.**

That cuts two ways and both are bad if unhandled:

- **Impute the gap** — fill it with a plausible estimate drawn from the person's
  normal days — and you erase the signal, making flare periods look like ordinary
  ones.
- **Drop the gap** — analyse only complete days — and you systematically delete
  the worst days, which are exactly the ones the study is about.

The honest handling is to treat **wear time as a variable in its own right**,
test whether non-wear predicts flare, and report it. If it does, that is a
finding, and quite possibly a more robust one than any accelerometer feature:
"the watch came off" is easy to measure and hard to fake.

**An everyday version.** You track your running with an app. On the weeks you
were injured, there are no entries. Filling in the blanks with your average pace
makes those weeks look fine. Deleting them makes you look like a more consistent
runner than you are. The blanks were the injury.

**Watch out for:** any wearable or app study that reports an imputation method
without discussing *why* data went missing. Look for a stated wear-time
threshold, an analysis of whether missingness relates to the outcome, and a
sensitivity analysis under a not-at-random assumption. This is the same family of
problem as informative censoring in entry 39, where patients who died were
treated as ordinary dropouts.

## 5. When the truth only gets measured if the patient turns up

The protocol declares its reference standard clearly: "the physician-reported
flare will serve as the gold standard." And it is honest that no agreed definition
of a psoriatic arthritis flare exists at all.

But look at when a physician assessment happens: at the five scheduled visits, or
at a **patient-initiated** visit, when someone "seeks help from the rheumatologist
due to a flare." So the truth gets measured when the patient decides to seek it.

Two consequences.

**Absence of a confirmed flare means two different things.** It can mean no flare
happened, or it can mean a flare happened and the person did not come in — because
it was mild, because they were busy, because they have had fifty of them and know
the drill. These are mixed together in the "no flare" category, so a detection
model that correctly spots an unattended flare is scored as **wrong**. Its
sensitivity will be understated and its false-positive rate overstated. This is
**verification bias**: the reference test is applied selectively, and selectively
in a way related to the outcome.

**And the instrument may be causing the outcome.** The app has a flare button;
pressing it restarts daily questionnaires. Does being asked daily about your pain
make you more likely to recognise a flare and go to the clinic? Plausibly yes. If
so, the app is partly generating the physician-confirmed flares against which the
app is being validated. That is not fraud, it is reactivity — the act of
measuring changes the thing measured — and in digital phenotyping it is a
first-order design question, because the measuring device is in the patient's
pocket all day.

**An everyday version.** You want to know how often your car makes a strange
noise, and you define "strange noise" as "a noise the mechanic confirmed." The
mechanic only hears the ones you drove in for. Every noise you ignored is
recorded as no noise — and the new app that pings you whenever it hears something
odd may be the reason you booked the appointment at all.

**Watch out for:** in any diagnostic or monitoring study, ask *who decided that
the truth would be measured on this occasion, and could the thing being evaluated
have influenced that decision?* If yes, the accuracy figures are biased, usually
against the new test for sensitivity and in unpredictable directions elsewhere.
This list has now met three versions: an outcome partly caused by the decision
under study (entry 37), a reference standard available only for transported
patients (entry 38), and here, a reference standard available only when the
patient presents.

# Jargon Translator

- **Psoriatic arthritis (PsA)** — an inflammatory arthritis occurring with
  psoriasis; affects joints, tendon attachments and skin.
- **Psoriasis (PsO)** — a chronic immune-mediated skin disease.
- **Flare** — a period of worsening disease activity. There is no agreed
  definition in psoriatic arthritis, which is central to this study's difficulty.
- **Enthesitis** — inflammation where a tendon or ligament attaches to bone.
- **Dactylitis** — a whole finger or toe swollen "like a sausage"; characteristic
  of psoriatic arthritis.
- **CASPAR** — the standard classification criteria for psoriatic arthritis.
- **PASDAS / DAPSA / MDA** — composite disease-activity scores for psoriatic
  arthritis.
- **PSAID** — Psoriatic Arthritis Impact of Disease, a patient-reported measure.
- **HAQ / SF-36 / EQ-5D / PHQ-9 / WPAI** — standard questionnaires for physical
  function, general health, quality of life, depression, and work productivity.
- **PGA / PtGA** — physician's and patient's global assessment of disease
  activity.
- **Patient-reported outcome (PRO)** — any measure reported directly by the
  patient.
- **Digital biomarker** — a health indicator computed from data captured by
  digital devices rather than from a laboratory or examination.
- **Digital phenotyping** — characterising someone's health from their everyday
  interaction with personal devices.
- **Passive versus active measurement** — collected automatically in the
  background versus requiring the participant to do something.
- **Keystroke dynamics** — how someone types: key hold time, flight time between
  keys, speed, deletion rate. Sensitive to finger stiffness and dexterity.
- **Inertial measurement unit (IMU)** — the accelerometer and gyroscope inside a
  phone or watch.
- **Beat-to-beat intervals** — the exact spacing between heartbeats; the raw
  material for heart-rate variability.
- **Body battery** — a proprietary Garmin index combining heart-rate variability,
  activity and sleep.
- **MediaPipe** — open-source software that locates body and hand landmarks in
  video.
- **Range of motion (RoM)** — the angle a joint travels through during a
  movement.
- **Fitzpatrick skin tone classification** — a six-category scale, originally
  devised to classify sunburn propensity, widely used (and widely criticised) as a
  skin-tone measure in image analysis.
- **Gut microbiome** — the community of microbes in the intestine, assayed here
  from stool samples.
- **Hair cortisol** — cortisol accumulated in hair, giving a retrospective
  measure of stress over months rather than minutes.
- **C-reactive protein (CRP)** — a blood marker of inflammation.
- **Prospective cohort** — participants enrolled and then followed forward, with
  measurements planned in advance.
- **Internal versus external validation** — testing a model on held-out data from
  the same study, versus on data from a different source. Only the second predicts
  deployment.
- **Mixed-effects model** — a regression that accounts for repeated measurements
  from the same person, so one person's many days are not treated as many
  independent people.
- **Cox proportional hazards model** — the standard model for time-to-event
  outcomes.
- **Events per parameter** — outcome events divided by the number of quantities a
  model estimates; a guard against overfitting. Conventionally at least 10.
- **Few-shot learning / foundation model** — adapting a very large pretrained
  model to a small dataset with few examples.
- **Modality fusion (early and late)** — combining different data types either as
  raw inputs or after each has been summarised into features.
- **Intraclass correlation coefficient (ICC)** — the share of a measurement's
  variation reflecting real between-person differences rather than noise; the
  basis of test-retest reliability.
- **Standard error of measurement** — how much a single measurement is expected to
  wobble for one person.
- **Minimal detectable change (MDC)** — the smallest change larger than
  measurement noise.
- **Minimal important change (MIC)** — the smallest change a patient would notice
  or care about.
- **Anchor-based versus distribution-based** — estimating important change by
  reference to an external judgement (such as the patient's own global rating)
  versus from the statistical spread of the measure.
- **Construct validity** — whether a measure actually captures the thing it
  claims to.
- **Verification bias** — the reference standard is applied only to a selected
  subset, in a way related to the outcome.
- **Missing at random** — the assumption that what is missing can be predicted
  from what was observed. Imputation methods usually need it.
- **Reactivity (Hawthorne effect)** — the act of measuring changes the behaviour
  being measured.

# What You Can (and Can't) Say

**You can say:** a European consortium has registered and begun a prospective
12-month study across 30 sites in four countries, aiming to enrol 554 people with
psoriatic arthritis, to test whether smartphone and smartwatch data can detect
and predict disease flares.

**You can say** the plan is unusually strong on measurement science: it commits
in advance to estimating test-retest reliability by intraclass correlation, the
minimal detectable change, and the minimal important change by two independent
methods — the three numbers that determine whether a monitoring tool can actually
be used, and which digital-health papers almost never report.

**You can say** the sample size is genuine: 554 reproduces exactly from two
independent calculations, one based on the precision needed for a 90% sensitivity
(~138 flare cases) and one on ten events per parameter for a 13-parameter model
(139 events).

**You can say** the patient and public involvement is substantive — patient
partners helped develop the methods and tested the app during design — and that
the image analysis prespecifies a skin-tone adjustment.

**You cannot say** anything about whether phones and watches can detect
psoriatic arthritis flares. There are no results. The study runs for 12 months
per participant and the protocol reports no enrolment.

**You cannot treat** this as fully prespecified in the usual sense. Recruitment
began in September 2024 and the protocol appeared in September 2026 — about two
years of data had accumulated before the plan was published, and no enrolment or
observed flare rate is reported.

**You cannot trust** a strong result from the all-modality fusion model without
knowing how outcome-triggered data were handled. Questionnaires run daily during
registered flares and fortnightly otherwise, and photos and videos are taken on
registered flare, so roughly 14 times more of these data exist during the outcome
than outside it. The continuously collected passive signals used for the primary
detection objective are not affected.

**You cannot read** the eventual sensitivity figure as unbiased. The reference
standard — physician-reported flare — is only recorded when a patient attends,
so flares that did not prompt a visit are counted as non-flares.

**You cannot assume** the models will work outside this cohort. Validation is
internal only, by the authors' own statement, and enrolment requires owning a
smartphone, agreeing to wear a smartwatch, and speaking one of four languages.

**You cannot conclude** that the planned deep-learning analysis is adequately
powered. The sample size justifies 13 parameters against 139 events; the named
feature families number around 79 before any time-windowing.

**You should note** that the registration number was dropped from the
open-access rendering of this paper and had to be recovered from the PubMed
record — the third protocol in this list where that has happened.

# Bottom Line for Your Life

If you have psoriatic arthritis, this study is two years from telling anyone
anything. But its premise is a real description of the problem, and there are
things in it worth acting on now.

**The gap this study is built around is the gap you live in.** You see a
rheumatologist a few times a year, and the disease does what it does in between.
The practical response does not require an app: keep a simple record. Dates when
things got worse, which joints, what was happening at the time — sleep, stress,
an infection, a missed dose, a change in the weather if you notice one. A
notes-app list or a paper diary gives your rheumatologist something the
examination cannot, because the examination only sees today.

**Two specifics worth raising at an appointment.** First, there is **no agreed
definition of a flare** in psoriatic arthritis — the authors of this study, who
are specialists in it, say so plainly. So it is reasonable to ask your own
clinician what *they* would count as a flare, and what they would want you to do
when one starts. Having that agreed in advance is more useful than any score.
Second, this study is spending real effort on **triggers** — sleep, stress,
mechanical load, gut microbiome, weather and air pollution — because, as the
paper says, these are poorly understood and patients have "an unmet need to
better understand their disease." If you think you have spotted a pattern in your
own flares, that is worth saying out loud. You have more observations of your
disease than anyone else does.

**On wearables you might already own.** A watch that tracks sleep and activity is
not a medical device and cannot tell you whether you are flaring. What it can do
is give you a rough objective record of how much you moved and how you slept,
which is harder to misremember than a feeling. If you use one that way, use it as
a memory aid, not a verdict.

And the honest expectation to hold about tools like this when they do arrive: the
question to ask is not "how accurate is it?" but "**how much does my score have
to change before that means something real?**" This study is, to its credit,
planning to answer exactly that — and until somebody does, a number that goes up
and down on a screen is not yet information.

**This is education about how to read a study, not medical advice. Decisions
about arthritis treatment and monitoring belong with you and your
rheumatologist.**

---

*Decoded 2026-10-09. Source: PubMed and PubMed Central, accessed 2026-10-09.
Full text read from PMC13629932; Tables 1, 2 and 3 rendered in full, Figures 1
and 2 did not, and the ClinicalTrials.gov identifier was dropped by the PMC
rendering and recovered from the live PubMed record (NCT06347237). Derived
figures — the reproduction of the 554 sample size by both stated routes (138.3
flare cases needed for a 90% sensitivity at +/-5 points, giving 553 patients at
25% prevalence; and 139 events over 13 parameters giving 10.7 events per
parameter); the finding that sensitivity rather than specificity is the binding
constraint (246 controls needed against 416 available); the Wilson interval
widths of 0.101 and 0.077 at the target values; the 14-to-1 ratio of
questionnaire observations inside versus outside a flare window; the crude count
of roughly 79 named feature families giving about 1.8 events per feature; and the
worked minimal-detectable-change table across ICC values of 0.70 to 0.95 — were
computed from the protocol's own stated numbers and standard formulae, and are
labelled as derived wherever they appear. Competing interests were not stated in
the text retrieved; funding is via the EU iPROLEPSIS project.*

**Verified source links**
- DOI: https://doi.org/10.1136/bmjopen-2025-115903
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42805667/
- Full text used: https://pmc.ncbi.nlm.nih.gov/articles/PMC13629932/
- Registration: ClinicalTrials.gov NCT06347237 (from the PubMed record)
