# Overuse and False Restraint in Large Language Model Recommendations for Choosing Wisely Scenarios

**Authors:** Ariel D (Department of Family Medicine, Clalit Health Services, Tel Aviv; Gray Faculty of Medical & Health Sciences, Tel Aviv University), Endelman S (Gray Faculty of Medical & Health Sciences, Tel Aviv University; Division of Dermatology, Rabin Medical Center–Beilinson Hospital, Petach Tikva), Laban G (Department of Industrial Engineering and Management, Ben-Gurion University of the Negev; Azrieli National Center for Autism and Neurodevelopment Research; School of Brain Sciences and Cognition, Ben-Gurion University) — 3 authors, Israel
**Journal:** Annals of Internal Medicine, 2026; 179(11): 1566–1576 (e-published 2026-10-20)
**Decoded:** 2026-11-19

**Analysis basis:** **ABSTRACT ONLY.** This is the structured abstract as indexed by PubMed, independently re-confirmed through a second literature service that returned the identical text. **The full paper could not be obtained**, and all four available routes were tried and documented: (1) **no PubMed Central copy** — a PMID-to-PMCID conversion returned PMID only, checked repeatedly over 30 days and again today; (2) a full-text literature service returned **"MCP tools require a paid scite plan"**; (3) the publisher host `www.acpjournals.org` **failed DNS resolution** under this session's network policy, exactly as `doi.org` and `www.bmj.com` have; (4) **no preprint or open-access copy** surfaced in a semantic search that did return the published record. *Annals of Internal Medicine* is subscription-access. **Everything below comes from the structured abstract, and the things I cannot see are listed explicitly rather than guessed at.**

**Source links (verified):**
- DOI: https://doi.org/10.7326/ANNALS-26-01667
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42896192/
- Full text: **none available.** No PMC copy exists and the publisher page could not be reached from this session, so **no full-text link is given rather than an unverified one.**

**Basis of link verification.** Direct URL fetching is blocked here, so verification was against the live PubMed/NLM record. According to PubMed, PMID 42896192 returns this exact title, these three authors with these affiliations, *Annals of Internal Medicine* volume 179 issue 11 pages 1566–1576, DOI `10.7326/ANNALS-26-01667`, and MeSH terms including Large Language Models, Medical Overuse, Unnecessary Procedures and Benchmarking. A PMID-to-PMCID conversion returned **no PMCID**, confirming there is no PMC full text to link. The same title, authors, journal and complete abstract were then returned independently by a second literature service, so every number quoted below has been seen in two places.

**Funding: explicitly none.** The abstract's primary funding source field reads "None."
**Conflicts of interest: not visible** — the disclosure statement is in the part of the paper I cannot read. **Not reported here means not retrievable, not absent.**
**Ethics:** **"No human participants were involved."** This is a benchmark study on software, so no approval would be expected.
**Reporting guideline: none visible in the abstract.** **TRIPOD-LLM** exists for exactly this kind of study and is the instrument entry 76 measured the field against at 40% mean completeness.

---

## 1. The Gist

**Three researchers in Israel asked six commercial AI chatbots 225 medical questions where the right answer was usually "don't order that test," and counted how often the AI said to order it anyway. The answer was 5.4% of the time. The interesting part is not that number — it is that almost all of it came from just two of the fifteen topics tested, and that the paper's own confidence interval quietly tells you the study is much smaller than its 4,050 responses make it sound.**

Start with what is being tested. **Choosing Wisely** is a campaign in which medical specialty societies name things their own members do too often — tests, scans and treatments that usually do not help and sometimes harm. "Don't do a thyroid ultrasound for a tiny nodule found by accident." "Don't do a routine ECG on a healthy low-risk adult." Each recommendation comes with caveats, because almost nothing is *never* indicated: the test that is wasteful for most patients is right for a few. **So the real skill is not knowing the rule. It is knowing when the rule does not apply.**

That is why this study design is good. **Clinicians are already using these chatbots**, and the obvious worry is that a system trained to be helpful will say yes to a test. But there is an opposite worry the authors took equally seriously: a system taught to be cautious might refuse care that someone actually needs. **So they measured both directions.**

**What they did.** They took **15 Choosing Wisely recommendations** and wrote **225 clinical scenarios** — for each recommendation, **10 where holding back was right and 5 where acting was right**. They put each scenario to **six commercial chatbots from OpenAI, Anthropic and Google, three times each**, phrased as a question from a doctor, using the companies' production programming interfaces in **February and March 2026**. That makes **4,050 responses**. Two co-primary outcomes: the **overuse rate** (recommending action when restraint was right) and the **false restraint rate** (withholding action that was right).

**I checked the structure and it reconciles exactly:** 15 recommendations × 15 scenarios each = 225; 225 × 6 models × 3 runs = 4,050.

**The results.**

- **Overuse: 5.4%** (95% CI, 0.6% to 12.2%)
- **No overuse at all in 8 of the 15 recommendations**
- **Thyroid ultrasound for an incidental nodule under a centimetre: overuse in 42.8% of responses**
- **Routine ECG in low-risk adults: overuse in 28.3%**
- **The remaining 5 recommendations: 0.6% to 3.3%**
- **False restraint: 0.6%** (CI, 0.1% to 1.2%), **absent in 11 of 15**, highest for PSA screening at 3.3%

**Now the three things I found by doing arithmetic the abstract does not do.**

**First, and most important: the 5.4% is an average of fifteen numbers, not a rate.** The abstract's own partition is complete — 8 recommendations at zero, 2 named outliers, 5 in the 0.6%–3.3% band, which is 8 + 2 + 5 = 15. If you take the unweighted mean of those fifteen per-recommendation rates, with the five low ones averaging around 2%, **you get 5.4% exactly.** So the headline is the **average topic**, not the average response, and certainly not the chance that a doctor asking a real question gets bad advice.

**And that matters because the distribution is wildly lopsided.** Those two outliers carry roughly **88% of all the overuse in the study**. The honest one-line summary is not "these systems recommend overuse 5.4% of the time." It is **"these systems were fine on thirteen topics and bad on two"** — and on the worst one, the thyroid nodule, the complement is the number to sit with: **it advised restraint only 57.2% of the time**, which on a yes/no question is barely better than a coin toss.

**Second: the confidence interval is the paper telling you the truth about its own size, and you have to know how to hear it.** A span from **0.6% to 12.2%** looks absurdly wide for a study with 4,050 responses. **It is wide because it is correct.** I computed what a naive interval would look like if those 4,050 responses were 4,050 independent observations: about **4.5% to 6.3%**. The reported interval's upper half is **eight times wider than that.** When I instead built the interval the way you must — treating the **15 recommendations** as the independent units, because scenarios within a recommendation are variations on one theme — I reproduced the reported upper bound of 12.2% to within **0.2 percentage points.** **So the authors did the hard, honest thing, and the reward for it is a headline number whose uncertainty runs from "almost never" to "one in eight."** That is the real finding about precision, and it deserves credit rather than suspicion.

