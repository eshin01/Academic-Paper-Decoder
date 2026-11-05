# Clinician Use of an Artificial Intelligence-Enabled Clinical Information Platform

**Authors:** Patel VR, Finlayson SG, Liu-Hass M, Ray M, Burk-Rafel J, Zack TI, Jena AB (seven authors — Harvard Medical School and Brigham and Women's Hospital, Boston; Massachusetts General Hospital, Boston; NYU Grossman School of Medicine, New York; Seattle Children's Hospital, Seattle; National Bureau of Economic Research, Cambridge. **Three of the seven authors — Finlayson SG, Ray M and Zack TI — are at OpenEvidence, Miami, Florida: the company that owns and operates the platform this paper studies.** That is disclosed on the author line itself, in the affiliations, which is the right place for it.)
**Journal:** JAMA, 2026 (published 15 October 2026)
**Decoded:** 2026-11-05

**Analysis basis:** **ABSTRACT ONLY.** This is the first abstract-only decode in this reading list since entry 10, and it is not a shortcut — it is the end of a twenty-one-day attempt.

**Why, exactly.** A PubMed Central record for this paper exists (PMC13673371) and has existed since the day it was indexed. **It serves an empty body.** I requested the full text from PMC on every one of the twenty-one consecutive days from 2026-10-16 through 2026-11-05 inclusive, and on every one of those days the `full_text` field returned as an empty string while the structured abstract returned complete. That is not a transient failure; it is a PMC record created for the citation and the abstract with no deposited body text, which is normal for JAMA's author-manuscript pipeline in the months after publication. The second route, Scite's indexed full text, was tried today against the DOI and returned the paid-plan error: *"MCP tools require a paid scite plan or an active free trial."* Direct URL fetching is blocked from this session because `doi.org` does not resolve under the network policy here. **Three independent routes, all closed.** The daily trigger's own instruction says to fall back to abstract-only only when full text is genuinely inaccessible and to say so explicitly in the analysis. That condition is now met and this paragraph is the explicit statement.

**What that costs you, stated plainly.** Everything in Section 2 below that is marked "not reported" is not a criticism of the authors — JAMA abstracts are capped at 350 words and the Methods almost certainly answer several of these questions. It means **I have not seen the answers and will not pretend to have.** Where a judgement in Section 3 or 4 depends on something only the Methods could settle, I say which way it would move if the Methods are good.

**Source links (verified):**
- DOI: https://doi.org/10.1001/jama.2026.21868
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42879271/
- PubMed Central record (exists, but serves no body text — **this is not the full-text link used, because there is no full text to link to**): https://pmc.ncbi.nlm.nih.gov/articles/PMC13673371/

**Basis of link verification.** Direct URL fetching is blocked from this session, so verification was done against the live PubMed/NLM record. According to PubMed, a query for PMID 42879271 returned this exact title, these seven authors with these affiliations, the journal JAMA, a publication date of 15 October 2026, DOI `10.1001/jama.2026.21868` and PMC ID `PMC13673371`. Every element of every link above comes from that record. **Nothing is guessed.** JAMA volume, issue and page numbers are **not present in the PubMed record** as of today, so they are not stated above rather than being inferred.

**Funding and competing interests: not available to me.** JAMA publishes both in a Conflict of Interest Disclosures section that is not part of the abstract. **I am not reporting them, because I have not read them.** What I can report is what the author line itself says, which is in the header above: three of seven authors are employees of the company whose product is the subject. Readers should go to the paper for the full disclosure statement; it will be more detailed than the affiliations.

**Ethics:** not stated in the abstract. A study of de-identified platform telemetry would normally carry an IRB exemption or a non-human-subjects determination. The abstract's statement that the data are "clinicians with National Provider Identifier-verified accounts" tells you the unit of analysis is the clinician, not the patient — no patient data are described anywhere in the abstract.

---

## 1. The Gist

**Nearly a million American clinicians asked an AI 271 million clinical questions in two and a half years, and this paper is the first real measurement of that.**

Not a trial. Not an accuracy study. A **census of behaviour** — who opened the tool, how often, and what they asked about. For a field that has spent a decade publishing model performance and almost nothing about use, that is a genuinely new kind of evidence, and it is the reason this paper matters even though it cannot tell you whether a single answer was correct.

**The three findings that would change how you think about medical AI:**

**It is not the specialists.** The heaviest users relative to their share of the workforce are **physicians within ten years of graduating (use ratio 2.54)** and **residents and fellows (1.84)** — the people still building their reference knowledge. Among specialties, oncology and haematology (2.00), internal medicine (1.88) and family medicine (1.80) lead; **ophthalmology (0.23), radiology (0.24) and orthopaedics (0.24) barely show up.** The pattern is not "AI for the technologically sophisticated." It is **AI for the cognitively broad** — the clinicians whose day involves an unbounded range of questions rather than a deep narrow one.

