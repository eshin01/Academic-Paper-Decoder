# When the AI Whispers the Wrong Answer, Do Doctors Listen?

**Paper:** Real-Time Artificial Intelligence Diagnostic Copilot in Simulated
Primary Care Consultations: Randomized Simulation Study
**Authors:** Cusacovich I, Pinilla M, Garcia Castro R
**Venue / Year:** JMIR Formative Research, 2026;10:e104579
**DOI:** https://doi.org/10.2196/104579
**PubMed:** https://pubmed.ncbi.nlm.nih.gov/42771885/
**Full text used:** https://pmc.ncbi.nlm.nih.gov/articles/PMC13597024/
**Basis of this analysis:** FULL TEXT (PubMed Central open-access copy,
retrieved 2026-09-25). Figures 1–4 and the supplementary CONSORT checklist were
not retrievable, so nothing here depends on a figure value.
**Date decoded:** 2026-09-25
**Evidence grade:** 4/5

---

# The Gist

Thirteen Spanish family doctors sat at home with headsets and talked to
fake patients — an AI playing a sick person out loud, in real time, over a
voice link. Each doctor did 20 of these consultations. For a random half of
them, a second AI listened in and quietly posted a running list of possible
diagnoses on the screen, plus suggestions for what to ask next. For the other
half, the doctor was on their own with nothing.

Afterwards, three other family doctors — who could not tell which
consultations had used the AI — graded whether the right answer was in the
doctor's final list.

With the AI listening in, doctors got the right diagnosis into their top three
about 75% of the time, versus about 65% without it. That is the headline, and
it is a real, randomized result.

But the study did a second thing that most AI studies skip, and it is the more
interesting half. The researchers went looking for the failure mode. They
counted the consultations where **the AI's own suggestion was wrong**, and
asked: did the doctor go along with it? When the wrong suggestion was on
screen, doctors echoed it 57% of the time. When the same wrong suggestion was
generated invisibly in the background — computed but never shown — doctors
landed on that same wrong answer only 40% of the time.

So the AI made doctors better on average, and also appears to have pulled them
toward its mistakes. The study was not big enough to prove the second part, and
the authors are careful to say so. That combination — a real benefit and an
unproven but plausible harm, honestly reported — is what makes this worth
reading.

# Study Snapshot

- **Study type:** A randomized, adjudicator-blinded **simulation study**. Real
  doctors, fake patients. This sits above the vignette and chart-review studies
  this reading list has mostly covered — it randomizes, which almost none of
  them did — but below a clinical trial, because no real patient was ever
  treated, helped, or harmed. The authors call it a "diagnostic stress test,"
  not a test of routine practice.
- **Participants:** 13 board-certified family and community medicine physicians
  from the Madrid regional health service, recruited through a shared link and
  social media. 8 women (62%), 5 men (38%). Median age 30 years (IQR 28–43),
  median 6 years of clinical experience (IQR 4–19). No more than one per clinic,
  to stop them comparing notes.
- **Consultations:** 260 total — each physician did 20. Randomization happened
  per case, not per doctor, so every doctor worked in both conditions.
- **Cases:** 40 deliberately difficult adult vignettes drawn from a peer-reviewed
  library previously validated by a separate panel of 7 primary care physicians.
  Chosen to be hard on purpose.
- **What was compared:** Real-time AI assistance (Medsys AI-Clinical Assistant
  V1.0.0, built on GPT-4o and GPT-4o-mini with retrieval over 1000+ Spanish
  clinical practice guidelines, no fine-tuning) versus an unassisted condition in
  which physicians were told to use **no external diagnostic aids at all**.
- **Patient simulator:** A separate GPT-4o Realtime voice system playing the
  patient. Deliberately walled off from the assistant — the assistant heard only
  the live conversation, never the underlying case file.
- **Main outcome:** "Top-3 diagnostic accuracy" — whether at least one of the up
  to three diagnoses the doctor submitted was correct.
- **Safety outcome:** Whether the doctor's *first* submitted diagnosis matched an
  AI suggestion that was wrong.
- **Who graded it:** 3 independent practicing family physicians, blinded to which
  arm each consultation came from. Majority rule. Agreement was excellent —
  Fleiss κ 0.902 (95% CI 0.864–0.937) for physician diagnoses.