**Third: the thing being counted was counted by another AI, and we are not told how well.** The abstract says responses were **"classified by LLM judge with physician adjudication"** and reports **no agreement statistic** — no kappa, no percentage concordance, no indication of how often the judge and the physicians differed. **This is not a nitpick, because it is the measuring instrument.** And it is plainly feasible: according to PubMed, a separate team testing 35 chatbots against all 142 US Preventive Services Task Force recommendations reported their LLM raters' interrater reliability as **kappa 0.8893 and 0.9366** (Johnson T & Gaissmaier W, *JMIR AI* 2026;5:e87034, PMID 42530970, verified independently). **Other people doing this exact kind of work publish the number. This abstract does not.**

**Two more gaps worth naming, both supplied by the published literature.**

**There is no human comparator, so "is 5.4% good?" has no answer here.** Clinicians overuse these same tests at substantial rates — that is why Choosing Wisely exists at all. And the direction of the comparison is not obvious: a benchmark study with over 6,000 scenarios and 7,000 physician annotations reports that **LLMs are more likely than physicians to recommend unnecessary care at baseline**. Without a physician arm, 5.4% floats free.

**And six models are pooled into one number.** The between-model spread in this literature is enormous: Johnson and Gaissmaier's 35 models ranged from **45.19% to 87.77%** concordance on the same task, a 43-point gap. **A single pooled "LLM overuse rate" averages over systems that may behave nothing alike** — and the abstract gives no per-model breakdown.

**What the paper gets right, and it is a lot.** It asked a question that matters, it **prespecified both error directions as co-primary outcomes**, it deliberately built in action-appropriate scenarios so false restraint could be measured at all, it **reported the per-recommendation breakdown** so the concentration is visible, it **computed its interval at the right level**, it took no funding, and its stated conclusion is narrow and accurate: *"The LLMs rarely withheld recommendations for treatment when it was appropriate. Overuse was concentrated in 2 recommendations."* **It does not say these systems are safe.**

## 2. Study Snapshot

**Study type:** **benchmark evaluation** — the abstract's own term. A constructed test set run against commercial software. **No patients, no clinical outcomes, no prospective component, and explicitly "No human participants were involved."** This is a study of model behaviour on authored scenarios, not of anything that happened to anyone.

**What was tested.** **Six commercial large language models** accessed through the **production application programming interfaces of OpenAI, Anthropic and Google**, during **February to March 2026**. **The individual model names and versions are not in the abstract** — which matters more here than usual, because production APIs are updated continuously, so this is a dated snapshot of six moving targets.

**The scenarios.** **15 Choosing Wisely recommendations**, each turned into **15 scenarios: 10 in which restraint was appropriate and 5 in which action was appropriate**, giving **225 scenarios** total. **How those 15 recommendations were selected from the several hundred Choosing Wisely has published is not stated in the abstract**, nor is who wrote the scenarios, nor whether anyone independent checked that the designated right answers were right.

**The prompt.** A single prompt **"from the clinician perspective."** **Single prompts without follow-up**, which the authors list as a limitation. So this measures a first answer to a doctor's question, not a conversation, and not what a patient would get.

**The responses.** **Three runs per model per scenario**, giving **225 × 6 × 3 = 4,050 responses** — which I verified reconciles exactly.

**The outcome measurement.** **Co-primary outcomes**, prespecified as such: the **overuse rate** (endorsing action when restraint was appropriate) and the **false restraint rate** (withholding an appropriate action). Responses were **"classified by LLM judge with physician adjudication."** **No inter-rater agreement statistic of any kind appears in the abstract.**

**A denominator distinction the abstract does not make, which I derived.** Overuse can only occur on a restraint-appropriate scenario and false restraint only on an action-appropriate one. So the two rates have **different denominators**: overuse rests on **15 × 10 × 18 = 2,700 responses** and false restraint on **15 × 5 × 18 = 1,350**, which sum to 4,050. **The "4,050 responses" in the abstract is the combined total, not the denominator of either headline rate.** In counts, 5.4% of 2,700 is about **146 overuse responses**, and 0.6% of 1,350 is about **8 false restraint responses.**

**Results, as reported.** **Overuse 5.4% (95% CI, 0.6% to 12.2%)**; **no overuse in 8 of 15 recommendations**; **thyroid ultrasound for an incidental subcentimeter nodule 42.8%**; **routine electrocardiography in low-risk adults 28.3%**; **the remaining 5 recommendations 0.6% to 3.3%**. **False restraint 0.6% (CI, 0.1% to 1.2%)**, **absent for 11 of 15 recommendations**, **highest for prostate-specific antigen screening at 3.3%**.

**Limitations the authors state, verbatim in substance.** **Single prompts without follow-up; a benchmark rather than real-world use; responses classified by LLM judge with physician adjudication**; and **"Findings may not extend to consumer-facing use."** That last one is a real act of restraint: the obvious headline would have been about patients asking chatbots for advice, and they declined it.

**The authors' conclusion.** **"The LLMs rarely withheld recommendations for treatment when it was appropriate. Overuse was concentrated in 2 recommendations."**

**Funding: None**, stated in the abstract's primary funding source field.

**Not reported in the abstract, or not retrievable:** **any inter-rater or judge-agreement statistic**; **the six models' names and versions**; **any per-model results**; **any measure of run-to-run variation across the 3 runs**; **the prompt text**; **how the 15 recommendations were chosen**; **who authored and validated the 225 scenarios**; **the per-recommendation rates for 13 of the 15** (only the two outliers and a range for five others are given); **any human or clinician comparator**; **the conflict-of-interest statement**; and **whether any reporting guideline was followed.** All of these sit in the full text, which could not be obtained.

## 3. How Strong Is This Evidence? (Grade 3 out of 5)

**This is a well-designed benchmark with a genuinely good measurement plan, reported in an abstract that shows more statistical discipline than most full papers in this reading list — and capped at 3 because I can only read the abstract, because the instrument that did the measuring has no reported reliability, and because the headline number is an average over topics with no human comparator to judge it against.**

**What is genuinely well done, and some of it is better than anything in the recent run.**

**Both error directions were prespecified as co-primary outcomes.** This is the single best feature of the study. Entry 81 earned credit merely for *naming* the asymmetric cost of false positives against false negatives in its discussion; **this paper built both directions into the design and the sampling frame**, deliberately including 5 action-appropriate scenarios per recommendation so that false restraint could be measured at all. Most AI-safety benchmarks test one direction and declare victory. **A system that never recommends overuse by refusing everything would score perfectly on one outcome and be caught immediately by the other.**