**It is not diagnosis.** The popular story about medical AI is the diagnostic puzzle. The actual queries are **treatment and management (33.1%)**, with **diagnosis at 13.9%** — less than half as much. Clinicians are not mostly asking "what is this?" They are asking **"what do I do about it?"**

**It is not physicians who use it hardest.** **Nurse practitioners (44.5 queries per active user-month) and physician assistants (44.5)** out-query **physicians (37.1)** by about 20%. And **35% to 88% of queries are about topics outside the clinician's own specialty** — the low end being oncologists and haematologists, the high end emergency physicians.

**What the paper does not say, and deserves credit for not saying:** it does not claim the tool helped anyone. The conclusion is a description of use and stops there. In a literature full of papers that measure one thing and conclude another, that restraint is worth noting at the top.

## 2. Study Snapshot

**Study type:** labelled a **cross-sectional study** by the journal. It is more precisely a **retrospective descriptive analysis of proprietary platform telemetry**, with a longitudinal time series inside it (monthly active users and queries per user tracked across 30 months). There is no comparison group, no randomisation, no intervention and no outcome in the clinical sense. Section 4 returns to the label.

**Platform:** OpenEvidence, described in the abstract as "a commonly used AI-enabled clinical information platform."

**Period:** 1 January 2024 through 30 June 2026 — **30 months**, which the abstract calls 2.5 years.

**Population:** **952,008 clinicians** with National Provider Identifier-verified accounts, of whom **556,200 are physicians** (58.4%) and the remaining 395,808 (41.6%) are other clinician types, with nurse practitioners and physician assistants named. **58.5% female** overall.

**Volume:** **271 million queries** over the period.

**The classified subset:** a **stratified random sample of 38.8 million queries** — **14.3% of the total** — had their clinical purpose and topic area assigned by **a large language model**. Every percentage in the purpose and topic findings comes from this subset. **Which large language model, and with what accuracy, is not stated in the abstract.** Whether any human adjudicated the labels is not stated.

**Stated outcome measures, four of them:**
- the number of active users and clinical queries
- the share of queries relative to representation in the national workforce (the "use ratio")
- the clinical purpose of queries
- the topic of queries

**Growth, as reported:**
- monthly active users: **355 in January 2024 to 703,265 in June 2026** — a 1,981-fold increase
- average monthly queries per active user: **18.0 to 39.5** — a 2.19-fold increase

**Intensity by clinician type, queries per active user-month:** nurse practitioners **44.5**, physician assistants **44.5**, physicians **37.1**.

**Use ratios by career stage:** physicians within a decade of graduation **2.54**; residents and fellows **1.84**.

**Use ratios by specialty:** oncology and haematology **2.00**; internal medicine **1.88**; family medicine **1.80**; ophthalmology **0.23**; radiology **0.24**; orthopaedics **0.24**.

**Query purpose:** clinical decision-making **51.9%**, within which treatment and management **33.1%**; diagnosis **13.9%**.

**Out-of-specialty queries:** **35%** among oncologists and haematologists rising to **88%** among emergency department physicians.

**What is not reported in the abstract, and therefore not known to me:**
- the definition of an "active" user and the window used
- the national workforce denominators behind every use ratio, and their source
- the identity and measured accuracy of the classifying language model
- whether any human validated the classifier, and with what agreement
- how "outside the clinician's own specialty" was operationalised
- how accounts were deduplicated, and how bot or shared institutional use was excluded
- any confidence intervals, on anything
- whether any answer was correct, and whether any patient was affected

**No reporting guideline is named in the abstract.** STROBE is the one that fits a cross-sectional observational study; whether the paper cites it is not visible from here.

## 3. How Strong Is This Evidence? (Grade 2 out of 5)

**The grade is capped by access and auditability, not by candour, and not by the size of the dataset.** This needs spelling out, because 271 million is the largest number this reading list has ever reported and it would be easy to mistake size for strength.

**What genuinely earns credit:**

**The conclusion matches the data.** The abstract's conclusion says clinicians submitted a lot of queries, that use varied by type, specialty and career stage, and that it was frequently for treatment decisions rather than diagnostic tasks. Every clause of that is a description of the telemetry. **There is no leap to benefit, accuracy, safety or outcomes.** Compare this to the thirty-odd model papers in this list that measured an AUC and concluded something about patient care.

