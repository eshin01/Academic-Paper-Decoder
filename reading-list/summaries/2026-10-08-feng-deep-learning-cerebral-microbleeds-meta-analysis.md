# Forty-Two Studies, Fourteen Tables, and One Number That Cannot Be Right

**Paper:** Accuracy of Deep Learning in Detecting Cerebral Microbleeds: Systematic
Review and Meta-Analysis
**Authors:** Feng Y, Zheng L, Zhang B, Zou W
**Venue / Year:** Journal of Medical Internet Research, 2026;28:e95041 (published
2026-09-21)
**DOI:** https://doi.org/10.2196/95041
**PubMed:** https://pubmed.ncbi.nlm.nih.gov/42767630/
**Full text used:** https://pmc.ncbi.nlm.nih.gov/articles/PMC13639419/
**Registration:** PROSPERO **CRD42024628447**, registered **prospectively**
**Basis of this analysis:** FULL TEXT (PubMed Central open-access copy,
retrieved 2026-10-08). Table 1, the study-characteristics table, rendered in full
and is used below. Figures 1–5 and all fourteen supplementary figures did not
render, so **the forest plots, the SROC curves, the QUADAS-2 figures, Deeks'
funnel plots and the Fagan nomograms were not seen** — only the numeric values
quoted for them in the body text. The complete search strategy (Table S1) was
also not retrievable.
**Date decoded:** 2026-10-08
**Evidence grade:** 3/5

All identifiers were verified against the live PubMed and PubMed Central records
on 2026-10-08. Nothing here rests on a guessed or reconstructed link.

Chosen today because it is the next unchecked queue entry and it **finally became
reachable**: this paper had no PubMed Central copy for sixteen days of daily
checks, and gained PMC13639419 overnight. The sixth time a "re-check rather than
abandon" entry has paid off.

---

# The Gist

**Cerebral microbleeds** are tiny old specks of bleeding in the brain, a few
millimetres across, visible on the right kind of MRI as small dark dots. They
matter because they are a signpost: where they sit in the brain helps distinguish
high-blood-pressure damage from cerebral amyloid angiopathy, and they bear on
decisions about dementia, stroke and whether it is safe to give blood thinners.

Counting them is miserable work. A radiologist scrolls through hundreds of image
slices hunting for dots that look much like calcium deposits, normal iron
deposits, and scanner artefacts. So this is an obvious job for a computer, and
this team set out to answer the sensible question: across everything published,
how accurately does deep learning actually find them?

They did the groundwork properly. The review was **registered in PROSPERO before
they started**, reported against PRISMA, appraised with QUADAS-2, and two
reviewers screened independently with their agreement reported (κ = 0.891). From
462 records they arrived at **42 studies**.

Then comes the finding that makes this paper worth reading, and the authors
deserve real credit for it, because most reviews would have buried it. They split
the results two ways:

- **Lesion level** — show the model a small patch of brain and ask "is there a
  microbleed in this patch?" Pooled sensitivity **0.96**, specificity **0.98**,
  area under the curve **0.99**. Near-perfect.
- **Patient level** — show the model a whole brain scan and ask "does this person
  have microbleeds?" Pooled sensitivity **0.89**, specificity **0.86**, AUC
  **0.93**.

That second set is the clinical question, and look at what happens to the false
alarms: 2 per 100 healthy people at the lesion level, **14 per 100** at the
patient level — a **sevenfold** increase. The authors explain exactly why, and
their explanation is excellent: a patient-level call means integrating "hundreds
to thousands of image patches across the entire brain," and a whole brain is full
of things that mimic microbleeds — vascular calcification, normal iron in the
basal ganglia, motion and metal artefacts, all of which are "extremely common in
older adults."

So the headline accuracy belongs to the easy version of the task.

Now the problem. The Results section says "42 studies were incorporated in the
meta-analysis." Buried in the risk-of-bias section is this: "**33 studies
provided only limited outcome data and could not be directly included in the
current meta-analysis.**" Forty-two minus thirty-three leaves **nine**. The
pooled numbers come from **5 contingency tables** at the patient level and 9 at
the lesion level — fourteen tables from at most nine studies, meaning some
studies were counted at both levels.

**78.6% of the studies in this review contributed nothing to any number in its
abstract.** And the entire patient-level clinical claim — the one that matters —
rests on **415 patients, 134 of whom had microbleeds.**

With samples that small, one reported figure collapses on inspection. The
sensitivity analysis reports a **diagnostic odds ratio of 1,738, with a 95%
confidence interval from 174 to 17,385** — a range spanning a **hundredfold**.
That is not an estimate of anything.

And one interval is internally impossible. I will show the arithmetic below, but
briefly: a confidence interval around a ratio should have the point estimate at
its geometric centre, and eleven of the twelve ratio intervals in this paper do.
The twelfth does not, and the lower bound that *would* make it work is **20.2**,
not the printed **9.3**.

# Study Snapshot

