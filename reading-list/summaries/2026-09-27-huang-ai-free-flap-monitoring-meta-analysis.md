# The Average Says 83%. The Next Hospital Could Get 21%.

**Paper:** Diagnostic Accuracy of AI in Prediction and Assessment of Compromised
Free Flaps: Systematic Review and Meta-Analysis
**Authors:** Huang KC, Wang MJ, Chu YY, Huang RW, Lu YJ, Lin CH, Hsu CC,
Chen SH, Lin YT, Lee CH
**Venue / Year:** Journal of Medical Internet Research, 2026;28:e91174
**DOI:** https://doi.org/10.2196/91174
**PubMed:** https://pubmed.ncbi.nlm.nih.gov/42771768/
**Full text used:** https://pmc.ncbi.nlm.nih.gov/articles/PMC13596764/
**Basis of this analysis:** FULL TEXT (PubMed Central open-access copy,
retrieved 2026-09-27). Figures 1–19 and the four supplementary appendices were
not retrievable; nothing here depends on a figure value. All numbers come from
the article body or Tables 1–3.
**Date decoded:** 2026-09-27
**Evidence grade:** 4/5

---

# The Gist

When a surgeon rebuilds a breast, a jaw, or a leg, they often move a piece of
living tissue — a "free flap" — from somewhere else on the body and reconnect
its blood vessels under a microscope. If those vessels clog or kink in the days
afterward, the tissue starts to die. Catch it within hours and you can usually
save it. Miss it and the whole operation is lost.

Right now catching it means a nurse or surgeon looking at the flap every hour
and deciding whether the colour looks wrong. That is subjective, exhausting, and
impossible to do consistently at 3am. So researchers have been building AI to
do it — some by photographing the flap and analysing its colour, others by
feeding in a patient's clinical details to predict who is at risk before
anything goes wrong.

This team gathered every such study they could find — 17 of them — and pooled
the results. Their headline: overall sensitivity 83% and specificity 87%, and
for the photograph-based systems, a summary AUC of 0.98, which is near-perfect.

But this paper does something most meta-analyses skip, and it is the reason this
is the most instructive paper in weeks. Alongside each average, the authors
report a **prediction interval** — the range where the *next* study's result is
likely to land. And those intervals are enormous. Sensitivity averages 83% but
the prediction interval runs from **21% to 99%**. Specificity averages 87% with
a prediction interval from **3% to 100%**. The pooled diagnostic odds ratio is
36 with a prediction interval from **0.09 to 14,886** — and a value below 1
would mean the AI is worse than useless.

So the honest summary is: on average these systems look good, and we have
essentially no idea what one would do in your hospital. The authors say almost
exactly this in their discussion. Their abstract, and everyone who cites them,
will say the first half.

# Study Snapshot

- **Study type:** Systematic review and meta-analysis of **diagnostic test
  accuracy** — the top of the evidence ladder in principle, but only ever as
  good as the studies fed into it. This one is built on mostly small,
  retrospective, single-hospital studies.
- **Registration:** Prospectively registered with PROSPERO
  (CRD420251175572) — registered *before* the work was done, which is the
  standard and is often skipped.
- **Reporting standards followed:** PRISMA-DTA (the diagnostic-accuracy
  extension), PRISMA 2020, PRISMA-S (for the search), and TITAN (AI
  transparency). Four checklists is unusually thorough.
- **Search:** PubMed, Embase, Cochrane, Web of Science, and Scopus, from
  inception to 21 June 2026, **no language restriction**, plus forward and
  backward citation chasing.
- **Selection:** 2098 records found; 792 duplicates removed; 1306 titles and
  abstracts screened; 129 full texts assessed; **18 studies included**, of which
  **17** had enough data to pool.
- **What the included studies were:** 15 retrospective, only **2 prospective**.
  External validation in only **5 of 17**. Eight used photographs of the flap;
  nine used clinical variables such as age, BMI, smoking, operative time.
- **Where from:** China, Taiwan, South Korea, United States, Canada, United
  Kingdom, Italy, Germany, Indonesia. Sample sizes ran from **7 patients** to
  4000.
