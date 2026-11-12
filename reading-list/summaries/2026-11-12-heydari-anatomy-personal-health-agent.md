# The anatomy of a personal health agent

**Authors:** Heydari AA, Gu K, Srinivas V, Yu H, Paruchuri A, Zhang Z, Zhang Y, He Q, Palangi H, Hammerquist N, Metwally AA, Winslow B, Kim Y, Ayush K, Yang Y, Narayanswamy G, Xu MA, Garrison J, Schmidgall S, Armento Lee A, Vafeiadou J, Graef B, Galatzer-Levy IR, Schenck E, Barakat A, Perez J, Shreibati J, Hernandez J, Faranesh AZ, Rezaei N, Prieto JL, Heneghan C, Zhan J, Malhotra M, Patel S, Liu Y, Althoff T, Liu X, McDuff D, Xu XO (**forty authors** — Google Research, Mountain View; Google DeepMind; Vituity, Emeryville; Columbia University.)
**Journal:** Nature, 2026; 659(8139): 197–207 (published 21 October 2026)
**Decoded:** 2026-11-12

**Analysis basis:** **FULL TEXT** (retrieved from PubMed Central, PMC13736220) — the complete Main text, all Results sub-sections, the Discussion including the Ethical risks and Limitations sections, the Methods including the Statistical analysis and Computational cost sections, and the Ethics statement. **Every figure, every Extended Data figure, and the entire supplementary appendix are unreachable** — Supplementary Sections A–G with **Tables 1–45 and Figures 1–7**, which hold every per-rubric statistic, the harm-review figures, and **the across-rubric Holm–Bonferroni robustness-check outcomes that the paper says are reported in each table caption.** Section 4 names exactly which two claims that gap leaves unverifiable.

**Why this paper today, and a deviation I am flagging rather than burying.** This paper was **deferred for 22 days** in this reading list because PubMed Central held no body text for it. **Today it does** — PMC13736220 appeared, and according to PubMed the conversion that returned nothing on ten previous days now returns a PMC identifier. Separately, today was the day the list's standing twenty-one-day rule fired on the **BMJ** LLM-trial reporting review (PMID 42869550), which still has no PMC copy and would therefore be an abstract-only decode. **The daily instruction puts full text ahead of abstract-only, so I took the full text that had just become available and am moving the BMJ abstract-only decode to tomorrow.** The BMJ decode will be identical whenever it happens; this one would not have been.

**Source links (verified):**
- DOI: https://doi.org/10.1038/s41586-026-11161-8
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42907512/
- Full text used: https://pmc.ncbi.nlm.nih.gov/articles/PMC13736220/

**Basis of link verification.** Direct URL fetching is blocked from this session (`doi.org` does not resolve under the network policy here), so verification was done against the live PubMed/NLM record. According to PubMed, a query for PMID 42907512 returned this exact title, these forty authors with these affiliations, *Nature* volume 659 issue 8139 pages 197–207, publication date 21 October 2026, and DOI `10.1038/s41586-026-11161-8`; a PMID-to-PMCID conversion returned **PMC13736220**; and the full text was then retrieved from PubMed Central by that PMC ID and matches the record. Both halves of the chain were confirmed independently.

**Ethics: fully reported, with three numbered protocols.** The **WEAR-ME** study was approved by **Advarra IRB #Pro 00074093**; the retrospective symptom-case collection for the domain-expert agent by **Advarra IRB #GH-SCD-001**; and the health-coach and integrated-system user studies by **WCG IRB #20244970**. Informed consent was obtained from all participants, with e-consent for WEAR-ME data use in research and publication.

**Funding, competing interests, data availability and code availability: not reportable from what I retrieved.** The extraction left only Nature's standard "Online content" pointer stating that author contributions, competing interests and the data and code availability statements "are available at" the article. **I am not reporting them, because I have not seen them.** This matters more than usual here, because **the paper repeatedly describes an "open-source agent implementation" and an openly released benchmark, and the repository address is in the statement I cannot read.** Readers should go to the article for it.

**Reporting guideline:** a **Nature Portfolio Reporting Summary** is referenced and deposited. No TRIPOD, DECIDE-AI or CONSORT variant is named — Section 4 places that in a now five-entry sequence.

---

## 1. The Gist

**Forty authors at Google built a health chatbot out of three specialist chatbots and a manager, then spent 1,350 hours of human effort finding out whether it was any good. The answer is interesting, and the two most important numbers in it are not in the abstract.**

The system is called the **personal health agent**, and its design premise is a genuine insight. Personal health questions are not one kind of question. *"How did my steps affect my resting heart rate last month?"* needs arithmetic on time-series data. *"What are the pros and cons of HIIT?"* needs factual grounding. *"How do I actually get myself to bed earlier?"* needs the skills of a coach. The authors found that **one model trying to do all three does all three worse**, so they built three — a **data science agent** that writes and runs Python on your wearable data, a **domain expert agent** that searches the literature and reads your blood tests, and a **health coach agent** trained on motivational interviewing — with an **orchestrator** that decides who answers and stitches the replies together.

**The evaluation is the largest in this reading list by a wide margin:** 11 benchmark tasks, **more than 7,000 human annotations**, and **1,350 hours** of assessment split almost evenly between **651 hours of end users and 699 hours of health experts**, grounded in a real cohort of **1,165 people** who wore Fitbits, filled in questionnaires and gave blood.

**And the integrated system won.** End users ranked it first **46.7%** of the time against 28.9% for a parallel version and 24.4% for a single-agent baseline. Experts ranked it first **66.7%** of the time.

**Now the two numbers that deserve to be in the abstract and are not.**

**First: experts saw about three times as much improvement as the people actually using it.** Across the integrated evaluation, the system's advantage over the baselines averaged **17.1% as judged by health experts and 4.6% as judged by end users.** The same gap appeared independently in the coaching study (**10.2% versus 3.5%**). And on one dimension — *user empowerment* — **experts preferred the new system 69.9% of the time while end users split it 48.4%, a coin flip.** The paper reports this and calls it a reason to use both rater groups. **The sharper consequence is that for a consumer product, the end-user number is the one that governs whether anybody benefits.**