**The conflict is disclosed in the most visible place available.** Three OpenEvidence employees, named with that affiliation, on the author line of a JAMA paper. Not buried in a footnote.

**The use-ratio framing is the right one.** Reporting raw query counts by specialty would have said nothing except "internal medicine is big." Normalising to each group's share of the national workforce is the correct construction and is what makes the ophthalmology-versus-oncology contrast interpretable at all.

**The scale is real and it is the point.** This is not a convenience sample of 200 clinicians at one academic centre answering a survey about whether they would hypothetically use AI. It is the actual behaviour of most of a national workforce. **No study design other than platform telemetry can produce this**, and the honest response is that the dataset is irreplaceable even though its provenance is a problem.

**What caps it at 2:**

**Nobody outside the company can check any of it.** The data are proprietary server logs. There is no replication path, no independent audit, no data availability statement that could matter — you cannot deposit 271 million clinician queries. **Three of the seven authors work for the company, and the company's commercial interest is in exactly the finding the paper reports: that clinicians use the product enormously and increasingly.** That is not an accusation of misconduct. It is a statement that the usual safeguard — someone else can re-run it — is structurally unavailable here, and the authors with access to the raw data are the ones with the interest in the result.

**Every interpretive percentage was produced by an unvalidated model.** The counts (952,008; 556,200; 271 million) are billing-grade telemetry and I would believe them. **The percentages are not.** "Clinical decision-making 51.9%", "treatment and management 33.1%", "diagnosis 13.9%", "out-of-specialty 35% to 88%" — all of these are the output of a large language model classifying 38.8 million free-text queries, with **no stated accuracy, no stated human adjudication and no stated inter-rater agreement.** Section 5 works through why that matters more than the sample size helps.

**I read the abstract.** A grade is a judgement about methods, and I have not seen the Methods. If they report classifier validation against a human-labelled gold standard with good agreement, the stated workforce denominators, a clean active-user definition and a deduplication procedure, **this moves to 3 out of 5** on the strength of the scale and the disciplined conclusion. It would not go higher than 3 while the data remain unauditable and the sponsor is an author.

**Why not 1 out of 5.** Because the thing it claims to measure is the thing it measured. A 1 in this list is reserved for papers whose conclusions are not supported by their own numbers. This paper's conclusions are supported by its numbers. The question is whether anyone can check the numbers.

## 4. The Editor's Concerns

**1. The use ratio is a closed system, and the abstract reads it as if it were an open one.** This is the most important methodological point in the paper and Section 5 derives it properly. In short: a use ratio is a share divided by a share, so **across the whole workforce the ratios must average to exactly 1.0** when weighted by workforce size. Internal medicine and family medicine are two of the largest specialties in American medicine, and the paper puts both near 1.85. That contribution alone forces most of the rest of the workforce below 1.0 **as a matter of arithmetic.** My reconstruction — using approximate workforce shares, so illustrative rather than exact — has the named high-use groups holding roughly 37% of the physician workforce and contributing about 0.56 of the total, which means **the remaining 63% must average about 0.70.** So "use was lower in procedural and diagnostic specialties" is partly a finding and partly an accounting identity. The genuinely informative numbers are not that ophthalmology is below 1 — something had to be — but **how far** below: 0.23 is a quarter of proportional use, which is far beyond what the constraint requires.

**2. The outcome variable is a model output, and no accuracy is given.** Everything in the purpose and topic findings rests on a language model's classification of 38.8 million queries. **Measurement error in an outcome does not shrink with sample size.** If the classifier systematically confuses "what dose?" (treatment) with "is this drug causing this?" (diagnosis), that bias sits in the 33.1% and the 13.9% unchanged whether you classify 38.8 million queries or 38,800. The abstract gives no accuracy, no gold standard, no human adjudication. The *Annals of Internal Medicine* paper still sitting on this list's deferred shelf uses the phrase "responses classified by LLM judge with physician adjudication" **in its own limitations section** — which is exactly the sentence this abstract does not contain. It may well be in the Methods.

**3. "Out-of-specialty" is close to definitional for the specialty at the top of the range.** Emergency medicine at **88%** out-of-specialty is the paper's most eye-catching number and probably its least meaningful one. Emergency medicine *is* the specialty of undifferentiated presentation; a topic map that assigns "chest pain in a diabetic" to cardiology or endocrinology will label almost everything an emergency physician asks as out-of-specialty. **The number is measuring the topic taxonomy as much as the clinician.** The 35% at the oncology end is the more interpretable figure, because oncology has a genuinely bounded topic domain.