- **How long:** Consultations ran April 1 to May 20, 2025.
- **Registration:** None. The authors explain why — no real patients, no care
  delivered, so trial registration did not apply. They did publish the protocol,
  the full 260-consultation dataset, adjudicator scores, statistical code, and a
  document mapping code output to manuscript numbers in a public repository.
- **Ethics:** A retrospective determination from the Research Ethics Committee of
  Hospital Universitario La Paz (reference 57/230428.9/26, 11 August 2026)
  confirming approval was not required. Physicians gave written informed consent
  and were not paid.
- **Funding:** **Not reported** in the text retrieved.
- **Conflicts of interest:** **No conflict-of-interest statement appears in the
  text retrieved.** However, one of the three authors lists their affiliation as
  Medsys AI, SL — the company that makes the system being tested. The system was
  supplied under licence from the manufacturer.

# How Strong Is This Evidence? — Grade 4/5

This is the strongest *design* this reading list has decoded in weeks, and the
grade reflects the design more than the conclusion.

**What this study did well:**

- **It randomized.** Almost every AI paper in this list compares a model against
  a historical dataset. This one allocated consultations by chance, at the case
  level, so every doctor served as their own comparison and individual skill
  cannot explain the gap.
- **It blinded the graders properly, and cleverly.** The AI's suggestions were
  generated in the background even for the unassisted consultations — so the
  adjudicators saw an AI suggestion attached to every case and genuinely could
  not tell which arm they were reading. That is a real piece of craft.
- **Agreement among graders was excellent and measured.** Fleiss κ of 0.902 with
  a tight confidence interval. Contrast this with yesterday's paper, where κ was
  0.16 and needed a page of explanation.
- **Nobody vanished.** All 260 randomized consultations were completed,
  adjudicated, and analyzed. No dropouts, no exclusions, no "completers only."
  That is rarer than it should be.
- **The statistics respect the structure of the data** (see Statistics Spotlight
  — this is the single best thing about the paper).
- **It went hunting for its own failure mode.** Most AI studies report average
  accuracy and stop. This one pre-specified a safety outcome about what happens
  when the AI is wrong.
- **Radical transparency.** Protocol, raw data, adjudicator scores, analysis
  code, and a document tying code output to every published number, all public.
- **The limitations section is unusually honest** — it names the rigged
  comparator, the circular subgroup metrics, and the small physician sample
  without being asked.

**What holds it back from a 5:**

- An author works for the company that makes the product, and no
  conflict-of-interest statement appears in the retrieved text.
- The comparator was deliberately stripped of the tools real doctors use.
- No sample size or power calculation appears anywhere in the retrieved text —
  which matters enormously for the safety finding.
- The safety signal is larger in absolute terms than the benefit signal and was
  reported as "not statistically significant."
- No real patient was involved, so no claim about clinical benefit survives.

# The Editor's Concerns

**The comparator was given nothing, and that inflates the gap.** Physicians in
the unassisted arm were instructed not to use any outside diagnostic aid — no
guidelines, no point-of-care reference, no internet search, no phoning a
colleague. Real family doctors use all of those constantly. So this measures
"AI versus a doctor with empty hands," not "AI versus a doctor working
normally." The authors state this plainly and even say the effect "should not
be interpreted as the incremental effect of AI over resource-enabled usual
care." Credit to them. But the +12.3 percentage points will be quoted for
years without that sentence attached.

**The safety number is bigger than the benefit number, and gets softer
language.** The benefit was an adjusted +12.3 percentage points on accuracy.
The safety finding was an adjusted **+17.0 percentage points** more
agreement with wrong AI suggestions (95% CI −2.7 to +36.8). In crude counts:
29 of 51 risk consultations (56.9%) versus 19 of 47 (40.4%). The benefit is
described as an association the study supports; the harm is described as "a
possible overreliance signal" that "did not reach statistical significance."
Both come from the same 260 consultations and the same modelling machinery.
One is a headline and one is a hedge.

