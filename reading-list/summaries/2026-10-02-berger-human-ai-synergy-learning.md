# Maybe the Problem Was That We Never Let Anyone Practise

**Paper:** Human learning is an understudied but promising lever for boosting
human–AI synergy
**Authors:** Berger J, Burton JW, Hertwig R, Kosch T, Kurvers RHJM,
Kurzenberger B, Lazik C, Onnasch L, Rieger T, Thoma AI, Wulff DU, Herzog SM
**Venue / Year:** Proceedings of the National Academy of Sciences,
2026;123(39):e2536100123
**DOI:** https://doi.org/10.1073/pnas.2536100123
**PubMed:** https://pubmed.ncbi.nlm.nih.gov/42766752/
**Full text used:** https://pmc.ncbi.nlm.nih.gov/articles/PMC13624608/
**Basis of this analysis:** FULL TEXT (PubMed Central open-access copy,
retrieved 2026-10-02).

**An unusual and important retrieval limitation, stated up front:** the PubMed
Central rendering of this paper has **dropped the Hedges' *g* point estimates
and every Bayes factor** from the inline text — they survive only in Figure 1D,
which was not retrievable, and in the supplementary appendix. What I can verify
and quote are the study counts, the effect-size counts, the upper bounds of
several credible intervals, and the posterior probabilities of direction. So
this summary reports the **direction and the evidence base** of every finding
but, for most results, **not the magnitude**. Where a number is missing I say so
rather than guessing. Nothing below is inferred from a figure.

**Date decoded:** 2026-10-02
**Evidence grade:** 4/5

---

# The Gist

Last year a large review asked a simple question: when a person works *with* an
AI, do they do better than the best of the two working alone? It pooled 74
studies across tasks like classifying images, predicting house prices and
writing code. The answer was no. On average, human–AI teams performed **worse**
than whichever of the two was better by itself. That finding travelled widely,
and it is gloomy: it says the combination subtracts rather than adds.

This paper, by a group at the Max Planck Institute for Human Development and
collaborators, went back to all 74 studies and asked a different question —
**not whether people are bad at working with AI, but whether anyone ever gave
them a chance to get good at it.**

What they found about the experiments themselves is the most solid part of the
paper. The typical study put a person in a single session, gave them **no
practice trials**, a **median of 30 tasks**, and — critically — **never told
them whether they had been right.** Only **10 of the 74 studies** gave
participants outcome feedback at all. **None** of the 74 deliberately compared
feedback against no feedback.

Then they reanalysed. Studies that did give feedback leaned toward positive
synergy; studies without it leaned negative. And the sharpest pattern was in the
combination: when people got **both** an explanation of the AI's reasoning
**and** feedback on whether they had been right, synergy tended to be positive.
When they got explanations **without** feedback, synergy was clearly negative.

That last contrast is the paper's real contribution, and it reframes a whole
industry's assumption. Explainable AI is widely sold as the fix for
over-reliance. This analysis suggests explanations only help **when you can
check whether they were any good** — and that showing someone an explanation
they have no way to verify may be worse than showing them nothing.

The honest caveat, which the authors state repeatedly: this is correlational,
nobody randomised feedback, and the headline cell rests on **24 effect sizes**.

# Study Snapshot

- **Study type:** A **reanalysis** of someone else's meta-analysis — a
  re-examination of the same 74 studies with new variables coded in. Not new
  experiments. It sits in an unusual place on the evidence ladder: stronger than
  an opinion piece because it is quantitative and exhaustive, weaker than a
  meta-analysis because the key variable was never randomised in any underlying
  study.
- **What was reanalysed:** All **74 studies** from Vaccaro et al.'s systematic
  review and meta-analysis of human, AI, and human–AI performance, comprising
  **370 experimental conditions** (reported as 370 effect sizes).
- **The tasks in those studies:** Wide-ranging — classifying images, predicting
  house prices, writing code, and others.