- **Study type:** Systematic review and **diagnostic test accuracy
  meta-analysis**, prospectively registered.
- **Registration:** PROSPERO CRD42024628447.
- **Reporting standard:** PRISMA. Risk of bias: QUADAS-2.
- **Searched:** IEEE, Web of Science, Embase, the Cochrane Library and PubMed, to
  1 November 2024, with the search **updated on 5 July 2026**. No language, date
  or study-type restrictions in the search itself (though English-only was an
  inclusion criterion).
- **Selection funnel:** 462 retrieved → 106 duplicates removed → 356 screened on
  title and abstract → 295 excluded → 61 full texts read → excluded 1 retracted
  article, 5 without deep learning, 2 that did not distinguish microbleeds from
  other disease, and 11 unpublished conference abstracts → **42 studies**. Every
  step reconciles.
- **Screening reliability:** two independent reviewers, **κ = 0.891**, a third
  investigator resolving disagreements.
- **The 42 studies:** published 2015–2026, from 9 countries, **all case-control**.
  26 single-centre, 11 multicentre, the rest mixed or unspecified. 40 binary
  classification tasks, 2 multiclass. Almost all MRI, dominated by
  susceptibility-weighted imaging (20 studies used SWI alone).
- **Validation design across the 42:** 23 used random sampling only; 6 k-fold
  cross-validation; 4 k-fold plus external validation; 4 random sampling plus
  external validation; 1 external validation only; the remainder other
  combinations. So **the large majority had no external validation at all.**
- **Statistical model:** bivariate mixed-effects model, pooling sensitivity,
  specificity, positive and negative likelihood ratios, diagnostic odds ratio and
  a summary ROC curve. Stata. Where studies did not supply a 2×2 table, tables
  were **reconstructed** from reported sensitivity, specificity, accuracy and case
  counts.
- **How many tables were actually pooled:** **5** at the patient level, **9** at
  the lesion level — the latter split into 5 directly extracted and 4
  reconstructed.
- **Patient-level results (5 tables, 134 cases / 415 total, 32% prevalence):**
  sensitivity **0.89** (95% CI 0.76–0.96), specificity **0.86** (0.77–0.92),
  PLR **6.3** (3.5–11.6), NLR **0.13** (0.05–0.32), DOR **50** (12–212), AUC
  **0.93** (0.91–0.95).
- **Lesion-level results (9 tables, 12,430 / 33,909, 37%):** sensitivity **0.96**
  (0.93–0.98), specificity **0.98** (0.94–0.99), PLR **39.5** (16.8–92.7), NLR
  **0.04** (0.02–0.07), DOR **1061** (293–3848), AUC **0.99** (0.98–1.00).
- **Directly extracted subgroup (5 tables, 11,357 / 25,248, 45%):** sensitivity
  **0.98** (0.95–0.99), specificity **0.98** (0.90–0.99), PLR **40.2**
  (9.3–79.9 — see concerns), NLR **0.02** (0.01–0.05), DOR **1738**
  (174–17,385), AUC 0.99.
- **Reconstructed subgroup (4 tables, 1,073 / 8,661, 12%):** sensitivity **0.95**
  (0.89–0.97), specificity **0.98** (0.96–0.99), PLR **41.2** (21.2–79.9), NLR
  **0.06** (0.03–0.12), DOR **736** (224–2418), AUC 0.99.
- **Clinical translation:** Fagan nomograms assuming a **30%** pre-test
  probability give, at the patient level, a positive predictive value of **73%**
  and a negative predictive value of **95%**; at the lesion level, 94% and 98%.
- **Publication bias:** Deeks' funnel plot, reported as non-significant at each
  level (p = .37, .51, .60, .51).
- **Heterogeneity:** **no I², no tau², no quantitative heterogeneity statistic is
  reported anywhere.** The limitations acknowledge "considerable clinical and
  methodological heterogeneity" in words only.
- **Risk of bias judgments:** patient selection **high** for all 42 (all
  case-control, with a well-argued explanation); index test **low**; reference
  standard **high or unclear** (13 studies blinded, 5 explicitly not, **24
  unspecified**); flow and timing no high risk; applicability **high** for 33
  studies because of limited outcome data.
- **A sophisticated limitation the authors raise themselves:** QUADAS-2 "did not
  explicitly assess AI-specific risks, such as the risk of data leakage between
  the training and validation sets, the adequacy of external validation, and
  generalizability across scanning devices," and QUADAS-AI "was not yet officially
  available at the start of our evaluation."
- **Funding and competing interests:** **not stated in the text retrieved.**

# How Strong Is This Evidence? — Grade 3/5

Three out of five: the process was done properly and the central qualitative
finding is sound and valuable, but the pooled numbers are built on far less than
the review appears to contain, and several of them are reported with a precision
the data cannot support.

**What earns the points.**

**Prospective registration in PROSPERO.** Registered before the work began, with
an ID a reader can check. This list has now seen enough protocols to know how
much that constrains later choices.

