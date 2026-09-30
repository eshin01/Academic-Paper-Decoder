# The AI Heard Old Age, Not Parkinson's

**Paper:** Demographic Confounding in Voice-Based Parkinson Disease Screening:
Methodological Analysis of the Bridge2AI Voice Dataset
**Authors:** Shukla S, Naliyatthaliyazchayil P, Gichoya JW, Purkayastha S
**Venue / Year:** Journal of Medical Internet Research, 2026;28:e95609
**DOI:** https://doi.org/10.2196/95609
**PubMed:** https://pubmed.ncbi.nlm.nih.gov/42623305/
**Full text used:** https://pmc.ncbi.nlm.nih.gov/articles/PMC13492483/

**Companion paper decoded alongside it:** Little M. "Explicit Mechanistic Causal
Analyses or Interventional Trials Are Required for Objective, Clinical,
Voice-Based Parkinson Disease Characterization." J Med Internet Res
2026;28:e111711.
**DOI:** https://doi.org/10.2196/111711 ·
**PubMed:** https://pubmed.ncbi.nlm.nih.gov/42804162/ ·
**Full text:** https://pmc.ncbi.nlm.nih.gov/articles/PMC13618403/

**Basis of this analysis:** FULL TEXT for both papers (PubMed Central
open-access copies, retrieved 2026-09-30). Figures 1–4 and the supplementary
appendix of the primary paper were not retrievable; nothing here depends on a
figure value.
**Date decoded:** 2026-09-30
**Evidence grade:** 5/5

---

# The Gist

For thirty years people have hoped you could diagnose Parkinson's disease by
listening. It makes sense: Parkinson's damages the motor system, the voice is
run by muscles, and a phone can record a voice for free. Recent papers using
deep learning report accuracy scores between 0.85 and 0.97 — the sort of numbers
that get companies funded.

This team downloaded a large public research dataset, trained one of those
models properly, and got 0.843 for Parkinson's. Respectable. In line with the
literature.

Then they did something almost nobody does. They threw away the audio entirely
and built a trivial model that knew only **one thing about each person: their
age.** No voice, no recording, no neural network.

**The age-only model scored 0.875. It beat the 86-million-parameter deep
learning model.**

The reason is embarrassingly simple once you see it. In this dataset the
Parkinson's patients averaged 72.3 years old and the healthy controls averaged
44.8 — a gap of **27.5 years**. Voices change with age all by themselves. So a
model listening to these recordings could score brilliantly by learning to hear
*old* rather than *ill*. It never needed to know what Parkinson's sounds like.

They then spent the rest of the paper doing the harder and more honest thing:
asking whether *any* real disease signal survives once you take the age gap
away. It does — but it is much smaller. Comparing only people aged 60 to 80, the
age-only model collapses to 0.568 (a coin flip is 0.5) while the voice model
holds 0.787. Strip out one more problem — an entire country in the dataset
contributed nothing but patients — and the cleanest estimate is **0.726**.

So: the voice does carry something real about Parkinson's. It just carries far
less than the headlines say. And of 13 published studies the authors surveyed,
**none** had run this check.

# Study Snapshot

- **Study type:** A methodological audit of an existing public dataset. Not a
  trial, not a new tool — a study whose purpose is to test whether an entire
  research literature is measuring what it thinks it is.
- **Dataset:** Bridge2AI Voice Dataset v3.0.0 — 833 participants across 5
  clinical sites in the United States and Canada, publicly available.
- **Parkinson's cohort:** 253 participants (106 cases, 147 controls), 2131
  recordings across 8 speech tasks — sustained vowel, pitch glides, rapid
  syllable repetition, a read passage, picture description, story recall,
  maximum phonation time.
- **Dementia cohort:** 221 participants (73 cases, 148 controls), 1791
  recordings, same 8 tasks. **The two cohorts share the same control group.**
- **The model:** An audio spectrogram transformer — **86.4 million parameters**,
  pretrained on 2 million general audio clips, fine-tuned end to end.
- **Validation:** 5-fold cross-validation split **at the participant level**, so
  no person's recordings appear in both training and testing. This is done
  correctly and is a real strength.
- **The key comparison:** A logistic regression using only age and sex, run
  through the identical cross-validation splits.
- **The age gaps:** Parkinson's cases 72.3 years (SD 8.7) versus controls 44.8
  (SD 19.3) — **27.5 years**. Dementia cases 74.9 (SD 7.6) versus the same
  controls — **30.2 years**.
