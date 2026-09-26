# Two Chatbots Walk Into a Medical School. Only One Beat Google — Sort Of.

**Paper:** Effectiveness of ChatGPT and DeepSeek in Urology Medical Education:
Randomized Controlled Trial
**Authors:** Yang W, Xu T, Wei J, Zheng W, Yan W, Wang J, Chu G, Niu H
**Venue / Year:** Journal of Medical Internet Research, 2026;28:e89315
**DOI:** https://doi.org/10.2196/89315
**PubMed:** https://pubmed.ncbi.nlm.nih.gov/42766393/
**Full text used:** https://pmc.ncbi.nlm.nih.gov/articles/PMC13592387/
**Basis of this analysis:** FULL TEXT (PubMed Central open-access copy,
retrieved 2026-09-26). Figures 1–4 and the two supplementary appendices were
not retrievable; nothing here depends on a figure value. All quoted numbers
come from the article body or Tables 2–6.
**Date decoded:** 2026-09-26
**Evidence grade:** 2/5

---

# The Gist

Researchers at Qingdao University in China took 220 medical students, split
them three ways by drawing sealed envelopes, and told each group how to revise
urology for the next few weeks. One group had to use ChatGPT o3-mini. One group
had to use DeepSeek R1. The third group was allowed only ordinary internet
searching — forums and search engines — and no AI at all. Then everyone sat the
same 50-question test.

The DeepSeek group scored about 66 out of 100. The ChatGPT group scored about
59. The control group scored about 52.

From this the paper's abstract concludes that DeepSeek "surpassed both the
control and ChatGPT o3-mini groups." Here is the problem, and it is the whole
reason this paper is worth your time: the study **directly tested** DeepSeek
against ChatGPT, and that comparison came back with a p-value of .35 — nowhere
near significant. DeepSeek beat the no-AI control. ChatGPT did not beat the
no-AI control. But "one of them beat the control and the other didn't" is not
the same finding as "one beat the other," and this paper's own numbers say the
two chatbots were statistically indistinguishable.

There is a second problem. About one student in five who was randomized never
turned up for the test. The authors deserve real credit for checking what
happens if those absent students would have done badly — and when they checked,
the entire DeepSeek advantage evaporated (p = .41).

So: a genuinely well-intentioned trial, with a registered protocol and a proper
sensitivity analysis, whose headline claim is not supported by its own
statistics. It is an excellent paper to learn from and a bad paper to cite.

# Study Snapshot

- **Study type:** Parallel-design, three-arm randomized controlled trial in
  education, plus a separate benchmark test of the two AI models, plus a
  questionnaire. Randomization puts it above the observational studies that
  dominate this reading list; the outcome is an exam score, not anyone's health.
- **Participants:** 228 clinical medicine undergraduates from a single
  institution, the Medical College of Qingdao University, years two to five.
  8 declined before randomization, leaving **220 randomized**. Entry required
  having passed core basic science courses with no failures.
- **Groups:** 1:1:1 — ChatGPT o3-mini, DeepSeek R1, or control. Allocation by
  drawing sealed, opaque, sequentially numbered envelopes, opened by an
  independent coordinator not involved in recruitment or assessment. Stratified
  by year of study and prior academic performance.
- **What each group did:** The two AI groups had to use their assigned tool and
  were forbidden other search engines; coordinators checked they each spent at
  least 30 minutes a day with it. The control group used only conventional
  internet searching and was forbidden any AI.
- **Learning material:** Identical across groups — NCCN guidelines, European
  Association of Urology guidelines, and Chinese medical textbooks, covering
  urinary tract injury, obstruction, stones, tuberculosis, and tumours.
- **Primary outcome:** Total score on a 50-question, 100-point,
  two-hour multiple-choice test drawn from past Chinese and US licensing
  examinations. Secondary and exploratory: scores on basic-knowledge (A1),
  clinical-scenario (A2), image-based, and text-based question subsets.
- **Blinding:** Students knew their group — unavoidable. The two researchers who
  scored the tests were blinded, with identities reduced to numeric IDs and the
  allocation key held by a third researcher. That part was done properly.
- **Separate benchmark:** 185 urology multiple-choice questions from China's
  standardized residency training examination, put to each model three times on
  14 March 2025.
- **Who finished:** **175 of 220** sat the test — a 20% loss after
  randomization, and the paper notes the DeepSeek group lost the most. Only 105
  of the AI-group students completed the questionnaire.
- **How long:** Recruitment from 9 March 2025; testing complete by 5 April 2025.
  A few weeks.