- **What counted as truth:** In nearly every study, "clinical evaluation" — a
  clinician's judgement. Only two studies used surgical confirmation.
- **Main outcomes pooled:** Sensitivity, specificity, positive and negative
  likelihood ratios, diagnostic odds ratio, and summary AUC.
- **Statistical machinery:** A bivariate random-effects model (the correct
  approach — it pools sensitivity and specificity jointly rather than
  separately), with Sidik-Jonkman between-study variance and Hartung-Knapp
  adjusted intervals, plus prediction intervals, a Fagan nomogram, Deeks funnel
  plot test, Q-Q plots, Mahalanobis distances, and Cook's distance for
  influence.
- **Quality appraisal:** QUADAS-2 for risk of bias, GRADE for certainty.
- **Certainty verdict:** **LOW** for both pooled sensitivity and pooled
  specificity, downgraded for serious risk of bias and serious inconsistency.
- **Ethics:** Not required — published data only.
- **Funding:** **Not reported** in the text retrieved.
- **Conflicts of interest:** **No statement appears** in the text retrieved.

# How Strong Is This Evidence? — Grade 4/5

There are two separate questions here, and keeping them apart is the whole
skill: *how good is this review?* and *how good is the evidence it reviews?*

**The review is genuinely well built.** It was registered in advance. It
followed four reporting standards. It searched five databases in any language.
It used the statistically correct bivariate model rather than pooling
sensitivity and specificity as if they were independent. It appraised every
study with QUADAS-2 and graded the whole body with GRADE. It ran a battery of
influence diagnostics to check whether any one study was driving the answer. It
tested for publication bias. **And it reported prediction intervals**, which the
large majority of meta-analyses simply omit — the single most important number
for a reader and the one that undercuts its own headline. Its discussion states
plainly that "the pooled estimates should not be interpreted as performance that
can be uniformly expected in all practice environments," and it names the
circular reference-standard problem in its own words: the AI is being graded
against a "silver standard" of subjective clinical intuition, so measured
performance "may represent a theoretical ceiling imposed by the noise within
training labels." That is a level of self-awareness worth real credit.

**The evidence it reviews is weak, and the review says so.** Fifteen of 17
studies retrospective. Only 5 externally validated. One study had 7 patients.
Heterogeneity was 98%. GRADE: low certainty.

**Why 4 and not 5.** Two extractable decisions inflate the headline numbers in
ways a reader cannot see from the abstract — the best-model selection and the
mixed unit of analysis, both detailed below. A third, including a study whose
specificity was literally zero, is disclosed in a range ("0.00 to 1.00") without
the reader being told what that zero means. And the GRADE table rates
imprecision as "not serious" next to a diagnostic odds ratio whose prediction
interval spans five orders of magnitude.

# The Editor's Concerns

**The best model from each study was cherry-picked — by design, and disclosed.**
Where a study tested several algorithms, the reviewers took "the best-performing
model identified by the original authors," or where none was named, the one with
the highest AUC. Look at what that means in practice: one included study tested
eight algorithms, another nine, another five. Taking the winner from each and
then averaging the winners does not estimate how well AI performs — it estimates
how well the luckiest algorithm performs on the dataset it was tuned on. The
authors acknowledge this "may slightly overestimate diagnostic performance" and
give a fair reason for the choice (including several models from one cohort
would double-count that cohort). The reason is sound; "slightly" is doing a lot
of work.

**Image studies counted images; clinical studies counted patients. These were
pooled together.** The Methods state that "analyses were conducted at the
patient level with image- or pixel-level data aggregated accordingly to avoid
distortion of diagnostic estimates." But the footnote to Table 2 says the
opposite: "'n' represents the unit of analysis reported in each study (images
for image-based models and patients for clinical variable–based models)." The
extracted counts settle it. *Deriving* from the paper's own table: one
image-based study contributes 5506 test observations from only **305 patients**
— about 18 observations per person. Another contributes 921 from 642 patients,
another 845 from 615. Photographs of the same flap are not independent
observations; they are the same flap, repeatedly. Counting them as independent
makes a study look far more precise than it is, and the image-based subgroup —
the source of the spectacular AUC 0.98 — is exactly where this concentrates.
This is the clustering problem from the 09-25 decode, appearing inside a
meta-analysis.