- **Statistics:** DeLong tests for comparing two AUCs, with **q-values** (false
  discovery rate correction for running many comparisons), and bootstrap
  confidence intervals from 2000 resamples.
- **Reporting:** TRIPOD+AI checklist filed.
- **Origin:** The confounding was first spotted by trainees at the 2025 Emory
  Health AI Summer School & Datathon — participants with **no prior experience
  in voice biomarker research identified it within hours.**
- **Funding:** **Not reported** in the text retrieved. The paper notes the
  training programme sits under an NIH Common Fund initiative.
- **Conflicts of interest:** **No statement appears** in the text retrieved.

# How Strong Is This Evidence? — Grade 5/5

This is the second consecutive 5/5, which is unusual enough to justify saying
what the grade means. It is not "this paper found something big." It is "the
work is trustworthy, and the authors worked hardest at the places where they
could most easily have fooled you."

Yesterday's 5/5 was a review that found nothing and refused to dress it up.
Today's earns it the opposite way: it found something — a genuine disease
signal — and then spent the paper systematically talking that finding *down*.

**What this study did that almost nobody does:**

- **It built the trivial baseline.** One logistic regression on age, run through
  the same splits. That single comparison is the whole paper, and it costs about
  five minutes of computing.
- **It identified which of its own results were independent.** Three analyses
  supported a residual disease signal. The authors state plainly that two of the
  three reuse predictions from the confounded full-cohort model and "are
  therefore not mutually independent," and name the de novo retrained estimate
  as "the independent corroboration." Most papers present three numbers as three
  confirmations.
- **It refused to double-count its own parallel finding.** The Parkinson's and
  dementia cohorts share one control group, so both showing the same pattern is
  "a single structural observation, not 2 independent validations."
- **It argued against its own most flattering number.** Having produced
  estimates of 0.787, 0.798 and 0.760, it identifies **0.726** — the lowest — as
  "arguably the least confounded performance estimate available from this
  dataset" and says "we recommend this figure be given greater interpretive
  weight."
- **It disqualified half of its own headline.** The dementia result of 0.809
  looks like the Parkinson's one. The authors say it "effectively functions as a
  country classifier" and that no site-controlled dementia estimate can be
  derived, because only 2 of 47 US participants aged 60–80 were cases.
- **It reported its own fragility.** Retraining on 129 participants gave fold
  scores from 0.667 to 0.889, standard deviation 0.085, and the authors call
  this "substantial instability" and warn the 0.798 "should be interpreted
  cautiously," naming the unfavourable ratio of 86.4 million parameters to 129
  people.
- **It tested whether the model survives a change of plumbing.** Applying the
  trained model to the same participants' recordings processed through a
  different pipeline dropped performance from 0.843 to **0.618**.
- **It flagged a methodological flaw in its own secondary analysis** — that
  interpolating phoneme probability vectors "lacks meaningful phonetic
  interpretation" and limits that comparison.
- **It corrected for multiple comparisons** with q-values, and it counted the
  field: 13 studies surveyed, 7 reporting both age distributions, **zero** with
  a demographic-only baseline.
- **It proposed three concrete, cheap reporting standards** rather than just
  complaining.

**Legitimate criticisms:** a single dataset; no prospective validation; no
funding or conflict-of-interest statement in the retrieved text; and the abstract
leads with the range 0.726–0.798 when the authors' own recommendation in the
discussion is to weight 0.726. These are small against what the paper does.

# The Editor's Concerns

Most of the criticism here belongs to **the field**, not this paper. The authors
found nearly all of it themselves.

**A model that cannot hear did better than one that can.** On the full
Parkinson's cohort, age-only scored 0.875 and the 86.4-million-parameter
transformer scored 0.843. *Deriving* from those numbers, the deep model was
**0.032 worse** than a one-variable regression. On dementia, 0.905 versus 0.895
— worse by 0.010. Neither difference was statistically significant (DeLong
p = .36 and p = .75), which the authors correctly read not as reassurance but as
the damning result: the transformer "contributes no measurable discrimination
beyond demographic features at full-cohort level."

**It really is age, not sex.** Sex alone scored 0.543 — essentially a coin flip.
Adding sex to age changed nothing (0.869 versus 0.875). In the regression, the
coefficient on age was about 2.1 and on sex about 0.1. One variable is doing all
the work.