- **Ethics:** Approved by the Ethics Committee of the Affiliated Hospital of
  Qingdao University (QYFYWZLL30898), written informed consent obtained.
- **Registration:** Chinese Clinical Trials Registry, ChiCTR2600118749. The
  registration **date is not stated** in the text retrieved. (The registry's
  numbering convention embeds the year, and a "26" prefix would indicate 2026 —
  after this March–April 2025 trial finished. Treat that as an apparent
  indication, not a confirmed fact.)
- **Funding:** **Not reported** in the text retrieved.
- **Conflicts of interest:** **No conflict-of-interest statement appears in the
  text retrieved.**

# How Strong Is This Evidence? — Grade 2/5

**What this study did well** — and these are not trivial:

- It randomized, with a real concealment procedure: opaque sequentially numbered
  envelopes opened by someone who had no role in recruiting or scoring.
- It blinded the outcome scorers, and explained exactly how.
- It ran a **prespecified sample size calculation** — 80% power, α = .05, three
  groups, 20% expected dropout, 76 per group.
- It named a single primary outcome in advance (total score) and labelled
  everything else secondary or exploratory.
- It corrected for multiple comparisons using Bonferroni.
- It reported effect sizes with bootstrap confidence intervals, not just
  p-values.
- It ran **intention-to-treat plus three sensitivity analyses**, including a
  worst-case scenario that undercut its own headline — and reported that
  honestly.
- It registered with a clinical trials registry and published its analysis code.
- Its limitations section volunteers the differential dropout, the possible
  survivorship bias, the novelty effect, and the risk that students could not
  cross-check AI outputs.

**Why it still only earns a 2:**

The problem is not carelessness. It is that the paper's conclusions do not
follow from the numbers it printed, in three specific ways:

1. The title and abstract compare ChatGPT to DeepSeek. The direct comparison was
   not significant (p = .35, and p = .13 in the complete-case analysis). The
   headline rests on a comparison the study did not demonstrate.
2. The one significant result sat at p = .045 with a confidence interval running
   from **0.28 to 25.01 points**. A lower bound of a quarter of a point out of
   100 is not a robust finding.
3. Every effect size reported was "small" by the authors' own label, with
   **every 95% confidence interval touching 0.00** (ε² values of 0.02 to 0.04).

Add a 20% post-randomization dropout that was worst in the winning arm, a result
that disappears under pessimistic imputation, an unblinded intervention, a
single institution, a few weeks of follow-up, no funding or conflict statement,
and internal numbers that do not reconcile (below) — and what you have is a
well-structured trial that cannot support its own conclusion.

# The Editor's Concerns

**The headline comparison was tested and failed.** This is the central issue.
Intention-to-treat results: DeepSeek versus control, +12.65 points (95% CI 0.28
to 25.01, p = .045). ChatGPT versus control, +6.45 points (95% CI −3.74 to
16.65, p = .21). DeepSeek versus ChatGPT, +5.94 points (95% CI −6.82 to 18.70,
**p = .35**). To their credit the authors say this plainly in the results — the
advantage "was primarily driven by its superiority over the control group rather
than by a measurable incremental benefit over ChatGPT." Then the abstract says
DeepSeek "surpassed both the control and ChatGPT o3-mini groups." Those two
sentences are in the same paper. See Statistics Spotlight.

**The study was far less powerful than planned, because the variability was two
and a half times what was assumed.** The sample size calculation assumed a
standard deviation of about 10 to 11 points. The actual standard deviations were
**27.62, 23.25, and 28.02** — students' scores ranged from 10 to 98 out of 100,
in every group including the control. *Deriving* from the paper's own figures:
the planned design (76 per group, a 10-point difference, SD ≈ 10.5) had
essentially 100% power; the study as actually run (about 58 per group, SD ≈ 26)
had roughly **50% power** to detect the 10-point difference it was designed
around — a coin flip — and about 70% power for the 14-point difference it
actually observed once Bonferroni correction is applied. A study that plans for
80% power and lands near 50% will produce exactly this pattern: one barely
significant result, several non-significant ones in the same direction, and a
strong temptation to read the pattern as a ranking.