**The patient-versus-lesion distinction is the paper's real contribution, and it
is handled beautifully.** Most reviews in this space pool everything and report
one impressive number. These authors separated the two levels, reported both,
noted that lesion-level results are "relatively simple" while patient-level
"more closely reflected whether an individual had CMBs in the actual clinical
settings," and gave a correct three-part mechanistic account of the gap:
heterogeneous lesion distribution, mimics that are "extremely common in older
adults," and image-quality variation amplified when a single bad slice can
swing a whole-patient judgment. That is the right analysis and the right lesson.

**They drew the correct clinical conclusion from it.** Not "AI detects
microbleeds accurately," but that clinical decisions "cannot rely solely on the
model's imaging output," that the tool is "an efficient screening or
interpretation tool," and that its output "still needs to be combined with
clinical information and ultimately confirmed by imaging experts, rather than
serving as an independent diagnostic basis." A review that reports an AUC of
0.99 and then refuses to recommend standalone use is being honest against its
own headline.

**They rated patient selection as high risk for all 42 studies and explained
why, in domain terms rather than box-ticking.** The explanation — that in
image-based deep learning, case and control groups "may differ in image
acquisition equipment, scanning parameters, or preprocessing procedures," so
these "directly impact the model input variables," and that including only
"extreme typical cases or healthy controls deviated significantly from clinical
target populations" — is better reasoning than most QUADAS-2 assessments contain.

**They reported screening reliability** (κ = 0.891) rather than merely asserting
that two reviewers agreed.

**They ran a sensitivity analysis on their own data-reconstruction step,**
pooling the five directly extracted tables separately from the four
reconstructed ones, and reported that the conclusions held. That is exactly the
right check to run when you have had to rebuild 2×2 tables from summary
statistics.

**They raised the QUADAS-AI gap against themselves.** Acknowledging that their
chosen appraisal tool does not cover data leakage, external-validation adequacy,
or cross-scanner generalisability — the three failure modes most likely to
inflate AI diagnostic accuracy — is a level of methodological self-awareness
this list has rarely seen.

**They identified the external-validation signal** even though they could not
quantify it: models "demonstrated lower sensitivity in the external validation
set than in the random sampling and cross-validation sets," and the current
evidence base "is largely derived from internal validation."

**What costs the points.**

**One: 78.6% of the included studies contributed nothing to the pooled
estimates.** "Ultimately, 42 studies were incorporated in the meta-analysis"
appears in the Results. "33 studies provided only limited outcome data and could
not be directly included in the current meta-analysis" appears in the
risk-of-bias section, several pages later. Both cannot be true in the sense a
reader will take. The honest headline is *nine studies, fourteen contingency
tables*. The abstract does say "At the patient level, 5 studies were included,"
which is to its credit — but the 42 is what will be cited.

**Two: the patient-level claim rests on 415 patients.** Five tables, 134 cases.
Every clinically relevant number in this paper comes from that. A pooled
sensitivity of 0.89 with a confidence interval from **0.76 to 0.96** is
compatible with a model that misses one in four cases and with one that misses
one in twenty-five. That interval is the result, and it is too wide to act on.

**Three: a diagnostic odds ratio of 1,738 with a hundredfold confidence
interval.** 174 to 17,385. Reported as a sensitivity analysis on five tables,
and then quoted in the abstract without comment. When sensitivity and
specificity both sit near 0.98 in a handful of small studies, the DOR explodes
and its interval explodes faster. The number should have been suppressed or
presented purely as "too imprecise to interpret."

**Four: one confidence interval cannot be right.** The directly extracted
subgroup's positive likelihood ratio is given as **40.2 (95% CI 9.3–79.9)**. For
a ratio measure the point estimate should sit at the geometric centre of its
interval, and √(9.3 × 79.9) = **27.3**, not 40.2. Eleven of the twelve ratio
intervals in this paper pass that check; this one fails by 47%. Solving for the
lower bound that *would* give 40.2 against an upper bound of 79.9 yields
**20.2** — and √(20.2 × 79.9) = 40.2 exactly. A digit transposition from 20.2 to
9.3 explains it completely. A second reason to doubt that line: its upper bound,
79.9, is **identical** to the reconstructed subgroup's upper bound, which would
be a remarkable coincidence.

**Five: no heterogeneity statistic anywhere.** No I², no tau², no prediction
interval. The limitations concede "considerable clinical and methodological
heterogeneity... across different imaging protocols, study populations, model
characteristics, sample sizes, and validation methods" — which is precisely the
situation in which a reader needs a number. Earlier in this reading list, a
network meta-analysis (entry 31) earned 5/5 partly for knowing when *not* to
pool. This review pools five tables across different scanners, sequences, field
strengths and countries and reports no measure of how much they disagree.

**Six: publication-bias tests on four to nine studies, reported as
reassuring.** Deeks' funnel plot is the right tool for diagnostic accuracy
reviews, and it has almost no power below about ten studies. Four
non-significant p-values from pools of 5, 9, 5 and 4 tables are not evidence of
no publication bias; they are the expected output of an underpowered test. The
paper states "no significant publication bias" four times without that caveat.