**The confidence interval is computed at the right level, and that is rare enough to be the paper's quiet achievement.** The 0.6%–12.2% span is not sloppiness; it is what you get when you treat the **15 recommendations** as your independent units instead of pretending you have 4,050. I reconstructed it and the upper bound reproduces to within **0.2 percentage points**. **The temptation to report 4.5%–6.3% instead must have been considerable, because it would have made the study look eight times more precise.** They did not take it.

**The per-recommendation breakdown is in the abstract**, which is the only reason anyone can see that the result is concentrated rather than diffuse. **Compare entry 76**, also abstract-only, whose seven mean completeness scores arrived with no decomposition and no intervals at all. **This abstract gives both.**

**The limitations are specific, and one of them is costly.** "Findings may not extend to consumer-facing use" closes off the most quotable version of this paper — chatbots giving patients bad advice — on the correct grounds that they tested a clinician's prompt.

**The conclusion is narrow and matches the data.** "Overuse was concentrated in 2 recommendations" is the right summary. **Nothing is overclaimed.**

**Three runs per model rather than one**, which at least acknowledges that these systems are stochastic. **Dates and providers stated**, which is essential provenance for software that changes weekly. **Funding none.**

**So why 3.**

**Abstract only.** I cannot see the methods, the judge validation, the prompt, the per-model results, or the conflicts statement. The standing rule in this list is that an abstract-only entry is capped, and the four access routes tried are documented above.

**No reliability statistic for the LLM judge.** The entire study reduces to a classification: did this response endorse action or restraint? **That classification was performed by another language model, with physician adjudication, and we are told nothing about how well the two agreed.** This is the same defect as entry 81's consensus labelling in a new and more unsettling form — **there, the instrument was three humans whose disagreement was destroyed by deliberation; here, the instrument is itself a language model of the kind under test.** And unlike entry 81, where no kappa was obtainable from the design, **here it plainly was obtainable**: another team reported kappa 0.8893 and 0.9366 for the same kind of LLM-rater setup.

**No human comparator**, so the central question — is 5.4% reassuring or alarming? — is unanswerable from this paper. Choosing Wisely exists because clinicians overuse these tests substantially; a physician arm would have turned a floating number into a comparison. Entry 78 was marked down for the same omission, and there the comparator was available and unrun.

**The headline is an unweighted average over recommendations, not a rate of anything.** With 88% of the overuse in 2 of 15 topics, the mean is a poor summary of a lopsided distribution, and **it is also the wrong weighting for the clinical question**: incidental thyroid nodules and routine ECGs in healthy adults are *common* situations, so a frequency-weighted rate would plausibly be **higher** than 5.4%, not lower.

**Six models pooled, with no per-model breakdown.** The between-model spread in this literature is 43 points in one verified comparator. **A pooled rate across six systems is an average over things that may not belong in the same average.**

**Three runs cannot measure run-to-run instability**, and none is reported. This matters concretely: according to PubMed, a six-model study of inpatient management vignettes found **internal consistency as low as 0.60** across five repeated queries of the same vignette, with some models changing their recommendation in two of five runs (Landon S et al., *J Gen Intern Med* 2026;41(5):1286–1291, PMID 41055682, verified independently). **In that study, instability was the headline finding. Here it is averaged into the point estimate and never reported.**

**The false restraint numerator is roughly 8 responses** out of 1,350. A rate built on single-digit events is extremely fragile, and "false restraint was rare" rests on it.

**15 recommendations from a corpus of hundreds, with no stated selection method.** If the 15 were chosen because they were interesting, the overuse rate is not an estimate of anything general.

**The scenarios were authored by the investigators, who also set the right answers.** No validation of either is visible. **The benchmark and the answer key come from the same three people.**

**Why not 2.** Entry 77 scored a 2 for claiming screening from cross-sectional data with its outcome possibly among its inputs — a mismatch between claim and evidence. **There is no mismatch here.** The design does what the title says, the interval is honest about the precision, the limitations name the right four things, and the conclusion is narrower than the data would have permitted. **Everything claimed is supported.**

**Why not 4.** The grade tracks what a reader may safely take away. From the abstract alone a reader may take away that **six commercial systems, on 15 selected topics in early 2026, recommended overuse on the average topic about 5% of the time with a very imprecise estimate, were clean on 8 topics, and were poor on 2** — measured by an instrument of unreported reliability, with no human comparator. **That is a useful finding and a bounded one.** Entry 79 earned a 4 by advancing a falsifiable thesis and quantifying it with counter-evidence included; this paper reports a competent benchmark.

**What would make this a 4, concretely.** **Report the judge's agreement with the physician adjudicators** — one kappa, and the comparator literature shows it is standard. **Report all 15 per-recommendation rates**, not two plus a range for five. **Report the six models separately**, so a reader can see whether the pooled 5.4% describes anything. **Report the run-to-run variation** already collected across the 3 runs. **And add a clinician comparator**, or state plainly that the rate is uninterpretable without one. **The first four need no new data at all** — they are re-reporting what the study already has. **This entry will be upgraded if a PMC body appears**, as the standing offer runs for entries 68 and 76.

## 4. The Editor's Concerns

**1. The 5.4% is the mean of fifteen numbers, and I can show that arithmetically.** The abstract's partition of the 15 recommendations is complete and non-overlapping: **8 with zero overuse, 2 named outliers at 42.8% and 28.3%, and 5 in the 0.6%–3.3% band — which is 8 + 2 + 5 = 15.** Taking the unweighted mean of those fifteen rates, with the five low values averaging about 2% (inside the stated range), **gives 5.41%, matching the reported 5.4%.** So the headline is **the average recommendation**, not the average response. **A reader who takes 5.4% as "the chance a chatbot steers a doctor wrong" has misread the unit.**

**2. And the distribution is too lopsided for a mean to describe it.** Summing those fifteen rates, **the two outliers account for about 88% of all the overuse in the study.** The accurate summary is not a rate but a shape: **clean on thirteen topics, poor on two.** The paper's own conclusion says this — "Overuse was concentrated in 2 recommendations" — which is to its credit; **the 5.4% in the results line is what will be quoted, and it is the less informative of the two statements.**

**3. Read the worst result as its complement.** On the thyroid nodule scenarios, overuse was recommended **42.8%** of the time, meaning restraint was correctly advised **57.2%** of the time — on a binary question, **barely above chance.** On routine ECG, 28.3% overuse means **71.7% correct.** These are not marginal underperformances; on two common clinical situations, the systems were close to unreliable.

**4. The wide interval is a correctly computed one, and it deserves credit, not suspicion.** A naive interval treating 4,050 responses as independent gives roughly **4.5% to 6.3%**. The reported interval is **0.6% to 12.2%**, whose upper half-width is **eight times larger**. Rebuilding it with the **15 recommendations** as the independent units reproduces the upper bound to within **0.2 percentage points**. **The authors could have reported an interval eight times tighter and did not.** The consequence must still be stated plainly: **the overuse rate is consistent with anything from almost never to one response in eight**, and that is the honest precision of this study.