**4. The "whereas" in the purpose finding compares two siblings, not a child to its parent.** The abstract says most queries addressed clinical decision-making (51.9%), **particularly** treatment and management (33.1%), **whereas** diagnosis accounted for 13.9%. Check the arithmetic: 33.1 + 13.9 = 47.0, which fits inside 51.9 with 4.9 points to spare. So treatment and diagnosis are both **sub-categories of clinical decision-making**, and the contrast is between two children of the same parent. That is a legitimate and interesting contrast — it is the paper's best finding — but the sentence structure invites you to read 13.9% as small against 51.9%, which would be comparing a part to its own whole. Read it as 33.1 against 13.9: treatment questions outnumber diagnostic ones by about **2.4 to 1.**

**5. A 2,000-fold growth in users makes every period-wide average an average over a different population.** 271 million queries over 30 months sounds like a stable rate. It is not. My arithmetic from the paper's own endpoints: June 2026 alone accounts for about **27.8 million queries, which is 10.3% of the entire study's volume in one month out of thirty.** The "2.5-year study" is dominated by its last few months. Any statistic quoted for the whole period is weighted toward the most recent, largest and least established cohort of users. Section 5 shows what else those endpoints give away.

**6. Rising intensity in a growing population has at least three explanations and telemetry separates none of them.** Queries per active user went **18.0 to 39.5** while the user base grew 1,981-fold. The product may have got better. Users may have learned to lean on it more. Or **the people who stayed are the ones who liked it** — survivorship, which operates most strongly in the early cohorts that have had the longest to churn. A server log cannot distinguish a behaviour change within people from a composition change between people. You would need to follow fixed cohorts, and the abstract does not say whether the paper does.

**7. Registered accounts, active accounts and people are three different denominators.** 952,008 clinicians have accounts; 703,265 were active in the final month — **73.9% of every account ever created was active in month 30**, which is a strikingly high retention figure and also a sign that most accounts were created recently. Meanwhile 271 million queries across 952,008 accounts over 30 months is **9.5 queries per account-month on average**, against the 39.5 reported per *active* user-month — a 4.2-fold gap confirming that most account-months are inactive. None of these numbers is wrong; they are answers to different questions, and the abstract moves between them without flagging the switch.

**8. No comparator, so no displacement story.** We learn nothing about what these 271 million queries replaced. UpToDate, a colleague down the hall, PubMed, a Google search, or nothing at all — each implies a completely different conclusion about what this technology is doing to medicine. This is an inherent limit of single-platform telemetry, not a flaw in the execution, but it bounds what the paper can mean.

**9. The "cross-sectional" label fits awkwardly.** A cross-sectional study measures a population at one point in time. This measures a growing population continuously over 30 months and reports its trajectory. The design is closer to a **retrospective open-cohort descriptive time series.** The label matters because it determines which reporting checklist a reader expects (STROBE cross-sectional) and which biases they go looking for.

**10. A check the paper passes, and it is worth saying so.** The reported **58.5% female** across a population that is 58.4% physicians and 41.6% nurse practitioners, physician assistants and others is internally consistent. Taking the US physician workforce as roughly 38-40% female and the NP and PA workforce as roughly 85% female, the predicted overall share is **57.5% to 58.7%** — which brackets 58.5% neatly. The sex distribution is what the occupational mix predicts. That is a genuine, if small, piece of evidence that the population is what the paper says it is.

## 5. Statistics Spotlight

Nine techniques, numbered from 185 in the running list in `queue.md`. The first three are the load-bearing ones.

**A use ratio is a closed system. Its weighted average is forced to be exactly 1.**

A use ratio here is: *that group's share of all queries* divided by *that group's share of the national workforce.* Write it as $R_i = q_i / w_i$, where $q_i$ is the query share and $w_i$ the workforce share.

Now notice that both the $q_i$ and the $w_i$ are shares of the same thing, so each set sums to 1. Multiply each ratio by its own workforce weight and add them up:

$$\sum_i w_i R_i = \sum_i w_i \cdot \frac{q_i}{w_i} = \sum_i q_i = 1$$

**The workforce-weighted mean of every use ratio in the study is 1.0, as a matter of definition.** Not approximately. Exactly. There is no dataset in which it could come out otherwise.

Why this matters for reading the paper: if you learn that some large groups are well above 1, you have already learned that other groups must be below 1, without being told anything about them. Internal medicine and family medicine between them are a large fraction of American physicians, and the paper puts both near 1.85. Using approximate workforce shares — internal medicine around 15%, family medicine 12%, radiology 4%, oncology/haematology 2%, ophthalmology 2%, orthopaedics 2% — the six named groups hold about 37% of the workforce and contribute about 0.557 toward the required total of 1. So the unnamed 63% must average $(1 - 0.557)/0.63 \approx 0.70$.