**One included study had zero true negatives.** *Deriving* from Table 2: Asaad
et al 2023 reports 14 true positives, 785 false positives, 0 false negatives,
and **0 true negatives** — 799 cases, which is exactly its test-set size. In
other words the model labelled **every single case positive**. That is not a
diagnostic test; it is a constant. Its sensitivity is trivially 100% and its
specificity is exactly 0%. The review reports that "specificity estimates ranged
from 0.00 to 1.00" and elsewhere notes Asaad "demonstrated an extreme
specificity of 0.00," but never says what a specificity of zero implies about
whether that study should have been pooled at all. It needed a continuity
correction of 0.5 added to all four cells just to make its odds ratio
computable.

**Several studies rest on a handful of events.** One had 7 patients and 5
compromised flaps. Another had 5 positive cases in its test set; another 4.
These are the studies generating the paper's own observation that study-level
diagnostic odds ratios "varied widely, ranging from 0.02 to 5390.00." A ratio of
5390 does not mean a brilliant model; it means almost nothing was misclassified
because there was almost nothing to classify.

**The truth standard is the thing the AI is meant to replace.** In nearly every
included study, the reference standard was "clinical evaluation" — a clinician
looking at the flap and deciding. Only two used surgical confirmation. So the AI
is being scored against the subjective human judgement whose subjectivity is the
stated reason for building the AI. If the humans are wrong 10% of the time, an AI
that agrees with them 90% of the time might be perfect or might be useless, and
this design cannot tell you which. To their credit the authors name this
directly.

**Seventy percent of studies were high or unclear risk on the domain that
matters most.** QUADAS-2 rated the index test domain — how the AI was applied
and interpreted — as unclear in 8 of 17 studies (47.1%) and high risk in 4
(23.5%). For a review about diagnostic accuracy, that is the central domain, and
12 of 17 studies fail to clear it.

**GRADE downgraded for inconsistency but not imprecision, which is hard to
defend.** The certainty table records imprecision as "not serious" for both
pooled sensitivity and specificity. Yet pooled specificity has a confidence
interval of 0.65 to 0.96 — the difference between a test that raises 35% false
alarms and one that raises 4% — and the diagnostic odds ratio's prediction
interval runs from 0.09 to 14,886. Both were rightly downgraded for
inconsistency. Calling that precise as well is generous.

**The GRADE participant count does not reconcile with the extracted data.** The
certainty table reports 11,542 participants across 17 studies. *Deriving* from
Table 2, the 2×2 tables sum to about **17,196** observations. The paper
footnotes that one study did not report participant numbers and — remarkably —
that in Table 2 "the cumulative total may contain an error." Candid, but a
reader cannot reconstruct the denominator.

**The sensitivity analysis is read more favourably than it supports.** Excluding
the two most influential studies "did not materially change the summary
estimates," which the authors call confirmation the results are "robust and not
unduly influenced by any single study." There is another reading: when
between-study variance is 98%, the pooled estimate is dominated by scatter rather
than by any individual study, so removing one changes little. Stability under
deletion is not the same as reliability.

**The Fagan nomogram is presented as good news and is more ambiguous than
that.** Starting from a 19% pretest probability, a positive AI result raises the
chance of flap compromise to about 62% and a negative result lowers it to about
4%. The paper calls this "strong rule-in and rule-out." Turn it around: roughly
**4 in 10 flagged flaps are false alarms**, each potentially triggering an
urgent theatre call; and about **1 in 25 reassured flaps is compromised
anyway**. In a setting where the whole point is not missing a dying flap, whether
that is good enough is a clinical judgement, not a statistical one. And the 19%
prevalence comes from the included studies' case mix, not from a real ward.