**Seven: the threshold-effect interpretation reads backwards.** "The correlation
coefficient was 1.00, suggesting no significant threshold effect" — for the
patient-level pool, and again for the reconstructed subgroup. In a bivariate
model, a strongly positive correlation between sensitivity and specificity
across studies is the *signature* of a threshold effect, not its absence. A
correlation of exactly 1.00 estimated from five studies is more likely a
boundary artefact of fitting a random-effects model to too few data points than
a meaningful quantity. Either way it needs explaining, and as written the
sentence does not parse.

**Eight: "the proportion of positive vessels."** This phrase introduces all four
pooled analyses. No vessels are being classified anywhere in this paper — the
units are patients and lesions. It is a copy-paste from a different review, and
while harmless to the numbers, it is the kind of thing that makes a reader
wonder what else was carried over.

**Nine: the Fagan analysis uses the most favourable prevalence in the paper's
own range.** The introduction cites microbleed prevalence of **5% to 35.7%**. The
nomograms assume **30%**. At 30% the patient-level positive predictive value is
73%, which reproduces exactly. At 5% it falls to **25%** — three of every four
positive calls would be wrong. Both numbers are defensible; presenting only the
first is not.

**Ten: "significantly lower" with no number.** The external-validation finding is
reported as "the sensitivity reported by a few studies implementing external
validation was significantly lower than that of internally validated models in
the same studies," while the same paragraph says the subgroup analysis "could not
be performed." A claim of statistical significance without a test, an effect size
or a count is not a finding; it is an impression. It is probably the most
important impression in the paper, which is why it needs a number.

# The Editor's Concerns

**Change the Results sentence and the abstract to say what was pooled.** "Nine of
42 studies supplied extractable 2×2 data; 14 contingency tables were pooled (5
patient-level, 9 lesion-level)." This is a one-line fix and it is the single most
important one.

**State whether the same studies appear in both pools, and handle the
dependency.** Fourteen tables from at most nine studies means overlap. If a study
contributed both a patient-level and a lesion-level table, the two pooled
analyses are not independent, and any comparison between them — which is the
paper's central claim — needs to account for that. At minimum, name which studies
appear where.

**Withdraw or quarantine the DOR of 1,738.** A hundredfold interval is not
reportable as a point estimate. If it stays, label it "too imprecise for
interpretation" in the abstract.

**Correct the directly extracted PLR interval.** The arithmetic above identifies
20.2 as the almost certain lower bound. Please check the Stata output.

**Report I² and tau² for every pool, plus a prediction interval.** With this much
acknowledged clinical and technical heterogeneity, a reader needs to know the
spread, not just the average. A prediction interval — the range a *new* study
would be expected to fall in — is far more useful here than a confidence
interval on the mean.

**Add the standard caveat to every publication-bias test,** or drop them. "Deeks'
test has insufficient power with fewer than ten studies; the absence of a
significant result should not be interpreted as absence of bias."

**Explain the correlation coefficient of 1.00,** and reconsider whether a
bivariate random-effects model is estimable at all on five studies. A simpler
fixed-effect summary, or a narrative synthesis with a forest plot and no pooled
point estimate, may be the honest choice at the patient level.

**Give the external-validation comparison a number,** even descriptively: how
many studies, what their internal and external sensitivities were, paired. Four
to five paired observations reported as a table would be more valuable than the
entire pooled DOR analysis, because it addresses the question clinicians
actually have.

**Present the Fagan analysis across the prevalence range**, at 5%, 15% and 30%,
so a reader in a low-prevalence setting can see their own numbers.

**Fix "positive vessels"** throughout.

**State funding and competing interests.**

**And a suggestion rather than a complaint:** the 33 excluded-from-pooling studies
are not wasted. A structured narrative synthesis of what they reported — their
sensitivities, their validation designs, whether they compared against clinicians
— would turn the review's greatest weakness into a contribution, and would let
the authors say something about the field's reporting practices that nobody else
is positioned to say.

# Statistics Spotlight

Five ideas. The third is a thirty-second audit that found this paper's error, and
it is the most immediately useful thing in this summary.

## 1. The diagnostic odds ratio, and when a ratio stops meaning anything

A diagnostic test produces four numbers: true positives, false positives, true
negatives, false negatives. There are many ways to summarise them, and this paper
reports most of them. The **diagnostic odds ratio (DOR)** is the most compressed:
it is how much more likely a positive result is in someone with the disease than
in someone without, expressed as a single number.

It has a simple identity worth knowing:

> **DOR = positive likelihood ratio ÷ negative likelihood ratio**

Check it on the patient-level numbers: PLR 6.3 ÷ NLR 0.13 = **48.5**, against the
reported DOR of **50** — the gap is rounding in the published PLR and NLR. On the
lesion level: 39.5 ÷ 0.04 = 988 against a reported 1061, again rounding.