**5. The measuring instrument is an LLM, and its reliability is unreported.** Everything in this paper depends on a binary judgement — did this response endorse action or restraint — made by an **"LLM judge with physician adjudication"** with **no kappa, no concordance rate, no count of disagreements.** This is entry 266's rule exactly: **when the measurement is a judgement, reliability *is* the precision.** It is also entry 81's gap in a sharper form, because **the instrument belongs to the same class of system being evaluated**, which raises a correlated-error question nobody can assess from the abstract. **And it was obtainable**: according to PubMed, Johnson T & Gaissmaier W (*JMIR AI* 2026;5:e87034, PMID 42530970, DOI 10.2196/87034, verified independently) report LLM-rater interrater reliability of **kappa 0.8893** in wave 1 and **0.9366** in wave 2 of a study testing 35 models against all 142 USPSTF recommendations. **The number is standard in this literature. Its absence here is a reporting choice.**

**6. No human comparator, so the number cannot be judged.** Choosing Wisely exists because **clinicians** order these tests too often. Is a 5.4% topic-average overuse rate better or worse than a doctor's? The abstract does not say, and the answer is not obvious in the reassuring direction: a large benchmark with over 6,000 scenarios and 7,000 physician annotations reports that **LLMs are more likely than physicians to recommend unnecessary care at baseline** (Gourabathina A et al., Findings of EMNLP 2026 — noted as a conference paper found through a literature search and **not independently verified against PubMed**, which does not index it, so treat the figure as indicative). **Technique 286 applies: the baseline that matters is the cheapest comparator you already have access to**, and here that is a panel of clinicians answering the same 225 scenarios.

**7. Six models pooled into one rate, with no breakdown.** The verified between-model spread in this literature is large: Johnson and Gaissmaier's 35 models ranged from **45.19% to 87.77%** baseline concordance, a **43-point** gap. **A single pooled rate across six commercial systems may be averaging a safe model and an unsafe one into a middling number that describes neither.** This is the most consequential thing the full text could fix with data already collected — and the practical question a clinician actually has is *which* chatbot, not whether chatbots in general.

**8. Three runs per model, and no measure of what varied between them.** These systems are stochastic: the same question can get different answers. Three runs is enough to average over that and **too few to characterise it**, and no run-to-run statistic is reported. The comparator is instructive: Landon S et al. (*J Gen Intern Med* 2026;41(5):1286–1291, PMID 41055682, DOI 10.1007/s11606-025-09888-7, verified independently) queried six LLMs on four inpatient vignettes in five independent sessions and found **internal consistency as low as 0.60**, with some models changing their recommendation in **two of five runs**. **In that study the instability was the finding; here the same phenomenon is absorbed into a point estimate.**

**9. False restraint "was rare" rests on about eight events.** The 0.6% rate has a denominator of **1,350** action-appropriate responses, so the numerator is roughly **8**. The authors' reported interval of **0.1% to 1.2%** is appropriately humble. **The conclusion sentence — "The LLMs rarely withheld recommendations for treatment when it was appropriate" — is the paper's most confident claim and it is carried by single-digit counts**, on 75 authored scenarios, with 11 of 15 recommendations contributing zero. It is probably true; it is not firmly established.

**10. The benchmark and its answer key were built by the same three people, and 15 topics were selected from hundreds.** Neither the selection method for the recommendations nor any validation of the 225 scenarios and their designated correct answers is visible in the abstract. **Entry 81's lesson transfers directly: performance tracks the operational precision of the label**, and here the labels are "restraint was appropriate" and "action was appropriate" on scenarios the investigators wrote themselves. **The caveats are the whole difficulty** — Choosing Wisely recommendations are explicitly conditional — so where exactly each scenario was placed relative to those caveats is the study's most load-bearing judgement and is entirely unexamined from outside.

**11. Six unnamed models on production APIs in a two-month window.** The abstract names the three providers and the dates, which is good practice, but **not the models or versions.** Production APIs are updated continuously, so this is a snapshot of six moving targets. **Without version identifiers the study is not replicable even in principle**, and a reader cannot tell whether the systems they use today are the ones tested.

**12. No reporting guideline visible, and TRIPOD-LLM is the one that fits.** Entry 76 — the BMJ review decoded six days ago — measured LLM trial reporting at **40% mean completeness against TRIPOD-LLM**, the lowest of its seven instruments, and found the gaps concentrated in **model versioning and access modality, inference parameters, and output postprocessing.** **Those are precisely the items missing here**: no model names or versions, no inference parameters, no description of how outputs were processed into the binary classification. **This is the running reporting-guideline observation inverted once more.** The standing rule holds — naming a checklist does not predict quality — but entry 76's specific finding predicted this paper's specific omissions with uncomfortable accuracy. **A caveat I should state: these items may well be in the full text. What I can say is that they are not in the abstract, and that the abstract is what most readers will see.**

## 5. Statistics Spotlight

Three concepts, numbered from 327 in the running list in `queue.md`. The first two are what this paper is really about.

**4,050 responses is not 4,050 pieces of evidence — and the paper's own wide interval is it telling you so.**

The abstract reports **4,050 responses**, which sounds enormous. It then reports an overuse rate of **5.4% with a 95% confidence interval from 0.6% to 12.2%** — a span so wide it looks like a typo. **Both things are correct, and understanding why is the single most useful statistical skill this paper can teach.**

**What a confidence interval is.** It is a range of values for the true rate that are reasonably consistent with what you observed. Wide means you have learned little; narrow means you have pinned it down. **How wide it is depends on how many *independent* observations you have** — and "independent" is the word doing all the work.

**Why 4,050 is not the right count.** Look at how those responses were built: **15 recommendations, each with 15 scenarios, each put to 6 models, 3 times.** The three runs of the same scenario on the same model are nearly the same observation. The 15 scenarios within one recommendation are variations on a single theme — if a model has a blind spot about incidental thyroid nodules, it will show up in all ten restraint scenarios for that recommendation at once. **They rise and fall together.** So the number of genuinely independent things being sampled is closer to the number of **recommendations: 15.**

**Here is the arithmetic, which I ran.** Treating the responses as 4,050 independent observations, a standard interval around 5.4% comes out at about **4.5% to 6.3%** — a half-width under one percentage point. The reported interval's upper half-width is **6.8 points, eight times larger.** And when I rebuilt the interval properly — taking the fifteen per-recommendation rates as the data, computing their spread, and using the appropriate multiplier for 14 degrees of freedom — **the upper bound came out at 12.4%, against the reported 12.2%.** **It reproduces to within two-tenths of a point.**

**So the wide interval is not a weakness in the paper. It is the paper being honest, and it is the strongest evidence that the authors understood their own design.** They could have published 4.5%–6.3% and looked eight times more precise.