- **The original finding being revisited:** On average, human–AI combinations
  performed **worse** than the better of human or AI alone. Positive synergy
  emerged only where humans beat the AI alone; where AI beat humans, synergy was
  negative. Neither AI confidence displays nor AI explanations explained the
  variation.
- **What this paper added:** Coding of design features that help or hinder
  learning — chiefly whether participants received **outcome feedback** (being
  told the correct answer after each case), plus practice trials and session
  structure.
- **How the coding was done:** Effect sizes and the AI-explanations variable
  came from the original authors' **open data**. The new features were coded by
  **two of six authors independently for every study**, with disagreements
  arbitrated by the first author. **No inter-rater reliability statistic is
  reported** for this new coding.
- **What the literature looked like:** The typical study was a **single session,
  no practice trials, a median of 30 task trials, and no outcome feedback.**
- **How rare feedback was:** **10 of 74 studies (13.5%)** had any condition with
  outcome feedback, contributing **98 of 370 effect sizes (26.5%)**. Of those 10,
  only **3** examined how people's use of AI changed across trials. **None**
  experimentally varied whether feedback was given.
- **Independent corroboration cited:** A separate survey by Lai et al. of 124
  human–AI decision-making studies found only **6 (4.8%)** offered outcome
  feedback.
- **The outcome measure:** **Hedges' *g*** for the standardized difference
  between the human–AI combination and **whichever of human or AI performed
  better alone**. Positive means the team beat the best solo performer; negative
  means it did not.
- **The statistics:** **Robust Bayesian model-averaged meta-regression (RoBMA
  version 3.5)**, reporting credible intervals, Bayes factors, and posterior
  probabilities of direction.
- **Main comparison:** 98 effect sizes with feedback against 272 without.
  Without feedback, synergy tended negative, with a 95% credible interval whose
  **upper bound was 0.00**. With feedback it tended positive, upper bound
  **0.34**. **Neither estimate was credibly different from zero.** The contrast
  between them had an upper bound of **0.69** and a **posterior probability of
  being positive of 84%**.
- **The headline interaction:** Among studies with AI explanations, those with
  feedback (**24 effect sizes, 14%**) tended toward positive synergy, upper
  bound **0.48**; those without feedback (**148 effect sizes**) were "clearly
  negative" — *both bounds of that interval were stripped from the retrieved
  text*. The feedback contrast among explanation studies ran from **0 to 0.94**
  with a **posterior probability of direction of 97%**. Without explanations,
  feedback did not moderate synergy.
- **Confounding check:** **12 further meta-regressions**, each adding one of
  Vaccaro et al.'s original moderators alongside feedback. "The effect directions
  remained consistent across all 12 models."
- **Within-study check:** Trial-level data was available for only **3 studies**.
  In those, participants "learned to align with better-performing AI over trials
  when informative signals were available, but not otherwise."
- **Point estimates and Bayes factors:** **Not retrievable** from the PMC
  rendering (see the note in the header).
- **Funding and conflicts of interest:** **Not reported** in the text retrieved.

# How Strong Is This Evidence? — Grade 4/5

**What this paper did well:**

- **It reanalysed every one of the 74 studies**, not a convenient subset, and
  built on the original authors' open data rather than re-deriving effect sizes
  and risking disagreement about them.
- **It double-coded the new variable.** Two of six authors independently read
  every study.
- **It tested the contrast directly.** This matters more than it sounds. Having
  found that feedback studies leaned positive and non-feedback studies leaned
  negative — and that **neither was individually credibly different from zero**
  — the obvious temptation is to say "feedback works and no-feedback doesn't."
  That is the difference-in-significance fallacy, and this reading list met a
  paper that fell straight into it a week ago. These authors instead computed the
  **difference between the two estimates** and reported the uncertainty on that
  difference. That is the correct move.
- **It checked for confounding by brute force**, running 12 further models each
  adding one of the original review's moderators, and reporting that directions
  held across all of them.
- **It labelled its own evidence correctly throughout** — "tentative evidence,"
  "our results are correlational," "experiments directly varying learning
  opportunities are needed for stronger, causal conclusions."
