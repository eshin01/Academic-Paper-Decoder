# Artificial intelligence versus clinicians: systematic review of design, reporting standards, and claims of deep learning studies

- **Authors:** Myura Nagendran, Yang Chen, Christopher A. Lovejoy, Anthony C. Gordon, Matthieu Komorowski, Hugh Harvey, Eric J. Topol, John P. A. Ioannidis, Gary S. Collins, Mahiben Maruthappu (Imperial College London, UCL, Stanford METRICS, University of Oxford, Scripps)
- **Venue:** The BMJ, 2020;368:m689 (published March 25, 2020)
- **DOI link:** https://doi.org/10.1136/bmj.m689
- **PubMed link:** https://pubmed.ncbi.nlm.nih.gov/32213531/ (PMID 32213531)
- **Full-text link:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7190037/ (PubMed Central, open access)
- **Basis:** FULL TEXT — introduction, results, discussion, methods, and stated limitations retrieved from PubMed Central. Competing-interest and funding statements were not present in the retrieved manuscript text; PubMed tags non-US-government research support. Identifiers verified against the live PubMed/NLM record.
- **Registration:** PROSPERO CRD42019123605.
- **Decoded:** 2026-09-09

---

# The Gist

Yesterday's paper asked whether the "AI beats doctors" studies agree with each other. This one asks a harsher question: **are those studies any good?** A team including two of medicine's most prominent methodology critics went through every study comparing a deep-learning imaging algorithm against expert clinicians, and formally graded each one for bias and reporting quality. The findings are blunt. Of 81 such studies, only nine were prospective and just six were ever tested in a real clinic. The typical study compared its algorithm against only **four experts**. Data was unavailable in 95% of studies and code in 93%. Nearly three-quarters were rated at high risk of bias. And 61 of 81 abstracts claimed the AI was at least as good as clinicians — while **not one** of the 23 studies claiming outright superiority mentioned in its abstract that further trials were needed.

# Study Snapshot

- **Study type:** Systematic review of study *quality* — it does not pool accuracy results, it grades methods. Pre-registered on PROSPERO. Uses formal validated instruments: **PROBAST** for bias in non-randomised prediction studies, the Cochrane tool for randomised ones, **TRIPOD** for reporting standards, and CONSORT for trials.
- **The search:** Medline, Embase, the Cochrane Central Register of Controlled Trials, and the World Health Organization trial registry, 2010 to June 2019.
- **What it found:** just **10 records** for randomised deep-learning trials — two published, eight still running — plus **81 non-randomised studies**.
- **How realistic those 81 were:** only nine (11%) were prospective, and only six were tested in a real clinical environment. Radiology accounted for 44%, ophthalmology 21%, dermatology 11%.
- **The human comparator:** a median of five clinicians per study, of whom a median of **four** were experts (range 1 to 91).
- **Transparency:** public data in four studies (5%), code in six (7%), and **both in exactly one study**.
- **Risk of bias:** **58 of 81 (72%) rated high risk**, with the "analysis" domain worst — specifically whether enough participants were included, whether all were analysed, whether performance measures were appropriate, and whether overfitting was accounted for.
- **Reporting:** adherence below 50% for 12 of the 29 TRIPOD items; overall median adherence 62%. Only 17% reported a sample-size calculation. Only 31% included a flowchart of how patients moved through the study.
- **A number that explains a lot:** the median rate of disease in these test sets was about **44%** — roughly one case in every two, in fields where real-world rates are often one in a hundred or far less.
- **The claims:** 61 of 81 abstracts said AI was at least comparable to clinicians — superior in 23 (30%), comparable-or-better in 13, comparable in 25, helpful to clinicians in 14, and not superior in just two. Only nine abstracts noted that prospective trials were still needed, and **none of the 23 superiority-claiming studies did**. Seven studies stated the algorithm was ready for clinical use, though only two of those seven had ever been tested prospectively.
- **One detail that says everything:** the authors note a retrospective study that "gave a website address in the abstract for patients to upload their eye scans and use the algorithm themselves."

# How Strong Is This Evidence?

**Grade: 5/5 — for the question it asks, this is about as strong as medical evidence gets.**

An important distinction before the praise: a 5/5 here is a judgment about *this paper's reliability*, not an endorsement of AI or a verdict against it. The paper's finding happens to be critical, but the grade reflects how trustworthy the appraisal is.