**So the shape of the finding was partly fixed before any data arrived.** What is *not* fixed, and is therefore the real information, is the magnitude: 0.23 for ophthalmology is a long way below the 0.70 the constraint merely requires. That gap is the finding. The sign is arithmetic; the size is evidence.

**How to use this on your own work.** Any time you see a metric built as *share divided by share* — a standardised morbidity ratio, an observed-to-expected ratio, a representation index, a location quotient, a lift in a marketing model — ask what the weighted average is pinned at. If it is pinned at 1, then "above average" and "below average" are not independent findings about separate groups. They are two halves of one constraint. **Report how far, not just which side.**

**When the outcome variable is produced by a model, sample size buys you nothing.**

This is the single most useful idea in this paper and it generalises everywhere.

Split the error in any measurement into two parts. **Sampling error** is the luck of which units you happened to observe; it shrinks as $1/\sqrt{n}$. **Measurement error** is the systematic gap between what your instrument records and what is true; it does not shrink with $n$ at all. More observations through a bent ruler give you a very precise estimate of the wrong length.

Here is the arithmetic for this paper. The classified subset is 38.8 million queries. For the reported 51.9%, the binomial standard error is

$$SE = \sqrt{\frac{p(1-p)}{n}} = \sqrt{\frac{0.519 \times 0.481}{38{,}800{,}000}} = 0.000080$$

which is **0.0080 percentage points**, giving a 95% interval of roughly 51.884% to 51.916%. For the 33.1% it is 0.0076 points; for the 13.9%, 0.0056 points. **The sampling uncertainty on every purpose percentage in this paper is about one hundredth of a percentage point.** It is invisible. It is irrelevant.

Now suppose the classifying model is 90% accurate — a perfectly respectable figure for free-text classification into clinical purpose categories, and one that nobody in the field would be embarrassed by. If its errors are symmetric and it misreads 10% of treatment queries as diagnostic and vice versa, the observed split between two categories with true shares $t$ and $d$ becomes

$$\text{observed } t = 0.9t + 0.1d, \qquad \text{observed } d = 0.9d + 0.1t$$

With true shares of 35% and 12%, you would observe 32.7% and 14.3% — which is close to the reported 33.1% and 13.9%. **A 10% symmetric classifier error moves these numbers by two percentage points, which is 250 times the sampling uncertainty.** Asymmetric error moves them further and in one direction.

**The lesson: when $n$ is enormous, stop reading the confidence intervals and start asking about the instrument.** The confidence intervals are theatre at this scale. The question that determines whether 33.1% means anything is: *how was a query assigned to "treatment and management", and how often was that assignment right?* That question has an answer, and it is in the Methods, and I have not read it. This is precisely why abstract-only is a real limitation rather than a formality.

**Entry 157 in this list taught that post hoc power is circular. This is its mirror image:** with $n$ in the tens of millions, power and precision are solved problems and **validity is the entire question.** A huge sample does not make a study strong. It makes a study precise. Those are different words for different things, and conflating them is how a reader ends up believing a classifier they have never seen.

**The total divided by the final period recovers the shape of a growth curve when only the endpoints are published.**

The abstract gives two points: January 2024 and June 2026. It gives no trajectory. But it also gives the total, and the total constrains the middle.

Compute the endpoints as monthly query volumes:

- January 2024: $355 \times 18.0 = 6{,}390$ queries
- June 2026: $703{,}265 \times 39.5 = 27{,}778{,}968$ queries

Now define the **effective number of final-volume months**: total queries divided by final-month queries.

$$\frac{271{,}000{,}000}{27{,}778{,}968} = 9.76$$

So the whole 30-month study contains as many queries as **9.76 months at the final rate.**

Compare that to what pure exponential growth would have produced. Fitting a constant monthly multiplier from the first month to the thirtieth gives $r = (27{,}778{,}968/6{,}390)^{1/29} = 1.3349$ — 33.5% growth per month. The sum of that geometric series is

$$6{,}390 \times \frac{1.3349^{30} - 1}{1.3349 - 1} \approx 110.7 \text{ million}$$

which is **3.99 effective final-volume months.**

**Observed 9.76 against exponential 3.99.** The real curve accumulated two and a half times more volume than smooth exponential growth between the same endpoints would have. There is only one way that happens: **growth was front-loaded and then flattened.** The platform reached something close to its final scale well before June 2026 and then held there, rather than climbing steeply to the end. The curve is S-shaped, not exponential.