**Why clustering inflates uncertainty, intuitively.** Imagine measuring the average height of adults in a country. You could measure 4,050 people chosen at random from everywhere. Or you could pick **15 families** and measure 270 members of each. **Both give you 4,050 measurements, and the second tells you far less**, because people in a family resemble each other — once you have measured a few, the rest add little new information. **Your effective sample size is closer to 15 than to 4,050.** Scenarios within a Choosing Wisely recommendation are a family.

**Watch out for:** the phrase "we analysed N responses" where N is scenarios times models times repeats. **Ask what the independent unit is**, then look at whether the reported interval is consistent with that unit or with the inflated count. **Two diagnostics that cost nothing.** First: compute the naive interval yourself from the big N — if the paper's interval is much wider, they clustered properly and deserve credit; **if the paper's interval matches the naive one, the precision is overstated, possibly by a factor of eight.** Second: **a suspiciously narrow interval on a repeated-measures benchmark is a red flag, and a suspiciously wide one may be a mark of quality.** That is the opposite of most people's instinct.

**An average across categories is not a rate — and when the distribution is lopsided, the average describes nothing.**

The reported overuse figure is **5.4%**. I showed in the concerns above that this is the **unweighted mean of fifteen per-recommendation rates**: 8 zeros, 42.8%, 28.3%, and five values averaging about 2%. **The partition is complete (8 + 2 + 5 = 15) and the mean comes out at 5.41%.**

**Why that is the wrong summary here.** Two of fifteen recommendations carry about **88% of all the overuse.** A mean is a good description of a cluster of similar numbers. **It is a bad description of thirteen small numbers and two large ones** — the same reason nobody reports the average wealth of a room containing a billionaire. The informative statement is the shape: **clean on thirteen, poor on two.**

**And there is a second, subtler problem: which weighting answers the clinical question?** An unweighted mean treats all fifteen recommendations as equally important. But a doctor does not encounter Choosing Wisely topics equally often. **Incidental small thyroid nodules and routine ECGs in low-risk adults are common situations** — a general practitioner meets them constantly. So if you weighted each recommendation by **how often it actually arises in practice**, the two worst performers would carry more weight, not equal weight, and **the overall rate would plausibly come out higher than 5.4%, not lower.** **The reassuring headline depends on a weighting choice that does not match clinical reality**, and the abstract never flags this as a choice.

**A tiny worked example.** Suppose a hospital has two departments. In cardiology, 1 of 1,000 procedures goes wrong (0.1%). In neurosurgery, 30 of 100 go wrong (30%). The **unweighted average across departments** is 15.05%. The **actual rate across all procedures** is 31 of 1,100, or 2.8%. **Those differ by more than fivefold, and both are "the error rate."** Which one you want depends entirely on your question — "how risky is the average department?" or "how risky is a procedure here?" **Neither is wrong; quoting one as if it were the other is.**

**Watch out for:** any headline rate in a study that tested several distinct topics, conditions, sites or tasks. **Ask: is this an average of the groups, or a rate over all the observations? And if it is an average of groups, is the distribution lopsided enough that the average describes none of them?** The tell is usually in the paper itself: **when the results section says "most of the effect came from two of the categories," the headline mean has already been undermined by the authors.** And ask the weighting question too: **equal weighting is a decision, not a default**, and it is rarely the one a clinician needs.

**When your measuring instrument is itself an AI, its reliability is your study's precision — and it is reportable.**

This entire study rests on a single judgement repeated 4,050 times: **did this response endorse action, or restraint?** That judgement was made by **"LLM judge with physician adjudication"** — one AI classifying another AI's answers, with doctors resolving some portion of cases. **The abstract reports no measure of how well those classifications held up.** No kappa, no percentage agreement, no count of how often the judge and the physicians disagreed.

**Why this is the central gap and not a technicality.** Every number in the paper is downstream of that classification. If the judge mislabels borderline responses — and Choosing Wisely scenarios are *built* out of borderline cases, since every recommendation carries caveats — **then the reported rates measure the judge as much as the models.** This is technique 266 in a new setting: **when the measurement is a judgement, the reliability of that judgement is the precision of the study**, and an unreported reliability means the precision is unknown.

**And there is a wrinkle specific to AI judging AI.** If the judge is the same kind of system as the models under test, its errors may not be independent of theirs — **it might share their blind spots.** A human rater who does not know a Choosing Wisely caveat and a chatbot that does not know it make *correlated* mistakes, and correlated errors between instrument and subject are the hardest kind to detect from outside. **Nothing in the abstract lets anyone assess this, in either direction.**

**The good news, and the reason this counts as a real omission rather than an impossibility: other teams report the number.** According to PubMed, Johnson T & Gaissmaier W (*JMIR AI* 2026;5:e87034, PMID 42530970) used LLM raters for an almost identical task — scoring whether chatbot answers matched official recommendations — and reported interrater reliability of **kappa 0.8893** in one wave and **0.9366** in another. **Kappa is agreement corrected for the agreement you would get by chance; above about 0.8 is usually called very good.** So this is routine, cheap, and standard practice in exactly this literature.

**And note what the Johnson study found that bears on the judging problem: "high rates of LLMs avoiding definitive recommendations."** If models frequently hedge rather than clearly endorsing action or restraint, **then classifying their answers into two bins is a genuinely hard task with a lot of borderline cases** — which makes the missing reliability statistic more important, not less.

**The everyday version.** You are testing whether six bakers can follow a recipe, and you hire a judge to decide for each loaf whether the recipe was followed. **You then report that the bakers failed 5.4% of the time — and never check whether your judge can tell.** If the judge is reliable, your number means something. If the judge is erratic, you have measured the judge. **And if your judge went to the same baking school as the bakers, you have a particular problem**, because judge and bakers may be wrong about the same things.

**Watch out for:** "classified by LLM judge," "scored by GPT-4," "automated evaluation," "adjudicated by the study team." **Ask for the agreement statistic, and ask what it was computed against.** Two specific follow-ups worth making habitual. **What fraction of cases went to human adjudication, and what was the disagreement rate on those?** And **was the judge validated on a sample scored independently by humans, or was it simply trusted?** A paper that reports a kappa of 0.85 has told you its measurement is sound. **A paper that names its judge and reports nothing about it has not told you its result is wrong — it has told you that you cannot know how precise it is.**

## 6. Jargon Translator

**Choosing Wisely** — a campaign, launched by US medical specialty societies and now international, in which each specialty names tests and treatments its own members overuse. **Crucially, every recommendation comes with caveats**: these are things usually not indicated, not never indicated.

**Overuse** — ordering a test, scan or treatment that is unlikely to help and may harm. The thing Choosing Wisely exists to reduce. Here measured as **endorsing action when restraint was appropriate.**

**False restraint** — the paper's term for the opposite error: **withholding an action that was appropriate.** Including it as a co-primary outcome is this study's best design decision.

