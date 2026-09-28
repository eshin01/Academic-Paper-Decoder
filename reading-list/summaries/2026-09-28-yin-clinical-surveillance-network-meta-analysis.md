# Twenty-Eight Trials, Six That Counted, and an Honest Shrug

**Paper:** Clinical Surveillance Technologies in Nonintensive Care Unit Hospital
Settings: Systematic Review and Bayesian Network Meta-Analysis of Randomized
Trials
**Authors:** Yin X, Li X, Huang G, Wang X
**Venue / Year:** Journal of Medical Internet Research, 2026;28:e98205
**DOI:** https://doi.org/10.2196/98205
**PubMed:** https://pubmed.ncbi.nlm.nih.gov/42784726/
**Full text used:** https://pmc.ncbi.nlm.nih.gov/articles/PMC13606342/
**Basis of this analysis:** FULL TEXT (PubMed Central open-access copy,
retrieved 2026-09-28). Figures 1–4 and the three supplementary appendices were
not retrievable; nothing here depends on a figure value.
**Date decoded:** 2026-09-28
**Evidence grade:** 5/5

---

# The Gist

Patients on ordinary hospital wards sometimes start dying slowly, and the signs
show up hours before anything dramatic happens — heart rate creeping up, blood
pressure drifting down, breathing getting faster. If someone notices in time,
you can often intervene. If nobody notices, the patient arrests or ends up in
intensive care.

Hospitals buy technology to catch this. There are three broad kinds. **Rule-based
systems** apply a fixed scoring formula to vital signs and fire an alert when a
threshold is crossed. **Predictive-model systems** — the machine-learning ones,
the ones hospitals are being sold hardest right now — estimate each patient's
individual risk and display or push that number. **Continuous monitoring**
straps a sensor on the patient and streams their vital signs instead of checking
every four hours.

This team gathered every randomized trial of all three and compared them
against each other and against ordinary care. Twenty-eight trials.

The answer is: **we do not know.** Not "they don't work" — genuinely, we do not
know. For death, the odds ratios were 0.91 for rule-based systems, 1.22 for
predictive models, and 0.70 for continuous monitoring, and every single
credible interval was wide enough to contain both "this saves a meaningful
number of lives" and "this kills a meaningful number of people." Same for
intensive care transfers. Confidence in every comparison was rated **very low**.

And here is the number that should stop you. The authors calculated how much
data would be needed to actually answer the mortality question, and compared it
to how much exists. The answer: **11.2%**. For ICU transfers, **5.2%**. After
decades of building and selling these systems, the randomized evidence base
contains about a ninth of the information needed to say whether they help people
die less.

This is the best-conducted paper this reading list has decoded, and it found
nothing. Those two facts are not in tension. That is the lesson.

# Study Snapshot

- **Study type:** Systematic review and **Bayesian network meta-analysis** of
  randomized trials — the design that lets you compare treatments that were never
  tested against each other, by routing through a shared comparator.
- **Registration:** PROSPERO CRD420261356381, registered 6 April 2026. The
  authors state plainly that registration "occurred after the review had
  commenced and after formal searching and screening had begun, but before data
  extraction, risk-of-bias assessment, and data synthesis." Partial protection,
  honestly labelled.
- **Reporting standards:** PRISMA 2020, PRISMA-S, Cochrane Handbook.
- **Search:** PubMed, Embase, Cochrane CENTRAL, Web of Science, from inception to
  28 February 2026, **no language restrictions**, plus supplementary registry
  surveillance and citation tracking through 22 July 2026.
- **Eligible designs:** Individually randomized, cluster-randomized, crossover,
  and stepped-wedge trials. Observational and model-development studies excluded
  — which is the point, since most of this literature is retrospective.
- **Settings:** Emergency departments, admission units, general wards,
  postoperative wards, stroke units, step-down units. Pure ICU studies excluded.
- **The four things compared:** rule-based electronic surveillance (RB-ES),
  predictive model–based electronic surveillance (PM-ES), continuous physiologic
  monitoring (CPM), and local standard care.
- **How interventions were sorted:** By "the principal randomized difference
  between study groups, rather than commercial terminology" — what actually
  differed between arms, not what the vendor calls it.