**Why you would care.** It changes the forecast completely. An exponential curve says next year is 30 times this year. A flattening curve says the growth is mostly done, and the 2.19-fold rise in queries per user is now the active part of the story rather than user acquisition. **The abstract does not tell you which, but its own three numbers do.** This technique works on any growth report that gives you a start, an end, and a cumulative total — revenue, enrolment, case counts, adoption of anything.

**Nested categories and the false "whereas".** When you see several percentages in one sentence, add the small ones and compare to the large one. If they fit inside it, you are looking at a hierarchy, not a comparison. Here 33.1 + 13.9 = 47.0 sits inside 51.9, so treatment and diagnosis are both children of clinical decision-making, and the honest comparison is 33.1 against 13.9 — a **2.4-fold** ratio — not 13.9 against 51.9. Mis-reading a part as a peer of its own whole makes small categories look smaller than they are.

**Registered, active, and people are three denominators.** 271 million over 952,008 accounts over 30 months is 9.5 queries per account-month. The paper reports 39.5 per *active* user-month. The 4.2-fold gap is not a contradiction — it is the inactivity rate, recoverable by division. Whenever a paper quotes a per-user rate, ask which users: everyone who ever signed up, everyone who did something this month, or everyone who exists in the world. The three can differ by an order of magnitude, and the most flattering one is the one most often quoted.

**Composition checks: predict a reported distribution from a known mix.** The paper says 58.5% female. You know the population is 58.4% physicians and 41.6% NP/PA/other. If physicians are roughly 38-40% female and NP/PA roughly 85%, then $0.40 \times 0.584 + 0.85 \times 0.416 = 0.587$. Predicted 58.7%, reported 58.5%. **The check passes**, which is weak positive evidence that the population is as described. Run this on any paper that reports a demographic breakdown alongside a composition — it is free, it takes thirty seconds, and when it fails it fails loudly.

**Survivorship in a rapidly growing cohort.** When a population grows 2,000-fold, the people present at the start have had 30 months to leave and the people present at the end have had none. Any average computed over "all users" is therefore dominated by recent arrivals, and any *trend* in per-user behaviour is confounded by who survived. The fix is **cohort analysis**: track the January 2024 joiners separately from the January 2025 joiners and see whether each cohort's intensity rises. Telemetry can do this easily; abstracts rarely report it.

**A definitional artifact masquerading as a finding.** Before believing a between-group range, ask whether the measure means the same thing in both groups. "Out-of-specialty" presumes each clinician has a bounded topic domain. That presumption holds for ophthalmology and fails for emergency medicine, so the 88% at the top of the range is partly measuring the taxonomy's inability to represent generalists. **A range is only interpretable if the measure is comparable at both ends.**

**Sponsor-as-author plus non-reproducible data: what survives and what does not.** This combination does not mean the paper is wrong. It means the error-correction mechanism is missing, so you should weight the findings by how hard they would be to get wrong. **Server-side counts of accounts and requests are hard to get wrong** — they are the same instrumentation a company bills and reports on, and they would be visible to engineers with no stake in the paper. **Model-generated interpretive categories are easy to get wrong**, require judgement calls about taxonomy and prompt, and are invisible to anyone outside. So: believe 952,008 and 271 million. Hold 51.9% and 88% loosely. **Grade the trustworthiness of each number by its distance from the raw instrumentation**, not by the reputation of the journal it appears in.

## 6. Jargon Translator

**Use ratio** — a group's share of the queries divided by its share of the workforce. A ratio of 2.0 means the group submitted twice the queries its headcount would predict. Across the whole workforce these must average exactly 1.0, which is the trap Section 5 unpacks.

**National Provider Identifier (NPI)** — a unique ten-digit number issued to every US healthcare provider who bills insurance. Verifying accounts against it means the users are real, licensed clinicians rather than anonymous signups. It is an identity check; it is not a check on whether one person shares a login with a team.

**Cross-sectional study** — a snapshot of a population at one moment, measuring what is there without following anyone forward or back. Good for describing how common something is; incapable of establishing that one thing caused another.

**Monthly active user (MAU)** — the count of accounts that did something in a given month. The definition of "something" is a choice, and different choices give very different numbers, which is why the definition matters and why its absence from the abstract is worth noting.

**Stratified random sample** — rather than drawing at random from everything, you divide the population into strata (here, probably by time, specialty or clinician type) and draw randomly within each. It guarantees small strata are represented rather than being swamped by luck. A good choice, and the right one here.

**Large language model classifier** — using an LLM to read each item and assign it a category. Fast and cheap at 38.8 million items; its accuracy is an empirical question that has to be measured against human labels, and that measurement is what you look for in the Methods.

**Measurement error versus sampling error** — sampling error is "I happened to look at these units"; it shrinks with more data. Measurement error is "my instrument is bent"; it does not. Section 5 shows that at 38.8 million, only the second one is left.