**Co-primary outcomes** — two main results, both declared in advance as the things the study is designed to measure. **Declaring them up front matters**, because it stops a researcher from running many analyses and presenting whichever looked best.

**Benchmark evaluation** — testing software against a fixed set of constructed problems with known right answers. **Not a clinical study**: no patients, no outcomes, and here explicitly "No human participants were involved."

**Large language model (LLM)** — the kind of AI behind commercial chatbots, which produces text by predicting what comes next. Not a database and not a reasoning engine with guaranteed consistency: **ask the same question twice and you may get different answers**, which is why this study used three runs.

**Production application programming interface (API)** — the commercial, live version of a model that companies sell access to, as opposed to a research version. **Updated continuously**, which is why the February–March 2026 window matters and why missing version numbers matter more.

**Run** — one repetition of asking the same question. **Three runs per model per scenario here.**

**LLM judge** — using one language model to grade another's output. Fast and cheap at scale. **Its reliability needs reporting, and here it is not reported** — technique 329.

**Physician adjudication** — doctors resolving cases the automated judge could not settle, or checking its work. **How many cases, and how often they disagreed, is not stated.**

**Kappa** — agreement between independent raters, corrected for the agreement chance alone would produce. Runs from 0 (chance) to 1 (perfect); above roughly 0.8 is usually very good. **Not reported in this abstract; reported as 0.89 and 0.94 by another team doing the same kind of work.**

**Confidence interval (CI)** — the range of true values reasonably consistent with what was observed. **Wide means imprecise.** Here 5.4% (0.6% to 12.2%) — wide because correctly computed across 15 recommendations rather than 4,050 responses.

**Clustering** — the fact that observations gathered in groups resemble each other within those groups, so you have fewer independent pieces of information than you have measurements. **The reason this study's interval is eight times wider than a naive one** — technique 327.

**Effective sample size** — how many truly independent observations you have, as opposed to how many rows are in your spreadsheet. **Here closer to 15 than to 4,050.**

**Unweighted mean** — the plain average of group-level rates, treating every group as equally important regardless of size or how often it arises. **What the 5.4% is** — technique 328.

**Subcentimeter thyroid nodule** — a lump in the thyroid gland smaller than 1 cm, usually found by accident on a scan done for something else. **Almost always harmless**, and scanning it leads to biopsies, anxiety and sometimes treatment of cancers that would never have caused trouble. **The worst-performing scenario here, at 42.8% overuse.**

**Routine electrocardiography (ECG) in low-risk adults** — a heart tracing in a healthy person with no symptoms. Recommended against because it rarely finds anything useful and often triggers further testing. **28.3% overuse here.**

**Prostate-specific antigen (PSA) screening** — a blood test for prostate cancer whose benefits and harms are genuinely balanced, so guidelines call for a shared decision rather than routine testing or routine refusal. **The highest false restraint rate here, at 3.3%** — and notably the most genuinely contested of the fifteen, which is what you would expect.

**TRIPOD-LLM** — the reporting guideline written for studies of language models in medicine. **Not visible in this abstract**, and the instrument against which entry 76 measured the field at 40% mean completeness.

## 7. What You Can (and Can't) Say

**You can say:**

"In a benchmark of 225 authored scenarios drawn from 15 Choosing Wisely recommendations, six commercial large language models accessed through OpenAI, Anthropic and Google production APIs in February–March 2026 generated 4,050 responses to a clinician-perspective prompt, with three runs per model."

"The rate of model-recommended overuse was 5.4%, with a 95% confidence interval from 0.6% to 12.2%."

"The models recommended no overuse at all in 8 of the 15 recommendations, and overuse was concentrated in two: thyroid ultrasound for an incidental subcentimeter nodule, at 42.8% of responses, and routine electrocardiography in low-risk adults, at 28.3%."

"False restraint — withholding an appropriate action — occurred in 0.6% of responses (CI 0.1% to 1.2%), was absent for 11 of 15 recommendations, and was highest for PSA screening at 3.3%."

"The study prespecified both error directions as co-primary outcomes and deliberately included action-appropriate scenarios so that false restraint could be measured."

"The authors state the limitations as single prompts without follow-up, a benchmark rather than real-world use, responses classified by an LLM judge with physician adjudication, and that findings may not extend to consumer-facing use."

"The authors' conclusion is that the models rarely withheld appropriate treatment recommendations and that overuse was concentrated in two recommendations. Primary funding source: none."

**You cannot say:**

"AI chatbots give doctors bad advice 5.4% of the time." **That is a misreading of the unit.** The 5.4% is the unweighted mean of fifteen per-recommendation rates — I verified that it reproduces as such — not a rate over responses and not a rate over clinical encounters.

"The overuse rate is 5.4%." **Better stated as 5.4% with a 95% confidence interval from 0.6% to 12.2%**, which is the authors' own figure and spans almost-never to one-in-eight.

"With 4,050 responses this is a large, precise study." **The independent unit is the 15 recommendations, not the 4,050 responses** — which is exactly why the authors' interval is eight times wider than a naive one.

"These models are safe for clinical use." **The paper does not say this, and a benchmark cannot establish it.** No patients, no outcomes, single prompts, one perspective, six unnamed models in a two-month window.

"Only 2 of 15 topics had problems, so the systems are 87% reliable." **Two of fifteen topics carried about 88% of the overuse, and on the worst one restraint was correctly advised only 57.2% of the time** — close to chance on a binary question.

"The models were better than doctors." **There was no human comparator**, so no comparison of any kind is supported — and the wider literature suggests the comparison may not favour the models.

"The classification of responses was accurate." **Unknown.** No agreement statistic for the LLM judge appears in the abstract, while another team reports kappa 0.89–0.94 for the same kind of setup.

"This applies to patients using chatbots." **Explicitly excluded by the authors**: the prompt was from the clinician perspective and they state findings may not extend to consumer-facing use.

"These results describe current AI systems." **They describe six unnamed models as they existed on commercial APIs in February and March 2026.** Production APIs change continuously, and no version identifiers are given in the abstract.

"Model X is safer than model Y." **No per-model results are reported in the abstract**, and the verified between-model spread in this literature is as large as 43 points.

**The honest one-sentence version:** *a carefully designed benchmark whose two best features are that it measured both directions of error and computed its confidence interval at the right level — and whose headline 5.4% is an unweighted average across fifteen topics, roughly 88% of it coming from two of them, measured by an AI judge of unreported reliability, with no human comparator and no per-model breakdown, which is why its own interval honestly runs from 0.6% to 12.2%.*

## 8. Bottom Line for Your Life