- **It stated that neither estimate was credibly different from zero**, in the
  body text, rather than burying it.
- **It argued its own estimate might be conservative, and said why** — because
  most studies report only average performance across all trials, which blends
  the early trials when a person has not yet learned anything with the later
  ones when they have.
- **It found independent corroboration** in a separate survey of 124 studies
  where only 5% provided feedback.
- **It made three concrete, checkable recommendations** rather than a vague call
  for more research: report standardized performance metrics even when they are
  not your primary outcome; share participant- and trial-level data; and widen
  search terms to include human factors and judgment-and-decision-making
  literature from before 2018.

**Why it is a 4 and not a 5:**

- **The headline cell is 24 effect sizes.** The novel claim — explanations plus
  feedback produce positive synergy — rests on 24 of 370 effect sizes,
  *deriving*, **6.5% of the total evidence base.**
- **Nobody randomised feedback.** Not in one of the 74 studies. So "studies with
  feedback" is a group of 10 studies that differ from the other 64 in every
  other respect too.
- **No inter-rater reliability is reported** for the coding the entire paper
  depends on.
- **A posterior probability of direction of 84% is weak**, and it is the figure
  behind the paper's broadest claim.
- **The central argument is partly unfalsifiable as stated.** "The pessimistic
  view of human–AI synergy may thus reflect sampling from a learning-handicapping
  part of the design space" is a claim about experiments nobody has run. It may
  well be right. It cannot be checked from these data.

# The Editor's Concerns

Nearly every concern here is one the authors raise themselves. The arithmetic is
mine.

**The finding everyone will quote rests on 24 effect sizes.** The novel,
interesting, genuinely surprising claim is the interaction: explanations help
only when paired with feedback. *Deriving* from the paper's counts, the
"explanations and feedback" cell contains **24 of 370 effect sizes — 6.5% of the
evidence base**, and 14% of the conditions that had explanations at all. Against
it sit 148 effect sizes with explanations and no feedback. A 24-versus-148
comparison inside a reanalysis of other people's experiments is a hypothesis,
not a result, and the authors say as much.

**Feedback was never randomised, so this is an observational study wearing a
meta-analysis costume.** The paper is explicit: "None of the studies
experimentally varied whether outcome feedback was provided or not." That means
the 10 feedback studies are not a treatment arm. They are 10 research groups who
chose to give feedback — and who may also have chosen longer sessions, better
paid participants, easier tasks, different populations, or more careful task
design. Their 12-model confounding check is the right instinct and it tests one
moderator at a time against a list someone else drew up. It cannot rule out the
thing it most needs to rule out: that giving feedback is a marker of a more
carefully run experiment.

**Neither of the two main estimates was credibly different from zero.** The
without-feedback estimate had a credible interval reaching up to exactly
**0.00**; the with-feedback estimate up to **0.34**. The paper says plainly:
"While neither estimate was credibly different from zero, there was tentative
evidence that synergy was higher in studies with than without feedback." The
contrast is the finding, and its posterior probability of running positive is
**84%** — *deriving*, that leaves roughly a **16% chance it runs the other way.**
In Bayesian reporting conventions, 84% is routinely described as "weak" or
"anecdotal" evidence.

**The stronger number applies to the smaller slice.** The 97% posterior
probability — much more persuasive — belongs to the feedback contrast *among
studies with explanations*, which is the 24-versus-148 comparison. So the paper's
most convincing statistic sits on its thinnest data. That is not a contradiction,
it is how interaction effects usually behave, and it is exactly why interactions
need replication before they are believed.

**No inter-rater reliability for the coding the paper is built on.** The effect
sizes came from the original authors' open data, which is good practice. But
*whether a study provided outcome feedback* was coded fresh by the authors, "by
two of six authors" with disagreements "arbitrated by J.B." Nowhere is a kappa,
an alpha, or a raw agreement rate reported. The entire paper hinges on that
binary variable, and a reader cannot tell how cleanly it could be applied.
Studies describe their procedures with varying clarity, and "did participants
learn the right answer after each trial?" is often genuinely ambiguous.