**Second: the safety review found real harm.** Five clinicians reviewed the health summaries the domain-expert agent wrote for 30 real participants. **83% carried no or minimal potential harm. 15% carried mild harm. 2% carried moderate-to-severe harm.** The authors' own words are that these are "non-trivial," and they flag it in the Discussion. **Seventeen percent of the summaries had some potential to hurt someone**, and Section 5 works through what a 2% rate means if something like this reaches consumer scale.

**One more figure worth knowing before anyone gets excited: 205 seconds.** That is how long the system takes, on average, to answer one question — **three and a half minutes**, against 36 seconds for the simple single-agent version that end users ranked only 22 points behind it.

**What the paper does not claim, and says so plainly:** that it helps anyone's health. *"Our evaluation provides evidence of conversational quality and short-term task efficacy, not sustained behavioural change or improvement in longitudinal health outcomes."*

## 2. Study Snapshot

**Study type:** a **system-development and capability-evaluation study** — an engineering paper with an unusually large human-evaluation programme attached. **No clinical outcome, no longitudinal follow-up, no randomised deployment.** Several components are blinded, counterbalanced randomised comparisons *of conversational quality*.

**The source cohort.** All personal-data evaluations are grounded in **WEAR-ME (Wearables for Metabolic Health), n = 1,165**. Consented participants linked a Fitbit account to Google Health Studies, authorising wearable collection for the study duration **and up to three months before joining**; completed questionnaires on demographics, health history and personal health insights; **attended a blood draw at a Quest patient service centre**; and wore a Fitbit or Pixel Watch day and night **for at least three of every four days.** The paper reports data-quality validation — "filtering users with short or unreliable wearing periods, and high missing data rates." **Medical records were limited to blood test results "because of protocol-level data access constraints."**

**How the four user needs were derived.** A user-centred design process synthesising **1,370 consumer health queries** from search engines and health forums, **health goal surveys from 555 users**, and a design workshop with **14 UX and engineering experts**. This produced four **critical user journeys** — general health knowledge, personal data insights, wellness advice, and personal medical symptoms — and **26 query sub-types** mapped to primary and supporting agents.

**The architecture.** Three specialists plus an orchestrator. The **data science agent** uses a two-stage design: generate a structured natural-language analysis plan, then translate it into executable Python with an **iterative self-correction loop**. The **domain expert agent** runs a multi-step reason-and-act loop over a tool suite including **web search, the NCBI API, the DataCommons API and a Python sandbox**. The **health coach agent** is grounded in **motivational interviewing**, separating a core personalised coaching module from specialised conversation-flow modules. The **orchestrator** decomposes queries, assigns tasks, and synthesises outputs "through an iterative reflection process," with a **persistent memory module** for conversational context. **Base model: the Gemini 2 family (Flash/Pro).** The paper states that "our focus is not to train a new LLM but to design and construct the agentic system around a given base LLM."

**Results, by component.**

*Data science agent — analysis plans.* Scored against an expert rubric on six prespecified dimensions (timeframe, data transforms, data sufficiency, summary statistics, statistical tests, overall alignment), using an **LLM autorater validated against 354 annotations from 10 expert data scientists, ICC(3,1) = 0.838**. The agent scored **75.6 ± 1.4% against the baseline's 53.7 ± 1.8%** (p<0.001, effect size 0.925, Wilcoxon signed-rank). The standout: **data availability rose from a near-failure 5.3 ± 1.6% to 66.5 ± 3.7%** — the paper attributes this to "a well-documented LLM weakness in detecting missingness and artefacts." **Statistical tests showed no significant difference**, a dimension where the baseline already did well.

*Data science agent — code.* Against **173 unit tests written by 7 data science experts across 25 query–plan pairs**: a **75.5 ± 3.3% first-attempt pass rate against Gemini's 58.4 ± 3.7%** (χ² = 26.3, p<0.001, McNemar's), rising to **79.0% after up to five self-correction trials**. Data-handling errors — "which typically render the entire pipeline unusable" — **fell from 25.4 ± 3.3% to 11.0 ± 2.4%** (χ² = 12.3, p<0.001). Gains were verified to generalise to other state-of-the-art LLMs, **indicating the architecture is model-agnostic.**

*Domain expert agent — factuality.* On **more than 2,000 expert-level multiple-choice questions** from board certification and coaching examinations across endocrinology, cardiology, fitness and sleep medicine: **83.6% against 81.8%** (χ² = 9.51, p = 0.002, OR = 1.67).

*Domain expert agent — diagnosis.* On **2,000 retrospective real-world consumer health cases** of common self-reported symptoms, it beat a Gemini 2.0 Pro-based state-of-the-art differential-diagnosis agent (p<0.001, effect size 0.156), reaching **top-one accuracy of 46.1%**, a **+4.7 point** gain, with consistent gains at top-five and top-ten.