A DOR of 1 means the test is useless. Higher is better, and it climbs very fast:
because it multiplies two ratios that are both improving, a test that goes from
90% to 98% sensitivity and specificity sees its DOR go from about 81 to about
2,400.

That steepness is also its weakness, and this paper demonstrates it. Here are the
four reported DORs with the width of their confidence intervals:

> patient level **50** (12–212) — a **17.7-fold** range
> lesion level **1061** (293–3848) — **13.1-fold**
> directly extracted **1738** (174–17,385) — **99.9-fold**
> reconstructed **736** (224–2418) — **10.8-fold**

A hundredfold interval. The honest reading of "DOR = 1738, 95% CI 174 to 17,385"
is *we cannot tell*. When sensitivity and specificity are both near the ceiling
in a handful of small studies, the DOR blows up and its uncertainty blows up
faster, because you are dividing by numbers close to zero.

**An everyday version.** You want to know how much faster your new car is than
your old one. The old one takes a measured 60 seconds. The new one takes
somewhere between 1 and 10 seconds — you only timed it twice. The ratio is
"somewhere between 6 and 60 times faster." That is technically a measurement and
practically useless.

**Watch out for:** large ratio estimates — odds ratios, hazard ratios, likelihood
ratios, DORs — quoted without their intervals, or with intervals you did not
look at. Compute **upper ÷ lower**. Under about 3 is tight; over about 10 means
the study cannot distinguish a modest effect from an enormous one. And be
especially careful when the underlying rates are near 0% or 100%: that is where
ratios become unstable, and it is exactly where impressive-looking AI results
live.

## 2. Lesion level or patient level — which question did they answer?

This is the paper's best contribution and the third time in four days this list
has met the same idea wearing a different hat.

Two different questions:

- **Lesion level.** Here is a small cube of brain. Is there a microbleed in it?
  Pooled: sensitivity **0.96**, specificity **0.98**, AUC **0.99**.
- **Patient level.** Here is a whole brain scan. Does this person have
  microbleeds? Pooled: sensitivity **0.89**, specificity **0.86**, AUC **0.93**.

Translate the specificities into what a patient experiences. Out of 100 people
who do *not* have microbleeds:

> lesion level: **2** get a false alarm.
> patient level: **14** get a false alarm.

**Seven times as many.** And out of 100 who do have them, the model misses 4 at
the lesion level and **11** at the patient level.

Why the collapse? The authors' explanation is correct and worth absorbing. A
patient-level verdict requires combining "hundreds to thousands of image patches
across the entire brain." Each patch carries a small chance of a false alarm, and
you only need one to call the whole patient positive. Meanwhile the brain is
full of microbleed impostors — vascular calcification, physiological iron in the
basal ganglia, paramagnetic artefacts — which the authors note are "extremely
common in older adults," exactly the population being scanned. Add that one bad
slice from movement or a dental implant can swing the whole judgment.

**An everyday version.** A proofreader who spots 98% of typos and only rarely
flags a correct word looks superb — per word. Run them over a 500-page book and
the handful of false flags per page becomes hundreds of spurious corrections, and
the question "does this book contain any typos?" gets answered "yes" every time,
for every book.

**Watch out for:** the unit the accuracy is measured in. Per lesion, per image,
per slide, per patch, per eye, per slice — none of these is per patient, and per
patient is almost always the clinical question and almost always the lower
number. This list has now seen the same distinction as a *clustering* problem
(1,626 lesions from 158 patients, entry 38), a *sample-size* problem (two eyes
per patient, entry 39), and here as a *task difficulty* problem. Same root:
counting things is not counting people.

## 3. A thirty-second audit: is the confidence interval log-symmetric?

This is the most transferable trick in this summary, and it found a real error.

Ratio measures — odds ratios, risk ratios, hazard ratios, likelihood ratios,
DORs — are not symmetric on the ordinary number line. Doubling and halving are
equal and opposite changes, but 2 is one unit above 1 while 0.5 is only half a
unit below. So statisticians compute these intervals on the **logarithmic** scale
and convert back. The consequence you can check: **the point estimate should sit
at the geometric mean of the interval**, that is √(low × high) — not at the
ordinary midpoint.

Run it on all twelve ratio intervals in this paper:

> PLR patient 6.3, interval 3.5–11.6 → √(3.5 × 11.6) = **6.37** ✓
> PLR lesion 39.5, interval 16.8–92.7 → **39.46** ✓
> PLR reconstructed 41.2, interval 21.2–79.9 → **41.16** ✓
> DOR patient 50, interval 12–212 → **50.4** ✓
> DOR lesion 1061, interval 293–3848 → **1061.8** ✓
> DOR directly extracted 1738, interval 174–17,385 → **1739.3** ✓
> DOR reconstructed 736, interval 224–2418 → **736.0** ✓

