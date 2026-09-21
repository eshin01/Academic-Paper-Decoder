# Trust in Generative AI for Health Information Consumption and the Effect of Learned Dependency: Randomized Controlled Experimental Study

- **Authors:** Arif Ahmed, Gondy Leroy, Agrim Sachdeva, Philip Harber, Stephen Rains, Seokjun Youn, Prosanta Barai (University of Arizona) — 7 authors
- **Venue:** Journal of Medical Internet Research, 2026;28:e98326 (published September 16, 2026)
- **DOI link:** https://doi.org/10.2196/98326
- **PubMed link:** https://pubmed.ncbi.nlm.nih.gov/42747973/ (PMID 42747973)
- **Full-text link used:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC13580606/ (PubMed Central, open access)
- **Basis:** FULL TEXT — introduction, theoretical framework, all five hypotheses, complete Methods for both experiments, the full regression table with coefficients and confidence intervals, the reliability and validity section, discussion, the nine stated limitations, and conclusions were read from the open-access PubMed Central copy. Figures and supplementary tables were not retrieved, so anything living only there is marked as not retrieved rather than guessed. Ethics: approved by the institutional review board under protocol STUDY00002235, with informed consent obtained and no personally identifiable information collected; the clinical text stimuli came from the MIMIC-III database under a data use agreement. Reporting followed the CHERRIES checklist for internet surveys, with CONSORT flow diagrams for both experiments. Funding and competing-interest statements were not present in the retrieved text. Identifiers verified against the live PubMed/NLM record; direct URL browsing is blocked in this environment, so links are constructed from that verified record.
- **Decoded:** 2026-09-21
- **Note:** queued on 2026-09-17 as unreachable. A PubMed Central copy appeared by 2026-09-20, so it could be decoded in full.

---

# The Gist

You have been reading decoded papers for three weeks now. This one is about what that habit might be doing to you. The researchers ran two randomized experiments — 338 students, then 563 online workers — showing people a real hospital discharge instruction next to a version rewritten by GPT-4o. Sometimes the rewrite was faithful. Sometimes it had medical details deliberately corrupted. Then they asked how much people trusted the AI version, and separately measured how much each person habitually leans on AI in daily life. The main result is uncomfortable. On average, people did trust the accurate version more, which is what you want. But **the more someone reported relying on AI generally, the less that gap mattered to them.** Heavy users trusted the corrupted summaries nearly as much as the correct ones. The researchers then tried the obvious fix — bolding the important text so people would look harder — and it did nothing at all. Twice. Even when they bolded six errors instead of three.

# Study Snapshot