**Watch the age-only score collapse as the age gap closes.** *Deriving* from the
paper's tables: with a 27.5-year gap, age-only scores 0.875. Narrow the window
to ages 55–85 and the gap falls to 4.1 years — age-only drops to 0.655. Narrow
again to 60–80, gap 1.4 years — age-only falls to **0.568**, near chance.
Meanwhile the voice model goes 0.843 → 0.805 → 0.787. Two curves separating is
exactly what you would want to see, and exactly what nobody had looked for.

**An entire country contributed only patients.** All **62** Canadian
participants in the Parkinson's cohort are cases. Zero Canadian controls. All
**70** Canadian dementia participants are cases. So for those participants,
country perfectly predicts diagnosis, and a model can score well by learning
what a Canadian recording studio sounds like. Restricting to US participants
aged 60–80 drops the Parkinson's estimate from 0.787 to **0.726**.

**The dementia half of the paper cannot be rescued, and the authors say so.**
The US-only, age-restricted dementia subgroup contains **2 cases against 45
controls**. Propensity matching was impossible. So the dementia figure of 0.809
necessarily includes the all-case Canadian sample. The authors' verdict is
blunt: it "effectively functions as a country classifier." A less careful team
would have reported 0.809 beside 0.787 as two parallel findings.

**The model is brittle to its own plumbing.** The same participants, the same
recordings, run through a different spectrogram extraction pipeline: performance
falls from 0.843 to **0.618** — *deriving*, a drop of 0.225, most of the way to
chance. Whatever the model learned is partly a property of one specific
preprocessing recipe, not of human voices. For a tool meant to run on arbitrary
phones in arbitrary clinics, that is the most operationally worrying number in
the paper.

**Nobody had checked.** Of 13 representative published studies, only 7 reported
the age distributions of cases *and* controls; **none** tested a
demographic-only baseline; **none** ran an age-restricted evaluation. One study
reporting AUC 0.753 on 726 participants acknowledged age as a confounder and
responded by excluding anyone under 50 — without ever testing whether age alone
could predict the outcome. The paper also notes that the TRIPOD+AI reporting
guideline already recommends assessing demographic factors, and that the
literature largely ignores it.

**The rescue analyses are small, and the authors are candid about it.** The
three estimates supporting a real signal rest on 129, 129 and 56 participants.
Confidence intervals are wide — the 0.787 comes with a bootstrap interval of
0.695 to 0.863. Retraining 86.4 million parameters on 129 people produced fold
scores from 0.667 to 0.889. The propensity matching retained only 28 of 39
eligible cases (72%).

**And the origin story is the indictment.** This was found by trainees at a
summer datathon, with no voice-biomarker expertise, "within hours." It needed no
special technique — only the willingness to ask what a stupid model would
achieve. Which raises the real question the paper poses to the field: why had
nobody asked?

## What the companion commentary adds

Max Little — who helped found voice-based Parkinson's detection — published a
commentary on this paper, and it sharpens the point in a way worth carrying.

His argument is that Shukla et al. demonstrate the problem but that the fix is
harder than it looks. Age is not merely *imbalanced* between groups; it is a
**common cause** of both the voice features and the diagnosis. Aging changes the
voice (a condition called presbyphonia), and aging raises Parkinson's risk. That
structure — one variable causing both the thing you measure and the thing you
predict — is what "confounding" properly means, and Little notes the term is
"loosely used" in the primary paper.

He identifies a second, subtler common cause: **individual identity**. Every
person has a distinctive voice, and Parkinson's does not spontaneously remit, so
a dataset typically has no recording of the same individual in both a healthy
and a diseased state. The person's own vocal uniqueness therefore becomes a
second confounder, and one that cannot be balanced away.

His most useful claim for a reader of this list: **cross-validation cannot fix
this.** Splitting data cleverly tests whether a model generalises to new
observations; it does nothing about a variable that caused both the input and
the label. And splitting by individual — which sounds like the obvious fix —
"generally biases the quantification of prediction error because, by
construction, the training and test sets no longer have the same distribution,
which invalidates hold-out methods like CV."

He is also sceptical of the repairs. Controlling for confounders as covariates
means you need the confounder's value at prediction time. Propensity matching,
which Shukla et al. use, "always increases statistical uncertainty and demands
positivity" — a condition violated exactly where the confounding is
deterministic, as it is with individual identity.

His conclusion is that the only complete solution is **interventional data** —
and since you cannot randomly assign someone Parkinson's, what that means in
practice is a **diagnostic trial**: randomise patients to be assessed with the
voice algorithm versus current standard care, and measure treatment outcomes.
Nothing in the observational literature substitutes for it.

# Statistics Spotlight