**If you are a patient:** nothing here is about you directly — the authors tested a doctor's question, not a patient's, and they say so. **But there is something genuinely useful in it.** Two of the fifteen things tested were an ultrasound for a small thyroid lump found by accident and a routine heart tracing in a healthy adult, and these were where the AI most often said "yes, order it" when the right answer was usually "no need." **Both of those are also things doctors over-order without any AI involved.** So if either is suggested to you and you have no symptoms, **"what would we do differently depending on the result?" is a fair and useful question** — not because of this study, but because that is what Choosing Wisely was set up to encourage.

**If you are a clinician using these tools:** the actionable finding is not the 5.4%. It is **where the failures clustered.** These systems were clean on eight of fifteen topics and poor on two, and the two were cases where the guideline says to hold back on something easy, cheap and reassuring to order. **That is the pattern to expect: a system trained to be helpful will lean toward doing something.** And the direction of the remaining risk is worth knowing — **false restraint was very rare** (about eight responses out of 1,350), so on this evidence these tools are far more likely to suggest an unnecessary test than to talk you out of a necessary one. **The important caveat: six models were pooled and none was named, so this says nothing about whichever tool you personally use.** That is the question the full paper may answer and the abstract does not.

**If you build or evaluate AI systems in medicine, this paper is worth copying in two specific ways.** **First, measure both directions of error and declare both in advance.** A system that avoids overuse by refusing everything would ace a one-directional benchmark; this design catches it. **Second, cluster your confidence intervals at the level of the thing you actually sampled.** The authors had 4,050 rows and reported an interval built on 15 independent units, which made their result look eight times less precise than they could have claimed. **That is what intellectual honesty costs and it is the right price to pay.** **And the one thing to do differently: report your judge's reliability.** If an LLM classified your outputs, publish its agreement with human raters — a single kappa. Other teams in this exact literature publish 0.89 and 0.94. **Without it, a reader cannot tell your findings from your instrument.**

**If you read papers, this entry teaches a counter-intuitive check worth keeping.** **A wide confidence interval can be a sign of quality.** Most people see "0.6% to 12.2%" and conclude the study is weak. Here it means the authors refused to pretend that 4,050 repeated measurements of 15 things were 4,050 independent observations. **So when you see a benchmark reporting thousands of responses and a very tight interval, do the naive calculation yourself and compare** — if their interval matches the naive one, the precision is probably overstated, and by a factor that can easily be eight. **The check takes two minutes and it inverts your first instinct.**

**And the headline-reading lesson, which generalises past AI entirely.** When a study tests many topics and reports one average, **find out whether the average describes anything.** Here the paper's own results section gives the game away — "overuse was concentrated in 2 recommendations" — while the quotable number is a mean over fifteen. **Thirteen good topics and two bad ones is a completely different finding from "5% bad across the board," and only the second one fits in a headline.**

**If you are reading the coverage:** expect "AI recommends unnecessary tests 5% of the time" or "study finds AI largely follows Choosing Wisely guidance." **Three things will likely be missing.** That the 5.4% is an average across topics, with roughly 88% of the overuse in two of them. That the authors' own confidence interval runs from 0.6% to 12.2%, so the number is far less settled than one decimal place suggests. And that **there was no comparison with what doctors do** — which, for a study about overuse, is the comparison the whole question turns on.

**This is education, not medical advice.** Nothing here concerns any diagnosis or treatment, and nothing in it should change what you do about a test your own clinician has recommended. Decisions about thyroid scans, ECGs or PSA testing belong with your own doctor, who knows your history.

---

## Appendix: verification, what the arithmetic showed, and status on 2026-11-19

**Why this paper today.** It was the standing deferred pick, held under this list's **twenty-one-day rule**: a paper with no PMC copy is decoded abstract-only once 21 days have passed since e-publication, rather than being dropped. E-published **2026-10-20**, so today is **day 30**, and its threshold date of 2026-11-19 was set in advance on 2026-11-17 and recorded again yesterday. **PMC was re-checked today and there is still no PMCID.**

**Landmark check, 2026-11-12 → 11-19 — three new records, all assessed, none displacing the queue.** (1) **PMID 43052445**, *Nature*, 2026-11-18, "Hypothalamic volume and cell-type changes in ageing and Alzheimer's disease" — a major atlas (458 MRI scans, 614,403 nuclei) in which machine learning is one analytic component inside a neuroscience resource paper, not the object of study. (2) **PMID 43045795**, *Nature Medicine*, 2026-11-17, "Generational gains in cognitive capacity and dementia incidence rates in Western countries" — **a genuinely important paper** (about 783,000 memory assessments from about 219,000 people across five cohorts followed up to 30 years, finding later-born generations have both higher memory entering old age and slower decline, plausibly accounting for the reported 13%-per-decade fall in dementia incidence), **but it is lifespan epidemiology rather than medical AI**, so it does not displace a medical-AI queue. **Noted as a candidate if this list ever widens its scope.** (3) **PMID 43018982**, *JAMA*, 2026-11-12, "Beyond the Rogue Agent—Preparing Health Systems for AI Failure" — a viewpoint with **no abstract**, not a primary study.

**Abstract-only status, documented across four routes.** (1) **PMC: none** — PMID-to-PMCID conversion returned PMID only, re-checked today and repeatedly across 30 days. (2) **Scite full text: refused** — "MCP tools require a paid scite plan or an active free trial." (3) **Publisher: blocked** — `www.acpjournals.org` failed DNS resolution exactly as `doi.org` and `www.bmj.com` have under this session's network policy; **per session guidance I stopped after one publisher host rather than trying more.** (4) **No preprint or open-access copy** — a semantic search returned the published record and nothing else; *Annals* is subscription-access and does not routinely carry preprints. **Independent corroboration of the abstract itself:** a second literature service returned the identical title, authors, journal and complete structured abstract, so **every number in this summary has been seen in two separate sources.**

**Arithmetic verified today, every check passing.** **Structure reconciles exactly:** 15 recommendations × (10 restraint + 5 action) = **225 scenarios**, as stated; 225 × 6 models × 3 runs = **4,050 responses**, as stated. **Denominator split, which the abstract does not make:** overuse is assessable only on restraint-appropriate scenarios, so its denominator is 15 × 10 × 18 = **2,700**, while false restraint rests on 15 × 5 × 18 = **1,350**; the two sum to 4,050. In counts that is about **146 overuse responses** and about **8 false restraint responses**. **The 5.4% reproduces as an unweighted mean:** the abstract's partition of the 15 recommendations is complete and non-overlapping (8 zeros + 2 outliers + 5 in band = 15), and 42.8 + 28.3 + five values averaging 1.98% gives **5.41%**, with the required mean of the five sitting **inside** the stated 0.6%–3.3% range. **Concentration:** summing the fifteen rates, the two outliers carry **87.6%** of all overuse. **Complements:** 42.8% overuse means restraint correctly advised **57.2%** of the time; 28.3% means **71.7%**. **The interval is cluster-level:** a binomial interval on 2,700 responses gives **4.5%–6.3%** (half-width 0.85 pp), against the reported upper half-width of **6.8 pp — a ratio of 8.0×**; and a 15-cluster t-interval using t(14) = 2.145 reproduces the reported upper bound of 12.2% to within **0.2 pp**. **The reported interval is also asymmetric** (−4.8 pp, +6.8 pp), consistent with a cluster bootstrap on a right-skewed distribution. **No arithmetic error was found anywhere in the abstract**, and the two reported intervals are mutually consistent with the design.