To be fair to the study, the harm applies only within the roughly 36% of
AI-assisted consultations where the AI was wrong (51 of 140). *Deriving*
from the paper's numbers: 36.4% × 17.0 points ≈ **6.2 percentage points** of all
AI-assisted consultations where a doctor may have adopted a wrong answer they'd
otherwise have avoided, against 12.3 points where they got it right. So the
net still favours the AI, roughly two to one — but that is a far narrower
margin than the abstract conveys, and it rests on a harm estimate the study
could not measure precisely.

**No power calculation appears anywhere.** With 13 physicians, the safety
analysis returning p = .09 is close to meaningless as reassurance. An
underpowered safety test that comes back "not significant" is the most
misleading result in medicine, and it deserves a section of its own below.

**The primary outcome is the most forgiving of the three measured, and the
strictest one failed.** Getting the right answer into a list of three was
significant (p = .01). Getting it into a list of two was significant
(p = .01). Getting it *right* — first diagnosis correct — was not
(50.8% versus 56.4%; adjusted +9.2 points, 95% CI −1.0 to +20.1, p = .08).
Top-3 was genuinely prespecified as primary and Top-1 was post hoc, so this is
not outcome-switching. But notice the mechanism: the AI displays a *running
list* of candidate diagnoses, and the doctor may submit *three*. A physician
who simply copies the AI's top three scores a win on the primary endpoint. The
outcome most sensitive to AI benefit is also the one most sensitive to the
copying behaviour the safety analysis was designed to detect.

**The subgroup findings are mathematically circular, and the authors say so.**
"Case difficulty" was *defined as* one minus the mean accuracy in the unassisted
arm. "Physician ability" was *defined as* that physician's unassisted
performance. Both were then used to explain how much the AI helped — which is
the difference between the two arms, one of which is the very thing the
moderator was built from. You cannot avoid finding a relationship there. It is
the same mathematical coupling trap as regression to the mean. The paper flags
it as hypothesis-generating; anyone quoting "the AI helped most on hard cases"
should flag it too.

**One subgroup result points the other way and deserves more air.** In the
*easiest* quartile of cases, AI assistance made doctors **worse** by 7.7
percentage points (95% CI −16.3 to −0.6) — a confidence interval that excludes
zero. Subject to the same circularity caveat, that is the same direction as the
overreliance signal: when the doctor didn't need help, the AI's presence hurt.

**Thirteen physicians, median age 30, one Spanish region, recruited via social
media.** They had to be comfortable enough with technology to run a voice-based
web app from home. That is not the average family doctor. The
leave-one-physician-out analysis is a nice robustness check, but as the paper
correctly notes, it tests whether one person drove the result — not whether the
result travels to other countries, other training backgrounds, or less
digitally confident clinicians.

**The AI cost time.** Consultations ran 10.7% longer with assistance (mean 364
versus 329 seconds, p = .04). In a ten-minute appointment slot that is not
free.

**And the copilot premise itself went unproven.** In an exploratory comparison,
physicians did not significantly outperform the AI running alone in either
arm, and the interaction test was null. The authors state it directly: these
findings "do not establish additive human-AI synergy." The whole point of a
copilot is that pilot plus copilot beats either one. This study cannot show
that.

# Statistics Spotlight

## Concept 1 — Clustering: why 260 consultations are not 260 independent facts

This is the most important idea in the paper, and the paper handles it
correctly, which makes it a good place to learn it.

The study has 260 consultations. It does **not** have 260 independent pieces of
evidence. Those 260 consultations came from only **13 doctors** and only
**40 cases**. Every consultation shares a doctor with 19 others and shares a
case with several more.

**Why that matters.** Suppose one of the 13 doctors is simply excellent. All 20
of their consultations will tend to be graded correct, in both arms. Those 20
results are not 20 separate votes on whether AI works — they are closer to one
vote, cast twenty times. The same goes for cases: if case #17 is nearly
impossible, everyone gets it wrong, and those observations move together.

Statisticians call this **clustering**: observations sitting inside the same
group resemble each other more than they resemble observations from other
groups.

**What goes wrong if you ignore it.** Standard statistics assume every
observation is independent. Feed 260 clustered observations into an ordinary
test and it believes it has 260 independent facts when it effectively has far
fewer. The result: confidence intervals come out **too narrow**, p-values come
out **too small**, and you declare victory on a result that is really just one
enthusiastic doctor repeated twenty times.