- **Study type:** Two randomized controlled experiments run online. Randomization applies to two things — whether the AI text was accurate and whether it was highlighted. The third variable, how dependent on AI each person is, was measured, not assigned. That distinction matters and is picked up below.
- **The setup, identical in both experiments:** participants saw two blocks of text side by side. On one side, a real discharge instruction from the MIMIC-III clinical database. On the other, a version of it produced by GPT-4o. Then they rated how much they trusted the AI version.
- **What was manipulated.** First, accuracy: the AI version either preserved the original clinical content or had critical medical details deliberately altered. Second, highlighting: key portions of the AI text were either shown in bold or shown plain.
- **Five different source texts were used,** so that any finding could not be an artifact of one particular discharge summary. With two accuracy conditions, two highlighting conditions, and five texts, participants were randomly assigned to one of 20 groups by the survey software, with back-navigation disabled.
- **Experiment 1: 338 participants,** junior-level business students given course credit. Nearly even by sex (171 male, 167 female), 99.41% aged 18 to 30, 78.70% White, 80.47% with high school as their highest completed education, and 97.93% business or economics majors. Errors were inserted at 3 places in each text.
- **Experiment 2: 563 participants** recruited from Amazon Mechanical Turk, paid 50 cents, US-based with a 95% approval rating. This sample was 77.98% male, mean age 31.7, 95.56% White, and far more educated — 72.82% held a bachelor's degree and 22.20% a master's. Errors were inserted at 6 places rather than 3, and all six were bolded in the highlighting condition.
- **How dependency was measured:** a self-report questionnaire about habitual reliance on AI for decisions and information. Six items in the first experiment, expanded to 17 in the second.
- **How trust was measured:** agreement with statements such as "the GenAI's output is accurate," on a five-point scale. Three items in the first experiment, four in the second after statistical testing removed two weak ones.
- **Result 1 — accuracy mattered, on average.** People trusted the correct version more than the corrupted version in both experiments, with very strong statistical support each time.
- **Result 2 — highlighting did nothing.** In experiment 1, the effect of bolding on trust was 0.149 with a confidence interval running from −0.622 to 0.920, a finding indistinguishable from zero. In experiment 2 it was 0.013, interval −0.074 to 0.101. Two experiments, two nulls, the second with twice as many errors highlighted.
- **Result 3 — habitual AI users trusted the AI more overall.** The association was 0.277 in experiment 1 and a much larger 0.822 in experiment 2.
- **Result 4, the central finding — dependency blunted the ability to tell good from bad.** The interaction between accuracy and dependency was negative in both experiments: −0.399 in the first, −0.459 in the second. In plain terms, the more someone leaned on AI generally, the smaller the trust difference between the accurate and the corrupted summary.
- **Result 5 — highlighting did not rescue heavy users either.** The three-way interaction was −0.023 in experiment 1 and 0.142 in experiment 2, both far from significant.
- **One measurement problem the authors report on themselves.** In experiment 1, the trust scale and the dependency scale could not be statistically distinguished from each other. They correlated at 0.697, above the threshold that shows two questionnaires are measuring different things. This was fixed in experiment 2 but stands as a caveat on the first experiment's dependency findings.
- **Funding / conflicts:** not present in the retrieved text.

# How Strong Is This Evidence?

**Grade: 3/5 — clean experimental design on the parts that were randomized, with a genuine replication and unusually candid reporting, undermined by a central variable that was measured rather than assigned and samples that are nothing like the people the findings are about.**

Several things here are done properly. Hypotheses were stated in advance with reasoning, rather than fished from the data. Two experiments were run with different populations and a strengthened manipulation the second time. The survey software handled randomization and blocked participants from going back. Five different source texts guard against a one-stimulus fluke. The questionnaires were subjected to formal factor analysis, weak items were removed and reported, and checks were run for questionnaire artifacts, multicollinearity, and participants clicking straight down the page. The paper lists nine limitations, several of which a less careful team would have omitted — including that their own first experiment's two key measures overlapped too much to be told apart.

But the study's headline is about learned dependency, and dependency was not randomized. Accuracy and highlighting were assigned by coin flip; dependency was whatever each person reported about themselves. That makes the dependency findings correlational sitting inside an experimental design, which is a subtler thing than it looks. People who say they rely heavily on AI may differ in dozens of ways — how carefully they read, how much they enjoy questioning things, how much time they spent on a 50-cent task. The paper's own wording is careful, using "associated with" rather than "causes." The framing invites the stronger reading anyway.

Then there are the samples. Experiment 1 is business students, 98% from one major, 80% with high school as their highest completed education. Experiment 2 is crowdworkers, 78% male, 96% White, 95% degree-holding. The paper's subject is "health information consumers." Neither group is a sample of people looking up health information about something that frightens them.

# The Editor's Concerns