**Comparators, independently verified against PubMed before use.** (1) **Johnson T & Gaissmaier W**, *JMIR AI* 2026;5:e87034, **PMID 42530970, PMC13473853, DOI 10.2196/87034** — 35 LLMs against all 142 USPSTF recommendations in two waves, reporting **LLM-rater interrater reliability of kappa 0.8893 (wave 1) and 0.9366 (wave 2)**, baseline concordance from **45.19% to 87.77%**, and the finding of **"high rates of LLMs avoiding definitive recommendations."** Supplies both the reliability statistic this abstract omits and the between-model spread it pools away. (2) **Landon S, Savage T, Greysen SR, Bressman E**, *J Gen Intern Med* 2026;41(5):1286–1291, **PMID 41055682, PMC13083678, DOI 10.1007/s11606-025-09888-7** — six LLMs, four inpatient vignettes, five independent sessions, 120 model-vignette interactions, **internal consistency as low as 0.60** with some models changing recommendation in two of five runs. Supplies the run-to-run instability this paper collected and did not report. (3) **Not verified, and flagged as such in the text:** a Findings of EMNLP 2026 benchmark (Gourabathina et al.) reporting that LLMs are more likely than physicians to recommend unnecessary care — **PubMed does not index it, so it is cited as indicative only.** **A fourth item found in the same search — an arXiv preprint reporting bimodal acquiescence from 0% to 100% across 19 models with an LLM judge validated at kappa 0.957 — was deliberately NOT used**, because it is an unrefereed preprint and this list does not lean on preprints for comparator numbers.

**Positive practice worth carrying forward.** **Co-primary outcomes covering both error directions, prespecified**, with the sampling frame built to make the second measurable (technique 330). **A confidence interval computed at the correct clustering level**, at visible cost to the apparent precision (327). **A per-recommendation decomposition in the abstract**, which is the only reason the concentration is detectable — and which entry 76, also abstract-only, lacked entirely. **A conclusion narrower than the data would have allowed.** **An explicit refusal of the most quotable extension** ("Findings may not extend to consumer-facing use"). **Providers and dates stated.** **Funding explicitly none.**

**What caps this at 3/5.** **Abstract only**, with four access routes documented. **No reliability statistic for the LLM judge** (329), where a verified comparator reports 0.89–0.94. **No human comparator** (286). **The headline is an unweighted mean over topics** (328), with ~88% of the overuse in 2 of 15, and the clinically relevant weighting would plausibly raise it. **Six models pooled with no breakdown**, against a verified 43-point between-model spread. **Three runs cannot characterise run-to-run instability** and none is reported, against a verified comparator finding consistency as low as 0.60. **False restraint rests on ~8 events.** **15 recommendations selected from hundreds with no stated method**, and **the scenarios and their answer key were authored by the same three investigators.** **Six unnamed models on production APIs**, so not replicable even in principle. **No reporting guideline visible; TRIPOD-LLM fits.**

**Why not 2:** entry 77 scored 2 for a mismatch between claim and evidence. **There is no mismatch here** — the design does what the title says, the interval is honest about precision, and the conclusion is correctly bounded. **Why not 4:** entry 79 earned a 4 by advancing a falsifiable thesis and quantifying it with counter-evidence included. **This is a competent benchmark read through an abstract.** **It is a 4 if the full text reports the judge's agreement, the fifteen per-recommendation rates, and the six models separately — all three of which re-report data already collected.** **Standing offer: this entry will be upgraded if a PMC body appears**, as for entries 68 and 76.

**Reporting-guideline pattern — and entry 76 predicted this paper's gaps specifically.** 71, 73, 74, 75, 77, 78 named none; 69 named TRIPOD+AI with the checklist; 70 named STROBE; **76 measured the phenomenon at 40% mean completeness against TRIPOD-LLM**; 79 named six instruments and applied them; 80 named TRIPOD with a deposited checklist; 81 named none; **82 names none visible in its abstract.** **The standing rule is unchanged — naming a checklist does not predict quality, so read the methods.** **But entry 76's specific finding lands here with unusual precision**: it reported that completeness was worst on **model versioning and access modality, inference parameters, and output postprocessing**, and those are exactly the three things missing from this abstract. **Caveat recorded: they may be present in the full text, and what I can verify is only that they are absent from the abstract most readers will see.**

**Deferred status, 2026-11-19.** ***Annals* Choosing Wisely (42896192) — DECODED TODAY as entry 82, abstract-only at day 30**, closing a deferral opened on 2026-10-28. **Gait foundation model (42995231) — day 11, re-checked today, still no PMC copy**; abstract-only date **2026-11-30**, eleven days out. It carries the largest multiplicity problem this list will have faced — **1,887 of 3,210 tested phenotypes called significant** — and the first question for it is what false-discovery-rate procedure ran across those 3,210 tests. **Note the connection formed today: that paper's problem is the mirror image of this one's.** Entry 82 has **15 independent units dressed as 4,050**; the gait paper has **3,210 tests whose dependence structure determines whether 1,887 "significant" findings mean anything.** Both are questions about how many independent things were really examined.

**Plan set on 2026-11-19.** **Next run takes shelf item (G)** — **SOFA score recalibration by ML-guided optimisation**, PMID 43024933, PMC13766654, *JMIR Med Inform* 2026, eICU database, 208 US hospitals, 14,848 admissions. **Three reasons, unchanged from yesterday and now reinforced.** It **learns integer weights for a legacy point score rather than replacing it with a black box**, testing the simple-versus-complex question entries 80 and 81 both raised. It uses **10-fold nested cross-validation grouped by hospital** — the grouped-CV check entry 81 did not run (319), and now also the clustering question entry 82 has made central (327): **a study that clusters its cross-validation by site is answering the same question as a study that clusters its confidence interval by recommendation.** And it excludes **133,684 of 148,532 encounters (90%) for at least one missing measurement**, the largest exclusion fraction this list will have examined. **Two questions written down now, before reading. (1) What does a 90% complete-case exclusion do to who is left — is the remaining 10% a sicker, more heavily monitored population, and does the paper characterise the 90% it dropped?** (2) **Does the recalibrated integer score beat the original SOFA by more than the selection noise** — i.e. is the comparison made on data untouched by the recalibration, and is the margin larger than the fold-to-fold spread? **Shelf after today: four spares — (H), (I), (J), (K).**

**Standing watch item:** PM Heart trial results (protocol PMID 42893738), quarterly.