**Telemetry** — data a software system records about its own use. It is exhaustive and precise about what happened inside the system, and silent about everything outside it, including whether anything it recorded was useful.

**Survivorship bias** — when the units you can still observe differ systematically from the ones that left, so your average describes the stayers rather than the population. Especially strong in fast-growing systems where the oldest cohorts have had the most time to churn.

**Nested categories** — when one reported percentage contains others inside it. Add the small ones; if they fit inside the large one, you are reading a hierarchy, and comparing a child to its own parent is a category error.

**Sponsor-as-author** — when employees of the company whose product is being studied are authors on the study. Standard and often unavoidable when the company holds the only copy of the data. It is disclosed here, which is correct; it still removes independent verification, which disclosure does not fix.

**Confusing precision with validity** — precision is how tightly your estimate clusters on repeat measurement; validity is whether it clusters on the truth. A huge sample guarantees the first and says nothing about the second.

## 7. What You Can (and Can't) Say

**You can say:**

"Between January 2024 and June 2026, 952,008 US clinicians with verified provider identifiers — including 556,200 physicians — submitted 271 million queries to one AI clinical information platform."

"Use was concentrated among earlier-career clinicians: physicians within ten years of graduation submitted about 2.5 times their proportional share of queries, residents and fellows about 1.8 times."

"Among the queries a language model classified, treatment and management questions outnumbered diagnostic questions by roughly two and a half to one."

"Nurse practitioners and physician assistants submitted about 20% more queries per active month than physicians did."

"Between a third and nearly nine-tenths of clinicians' queries concerned topics outside their own specialty, varying widely by specialty."

**You cannot say:**

"AI is making doctors better." The study contains no outcome, no accuracy measure, and no patient. It measures use. Use is not benefit.

"Doctors trust AI more than their colleagues." Nothing here compares the platform to any alternative source. There is no comparator.

"Radiologists and ophthalmologists are resisting AI." Their low use ratios are partly forced by the arithmetic in Section 5, and in any case these specialties use AI heavily inside their own imaging workflows — a text question-answering platform is simply not the tool their day calls for. Low use of one product is not resistance to a technology.

"Diagnosis is only 14% of what clinicians wonder about." It is 13.9% of what a language model labelled as diagnostic among queries typed into one platform. People do not type their easy questions into anything.

"88% of emergency physicians' questions are outside their expertise." That number depends entirely on how the topic taxonomy carved up medicine, and emergency medicine is the specialty least well represented by any such carving.

"Use grew exponentially and will keep growing at that rate." The paper's own three numbers imply the opposite — Section 5 shows the curve flattened.

"This has been independently verified." It has not and it structurally cannot be. The data are proprietary logs and three of the seven authors work for the company.

**The honest one-sentence version:** *a large fraction of the American clinical workforce now routinely asks an AI system what to do about patients, most often about treatment rather than diagnosis, and most heavily early in their careers — and nobody has yet published whether the answers are any good.*

## 8. Bottom Line for Your Life

**If you are a patient:** the clinician treating you quite possibly consulted an AI about your case, and the odds are it was about **what to do** rather than **what you have.** That is not a scandal and it is not reassurance — it is just the current state of the tool. The question worth asking, if you ever want to ask it, is not "did you use AI?" but "what did you check it against?" Good practice with any reference, human or machine, is verification against something independent. This paper cannot tell you whether that is happening.

**If you are a clinician:** the pattern in this paper is probably about you or your colleagues. The finding that early-career clinicians and generalists use it most, and that two-thirds of queries are not diagnostic, says the tool is functioning as a **reference** rather than an oracle. Worth knowing: this study says absolutely nothing about whether the answers were right. Its own authors do not claim otherwise. **Treat your own use accordingly**, and note that the one paper in this reading list that benchmarked LLM clinical recommendations against a restraint standard — the *Choosing Wisely* study still on the deferred shelf — found overuse concentrated in two specific recommendations, not spread evenly. Specific failures in specific places is what you should expect.

**If you are evaluating or buying this technology:** this paper is evidence of **adoption**, which is a real and relevant thing to know, and it is not evidence of **value**. Those are separate purchases. The numbers to ask a vendor for next are the ones this paper does not contain: accuracy against a reference standard, the error modes, what happens at the specific decisions your clinicians make, and whether anyone independent has looked.

**If you are designing a study:** this is a model of how to describe behaviour at scale, and a warning about where scale helps. It helped with precision, which was never the problem. The limiting factor is the classifier, and the classifier is a measurement instrument that needs validating like any other. **If your outcome variable comes out of a model, your paper's accuracy section is about the model, not about your sample size.**