**The numbers describing who was analyzed do not reconcile.** The Methods say
the intention-to-treat analysis covered "all randomized participants (N=228)"
and that missing scores were imputed for "the 8 participants who did not attend
the examination," with a complete-case analysis of "n=220." The Results say 8
students withdrew **before** randomization and **45** did not complete the test,
leaving **175** who sat it — and Table 3 splits the 228 into 175 respondents and
53 non-respondents, which is 8 + 45. Table 2's group sizes sum to 175, and its
group means reproduce the complete-case estimates exactly (66.14 − 51.83 =
14.31; 58.67 − 51.83 = 6.84; 66.14 − 58.67 = 7.47, all matching Table 6). So the
complete-case analysis had **175** participants, not 220, and **53** outcomes
were missing, not 8. Also, 220 were randomized, not 228 — the 8 who withdrew
beforehand cannot be in an intention-to-treat population. None of this changes
the reported estimates, but a reader cannot reconstruct the analysis from the
Methods as written.

**Twenty percent of randomized students vanished, and most heavily from the
winning arm.** The authors flag this themselves and name the risk: survivorship
bias, where the more motivated or more technically capable students were the
ones who stuck with the newer tool and also the ones who would have scored well
anyway. Their worst-case analysis is the test of this, and it fails: DeepSeek
versus control falls to +4.20 points (95% CI −5.74 to 14.14, **p = .41**). The
finding survives only if you assume the absentees would have scored like the
people who showed up.

**The comparison may be measuring study time and novelty, not AI.** AI-group
students were monitored to ensure at least 30 minutes a day with the tool.
No equivalent time floor is described for the control group. If the AI groups
simply revised more, that alone could produce the gap. The paper also notes that
AI-group students could consult urologists invited by the researchers when they
struggled with AI-generated content; no comparable support is described for
controls. And the authors themselves raise the novelty effect — a shiny new
conversational interface is more engaging than a search engine, independent of
content quality.

**Every effect size interval includes zero.** ε² was 0.03 for total score (95%
CI 0.00–0.10), 0.03 for A1 questions (0.00–0.09), 0.02 for A2 (0.00–0.07), 0.04
for image questions (0.00–0.11), 0.03 for text questions (0.00–0.09). The
authors label all of these "small." A significance test saying "there is an
effect" alongside an effect-size interval that includes "there is no effect" is a
contradiction the paper does not resolve.

**The benchmark comparison has no statistical test at all, and some categories
have five questions.** DeepSeek scored 84.32% (156/185) overall versus ChatGPT's
68.11% (126/185) — a large, believable gap. But the paper then claims
"particularly significant advantages in the areas of diagnosis, complications,
and treatment" without reporting any test for those comparisons. "Complications"
was **five questions**: DeepSeek got 5 of 5, ChatGPT 3 of 5. "Etiology" was five
questions, with both models scoring 4 of 5. Anatomy and clinical manifestations
were nine each. Per-category differences on five items are noise. (There is also
a transcription error in the text: ChatGPT's complications result is written
"3/51, 60%" where Table 5 makes clear it is 3 of 5.)

**One genuinely interesting benchmark finding goes unremarked.** Each question
was asked three times. DeepSeek answered 156 questions right all three times and
28 wrong all three times, with just one question split — it was almost perfectly
consistent. ChatGPT split on 29 questions (16 mostly-right, 13 mostly-wrong).
That is a real difference in **reliability**, not just accuracy, and it is
arguably the paper's most useful observation about the two models. It is not
discussed.

**The questionnaire tells you almost nothing.** It went only to the AI groups —
so there is no comparison — and only 105 of them answered. The authors
acknowledge that non-respondents may hold less favourable views. "96.19% of
respondents reported using AI during their undergraduate studies" is a fact
about students who volunteered to answer a survey about AI after being assigned
to use AI.

**Short, narrow, single-site.** A few weeks, one medical college, one specialty,
one language. Nothing here speaks to whether knowledge was retained, and the
authors say so.

# Statistics Spotlight

## Concept 1 — A difference in significance is not a significant difference

This is the single most common statistical error in published research, and this
paper is a clean specimen of it.

**The setup.** Three groups. DeepSeek beat control: p = .045, significant.
ChatGPT did not beat control: p = .21, not significant. The tempting conclusion:
*DeepSeek works and ChatGPT doesn't, therefore DeepSeek is better than
ChatGPT.*

**Why that doesn't follow.** "Significant" is not a property a treatment has. It
is the outcome of one specific comparison, and it depends on where a somewhat
arbitrary line at p = .05 happens to fall. Two results can sit on opposite sides
of that line while being almost identical to each other.