**The within-trial analysis — the one that would actually demonstrate learning —
had three studies.** The authors note that most studies report only average
performance across trials, which is why they cannot see learning happen. So they
looked at the three studies where trial-level data existed, and report that
participants "learned to align with better-performing AI over trials when
informative signals were available, but not otherwise." Read that conditional
carefully: in three studies, learning happened when the conditions for learning
were present. That is the mechanism the paper proposes, observed in three
instances, with a caveat attached.

**"Our results may actually represent a conservative estimate" is an argument
that cannot lose.** The authors reason that because studies average across all
trials, including the early ones before anyone has learned, the true effect of
learning must be larger than what they measured. This is plausible. It is also
unfalsifiable in the direction they need: any null result can be explained by
pointing to averaging. The honest version is the one they also give — that
meta-analysing only later trials would settle it, and the data to do that are
not public.

**The three recommendations quietly reveal how thin the foundations are.**
Asking for trial-level data sharing and noting "a dearth of publicly available
datasets" is an admission that the question the paper poses cannot currently be
answered by anybody, including them.

**A broader reading worth holding onto.** This paper argues the field has been
too pessimistic because it sampled from a "learning-handicapping part of the
design space." Maybe. But notice what that implies for everything else in this
reading list: the same argument applies in reverse to any human–AI study showing
a *benefit*. If a 30-trial session with no feedback understates what people could
achieve, a study that hands clinicians an AI with no training and no feedback
loop is also not telling you what the tool would do once people learned its
quirks — in either direction. The 09-25 decode found no additive human–AI
synergy in a simulated clinic where physicians got one 30-minute orientation and
no outcome feedback at all. By this paper's logic, that study was sampling the
same handicapped corner of the design space.

**And no funding or conflict-of-interest statement appears in the retrieved
text.**

# Statistics Spotlight

## Concept 1 — Hedges' *g*, and the brutal definition of "synergy"

Before the statistics, notice how demanding the question is.

**What synergy means here.** The outcome is the standardized difference in
performance between the human–AI combination and **whichever of the two did
better alone**. Not the average of the two. Not the human alone. The *better*
one. So "positive synergy" means the team beat the best individual performer; if
the AI alone scores 80 and the human alone scores 60, the team must beat 80 to
count as synergy.

**Why that bar matters.** This is why the original pessimistic finding is less
shocking than it sounds. A human–AI team that scores 75 in the example above has
*helped the human enormously* and still counts as negative synergy. The original
review found exactly this pattern: positive synergy where humans beat the AI,
negative where the AI beat humans. That is close to arithmetic. If the AI is
better and the human can override it, the human's overrides mostly subtract.

**What Hedges' *g* is.** A standardized effect size — the difference between two
groups divided by their pooled spread:

> *g* ≈ (mean of group A − mean of group B) ÷ pooled standard deviation

Dividing by the spread is what makes it portable. One study measures accuracy in
percent, another measures house-price error in dollars, another counts code bugs.
You cannot average those. But "how many standard deviations apart were they" is
the same unit everywhere, so you can.

**Rough conventions:** 0.2 is small, 0.5 medium, 0.8 large. On that scale, the
intervals this paper reports — reaching up to 0.34, 0.48, 0.69, 0.94 — span
"nothing" to "moderately large," which is another way of saying the data do not
pin the size down.

**Why *Hedges'* and not Cohen's *d*.** They are the same idea; Hedges' *g*
applies a small-sample correction, because Cohen's *d* is biased upward when
groups are small. With a median of 30 trials per study, that correction earns its
keep.

**An everyday version.** You want to know whether a cook and a recipe app
together make better food than the better of the two alone. Some dishes are
judged out of 10, some by how many diners finish the plate, some by a chef's
written critique. Converting every judgement into "how many standard deviations
better than usual" lets you combine them. And defining success as *beating the
better of cook-alone or app-alone* is a high bar: a cook who improves a lot by
using the app still fails it, if the app alone would have done better.