- **The effect sizes do not replicate, only their directions do.** This is the concern that should give a reader most pause and the paper does not address it. The effect of accuracy on trust was 2.107 in experiment 1 and 0.203 in experiment 2 — roughly a tenfold difference on the same five-point scale. Meanwhile the effect of dependency went the other way, tripling from 0.277 to 0.822. The second experiment used a *stronger* accuracy manipulation, so a much smaller accuracy effect is genuinely puzzling. Two studies agreeing on the sign of an effect while disagreeing by an order of magnitude on its size is weaker evidence than "replicated" suggests.
- **An effect of 2.107 on a five-point scale is implausibly large on its face.** The scale runs from 1 to 5, so the entire available range is 4 points. A single manipulation moving average trust by more than half the total range would be a remarkable result, and it did not reappear in the larger, better-measured experiment.
- **Dependency was measured, not assigned,** so the two most interesting findings sit outside the experiment's causal protection. Whether habitual AI use *makes* people less discerning, or whether less discerning people gravitate to AI, cannot be separated here. The authors call for longitudinal work, which is the right answer.
- **In experiment 1, trust and dependency could not be told apart statistically.** The two scales correlated at 0.697, exceeding the threshold for showing they measure distinct things. So one reading of experiment 1's dependency result is that a trust-flavoured questionnaire correlated with another trust-flavoured questionnaire. The authors report this and note it was resolved in experiment 2.
- **Two dependency items in experiment 1 barely worked.** Their statistical loadings were 0.109 and 0.489, where 0.7 is a common minimum. An item loading at 0.109 is contributing almost nothing but noise to the score.
- **No manipulation check.** Nobody verified that participants actually noticed the errors. The authors chose this deliberately, reasoning that asking would contaminate the trust measure, and list it as a limitation. It is a defensible trade and it means we do not know whether the null highlighting result reflects people looking and not caring, or never looking.
- **Trust was stated, not acted on.** Participants rated agreement with sentences. Nobody had to decide anything, follow the instructions, or seek a second opinion. The paper is explicit that behavioral outcomes were out of scope.
- **The task is nothing like real use.** Participants saw the AI text next to the correct original. Anyone who reads both carefully can find the errors by comparison. In actual use there is no correct version sitting alongside, which arguably makes the real-world problem much worse than measured here.
- **A single exposure cannot observe a habit forming.** "Learned dependency" is by definition something that develops over repeated use, and this design captures one moment.
- **The bolding intervention was narrow,** which the authors say clearly: they used bold text only, and the null result should not be read as evidence that richer cues like confidence indicators or uncertainty displays would also fail.
- **What this study did well:** stated all five hypotheses with theoretical reasoning before testing; randomized by software with back-navigation disabled; used five source texts so one stimulus could not drive the result; replicated in a different population with a deliberately strengthened manipulation; ran factor analysis on both scales, removed weak items, and published which ones; tested and *reported failing* discriminant validity in the first experiment rather than burying it; checked for questionnaire artifacts, multicollinearity, and straight-line responding; obtained ethics approval and used clinical text under a formal data agreement; followed reporting checklists for both online surveys and randomized trials; and wrote nine limitations that name most of the problems above.

# Statistics Spotlight

**1. Interaction effects — when the size of one thing's effect depends on another thing.**
- *What it is:* A main effect answers "does accuracy change trust?" An interaction answers a different question: "does the effect of accuracy on trust change depending on who is looking?" A negative interaction means the first effect shrinks as the second variable grows.
- *How this paper used it:* The whole argument rests on one number, reported twice. The interaction between accuracy and dependency was −0.399 in experiment 1 (interval −0.695 to −0.104) and −0.459 in experiment 2 (interval −0.577 to −0.340). Both are negative, both exclude zero. Read the sign: as dependency goes up, the benefit of the text being accurate goes *down*.
- *The theory, with a worked example:* Imagine testing whether adding salt improves soup. On average, yes. Now suppose you also measure how bad each taster's cold is. Among healthy tasters the salted soup scores much higher; among badly congested tasters the two soups score about the same. Salt still works. The *detection* of salt is what the cold destroys. That is exactly the shape of this finding: accuracy still matters, but heavy AI users have, in effect, a head cold about it. Note the crucial thing this does not say — it does not say dependent people trust AI less, or more, on average. That is the separate main effect, and it went in the opposite direction: they trusted it more overall while distinguishing less. Those two facts together are the definition of poorly calibrated trust.
- *Watch out:* Interactions are the least stable results in statistics and need far more data than main effects to pin down reliably. Textbook guidance is that detecting an interaction can require several times the sample needed for a main effect of the same size. That is a large part of why interaction findings so often fail to replicate, and why this paper's decision to run the whole thing twice is the right instinct. When you see a headline of the form "X only works for certain people," ask whether that split was predicted beforehand or discovered afterwards, and whether anyone has reproduced it. Here it was predicted in advance and reproduced, which is about as good as this kind of claim gets.

