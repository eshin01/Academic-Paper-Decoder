# The Mental Map — Evaluating AI Model Performance

Reference for study design and paper appraisal. Invoked by the prompt
**"mental map"**, which renders this landscape on demand.

Core idea: **model evaluation has three separate report cards.** A paper that
shows only one has shown you a third of the truth. Which card matters most
depends on what the model's output is actually used for.

---

## Family 1 — DISCRIMINATION
*"Can it rank sick above healthy?"*

Threshold-free. Measures ordering, not decisions and not probabilities.

- **AUROC / C-statistic** — probability that a random true case is scored above
  a random non-case. 0.5 = coin flip, 1.0 = perfect.
- **Concordance index (Harrell's c)** — the survival-analysis cousin, for
  time-to-event outcomes with censoring.
- **Rank-biserial r / Somers' D** — effect sizes for ordinal comparisons.

**Blind spot:** insensitive to class imbalance. On a rare disease, AUROC can
sit in the 0.90s while nearly every alarm is false. It also says nothing about
whether the model's stated probabilities mean anything.

**Report when:** the output is a ranking or triage order.

---

## Family 2 — CLASSIFICATION AT A DECISION POINT
*"Once it commits to yes/no, is it right, and is the alarm burden survivable?"*

Threshold-dependent. This is where a model becomes an action.

- **Sensitivity / specificity pair** — always as a pair, at a stated threshold.
- **PPV / NPV** — what a positive or negative result means for this patient;
  both move with prevalence.
- **F1 score** — harmonic mean of PPV and sensitivity; cannot be gamed by
  favoring one; ignores true negatives; the metric that lets a model be
  compared against humans, who give one hard call rather than a curve.
- **AUPRC** — precision-recall curve area; the imbalance-aware answer to
  AUROC. Baseline equals prevalence, so it is not comparable across cohorts.
- **Work-up-to-detection ratio (number needed to evaluate)** — how many
  patients are investigated per true case found. The alert-fatigue metric.
- **Net benefit / decision curve analysis** — folds in the relative cost of
  false positives vs false negatives across plausible thresholds.

**Blind spot:** every number here shifts with prevalence and with the chosen
cutoff. Enriched test sets inflate them.

**Report when:** the output triggers an action — an alert, a referral, a test.

---

## Family 3 — CALIBRATION
*"Are its probabilities honest?"*

- **Calibration plot** (predicted vs observed probability, with a slope and
  intercept) — the least foolable of the three; always prefer the plot.
- **Brier score** — mean squared error of predicted probability; punishes
  confident-and-wrong hardest. Blends calibration with discrimination, so a
  model that predicts the base rate for everyone can score deceptively well.
- **Expected calibration error (ECE)** — binned average gap between predicted
  and observed rates.
- **Avoid Hosmer–Lemeshow at large n** — it flags trivial deviations as
  significant once sample sizes reach the tens of thousands.

**Blind spot:** a perfectly calibrated model can still be useless at ranking.
Calibration is necessary, never sufficient.

**Report when:** a number is shown to a human, or a threshold drives care.
A model can rank flawlessly and still double everyone's stated risk — which
silently treats the wrong patients when the protocol says "act above 15%."

---

## Cross-cutting: does the number survive contact with reality?

These sit outside the three families and decide whether any of the above
generalizes.

- **Uncertainty** — confidence intervals on every headline metric (bootstrap
  for AUROC/F1). A point estimate without an interval is a rumor.
- **Validation tier** — internal split < temporal split < external site <
  prospective. Distinguish *architecture generalization* (recipe retrained
  elsewhere) from *external validation* (frozen model shipped elsewhere).
- **Reliability of the ground truth** — inter-rater agreement (Krippendorff's
  alpha, Cohen's/Fleiss' kappa). No model can be validated beyond the
  reliability of its answer key. Biopsy-proven truth > expert consensus >
  chart codes > proxy labels.
- **Label choice** — what is the model *actually* trained to predict, and for
  whom is that proxy distorted? (Cost as a proxy for health need; billing
  codes as a proxy for diagnosis.)
- **Subgroup performance** — the aggregate number hides per-group failure.
- **Robustness** — order sensitivity, prompt sensitivity, and stability across
  reruns, especially for LLMs.
- **Comparator fairness** — was the human baseline stripped of context the
  model also lacked, or of context a real clinician would have?

---

## Design checklist (use when planning a study)

1. What decision does the output drive? That names the primary family.
2. What is the ground truth, and how reliable is it? Measure and report it.
3. What is the real-world prevalence, and does the test set match it? If
   enriched for measurement, say so and state what will not generalize.
4. Pre-specify the threshold and the primary metric. Report a metric from each
   family, each with a confidence interval.
5. Report alarm burden in clinical units, not just accuracy.
6. State the validation tier honestly, and pre-plan subgroup analyses.
7. Name the asymmetry: is a miss worse than a false alarm here? If yes, F1's
   equal weighting is the wrong summary — use F-beta, net benefit, or
   sensitivity at fixed specificity.