**Watch out for:** standardized effect sizes quoted without the raw numbers.
Dividing by the spread hides whether a "medium effect" is a meaningful real-world
difference. A *g* of 0.5 on a test where everyone scores within two points of
each other may be clinically trivial. Always ask what the underlying measurement
was. And whenever you see a claim about teamwork, ask what the comparison was —
against the better member, the average member, or the weaker one. The three
questions have three different answers, and only one of them is flattering.

## Concept 2 — Posterior probability of direction, and how to read Bayesian evidence

This paper reports its findings as "posterior probability of direction" — 84%
and 97% — rather than p-values. That is becoming common and is worth being able
to read.

**What it is.** The posterior probability of direction is the probability, given
the data and the model, that the effect is **positive rather than negative**. It
answers the question most people wrongly think a p-value answers: *how likely is
it that this goes the way I think it goes?*

**How to read the two values here:**

- The main feedback contrast: **84%**. *Deriving*: roughly a **16% chance the
  effect runs the other way** — that feedback is associated with *worse* synergy.
  One in six. That is genuinely weak, and the authors call it "tentative
  evidence."
- The feedback contrast among studies with explanations: **97%**, so about a 3%
  chance of the opposite direction. Much more persuasive — on 24 effect sizes.

**A rough translation, with a caveat.** A posterior probability of direction of
97.5% corresponds loosely to a two-sided p-value of about 0.05 when the prior is
uninformative. So 84% is in the neighbourhood of p ≈ 0.3, and 97% near p ≈ 0.06.
The mapping is approximate and breaks down with informative priors, but it is
useful for calibrating your reaction: **84% is not a finding, it is a direction
worth checking.**

**What makes direction different from magnitude.** You can be very confident
about the sign of an effect and know almost nothing about its size. A credible
interval running from 0 to 0.94, as the explanation-plus-feedback contrast does,
says "almost certainly positive, somewhere between nothing and large." Both
halves of that sentence are the finding.

**What Bayes factors add, and why I cannot give you them.** The paper also
reports Bayes factors — the ratio of how well the data are predicted by a model
with an effect versus one without. A Bayes factor of 3 means the data are three
times more consistent with an effect; conventional readings call 1–3 anecdotal,
3–10 moderate, above 10 strong. These were **stripped from the text I could
retrieve**, so I cannot tell you how strong the authors' own evidence
assessments were. That is a real gap in this summary, and it is why the grade
rests on design and counts rather than on magnitudes.

**And the method behind it.** RoBMA — robust Bayesian model-averaged
meta-analysis — does not fit one model. It fits many, including models that
assume publication bias and models that assume none, and averages their
conclusions weighted by how well each fits. This matters because the usual
alternative is picking one model and hoping. For a reanalysis of a literature
where null results are unlikely to have been published, building publication
bias into the model rather than testing for it afterwards is the more honest
choice.

**Watch out for:** a posterior probability of direction presented as though it
were a probability that the hypothesis is true in any absolute sense. It is
conditional on the model and the prior, exactly like everything else Bayesian.
And watch for the number being quoted without the credible interval — 97% sounds
decisive until you see it attached to an interval starting at zero.

## Concept 3 — Moderators in meta-analysis: observational epidemiology in disguise

This is the concept that determines how much to believe this paper, and it
generalises to every meta-analysis you will ever read.

**The setup.** A meta-analysis pools studies. A **moderator analysis** asks
whether the pooled effect differs according to some feature of the studies — here,
whether they gave participants feedback.

**The trap.** Within each original study, participants may have been randomised
to conditions. But **studies were not randomised to be the kind of study that
gives feedback.** Researchers chose. So comparing feedback studies against
non-feedback studies is an **observational comparison between research groups**,
not an experiment — even though every brick in the wall came from a randomised
experiment.

This is the single most misunderstood thing about meta-analysis. People treat it
as the top of the evidence pyramid and assume everything inside inherits that
status. Pooled main effects largely do. **Moderator analyses do not.** They are
observational, and subject to exactly the confounding this reading list covered
two days ago: something else about those 10 studies could be producing the
pattern.

