# Deep learning-based echocardiography for cardiac assessment: a systematic literature review and meta-analysis

**Authors:** Romano-Martinez A, Zeid S, Krolevets M, Kontohow-Beckers K, Ten Cate V, Lurz P, Engelhardt S, Kramer S, Troebs SO, Wild PS (ten authors — Preventive Cardiology and Preventive Medicine, University Medical Centre of the Johannes Gutenberg-University Mainz; Institute of Molecular Biology, Mainz; German Centre for Cardiovascular Research (DZHK), Rhine-Main and Heidelberg/Mannheim; Centre for Thrombosis and Hemostasis, Mainz; Heidelberg University Hospital; Institute of Computer Science, Mainz. One author's author-line affiliation includes Boehringer Ingelheim International GmbH.)
**Journal:** European Heart Journal — Digital Health, 2026; 7(9): ztag148 (published 19 October 2026)
**Decoded:** 2026-10-30
**Analysis basis:** **FULL TEXT** (retrieved from PubMed Central, PMC13678652; 53,131 characters). The complete body was read — search strategy, eligibility criteria, data extraction rules, statistical methods, all five results sections, sensitivity analyses, discussion and limitations, plus Tables 1 and 2 in full. **Three things are not retrievable and are flagged throughout:** the forest plots (Figures 4, 5 and 6), whose alt-text is qualitative only; Table 3's per-study rows, which span the raw data; and the supplementary material, which holds the search query, the risk-of-bias detail and the 160-study list.

**Source links (verified):**
- DOI: https://doi.org/10.1093/ehjdh/ztag148
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42899077/
- Full text (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC13678652/

**Basis of link verification.** Direct URL fetching is blocked from this session (`doi.org` does not resolve under the network policy here). Verification was done against the live PubMed/NLM record: a query for PMID 42899077 returned this exact title, these ten authors, European Heart Journal — Digital Health volume 7 issue 9 article ztag148, DOI `10.1093/ehjdh/ztag148` and PMC ID `PMC13678652`; the full text was then retrieved from PubMed Central by that PMC ID and matches. Both halves of the chain were confirmed independently.

**Reporting guideline: PRISMA**, named in the Figure 1 caption and used for the study-selection flowchart. Risk of bias assessed with a **modified Risk of Bias Assessment Tool for non-randomized Studies**. **No PROSPERO or other prospective protocol registration appears anywhere in the retrieved text.** **Funding: not reported in the text retrieved. Competing interests: no statement in the text retrieved** — though one author's affiliation line names a pharmaceutical company, which is disclosed there.

> **Why this paper today.** All four deferred papers were re-checked and remain blocked; the JAMA OpenEvidence study (PMID 42879271, PMC13673371) reached **day 15** of serving an empty PMC body. This was spare #2 from the 10-28 restock, and it is **the first meta-analysis in sixty-two decoded papers.** Everything this list has graded so far has been a single study. A meta-analysis sits a rung higher on the evidence ladder by design — it is supposed to take many studies and produce one trustworthy number. What makes this one worth a full day is that it is carefully built and **it does not produce that number**, and the reason why is the most useful statistics lesson available this week.

---

## 1. The Gist

An echocardiogram is an ultrasound of the heart — a short video loop showing the chambers moving. Cardiologists use them constantly: to measure how hard the heart is pumping, to spot a leaky valve, to decide what happens next. Reading one takes training and time, and two experts reading the same loop often disagree.

So for about a decade people have been building deep learning models to read them automatically. Hundreds of papers now exist, nearly all reporting good results.

Ten researchers in Mainz asked the obvious next question: **put together, what do all those papers actually show?** They searched three databases, screened **16,248 records**, read 635 papers in full, and included **160** — every study they could find where a model works on echo video start to finish with no human touching it in between. They sorted them into five jobs: predicting disease or death, reproducing standard measurements, outlining heart chambers, identifying which view the camera is showing, and judging image quality. Then they pooled the results.

**The pooling did not work, and the paper says so.**

For almost every task, the studies disagreed with each other far more than chance could explain. The statistic for this is called I², and it ran at **98–99%** across most analyses — meaning essentially all the variation between study results came from the studies being genuinely different, not from random noise. The authors then tried to explain the differences using model architecture, prediction target, training size, video resolution, frame count and batch size. For prediction tasks that brought I² down from 99.9% to **76.8%** — real progress, and still three-quarters unexplained. For segmentation, adding the moderators made it slightly **worse**, and a formal test said they explained nothing at all (p = 0.99).

And here is the thing that follows from it, which took some checking to be sure of: **not one pooled estimate appears anywhere in this paper's abstract or results text.** Every pooled number lives inside a forest plot. The running text reports heterogeneity statistics and moderator tests, and no answer.

That is not a failure of effort. It is the honest output of a well-run synthesis of a literature that is not yet poolable — and the descriptive findings that come with it are genuinely valuable. **Nearly half the work in this field, 75 of 161 task entries, has never been tested on data from outside the institution that built it.** Only 16 of the 160 papers used the architectures the rest of machine learning has moved to. And for chamber segmentation, performance on outside data has been **getting worse** over seven years.

## 2. Study Snapshot

**Study type:** a **systematic review with meta-analysis** of diagnostic and prediction-model performance. On the evidence ladder this design sits above any single study, because it is built to find everything rather than report one result — but it inherits the quality of what it finds.

**Search:** PubMed, Cochrane CENTRAL and Web of Science, limited to work published after 2014 up to 9 June 2026. The search query is in the supplement, which was not retrievable.

**Selection flow (PRISMA):** **16,248** records identified → **7,903** duplicates removed, leaving 8,345 → **7,710** excluded on title and abstract → **635** full texts assessed → **160** included. The arithmetic reconciles exactly. **475 of the 635 papers read in full — 74.8% — were excluded at that stage**, and the overall yield was 160 in 16,248, just under 1%.

**Who screened:** two researchers independently, with uncertainties resolved by two further reviewers (a cardiologist and the senior author). On a random sample of **103 abstracts** the two screeners agreed **92.2%** of the time, **Cohen's κ = 0.78** (p < 0.001). Eligibility criteria were developed jointly by epidemiologists, cardiologists and deep-learning specialists.

**The inclusion rule that defines this review:** fully automated only — "execution without manual pre-processing, user-guided feature selection, or expert interpretation at inference time." Studies needing a human to pick frames, pull still images from video, assign the view, or draw a region of interest before the model runs were excluded. Manual annotation used only to create training labels was allowed. Image enhancement, denoising and reconstruction were excluded as not clinically interpretive. Transoesophageal, intracardiac, foetal, paediatric and animal studies excluded; point-of-care and stress echo included.

**The five task categories, across 161 task entries from 160 articles** (studies can appear in more than one):
- Prediction of disease or mortality — **59** (36.6%)
- Replication of established measurements — **59** (36.6%)
- Segmentation of cardiac structures — **59** (36.6%)
- Classification of chamber views — **22** (13.7%)
- Assessment of image quality — **10** (6.2%)

**The single most important descriptive number:** validation type was **external in 86 entries (53.4%) and internal only in 75 (46.6%)**. Nearly half this literature has never been tested on outside data. The paper defines external strictly — "independent datasets used for model testing only; studies in which the model was retrained or fine-tuned on the same dataset were not considered to have external validation."

**What the studies were about:** among prediction studies, valvular heart disease was the commonest target (21), then non-ischaemic cardiomyopathy (13), other structural disease (10) and heart failure (10); only 2 predicted mortality. Among replication studies, 42 of 59 targeted systolic function, usually left ventricular ejection fraction. Among segmentation studies, 53 of 59 segmented cardiac chambers.

**Architectures:** U-Net dominated segmentation; ResNet and 3D convolutional networks dominated prediction and measurement replication. **Only 16 of the 160 articles used what the authors call state-of-the-art architectures** — transformers and foundation models — which they describe as "a marked methodological gap between echocardiography research and the broader DL literature."

**Statistical approach:** random-effects meta-analysis; proportions transformed with the **double-arcsine (Freeman–Tukey)** method before pooling; variance for proportion metrics derived from the reported estimate and the testing sample size; separate analyses per metric per task, never mixing metric types without a valid transformation; **multilevel models** to handle studies contributing several effect sizes; meta-regression with moderators where at least five studies reported the variable; **Cook's distance** for outliers; funnel plots for small-study effects. Analyses in R 4.2.1 with `metafor`.

**Heterogeneity, which is the actual result:**
- *Prediction* (accuracy: 22 studies, 36 effect sizes; AUC: 23 studies, 70 effect sizes) — I² **99.9% / 98.8%** with architecture alone; **98.4% / 98.1%** adding target; **76.8% / 82.8%** adding training participants, resolution, frames and batch size.
- *LVEF mean absolute error* (9 studies) — I² **98.1%**; no architecture differences.
- *Segmentation, externally validated* (21 studies) — I² **98.2%**; by target **97.5% / 94.9%**; adding architecture, segmented area and training size took it **up to 98.8%**, and a formal test of moderators returned **p = 0.99**.
- *View classification, externally validated* (9 studies) — I² **75.8%**; splitting by chamber did not resolve it.
- *Quality assessment* (4 studies) — high heterogeneity, not resolved; accuracy lower than for the other tasks.

**Sensitivity analyses:** no Cook's distance above 1 for prediction-accuracy, view classification or quality studies. One above 1 among replication studies, after whose removal heterogeneity could not be computed for lack of power. **Five of the 21 segmentation studies had Cook's distance above 1, and after removing them I² fell to 0.00%.**

**Time trends, which point in different directions.** Prognostic generalisability has improved in recent studies. LVEF estimation has improved both internally and externally. View classification shows "enhanced generalization performance, despite a gradual decline in performance within derivation cohorts." And **segmentation performance on external data "has decreased over the past seven years."** Risk-of-bias ratings improved: studies from 2024 onward were less often rated high risk.

## 3. How Strong Is This Evidence? (Grade 3/5)

**The two halves of this paper deserve different grades, and the honest summary is that the review earns a 4 and the meta-analysis earns a 2.**

**What the review half does well:**

**Three databases, a decade-long window, PRISMA flow, and a reconciling audit trail.** 16,248 → 8,345 → 635 → 160, every step stated, every subtraction correct.

**Dual independent screening with the agreement quantified.** 103 abstracts double-screened, 92.2% raw agreement, κ = 0.78. Most reviews assert that screening was independent; far fewer measure it.

**An eligibility criterion that is genuinely well-chosen.** "Fully automated" is defined operationally and restrictively, with a list of the manual steps that disqualify a study. That single rule is what makes the 160 papers comparable to each other in the one way that matters for the question asked — can this run without a human? — and it is the strongest design decision in the paper.

**A data-extraction rule that prefers external results.** External testing results taken whenever available, held-out results only otherwise. That is the right precedence and it is stated.

**Multilevel models for dependent effect sizes**, which is the correct handling when one study contributes several numbers, and is frequently skipped.

**Funnel plots reported with the correct caveat** — that they are hard to interpret for heterogeneous diagnostic and prediction studies, and were therefore treated as exploratory and "not interpreted as definitive evidence for or against publication bias." This list has not previously seen a paper decline to over-read its own funnel plot.

**Limitations that name the real threats**, including the one that matters most: "overlap in training datasets, derivative model development, and repeated use of the same validation cohorts across studies may have reduced the independence of some performance estimates."

**What the meta-analysis half does not deliver:**

**There is no pooled estimate anywhere in the abstract or the results text.** I checked every occurrence of "pooled" and every confidence-interval mention in the running prose: all of them are in figure captions describing forest plots, or in the methods explaining the pooling procedure. The abstract's conclusion is "DL models achieve high performance across various applications in echocardiography" — with no number. For a paper whose stated purpose was "to provide pooled performance estimates," this is the central shortfall, and it is a reporting choice rather than an inevitability: the numbers exist in Figures 4, 5 and 6 and could have been written into the text.

**Heterogeneity at 98% was not resolved, and the paper reports pooled estimates anyway.** When between-study variation is that large, a pooled mean describes no real population. The authors say this; they also draw the forest plots.

**Dataset overlap is named but not quantified.** In echocardiographic deep learning a handful of public datasets are reused across very large numbers of papers. Twenty-one segmentation studies "externally validated" on substantially the same public data are not twenty-one independent tests. The review had the data to count this — it extracted dataset information from all 160 papers — and does not report it. This is the single biggest unaddressed threat to the pooled numbers.

**No prospective protocol registration appears in the retrieved text.** PROSPERO registration is the standard safeguard against a review's questions and analyses shifting after the results are seen, and it is not mentioned.

**No funding statement and no competing-interests statement** appear in the retrieved text, in a paper where one author's affiliation line names a pharmaceutical company and another names a university computer-science institute. The affiliation is disclosed; a formal declaration is the usual accompaniment.

**What would make it a 4:** write the pooled estimates and their intervals into the results text, and quantify dataset overlap across the included studies — even a single sentence saying how many of the 86 "external" validations used the same public datasets would change how every pooled number should be read.

**Why it is not a 2:** the descriptive findings are solid, well-supported and genuinely useful. That 46.6% of this literature has never been externally validated, that only 16 of 160 papers use current architectures, that segmentation performance on outside data has declined for seven years, and that risk of bias improved from 2024 — these are facts about the field that no single study could establish, they follow directly from a search that reconciles, and they are the kind of thing a reader of this list should actually act on.

## 4. The Editor's Concerns

**A meta-analysis that reports heterogeneity but not effects has inverted the usual reporting failure.** Most papers in this list over-report their point estimate and under-report the uncertainty. This one does the opposite: five results sections, every one leading with an I², and not a single pooled accuracy, AUC or Dice coefficient in the prose. A reader who takes away "deep learning does well at echocardiography" cannot say how well, from the text, at any task.

**The time trend nobody follows up.** Buried in the segmentation section: "Longitudinal assessment of Dice coefficients for the four major cardiac chambers indicates that **external performance of DL segmentation models has decreased over the past seven years**." That is a remarkable statement and the Discussion never returns to it. There are benign explanations — later studies testing on harder or more varied data, stricter reporting, less favourable test-set selection — and a less benign one, that the earliest externally-validated results were optimistic. The review is uniquely positioned to tell these apart and does not try.

**The view-classification trend is the mirror image and is also left alone.** Models show "enhanced generalization performance, despite a gradual decline in performance within derivation cohorts." Internal performance falling while external performance rises is the signature of a field learning to stop overfitting — arguably the single most encouraging finding in the paper, and it gets one clause.

**"External validation" is doing heavy lifting across very different situations.** The paper's definition is strict and good. But an external dataset from the same vendor, the same country and the same public repository is a much weaker test than one from a different health system, and the review treats them alike in the 53.4% figure. The authors raise the underlying issue in the limitations; the headline number does not reflect it.

**The unit of analysis varies across the pooled studies, and it sets the weights.** Sample size was reported as individuals in 134 entries (83.2%), as echocardiographic videos in 88 (54.7%) and as echocardiographic studies in 34 (21.1%) — these overlap. Variance, and therefore weight, was computed from the point estimate and the testing sample size. The authors handled this carefully, excluding studies without a count of individuals and marking ambiguous cases with an asterisk in the forest plots where "it could be reasonably interpreted from the text that a one-to-one correspondence with participants was intended." That is a disclosed judgement call that directly determines how much each study counts, and in a pooled analysis the weights are half the answer.

**Removing five of twenty-one studies produced perfect homogeneity, which should be read in both directions.** The sensitivity analysis found five segmentation studies with Cook's distance above 1; after removing them, I² was **0.00%**. One reading: a quarter of the studies were generating all the apparent disagreement, and the remaining sixteen tell a consistent story. The other reading: deleting the 24% of observations that disagree most and announcing that the rest agree is close to assuming the conclusion. Both readings are available and the paper offers neither.

**Within "prediction of disease or mortality" the studies are not predicting the same thing.** The category pools valvular disease (21 studies), cardiomyopathies (21), heart failure (10), mortality (2) and others. A pooled accuracy across those has no clinical referent — there is no patient for whom it is the answer. The authors mitigate this by entering target as a moderator, which cut I² only from 99.9% to 98.4%, so the mitigation did not work. Separate syntheses by target would have been the alternative, and the paper notes that for some targets, such as right ventricular segmentation, too few studies exist.

**Credit where it is due on two points this list usually criticises.** First, the authors explicitly refused to over-interpret their own funnel plots, giving the correct technical reason. Second, they connected their findings to the regulatory world honestly — naming three commercially approved systems (Caption Guidance, EchoGo Core, Us2.ai), noting those have undergone multicentre validation that most included studies have not, and flagging their exclusion as a source of bias that probably makes the review *understate* what the technology can do. Papers rarely volunteer that their own estimate may be too low.

**Where I am uncertain, stated plainly.** The forest plots in Figures 4, 5 and 6 contain every pooled estimate in this study and their alt-text descriptions are qualitative only, so **I cannot quote a single pooled number from this meta-analysis** — not one accuracy, AUC or Dice coefficient. Table 3's per-study rows were not parseable in the retrieved rendering. The supplementary material — the search query, the risk-of-bias detail, the full list of 160 studies, the time-trend figures and the additional meta-analyses — was not retrievable. Everything quoted above comes from the main text and Tables 1 and 2.

## 5. Statistics Spotlight

Three things, and the first two are the core machinery of every meta-analysis you will ever read.

### I² is a ratio, not an amount — and that is why 98% is less alarming than it sounds

When you combine studies, their results differ for two reasons. Some of the difference is just luck — each study tested a finite number of patients, so each estimate wobbles around the truth. The rest is real: the studies used different data, different patients, different machines, different definitions.

**I² is the share of the total observed variation that is the second kind.**

> I² = (variation between studies) ÷ (variation between studies + sampling variation)

So I² = 98.2% for segmentation means: of all the spread seen in those 21 Dice coefficients, 98.2% reflects the studies genuinely differing, and only 1.8% is the noise you would expect from finite test sets.

**Here is the part everybody gets wrong.** I² does not measure *how much* the results differ. It measures how much they differ *relative to their own precision*. Make the studies bigger and the sampling variation in the denominator shrinks, so I² goes up — even though nothing about the real disagreement changed.

**Worked intuition.** Suppose ten studies report accuracies between 0.88 and 0.92 — a spread of four points, which for most purposes is nothing. If each tested 50 patients, that spread is well within sampling noise and I² will be near zero. If each tested 50,000 patients, the same four-point spread is enormous relative to each study's precision and I² will be above 95%. **Identical disagreement, opposite verdicts.** This is why I² above 90% is routine in diagnostic and prediction meta-analyses, where test sets are often large, and why it is not on its own a reason to discard the work.

**What to do instead.** Look at the actual spread of the individual estimates on the forest plot, and at the **prediction interval** — the range a new study would be expected to fall in. That is a number in the original units, and it is the one a clinician can use. This paper reports I² extensively and, as far as the text goes, neither the pooled estimates nor prediction intervals.

**Watch out for one more thing this paper demonstrates nicely.** Adding explanatory variables to a meta-regression is supposed to reduce the *residual* heterogeneity. For prediction tasks it did: 99.9% → 98.4% → **76.8%** as target, then training size, resolution, frames and batch size went in. For segmentation it went the other way — 98.2% baseline, **98.8%** after adding architecture, segmented area and training size — and the formal test of moderators returned **p = 0.99**. Residual heterogeneity rising when you add variables is a signal that the variables are noise, and the p-value confirms it. **Moderators that explain nothing can make the number look worse, and that is informative rather than a mistake.**

### Why you cannot just average proportions — and what the double-arcsine does

Most of what this paper pools is a proportion: accuracy, a Dice coefficient, agreement with an expert. Averaging proportions directly is a trap, and the reason is the same boundary problem that broke the confidence intervals in yesterday's paper.

**The variance of a proportion depends on the proportion itself:**

> variance = p(1 − p) / n

Work out p(1 − p) across the range:

- p = 0.50 → 0.2500
- p = 0.80 → 0.1600 (0.64× as large)
- p = 0.90 → 0.0900 (0.36×)
- p = 0.95 → 0.0475 (0.19×)
- p = 0.99 → 0.0099 (**0.04×**)

In a meta-analysis studies are weighted by the inverse of their variance — less wobbly studies count more. So **a study reporting 99% accuracy gets about 25 times the weight of an equally sized study reporting 50%, purely because of where its number sits on the scale.** Not because it was bigger, not because it was better run. The optimistic studies would automatically dominate the pooled answer.

The **double-arcsine, or Freeman–Tukey, transformation** fixes this. You convert each proportion:

> t = arcsin(√(x/(n+1))) + arcsin(√((x+1)/(n+1)))

and the variance of *t* is approximately **1/(n+1)** — which no longer contains *p* at all. Worked at n = 100:

- 50/100: raw variance 0.002500 → transformed variance 0.009901
- 90/100: raw variance 0.000900 → transformed variance 0.009901
- 99/100: raw variance 0.000099 → transformed variance 0.009901

Same weight for all three, set by sample size alone, which is what you wanted. You pool on the transformed scale and convert back at the end.

**Watch out.** The double-arcsine is standard and the authors were right to use it, but it has a known weakness that is actively debated in the methods literature: **back-transforming the pooled value can misbehave when the studies have very different sample sizes**, occasionally producing a summary outside the range of the data. Several methodologists now recommend a logit transformation instead for exactly this reason. This paper's included studies range from small single-centre series to large multicentre cohorts, so the conditions that cause trouble are present. It is not a reason to disbelieve the work; it is a reason to want the pooled numbers printed, so a reader could sanity-check them against the individual studies — which, as Section 4 notes, is not possible from the text.

### Cohen's kappa again, and why the same agreement gives a different answer

Yesterday's paper gave us kappa in a diagnostic setting. This one gives it in a completely different one — two people deciding which abstracts to keep — and the contrast teaches the thing that matters most about the statistic.

The screening check: **103 abstracts, 92.2% agreement, κ = 0.78.** The raw agreement count is 95 of 103.

Now run the formula backwards to see what the chance agreement must have been. Since κ = (p_o − p_e)/(1 − p_e):

> p_e = (p_o − κ)/(1 − κ) = (0.922 − 0.78)/0.22 = **0.645**

So **64.5% of the agreement was free** and only 35.5% had to be earned. If both screeners included roughly the same fraction of abstracts, that chance agreement implies each was including about **23%** of what they read — and in screening, where most things get rejected, that lopsidedness is exactly what inflates chance agreement.

Line the two papers up:

- **Yesterday (PECARN):** 95.4% raw agreement, chance 58.5%, **κ = 0.889**
- **Today (abstract screening):** 92.2% raw agreement, chance 64.5%, **κ = 0.780**

Three points less raw agreement, but nearly eleven points less kappa — because the second task's categories are more lopsided, so more of its agreement was available for free.

**The lesson, which is the single most misused property of kappa: it is not comparable across settings.** A κ of 0.78 in a screening task where 77% of items are rejected is not worse performance than a κ of 0.89 in a task where the split is 72/28. They are measured against different amounts of free agreement. Kappa answers "how much better than guessing, given how often each rater says yes" — and "how often each rater says yes" changes with the job. **Benchmarks like "κ above 0.8 is excellent" are therefore rules of thumb with no theoretical standing**, and should never be used to rank two studies that screened different literatures or diagnosed different conditions.

What κ = 0.78 does tell you here is concrete and useful: on 103 abstracts the two screeners disagreed 8 times, and a reasonable share of their agreeing was not luck. For a 16,248-record screen, that is a reassuring audit — and it is reported, which most reviews do not do.

## 6. Jargon Translator

**Echocardiogram / echo** — an ultrasound scan of the heart, recorded as moving video loops.

**Echocardiographic loop / view** — a short video clip from one camera angle. Standard angles have names: apical four-chamber, apical two-chamber, parasternal long axis. Which view you are looking at determines what you can measure.

**Left ventricular ejection fraction (LVEF)** — the share of blood the main pumping chamber squeezes out with each beat. The single most-used number in cardiology, and the most common target in this review (42 of 59 measurement studies).

**Systematic review** — a search designed to find *all* the studies on a question, with the search strategy and inclusion rules written down so someone else could repeat it.

**Meta-analysis** — the statistical step that combines those studies into one pooled estimate.

**PRISMA** — the reporting standard for systematic reviews, including the flow diagram tracking records from identification to inclusion.

**PROSPERO** — the international register where review protocols are deposited before the work starts, so the question and analysis cannot quietly change after the results are seen. Not mentioned in this paper.

**Random-effects meta-analysis** — pooling that assumes each study estimates a slightly different true value, rather than all estimating one identical truth. The right default when studies differ.

**I²** — the share of observed variation between studies attributable to real differences rather than sampling noise. A ratio, not an amount. See Section 5.

**Heterogeneity** — the studies disagreeing with each other more than chance explains.

**Meta-regression** — using study characteristics (architecture, training size, resolution) to try to explain that disagreement.

**Moderator** — a study characteristic entered into a meta-regression as a candidate explanation.

**Residual heterogeneity** — the disagreement left over after the moderators have done what they can.

**Multilevel meta-analysis** — the version used when one study contributes several results, which would otherwise be counted as independent when they are not.

**Double-arcsine / Freeman–Tukey transformation** — a change of scale that makes a proportion's variance independent of the proportion. See Section 5.

**Inverse-variance pooling** — weighting each study by the reciprocal of its variance, so more precise studies count more.

**Cook's distance** — a measure of how much a single study changes the overall result if you remove it. Values above 1 are conventionally treated as influential.

**Funnel plot** — a scatter of effect size against precision, used to look for publication bias. Asymmetry suggests small negative studies are missing. Hard to interpret for diagnostic studies, as this paper correctly notes.

**Publication bias** — the tendency for studies with impressive results to get published and unimpressive ones not to, which makes any pooled estimate too optimistic.

**Dice coefficient** — the standard score for segmentation: how much the outline the model drew overlaps the outline a human drew. 0 is no overlap, 1 is perfect.

**Segmentation** — automatically tracing the boundary of a structure, here a heart chamber, in every frame.

**Mean absolute error (MAE)** — the average size of the mistake, ignoring direction. For LVEF it is in percentage points.

**External validation** — testing a model on data from a source it was not built on, with no retraining. The strict definition this review uses.

**Held-out / internal validation** — testing on a slice of the same dataset the model was built from. Weaker.

**Cohen's kappa** — agreement between two raters corrected for chance. See Section 5.

**U-Net, ResNet, 3D CNN, ViT, transformer, foundation model** — families of neural network design. U-Net is the standard for segmentation; ResNet and 3D convolutional networks dominate here; transformers and foundation models are the current frontier and were used by only 16 of the 160 studies.

## 7. What You Can (and Can't) Say

**Fair to say:**

- ✅ "A systematic review found 160 studies of fully automated deep learning on echocardiogram video, from 16,248 records screened." Verified; the PRISMA arithmetic reconciles exactly.
- ✅ "Nearly half of this literature — 75 of 161 task entries, 46.6% — has never been tested on data from outside the institution that produced the model." Reported in Table 2, with a strict definition of external.
- ✅ "Results across studies disagreed far more than chance can explain, with I² around 98% for most tasks." Reported throughout.
- ✅ "Even after accounting for architecture, target, training size, video resolution, frames and batch size, more than three-quarters of the variation in prediction studies remained unexplained." 99.9% → 76.8% for accuracy; 98.8% → 82.8% for AUC.
- ✅ "For segmentation, the explanatory variables explained nothing — a formal test returned p = 0.99." Reported.
- ✅ "Only 16 of the 160 studies used transformer or foundation-model architectures." Reported in the Discussion.
- ✅ "Risk-of-bias ratings improved: studies from 2024 onward were less often rated high risk." Reported.
- ✅ "External segmentation performance has declined over the past seven years." Reported, and not explained.
- ✅ "Two screeners double-checked 103 abstracts and agreed 92.2% of the time, kappa 0.78." Reported, and most reviews do not measure this.

**Not fair to say:**

- ❌ "This meta-analysis found that deep learning achieves X% accuracy on echocardiograms." **No pooled estimate appears in the abstract or the results text** — every one is inside a forest plot. There is no number to quote.
- ❌ "Deep learning matches expert echocardiography." Nothing in this review compares models against experts head to head; the comparison is against each study's own ground-truth reference.
- ❌ "The high heterogeneity means the studies are bad." I² is a ratio against each study's own precision. Large test sets make it rise even when real disagreement is modest. See Section 5.
- ❌ "Removing outliers showed the segmentation literature is actually consistent." Five of 21 studies were dropped — 24% — before I² reached 0.00%. That is a sensitivity analysis, not a finding.
- ❌ "Over half of these models have been externally validated, so the field is in good shape." 53.4% have, by a strict definition — but external datasets here are often the same public repositories, which the authors name as a threat to independence and do not quantify.
- ❌ "Newer architectures perform better." Architecture was never a significant moderator for any task, in either direction.
- ❌ "Model performance depends on input resolution and frame count." Those moderators reduced residual heterogeneity when added together, but the paper states that input size and resolution "had no significant influence on model performance when examined in isolation."
- ❌ "This is the full picture of what deep learning can do in echocardiography." Preprints were excluded, and so were commercial systems — which the authors say have undergone more rigorous multicentre validation and whose exclusion probably makes this review **understate** achievable performance.
- ❌ "A meta-analysis is automatically the strongest evidence." It inherits the quality of what it pools. This one found a literature too inconsistent to pool, and says so.

## 8. Bottom Line for Your Life

If you have had an echocardiogram, the practical content here is modest and worth knowing: software that measures your heart's pumping function automatically is real, is already approved in several commercial products, and the evidence suggests it is **more consistent than human readers** — the review notes repeatedly that automated measurements vary less than measurements by different experts, sometimes less than between experienced clinicians. For a number like ejection fraction, where a few percentage points can change a treatment decision, consistency is worth something. These tools are not reading your scan instead of a cardiologist; they are taking the measuring off the cardiologist's hands.

The less comfortable finding is about the research, not the care: **nearly half the published models in this field have never been tried on data from anywhere but the hospital that built them.**

For anyone appraising research, this paper teaches one big thing and hands you two tools.

**The big thing: a meta-analysis is only as poolable as its literature, and the heterogeneity statistic is the honest report of that.** The design sits at the top of the evidence hierarchy, which tempts people to treat any pooled number as settled. This one searched carefully, screened 16,248 records, included 160 studies — and found results so inconsistent that no summary number survives in its own text. **That is a real finding about the field**, and the authors were right not to paper over it. When you see I² near 98% in any review, the pooled estimate underneath it is a description of a mean, not of a thing that exists.

**The first tool: I² is a ratio, not a quantity.** It compares real disagreement against each study's own precision, so bigger studies push it up without anything substantive changing. Before concluding that studies are hopelessly inconsistent, look at the actual spread of the numbers on the forest plot and ask whether a four-point range matters for your purpose. And watch what happens when moderators are added: falling residual heterogeneity means the explanation is working, **rising residual heterogeneity means the explanation is noise** — as this paper's segmentation analysis shows, with the moderator test at p = 0.99 to confirm it.

**The second tool, carried over from yesterday and sharpened: never compare kappas across different tasks.** Yesterday, 95.4% agreement gave κ 0.89. Today, 92.2% agreement gives κ 0.78 — a much bigger drop than the raw figures suggest, because screening rejects most of what it sees and that lopsidedness hands out more free agreement (64.5% here versus 58.5% yesterday). **Kappa is always measured against a baseline that depends on the job**, so "κ above 0.8 is excellent" is folklore, not statistics. Ask what the chance agreement was. If the paper does not say, you can work it out from the two numbers it does give.

---

## Appendix — deferred-paper status, 2026-10-30

- **Google, "The anatomy of a personal health agent"** (Nature, PMID 42907512): no PubMed Central copy. Unchanged.
- **BMJ, LLM-trial reporting completeness review** (PMID 42869550): no PMC copy; Scite paywalled. Unchanged.
- **Annals of Internal Medicine, Choosing Wisely benchmark** (PMID 42896192): no PMC copy. Unchanged. Standing note: its overuse rate of 5.4% with a 95% CI of 0.6–12.2% is a clustering signature — the interval is almost certainly computed across the 15 recommendations rather than the 4,050 responses.
- **JAMA, "Clinician Use of an AI-Enabled Clinical Information Platform"** (PMID 42879271, PMC13673371): PMC record exists and serves an **empty body for the fifteenth consecutive day.** Standing instruction unchanged — **if still empty on 2026-11-05 (day 21), decode abstract-only and say so explicitly.**

---

*This is an educational analysis of a published scientific paper, not medical advice. Nothing here is guidance about heart conditions, echocardiograms or your own care. If you have questions about a heart scan or its results, speak to your cardiologist.*