- **Primary outcomes:** All-cause in-hospital or 30-day mortality; unplanned or
  emergent transfer to intensive care.
- **The evidence funnel:** 1645 records found, plus 14 from citation tracking →
  1063 screened → 109 full texts → **28 independent trials included** → 23
  contributed to any analysis → 9 met strict criteria → 7 entered a primary
  network → **6 trials in each primary network**.
- **How many patients:** 13,716 analyzed observations for mortality; 13,441 for
  ICU transfer. The authors deliberately refuse to state one overall participant
  total, because trials counted participants, admissions, encounters and visits
  differently.
- **Statistical machinery:** Contrast-based Bayesian random-effects models in
  JAGS via the gemtc package; four Markov chains, 20,000 adaptation and 100,000
  sampling iterations each; half-normal prior with scale 0.5 on heterogeneity,
  re-run at 0.2 and 1.0. Convergence: maximum R-hat 1.003, minimum effective
  sample size above 7200.
- **Risk of bias:** RoB 2. Among the 9 strict trials — **1 low risk, 5 some
  concerns, 3 high risk.**
- **Certainty:** CINeMA. **Very low for every primary network comparison.**
- **Prespecified "no important difference" zone:** odds ratio 0.80 to 1.25.
- **Funding:** **Not reported** in the text retrieved.
- **Conflicts of interest:** **No statement appears** in the text retrieved.

# How Strong Is This Evidence? — Grade 5/5

This is the second 5/5 in this reading list, and the first for a paper that
found nothing. That is deliberate, and it is worth being explicit about why.

The grade in these summaries is for **how trustworthy the work is**, not for how
exciting the result is. A study that runs a clean design, reports what it found,
and refuses to dress it up is more useful to you than a study that finds
something and hides how it got there. By that standard this paper is close to
exemplary, and the specifics are worth listing because they are a checklist you
can apply elsewhere:

- **It refused to rank the treatments.** Network meta-analyses almost always
  publish a league table and a "SUCRA" ranking, because rankings get cited.
  These authors explicitly declined: rankings "were not used as principal
  results because the strict networks were sparse, active strategies had not
  been compared directly, and rankings could imply an unsupported clinical
  hierarchy." Turning down the most quotable output of your own method is rare.
- **It classified interventions by what actually differed between arms**, not by
  what the product is called. Two systems with the same algorithm but different
  alert pathways are different interventions; two with different algorithms and
  the same workflow may not be.
- **It reported that a positive finding disappeared under better methods.** In
  the discussion: "After publications were linked to independent trials,
  procedural and treatment-guidance technologies were excluded, adjusted
  cluster-trial estimates were prioritized, and the intervention nodes were
  defined according to their principal randomized function, the apparent
  rule-based advantage was no longer present." An earlier version of this
  analysis showed rule-based systems working. Better classification erased it,
  and they said so in print.
- **It retracted its own unsupported methods claim.** "The unsupported statement
  in the original paper that κ had been assessed was therefore removed." Most
  authors would have quietly left it in.
- **It said what it could not test, instead of implying absence.** With a
  star-shaped network there is no way to check whether direct and indirect
  evidence agree. The paper: this "was reported as an inability to assess
  incoherence rather than as evidence that incoherence was absent."
- **It refused to compute a tidy total sample size** because the trials counted
  different things, and reported outcome-specific denominators instead.
- **It declined underpowered statistical tests** rather than running them for
  the appearance of rigour: with fewer than 10 trials per network, no funnel
  asymmetry test, no trim-and-fill. "Publication bias could neither be confirmed
  nor excluded."
- **It kept clean and messy analyses apart** and labelled the messy ones
  exploratory — including the one analysis that produced a statistically
  significant result.
- **It separated adjusted from unadjusted estimates**, did not treat hazard
  ratios as odds ratios, and did not force differently anchored continuous
  outcomes into one scale.

**What it cannot do.** The evidence base is tiny and mostly biased, so this
review cannot tell you which system to buy, or whether any of them helps. The
authors are unambiguous that this is not evidence of ineffectiveness: the data
are "insufficiently precise to confirm or exclude meaningful clinical effects."