*Domain expert agent — personalisation.* **50 curated personalised questions**, judged by **17 end users** in a blinded study with Boolean rubrics and side-by-side rankings (**Fleiss' κ ≥ 0.684**). The largest gap was **trustworthiness: 96.9 ± 0.8% against 38.7 ± 3.3%** (p<0.001, effect size 6.873). **Relevance to query and groundedness in data were comparable across systems.** Side-by-side, users preferred the agent on personalisation and contextualisation (**71.9 ± 1.5%**) and citation credibility (**76.9 ± 1.5%**), both p<0.001.

*Domain expert agent — multimodal summaries, and the safety review.* Unstructured text, structured wearable data and **PDF laboratory results from 30 WEAR-ME participants**, synthesised into health summaries and judged blind by **five expert clinicians**. The agent beat the base model on clinical significance (**96.4% vs 73.8%**), cross-modal association (**79.4% vs 50.0%**), comprehensiveness (**96.4% vs 64.2%**) and citation credibility (**77.6% vs 42.7%**), all p<0.001. Clinicians preferred its summaries on comprehensiveness (**93.3%**) and trustworthiness (**82.4%**). On overall clinical usefulness, **65% were rated useful or very useful against 30%** for the base model. **And the safety review: 83% no or minimal potential harm, 15% mild harm, 2% moderate-to-severe harm** — the paper's words, "although they are non-trivial," with the concern carried into the Discussion.

*Health coach agent.* Six design themes from a formative interview study with **11 health experts**. Then **31 participants** in blinded counterbalanced sessions against a baseline on the same base model, using the chatbot usability questionnaire, the Working Alliance Inventory, client evaluation of motivational interviewing, and SMART goal-setting instruments. Significant advantages on conversation flow, motivational interviewing and feedback handling; **preferred on five of six themes with win rates of 61–71%**, significant on active listening (p = 0.025); **more natural conversation endings, 83.9% against 74.2%.** **The one exception: the baseline scored higher on progress measurement.** Then **3 health experts** re-rated the same transcripts: the agent won on nearly every dimension (**Δ = 7–16%**, all p<0.001 except clarity), with **win rates 64.5–72.0%** across all six themes. **The expert-perceived advantage was much larger than the end-user-perceived advantage: 10.2 ± 1.2% against 3.5 ± 2.5%.** And a flat disagreement on **user empowerment** — experts 69.9% win rate, **end users 48.4%.** Experts also gave the baseline the edge on progress measurement.

*The integrated system.* Compared against **two strong baselines** — a capable single-agent system (**PHIA**, from previous published work) and a **parallel multi-agent** version where the three specialists answer independently — judged by **45 end users** covering all WEAR-ME persona profiles, plus **3 health experts**. End users ranked the integrated system first **46.7%** (overall preference) and **44.4%** (response quality), against parallel's 28.9%/31.1% and PHIA's 24.4%/24.4%. It "numerically outperforms both baselines on every rubric," reaching significance on **personalised coaching (p<0.001), natural conversation (p = 0.002), user empowerment (p = 0.032) and overall quality (p = 0.044)**, plus data science analysis against the parallel system (p = 0.016). Experts rated it **72.8 ± 1.4% against 64.3 ± 1.3% and 54.4 ± 1.4%** (all pairwise p<0.001), with the advantage "extending across nearly all **17** individual rubrics," and ranked it best in **66.7%** of conversations on overall quality and **62.2%** on effectiveness.

*A scaled synthetic replication.* **50 WEAR-ME personas** drove **150 multi-turn conversations (50 × 3)** between persona-instructed user LLM agents and the three systems, rated by a separate cohort of **20 end-user generalist evaluators and 5 health experts** on the same rubrics, with "consistent patterns."

**Computational cost, from the Methods.** Single-agent PHIA: **3.0 LLM calls per round, 36.4 ± 1.6 s**. The integrated system: **6.5 calls, 205.3 ± 15.0 s**. Parallel multi-agent: **7.0 calls, 244.4 ± 11.4 s**.

**Statistical handling, reported in detail and worth quoting.** GLMM with a log link, **system as fixed effect and rater (and conversation script where applicable) as random effects**; pairwise contrasts by **Tukey's honest significance test**; each rubric "treated as a confirmatory test of a pre-specified, conceptually distinct quality dimension"; **plus an across-rubric Holm–Bonferroni robustness check whose outcome "has been reported in the caption of each corresponding result table"**; rankings by **Friedman omnibus then post-hoc Wilcoxon with Holm–Bonferroni**; **effect sizes and confidence intervals alongside p-values; all tests two-sided.**

**Limitations the authors state themselves:** evidence of "conversational quality and short-term task efficacy, **not sustained behavioural change or improvement in longitudinal health outcomes**"; partial reliance on **LLM autoraters**, which "can be sensitive to ordering, formatting, length and source"; **WEAR-ME is Fitbit-centric**, limiting device generalisability; **"condition-stratified participant matching on WEAR-ME was intended to increase scenario relevance but cannot eliminate perspective-taking bias,"** with the recommendation that longitudinal studies "recruit people **responding as themselves**"; the need for evaluation "across devices, languages, literacy levels and demographic groups, including older adults and people with disabilities"; and the **computational burden**, with the figures above.

**And an ethical-risks section with concrete proposals:** that the system "is a research prototype for consumer wellness, not a diagnostic or clinical triage system, and should not replace professional care"; that health agents "risk reinforcing disparities when their models or evaluation data underrepresent populations"; that future versions should add **persistent cross-turn notices, high-risk query detection, and explicit handoff to a clinician** so the system "does not delay care"; that open-web retrieval "creates a related risk of conflicting or low-quality evidence," so deployment should **restrict retrieval to curated sources such as WHO, PubMed, NICE and CDC and display source provenance beside each recommendation**; and that real-world deployment "requires systematic code validation and standardized privacy and security controls."

**Not reported or not reachable:** all figures and the entire supplementary appendix (Sections A–G, Tables 1–45, Figures 1–7), including every per-rubric statistic and **the Holm–Bonferroni robustness-check outcomes**; the data, code and competing-interests statements; the repository address for the open-source implementation; whether the 2% moderate-to-severe harm figure is a proportion of summaries or of ratings.

## 3. How Strong Is This Evidence? (Grade 3 out of 5)

**The engineering and the evaluation programme deserve a 4. What caps the grade at 3 is that nobody has shown this helps anyone's health — and that the one capability the architecture exists to deliver was tested on people reasoning about strangers' data.**

**What earns real credit.**

**The evaluation is the largest and most carefully instrumented in this list.** 11 tasks, 7,000+ annotations, **1,350 hours split 651 end-user and 699 expert** — and that split matters, because most AI-in-health papers evaluate with one group or the other.

**The statistics are handled properly, including the multiplicity.** GLMM with **rater and conversation script as random effects** is the correct structure for repeated ratings of the same transcripts. Tukey for pairwise contrasts. Prespecified confirmatory rubrics. **And an across-rubric Holm–Bonferroni robustness check, run and reported.** This reading list has spent weeks noting the absence of exactly this; here it is present, and Section 4 identifies precisely which claims it decides.

**Three IRB protocols with numbers, and informed consent throughout.** Including e-consent for the wearable and blood data.

**The baselines are strong and fairly chosen in one important respect:** the parallel multi-agent comparison isolates *orchestration* from *having three specialists*, which is the right ablation for the paper's actual claim.

**Model-agnosticism was checked**, not assumed — the data science and domain expert gains were verified to generalise to other state-of-the-art LLMs.

**The autorater was validated against humans before being used**, with a reported **ICC(3,1) = 0.838**, and the paper says autorater conclusions "should remain cross-checked against blinded human judgements."

**They ran a safety review and published the bad numbers.** 15% mild and 2% moderate-to-severe potential harm, described as "non-trivial" and carried into the Discussion. **A team that wanted a clean paper would not have run that review, and having run it would not have foregrounded it.**

**The ethical-risks section is specific rather than ritual** — curated retrieval sources named, provenance display, high-risk detection, clinician handoff, HIPAA and GDPR controls.

**And the central claim is bounded accurately:** conversational quality and short-term task efficacy, explicitly not behavioural change or health outcomes.

**What holds it to 3.**

**No outcome, of any kind.** Nobody slept better, moved more, or caught a condition earlier. For a system whose purpose is behavioural change, the absence of behavioural data is the whole ceiling — and the authors say so.

**The personalisation findings were produced by people evaluating personalisation to someone else.** This is the most consequential thing I found. The live studies used **condition-stratified matching to WEAR-ME personas**, and the paper's own limitation is that this "cannot eliminate perspective-taking bias," with longitudinal work needing people "responding as themselves." **So the headline judgements — trustworthiness 96.9%, personalisation preference 71.9%, personalised coaching p<0.001 — were made by participants reasoning about a stranger's wearable data and blood tests.** Personalisation is the one capability this architecture exists for. It has not yet been judged by anyone whose own data was in play.

**The claims that matter most rest on the smallest samples.** The large numbers are automated or retrospective — 2,000 MCQs, 2,000 diagnosis cases. The live studies are **17, 31 and 45 end users**, and **the paper's strongest single result — experts rating the integrated system 72.8% against 64.3% and 54.4%, all pairwise p<0.001 — comes from three health experts.** Three.

**Google built it, Google's model runs it, Google evaluated it.** Forty authors, nearly all from Google Research and Google DeepMind. The structural safeguard of independent evaluation is absent, and the open-source release is the right partial remedy — though the repository address sits in a statement I could not retrieve.

**Two findings sit on the edge of the multiplicity correction the paper itself ran.** Section 4 names them.

**And 205 seconds.** Three and a half minutes per answer is not a detail; it is the difference between a research prototype and a product, and the Results section frames the cost comparison against the slower baseline rather than the faster one.

**Why not 4.** Because the grade in this list tracks what a reader may conclude, and what a reader may conclude here is that a well-built prototype produces conversations that experts like considerably and users like slightly, with unknown effect on health and a measured potential for harm in roughly one summary in six. **Why not 2.** Because the evaluation programme is genuinely exemplary, the statistics are right, the safety review was run and published, and the paper's own stated claim matches its own evidence.

## 4. The Editor's Concerns

**1. Experts saw three times the improvement users did, and the paper draws the gentler conclusion.** Measured twice, independently: **17.1% average expert delta against 4.6% end-user delta** in the integrated study; **10.2% against 3.5%** in the coaching study. Plus the outright reversal on user empowerment — **experts 69.9%, users 48.4%.** The paper calls this "the value of incorporating both perspectives," which is true and insufficient. **For a consumer product the end-user delta is the one that governs whether anyone benefits**, and it is 4.6%. The expert delta establishes that the system is better by expert standards; it does not establish that users will notice it, prefer it, or act on it. This is the same lesson as entry 68's finding that a model scoring 94.9% alone produced **zero measured benefit** once a human was in the loop — and the same structure as technique 229. **The thing being deployed is the system plus the user, and the user's perception is part of the system.**

**2. The 2% is the number that decides whether this ships, and it is not in the abstract.** Five clinicians, 30 participants' summaries: **83% no or minimal harm, 15% mild, 2% moderate-to-severe.** So **17% of summaries carried some potential to hurt someone.** Section 5 does the scale arithmetic. The authors ran the review, called the figures non-trivial, and discussed them — all to their credit. **But a consumer wellness product's harm rate belongs beside its usefulness rate**, and "65% rated useful or very useful" made the abstract while "2% moderate-to-severe" did not.

**3. Personalisation was evaluated by people personalising to a stranger.** Covered in Section 3 and worth restating as a concern rather than a caveat: **the paper's distinctive capability has not been tested on anyone whose own data was in play.** The disclosure is exemplary; the gap is central. Until someone runs this on participants' own wearables and blood results, **the personalisation findings measure whether the output reads as personalised, not whether it is.**

**4. Three health experts carry the paper's strongest claim.** The integrated expert evaluation — 72.8% against 64.3% and 54.4%, all pairwise p<0.001 — rests on **three raters.** The GLMM treats rater as a random effect, which is the right structure and does not manufacture raters. With three, the between-expert variance is estimated from two degrees of freedom. The synthetic replication added five more experts and found "consistent patterns," which helps. **The headline comparison in a Nature paper should not depend on three people's judgement, however expert.**

**5. Two findings sit exactly where the correction bites, and I cannot check which way it went.** The expert evaluation spans **17 rubrics**; a naive Bonferroni threshold would be **0.05/17 = 0.0029**. Of the end-user integrated findings: personalised coaching (p = 0.001) and natural conversation (p = 0.002) clear it; **user empowerment (p = 0.032), overall quality (p = 0.044) and the data-science contrast (p = 0.016) do not.** The paper **ran** an across-rubric Holm–Bonferroni robustness check and reports the outcome "in the caption of each corresponding result table" — captions inside the supplementary material I could not retrieve. **So: the check exists, which is more than most papers manage; I cannot verify its result; and these three claims are the ones whose status it decides.** A reader should treat "significant on user empowerment and overall quality" as provisional until they read those captions.

**6. The cost framing picks the flattering comparison in the Results and the honest one in the Discussion.** Results: the system "requires fewer LLM calls and responds faster than the parallel multi-agent baseline… delivers superior user experience with greater computational efficiency." True — **1.19× faster than parallel.** Discussion and Methods: **205.3 s against 36.4 s for the single agent, 5.64× slower, with 2.17× the LLM calls.** And end users ranked that single agent only 22 points behind. **A reader who stops at the Results heading "Relative computational cost advantage" will not learn that the system takes three and a half minutes to reply.**

**7. The baseline beat it on progress measurement, twice, and then the design changed.** Both end users and experts gave the baseline the edge on progress measurement, and the paper says it "explicitly address[es] this in the integrated PHA design." **Honest, and it means the coaching comparison and the integrated comparison are not evaluating the same artefact** — a known weakness was fixed between studies. That is good engineering and it makes the two sets of numbers non-comparable in that one respect.

**8. Two headline metrics read differently as their complements.** **Top-one diagnostic accuracy of 46.1%** means **the correct condition was not the first suggestion in 53.9% of cases** — on common, self-reported symptoms. The paper reports it as +4.7 points over prior state of the art, which is the fair framing for a methods contribution and not the one a user needs. And **factuality of 83.6% against 81.8% is a 1.8-percentage-point gain**, reported alongside **OR = 1.67** — a correct statistic for paired data that a reader may easily take as "67% better." Section 5 unpacks it.

**9. Google built it, Google's model runs it, Google evaluated it.** Forty authors, nearly all from Google Research and Google DeepMind, with one at Vituity and one at Columbia. No independent evaluation, and the base model is the sponsor's own. **The open-source release of implementation and benchmark is exactly the right remedy** — and the paper's framing is unusually modest about it: "We do not aim to claim that our configuration is universally optimal… we intend this work as a reusable foundation for the community to critique, swap in different agents or base models, and build stronger PHAs." **That invitation is worth something only if the code is findable, and the availability statement is in the part I could not read.**

**10. No reporting guideline named, completing a five-entry sequence.** A Nature Reporting Summary is deposited, which is the journal's own instrument. But **DECIDE-AI** exists specifically for early-stage live clinical evaluation of AI decision-support systems, and this is early-stage live evaluation. The running tally: entry 69 named TRIPOD+AI with the checklist; entry 70 named STROBE; entry 71 named none; entry 73 named none and called for a checklist that does not exist; entry 74 named none while doing more of what TRIPOD+AI asks than any of them; **and entry 75 names none while running the best multiplicity treatment in the list.** Five consecutive entries, and the correlation between naming a checklist and following good practice is now reliably near zero. **Read the methods.**

**11. Credit for a sentence that cost the authors something.** On symptoms, the paper could have claimed a triage capability. Instead: the architecture "is not designed to offer definitive medical diagnoses or replace the judgement of a qualified health-care professional. **Yet simply deferring such questions to clinicians may not address the delays that often motivate people to seek artificial intelligence support.**" And then a concrete alternative — help users record symptoms, spot patterns, prepare questions and navigate care **without diagnostic claims**. That is a harder and more useful position than either "it can triage" or "ask your doctor," and it is the most thoughtful paragraph in the paper.

## 5. Statistics Spotlight

Ten techniques, numbered from 254 in the running list in `queue.md`. The first three are the load-bearing ones.

**When experts and users disagree about how much better something is, the user's number is the one that predicts whether it works.**

This paper measured the same quantity twice, in two separate studies, with two separate rater groups, and got two very different answers:

- Coaching agent: **experts perceived a 10.2 ± 1.2% advantage; end users perceived 3.5 ± 2.5%.** Ratio **2.9×**.
- Integrated system: **expert deltas averaged 17.1%** (range 5.7–39.0%); **end-user deltas averaged 4.6%** (range 1.6–15.4%). Ratio **3.7×**.
- And on *user empowerment*: **experts preferred the new system 69.9% of the time; end users 48.4%** — statistically indistinguishable from flipping a coin.

**Why the gap is real and not a measurement artefact.** Experts are trained to see things users cannot: whether a coaching conversation actually used motivational interviewing technique, whether a SMART goal was properly specified, whether a data analysis handled missingness. The paper says this directly — experts "identified major quality differences that, although not immediately apparent to end users, are fundamental to providing safe and robust guidance."

**And here is the consequence the paper does not spell out.** A consumer health app changes someone's health only if that person **uses it, trusts it, and acts on it.** All three depend on what the *user* perceives. **An improvement visible only to experts is a real improvement in craft and a near-invisible one in effect.** The 17.1% tells you the engineering got better. The 4.6% tells you how much of that reached the person.

**The everyday version.** A professional sommelier can reliably distinguish a £15 wine from a £60 one and will tell you the difference is large. Most guests at the dinner party cannot. **Both reports are accurate.** If your goal is to win a tasting competition, buy the £60 bottle. **If your goal is for your guests to enjoy the evening more, you have paid £45 for something they will not notice** — and you need the guests' judgement, not the sommelier's, to know that.

**Watch out for:** a paper that reports expert ratings prominently and end-user ratings in a supplement, or that pools them. **Ask which group's judgement determines whether the intervention works in the real world, and look up that group's number.** For clinician-facing tools, the clinician is the user and the expert — so this gap does not arise. For consumer tools it is the central measurement problem, and this paper is the clearest demonstration of it in this list precisely because it measured both.

**A harm rate is a rate. Multiply it by the deployment.**

The safety review here is small and the finding is large: five clinicians reviewed health summaries for 30 participants and judged **83% no or minimal potential harm, 15% mild, 2% moderate-to-severe.**

Those percentages are easy to read as reassuring — 83% is most of them. **Rates do not stay percentages when a product ships.** Apply the reported 2% and 15% to plausible usage:

- **1,000 summaries** (one clinic's list): **20** moderate-to-severe, **150** mild
- **100,000** (one mid-sized health system): **2,000** moderate-to-severe, **15,000** mild
- **1,000,000** (a modestly popular app): **20,000** moderate-to-severe, **150,000** mild

**For calibration on what "consumer scale" means in this field, entry 68 of this reading list analysed a clinical AI platform that handled 271 million queries in 30 months.**

**Two things must be said carefully.** First, **this is not a deployment estimate** — it is the reported rate carried forward, and a shipped product would have different prompts, guardrails, disclaimers and users. Second, **harm here means potential harm from a text summary as judged by a reviewing clinician**, not a documented injury. **Neither caveat changes the shape of the problem:** a 2% moderate-to-severe rate is tolerable in a research prototype reviewed by clinicians and intolerable in a product that reaches a million people unsupervised. The authors understood this, which is why the Ethical risks section proposes high-risk query detection and clinician handoff.

**The everyday version.** A food process that spoils 2% of batches sounds like a good process. At one batch a week it is one bad batch a year. **At ten thousand batches a day it is two hundred poisonings before lunch.** The rate did not change; the exposure did.

**Watch out for:** a safety or error rate reported as a percentage with no statement of intended scale. **Multiply it out yourself, at the scale the product is aiming for**, and ask whether the resulting absolute number is acceptable. And note the direction of the incentive — **this is the one calculation a developer has no reason to publish**, which is why running the safety review at all deserves the credit this paper gets for it.

**Multiplicity across many rubrics: the two-layer approach, and how to spot which claims it decides.**

When you rate three systems on seventeen quality dimensions, you are running a lot of tests. The naive fix — Bonferroni, dividing α by 17 to get **0.0029** — is too strict, because the rubrics are correlated (a system good at natural conversation tends to be good at empowerment) and because each rubric is a genuinely separate question you prespecified.

**What this paper did, which is the right two-layer answer.** Each rubric was "treated as a confirmatory test of a pre-specified, conceptually distinct quality dimension" — so no correction *within* the primary analysis, justified by prespecification. **And then, to check that this framing was not understating the error rate, they additionally ran an across-rubric Holm–Bonferroni robustness check and reported its outcome in each table caption.** Plus: GLMM with **rater and conversation script as random effects** (so repeated ratings of the same transcript by the same person are not treated as independent), **Tukey's HSD** for the pairwise system contrasts, **Friedman then Wilcoxon with Holm–Bonferroni** for the rankings, effect sizes and CIs throughout, and all tests two-sided.

**That is the best multiplicity treatment in this reading list**, and the layering is the part worth copying: **prespecify, analyse per-outcome, then show your work under a stricter correction so the reader can see which findings depend on the framing.**

**And here is how to use it as a reader.** Take the p-values and compare them against the strict threshold yourself:

- personalised coaching, **p = 0.001** → clears 0.0029
- natural conversation, **p = 0.002** → clears 0.0029
- data science (vs parallel), **p = 0.016** → does not
- user empowerment, **p = 0.032** → does not
- overall quality, **p = 0.044** → does not

**So three of the five end-user findings are the ones a cross-rubric correction puts in question — and "overall quality" is among them.** The paper ran the check; its outcome lives in supplementary table captions I could not retrieve. **The honest position is therefore: the robustness check exists, which is to the paper's credit; I cannot verify its result; and these three claims are exactly the ones it adjudicates.**

**A tiny worked example of why the correction matters.** Rate two identical systems on 17 rubrics, by pure noise. The chance that at least one rubric shows p<0.05 is roughly 1 − 0.95¹⁷ = **58%.** More likely than not, you will find a "significant" difference between two things that are the same. **That is what a cross-rubric check protects against**, and why a paper reporting significance on 4 of 17 rubrics needs you to know which survive.

**Watch out for:** a paper reporting many rubrics, several marginal p-values, and no statement of how multiplicity was handled. **And its mirror:** a paper that applies a crushing Bonferroni to correlated prespecified outcomes and declares nothing significant. Neither extreme is right; **this paper's two-layer approach is.**

**257. An odds ratio on paired data is not a percentage improvement.** Factuality: **83.6% against 81.8%**, McNemar χ² = 9.51, p = 0.002, **OR = 1.67.** The accuracy gain is **1.8 percentage points.** The odds ratio describes the ratio of **discordant pairs** — questions where exactly one system was right — and 1.67 means the agent won about five of those for every three the baseline won. **It is the correct statistic for paired comparisons and it reads like a much bigger effect than it is.** Whenever you see an OR from a paired test, **find the two raw accuracies** — and note that the significance here comes from n exceeding 2,000, not from the size of the difference.

**258. Read a top-one accuracy as its complement.** **Top-one diagnostic accuracy 46.1%** means **53.9% of the time the right answer was not the first suggestion.** Both framings are honest; the paper's (+4.7 points over prior state of the art) is appropriate for a methods comparison, and the complement is what a person typing symptoms into a box needs to know. **The same move applies to top-five and top-ten accuracies, which sound impressive and silently concede that the first answers were wrong.**

**259. Validating an autorater, and what an ICC of 0.838 licenses.** Human evaluation at this scale is unaffordable, so the paper built an LLM autorater and **validated it against 354 annotations from 10 expert data scientists, reporting ICC(3,1) = 0.838.** The intraclass correlation measures how much of the variation in scores reflects real differences between the things scored rather than disagreement between raters. By convention, 0.75–0.90 is **good** and above 0.90 excellent. **So 0.838 licenses using the autorater to rank systems on aggregate, and does not license treating any single autorated score as a human judgement.** The paper's own guard is correct: autorater conclusions "should remain cross-checked against blinded human judgements as models and prompts change." **Watch out for** an LLM-judged benchmark with no human validation and no agreement statistic — which is exactly the gap entry 68 had, and this paper does not.

**260. Role-played personalisation measures whether output reads as personal, not whether it is.** The live studies matched participants to **WEAR-ME personas**, so people judged responses built on a stranger's wearable and blood data. The paper names the problem — **"perspective-taking bias"** — and prescribes the fix: "recruit people **responding as themselves**." **The general rule: when the capability under test is personalisation, the participant must be the person being personalised to.** Otherwise you measure plausibility of personalisation, which is a different and easier thing. This is the explanation-versus-reality distinction of technique 249 transplanted into user research.

**261. When a system sits between two baselines, note which comparison the paper leads with.** Latency: single agent **36.4 s**, this system **205.3 s**, parallel multi-agent **244.4 s**. The Results section reports the system as faster and cheaper "than the parallel multi-agent baseline" — **true, by 1.19×.** Against the single agent it is **5.64× slower.** Both comparisons are in the paper; only one is in the Results heading. **With three or more arms, check whether the headline comparison is against the nearest competitor or the most convenient one** — and look up the absolute value, because 205 seconds is a product decision and "19% faster" is not.

**262. A baseline that wins on one dimension, then gets "addressed" between studies.** The simple baseline beat the coaching agent on **progress measurement**, per both end users and experts, and the paper says it "explicitly address[es] this in the integrated PHA design." **Honest reporting, and it means the two studies evaluate different artefacts.** When a paper fixes a weakness identified in study one before running study two, **the second study's numbers cannot be compared to the first's on that dimension** — and a reader should check whether any headline claim depends on the fix.

**263. Capability evaluation and outcome evaluation answer different questions.** This paper measures **whether the conversations are good**: 11 tasks, 7,000 annotations, expert and user rubrics. It does not measure **whether anyone's health changed** — and says so: "evidence of conversational quality and short-term task efficacy, not sustained behavioural change or improvement in longitudinal health outcomes." **Both are legitimate; only one is a health claim.** The design that would answer the second is a multi-session deployment measuring engagement, adherence and behaviour over time, with people using their own data. **When a health-AI paper reports preference rankings and rubric scores, it is a capability paper, and the health question is still open.**

## 6. Jargon Translator

**Agent (in this sense)** — a language model wrapped in a loop that lets it call tools, write and run code, and take several steps before answering, rather than replying in one shot.

**Multi-agent / orchestrator** — several specialist agents plus a coordinator that decides which to use for a given question and merges their answers. The alternative tested here is a **parallel** version where all three answer independently with no coordination.

**Monolithic / single-agent** — one model doing everything. The paper's claim is that this does each sub-task worse because the objectives compete.

**Motivational interviewing** — an evidence-based counselling style built on asking rather than telling, used in behaviour change. The coaching agent is built on it, and experts rated it against instruments designed to measure it.

**SMART goal** — specific, measurable, achievable, relevant, time-bound. A standard against which coaching output can be scored.

**Working Alliance Inventory** — a validated instrument measuring the quality of the bond and agreement on goals between a client and a helper. Borrowed here from psychotherapy research to score a chatbot.

**Critical user journey** — a product-design term for a distinct kind of thing users come to do. The four here were derived empirically from 1,370 real queries plus surveys.

**Wearable time series** — the continuous stream from a watch: steps, heart rate, heart-rate variability, sleep stages.

**Autorater** — an LLM used to score outputs in place of a human, so evaluation can scale. **Only as trustworthy as its validation against humans** — technique 259.

**Intraclass correlation coefficient (ICC)** — how much of the variation in scores reflects real differences between things scored rather than rater disagreement. 0.75–0.90 is conventionally good.

**Fleiss' kappa** — agreement among three or more raters, corrected for the agreement you would get by chance. Reported here at ≥ 0.684.

**McNemar's test** — the right test when the same items are scored by two systems, because it looks only at the items where they disagreed.

**Odds ratio on paired data** — the ratio of those disagreements. **Not a percentage improvement** — technique 257.

**GLMM (generalised linear mixed model)** — a regression that handles both fixed effects (which system) and random effects (which rater, which transcript), so repeated ratings by the same person are not treated as independent observations.

**Tukey's honest significance test** — adjusts for making all pairwise comparisons among three or more groups.

**Friedman test** — a rank-based omnibus test for whether three or more systems differ when the same raters rank all of them.

**Holm–Bonferroni** — a multiple-comparison correction that is less crushing than plain Bonferroni while still controlling the family-wise error rate.

**Top-one / top-five accuracy** — how often the correct answer was the first suggestion, or somewhere in the first five. **Read the complement** — technique 258.

**Differential diagnosis** — the ranked list of conditions that could explain a presentation. Harder than naming one disease.

**DataCommons / NCBI API** — public structured-data and biomedical-literature services the domain expert agent queries as tools.

**Perspective-taking bias** — the distortion introduced when someone judges a personalised output built on data that is not theirs. The paper names it as a limitation — technique 260.

## 7. What You Can (and Can't) Say

**You can say:**

"A 40-author Google team built a modular multi-agent health assistant — a data-science agent, a domain-expert agent and a coaching agent under an orchestrator — and evaluated it across 11 tasks with more than 7,000 human annotations and 1,350 hours of end-user and expert effort, grounded in a 1,165-person cohort with wearable, questionnaire and blood-test data."

"The orchestrated system was preferred over both a single-agent and a parallel multi-agent baseline: end users ranked it first 46.7% of the time, health experts 66.7%."

"Each specialist agent improved its targeted capability — analysis-plan quality rose from 53.7% to 75.6%, first-attempt code pass rate from 58.4% to 75.5%, and clinician-rated usefulness of health summaries from 30% to 65%."

"Health experts perceived roughly three times the improvement that end users did — 17.1% against 4.6% on average."

"An expert safety review of the system's health summaries found 15% with mild potential harm and 2% with moderate-to-severe potential harm."

"The implementation and evaluation benchmark are described as openly released, and the authors explicitly invite the community to swap in different agents and base models."

**You cannot say:**

"An AI health agent improves health." **No outcome of any kind was measured.** The authors are explicit: conversational quality and short-term task efficacy, "not sustained behavioural change or improvement in longitudinal health outcomes."

"Users prefer it." They do — by **4.6% on average**, and on two of the dimensions where significance was reported the p-values (0.032, 0.044) sit where a cross-rubric correction bites, and I could not verify whether they survived it.

"It personalises advice to your data." **In the live studies, participants were matched to other people's personas** and judged personalisation to a stranger. The paper names this as perspective-taking bias.

"It can tell you what's wrong with you." **Top-one diagnostic accuracy was 46.1%** — wrong first guess more than half the time — and the paper states the architecture "is not designed to offer definitive medical diagnoses or replace the judgement of a qualified health-care professional."

"It's safe." **2% of its health summaries were judged to carry moderate-to-severe potential harm** and 15% mild, by the authors' own clinician review.

"It's more efficient than the alternatives." More efficient than the **parallel** multi-agent version. **5.6× slower than the single-agent baseline**, at 205 seconds per answer.

"Experts validated it." **Three** health experts produced the integrated expert evaluation; five more rated the synthetic replication.

"This was independently evaluated." Google built it, Google's Gemini runs it, Google evaluated it. The open-source release is the remedy, and it is a remedy for the future rather than a property of this paper.

**The honest one-sentence version:** *forty Google researchers built a genuinely clever three-specialist health chatbot, evaluated it more thoroughly than anything else in this reading list — 1,350 hours of human assessment, multiplicity handled properly, a safety review they published the bad half of — and showed that health experts think it is substantially better than the alternatives while end users think it is slightly better, that it takes three and a half minutes to answer, that one summary in six carries some potential for harm, and that whether it improves anybody's health remains entirely unknown.*

## 8. Bottom Line for Your Life

**If you use a consumer health app or wearable:** this is a research prototype, not a product you can get, and the authors say it "should not replace professional care." What is worth taking from it: **the best current systems of this kind get the right answer first about half the time on symptom questions**, and **a clinician review of their health summaries found one in six carried some potential for harm.** If an app tells you something about your blood results or your sleep data that worries you or that would change what you do, **that is the moment to involve a person**, not to ask a follow-up question.

**If you are a clinician whose patients bring you AI-generated health summaries:** this paper tells you what those summaries are good and bad at. Good: comprehensiveness, pulling wearable and lab data into one narrative, citing sources. **Bad in a specific way worth knowing: the safety review found 15% mild and 2% moderate-to-severe potential harm**, and the paper's proposed fix is exactly the one you would want — **restricting retrieval to curated sources like WHO, PubMed, NICE and CDC, and showing provenance next to each recommendation.** If a summary a patient shows you has no sources, that is the version without the fix.

**If you build consumer health AI:** three findings here are directly actionable. **Measure end-user perception separately from expert perception, and plan around the smaller number** — the gap was 3× here, twice, and the user's number is what drives use. **Run the safety review and publish it**, because 2% moderate-to-severe is the figure that decides whether the thing can ship and you will not learn it any other way. And **205 seconds is not shippable** — the paper's own suggestions (parallel execution, caching, lighter routing models) are the work that stands between this architecture and a product.

**If you design evaluations:** copy the multiplicity treatment. **Prespecify your rubrics, analyse each as a confirmatory test, then run a cross-rubric Holm–Bonferroni robustness check and report its outcome** so a reader can see which findings depend on the framing. Copy the **rater-as-random-effect** GLMM. Copy the **autorater validated against human annotations with a reported ICC** before use. And copy the thing that costs most: **recruiting both end users and experts**, because the disagreement between them was the most informative result in the paper.

**If you are reading the coverage:** expect "Google's AI health agent beats the alternatives," built on the 46.7% and 66.7% preference numbers. Both are real. The three figures that will not make the headlines are **4.6%** (how much better end users thought it was), **205 seconds** (how long it takes), and **2%** (how many of its health summaries a clinician panel judged capable of moderate-to-severe harm).

**This is education, not medical advice.** Nothing here should change anyone's treatment or any decision based on a wearable or a blood test. If an AI tool has told you something about your health, that is a conversation with your own clinician.

---

## Appendix: deferred papers, shelf, status on 2026-11-12

**One deferral resolved after 22 days.** PMID 42907512 had no PubMed Central copy on every check from 2026-10-22 onward. **Today the conversion returned PMC13736220**, and the full text retrieved cleanly. **Closed, decoded above.** Standing note for the record: this is the second time in this list that a PMC body has appeared well after indexing — the JAMA OpenEvidence paper (entry 68) went the other way, serving an empty body for twenty-one consecutive days and never filling.

**A deviation from the standing rule, stated plainly.** Today was the day the twenty-one-day rule fired on the **BMJ** LLM-trial reporting-completeness review (PMID 42869550, [DOI](https://doi.org/10.1136/bmj-2026-100855), 395:e100855), **day 29**, whose PMC body is still absent — I re-checked today and the conversion returns no PMC identifier. The rule said it takes priority. **It did not, because a full text that had been blocked for 22 days became available this morning, and the daily instruction puts full text ahead of abstract-only.** The BMJ decode will be the same abstract-only exercise tomorrow as it would have been today. **It takes priority on 2026-11-13 and is the next run's pick**, ahead of the shelf.

**Deferred papers — three, all re-checked today.** **Gait foundation model**, *Nature Medicine* (PMID 42995231, [DOI](https://doi.org/10.1038/s41591-026-04724-9)) — **day 4**, still no PMC copy, abstract-only date **2026-11-30**. **BMJ** reporting-completeness review (42869550) — **day 29, next run's pick, abstract-only.** ***Annals* *Choosing Wisely*** (PMID 42896192, [DOI](https://doi.org/10.7326/ANNALS-26-01667)) — **day 23**, still no PMC copy, weekly re-check, **abstract-only date 2026-11-19**.

**Landmark check for the past week.** According to PubMed, four records, all previously assessed: the NEJM mass-surveillance Perspective (43001754), the *Nature Medicine* gait commentary (43003904), the gait foundation model itself (42995231) and the Nature structRFM RNA model (42983082). **No new candidates and none displaces the queue.**

**Shelf status: five spares, unchanged** — **(B)** bone-tumour review arguing reference-standard instability is the binding constraint (PMID 42997475, PMC13742044); **(C)** diabetic retinopathy at AUROC 0.972 from eight routine labs (42974596, PMC13727297); **(D)** glaucoma visual-field prediction with external validation on two OCT devices (42997014, PMC13740841); **(E)** MIBC pathological complete response, 102 models screened, calibration-slope CI 0.469–1.639 (42997524, PMC13741961); **(F)** bitewing positioning errors trained entirely on mannequins (42981213, PMC13734376). **After tomorrow's BMJ decode, item (C) is next**, as the deliberate contrast with entry 74 that yesterday's plan set out.

**Watch item:** PM Heart trial results (protocol PMID 42893738), quarterly.