Seven exact matches, and the four NLR intervals also match once you allow for
their being printed to only two decimal places. Eleven of twelve.

The twelfth:

> **PLR directly extracted: 40.2, interval 9.3–79.9 → √(9.3 × 79.9) = 27.3**

That is 47% away from the printed point estimate. It cannot be rounding. So solve
for the lower bound that *would* work: 40.2² ÷ 79.9 = **20.2**. And √(20.2 ×
79.9) = **40.2**, exactly. A **20.2** misprinted as **9.3** accounts for the
whole discrepancy — and note that the printed upper bound, 79.9, is identical to
the one in the row below it, which is further reason to think that line was
mis-transcribed.

**An everyday version.** Someone tells you the average of two numbers is 40, and
the two numbers are 9 and 80. You can check that in your head and know something
is wrong. This is the same check, with geometric rather than arithmetic
averaging because the quantity is a ratio.

**Watch out for:** do this on any ratio with an interval, in any paper. It takes
seconds, it requires only a square root, and it catches transcription errors,
unit mix-ups and intervals computed on the wrong scale. If the geometric mean is
badly off the point estimate, something in that line is wrong, and you should not
use the number until you know what.

## 4. Likelihood ratios are portable. Predictive values are not.

The paper translates its accuracy figures into something clinically meaningful
using a **Fagan nomogram**, and this is the right instinct — but the translation
depends entirely on one assumption the authors chose.

A **likelihood ratio** is a property of the test. The **positive likelihood
ratio** is how many times more likely a positive result is in someone with the
disease; the **negative** one, the same for a negative result. They travel
between settings unchanged. The patient-level values here are PLR **6.3** and NLR
**0.13**.

A **predictive value** is not a property of the test. It depends on how common
the disease is where you are working. You combine them with odds:

> pre-test odds × likelihood ratio = post-test odds

The paper assumes a **30%** pre-test probability. Working that through: odds =
0.30/0.70 = 0.4286; × 6.3 = 2.70; probability = 2.70/3.70 = **73%**. That
reproduces the reported positive predictive value exactly.

But the paper's own introduction says microbleed prevalence ranges from **5% to
35.7%**, and 30% is near the top. Recomputing across that range:

> at **5%** prevalence: positive predictive value **25%**, negative **99.3%**
> at 10%: **41%** / 98.6%
> at 15%: **53%** / 97.8%
> at 20%: **61%** / 96.9%
> at **30%**: **73%** / 94.7% ← the paper's assumption
> at 35.7%: 78% / 93.3%

So in a setting where 5% of scanned patients have microbleeds, a positive call
from the model is **wrong three times out of four** — while a negative call is
right more than 99 times out of 100.

That asymmetry is the real clinical message, and the paper does not draw it: at
the patient level, this is a **rule-out** tool. A negative result is genuinely
reassuring across the entire plausible prevalence range. A positive result is a
reason to look, not a finding.

**An everyday version.** A metal detector that beeps at 95% of real coins and
rarely at anything else is wonderful on a beach full of coins. On a beach with
one coin and a million bottle tops, almost every beep is a bottle top — the
detector did not get worse, the beach changed.

**Watch out for:** any PPV, NPV, or "the model was right X% of the time" without
the prevalence it assumes. Find the assumed prevalence, compare it to your
setting, and if they differ, recompute with the likelihood ratios — which is two
multiplications. And notice when a paper picks the most favourable prevalence in
its own cited range, as happened here.

## 5. What "included in the meta-analysis" can mean

A systematic review has two separate counts, and they are often very different:
how many studies were **included in the review**, and how many contributed data
to each **pooled estimate**.

This paper says both, several pages apart.

> "Ultimately, 42 studies were incorporated in the meta-analysis."
> "33 studies provided only limited outcome data and could not be directly
> included in the current meta-analysis."

42 − 33 = **9**. The pooled numbers rest on **14 contingency tables** from at
most those nine studies — which also means some studies were counted twice, once
at each level, so the two pools are not independent.

And then there is what those nine studies contain. The patient-level pool: **415
patients, 134 with microbleeds.** Every clinically relevant figure in the
abstract comes from that.

Why do studies get dropped at this stage? Usually because meta-analysis of
diagnostic accuracy needs the full 2×2 table — true positives, false positives,
true negatives, false negatives — and many papers report only an AUC, or only
sensitivity, or a bar chart. The authors here tried hard to rescue some by
**reconstructing** tables from reported sensitivity, specificity, accuracy and
case counts, and then — to their real credit — checked whether that
reconstruction mattered by pooling the extracted and reconstructed tables
separately. It did not change their conclusions.

**An everyday version.** "We surveyed 42 restaurants" and "9 of them told us
their prices" are both true. Only the second supports an average price.

**Watch out for:** in any meta-analysis, find the number attached to each pooled
estimate, not the number in the title or the flow diagram. It is usually in the
forest plot as a count of rows, or in a sentence like "k = 5." Then ask how many
*patients* those studies contain. A review of 42 studies whose headline rests on
415 people is a different object from what the phrase "42 studies" suggests — and
that is true however carefully the review was otherwise conducted.