**The legitimate criticisms of the review itself** are small: PROSPERO
registration happened after screening began (disclosed); there is no funding or
conflict-of-interest statement in the retrieved text; and the abstract mentions
the one significant exploratory result in a way a hurried reader could
misinterpret.

# The Editor's Concerns

Most of what follows is a criticism of **the field**, not of this paper — the
authors identified nearly all of it themselves. That is what a good review does:
it tells you how thin the ground is.

**Twenty-eight trials became six.** The abstract's "28 independent trials"
sounds like a substantial evidence base. Follow it through: 23 contributed to
any analysis, 9 met the strict criteria, 7 reached a primary network, and **each
primary network rests on 6 trials** spread across three technology classes plus
standard care. That is roughly two trials per comparison. The headline count and
the working count differ by a factor of nearly five.

**The evidence base is at 11% of what it needs.** The trial sequential analysis
is the most quotable finding in the paper and gets three sentences. For
mortality, the accumulated 927 participants represent **11.2%** of the required
information size of 8262 — *deriving* from those numbers, about **nine times**
more data is needed. For ICU transfer, 1177 participants against a required
22,597 is **5.2%** — roughly **nineteen times** more. Nobody should be surprised
these trials are inconclusive. They are collectively a pilot study.

**Only one of nine trials was at low risk of bias.** Five raised some concerns
and three were high risk. The specific failures matter: in the CoMET trial,
"clinicians preferentially transferred patients perceived to be sicker to
display-on beds, and bed movement resulted in censoring" — so the sickest
patients were selected into the monitored group, which biases against the
technology and then loses them from the analysis. The VIGILANCE and TRaCINg
pilots had "substantial intervention nonadherence, monitoring discontinuation,
or crossover," meaning many patients in the monitoring arm were not actually
monitored.

**Every comparison between the three technologies is imaginary.** "No head-to-head
randomized trial has directly compared RB-ES, PM-ES, and CPM." Every
active-versus-active number in this paper is reconstructed by routing through
standard care. And because the network has no closed loop, there is no way to
check whether that reconstruction is sound. See the Statistics Spotlight.

**Every primary interval contains both meaningful benefit and meaningful harm.**
The authors prespecified odds ratios between 0.80 and 1.25 as "no clinically
important difference." *Deriving* from the six primary estimates: all six
credible intervals extend below 0.80 **and** above 1.25. So this is not "no
effect found." It is "compatible with saving a lot of lives, doing nothing, and
costing a lot of lives, simultaneously." That is a far more honest description
of ignorance than "not statistically significant."

**The only result that excludes no-effect is the messiest analysis in the
paper.** Core continuous-monitoring length of stay across 3 trials: ratio of
means 0.91 (95% CI 0.76–1.09) — nothing. Expand to 7 trials and it becomes 0.86
(95% CI 0.74–0.99) — a "significant" 14% reduction. But that expanded set adds
passive monitoring, a multicomponent decision-support intervention, a cluster
trial without cluster-adjusted estimates, and a stroke-specific unit, with
heterogeneity of 69.4%. The authors call it "hypothesis-generating rather than
confirmatory," which is correct. It is also exactly the number a vendor would
put on a slide.

**Intensive care transfer is a two-faced outcome, and the paper is right to
worry.** Fewer ICU transfers could mean deterioration was prevented — or that
patients who needed escalation did not get it. More transfers could mean more
deterioration — or better, earlier recognition. The paper cites the CONCERN
trial, where "a greater number of unanticipated ICU transfers occurred alongside
a lower adjusted instantaneous risk of death." The same direction of movement in
the same number meant good news. Any analysis treating ICU transfer as purely
undesirable is mismeasuring.

**Predictive accuracy and clinical benefit are different things, and this is the
cleanest demonstration yet.** The paper's own framing: "A model can identify
high-risk patients accurately but fail to improve outcomes when it does not
alter clinical decisions, responsibility for action is unclear, or the
information arrives after clinicians have already recognized the problem."
Predictive-model surveillance had the *worst* mortality point estimate of the
three (odds ratio 1.22, favouring standard care, though with a credible interval
from 0.61 to 2.31 that settles nothing). The machine-learning systems, which
dominate retrospective AUC papers, have the least encouraging randomized signal.