Look at what the study actually measured. DeepSeek was +12.65 points above
control. ChatGPT was +6.45 points above control. The gap between the two AI
groups is therefore about 6 points — and when the study tested that 6-point gap
directly, it got **p = .35**, with a confidence interval from −6.82 to +18.70.
That interval comfortably contains zero. The honest reading is: *we cannot tell
these two chatbots apart.*

**The intuition.** Imagine two runners racing against a clock. Runner A finishes
clearly under the qualifying time; runner B misses it by a hair. You now know A
qualified and B didn't. You do **not** know that A is meaningfully faster than
B — they may have finished a step apart. To compare the runners you have to time
them against **each other**, not against the threshold.

**A tiny worked example.** Suppose a control group averages 50. Group A scores
57 and just clears significance. Group B scores 56 and just misses. The
difference between A and B is one point. Yet the naive reading — "A works, B
doesn't" — invites you to believe A is the better intervention, when the data
say the two are nearly the same.

**Why it's so seductive.** The brain converts "significant / not significant"
into "real / not real," which is a category difference, and category differences
feel like big differences. But p = .045 and p = .055 describe almost identical
evidence. The line at .05 is a convention, not a fact about the world.

**Watch out for:** any claim that treatment A is better than treatment B where
the evidence offered is that A beat placebo and B didn't. It appears constantly
— two drugs each trialled against placebo, two teaching methods, two diets, two
exercise regimes, subgroup claims ("it worked in men but not women," when the
men-versus-women interaction was never tested). **The question to ask is always
the same: was A ever compared directly with B, and what did that comparison
say?** In this paper, it was, and it said p = .35.

