# A Triage Tool That Misses One Polyp in Three — and the 11,278 Cases That Went Missing

**Paper:** Development of an Interpretable Triage Tool for Colorectal Polyp Risk
Stratification Within a Population-Based Screening Program: Machine Learning
Approach
**Authors:** Ye Z, Li J, Xie Y, Li Q, Huang Y, Zhang G, Yang X
**Venue / Year:** JMIR Medical Informatics, 2026;14:e89422 (published 2026-09-30)
**DOI:** https://doi.org/10.2196/89422
**PubMed:** https://pubmed.ncbi.nlm.nih.gov/42815038/
**Full text used:** https://pmc.ncbi.nlm.nih.gov/articles/PMC13626646/
**Basis of this analysis:** FULL TEXT (PubMed Central open-access copy,
retrieved 2026-10-03). Table 1 was rendered in full and is used here. Figures
1–7 and Multimedia Appendices 1–6 were **not** retrievable. Appendix 4 holds the
per-model performance table and Appendix 5 the confusion matrices, so the
**specificity, positive predictive value and F-score of the chosen model are not
available in the text retrieved.** Where that matters below, it is said plainly
rather than estimated.
**Date decoded:** 2026-10-03
**Evidence grade:** 2/5

All identifiers above were verified against the live PubMed and PubMed Central
records on 2026-10-03. Nothing here is based on a guessed or reconstructed link.

---

# The Gist

China runs a two-step bowel-cancer screening programme. Step one is cheap: a
questionnaire and a stool test. Anyone who looks high-risk on either gets step
two — a colonoscopy, which is invasive, expensive, and in short supply.

This team's idea is to slot a third thing in between: a computer model that
re-sorts the people who passed step one, so the ones most likely to actually
have a polyp get their colonoscopy first. The model uses only things already
collected — age, sex, smoking, family history, waist, diet — so it costs nothing
extra to run. That is a genuinely sensible ambition, and the authors are
upfront that the point is rationing a scarce resource, not making a diagnosis.

They built nine different models on 4,108 people aged 50–74 in Wenzhou, and
picked one, LightGBM, because it caught the most polyps. Here is what it caught:
**106 of the 163 polyp cases in the test set.** That is the paper's headline
"recall" of 0.6503. The other way to say it is that **the tool misses 57 of 163
polyps — 35% of them.**

Now hold that against what the tool is for. Everyone in this study had *already*
been referred for colonoscopy by the existing programme, and all of them got
one. So the current protocol, in this cohort, catches 100% of the polyps by
construction. A triage layer can only *reduce* colonoscopies — by refusing some
people the current rules would have sent. This one refuses 35% of the polyps
along with them. The paper never reports how many colonoscopies that would save,
and the number needed to work it out is in an appendix that did not render.

The discrimination number is weak and the authors say so: the best model
reached an **AUC of 0.672 (95% CI 0.623–0.722)**, where 0.5 is a coin flip. For
scale, in this same cohort you can get about two-thirds of the way there with
one question — "is this person male?" — which by itself catches 56.4% of polyps.
The nine algorithms, twenty-one predictors, SHAP plots and LIME plots buy you
roughly **9 extra percentage points of sensitivity** over that single question,
and the paper does not report the specificity you would have to give up to get
them.

But the thing that most changes how you should read this paper is a number in
the methods that the discussion never returns to. The screening programme
colonoscoped 18,914 people and found polyps in 12,094 of them — a 63.9% hit
rate. The study then analysed 4,108 of those people, of whom 816 had polyps —
19.9%. **The authors kept 48.3% of the no-polyp people and 6.7% of the polyp
people.** Controls survived the exclusion criteria at **7.2 times** the rate of
cases. 11,278 polyp cases were dropped, and the paper does not say why.

That single fact means the 19.9% polyp rate the model was trained and scored
against is an artefact of the authors' exclusions, not a property of anybody
they would ever screen. And nearly every number downstream — the calibration
plots, the chosen cutoffs, any claim about who to refer — inherits that artefact.

# Study Snapshot

- **Study type:** **Cross-sectional** model development with an internal
  hold-out split. The authors label it cross-sectional themselves, which is
  honest and matters: predictors and polyps were measured at the same moment, so
  nothing here establishes that anything *causes* a polyp or precedes it.