**Why it bites especially hard here.** Think about who gives participants
feedback. Plausibly: researchers studying learning, who therefore run longer
sessions, include practice trials, recruit more engaged participants, pay better,
pick tasks where a correct answer actually exists, and design the AI advice more
thoughtfully. Every one of those could independently raise synergy. "Gave
feedback" may be a marker for "ran a better experiment."

**What the authors did about it, and why it is not enough.** They ran **12
additional meta-regressions**, each adding one of the original review's
moderators alongside feedback, and reported that "the effect directions remained
consistent across all 12 models." That is genuinely good practice and worth
crediting. But it can only adjust for confounders somebody already thought to
code. Nobody coded "how carefully was this experiment designed," because nobody
can.

**An everyday version.** You notice that restaurants with cloth napkins get
better food reviews, so you pool a thousand reviews and confirm it. Does the
napkin cause the food? Obviously not — restaurants that buy cloth napkins also
hire better chefs and buy better ingredients. Controlling for price and cuisine
helps a bit. It does not fix it. The only clean answer is to take one restaurant
and randomise the napkins.

**What would settle it, and the authors say so.** Take one task, one AI, one
population, and **randomise whether participants receive feedback.** The paper's
closing recommendation is exactly this — "experiments directly varying the
presence and type of feedback." Until someone runs it, this is a well-argued
hypothesis.

**Watch out for:** subgroup and moderator findings from meta-analyses presented
with the authority of the pooled result. The tell is a sentence of the form
"studies that did X showed bigger effects." Ask: *was X randomised, or chosen by
the researchers?* If chosen — and it almost always is — you are reading an
observational study about the habits of research groups, however rigorous the
individual trials inside it were.

# Jargon Translator

- **Human–AI synergy:** The team outperforming **whichever of human or AI was
  better alone**. A deliberately high bar.
- **Outcome feedback:** Being told the correct answer after each case. The
  variable this whole paper turns on, and the one almost no study provided.
- **Explainable AI / AI explanations:** Showing the user why the model produced
  its answer. Widely promoted as the cure for over-reliance; this paper suggests
  it only helps alongside feedback.
- **Hedges' *g*:** A standardized effect size — the difference between groups in
  units of their pooled spread — with a correction for small samples. Lets
  studies measuring different things be combined.
- **Effect size (as a count):** Here, one measurement per experimental condition.
  370 of them across 74 studies, because most studies had several conditions.
- **Meta-regression:** A meta-analysis that models *why* studies differ, rather
  than just averaging them.
- **Moderator:** A study feature that might change the size of the effect. Here:
  feedback, explanations, and the 12 features from the original review.
- **Credible interval:** The Bayesian interval. Unlike a confidence interval, it
  can legitimately be read as "95% probability the true value is in here, given
  the model."
- **Posterior probability of direction:** The probability the effect is positive
  rather than negative. 84% and 97% here.
- **Bayes factor:** How many times better the data are predicted by a model with
  an effect than one without. **Reported in the paper but stripped from the text
  retrieved.**
- **RoBMA (robust Bayesian model-averaged meta-analysis):** Fits many models,
  including ones that assume publication bias, and averages them by fit rather
  than picking one.
- **Practice trials:** Rounds before the real task, so a participant can learn
  the interface and the problem. The typical study here had none.
- **Trial-level data:** The record of what each participant did on each
  individual case, rather than their average. Available for only 3 of 74 studies.
- **Design space:** The set of all possible experiment designs. The paper's
  central claim is that the field has only sampled a corner of it.

# What You Can (and Can't) Say

**Fair to say:**

- Reanalysing all 74 studies from a prior meta-analysis of human–AI performance,
  this paper found the typical study was a single session with no practice
  trials, a median of 30 trials, and no outcome feedback.