To be fair to these authors, they state the correct interpretation in their
results and their conclusion ("the higher scores observed with ChatGPT were only
numerical and lacked statistical significance"). It is the abstract — the part
almost everyone reads — that overreaches.

## Concept 2 — Multiple comparisons and what Bonferroni costs you

With three groups you cannot just run three tests and keep α = .05, because
every test you run is another chance to be fooled by luck.

**The core problem.** If nothing is really going on, each test at the .05 level
has a 5% chance of a false positive. Run three independent tests and the chance
of at least one false positive is not 5% but about 14% — one minus 0.95 cubed.
Run twenty and it's around 64%. This is why data-dredging works: keep testing and
something will eventually cross the line.

**The everyday version.** Flipping five heads in a row is impressive from one
person. If a thousand people each flip five times, about 31 will manage it, and
none of them is magic. The question is never "how unlikely was this result?" but
"how many chances did it have to appear?"

**What this study did.** It used a two-step procedure. First a single overall
test across all three groups at once — the **Kruskal-Wallis test**, a rank-based
comparison used here because the score data were not normally distributed
(scores clustered at the extremes, with ranges of 10 to 98). Only if that
overall test came back significant did it proceed to the three pairwise
comparisons, using **Dunn's test with a Bonferroni correction**.

Bonferroni is the simplest correction there is: divide your threshold by the
number of comparisons. Three comparisons means each needs p < .05 ÷ 3 = .0167 to
count. That is the right instinct and it is why the paper's pairwise findings
should be taken more seriously than uncorrected ones would be.

**What it cost.** Being stricter about false positives always means being more
vulnerable to false negatives. *Deriving* from this paper's own numbers: with
about 58 students per group and the observed standard deviation of roughly 26
points, the study had around 83% power for its observed 14-point difference at
α = .05 — but only around **70%** once the threshold tightened to .0167. So
roughly a three-in-ten chance of missing a real effect of that size, and far
worse for smaller ones. This is the trade-off, not a flaw: you cannot reduce one
error type without increasing the other.

**Watch out for two opposite abuses.** The first is no correction at all — a
paper reporting fifteen comparisons and celebrating the two that hit p < .05.
The second, subtler one is **correcting within families but not across them**.
This study ran the Kruskal-Wallis test five separate times: total score, A1
questions, A2 questions, image questions, text questions. Within each, the three
pairwise comparisons were corrected. Across the five outcomes, nothing was. That
is defensible because total score was prespecified as primary and the rest were
labelled secondary — but it means four of the five reported "significant
differences" should be read as exploratory, not as four independent
confirmations. The abstract's framing, which highlights DeepSeek surpassing
others "in total scores across various question types," invites the opposite
reading.

## Concept 3 — Missing data, intention-to-treat, and why the worst case matters

About 45 of 220 randomized students never sat the test. What you do with those
gaps can flip a result — and in this paper, it does.

**Why you cannot just ignore them.** The obvious move is to analyse whoever
showed up. That is a **complete-case analysis**, and it quietly breaks
randomization. Randomizing makes groups comparable; people dropping out for
their own reasons makes them non-comparable again. If the students who
disappeared from the DeepSeek arm were the ones finding it frustrating — while
the ones who stayed were the keenest and most capable — then the surviving
DeepSeek group is a hand-picked elite, and its high score reflects who remained
rather than what they used. The authors name this exact risk as survivorship
bias, and note the DeepSeek arm lost the most students.

**Intention-to-treat.** The standard defence is to analyse everyone as
randomized, regardless of what they actually did — including people who dropped
out, switched, or ignored instructions. It feels wrong (why include people who
didn't do the thing?) but it is the only way to preserve the comparison
randomization bought you. It also answers the more honest question: not "does
this work in people who stick with it?" but "what happens if we offer it?" — the
second being what a teacher or clinician actually gets to decide.

**How this paper filled the gaps.** It used **multiple imputation by chained
equations** — statistical software estimates each missing score from the
patterns in the data it does have, does this 20 separate times to represent
genuine uncertainty, and averages the answers. This rests on an assumption
called **missing at random**: that once you account for what you observed, the
people who vanished were not systematically different. Reasonable, and
unprovable.

**Then they stress-tested it, which is the part to admire.** They reran
everything under deliberately extreme assumptions:

- Multiple imputation (missing-at-random): DeepSeek +12.65 points, p = .045
- Complete cases only: +14.31, p = .004
- **Worst case** (every absentee given the lowest score in their group): +4.20,
  **p = .41**
- Best case (every absentee given the highest score in their group): +16.11,
  p = .001

Read that ladder. The finding is robust under optimistic and moderate
assumptions and **collapses entirely** under a pessimistic one. The
DeepSeek-versus-ChatGPT comparison was non-significant under every single
assumption.

**The right conclusion is the conditional one:** DeepSeek-assisted study beat
conventional searching *if* the students who skipped the exam would have
performed roughly like those who took it. If the dropouts were the ones
struggling, there is no demonstrated effect at all.

**An everyday version.** A gym advertises that members lose 15 pounds on
average. That average covers the people still turning up. Everyone who quit in
week two isn't in the number. To honestly evaluate the gym you need everyone who
signed up — including those who gave up — and if you can't find them, you must
at least ask: what if the quitters did badly? That question is the worst-case
analysis, and this paper asked it.

**Watch out for:** any trial where more than about 10% of participants are
missing from the analysis and only one method of handling them is reported —
especially when dropout differs between arms. If a paper reports only a
complete-case analysis, the result is an upper bound on the true effect, not an
estimate of it. And when a paper does run a worst-case analysis and the result
disappears, that is not a footnote. That is the finding.

# Jargon Translator

- **Generative AI / large language model:** Software that produces text by
  predicting plausible continuations. ChatGPT o3-mini (OpenAI) and DeepSeek R1
  (DeepSeek, China) are the two tested here.
- **A1 and A2 question types:** Chinese examination categories. A1 tests recall
  of basic facts; A2 gives a clinical scenario and tests reasoning. The AI
  advantage appeared on A1 (facts) and not on A2 (reasoning) — arguably the most
  telling pattern in the paper.
- **Sealed envelope randomization:** Allocation hidden inside opaque
  sequentially numbered envelopes, so nobody can steer who lands where.
- **Stratified randomization:** Randomizing separately within blocks (here, year
  of study and prior performance) so groups stay balanced on things that matter.
- **Kruskal-Wallis test:** Compares three or more groups by rank rather than by
  mean. Used when data aren't normally distributed, as here.
- **Dunn's post hoc test:** The follow-up that identifies *which* pairs differ
  after Kruskal-Wallis says *some* pair does.
- **Bonferroni correction:** Divide your significance threshold by the number of
  comparisons. Here, .05 ÷ 3 = .0167.
- **ε² (epsilon squared):** An effect size for rank tests — roughly, the share of
  variation in scores explained by group. 0.03 means about 3%.
- **β (beta) in Table 6:** The estimated point difference between two groups on
  the 100-point test.
- **Bootstrap confidence interval:** Resampling the data (1000 times here) to see
  how much an estimate wobbles.
- **Missing at random (MAR):** The assumption that absentees aren't
  systematically different once you account for what you measured. Necessary for
  imputation, and never verifiable.
- **Multiple imputation by chained equations:** Filling in missing values
  repeatedly (20 times here) so the final answer carries the uncertainty rather
  than hiding it.
- **Predictive mean matching:** An imputation method that borrows a real observed
  value from a similar participant instead of inventing a number.
- **Survivorship bias:** Drawing conclusions from who remained, while the people
  who left — and the reasons they left — are invisible in the data.
- **CONSORT-EHEALTH:** The reporting checklist for trials of digital health and
  e-learning interventions. Filing one is a good sign.
- **Temperature (model setting):** How much randomness the model uses. Left at
  default here, meaning answers could vary between runs — which is why each
  question was asked three times.

# What You Can (and Can't) Say

**Fair to say:**

- In a three-arm randomized trial at one Chinese medical college, students told
  to revise urology with DeepSeek R1 scored about 66 out of 100, students told
  to use ChatGPT o3-mini scored about 59, and students restricted to ordinary
  internet searching scored about 52.
- The DeepSeek-versus-control difference reached significance under the main
  analysis (+12.65 points, p = .045) but its confidence interval nearly touched
  zero (0.28 to 25.01).
- The ChatGPT-versus-control difference was **not** significant (p = .21).
- The direct DeepSeek-versus-ChatGPT comparison was **not** significant
  (p = .35) under any missing-data assumption.
- Under a worst-case assumption about the 20% who skipped the exam, the DeepSeek
  advantage disappeared (p = .41).
- All reported effect sizes were small, with every confidence interval including
  zero.
- On a separate 185-question benchmark, DeepSeek answered 84.32% (156/185)
  correctly versus ChatGPT's 68.11% (126/185), and was markedly more consistent
  across repeat attempts.
- The AI advantage appeared on basic-recall questions and did **not** reach
  significance on clinical-reasoning questions.
- Students surveyed were enthusiastic, and 73.33% (77/105) wanted formal AI
  training — but only AI-group students were surveyed, and only 105 answered.

**Not fair to say:**

- ~~"DeepSeek is better than ChatGPT for medical education."~~ Tested directly,
  p = .35. This is the paper's own headline and its own data contradict it.
- ~~"AI improves medical student learning."~~ One of two AI tools beat a
  restricted control on one test at one college over a few weeks, at p = .045,
  and the finding vanishes under pessimistic assumptions about dropouts.
- ~~"AI helps students reason clinically."~~ The A2 clinical-scenario comparison
  was not significant (p = .09). The authors say this explicitly.
- ~~"DeepSeek is 84% accurate at urology."~~ That is performance on
  multiple-choice residency exam questions, asked three times each. The paper
  itself warns that "accuracy on standardized multiple-choice assessments does
  not translate to clinical validity, diagnostic reliability, or therapeutic
  safety."
- ~~"DeepSeek is dramatically better on complications and etiology."~~ Those
  categories had five questions each.
- ~~"96% of medical students use AI."~~ 96.19% of 105 self-selected respondents
  who had just been assigned to use AI.
- ~~"This shows AI should be integrated into medical curricula."~~ A few weeks,
  one specialty, one site, no retention testing, and a primary result that does
  not survive its own sensitivity analysis.

# Bottom Line for Your Life

**The lesson here is a sentence you can use for the rest of your life: "was that
ever compared directly?"** This paper's entire headline is the
difference-in-significance fallacy — DeepSeek cleared the p < .05 bar, ChatGPT
missed it, and the abstract silently converts that into DeepSeek beating
ChatGPT. The direct test, printed in the paper's own Table 6, says p = .35. You
will meet this error in drug comparisons, diet studies, education research, and
every argument where someone says "X is proven and Y isn't, so X is better."
Most of the time nobody ever raced X against Y.

**The second habit: when a study is missing people, ask what happens if the
missing ones did badly.** These authors deserve genuine credit — they asked that
question themselves, published the answer, and the answer undid their headline
(p = .045 became p = .41). Almost no paper does this. When you see a trial where
a fifth of participants vanished and only one way of handling them is reported,
you are looking at the most flattering version of the result.

**And the finding buried in the pattern is more interesting than the headline.**
The AI advantage showed up on questions asking students to recall facts, and did
not reach significance on questions asking them to work through a clinical
scenario. That is exactly what you would predict if chatbots are excellent at
handing you information and neutral at teaching you to think. Whether that
matters depends on which of those two things you believe medical education is
for — and this study, over a few weeks with no retention testing, cannot tell
you.

---

*Education, not medical advice. Decoded 2026-09-26 from the PubMed Central
open-access full text. Derived calculations — the power estimates, the
reconciliation of participant counts, and the group-mean differences confirming
the complete-case sample size — are labelled as derived and were computed from
the paper's own reported values.*