# Jargon Translator

- **Cerebral microbleed (CMB)** — a tiny deposit of old blood breakdown product in
  the brain, visible as a small dark dot on certain MRI sequences.
- **Hemosiderin** — the iron-containing residue left by old bleeding; what makes
  microbleeds visible.
- **Susceptibility-weighted imaging (SWI) / T2*-weighted imaging / gradient echo
  (GRE)** — MRI sequences sensitive to iron and blood products. SWI detects more
  microbleeds but takes longer to acquire.
- **Quantitative susceptibility mapping (QSM)** — a newer MRI technique that
  measures magnetic susceptibility numerically; better at telling microbleeds from
  calcium, but technically demanding.
- **Field strength (1.5T, 3.0T, 7.0T)** — magnet power. Higher detects more
  microbleeds; 7T is rare outside research.
- **Cerebral amyloid angiopathy** — amyloid protein in brain blood vessels; its
  microbleeds sit in the outer brain (lobar), unlike hypertensive ones which sit
  deep.
- **Boston criteria v2.0** — the current diagnostic rules for cerebral amyloid
  angiopathy, which use MRI findings including where the bleeds are.
- **Systematic review** — a structured search of all published evidence on a
  question, with prespecified rules for what to include.
- **Meta-analysis** — statistically combining results across studies into a pooled
  estimate.
- **PROSPERO** — the international register for systematic review protocols.
  Registering before you start prevents quiet changes later.
- **PRISMA** — the reporting checklist for systematic reviews.
- **QUADAS-2** — the standard risk-of-bias tool for diagnostic accuracy studies,
  covering patient selection, index test, reference standard, and flow and timing.
- **QUADAS-AI** — an AI-specific extension covering data leakage, external
  validation and cross-device generalisability. Not yet available when this review
  began.
- **2×2 / four-fold contingency table** — the four counts a diagnostic test
  produces. Required raw material for this kind of meta-analysis.
- **Reference standard** — the thing treated as truth, here expert reading of the
  MRI.
- **Case-control design** — cases and controls selected separately rather than
  consecutively from a real population. Tends to inflate apparent accuracy.
- **Sensitivity** — of those who have it, the share detected.
- **Specificity** — of those who don't, the share correctly cleared.
- **Positive / negative likelihood ratio (PLR / NLR)** — how much a positive or
  negative result shifts the odds of disease. Properties of the test; portable
  between settings.
- **Diagnostic odds ratio (DOR)** — PLR ÷ NLR. One number for overall
  discrimination; unstable when accuracy is near-perfect.
- **Positive / negative predictive value (PPV / NPV)** — of those who tested
  positive or negative, the share who truly do or don't have it. Depend on
  prevalence; not portable.
- **Fagan nomogram** — a chart for converting a pre-test probability plus a
  likelihood ratio into a post-test probability.
- **Pre-test / prior probability** — how likely the disease is before testing;
  usually the prevalence in your setting.
- **Summary ROC (SROC) curve** — the meta-analytic version of an ROC curve,
  drawn across studies.
- **Bivariate mixed-effects model** — the standard way to pool sensitivity and
  specificity together, respecting that they trade off against each other.
- **Threshold effect** — when studies used different cut-offs, so their
  sensitivity and specificity move together across studies.
- **Deeks' funnel plot** — a publication-bias test designed for diagnostic
  accuracy reviews. Low power below about ten studies.
- **Publication bias** — the tendency for flattering results to get published more
  readily.
- **I² / tau²** — measures of how much studies disagree beyond chance. Not
  reported in this paper.
- **Prediction interval** — the range in which a *new* study's result would be
  expected to fall. More informative than a confidence interval when heterogeneity
  is high.
- **Kappa (κ)** — agreement between raters, corrected for chance. 0.891 here, for
  study screening.
- **External validation** — testing on data from a different source than the
  training data. The large majority of these 42 studies had none.
- **Data leakage** — information from the test set reaching the model during
  training.
- **Dice coefficient** — a measure of how well a predicted region overlaps a true
  region, used for image segmentation. The authors wanted it and found it
  unreported.

# What You Can (and Can't) Say

**You can say:** a prospectively registered systematic review found that deep
learning models detect cerebral microbleeds on MRI with pooled sensitivity 0.96
and specificity 0.98 when the task is classifying an individual image patch, and
with pooled sensitivity 0.89 and specificity 0.86 when the task is deciding
whether a whole patient has microbleeds.

**You can say** that the gap between those two is the review's most useful
finding, that the patient-level task is the clinically relevant one, and that
false alarms are about seven times more common there (14 per 100 unaffected
people, versus 2).

**You can say** the authors explicitly conclude that these models cannot be used
as an independent diagnostic basis and that their output must be confirmed by
imaging experts.