**Publication bias "undetected" means the test could not detect it.** Deeks'
test returned p = .15 against a threshold of .10. Funnel-plot methods are
notoriously underpowered with fewer than about 20 studies; with 17 heterogeneous
ones, a null result is close to uninformative. "Undetected" is not "absent," and
the GRADE table's "undetected" should be read that way.

**Nearly half the studies did not report the numbers needed.** The authors had to
reconstruct the 2×2 contingency table for 44% (8 of 18) of studies from other
reported statistics, and call this "a pervasive reporting gap in the
microsurgical literature." They are right, and it adds uncertainty that no
confidence interval in this paper captures.

# Statistics Spotlight

## Concept 1 — Confidence interval versus prediction interval

If you take one idea from this reading list, consider taking this one. It is the
difference between "what is the average?" and "what will happen to me?" — and
almost nobody reports both.

**What a confidence interval tells you.** A 95% confidence interval describes
uncertainty about the **average**. Here, pooled sensitivity was 0.83 with a
confidence interval of 0.70 to 0.91. Read that as: *the true average sensitivity
across this kind of study is probably somewhere between 70% and 91%.* Add more
studies and this interval narrows, because you are pinning down an average more
precisely.

**What a prediction interval tells you.** A 95% prediction interval describes
where a **single new study** would land. For the same pooled sensitivity of
0.83, the prediction interval was **0.21 to 0.99**. Read that as: *if a
hospital installs one of these systems tomorrow, its sensitivity could plausibly
be anywhere from 21% to 99%.* Adding more studies does **not** necessarily narrow
this, because it is dominated by real differences between settings, not by
sampling noise.

Look at the full set from this paper:

- Sensitivity 0.83, confidence interval 0.70–0.91, **prediction interval
  0.21–0.99**
- Specificity 0.87, confidence interval 0.65–0.96, **prediction interval
  0.03–1.00**
- Negative likelihood ratio 0.22, confidence interval 0.10–0.47, **prediction
  interval 0.01–5.11**
- Diagnostic odds ratio 36.17, confidence interval 8.27–158.26, **prediction
  interval 0.09–14,886.43**

Two of these deserve a second look. A specificity prediction interval reaching
down to **0.03** means the next study could find the system flags 97% of healthy
flaps as compromised. A negative likelihood ratio above 1 means a *negative*
result makes disease **more** likely — and that prediction interval goes up to
**5.11**. And a diagnostic odds ratio below 1 means the test is actively
misleading; that prediction interval starts at **0.09**. The evidence is
compatible with the next AI system being worse than no AI at all.

**The intuition.** Suppose you measure the height of adult men in ten countries
and average it. Your confidence interval tells you how well you have estimated
the *worldwide average* — and with enough countries it gets very tight, maybe
175 to 176 cm. Your prediction interval tells you how tall the *next man you
meet* might be — and no amount of extra data shrinks that below roughly 160 to
190 cm, because men genuinely differ. Averaging harder does not make people more
uniform.

Or closer to home: a restaurant chain averages 4.2 stars. That average is
precisely estimated from 40,000 reviews. It tells you almost nothing about the
branch near you, which might be a 2 or a 5. The confidence interval is about the
chain; the prediction interval is about your dinner.

**Watch out for:** any meta-analysis that reports only confidence intervals.
Because pooling many studies mechanically shrinks the confidence interval, a
meta-analysis of wildly inconsistent studies can produce a **tight** interval
around a **meaningless** average — and that tight interval reads as authority.
When you see a pooled estimate with a narrow confidence interval and a high I²
(next section), the prediction interval is the number being hidden, and it is the
one that answers your actual question. If a paper does not report it, you cannot
assume the pooled figure applies to your setting. This paper does report them,
which is exactly why it grades a 4.

## Concept 2 — Sensitivity, specificity, likelihood ratios, and what a result actually changes

These four terms get used interchangeably in conversation and mean quite
different things. Here is the chain, built on this paper's numbers.

**Sensitivity** — of the flaps that really were compromised, what share did the
AI catch? Pooled: **0.83**. So it misses about 17 in every 100 dying flaps.

**Specificity** — of the flaps that were fine, what share did the AI correctly
leave alone? Pooled: **0.87**. So it raises a false alarm on about 13 in every
100 healthy flaps.