**The unit of analysis is inconsistent across trials.** Participants,
admissions, hospital encounters, and inpatient visits were all used. "13,716
analyzed observations" is not 13,716 people. The authors refuse to imply
otherwise, and explicitly ask future trials to report this properly.

**Several inputs were reconstructed.** Some adjusted risk ratios were converted
to odds ratios using reported control-group risks; some continuous outcomes were
estimated from medians and interquartile ranges; one trial's event counts were
rebuilt from rounded percentages. Each was confined to sensitivity analyses,
which is the right handling, but it is uncertainty no interval captures.

**The heterogeneity estimate is itself barely estimated.** Posterior median
between-study heterogeneity of 0.275 with a credible interval of 0.016 to 0.859
for mortality. With six trials you cannot pin down how much the trials disagree,
which means the prior you chose is doing real work — hence the re-runs at 0.2
and 1.0.

# Statistics Spotlight

## Concept 1 — Network meta-analysis: comparing things nobody compared

The central problem this paper faces: hospitals want to know whether continuous
monitoring beats a predictive model. **No trial has ever tested that.** Network
meta-analysis is the machinery for answering anyway, and understanding both what
it can and cannot do is worth your time.

**The basic move.** Suppose trials compared A against standard care and found A
better by 10 points. Other trials compared B against standard care and found B
better by 4 points. Nobody compared A with B. Network meta-analysis says: if
those two sets of trials were run in comparable patients, then A should beat B
by about 10 − 4 = 6 points. That difference is an **indirect comparison**.

**An everyday version.** You want to know who is taller, your cousin in Tokyo or
your colleague in Lisbon. You cannot stand them side by side. But you know your
cousin is 8 cm taller than you and your colleague is 3 cm shorter than you. So
your cousin is about 11 cm taller. This works — *provided* you were the same
height on both occasions. If you measured yourself as a teenager in Tokyo and as
an adult in Lisbon, the chain breaks.

**That proviso has a name: transitivity.** For indirect comparison to be valid,
the shared comparator has to mean the same thing in every trial. Here the shared
comparator is "local standard care" — and standard care in a Danish postoperative
ward is not standard care in a mixed acute unit that already runs an early
warning score. The authors assessed transitivity explicitly by comparing
settings, baseline risk, target conditions, alert presentation, and response
pathways, and concluded that "relevant effect modifiers remained unevenly
distributed across nodes." That is a polite way of saying: this chain may not
hold.

**Now the structural problem, and it is the key point.** Look at the shape of
the evidence. Every trial compared *something against standard care*. Nothing
was compared against anything else. Drawn as a diagram, standard care sits in
the middle with three spokes coming off it and no connections between the spokes.
That is a **star-shaped network**.

Why this matters: normally network meta-analysis has a safety check. If some
trials compared A with B *directly*, and you can also compute A versus B
*indirectly* through standard care, you compare the two answers. If they
disagree, something is wrong — that disagreement is called **incoherence** (or
inconsistency), and it is the main way you catch a broken transitivity
assumption. A star network has no closed loops, so there is no direct comparison
to check the indirect one against. **The safety check cannot be run at all.**

This paper's handling is a model of how to say so. The authors write that this
"was reported as an inability to assess incoherence rather than as evidence that
incoherence was absent." Read that twice. The difference between "we checked and
found no problem" and "we could not check" is the difference between reassurance
and silence, and an enormous amount of published research blurs it.

**A second consequence, easy to miss.** In a star network, an indirect A-versus-B
estimate inherits *all* the uncertainty from both direct comparisons. The paper
quantifies this: "For each active-vs-active comparison, half of the contribution
arose from each of the 2 direct comparisons." You are subtracting two noisy
numbers, and the noise adds. That is why comparisons like continuous monitoring
versus rule-based systems for mortality come out as 0.77 with a credible
interval from 0.24 to 2.36 — a tenfold range.