- **Setting:** A population-based colorectal cancer screening programme across
  all 12 districts and counties of Wenzhou, Zhejiang Province, China,
  May–November 2021. The authors call this "multicenter recruitment," then in
  the limitations call it a "single-center screening program." Both can be true
  — many sites, one programme — but the first framing oversells it.
- **Who:** Residents aged 50–74.
- **The funnel:** 276,395 enrolled in the programme → 257,481 never had a
  colonoscopy (not flagged high-risk, or declined) → 18,914 completed one →
  12,094 with polyps, 6,820 without → **4,108 analysed (816 cases, 3,292
  controls)** after excluding prior malignancy, precancerous gastrointestinal
  lesions, hereditary syndromes, inflammatory bowel disease, severe
  comorbidity, and incomplete data.
- **Outcome:** Any histologically confirmed colorectal polyp found at
  colonoscopy. **Not** stratified by subtype — a trivial hyperplastic polyp and
  a sessile serrated lesion count the same. The authors flag this as a
  limitation; it is a large one, because the subtypes have very different
  cancer risk.
- **Predictors:** 36 candidates narrowed to 21 by LASSO regression and the
  Boruta algorithm, both run on the training set only.
- **Split:** 80:20. Training 3,287 (653 cases); validation 821 (163 cases).
- **Rebalancing:** SMOTE applied **to the training set only**, bringing it to
  a 50:50 class split.
- **Models:** Nine — logistic regression, support vector machine, Gaussian
  naive Bayes, multilayer perceptron, decision tree, random forest, XGBoost,
  LightGBM, CatBoost. Hyperparameters by 10-fold cross-validation.
- **How evaluated:** AUC with DeLong confidence intervals, precision-recall
  curves with average precision, accuracy, sensitivity, specificity, predictive
  values, F-score, Brier score, calibration plots, decision curve analysis.
  Interpretability by SHAP and LIME.
- **Headline results:** XGBoost best AUC at 0.672 (95% CI 0.623–0.722), average
  precision 0.430. LightGBM chosen for triage on recall 0.6503 (106/163).
  Referral cutoffs 0.2432 for XGBoost, 0.1395 for LightGBM.
- **External validation:** **None.** The authors say so.
- **Registration / reporting standard:** No prospective registration and no
  TRIPOD or TRIPOD+AI statement mentioned. Ethics approval from Zhejiang Cancer
  Hospital (IRB-2023-464); written informed consent obtained.
- **Funding and conflicts:** Not stated in the text retrieved.

# How Strong Is This Evidence? — Grade 2/5

Two out of five means: the measurements and the reporting are good enough to
work with, but the conclusion the paper draws is not supported by them, and you
should not act on the recommendation.