**If you are reading the news about this paper:** expect the 271 million to be the headline and the 13.9% diagnosis figure to be misreported as a comparison against 51.9%. Both numbers are real. Section 5 and Section 7 tell you what they can carry.

**This is education, not medical advice.** Nothing here should change anyone's treatment. If something in this paper or this summary bears on your own care, raise it with your clinician.

---

## Appendix: deferred papers, status on 2026-11-05

**All four re-checked today against the live PubMed record.** According to PubMed:

**1. This paper — JAMA, OpenEvidence usage (PMID 42879271, PMC13673371).** **Resolved today by decoding abstract-only, per the standing instruction set on 2026-10-29.** Day 21 of an empty PMC body. The standing instruction read: *"if still empty on 2026-11-05 (day 21), decode abstract-only and say so explicitly."* It fired, and the analysis above is the result. **Closed.** Standing offer: if the full text becomes available in PMC, or if a PDF is supplied, this summary can be upgraded in place — the Methods would most likely move the grade from 2 to 3.

**2. "The anatomy of a personal health agent" — Nature (PMID 42907512, DOI 10.1038/s41586-026-11161-8).** Re-checked today: the PubMed record carries no `pmc` identifier, so **no PMC copy exists** and there is nothing to retrieve. Now confirmed as Nature **volume 659, issue 8139, pages 197-207**, published 21 October 2026, with 40 authors from Google Research, Google DeepMind, Vituity and Columbia. Of interest when accessible: 11 benchmark tasks, more than 7,000 annotations, 1,350 hours of expert and end-user effort, and an **open-source framework** — so the code at least may be inspectable even if the paper is not. **Deferred. Day 16.** Standing plan: re-check weekly rather than daily from here, since a Nature research article with no PMC record is unlikely to acquire one soon; next check 2026-11-12.

**3. BMJ review of LLM-trial reporting completeness (PMID 42869550, DOI 10.1136/bmj-2026-100855).** Re-checked today: still **no PMC copy**. Now confirmed as BMJ **volume 395, page e100855**, published 13 October 2026, 12 authors including Moons KGM and Collins GS — the authors of TRIPOD itself — and Bitterman DS as senior author. The abstract is unusually informative: 461 records screened, 68 trial reports, 15 protocols, 378 registrations; mean reporting completeness **TRIPOD-LLM 40%, CONSORT 2025 44%, CONSORT-AI 59%, CHART 52%, SPIRIT 2025 51%, SPIRIT-AI 57%, WHO dataset 61%.** **This is the single most relevant paper on the shelf for this reading list's purpose** and the abstract alone would support a decode. **Deferred. Day 23.** Standing plan: **if no PMC body by 2026-11-12, decode abstract-only** — the same twenty-one-day rule that fired today, applied from its own first check date.

**4. *Annals of Internal Medicine*, overuse and false restraint in LLM *Choosing Wisely* recommendations (PMID 42896192, DOI 10.7326/ANNALS-26-01667).** Re-checked today: still **no PMC copy**. Three authors, Israeli institutions, published 20 October 2026. **Standing note, carried unchanged since 2026-10-24:** the headline overuse rate of **5.4%, 95% CI 0.6% to 12.2%** has an interval far too wide for 4,050 responses — a simple binomial interval on 5.4% of 4,050 would be roughly 4.7% to 6.2%. The width is a **clustering signature**: the interval is computed across the **15 recommendations**, not the 4,050 responses, which is the statistically correct choice because responses within a recommendation are not independent. The abstract confirms the mechanism — two recommendations account for most of the overuse (thyroid ultrasound 42.8%, routine ECG 28.3%) while five others sit at 0.6% to 3.3% and eight show none at all. **That is the right way to report a clustered benchmark and it deserves saying.** Also noted: this abstract states its own limitations including "responses classified by LLM judge with physician adjudication" — the exact sentence today's JAMA abstract lacks. **Deferred. Day 16.** Standing plan: weekly re-check, next 2026-11-12; decode abstract-only if still blocked on 2026-11-19.

**Shelf status:** five spares remain, in order — (2) gestational-age estimation across two health systems (PMID 42957585, PMC13719529); (3) bipolar speech/NLP, 6,373 features on 160 people (42967232); (4) NOTIFY-DISCUSS qualitative study of a deployed AI tool (42965008); (5) precision-psychiatry six-stage framework review (42947584); (6) explainable-AI urology review of 70 studies (42960345). **Next run takes spare (2)**, which has a confirmed PMC body.

**Watch item:** PM Heart trial results (protocol PMID 42893738), quarterly.