- Only **10 of 74 studies (13.5%)** gave participants outcome feedback,
  contributing 98 of 370 effect sizes; only 3 of those 10 tracked change across
  trials; and **none** of the 74 experimentally varied whether feedback was
  given.
- A separate survey of 124 studies found only 6 (4.8%) provided feedback, which
  corroborates the point independently.
- Studies with feedback leaned toward positive synergy and those without leaned
  negative, but **neither estimate was credibly different from zero**, and the
  contrast between them had a posterior probability of direction of **84%**.
- Among studies that provided AI explanations, those also providing feedback
  (24 effect sizes) leaned positive while those without (148) were clearly
  negative; that contrast had a credible interval of **0 to 0.94** and a
  posterior probability of direction of **97%**.
- Without AI explanations, feedback did not moderate synergy.
- Directions held across 12 further models each controlling for one of the
  original review's moderators.
- The authors state their results are **correlational** and call for experiments
  that directly vary learning opportunities.

**Not fair to say:**

- ~~"Feedback makes human–AI teams work."~~ Nobody randomised feedback in any of
  the 74 studies. This is an association between research-design choices and
  outcomes.
- ~~"The earlier pessimistic finding was wrong."~~ The paper does not overturn it.
  It argues the experiments were not designed to detect the thing they were
  measuring.
- ~~"Explanations only work with feedback."~~ That is the hypothesis, supported by
  24 effect sizes against 148, with no experimental manipulation.
- ~~"Human–AI collaboration does work after all."~~ The authors' own framing is
  that the literature "underestimates the potential" — a claim about unexplored
  designs, not a demonstrated benefit.
- ~~"This shows 84% confidence that feedback helps."~~ A posterior probability of
  direction of 84% means roughly a 1-in-6 chance the effect runs the other way.
- ~~"PNAS confirms AI explanations are counterproductive."~~ The negative-synergy
  finding for explanations-without-feedback comes from the original review and
  is reproduced here, not newly established, and remains observational.

# Bottom Line for Your Life

**The idea worth taking from this is about how a question gets asked.** A large
review concluded that people and AI together do worse than the better of the two
alone, and that conclusion spread. This paper points out that in the typical
experiment behind it, a person was shown an AI's answer thirty times and never
once told whether they had been right. You would not test whether someone can
drive by putting them in a car with the windscreen painted over. The finding may
still be true. But it was measured in conditions where improvement was close to
impossible, and that is a fact about the measurement, not about people.

Carry that as a habit: when a study reports that humans fail at something, ask
**what the humans were allowed to learn from.** It is the same question as "what
did you take away from the human?" from two days ago, pointed at experience
rather than at tools.

**The practical lesson, if you ever use an AI tool seriously:** explanations
without verification may be actively bad for you. The pattern here — explanations
with feedback leaning positive, explanations without feedback clearly negative —
suggests that a confident-sounding rationale you have no way to check mostly
teaches you to trust the tool, not to calibrate against it. Which means the
useful thing is not a better explanation. It is **keeping score**: noticing when
the tool was right and when it was wrong, often enough and soon enough that you
learn where its edges are. Almost no product is designed to help you do that, and
on this evidence almost no experiment has been either.

**And a caution about the paper itself.** Its most interesting claim rests on 24
of 370 effect sizes, from studies nobody randomised. The authors are unusually
straight about this — they call the results correlational, say neither estimate
differed credibly from zero, and ask for the experiment that would settle it. The
right response is to find the hypothesis genuinely promising and to hold it
loosely, which is what they ask for. When a paper tells you how it could be
wrong, believe that part too.

---

*Education, not medical advice. Decoded 2026-10-02 from the PubMed Central
open-access full text. **The PMC rendering dropped the Hedges' g point estimates
and all Bayes factors**, which survive only in Figure 1D and the supplementary
appendix; this summary therefore reports directions, counts, credible-interval
bounds and posterior probabilities, and states explicitly where a magnitude could
not be retrieved. Derived calculations — the share of the evidence base in each
cell, and the complement of each posterior probability of direction — are
labelled as derived and were computed from the paper's own reported counts.*