**An everyday version.** You want to know if a new teaching method works, so you
test 300 children. But those 300 children sit in 10 classrooms of 30. If one
teacher is outstanding, their 30 children all score well — that's one good
teacher, not 30 independent confirmations. Analysing it as 300 independent
children would make a mediocre method look conclusively proven.

**What this paper did instead.** It fitted a **generalized linear mixed model**
with **random intercepts for physician and for case**. In plain terms: the model
gives every doctor their own private baseline skill level and every case its own
private difficulty level, and estimates the AI effect *after* allowing for both.
So a strong doctor's good scores get attributed to that doctor rather than
credited to the AI.

You can see the machinery working. The crude numbers were 65% versus 75% — a
10-point gap. After the model accounted for who did which case, the adjusted
figures were 62.3% versus 74.6%, a **12.3**-point gap with a confidence interval
running from +2.7 to +22.6 points. That interval is wide precisely *because* the
model is honest about only having 13 doctors. A naive analysis would have
reported a much tighter, much more confident-looking interval — and it would
have been wrong.

**Watch out for:** any study reporting a large number of observations collected
from a small number of people, sites, hospitals, or raters — repeated
measurements on patients, multiple images per person, several questions per
participant, patients clustered within clinics. Ask: *how many independent
units are really here?* If the paper reports its sample size as the number of
observations and never mentions clustering, mixed models, random effects, or
"robust standard errors," treat every p-value in it with suspicion. Here, the
honest answer to "what is the sample size?" is closer to **13** than to 260.

## Concept 2 — Number needed to treat: turning a percentage into a person

The paper reports a "simulation-context NNT-equivalent of 8.1 (95% CI 4.4 to
37.2)." This is worth knowing because NNT is the single best tool for
translating a statistical result into something you can picture.

**What it is.** Number needed to treat answers: *how many people must get this
intervention for one extra person to benefit?* The arithmetic is simply one
divided by the absolute difference:

> NNT = 1 ÷ absolute risk difference

Here the absolute difference was 12.3 percentage points, or 0.123. So
1 ÷ 0.123 ≈ **8.1**. Meaning: run about **8 consultations with the AI switched
on, and one extra consultation ends up with the right diagnosis in the list**
that would otherwise have missed it. The other seven would have come out the
same either way.

**Why it beats a percentage.** "A 32.6% relative reduction in errors" and
"12.3 percentage points" and "NNT of 8" are the same fact. But relative
reductions are slippery — a 50% reduction sounds identical whether it takes you
from 2% to 1% (NNT 100) or from 40% to 20% (NNT 5). NNT forces the absolute
scale back into view. For comparison, statins for primary prevention of heart
attack have NNTs in the range of many dozens over years, and are still worth
taking. An NNT of 8 for a single consultation is, on its face, a big effect.

**The two watch-outs, both live here.**

*First, read the interval.* The NNT is 8.1, but its 95% confidence interval runs
from **4.4 to 37.2**. The data are compatible with "one extra correct diagnosis
for every 4 consultations" — excellent — and equally compatible with "one for
every 37" — marginal. That range is wide because 13 physicians is not many.
Quoting "8.1" alone hides most of what the study does not know.

*Second, NNT is not portable.* It depends entirely on the baseline. These cases
were chosen to be hard, and the comparison doctor had no reference tools. In
ordinary primary care, where most presentations are common and doctors can look
things up, the baseline accuracy would be far higher and the room to improve far
smaller — so the real-world NNT would be much bigger, meaning much less benefit
per consultation. The authors say exactly this, and it is why they call it an
"NNT-equivalent" rather than an NNT.

**The mirror image worth knowing: NNH, number needed to harm.** Same formula,
applied to the bad outcome. The safety analysis found a 17.0 percentage point
increase in agreeing with wrong suggestions, which gives 1 ÷ 0.17 ≈ **6**. In
other words, *within the consultations where the AI was wrong*, roughly one in
every six doctors may have been pulled into an error they'd otherwise have
avoided. Holding the benefit (NNT ≈ 8) next to the harm (NNH ≈ 6) is a far more
honest summary than either number alone — though both estimates are imprecise.

## Concept 3 — An underpowered safety result is not a safety clearance