**2. A null result that means something — and how to tell.**
- *What it is:* Most findings of "no effect" are uninformative, because a study too small or too weak to detect anything will find nothing whether or not something is there. Occasionally a null is genuinely informative. The difference lies in whether the study could have found an effect had one existed.
- *How this paper used it:* Highlighting did nothing, twice. In experiment 1 its effect was 0.149 with an interval from −0.622 to 0.920 — a wide interval, so this null on its own is weak. In experiment 2 the effect was 0.013 with an interval from −0.074 to 0.101, which is both centred on zero and narrow. And critically, the second experiment used a *stronger* treatment: six bolded errors rather than three, with every error highlighted. The authors argue that failing to find an effect after doubling the dose is meaningful, and on this specific point they are right.
- *The theory, with an analogy:* Searching a room for your keys and not finding them tells you nothing if you glanced for five seconds. It tells you a lot if you searched for an hour with a torch. Sample size and treatment strength are the torch. In experiment 1 the interval spanned from a meaningful negative effect to a meaningful positive one — that is a five-second glance. In experiment 2 the interval is squeezed close to zero, meaning the study could have detected even a small effect and did not. **The width of the confidence interval, not the p-value, is what tells you whether a null is worth anything.**
- *Watch out:* Two opposite errors. First, treating any "no significant difference" as proof of no difference — usually wrong, and the reason "not significant" and "no effect" are different sentences. Second, and rarer, dismissing a well-powered null as a failed study. Nulls like this one are findings. Here the finding is practical and slightly depressing: the cheap interface fix that every product team would reach for does not work. The authors are careful to bound it, noting their result applies to bold text and not to richer interventions they did not test.

**3. Construct validity — proving your questionnaire measures what you say it does.**
- *What it is:* Trust and dependency are not things you can weigh. You measure them by asking several questions and combining the answers. That raises a problem nobody has when measuring blood pressure: how do you know your set of questions captures the thing you named, and not something else?
- *How this paper used it:* Extensively, and with a result that cuts against them. Several checks were run. One asks whether the questions in a scale hang together — the trust scale scored 0.724 in experiment 1 and 0.796 in experiment 2, both above the usual 0.7 floor. Another asks whether two supposedly different scales are actually different. **In experiment 1 that check failed.** The correlation between trust and dependency was 0.697, above the threshold, which means the two questionnaires were not empirically distinguishable in that sample. In experiment 2, after refining both scales, it passed at 0.643.
- *The theory, with an analogy:* Suppose you build a questionnaire to measure "optimism" and another to measure "happiness," then discover people's scores on the two are nearly identical. You have not shown optimism predicts happiness. You have shown you wrote the same test twice. That is the risk experiment 1 ran into. When a study reports that variable A predicts variable B, and A and B cannot be told apart by the measurement check, the relationship may be a scale correlating with itself. This is why the authors' decision to publish the failure matters, and why experiment 2 is the one to lean on.
- *Watch out:* This applies to a huge amount of research on attitudes, satisfaction, wellbeing, burnout, and trust — anywhere the outcome is a questionnaire. Two questions worth asking of any such paper: does it report reliability figures at all, and does it check that its separate concepts are actually separate? Many do the first and skip the second. And notice the broader point for reading any study: a statistically significant relationship is only as meaningful as the measurements underneath it. No amount of correct arithmetic rescues a number that was measuring the wrong thing.

# Jargon Translator