Both are properties of the test. Neither answers the question you actually have
at the bedside, which is: *the alarm just went off — what are the odds this flap
is really in trouble?* For that you need two more things.

**Likelihood ratios** convert a test result into a change in the odds.

> Positive likelihood ratio = sensitivity ÷ (1 − specificity)
> = 0.83 ÷ 0.13 ≈ **6.4** (the paper's model-based figure is 7.63)

A positive likelihood ratio of about 7.6 means a positive result is 7.6 times
more likely to come from a compromised flap than a healthy one. Rough guide: 10
or more is a strong rule-in, around 5 is moderate, under 2 is nearly useless.

> Negative likelihood ratio = (1 − sensitivity) ÷ specificity
> = 0.17 ÷ 0.87 ≈ **0.20** (paper: 0.22)

A negative likelihood ratio of 0.22 means a negative result is about a fifth as
likely to come from a compromised flap. Under 0.1 is a strong rule-out.

**The diagnostic odds ratio** squashes both into one number — positive likelihood
ratio ÷ negative likelihood ratio, here 7.63 ÷ 0.22 ≈ **36**. It is compact and
it is fragile: because it divides by very small counts, a study with almost no
mistakes produces an astronomical value. That is precisely why this paper's
study-level odds ratios span **0.02 to 5390**, a fact the authors flag
themselves. A high diagnostic odds ratio can mean an excellent test or a tiny
sample.

**Now the part that matters: the starting point decides everything.** A
likelihood ratio does not give you a probability. It *multiplies* the odds you
started with. This paper works it through with a **Fagan nomogram**:

- Start at the observed prevalence: **19%** of flaps compromised. As odds:
  0.19 ÷ 0.81 = 0.23.
- AI says compromised: 0.23 × 7.63 = 1.79 → back to probability, **about 62%**.
- AI says fine: 0.23 × 0.22 = 0.052 → **about 4%**.

So the alarm takes you from 19% to 62%, and silence takes you from 19% to 4%.
That is genuinely useful movement. It is also not a diagnosis: at 62%, nearly
four in ten alarms are false.

**And watch what happens if the starting point changes.** Suppose your unit's
flap-compromise rate is 3% rather than 19% — plausible, since these studies
deliberately enriched for difficult cases. Odds 0.031 × 7.63 = 0.236 →
probability **19%**. The identical test, with the identical likelihood ratio, now
means a positive alarm is wrong four times out of five. Nothing about the AI
changed. Only the population did.

**Watch out for:** sensitivity and specificity quoted as if they told you what a
result means. They never do on their own. Whenever someone tells you a test is
"90% accurate," the question is *what was the prevalence?* This is the single
most common misreading of screening tests, and it is why a highly specific test
for a rare disease still produces mostly false positives.

## Concept 3 — I² of 98%, and when you should refuse to pool

I² answers: what share of the variation between study results reflects real
differences between the studies, rather than ordinary sampling noise?

Conventional reading: 25% is low, 50% is moderate, 75% is high.

**This paper reports I² of 98.1% for sensitivity and 98.6% for specificity.**

That is about as high as the statistic goes. It says: essentially none of the
spread across these 17 studies is chance. The studies genuinely disagree, because
they are not measuring the same thing. And when you read the details, of course
they aren't: one defined the target as "venous congestion," another as "flap
takeback," another as "complete flap failure." Some photographed flaps, others
fed in BMI and smoking status. Populations ran from 7 patients to 4000, event
rates from under 1% to 30%. Different tests, different diseases, different
patients, one average.

**The intuition.** Imagine averaging the top speed of ten vehicles and reporting
"the average vehicle travels 68 km/h." If the ten were all mid-size sedans,
that average is informative and the spread is just measurement noise — low I².
If the ten were a bicycle, a tractor, three sedans, a motorbike and a Formula 1
car, the average is arithmetically correct and tells you nothing about any
vehicle, and the spread is real — I² near 100%. The number does not warn you.
I² does.

**The trap this sets.** Pooling more studies always narrows the confidence
interval, because that interval is about the precision of an average. So a
meta-analysis of hopelessly mixed studies can report a **tight** interval around
an average of things that should never have been averaged — and the tightness
reads as certainty. Pooled specificity here has a confidence interval of 0.65 to
0.96, which looks like an answer; the prediction interval of 0.03 to 1.00, driven
by that 98.6%, is the honest version.

**What good practice looks like, and what this paper did.** When I² is very high
you have three options: don't pool at all and describe the studies narratively;
pool but explain the heterogeneity through subgroups; or pool and report
prediction intervals so readers see the real spread. This review took the second
and third. Its subgrouping is genuinely illuminating: splitting by input type
showed image-based models at sensitivity 0.92 and specificity 0.95 (AUC 0.98)
against clinical-variable models at 0.69 and 0.72 (AUC 0.79). That is a large,
plausible difference and it explains part of the scatter — photographs see a
flap changing colour; a patient's BMI cannot.

But notice: even inside the image-based subgroup, the prediction intervals stay
wide (sensitivity 0.43–0.99, specificity 0.43–1.00), and the clinical-variable
subgroup's specificity prediction interval runs from **0.00** to 1.00. Splitting
into more homogeneous buckets helped and did not solve it. Which is the honest
conclusion: the field has not yet produced consistent enough evidence for a
single number to mean anything.

**Watch out for:** a pooled estimate presented without any heterogeneity
statistic — and, more subtly, a high I² acknowledged in the methods and then
ignored in the abstract. Ask: *were these studies similar enough that an average
of them is a thing?* If the answer is no, the confidence interval is a precise
measurement of a quantity that does not exist.

# Jargon Translator

- **Free flap:** Living tissue moved from one part of the body to another, with
  its blood vessels reconnected under a microscope.
- **Vascular compromise:** The reconnected vessels stop working — blocked artery,
  congested vein — and the tissue begins to die. The thing all these AI systems
  are trying to catch.
- **Flap takeback / reexploration:** Returning the patient to theatre to try to
  rescue a failing flap. Speed determines success.
- **Diagnostic test accuracy (DTA) review:** A meta-analysis about how well a
  test detects a condition, rather than whether a treatment works. Has its own
  statistics and its own reporting standard, PRISMA-DTA.
- **PROSPERO:** The public register where reviewers record their plan before
  starting, so they cannot quietly change the question after seeing results.
- **QUADAS-2:** The standard tool for rating bias in diagnostic accuracy studies,
  across patient selection, index test, reference standard, and flow and timing.
- **GRADE:** A framework for rating how much confidence to place in a body of
  evidence overall. Here: low.
- **Reference standard:** What the test is graded against — the assumed truth.
  Here, usually a clinician's opinion, which is the weak link.
- **Index test:** The test being evaluated. Here, the AI.
- **Bivariate random-effects model:** Pools sensitivity and specificity
  *together*, respecting the fact that they trade off against each other. The
  right method; pooling them separately overstates precision.
- **Summary ROC curve and AUC:** A curve through the studies' accuracy points;
  the area under it summarises discrimination. 1.0 is perfect, 0.5 is a coin
  flip.
- **Hartung-Knapp adjustment and Sidik-Jonkman estimator:** Technical corrections
  that widen intervals appropriately when there are few studies and high
  heterogeneity. Using them is a mark of care.
- **Continuity correction:** Adding 0.5 to every cell when a study has a zero,
  so ratios can be calculated at all. Necessary, and a sign the underlying data
  are thin.
- **Fagan nomogram:** A chart that turns a test result plus a starting prevalence
  into a post-test probability.
- **Deeks funnel plot test:** A check for publication bias adapted to diagnostic
  accuracy studies. Weak when there are few studies.
- **Cook's distance / Mahalanobis distance / Q-Q plot:** Diagnostics for spotting
  studies that distort the pooled estimate or break the model's assumptions.
- **SMOTE / ROSE / oversampling:** Techniques for training models when one
  outcome is rare — they manufacture or reweight examples of the rare class, and
  can inflate apparent performance if evaluated carelessly.
- **Class imbalance:** When the thing you want to detect is rare. Makes plain
  accuracy meaningless and sensitivity hard to achieve.

# What You Can (and Can't) Say

**Fair to say:**

- A prospectively registered meta-analysis of 17 studies found that AI systems
  for detecting free flap compromise had a pooled sensitivity of 83% (95% CI
  70–91%) and specificity of 87% (95% CI 65–96%), with a summary AUC of 0.92.
- Photograph-based systems substantially outperformed systems using clinical
  variables: sensitivity 92% versus 69%, specificity 95% versus 72%, AUC 0.98
  versus 0.79.
- The prediction intervals were very wide — sensitivity 21% to 99%, specificity
  3% to 100% — meaning performance in any single new setting is close to
  unpredictable.
- Heterogeneity was 98%, and GRADE rated the certainty of this evidence as
  **low**.
- Only 2 of 17 studies were prospective and only 5 reported external validation;
  most were single-centre and retrospective.
- Starting from a 19% pretest probability, a positive AI result moved that to
  about 62% and a negative result to about 4%.
- The authors' own conclusion is that this evidence is "insufficient to justify
  widespread clinical implementation without prospective multicenter validation
  and rigorous external evaluation," and that these tools should be adjuncts to,
  not replacements for, surgical judgement.

**Not fair to say:**

- ~~"AI detects failing flaps with 98% accuracy."~~ AUC 0.98 is the summary of a
  subgroup with 98% heterogeneity, built partly from repeated photographs of the
  same flaps counted as independent cases, using each study's best-performing
  model.
- ~~"AI is 83% sensitive for flap compromise."~~ That is an average whose
  prediction interval runs from 21% to 99%. It is not what your hospital would
  get.
- ~~"This proves AI should be used for flap monitoring."~~ GRADE says low
  certainty and the authors say not yet.
- ~~"The AI beats clinical examination."~~ It was scored *against* clinical
  examination. No study here compared AI with clinicians on an independent truth
  standard.
- ~~"A diagnostic odds ratio of 36 shows strong performance."~~ Its prediction
  interval starts at 0.09, below 1, which would mean actively misleading.
- ~~"No publication bias was found."~~ A test with 17 heterogeneous studies
  returning p = .15 has not found much of anything.
- ~~"Image-based AI is ready and clinical-variable models are not."~~ The
  comparison was not a head-to-head test; it is a subgroup contrast across
  different studies, different patients, and different definitions of the target
  condition.

# Bottom Line for Your Life

**The habit to build from this paper is asking for the prediction interval.**
Confidence intervals answer a question you probably don't have — how precisely do
we know the average? — and they get narrower simply by adding studies, which
makes inconsistent evidence look authoritative. The prediction interval answers
the question you do have: what might happen here? This paper's headline
sensitivity of 83% has a confidence interval of 70–91% and a prediction interval
of 21–99%. Both are correct. Only one of them tells you whether to buy the
system. When a meta-analysis reports only the first, the second is the number
that went missing.

**The second habit: ask what the AI was graded against.** Here the answer is
"a clinician looking at the flap." That makes the ceiling on measured performance
equal to the reliability of the thing being replaced — a point these authors make
themselves, calling it a "silver standard." Any time you read that an AI matched
or beat human performance, find out who decided what the right answer was. If
the answer is "humans," you have learned about agreement, not about accuracy.

**And the practical takeaway if this ever touches you or someone you know:**
these systems are not a substitute for someone checking the flap. On these
numbers, a reassuring AI reading still leaves roughly a 1-in-25 chance the flap
is in trouble, and the evidence base cannot promise that figure travels to any
particular hospital. The surgeons who wrote this review reached the same
conclusion — adjunct, not replacement — and they had every professional incentive
to conclude otherwise.

---

*Education, not medical advice. Decoded 2026-09-27 from the PubMed Central
open-access full text. Derived calculations — the observations-per-patient ratios,
the zero-true-negative study, the sum of the extracted 2×2 tables, and the
worked post-test probabilities — are labelled as derived and were computed from
the paper's own reported values.*