What earns the points. The methods reporting here is better than most papers
this list has seen. They tested whether their missing data were missing at
random (Little's test, p=.37) before deleting incomplete records, instead of
assuming it. They ran feature selection inside the training set only and said
so explicitly. They applied SMOTE to the training set only — which, if you are
going to oversample at all, is the correct way. They reported calibration
plots, Brier scores, decision curve analysis, and precision-recall curves with
average precision, not just an AUC. They used DeLong confidence intervals. They
stated their AUC of 0.672 plainly rather than burying it. Their limitations
section names the single programme, the absent external validation, the
unstratified histology, and the impossibility of causal inference. A reader can
audit this paper, which is precisely why the problems below are findable.

What costs the points, in order of how much it matters.

**One: the selection cliff.** 93.3% of the available polyp cases were discarded
and 51.7% of the available controls — controls retained at 7.2 times the rate
of cases. This converts the study from a cohort into something closer to an
investigator-chosen case-control mix, and the paper neither says so nor adjusts
for it. Everything prevalence-dependent is then uninterpretable: the calibration
plots, the positive predictive value, and above all the two referral cutoffs,
which are probabilities and therefore only mean something relative to a base
rate. The exclusion criteria listed cannot plausibly account for it — one of
them, "precancerous gastrointestinal lesions," would if applied literally
remove most of the polyp cases, since colorectal polyps *are* precancerous
gastrointestinal lesions. Either the criterion was applied in a way the paper
does not describe, or the case losses came from somewhere unstated.

**Two: the cutoff was chosen on the test set.** The methods say "the optimal
probability cutoffs were derived from the validation dataset" — the same 821
people used to report the performance. So recall 0.6503 is not an out-of-sample
estimate of anything. It is the best operating point findable on the very data
it is quoted from. The honest version of that number is unknown and lower.

**Three: the discussion contradicts the results.** The paper writes that its
model "showed substantially better discrimination" than prior work, and then in
the same paragraph lists the comparators: an electronic-health-record AdaBoost
model at AUC 0.687, a genetic-risk-score logistic model at 0.666, and
questionnaire or nomogram models at 0.68 to 0.75. Its own figure is 0.672.
Three of the four comparators are *better*, and two sentences later the paper
calls the AdaBoost model "comparable to our results." Both claims cannot stand.

**Four: the Brier claim is measured against the wrong yardstick.** The paper
reassures the reader that "Brier scores [were] consistently below 0.25." 0.25
is the score you get on a perfectly balanced dataset by predicting 0.5 for
everyone. On this validation set, where polyps run at 19.9%, the
no-information score is p(1−p) = **0.159**. Any model scoring between 0.159 and
0.25 is therefore *worse than quoting the base rate*, and the paper's stated
bar cannot distinguish the two. This is not a nitpick — it is the exact
fingerprint of having trained on SMOTE-balanced data and then forgotten which
world the test set lives in.

**Five: the Results and the Discussion disagree about waist circumference.**
The Results report that beyond roughly 85 cm "the SHAP values decreased sharply
and nearly linearly" — the model treats a bigger waist as *lower* risk past that
point. The Discussion then presents the same 85 cm inflection as confirming
that central obesity drives polyp risk, citing literature on elevated waist
circumference. The model's behaviour as described and the mechanism as narrated
point in opposite directions.

**Six: the paper's own worked examples break its own threshold.** The LightGBM
referral cutoff is 0.1395. The SHAP force plot the paper presents as a
**low-risk** individual has a predicted risk of **0.143** — above the cutoff, so
that person gets referred. And the individual presented as **high-risk** scores
**0.178**, which is *below* the model's own average prediction of 0.198. Both
illustrative patients would be sent for colonoscopy, and neither illustrates
what it is captioned as illustrating.

**Seven: no external validation, and a cross-sectional design.** The authors
name both. The thresholds (85 cm waist, 25 kg/m² BMI, age 50) are presented as
discovered biology; they are features of one gradient-boosted model fitted to
one city's data with no replication.

# The Editor's Concerns

If this came across my desk at a journal, these are the queries I would send
back before considering it.

**The 11,278 missing cases need a full accounting.** Give the exclusion
cascade as counts, case and control separately, criterion by criterion. Until
that is in the paper, no prevalence-dependent result in it can be read. This is
a major revision, not a clarification.

**Re-derive the cutoffs somewhere other than the test set,** by nested
cross-validation inside the training data, and re-report sensitivity and
specificity at those fixed cutoffs on the untouched hold-out. Expect the recall
to fall.

**Report the number this paper exists to establish, and does not contain:**
how many colonoscopies the tool saves per polyp missed. One sentence —
"referring the X% of the validation set above the cutoff would have required N
colonoscopies instead of 821, catching 106 of 163 polyps instead of 163" — would
let a reader judge the trade. Its absence is the paper's central reporting gap.

**Benchmark against the trivial rule.** In the authors' own Table 1, "refer
every man" has sensitivity 0.5637 (460/816) and specificity 0.5933
(1 − 1,339/3,292), implying an AUC of 0.578 for a one-variable rule. A reader
cannot tell from the text retrieved whether LightGBM's operating point beats it,
because LightGBM's specificity is only in an appendix. **For the headline point
to be a real improvement, its specificity at recall 0.6503 must exceed roughly
0.59** — put that comparison in the main text.

**Reconcile or retract "substantially better discrimination."** As the
comparator AUCs are listed, the claim is contradicted on the page.

**Fix the Brier reference point** to the no-information score at the test set's
actual prevalence (0.159), and report a scaled Brier or Brier skill score so the
reader sees how much of the uncertainty is explained. Also report calibration
slope and calibration-in-the-large after the SMOTE-induced inflation, not only a
plot.

**Three internal inconsistencies to correct.** (a) The text says the control
group was "1399 out of 3292 (42.5%)" male; Table 1 says 1,339 (40.7%), and
1,799 total males minus 460 case males is 1,339, so the text is wrong. (b) The
training set is described as "case-to-control ratio=653:3287" — but 653/3,287 =
19.87%, which is the figure quoted, so 3,287 is the training *total*, and the
controls number 2,634. As written the two numbers sum to 3,940 out of a dataset
of 4,108. (c) The balanced training set is given as "2643 cases and 2643
controls," where the implied control count is 2,634.

**One reported p-value cannot be right.** Unexplained weight loss appears in
7 of 816 cases and 0 of 3,292 controls, with p=.40. A Fisher exact test on that
table gives **p ≈ 2.4 × 10⁻⁵**. Either the counts or the p-value is in error,
and the variable was carried into the final 21 predictors.

**Soften "largely comparable."** The Results state the two groups were
"largely comparable across most sociodemographic, clinical, and lifestyle
variables" apart from age and sex. By the authors' own Table 1, BMI, waist
circumference, education, smoking status, secondhand smoke, alcohol, family
history of cancer, family history of polyps and diabetes all differ at p<.001 —
nine further variables.

**Explain hematochezia.** It was retained as a predictor, yet appears in 0.2%
of cases and 0.6% of controls — rectal bleeding is *less* common in the polyp
group. Perhaps real, perhaps a coding artefact, but it needs comment before a
model trained on it is proposed for triage.

**State when outliers were winsorised.** Feature selection is explicitly
post-split, but the outlier replacement (to the 1st/99th percentile) and
Little's test are described before the split. If the percentiles were computed
on the whole dataset, that is leakage.

**Withdraw "immediately implementable."** A model at AUC 0.672, with a
test-set-tuned cutoff, no external validation, and a training prevalence that
is an artefact of unexplained exclusions, is a research finding. The conclusion
as written asks for deployment.

# Statistics Spotlight

Six ideas, each of which this paper makes unusually concrete.

## 1. SMOTE, and the world a model thinks it lives in

Only 19.9% of these people had polyps. Many algorithms respond to that by
learning the cheap trick: predict "no polyp" for everyone and be right 80% of
the time. The standard fix is **SMOTE** — synthetic minority oversampling
technique. It takes each real case, finds its nearest neighbours among the other
cases, and manufactures new fake cases on the lines between them, until the
classes are even.

Here is the scale of it in this paper. The training set had 653 real cases and
2,634 real controls. Balancing it to 50:50 required **1,981 invented cases**. So
**75.2% of the polyp patients the model learned from do not exist.** They are
interpolations between real patients.

What that costs you is not discrimination — the *ranking* often survives
oversampling fine. What it costs you is **calibration**: the meaning of the
number the model outputs. A model trained on a 50:50 world has learned that
polyps are a coin flip, so it emits probabilities centred near 0.5 and scaled to
a prevalence that is twice and a half the real one. Feed it a real patient at
19.9% prevalence and "0.4" does not mean a 40% chance of a polyp. It means
nothing in particular until you recalibrate, which this paper does not do.

And that is exactly why the Brier reassurance misfires (idea 2), and why the two
cutoffs — 0.2432 and 0.1395 — float free of any base rate.

**The pairing with yesterday's paper.** Entry 34 in this list, Shimizu et al. on
pneumonia risk in Japanese over-75s, faced a far worse imbalance: 0.41%
outcomes, not 19.9%. They **deliberately refused to rebalance** — no
oversampling, no class weighting, no SMOTE — on the stated grounds that
artificial rebalancing inflates baseline risk and wrecks calibration. Their
model's calibration came out close to perfect, and that was the single most
impressive thing in the paper. Ye et al. rebalanced, and their calibration claim
is the weakest thing in theirs. Same methodological fork, opposite turns, two
days apart, and the results came out exactly as the theory predicts. If you
remember one contrast from this list, make it this one.

The practical rule: **rebalance if you only care about ranking people; never
rebalance if you care what the probability means.** Anything that gets used at a
threshold — refer or don't refer, treat or don't treat — cares what the
probability means.

## 2. The Brier score has a reference point, and it moves

A **Brier score** is the average squared error of a probability forecast. Say
30% and the thing happens: you are charged (1 − 0.30)² = 0.49. Say 30% and it
doesn't: (0 − 0.30)² = 0.09. Lower is better, 0 is perfect.

The trap is that a raw Brier score is meaningless without knowing what the
lazy forecast scores. The lazy forecast is "say the base rate to everybody," and
it scores exactly **p(1 − p)**.

- On this paper's validation set, p = 0.1986, so the lazy score is **0.159**.
- On a perfectly balanced 50:50 set, p = 0.5, so the lazy score is **0.250**.

The paper's bar — "Brier scores consistently below 0.25" — is the lazy bar for
the *balanced training set*. On the real validation set, any score between 0.159
and 0.25 is worse than knowing nothing but the base rate. The bar as stated
cannot tell a useful model from a useless one.

The fix is to report a **scaled Brier score** (also called Brier skill score):

> scaled Brier = 1 − (model Brier ÷ base-rate Brier)

0 means no better than the base rate; 1 means perfect; **negative means worse
than saying nothing.** Shimizu et al. reported theirs — it was 0.7%, and quoting
it was the most honest number in that paper. When you read any model paper,
look for this. If you only see a raw Brier, compute p(1 − p) yourself from the
prevalence and check which side of it the model landed on.

## 3. Average precision, and why *its* baseline is the prevalence

When the outcome is rare, the ROC curve flatters models, because specificity
has a huge denominator and a flood of false positives barely moves it. The
honest companion is the **precision-recall curve**: recall (of the people who
have polyps, what share did we flag?) against precision (of the people we
flagged, what share have polyps?). **Average precision (AP)** is the area under
it.

Credit where due: this paper reported it, which most don't. XGBoost's AP was
**0.430**.

The crucial fact nobody tells you: **the no-skill baseline for average precision
is not 0.5 — it is the prevalence.** A model that ranks at random achieves
precision equal to the base rate at every recall, so AP = 0.1986 here. So:

> AP 0.430 ÷ 0.1986 baseline = **2.17× better than random ranking**

That is the most favourable honest reading available of this paper, and it
deserves stating. The ranking really does carry signal — roughly a doubling of
precision over chance. The problem is not that the model is noise. The problem
is that a 2.17× lift on a 0.672 AUC is not enough to hang a referral decision
on, and the paper's conclusion needs it to be.

Whenever you see an AUC near 0.5 declared useless and an AP near 0.4 declared
good, check the prevalence before you believe either.

## 4. Choosing the cutoff on the test set

A model outputs a number between 0 and 1. Turning that into "refer / don't
refer" needs a **threshold**, and the threshold is a *fitted parameter* just as
much as any coefficient. If you pick it by looking at the data you then report
performance on, you have let the test set into the training.

This paper says it plainly: "The optimal probability cutoffs were derived from
the validation dataset." That is the same 821 people whose 106-of-163 recall is
the headline.

Why it inflates: with 163 cases there are many candidate thresholds, and the
one that looks best is partly best by luck. On fresh data that luck does not
repeat. The usual fix is **nested cross-validation** — choose the threshold in
inner folds of the training data, then apply it, frozen, to a hold-out you have
never looked at.

This is a cousin of the better-known leak (doing feature selection before the
split), and this paper correctly avoided *that* one. It is worth seeing that you
can get the famous leak right and the obscure one wrong in the same paper.

**The reader's test:** find the sentence that says where the cutoff came from.
If it came from the same data as the reported sensitivity, treat the sensitivity
as an upper bound.

## 5. When the sample's prevalence is the investigator's choice

A **cohort** takes everybody and watches what happens; the share with the
outcome is a fact about the world. A **case-control** study picks cases and then
picks controls; the share with the outcome is a fact about the *researcher*.

This paper is described as cross-sectional, but look at what the exclusions did:

- Available: 12,094 cases, 6,820 controls (63.9% cases)
- Analysed: 816 cases, 3,292 controls (19.9% cases)
- Retention: **6.7% of cases, 48.3% of controls** — 7.2:1

The outcome rate was effectively *set* by the exclusion process, from 63.9% down
to 19.9%, and the paper does not explain how.

Three things break when that happens, and they are exactly the three things this
paper's conclusion rests on.

**Positive predictive value breaks.** PPV depends on prevalence and nothing
else can rescue it. A PPV measured at a manufactured 19.9% tells you nothing
about PPV at the 63.9% the real screening queue runs at — nor at the ~6.8% of
all enrollees (18,914 of 276,395) the programme actually colonoscopes.

**Calibration breaks.** A calibrated probability is calibrated *to a base rate*.
Change the base rate and every predicted probability is wrong by a predictable
factor — which is why the calibration plots cannot be read at face value.

**The threshold breaks.** 0.1395 is a probability. Probabilities are only
comparable within a fixed prevalence.

Discrimination — AUC, and the ranking of one person above another — is the one
thing that *does* survive, because it only depends on order. That is why 0.672
is the only number in this paper you can take more or less at face value, and
it is a weak number.

**What to look for in any paper:** find the flow diagram, and check whether
cases and controls were lost at the same rate. If they weren't, and nobody says
why, stop reading the probabilities and read only the rankings.

## 6. The trivial baseline, in one line

Before you are impressed by nine algorithms, ask what one question gets you.
This paper's Table 1 lets you check, because it reports sex by group.

"Refer every man":

- sensitivity = 460 / 816 = **0.564**
- specificity = 1 − 1,339 / 3,292 = **0.593**
- referral rate = 1,799 / 4,108 = **0.438**

And a useful trick: for a **binary** rule, the AUC is just the average of
sensitivity and specificity.

> AUC of "refer every man" = (0.564 + 0.593) / 2 = **0.578**

Against the paper's 0.672. So the machinery does add discrimination — about 9
points of AUC, and 8.7 points of sensitivity at the chosen operating point —
but you now know the scale of what is being added, and it is not the leap the
abstract implies. Whether the chosen point is a *net* improvement over "refer
every man" depends on its specificity, which the retrieved text does not
contain; it would have to clear roughly 0.59.

Run this check on every prediction paper you read. Age alone, sex alone, "the
oldest third," "anyone already on three medications" — compute the trivial
rule's sensitivity and specificity from the baseline table and average them. It
takes thirty seconds and it reframes most machine-learning abstracts.

# Jargon Translator

- **AUC / area under the ROC curve** — pick one person with a polyp and one
  without at random; the AUC is the chance the model scores the polyp person
  higher. 0.5 is a coin flip, 1.0 is perfect. Here, 0.672.
- **Recall / sensitivity** — of the people who truly have the thing, the share
  the model flags. Here 0.6503, i.e. 106 of 163.
- **Precision / positive predictive value** — of the people the model flags, the
  share who truly have the thing. Depends on prevalence. Not in the text
  retrieved.
- **Specificity** — of the people who truly don't have the thing, the share the
  model correctly leaves alone. Not in the text retrieved.
- **SMOTE** — manufactures synthetic examples of the rare group by interpolating
  between real ones, until the classes are even. Here it invented 1,981 of the
  2,634 training cases.
- **Class imbalance** — when one outcome is much rarer than the other, so a
  model can score well by always guessing the common one.
- **Brier score** — average squared error of a probability forecast. Only
  interpretable against p(1−p), the score for always predicting the base rate.
- **Average precision (AP)** — area under the precision-recall curve. Its
  no-skill baseline is the prevalence, not 0.5.
- **Calibration** — whether "20%" actually happens 20% of the time. Separate
  from, and more fragile than, discrimination.
- **Decision curve analysis (DCA)** — plots net benefit against the threshold a
  clinician would act at, comparing the model to "treat everyone" and "treat
  nobody."
- **LASSO regression** — a regression that shrinks unhelpful predictors' weights
  to exactly zero, selecting features as a side effect.
- **Boruta** — a random-forest wrapper that keeps a predictor only if it beats
  randomly shuffled copies of itself ("shadow features").
- **XGBoost / LightGBM / CatBoost** — gradient-boosted tree ensembles. They
  build many small decision trees in sequence, each correcting the last. Good at
  finding thresholds and interactions; they do not output calibrated
  probabilities by default.
- **SHAP (Shapley Additive Explanations)** — splits a single prediction into a
  baseline plus one contribution per feature. Describes what the *model* did,
  not what the *body* does.
- **LIME** — fits a simple local model around one prediction to explain it.
- **DeLong method** — the standard way to put a confidence interval on an AUC.
- **Little's MCAR test** — checks whether missing values look randomly scattered.
  Non-significant (here p=.37) is weak reassurance that deleting incomplete rows
  won't bias things.
- **Winsorising** — replacing extreme values with a percentile cap rather than
  deleting them.
- **Cross-sectional** — everything measured at one time point, so you cannot
  tell which came first.
- **Nested cross-validation** — tune choices (including thresholds) in inner
  folds, measure performance in outer folds, so tuning never sees the scoring
  data.

# What You Can (and Can't) Say

**You can say:** a machine-learning model built on routine questionnaire data
from 4,108 screening participants in Wenzhou, China ranked people's colorectal
polyp risk better than chance — AUC 0.672 (95% CI 0.623–0.722), average
precision 0.430 against a 0.199 no-skill baseline.

**You can say:** at the operating point the authors selected, the model
identified 106 of 163 polyp cases in the hold-out set, and missed 57.

**You can say:** the authors reported calibration, decision curves and
precision-recall alongside the AUC, tested their missing-data assumption, and
confined feature selection and oversampling to the training set — all of which
is better practice than most prediction-model papers manage.

**You cannot say** this tool is ready to triage anybody. The referral threshold
was chosen on the same data used to report its performance; there is no external
validation; and the prevalence it was fitted at is a product of unexplained
exclusions.

**You cannot say** it reduces missed diagnoses. It can only reduce colonoscopies
relative to the existing protocol, and it does so by declining 35% of the
polyps. The paper's framing of a "high-recall digital filter" that "minimises
the risk of missed diagnoses" inverts this: compared with what the programme
already does for these people, the tool *adds* missed diagnoses.

**You cannot say** the model outperforms existing approaches. Three of the four
comparators the paper itself cites have equal or higher AUCs.

**You cannot say** 85 cm of waist, 25 kg/m² of BMI or age 50 are validated risk
thresholds. They are inflection points in one unreplicated model's SHAP plots,
and in the case of waist circumference the Results and Discussion describe the
direction differently.

**You cannot say** smoking, sex or family history were shown to *cause* polyps.
This is cross-sectional, and SHAP describes the model, not biology.

**You cannot use** the predicted probabilities as risk estimates for an
individual. They came from a model trained on a 50:50 synthetic world and were
never recalibrated.

# Bottom Line for Your Life

If you are 50 to 74 and your country offers bowel-cancer screening, the useful
information in this paper is not the model. It is the setting the model was
built in: a two-step programme that screens with a questionnaire and a stool
test, and sends the people who flag positive for colonoscopy. That programme
colonoscoped 18,914 people and found polyps in 12,094 of them. **Do the
first step.** A stool test and a questionnaire are the cheapest high-value thing
in cancer screening, and polyps removed early are cancers that never happen.

The risk factors the model leaned on are the familiar ones and they are real
enough on other evidence: being male, currently smoking, a family history of
polyps, a larger waist, and age over 50. The one of those you can change is
smoking, and the paper cites evidence that twenty years after quitting the
excess risk is comparable to never having smoked.

What this paper does **not** give you is a reason to accept or decline a
colonoscopy. If a programme has already flagged you, a model that misses one
polyp in three is not a second opinion. Go.

And if you ever see a tool like this offered as a reason to *delay* your
colonoscopy — that is the use case the authors propose, and it is the one their
own numbers do not support. Ask what its sensitivity is, who tuned its
threshold, and on whose data it was checked.

**This is education about how to read a study, not medical advice. Decisions
about screening belong with you and your doctor.**

---

*Decoded 2026-10-03. Source: PubMed and PubMed Central, accessed 2026-10-03.
Full text read from PMC13626646; Figures 1–7 and Multimedia Appendices 1–6 were
not retrievable, so the chosen model's specificity, PPV and F-score are not
reported above. Derived figures — the 7.2:1 case/control retention ratio, the
1,981 synthetic cases (75.2% of the training minority class), the 0.159
no-information Brier score, the 2.17× average-precision lift, the "refer every
man" baseline (sensitivity 0.564, specificity 0.593, AUC 0.578), and the Fisher
exact p ≈ 2.4 × 10⁻⁵ for unexplained weight loss — were computed from the
paper's own reported counts and are labelled as derived wherever they appear.*