## Concept 1 — Confounding: when the thing you measure and the thing you predict share a parent

This reading list has circled this idea for weeks. Here it is directly.

**The setup.** You want to know whether voice predicts Parkinson's. You find that
it does, strongly. The question is *why*.

There are two possible structures. In the one you hope for, Parkinson's damages
the motor system, which changes the voice, and the model detects that change.
In the other, something else causes both. Here that something is **age**: aging
changes the voice on its own, and aging makes Parkinson's more likely. Age sits
upstream of both, a **common cause**.

When a common cause exists, an association appears between voice and diagnosis
even if the disease has no effect on the voice whatsoever. The association is
real. The causal claim behind it is not. That is confounding.

**How this paper made it visible.** The trick is beautifully simple: build a
model that uses *only the suspected confounder* and see how well it does. Age
alone scored **0.875**, beating the voice model's 0.843. At that point you know
that whatever the transformer learned, it did not need the audio to get there.

Then they narrowed the comparison to people of similar ages. With cases and
controls both averaging around 70, age can no longer separate them — and it
doesn't: age-only falls to **0.568**, near chance. The voice model holds
**0.787**. That gap is what a real signal looks like after the confounder is
removed.

**An everyday version.** Towns with more storks have more babies. The
correlation is real and strong. Storks do not deliver babies — rural areas have
both more storks and higher birth rates. "Rural" is the common cause. Measure
only rural towns and the stork–baby correlation vanishes, which is precisely
what the age-restricted analysis does here.

Or, closer to medicine: for decades, carrying a lighter did seem to predict lung
cancer. It does. It causes nothing. Smoking causes both.

**The structural point, from the commentary.** Little's addition is that
confounding is a claim about the *causal diagram*, not about the numbers. You
cannot detect it by staring at a correlation matrix, and no amount of
statistical sophistication substitutes for knowing which arrows point where.
He also names a second confounder no rebalancing can remove — each person's
unique voice, since no one in these datasets appears as both a case and a
control.

**Watch out for:** any claim that a model "detects disease X from signal Y,"
where X is strongly associated with age, sex, ethnicity, body size, the hospital
someone attends, or the device used to record them. Ask the same question these
authors asked: *what would a model that knew only the obvious confounder
achieve?* If the paper doesn't say, you cannot tell what the model learned.
Medical imaging has known this for years — models that read the scanner rather
than the patient — and the paper's point is that voice research simply hadn't
caught up.

## Concept 2 — The trivial baseline: the cheapest, most revealing test in machine learning

If you take one habit from this decode, take this one.

**What it is.** Before believing any model, build the dumbest possible competitor
and run it through the identical evaluation. Not a weaker version of your model
— something almost insultingly simple. Here it was one logistic regression on
age, using the same cross-validation folds.

**Why identical splits matter.** If the baseline were evaluated on different
data, or with a different procedure, the comparison would prove nothing. Same
folds, same participants, same metric — so any difference is attributable to the
information used, not the evaluation setup.

**What it revealed.** A model costing seconds to fit beat one with 86.4 million
parameters. That single comparison reframes an entire literature.

**Why it is so often skipped.** Partly effort, but mostly incentive. A strong
baseline can only make your result look worse. Nobody's grant renewal depends on
proving that age explains their findings. Of 13 studies the authors surveyed,
**zero** ran one.

**A tiny worked example.** Suppose a model predicts hospital readmission with
80% accuracy. Impressive? Depends entirely on the baseline. If 80% of patients
are never readmitted, a model that says "no" to everyone also scores 80% — and
is useless. The trivial baseline is what tells them apart.

**The family of questions worth asking:**
- *Always guess the most common answer* — what does that score?
- *Use only the single most obvious variable* — age, sex, how sick they already
  were — what does that score?
- *Use the information the clinician already has* before the new test — what
  does that score?

The last one is the most important for medicine. A biomarker is only worth
having if it adds something beyond what the doctor already knows for free.

**Watch out for:** performance figures quoted with no baseline at all. "AUC
0.85" is not a fact about a model, it is a fact about a model *and* a dataset
*and* a comparison. And notice the asymmetry the paper exposes: the field
reported 0.85 to 0.97 for years, while the least-confounded estimate obtainable
from a well-constructed public dataset is **0.726**.

## Concept 3 — Why cross-validation cannot save you

Cross-validation is the workhorse of machine learning evaluation, and this paper
used it correctly. Understanding what it *cannot* do is the deeper lesson.

**What it does.** Split the data into parts — here 5. Train on four, test on the
fifth, rotate, average. The point is to stop a model being graded on data it
memorised.