The safety analysis returned p = .09 and was described as "not statistically
significant." It is essential to understand what that does and does not mean.

**It does not mean "no harm was found."** It means "this study was not able to
tell the difference between no harm and quite a lot of harm."

The honest way to read any non-significant result is to ignore the p-value and
look at the confidence interval. Here it was **−2.7 to +36.8 percentage
points**. Read it out loud: the data are consistent with the AI making doctors
very slightly *less* likely to follow a wrong suggestion (−2.7), and equally
consistent with it making them **36.8 points more likely** — which would be a
serious safety problem. The interval contains zero, so the test is
"non-significant." The interval also contains a catastrophe.

**Why this keeps happening.** Studies are usually powered — sized — to detect
the *benefit* they hope to find. The safety question is then asked of whatever
data happen to be lying around. Here the safety analysis ran on only the 98
consultations where the AI was wrong (51 in one arm, 47 in the other), from 13
doctors. That is a small study inside a small study. No sample size calculation
appears anywhere in the retrieved text, so we cannot even say what this analysis
was capable of detecting.

**The asymmetry to remember.** For benefits, we demand strong evidence before
believing a drug works — the burden of proof sits on the claim. For harms, that
logic inverts and becomes dangerous: demanding statistical significance before
taking a safety signal seriously means rare and moderate harms are systematically
dismissed. This is not a hypothetical failure mode; it is roughly the history of
several drug withdrawals.

**An everyday version.** You test a smoke alarm four times. It fails once. Four
tests can't prove the failure rate differs from zero — p would be nowhere near
significant. Nobody sane concludes the alarm is fine. You conclude you need more
tests, and meanwhile you don't trust the alarm.

**What honest phrasing looks like.** Compare "no significant increase in
overreliance was observed" — which sounds like reassurance and is the sentence
that gets quoted — with "this study could not rule out an increase of up to 37
percentage points in agreement with incorrect AI suggestions." Same result. To
their considerable credit, the authors of this paper lean toward the second:
they call it a "possible overreliance signal," say the estimate was "imprecise,"
and conclude the system is *not* ready for deployment. That is what good faith
looks like. Watch what happens to this finding when other people cite it.

# Jargon Translator

- **Simulation study:** Real clinicians, fake patients. Lets you test risky
  things safely; cannot tell you what happens with real illness.
- **Case-level randomization:** The coin was flipped for each consultation, not
  each doctor — so every doctor worked in both conditions and their personal
  skill affects both arms equally.
- **Adjudicator-blinded:** The people grading the answers didn't know which arm
  each answer came from, so their expectations couldn't tilt the scores.
- **Top-3 accuracy:** Was the right answer anywhere in the doctor's list of up to
  three? Top-1 is the stricter version: was their *first* answer right?
- **Adjusted odds ratio (AOR):** How much the odds of a correct diagnosis
  changed with AI, after accounting for doctor and case. 2.68 means the odds
  roughly 2.7×. Odds ratios exaggerate when outcomes are common — which is why
  the +12.3 percentage point figure is the more useful one.
- **Absolute risk difference:** Straight subtraction of one percentage from the
  other. The most honest single number in any trial.
- **Relative error reduction (RER):** Errors fell 32.6% *relative to* the
  unassisted error rate — from 35% of consultations wrong to 25%. Relative
  figures always sound bigger than absolute ones.
- **Random intercept:** Giving each doctor and each case its own baseline in the
  model, so their quirks don't get mistaken for the treatment effect.
- **Profile-likelihood confidence interval:** A more accurate way of drawing
  error bars than the usual formula, useful with small samples and skewed data.
- **Parametric bootstrap:** Simulating the study thousands of times (10,000 here)
  from the fitted model to see how much the answer wobbles.
- **Gauss-Hermite integration:** Mathematical machinery for averaging model
  predictions across all the doctor- and case-level variation. 30 nodes = 30
  points of numerical precision.
- **Likelihood-ratio test:** Compares a model with the AI effect against one
  without it, and asks whether the extra term earns its keep. Source of the
  χ² values.
- **Risk scenario:** A consultation where the AI's own leading suggestion was
  wrong — the subset used for the safety analysis.
- **Automation bias / overreliance:** The documented human tendency to defer to a
  machine's recommendation even when your own judgement was better.