**You cannot say** this review represents 42 studies' worth of evidence. Thirty-
three of the 42 could not supply extractable data; the pooled numbers come from
14 contingency tables, and the patient-level figures from **5 tables covering
415 patients**.

**You cannot treat** the patient-level sensitivity of 0.89 as precise. Its
confidence interval runs from **0.76 to 0.96** — consistent with missing one case
in four, and with missing one in twenty-five.

**You cannot use** the diagnostic odds ratio of 1,738. Its interval spans 174 to
17,385, a hundredfold range from five tables.

**You cannot rely on** the directly extracted positive likelihood ratio interval
as printed. The arithmetic shows the lower bound of 9.3 is inconsistent with the
point estimate of 40.2; it is almost certainly 20.2.

**You cannot conclude** there is no publication bias or no important
heterogeneity. The publication-bias tests were run on 4 to 9 studies, where they
have little power, and **no heterogeneity statistic is reported at all** despite
the authors acknowledging considerable heterogeneity in words.

**You cannot assume** a positive result means much in a low-prevalence setting.
At the 5% prevalence that the paper's own introduction gives as the bottom of the
range, the patient-level positive predictive value falls from 73% to **25%**.

**You cannot generalise** to routine practice. All 42 studies were case-control,
which the authors rate as high risk of bias for patient selection; most had no
external validation; only 13 of 42 clearly blinded the reference standard, with
24 not saying; and no prospective study exists.

**You cannot tell** from this review how much performance drops outside the
development centre. The authors report that external-validation sensitivity was
lower but state they could not perform the subgroup analysis, and give no
numbers.

# Bottom Line for Your Life

If you or a relative has had a brain MRI that mentions **microbleeds**, here is
what this paper is and isn't about.

It is not about whether you should worry. Microbleeds are common with age — the
reported prevalence runs from about 5% to 36% depending on who is scanned and
how carefully you look — and finding a few is often an incidental observation
rather than a diagnosis.

What they mean depends heavily on **where they are**, and that is worth knowing
because this review highlights it. Microbleeds deep in the brain tend to go with
long-standing high blood pressure. Microbleeds in the outer layers tend to go
with cerebral amyloid angiopathy, and the current diagnostic criteria for that
condition depend on the pattern and count. So "how many, and where?" is a
reasonable and specific question to ask, and it is more informative than "are
there any?"

The reason it can matter practically: the number and location of microbleeds
feed into decisions about **blood thinners** — balancing stroke prevention
against bleeding risk. If you are on anticoagulation and a scan reports
microbleeds, that is a conversation to have rather than a reason to stop
anything on your own.

On the AI: the useful conclusion from this review is the one its own authors
reach. These tools look genuinely good at flagging candidate spots for a
radiologist to check, and distinctly less good at deciding whether a whole
person has microbleeds — because a brain is full of things that look like
microbleeds and are not: calcium, normal iron deposits, scanner artefacts. The
authors say the output "still needs to be combined with clinical information and
ultimately confirmed by imaging experts." That is the right expectation to carry
into a clinic where a report says "AI-assisted."

And the asymmetry worth remembering, which falls out of the numbers rather than
the text: at the patient level a **negative** result from one of these models is
genuinely reassuring across every plausible prevalence — above 99% reliable at
the low end. A **positive** result is a prompt to look more carefully, not a
conclusion. If a scan is flagged, the question is "has a radiologist confirmed
it?", and the answer is often that the flag was one of the impostors.

**This is education about how to read a study, not medical advice. Decisions about
imaging findings and blood thinners belong with you and your doctors.**

---

*Decoded 2026-10-08. Source: PubMed and PubMed Central, accessed 2026-10-08.
Full text read from PMC13639419, which became available overnight after sixteen
days of daily checks. Figures 1-5, all fourteen supplementary figures and the
search strategy table did not render, so the forest plots, SROC curves, QUADAS-2
figures, Deeks' funnel plots and Fagan nomograms were not seen; only the numeric
values quoted for them in the body text. Table 1 rendered in full. Derived
figures - the 9-of-42 poolable count and the 78.6% that contributed nothing; the
14-tables-from-9-studies dependency; the log-symmetry audit of all twelve ratio
intervals and the identification of 20.2 as the probable true lower bound of the
directly extracted PLR; the DOR interval widths of 17.7, 13.1, 99.9 and 10.8
fold; the DOR = PLR/NLR reconciliations; the sevenfold false-alarm ratio between
levels; the recomputation of positive and negative predictive values across the
paper's own 5%-35.7% prevalence range, which reproduces its 73% and 95% at a 30%
prior; the blinding proportions; and the screening-funnel reconciliation - were
computed from the paper's own reported numbers and are labelled as derived
wherever they appear. Funding and competing interests were not stated in the text
retrieved.*

**Verified source links**
- DOI: https://doi.org/10.2196/95041
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42767630/
- Full text used: https://pmc.ncbi.nlm.nih.gov/articles/PMC13639419/
- Protocol registration: PROSPERO CRD42024628447