**What this paper got right.** They split **at the participant level**: every
recording from one person goes entirely into training or entirely into testing.
Split naively by recording instead, and a model can recognise a voice it heard
in training and recall that person's label — a form of cheating that inflates
scores dramatically. Many published studies get this wrong. These authors did
not.

**What it still cannot do.** Cross-validation checks whether a pattern holds in
data you held back **from the same dataset**. If the age gap exists in all five
folds — and it does, because it is baked into how the cohort was recruited —
then the shortcut is available in every fold. The model exploits it during
training and gets rewarded for it during testing. Cross-validation confirms the
shortcut is *reliable*. It says nothing about whether it is *real*.

Little puts it plainly: cross-validation "cannot correct for causal
confounding."

**And the obvious fix has a catch.** Stratifying folds by individual, age or sex
— splitting so those variables are balanced — seems like the answer. But Little
notes it "generally biases the quantification of prediction error because, by
construction, the training and test sets no longer have the same distribution,
which invalidates hold-out methods like CV." The mathematics of cross-validation
assumes training and test data come from the same distribution. Deliberately
making them differ breaks the guarantee you were relying on.

**An everyday version.** You want to know if a student understands maths, so you
split the practice questions into five piles and test on each in turn. If every
pile contains the same kind of question with the same trick, the student can
learn the trick and score well on all five. Cross-validation proves the trick
works consistently. Only a genuinely different exam reveals whether they
understand anything — which is what the cross-version test did here, and
performance fell from 0.843 to 0.618.

**What actually resolves it, in increasing order of strength:** balance the
groups by design at recruitment; restrict the analysis to a range where the
confounder cannot operate (what this paper did); apply explicit causal-inference
methods such as propensity matching (also done here, with the authors noting it
discards data and needs assumptions that fail under deterministic confounding);
and finally, the only complete answer — **interventional data**. Since you cannot
randomise someone into having Parkinson's, that means a **diagnostic trial**:
randomise which patients get assessed with the algorithm, and measure what
happens to them.

**Watch out for:** "we used cross-validation" offered as evidence of rigour. It
is necessary and it is not sufficient. The questions that matter are: *was the
split at the level of the person or the recording?* and *is the thing the model
might be exploiting present in every fold?* If it is, cross-validation will
certify it rather than catch it.

# Jargon Translator

- **Audio spectrogram transformer (AST):** A model that converts sound into a
  picture of frequencies over time and analyses that picture the way an image
  model would. Here: 86.4 million parameters, pretrained on 2 million general
  audio clips.
- **Spectrogram / Mel bins:** The frequency-versus-time picture of a sound. Mel
  bins are the frequency rows — 60 in one dataset version, 201 in another, which
  is what the brittleness test exploited.
- **AUC (area under the ROC curve):** The chance the model ranks a randomly
  chosen patient above a randomly chosen healthy person. 0.5 is a coin flip, 1.0
  is perfect.
- **Out-of-fold prediction:** A prediction made for a participant by a model that
  never saw them during training. The correct way to score cross-validation.
- **Participant-level split:** All of one person's recordings kept together. The
  difference between honest evaluation and accidental memorisation.
- **DeLong test:** The standard test for whether two AUCs measured on the same
  people genuinely differ.
- **q-value:** A p-value adjusted for the fact that many comparisons were run —
  false discovery rate correction. Reporting q alongside p is a mark of care.
- **Bootstrap confidence interval:** Resampling the data repeatedly (2000 times
  here) to see how much an estimate wobbles.
- **Propensity score matching:** Pairing each case with a control who looks
  similar on chosen variables — here age and sex — to mimic a balanced
  comparison. The 28 pairs came from a caliper of 0.2 standard deviations.
- **Standardized mean difference:** How far apart two groups are on a variable,
  in standard deviations. Below 0.1 counts as balanced; the matched pairs
  achieved 0.095 for age and 0.071 for sex.
- **Positivity:** The assumption, required by matching, that everyone could in
  principle have been in either group. It fails outright for a confounder like
  personal vocal identity.
- **Presbyphonia:** The normal ageing of the voice — lower pitch, more jitter,
  weaker harmonics. The mechanism behind the entire confound.
- **Shortcut learning:** A model solving the task by an easier route than
  intended — reading the scanner, the site, or the patient's age instead of the
  disease.
- **TRIPOD+AI:** The reporting checklist for AI prediction models. It already
  recommends assessing demographic factors.