- **Retrieval-augmented generation (RAG):** The AI looks answers up in a curated
  document library — here, 1000+ Spanish clinical guidelines — before replying.
- **Leave-one-physician-out analysis:** Re-run the whole analysis 13 times, each
  time dropping a different doctor, to check no single person drove the result.
  Here the effect stayed between +9.2 and +14.3 points — reassuringly stable.
- **Fleiss κ:** Agreement among three or more raters, corrected for chance. 0.902
  here is excellent.
- **Welch's t test:** A comparison of two means that doesn't assume the two
  groups have equal spread. Used for consultation times.

# What You Can (and Can't) Say

**Fair to say:**

- In a randomized simulation with 13 Spanish family doctors and 260
  consultations, a real-time AI assistant raised the chance the right diagnosis
  appeared in the doctor's top three from about 65% to about 75%.
- The effect survived leaving out any single doctor, and survived dropping the
  16 consultations where the fake patient misbehaved.
- The cases were chosen to be unusually hard, and the comparison doctor was
  allowed no reference tools at all.
- When the AI's suggestion was wrong and visible, doctors agreed with it 57% of
  the time, versus 40% when the same wrong suggestion was never shown — a signal
  consistent with overreliance, which this study was too small to confirm.
- Benefit was concentrated in harder cases and less accurate doctors; on the
  easiest quarter of cases the AI appeared to make doctors slightly worse. These
  subgroup findings are circular by construction and should be treated as
  hypotheses.
- AI-assisted consultations took about 11% longer.
- The authors' own conclusion is that the system is **not** ready for clinical
  deployment and needs prospective testing in real workflows.

**Not fair to say:**

- ~~"AI makes doctors better at diagnosis."~~ It made 13 self-selected young
  doctors better at a curated set of hard fake cases while forbidden from using
  a textbook. No real patient was diagnosed.
- ~~"AI improves diagnostic accuracy by 12 percentage points."~~ Against a
  comparator deliberately stripped of the tools doctors actually use. The
  authors explicitly warn against this reading.
- ~~"The study found no safety problem."~~ It found a 17-point gap it lacked the
  power to confirm, with an interval reaching +36.8 points. That is "couldn't
  tell," not "nothing there."
- ~~"Doctors plus AI beat AI alone."~~ Directly tested and not demonstrated. The
  paper says the data "do not establish additive human-AI synergy."
- ~~"You'd only need to use it 8 times to help someone."~~ The interval runs from
  4.4 to 37.2, and the number applies to hard cases with an unaided comparator.
- ~~"This proves AI is ready for the clinic."~~ The authors say the opposite in
  their own conclusion.

# Bottom Line for Your Life

**The finding that should stick with you is the one about the invisible
suggestion.** The researchers computed the AI's answer for *every* consultation,
but only showed it in half of them. That single design choice is what makes the
overreliance number interpretable — without the hidden-suggestion arm, you'd
have no way to separate "the doctor and the AI made the same mistake because
the case is genuinely misleading" from "the doctor made that mistake *because
the AI said so*." The gap between 40% and 57% is the closest thing anyone has to
a measurement of the second thing. Remember that trick; it's how you tell
influence from coincidence.

**The practical lesson for reading any AI study: check what the human was
allowed to use.** An AI that beats a doctor with no reference materials, no
guidelines, and no colleague to ask has cleared a bar nobody in practice
actually stands at. This paper is unusually honest about that. Most aren't. When
you see a human-versus-AI comparison, the first question is never "how good was
the AI?" — it's "what did you take away from the human?"

**And the habit worth building: when a study says "not statistically
significant," ask what the confidence interval was.** "No significant increase
in overreliance" and "we could not rule out a 37-point increase in overreliance"
describe the identical result. One sounds like safety. The other is the truth.
Almost every time you see a reassuring null result about a harm — in a drug
trial, a device study, a workplace exposure report — this question is the one
that opens it up.

---

*Education, not medical advice. Decoded 2026-09-25 from the PubMed Central
open-access full text. Every figure quoted comes from the article body or
Tables 1–3; the two derived calculations (the 6.2-percentage-point net harm
estimate and the NNH of roughly 6) are labelled as derived and were computed
from the paper's own reported values.*