Why it earns the top mark: it asks a well-defined question, pre-registers its plan, searches trial registries as well as journals (catching the eight unpublished ongoing trials that a journal-only search would miss), and — crucially — applies **formal, validated risk-of-bias instruments** rather than the authors' impressions. That last point is exactly what yesterday's Lancet review explicitly declined to do. Its conclusions are simple counts anyone can check, its author list includes the people who wrote the reporting standards being applied, and its limitations section is genuinely self-critical: the search may have missed studies, TRIPOD and PROBAST were built for conventional prediction models rather than deep learning, the findings cover imaging only, and bias judgments involve subjectivity.

# The Editor's Concerns

- **The tools were borrowed.** TRIPOD and PROBAST were designed for traditional statistical prediction models, not neural networks. The authors say so themselves, and it means a low adherence score partly reflects a checklist asking for things (like listing every predictor variable) that do not translate to deep learning. The reporting problem is real; the exact percentages should be read with that caveat.
- **Imaging only.** Everything here concerns diagnostic medical imaging. The authors are explicit that they cannot generalise to other medical AI — which, notably, would exclude several papers on your own list, such as the electronic-health-record and sepsis work.
- **Bias grading involves judgment.** Different reviewers with different experience could rate borderline studies differently. Formal tools reduce this but do not eliminate it.
- **A snapshot from 2019.** The literature has moved on; reporting standards this paper helped prompt (CONSORT-AI, SPIRIT-AI, TRIPOD extensions) now exist. Whether adherence has actually improved is a separate empirical question this paper cannot answer.
- **It counts claims, not truth.** A study claiming superiority might be right. The finding is that these claims routinely outrun the evidence supporting them — not that every algorithm is worse than advertised.
- **What this study did well:** pre-registration; searching trial registries alongside journals; formal validated instruments applied consistently; separating what studies *found* from what they *claimed*, which is the innovation here; reading both abstracts and discussion sections, since spin concentrates in abstracts; quantifying transparency precisely rather than complaining generally; and an author list combining domain clinicians with the methodologists who wrote the standards.

# Statistics Spotlight

**1. Formal risk-of-bias assessment — the difference between opinion and appraisal.**
- *What it is:* A structured instrument that walks a reviewer through pre-set questions about a study's design and analysis, producing a rating that another reviewer could reproduce. PROBAST, used here, poses 20 signalling questions across four domains: participants, predictors, outcomes, and analysis.
- *How this paper used it:* Every one of the 81 non-randomised studies was scored. **58 (72%) came out at high risk of bias**, and the "analysis" domain failed most often — chiefly on whether the sample was large enough, whether everyone enrolled was actually included in the results, whether the right performance measures were used, and whether overfitting was accounted for.
- *The theory, with an analogy:* Think of the difference between a friend saying a used car "seems fine" and a mechanic working through a standard inspection checklist. The checklist does not guarantee a perfect judgment, but it makes the judgment consistent, comparable across cars, and auditable by someone else. Notice that this is precisely the step yesterday's Lancet review skipped — which is why that review had to treat a careful study and a sloppy one as equals in its pooled average.
- *Watch out:* "High risk of bias" does not mean "the result is wrong." It means the study's design leaves room for the result to be wrong in a predictable direction, so you cannot rely on it as it stands. When you read any systematic review, look for whether a named tool (PROBAST, QUADAS-2, Cochrane RoB) was applied — and if the review says nothing about risk of bias, that silence is itself information.

**2. The retrospective-to-prospective collapse — the most important number in the paper.**
- *What it is:* The gap between how an algorithm performs on stored data and how it performs when actually deployed on patients in real time.
- *How this paper used it:* The review surfaced one of the two completed randomised trials — 350 children at eye clinics in China, randomised to cataract assessment with or without an AI platform. The same algorithm that had scored **98% accuracy in a non-randomised test scored 87% in the randomised trial**. Meanwhile senior consultants scored **99%**. For treatment recommendations the fall was steeper: 93% down to 71%, with specificity of just 44%. Patients were nonetheless *more satisfied* with the AI, because it was faster.
- *The theory, with a worked example:* Imagine a chess program tested by replaying famous games — it looks brilliant, because every position it faces was reached by good players and is well-represented in its training. Put it in a live tournament and it meets strange positions, time pressure, and situations nobody curated for it. Its rating drops. Retrospective medical data is the replayed game: pre-selected, pre-cleaned, and complete. Real patients arrive in the wrong order, with missing tests and confusing presentations.
- *Watch out:* This single trial is the empirical answer to every retrospective paper on your reading list, including the ones with the most impressive AUCs. It also shows the failure runs both ways: patients preferred the faster, less accurate option. Speed and satisfaction are real benefits, but they are not accuracy, and a study measuring one should never be quoted as evidence of the other.