- **Diagnostic trial:** Randomising which patients are assessed with a new test
  rather than which have the disease, and measuring outcomes. Little's proposed
  endpoint for this field.

# What You Can (and Can't) Say

**Fair to say:**

- On a public multi-site voice dataset, a model using only participants' age
  scored 0.875 for Parkinson's — higher than an 86.4-million-parameter deep
  learning model on the actual recordings (0.843). For dementia, 0.905 versus
  0.895.
- The cause is a case-control age gap of 27.5 years for Parkinson's and 30.2
  for dementia, in a dataset where both conditions share one young control group.
- Restricting to participants aged 60–80 drops age-only performance to 0.568
  while the voice model holds 0.787 — evidence of a genuine disease-specific
  acoustic signal.
- Three convergent estimates put that residual signal at 0.760 to 0.798, and
  only one of the three is statistically independent of the confounded model.
- All 62 Canadian Parkinson's participants and all 70 Canadian dementia
  participants are cases, with no Canadian controls, so country perfectly
  predicts diagnosis for them.
- The authors' own recommended figure — the least confounded available — is
  **0.726**, from US participants aged 60–80.
- The dementia estimate cannot be corrected the same way and, in the authors'
  words, "effectively functions as a country classifier."
- Reprocessing the same recordings through a different pipeline dropped
  performance from 0.843 to 0.618.
- Of 13 surveyed studies, 7 reported both case and control age distributions and
  **none** used a demographic-only baseline or an age-restricted evaluation.
- The commentary by Little argues that cross-validation cannot correct causal
  confounding, that individual vocal identity is a second confounder that
  rebalancing cannot remove, and that diagnostic trials are ultimately required.

**Not fair to say:**

- ~~"AI can't detect Parkinson's from voice."~~ The paper establishes that it
  can — at 0.726 to 0.798, not 0.85 to 0.97.
- ~~"Voice-based Parkinson's screening is a fraud."~~ It is an overestimate
  produced by convenience sampling, which is a design failure, not deception.
- ~~"The deep learning model was useless."~~ It carried information age did not:
  combining the two reached 0.924 on the full cohort, and it beat age-only by a
  wide margin once ages were matched (+0.225, 95% CI +0.089 to +0.361, p = .001).
- ~~"This dataset is bad."~~ The confound is common to the field; Bridge2AI is
  simply public enough to audit. The authors say the structure "is not unique to
  Bridge2AI."
- ~~"Voice AI can detect dementia at 0.809."~~ That figure is inseparable from
  site confounding by the authors' own analysis.
- ~~"Age restriction fixes confounding."~~ It handles age. Site remained, and
  identity cannot be handled this way at all.
- ~~"The 0.618 result proves the model doesn't generalise."~~ The authors
  specifically caution it conflates preprocessing mismatch with a genuine
  generalisation gap; it measures sensitivity to the pipeline.

# Bottom Line for Your Life

**The single most useful question in this whole reading list might be: *what
would a stupid model get?*** Every time you meet an impressive accuracy figure —
for a medical AI, a hiring algorithm, a fraud detector, a risk score — ask what
a one-variable model using the most obvious confounder would have achieved on
the same data. Here the answer was that a regression on age, costing seconds,
beat a transformer with 86.4 million parameters. That question is nearly free to
ask, it is devastating when the answer is bad, and of 13 published studies in
this field, not one had asked it.

**The second habit: when told that A predicts B, look for the shared parent.**
Not "is this correlation real?" — it almost always is — but "what else could be
causing both?" Age, sex, which hospital, which machine, how sick someone already
was. In this paper the answer was age, and it accounted for most of an entire
literature's headline numbers. Little's commentary sharpens it further: because
no one in these datasets appears as both a patient and a healthy person, each
individual's own distinctive voice is a second common parent that no
rebalancing can remove.

**And notice who found it.** Not a rival lab, not a regulator — trainees at a
summer school, within hours, with no expertise in the field, because someone had
set them the exercise of looking for bias. The technique required nothing anyone
reading this couldn't learn. What it required was the willingness to run the
comparison that could only make the result look worse. That is the whole skill,
and it is available to you on every paper anyone ever cites at you.

---

*Education, not medical advice. Decoded 2026-09-30 from the PubMed Central
open-access full texts of both papers. Derived calculations — the margin by
which age-only beat the transformer, the ladder of AUC estimates as each
confounder is removed, the collapse of the age-only score as the age gap
narrows, and the size of the cross-version drop — are labelled as derived and
were computed from the papers' own reported values.*