- **Generative AI (GenAI):** systems like ChatGPT that produce text in response to a prompt.
- **Trust calibration:** matching how much you trust a system to how reliable it actually is. Trusting a good system and doubting a bad one are both well calibrated.
- **Overreliance / automation bias:** accepting a machine's answer without checking, especially when you believe the machine is competent.
- **Learned dependency:** the paper's central term — habitual reliance on AI built up through repeated use, at the cost of independent evaluation.
- **Cognitive offloading:** handing a mental task to an external tool and gradually doing less of it yourself.
- **Randomized controlled experiment:** participants are assigned to conditions by chance, so differences between groups can be attributed to the condition.
- **Between-participants design:** each person experiences only one condition, rather than all of them.
- **2 × 2 factorial:** two variables, each with two settings, producing four combinations.
- **Moderator:** a variable that changes how strongly two other things are related. Dependency is the moderator here.
- **Interaction term:** the part of a statistical model that tests for moderation.
- **Mean-centering:** subtracting the average from a variable before building interaction terms, a routine step to keep the model stable.
- **Regression coefficient (β):** how much the outcome moves for a one-unit change in the predictor.
- **Confidence interval:** the range of values consistent with the data. An interval crossing zero means the study cannot rule out no effect.
- **Likert scale:** the familiar strongly-disagree to strongly-agree response format. Five points here.
- **Cronbach's alpha / composite reliability:** measures of whether questions in a scale hang together. Above about 0.7 is the usual minimum.
- **Average variance extracted (AVE):** how much of a scale's variation comes from the concept it is meant to measure. 0.50 is the usual threshold.
- **Discriminant validity:** the check that two scales measure genuinely different things. It failed in experiment 1.
- **Confirmatory factor analysis (CFA):** the statistical procedure used to test whether questionnaire items behave as intended.
- **Manipulation check:** a test confirming participants noticed the thing you changed. Deliberately not done here.
- **MIMIC-III:** a large, de-identified database of real intensive care records, widely used in research and the source of this study's texts.
- **Amazon Mechanical Turk (MTurk):** an online platform where people complete small paid tasks, commonly used to recruit study participants.

# What You Can (and Can't) Say

**Fair to say:**
- "Two randomized experiments with 338 and 563 participants found that people who reported relying more heavily on AI showed a weaker ability to distinguish accurate from deliberately corrupted AI-generated health summaries."
- "Heavier AI users also reported higher overall trust in AI output, so they trusted more while discriminating less."
- "Bolding the key text had no measurable effect on trust in either experiment, including when the number of highlighted errors was doubled."
- "The authors report that in their first experiment, the trust and dependency questionnaires could not be statistically distinguished from each other."
- "The study measured stated trust immediately after a single exposure, not behavior or health decisions."

**Not fair to say:**
- "Using AI makes you worse at spotting misinformation" — dependency was measured, not assigned. The study cannot separate AI use causing poor discrimination from poor discriminators using more AI.
- "Highlighting doesn't help people catch AI errors" — the finding applies to bold text in this setup. The authors explicitly say richer cues, such as uncertainty indicators, were not tested.
- "AI-dependent people can't tell accurate from inaccurate health information" — the effect is a weakening of the difference, not its disappearance, and it is an average across people.
- "This shows consumers are being harmed by AI health information" — nobody made a health decision, followed any instruction, or came to any harm in this study.
- "The results replicated" — the directions replicated. The effect sizes differed by up to a factor of ten between the two experiments, which the paper does not address.

# Bottom Line for Your Life

Twenty-four papers in, this is the one pointed at the reader rather than the machine.

Its claim, stated at the strength the evidence supports: among people who report leaning heavily on AI, the gap in trust between a correct medical summary and a deliberately corrupted one gets noticeably smaller. Not gone. Smaller. And those same people trusted the AI more to begin with. Trusting more while checking less is the exact shape of a bad habit.

Two honest caveats before you take that personally. The study cannot tell you which way the arrow runs — it may be that people who do not scrutinise things gravitate to tools that do the thinking for them. And the participants were business undergraduates and crowdworkers doing a ten-minute task for credit or fifty cents, which is not a person at 2am reading about their own test results.

What the study does establish cleanly, because this part was randomized, is that the obvious fix failed. Bolding the important sentences changed nothing, twice, even with twice as many errors marked. Surface cues do not restore attention that has already been handed over. Whatever the solution is, it is not typography.

The practical version of this, for using any AI on a health question: the thing that protected the careful participants was that the correct text sat right beside the AI's version. You will not usually have that. So build your own — check the claim against one independent source you already trust, especially when the answer arrives fluent, fast, and exactly in the shape you were hoping for. Fluency is the part these systems are best at, and it is not evidence of anything.

One study is one data point, and this is two studies that agree on direction and not on size. This is an educational breakdown, not medical advice.

---

**Sources** (based on articles retrieved from PubMed and PubMed Central; identifiers verified against the live PubMed/NLM record — URL browsing is blocked in this environment, so links are constructed from that verified record):
- DOI: https://doi.org/10.2196/98326
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42747973/ (PMID 42747973)
- Full text (PMC, open access): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC13580606/