**Watch out for:** league tables and rankings from network meta-analyses,
especially the "SUCRA" percentage you sometimes see ("treatment X has a 78%
probability of being best"). Rankings are computed even when every comparison is
worthless, and a treatment can rank first on almost no evidence — being ranked
best among four options where all intervals overlap tells you nothing. The
authors of this paper refused to publish rankings for exactly this reason. When
you see a ranking, ask: *was this network star-shaped, and how many trials are
behind the winner?*

## Concept 2 — Credible intervals: what Bayesian statistics actually buys you

Every interval in this paper is a **95% credible interval**, not a confidence
interval. The distinction is usually presented as philosophy. It has one
practical consequence worth knowing.

**What a confidence interval does not mean.** A 95% confidence interval of 0.36
to 1.29 does *not* mean "there is a 95% probability the true odds ratio is
between 0.36 and 1.29." It means: if you repeated this study endlessly, 95% of
the intervals you constructed this way would contain the true value. The
probability statement is about the *procedure*, not about *this* interval.
Almost everyone reads it the wrong way, including many researchers.

**What a credible interval does mean.** Exactly the thing everyone wants. Given
the data and the assumptions, there is a 95% probability the true value lies in
that range. So when this paper reports continuous monitoring at an odds ratio of
0.70 with a credible interval of 0.36 to 1.29, you may legitimately say: *given
this evidence, the true effect is 95% likely to be somewhere between a 64%
reduction in the odds of death and a 29% increase.* You can read it the natural
way because it was built to be read the natural way.

**The catch: you have to bring a prior.** Bayesian analysis requires stating
what you believed before seeing the data. Here the important one is the prior on
**heterogeneity** — how much the authors expected trials to genuinely differ.
They used a half-normal distribution with scale 0.5, and re-ran everything at
0.2 and 1.0 to check it mattered little.

**Why that prior is doing real work here.** With only six trials you cannot
estimate how much trials disagree — the paper's own heterogeneity estimate is a
posterior median of 0.275 with a credible interval from 0.016 to 0.859, which
spans "essentially identical" to "wildly different." When the data cannot pin
something down, the prior fills the gap. Re-running under different priors, as
these authors did, is how you show your conclusion is not an artefact of your
assumptions.

**An everyday version.** A friend says a new café is good. If you have no prior
information, their word is most of what you have. If you have been to fifty
cafés on that street and they were all mediocre, one enthusiastic review moves
you a little. Bayesian analysis makes that starting position explicit and
arithmetical instead of leaving it in your head. The honest version states the
prior and shows what happens if you had started somewhere else.

**"Posterior median"** is just the middle of the resulting probability
distribution — the single best summary of what you now believe.

**Watch out for:** credible intervals reported without the prior, and — the
reverse error — treating "Bayesian" as a synonym for "more rigorous." A Bayesian
analysis with a strong prior and thin data can manufacture confidence out of
assumptions. The tell of a trustworthy one is prior sensitivity analysis, which
this paper ran and reported.

## Concept 3 — Trial sequential analysis: have we even collected enough data to ask?

This is the concept that reframes the whole paper, and it is buried.

**The problem it solves.** When a meta-analysis comes back inconclusive, there
are two very different explanations. Either the treatment genuinely does not
work, or nobody has collected enough data yet. These look identical in a forest
plot, and they have opposite implications: one says stop, the other says the
question is still open and needs a proper trial.

**How it works.** Trial sequential analysis borrows a technique from interim
monitoring of single trials. Before running a trial you calculate a sample size
— how many patients you need to detect an effect of a given size with
acceptable error rates. Trial sequential analysis does the same for an entire
literature: it computes a **required information size**, the total number of
participants across all trials needed to settle the question, then asks how much
of that total has actually accumulated.

**What this paper found.** For mortality, the required information size was
**8262 participants**. The accumulated evidence was **927** — *deriving* from
those figures, **11.2%**, meaning roughly **nine times** more data is needed. For
ICU transfer, required 22,597, accumulated 1177 — **5.2%**, about **nineteen
times** short.

Sit with that. These technologies have been developed, marketed, procured and
installed in hospitals worldwide. The randomized evidence on whether they reduce
death has covered about a ninth of the ground needed to find out.

**Why this changes the reading.** Without it, "no significant difference across
28 trials" sounds like a verdict — these things don't work. With it, the correct
reading is: *the question has barely been asked.* The paper is careful about
this, insisting the results "should not be interpreted as evidence that any
surveillance class is ineffective."

**The second thing it adds: adjusted boundaries.** Because a growing
meta-analysis gets re-run every time a trial is published, it is repeatedly
testing the same hypothesis — the multiple-comparisons problem stretched across
years. Trial sequential analysis applies **alpha-spending boundaries**
(Lan-DeMets O'Brien-Fleming here) that demand stronger evidence early, when
little data has accumulated, and relax toward the usual threshold as the
required information size is approached. It protects against an early lucky
result being crowned.

**An everyday version.** You are trying to work out whether a coin is biased.
After 8 flips you have 5 heads. Is the coin fair? The honest answer is not "yes"
or "no" — it is *8 flips cannot tell you.* You would need hundreds. Reporting "no
significant deviation from fairness after 8 flips" is technically true and
deeply misleading. This literature has done the equivalent of 8 flips and the
paper says so out loud.

**Watch out for:** "no significant difference" presented as a conclusion when it
is really a description of insufficient data. The question to ask of any null
meta-analysis is *how much data would it take, and how much do we have?* If the
paper does not say, the null may be meaningless. And the reverse caution, which
these authors also observe: trial sequential analysis estimates information
size, and they explicitly note it "was not used as a substitute for
certainty-of-evidence assessment" — a large enough sample of biased trials still
gives you a confident wrong answer.

# Jargon Translator

- **Clinical deterioration:** A ward patient getting sicker in a way that leads
  to cardiac arrest, ICU transfer, or death if not caught.
- **Early warning score:** A scoring formula applied to vital signs; cross the
  threshold and an alert fires. The oldest of the three approaches.
- **Rapid response team / Code Blue:** The team called when a patient is
  deteriorating or has arrested. The paper deliberately does not treat a *call*
  as equivalent to a confirmed arrest — calls measure behaviour, arrests measure
  the patient.
- **Stepped-wedge trial:** Every site eventually gets the intervention, but the
  order of switchover is randomized. Common when withholding something from a
  whole hospital is impractical.
- **Cluster-randomized trial:** Whole wards or hospitals are randomized, not
  individual patients. Requires statistical adjustment, since patients in one
  ward resemble each other.
- **Odds ratio:** How the odds of an outcome change. Below 1 favours the
  intervention. It exaggerates when outcomes are common, which is why the
  prespecified "no important difference" zone of 0.80 to 1.25 matters.
- **Ratio of means:** For continuous outcomes like length of stay — 0.91 means
  9% shorter. Used here instead of standardized mean difference, which would
  have mixed differently anchored measurements.
- **Transitivity:** The assumption that the shared comparator means the same
  thing across all trials. Indirect comparison collapses without it.
- **Incoherence / inconsistency:** Disagreement between direct and indirect
  estimates of the same comparison. Untestable in a star network.
- **Star-shaped network:** Every treatment compared only with a common
  comparator, never with each other. No loops, no safety check.
- **Contribution matrix:** A breakdown of which trials drove which conclusion.
  Here it revealed that every active-versus-active comparison was 100% indirect.
- **RoB 2:** The current Cochrane tool for judging bias in randomized trials.
- **CINeMA:** The framework for rating confidence in network meta-analysis
  estimates across six domains. Verdict here: very low, everywhere.
- **JAGS / Markov chain Monte Carlo / R-hat / effective sample size:** The
  simulation engine for Bayesian models and its convergence checks. R-hat near
  1.00 and large effective sample sizes mean the simulation ran properly — a
  statement about the *computation*, not about whether the answer is right.
- **Half-normal prior:** The starting assumption about how much trials differ.
  Scale 0.5 here; re-run at 0.2 and 1.0.
- **Alpha-spending boundary:** A stricter evidence threshold applied when data
  are still accumulating, to stop early flukes being mistaken for answers.
- **Continuity correction:** Adding a small constant when a trial has zero
  events, so ratios can be computed at all.
- **Effectiveness-implementation hybrid design:** A trial that measures both
  whether something works and how it gets used — which this paper argues is what
  the field actually needs.

# What You Can (and Can't) Say

**Fair to say:**

- A Bayesian network meta-analysis of 28 randomized trials found no clear
  evidence that rule-based alerts, predictive-model alerts, or continuous
  monitoring reduce death or unplanned ICU transfer on ordinary hospital wards.
- For mortality the odds ratios versus standard care were 0.91 (95% CrI
  0.35–2.30) for rule-based, 1.22 (0.61–2.31) for predictive-model, and 0.70
  (0.36–1.29) for continuous monitoring. Every interval includes both important
  benefit and important harm.
- Continuous monitoring had directionally favourable point estimates for both
  primary outcomes, but nothing approaching statistical or clinical certainty.
- **No randomized trial has ever directly compared the three approaches.** Every
  comparison between them in this paper is indirect, and the network's shape
  makes that indirectness impossible to verify.
- Confidence in every primary comparison was rated **very low**.
- The accumulated randomized evidence represents about **11%** of what is needed
  to settle the mortality question and about **5%** for ICU transfer.
- Only 1 of the 9 core trials was at low risk of bias.
- The authors' conclusion: algorithm class "is an inadequate basis for selecting
  a surveillance strategy," and what matters is the whole pathway — data
  quality, alert presentation, who is accountable for responding, staffing, and
  escalation protocols.

**Not fair to say:**

- ~~"Hospital early warning systems don't work."~~ The paper explicitly rejects
  this reading. It is not a null result; it is an absence of adequate evidence.
- ~~"AI-based deterioration prediction is no better than simple rules."~~ That
  comparison was never made directly by anyone, and the indirect estimate
  (1.34, 95% CrI 0.41–4.11 for mortality) is compatible with almost anything.
- ~~"Continuous monitoring reduces length of stay by 14%."~~ That came from the
  expanded exploratory analysis mixing four kinds of intervention with 69.4%
  heterogeneity. The clean analysis showed 0.91 (95% CI 0.76–1.09).
- ~~"Continuous monitoring is the best of the three."~~ It had the most
  favourable point estimates and the authors specifically refused to rank, since
  the intervals overlap almost completely.
- ~~"The evidence shows these systems are safe."~~ The intervals extend well into
  harm. Safety has not been established either way.
- ~~"28 randomized trials is a solid evidence base."~~ Six trials supported each
  primary question.

# Bottom Line for Your Life

**The most useful thing here is a distinction most people never make: "no
evidence of benefit" and "evidence of no benefit" are completely different
statements.** This paper is the first; it is constantly quoted as though it were
the second. The tool for telling them apart is the one in the Statistics
Spotlight — ask how much data would be needed and how much exists. At 11% of the
required information size, "we found nothing" means "we looked through a
keyhole." At 150%, it would mean something quite different. That single question
separates a settled negative from an unasked question, and almost no press
release distinguishes them.

**The second takeaway is about what these systems actually are.** The paper's
best insight is that a deterioration alert is not a diagnostic test — it is a
chain: measure the patient, compute a risk, get that risk to the right person,
have that person believe it, and have someone act. An algorithm with a
spectacular AUC that fires into a pager nobody answers accomplishes nothing.
That is why the same algorithm can help in one hospital and not another, and why
buying the cleverest model is not the same as buying a better outcome. It also
explains the single most counterintuitive number in the paper: the
machine-learning systems, which dominate the retrospective accuracy literature,
had the *least* encouraging randomized mortality estimate of the three.

**And notice what a 5/5 paper that found nothing looks like.** These authors
declined to publish a ranking their own method would have generated. They
reported that an earlier positive finding vanished when they classified the
interventions more carefully. They deleted a claim from their own methods
section that they could not support. They said "we could not test this" where a
lesser paper would have said "we found no evidence of a problem." None of that
makes the result more exciting — it makes the result *believable*, which is the
only property that matters when you are deciding what to do. When you are
judging research, grade the conduct, not the conclusion. A confident answer from
sloppy work is worth less than an honest shrug from careful work.

---

*Education, not medical advice. Decoded 2026-09-28 from the PubMed Central
open-access full text. Derived calculations — the evidence funnel, the trial
sequential analysis shortfall multiples, the low-risk-of-bias share, and the
check that all six primary credible intervals span the prespecified
important-benefit and important-harm thresholds — are labelled as derived and
were computed from the paper's own reported values.*