**3. Claim inflation — measuring spin as a countable phenomenon.**
- *What it is:* The gap between what a study's data support and what its abstract asserts. The authors treat this as data: they read every abstract and classified its claim, then checked whether the appropriate caveat appeared.
- *How this paper used it:* 61 of 81 abstracts claimed AI was at least comparable to clinicians. Only nine included a caveat that prospective trials were needed — and **none of the 23 studies claiming outright superiority did**. Even in the fuller discussion sections, only 31 of 81 (38%) called for prospective work. The pattern is striking: the stronger the claim, the less likely the caveat.
- *The theory, with an analogy:* Think of a job applicant's résumé versus their references. The résumé is optimised to be read quickly and to impress; the references contain the qualifications. Abstracts are résumés. The authors also point out why this matters beyond academia, citing evidence that patients are more likely to believe a treatment works when news coverage is written with spin, and that false news spreads faster online than true news. An overstated abstract is not a private sin — it is the input to the whole public information chain.
- *Watch out:* This is the most directly useful finding for anyone who reads science through headlines. The claim in an abstract is a *claim*, not a result. Two habits defuse it: check whether the abstract's confidence is matched by a limitations paragraph in the body, and be most suspicious of the strongest claims, since this paper shows they carry caveats least often.

# Jargon Translator

- **Systematic review:** a study of studies, gathered by rules set in advance so the conclusion cannot be built from cherry-picked papers.
- **Prospective:** planned in advance and carried out going forward on new patients — as opposed to retrospective, which analyses records of things that already happened.
- **Randomised trial:** patients are assigned by chance to receive one approach or another, the only design that reliably shows a tool actually changes outcomes.
- **PROBAST:** a validated checklist for judging risk of bias in studies that build prediction models.
- **TRIPOD:** the reporting standard specifying what a prediction-model study must disclose.
- **CONSORT:** the equivalent reporting standard for randomised trials.
- **Risk of bias:** the extent to which a study's design could push its result in a particular direction, regardless of whether it actually did.
- **Overfitting:** when a model learns the quirks of its training data rather than the real pattern, so it looks better in testing than it will in practice.
- **Event rate:** the proportion of the test set that actually has the disease — about 44% here, versus far lower in real screening populations.
- **Adenoma detection rate:** in colonoscopy, the proportion of procedures finding a pre-cancerous growth; a standard quality measure.
- **Spin:** presenting results more favourably than the data support, usually by omission rather than falsehood.

# What You Can (and Can't) Say

**Fair to say:**
- "A 2020 BMJ systematic review found that of 81 studies comparing deep learning with clinicians on medical images, only nine were prospective, six were tested in a real clinical setting, and 72% were at high risk of bias."
- "The typical study compared its algorithm against a median of four experts, and data and code were unavailable in 95% and 93% of studies respectively."
- "61 of 81 abstracts claimed AI was at least comparable to clinicians, and none of the 23 claiming superiority mentioned in the abstract that further trials were needed."
- "In one of only two completed randomised trials, the same cataract algorithm fell from 98% accuracy in retrospective testing to 87% in the trial, while senior consultants scored 99%."

**Not fair to say:**
- "This proves medical AI doesn't work" — it assesses how well studies were done and reported, not whether algorithms are effective. High risk of bias means unproven, not disproven.
- "AI is worse than doctors" — one small randomised trial in one task found that; the review's point is that almost nobody has run the trials that would tell us either way.
- "These findings apply to all medical AI" — the authors explicitly limit them to diagnostic imaging.
- "Nothing has changed since" — this is a 2019 snapshot that helped prompt the reporting standards now in place.

# Bottom Line for Your Life

This is the paper that explains why the previous ten entries on your reading list needed such careful reading. It quantifies the machinery of scientific overclaiming: the strongest assertions carried the fewest caveats, the human comparison groups were tiny, almost nothing was tested on real patients, and the underlying materials were essentially never available for anyone to check. The most valuable single fact to carry away is the cataract trial — **98% on stored data, 87% on real patients, against 99% for the human consultants** — because it converts an abstract worry into a measured number. When you next see a study cited as proof that some technology matches or beats doctors, three questions now do almost all the work: was it prospective, how many humans was it compared against, and did the abstract admit what was still unknown? One study is one data point, and this one is a study of how often those data points are dressed up. This is an educational breakdown, not medical advice.

---

**Sources** (based on articles retrieved from PubMed / PubMed Central; identifiers verified against the live NLM record — URL browsing is blocked in this environment, so links are constructed from that verified record):
- DOI: https://doi.org/10.1136/bmj.m689
- PubMed: https://pubmed.ncbi.nlm.nih.gov/32213531/
- Full text (PMC, open access): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7190037/
- Protocol registration: PROSPERO CRD42019123605
