# NOTIFY-DISCUSS: Patient and clinician perspectives on opportunistic screening for coronary artery calcification using artificial intelligence

**Authors:** Keamy-Minor E, Dudum R, Bragdon CL, Ngo S, Xu S, Asch SM, Maron DJ, Brown-Johnson C, Sandhu AT, Rodriguez F (ten authors — Division of Cardiovascular Medicine, Stanford University; Evaluation Sciences Unit, Stanford; Division of Primary Care and Population Health, Stanford; Stanford Prevention Research Center; Stanford Cardiovascular Institute; Center for Digital Health, Stanford; Division of Cardiovascular Medicine, UCSF; Division of Cardiology, UCLA; Greater Los Angeles VA Healthcare System.)
**Journal:** American Heart Journal Plus: Cardiology Research and Practice, 2026; 72: 100989 (published 22 October 2026)
**Decoded:** 2026-11-08

**Analysis basis:** **FULL TEXT** (retrieved from PubMed Central, PMC13720997) — the complete Introduction, Methods, all eight Results sub-sections with their verbatim participant quotes, the full Discussion including the AHA-framework mapping, Limitations, Conclusion, CRediT statement, generative-AI declaration, Funding and Declaration of Competing Interest. **Table 1 (participant characteristics) and the two figures mapping the themes did not extract** — their in-text references came through empty — so **no participant demographics, ages, sexes, CAC severities or statin statuses are available to me**, and I report none. **This is the first qualitative study decoded in this reading list**, and Section 5 is accordingly about qualitative method rather than about model metrics.

**Source links (verified):**
- DOI: https://doi.org/10.1016/j.ahjo.2026.100989
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42965008/
- Full text used: https://pmc.ncbi.nlm.nih.gov/articles/PMC13720997/

**Basis of link verification.** Direct URL fetching is blocked from this session (`doi.org` does not resolve under the network policy here), so verification was done against the live PubMed/NLM record. According to PubMed, a query for PMID 42965008 returned this exact title, these ten authors with these affiliations, *American Heart Journal Plus* volume 72 article 100989, publication date 22 October 2026, DOI `10.1016/j.ahjo.2026.100989`, publisher identifier `S2666-6022(26)00279-X` and PMC ID `PMC13720997`; the full text was then retrieved from PubMed Central by that PMC ID and matches the record. Both halves of the chain were confirmed independently.

**Funding: partially stripped by the text extraction and therefore partially unreportable.** The statement reads that Dr Rodriguez "was funded by grants from the NIH(;;) and the(Grant #)" — **the grant numbers and the second funder's name were removed by the extraction and I am not guessing them.**

**Competing interests: fully present, and directly germane to this paper.** Dr Rodriguez (senior author) reports consulting fees from **Novartis, Esperion Therapeutics, Edwards, Arrowhead Pharmaceuticals, HeartFlow, iRhythm, Amgen, Boehringer Ingelheim, Bristol Myers Squibb and Cleerly Health**, all stated as outside the submitted work. The remaining nine authors report none. Section 4 says plainly why this constellation is worth naming here rather than passing over: several of those firms make or develop lipid-lowering therapies and the intervention studied **increases statin prescribing**, while HeartFlow and Cleerly Health are coronary-imaging AI companies — the intervention's own product category. Fully and properly disclosed; worth the reader's attention all the same.

**Generative AI: declared, and the declaration is itself notable.** "During the preparation of this work the authors used **OpenEvidence** to perform aspects of the literature review. The authors also used **Claude Sonnet 3.5** (enterprise version with data protections) to proofread portions of the work and provide suggestions on organizational structure," with the authors taking full responsibility. **OpenEvidence is the platform that was entry 68 in this list, decoded three days ago.** This is the first paper here to disclose using it, and the second to disclose generative-AI writing assistance.

**Reporting guideline: none named.** **COREQ** (32 items) and **SRQR** are the reporting standards for interview and focus-group research, and neither appears anywhere in the paper. Section 4 places this in a three-paper sequence.

**Ethics:** "approved with oversight by the Stanford Institutional Review Board and **written informed consent was obtained**" — for this qualitative study. Note carefully, because it is the heart of the paper's own central tension: **the parent NOTIFY-1 project did not obtain written consent before patients' imaging was reviewed by the algorithm**, because it was a quality improvement project.

---

## 1. The Gist

**Seventy papers in this list measured what AI can do. This one asks the twenty people who had it done to them.**

The parent study, NOTIFY-1, did something unusual and rather clever. Thousands of people have had chest CT scans for reasons having nothing to do with their hearts — a cough, a suspected fracture, a cancer follow-up. Those old scans contain the heart, and the heart's arteries may contain calcium, which is one of the strongest predictors of future heart attack we possess. So NOTIFY-1 pointed a deep-learning algorithm at scans **already sitting in the archive, most of them more than two years old**, found the coronary calcium nobody had looked for, and told the patients and their doctors. Statin prescribing went up.

**NOTIFY-DISCUSS then interviewed the people on the receiving end** — 11 patients and 9 primary care clinicians, in 90-minute focus groups and interviews — and asked what that was actually like.

**What they liked was concreteness.** A picture of your own calcified artery does something a risk percentage cannot. One clinician described the conversation: *"this is your heart. See all that white stuff, that's calcium, and well, your medication is going to help with that."* Clinicians found it moved patients *"who are resistant to taking medications."* One patient was *"grateful in a way, because I found out about something before it became more of a problem and I could take action."*

**What they worried about is the part worth your time, because it is not on any accuracy leaderboard.**

**Consent.** NOTIFY-1 ran an algorithm over patients' existing scans without asking first. One patient: *"If you're going to use any of my data, I want you to have my permission. I want to know you're doing it, and I want to give my consent."* Another took the opposite view: *"if somebody can get an early diagnosis of a glioblastoma, I, for one, want to get it. And if they got my permission or not, I'd welcome it."*

**Clinician burden, described with some force.** *"Sometimes you just feel like you have ants crawling all over you with so many different things you're expected to cover."* And more precisely: *"it's not just the finding, it's the follow-up, it's the notification of the patient. It's the immense burden of reassurance when sometimes we don't know if we should be reassuring them."*

**Harm that nobody had put on the list.** Patients were *"entirely shocked"* and *"jarring"* was used. But the sharpest item is one the design team plainly had not anticipated: **patients raised the prospect of discrimination based on an incidental finding — health insurance eligibility, employment, and admission to assisted living communities.**

**And the delay.** Because the scans were old, patients were being told about something found years after the picture was taken. One asked for a repeat scan, not trusting the old result. One found it *"not very encouraging"* that the finding appeared to have been missed the first time. A clinician said these conversations made them feel they were *"more managing the news than managing the condition."*

**The single most useful thing here is not a frequency. It is an existence proof.** It does not matter what fraction of patients worry about insurance discrimination. One person raising it establishes that the harm pathway is real, and anyone deploying this tool now has to design for it. Section 5 is about why that is the correct use of twenty people — and why the paper's own abstract overreaches the moment it says *"most."*

## 2. Study Snapshot

**Study type:** a **qualitative study** — semi-structured interviews and focus groups with thematic analysis — nested as a companion to a prospective randomised quality improvement project. **No quantitative outcome is measured or reported here.** The parent study's effect on statin prescribing is cited, not re-analysed.

**The parent project, NOTIFY-1, as this paper describes it:** a prospective, randomised quality improvement project in participants **not on lipid-lowering therapy and free of clinical atherosclerotic cardiovascular disease at baseline.** A validated deep learning algorithm identified coronary artery calcium on non-gated chest CT scans — **the majority obtained more than two years before notification** — and **results were subsequently reviewed by a radiologist.** Clinicians were notified and prompted to discuss. Patients were notified by automated patient-portal message, **with a paper mailing to those who had not opened the online message.** The effect on statin prescribing is reported elsewhere.

**Why the paper says this matters now:** it reports that **the updated 2026 multisociety dyslipidemia guidelines state that AI-identified coronary calcium on non-cardiac CT scans should actively inform treatment decisions.** (Reported as the paper states it; the supporting citation was stripped by extraction and I have not verified the guideline text independently.)

**Participants: 20 total — 11 patients and 9 clinicians.** **All clinicians were primary care providers.** **All patients had already received their incidental coronary-calcium results before being interviewed.** All participants from NOTIFY-1 with available contact information were invited.

**Response rate — the dominant number in this paper, and the paper reports it itself:** **9 of 63 clinicians (14.3%) and 11 of 129 patients (8.5%)**, which is **20 of 192 invited, or 10.4%.** Roughly nine in ten of those invited did not take part. Note too that the denominator is those "with available contact information," so the NOTIFY-1 population was larger still.

**Procedure:** **90-minute** focus groups and interviews, conducted **virtually via Zoom in 2024–2025**, held **separately for patients and clinicians.** Stated goals: patient perspectives on reporting incidental findings, patient perceptions of AI use on their data, and barriers to guideline-directed statin therapy. Topics covered perceptions of AI in medicine, personal experience with the notification, communication in both directions, perceptions of treatment, and **perceptions of AI and bias.**

**Analysis: a Consensual Qualitative Research approach.** The paper states four emphases: iterative definition of codes informed by data, coder and research team; **multiple team perspectives on transcript coding**; consensus decision-making to resolve differences; and returning to raw data to clarify. The described procedure: transcription; **a codebook with code names, descriptions and exemplary quotes created iteratively by the qualitative researcher (CB) and the qualitative expert (CBJ) in conversation with the project leadership and implementation team (FR, RD)**; then **transcripts coded by one researcher (CB) in NVivo, with review by the qualitative expert (CBJ)**; with questions resolved by returning to transcript data.

**Seven themes, which the paper groups as concerning AI in healthcare, the implementation of an AI screening tool, or both:**
- personalised data for behaviour change and shared decision-making
- potential to improve follow-up of incidental findings
- impacts on health equity
- concern about consent to the use of AI
- concern about data rights, usage and security
- concern about burden on clinicians
- concern for potential unintended harms, and need for timely notifications

**Selected verbatim findings, by theme.** On shared decision-making: *"the cornerstone of what we do"* (Clinician 1), preferable to *"the old school, 'Don't worry, I looked at your scan, it's fine'"* (Clinician 4); and from a patient, *"You and your doctor are the final arbiters about what you really need to do"* (Patient 9). One patient **likened her incidental calcium finding to the mammography result that caught her early breast cancer**, noting both diseases are asymptomatic; several expressed variations on *"I wouldn't have known until probably it was too late"* (Patient 11).

On incidental findings: missed findings described as *"little landmines…just waiting for somebody to step on them before they actually cause harm"* (Clinician 8). One patient recalled a chest x-ray decades earlier showing findings consistent with sarcoidosis with *"no comment…it was never noted"* (Patient 7).

On equity: clinicians raised **underserved populations** who *"struggle to get access to basic healthcare"* (Clinician 3) and **sex differences in presentation and diagnosis** — *"gender would be the number one thing that I would think about"* (Clinician 2) — while also naming a systemic barrier: *"you're going to have trouble sending the letters to our homeless patients"* (Clinician 1).

On consent: alongside the two opposed patient views quoted in Section 1, some clinicians wanted consent because bypassing it made preparing patients harder — *"I try to really tell them the point of me doing this test is for us to decide together whether or not you need a statin"* (Clinician 4) — while others suggested **a blanket consent or "big statement" alongside "consent to receive care,"** analogous to notifications about trainee involvement in a teaching hospital (Clinician 3).

On data security: *"Is all this stuff really secure or not?"* (Clinician 4), with hospital cyber attacks cited as evidence that *"the secure-ness of the data in general is not what it is in other industries at all"* (Clinician 8). **Some patients said they would want to be sure AI tools were not using any of their personal information at all.**

On harms: *"people were freaked out"* (Clinician 3). One patient dissented, finding the results *"written in such a way that I could tell it was not a life-threatening thing. I mean, a lot of people have mild coronary artery disease"* (Patient 2). Clinicians urged targeting: notifying patients already on maximal therapy would be *"burdensome and also cruel to the people who are trying to get through their day"* (Clinician 4), and *"sending that letter right after somebody's just been in the hospital for their cancer treatment is not helpful"* (Clinician 1).

On timeliness: **only one patient viewed the delay positively**, reading it as evidence that *"people are trying to come up with new things and new ways of looking at the data"* (Patient 9). Clinicians raised the **implicit liability concern** in patients' questions about the delay and hoped for notification *"as close to real time as possible"* (Clinician 5).

**The paper maps its findings onto the four principles of a published American Heart Association scientific advisory for evaluating and monitoring AI in healthcare** — strategic alignment, ethical evaluation, usefulness and effectiveness, and financial performance — and notes that this framework **was published after the interviews were conducted**, so clinicians' request for an accompanying workflow was made without knowledge of it.

**Two pieces of context the paper supplies about the delay, which matter a great deal:** **NOTIFY-PICTURE** delivered notifications **within weeks** of CT acquisition and **also increased statin prescribing**; and **a pooled analysis of NOTIFY-1 and NOTIFY-PICTURE found no difference in effect size between timely and delayed notification.**

**Limitations the paper names itself:** the low participation (with the exact fractions); that participants may have had strong opinions and may differ from non-responders; that **patients who received a new statin prescription appeared to have particularly positive views**; that **prospective studies linking incidental AI-calcium to mortality are lacking** and further work is needed to assess whether such programmes **contribute to lead time bias**; that it is single-site; that NOTIFY-1's demographics **limited racial and ethnic representation to primarily white participants**; and that **calcium severity was not included in the notifications**, although available in most radiology reports, with **no heterogeneity of effect by amount of calcium in NOTIFY-1.**

**Not reported, or not reachable:** participant demographics (Table 1 did not extract); whether thematic saturation was assessed (never mentioned either way); any inter-coder agreement statistic; the full interview guide; NIH grant numbers; the cited guideline text.

## 3. How Strong Is This Evidence? (Grade 3 out of 5)

**This is the first qualitative study in this list, so the grading has to start by saying what it is being graded against.** A qualitative study is not a weak quantitative study. It is a different instrument answering a different question: not *how often* or *how much*, but *what is going on, in whose words, and what did nobody anticipate.* Graded as a quantitative study it would score 1. Graded as what it is, it scores 3 — and the ceiling is set by specific, fixable gaps rather than by the design.

**What it genuinely achieves, and almost nothing else in this list does:**

**It asks people who actually experienced a deployed tool.** The paper makes this point and it is correct: prior work on AI perceptions has largely surveyed **general attitudes** toward AI in the abstract. These 20 people had an algorithm run over their own old scans and got the result. **General attitudes toward AI are nearly worthless for design; reactions to a specific implementation are not.**

**It interviewed both sides, separately, and found a conflict between them.** Patients wanted to discuss results **with a trusted clinician**. Clinicians were worried about **the time cost of exactly that conversation.** Those two preferences are in direct tension, and neither group would have reported the tension alone. The paper names it as "a central tension between the strategic priorities of patients and clinicians." **That finding required talking to both, and separately, so neither moderated in front of the other.**

**It surfaced a harm the design team had not listed.** Insurance eligibility, employment, assisted-living admission. That is not in any accuracy metric, any calibration plot, or any AHA framework principle, and it came out of a patient's mouth. **This is what qualitative work is for.**

**The limitations section is honest about the things that matter most**, including the exact response fractions, the statin-responder positivity, the racial homogeneity, and — unusually for a qualitative paper — **lead time bias**, which is precisely the right statistical concept for why *"it saved my life"* testimony cannot establish that the programme saves lives. Naming it is a real mark of quality.

**It separates a behavioural effect from a perceptual one.** Delay damaged the *experience* badly, but the paper reports that a pooled analysis found **no difference in effect size** between timely and delayed notification. So the thing that upset people did not reduce what the programme accomplished. Keeping those apart is a genuine analytic contribution.

**And the 90-minute sessions are substantial.** Depth is the currency here, and an hour and a half per group buys a lot of it.

**What holds it to 3:**

**It makes frequency claims a 10.4% self-selected sample cannot support, starting in the abstract.** *"Most participants appreciated the notification tool."* *"Many clinicians and patients praised…"* *"Some patients felt strongly…"* *"a minority of our participants…"* **There is not a single count anywhere in the paper.** With 11 patients, one person is 9% of the patient sample. And Section 5 makes the sharp version of this point: **Consensual Qualitative Research, the approach this paper names, has a standard convention that solves exactly this**, labelling each theme by how many cases show it. The paper names the method and does not use its central reporting device.

**One coder, in tension with its own stated principles.** The paper lists "multiple team perspectives on transcript coding" among its CQR emphases, then describes coding by **one researcher with review by one expert.** No inter-coder agreement is reported. The audit is real and worth something; it is not the same as independent double coding.

**The codebook was shaped by the people who built the intervention.** The Methods say so plainly: created "in conversation with the project leadership and implementation team (FR, RD)" — authors of NOTIFY-1, the thing being evaluated. **This is a textbook reflexivity concern and it is not listed as a limitation.** Section 4 expands.

**No COREQ or SRQR**, and no saturation assessment either way.

**And the response rate, while not fatal to a qualitative study, is severe enough to be worth a sentence of its own.** The participants are plausibly the most opinionated tenth — in both directions, which is the awkward part, because self-selection on *strength* of opinion does not bias in a predictable direction.

**Why not 4.** Because the fixes are all cheap and standard — report counts, double-code a subsample, name COREQ, flag who built the codebook — and a paper that names CQR should have done the first of them. **Why not 2.** Because the themes do not become false at a 10% response rate. The concerns were articulated; they exist; the design implications stand regardless of prevalence. That is the whole point of the instrument, and the paper's conclusion claims exactly that and no more: these concerns "will be essential to address when designing and deploying future AI tools."

## 4. The Editor's Concerns

**1. The abstract's first Results sentence is the paper's weakest claim.** *"Most participants appreciated the notification tool."* From a sample that is **8.5% of invited patients and 14.3% of invited clinicians**, with no counts given. "Most" of 20 is somewhere between 11 and 20 people, and the reader cannot narrow it. **The damage is confined precisely to the frequency words** — everything the paper says about *what* people said is unaffected — but those words are in the abstract, which is what will be read and cited.

**2. The method named supplies the remedy the paper did not use.** Consensual Qualitative Research, as conventionally formulated, labels each theme by case count: **general** (all or all but one case), **typical** (more than half), **variant** (two or three cases up to half). Applied here that would read "general (10–11 of 11 patients)" or "variant (3 of 9 clinicians)" and the reader would know exactly where they stood. This is not an exotic demand — it is the reporting device of the approach the paper names in its own Methods. **Its absence is the single most fixable flaw in the paper.**

**3. Who built the codebook, and why that is a reflexivity problem.** The codebook was created "in conversation with the project leadership and implementation team (FR, RD)." **FR and RD are authors of NOTIFY-1** — the intervention being evaluated — and FR is this paper's senior author. In qualitative research the standing concern is that the analyst's investment shapes what gets recognised as a theme, and here the investment is structural: the people who designed and ran the programme helped decide the categories through which reactions to it were read. **This is stated openly in the Methods, which is to the paper's credit, and it is not among the limitations, which is not.** Involving the implementation team buys real contextual knowledge; the standard mitigation is to say so as a limitation and describe how it was guarded against. Neither happens.

**4. One coder is not "multiple team perspectives."** The paper's stated CQR emphases include multiple perspectives on coding; the procedure is one coder plus one reviewer. The gap between the stated principle and the described practice is internal to the paper. Independent double coding of even a subsample, with a reported agreement figure, would have closed it.

**5. Saturation is never mentioned, in either direction.** The conventional justification for a small qualitative sample is that new interviews stopped producing new themes. The paper instead argues that "our smaller sample still allowed us to obtain in-depth input" — a defence of depth, not of sufficiency. **Not claiming saturation when you did not assess it is honest**, and I prefer it to an unsupported assertion. But it leaves the reader unable to judge whether an eighth theme was waiting in the twelfth patient.

**6. The whole study is a study of *delayed* notification, and that is a near-total confound for the experience it measures.** The scans were a median of more than two years old. So "patients were shocked," "patients distrusted the result," "a patient requested a repeat scan," and the clinicians' liability worry are **all reactions to being told about an old finding.** The paper handles this unusually well — it makes timeliness a named theme and reports that NOTIFY-PICTURE's timely notifications also raised statin prescribing, with **no difference in pooled effect size.** The implication is worth stating sharply: **the delay cost the programme nothing in behaviour and a great deal in trust.** Those are different currencies and a health system spends both.

**7. Selection within selection: the statin responders liked it most.** The paper notes patients who received a new prescription "appeared to have particularly positive views." So inside an already self-selected 8.5%, the most favourable voices are those who **acted on the result** — evaluation conditioned on the action taken. And the paper draws the right inference rather than the flattering one, pointing out that studies linking incidental AI-calcium to mortality are lacking and raising **lead time bias** by name. Section 5 works that through, because it is the reason a sincere *"I wouldn't have known until it was too late"* cannot be treated as evidence of benefit.

**8. The consent question is the real finding, and the paper's resolution of it deserves scrutiny.** NOTIFY-1 ran an algorithm over patients' scans **without written consent**, lawfully, because it was quality improvement. Some patients said they would have wanted to be asked. The paper's answer, drawn from a cited ethical framework, is that consent "may not be necessary or feasible in situations where the likelihood of harm from use of an AI tool is low," with **notification at the point of care** being appropriate for lower-risk tools. That is a defensible position and probably the right one. **But the paper also supplies the evidence that complicates it**, and does so itself: "our results suggest that patients may perceive more severe harm — characterized by the distress of receiving anxiety-provoking results — than clinicians do." If the justification for skipping consent is that harm is low, **and patients rate the harm higher than clinicians do, then whose estimate licenses the waiver?** The paper gets there — "a notification approach, while perhaps legally and ethically justifiable, may nonetheless erode patient trust" — which is an honest place to land, and the tension is not resolved so much as named.

**9. The insurance-discrimination finding deserved more than one clause.** Patients raised **health insurance eligibility, employment opportunities, and admission to assisted living communities.** That is a concrete, mechanism-level harm from generating a new diagnosis in someone's record, and it appears once, in a single sentence, and is not carried into the Discussion or the AHA-framework mapping. It is arguably the most actionable thing in the paper — it bears directly on what gets written into a chart and who can see it — and the paper's own framework discussion addresses ethics without returning to it.

**10. No COREQ or SRQR, completing a three-paper sequence worth noting.** Entry 69 (two days ago) named **TRIPOD+AI** and deposited the completed checklist. Entry 70 (yesterday) named **STROBE** and deposited it, while being arguably the most methodologically careful paper in this list. This paper names **none**. **Three consecutive entries, three levels of checklist adherence — and the methodological care runs in close to the opposite order.** That is exactly the gap between reporting-guideline compliance and actual rigour that the deferred BMJ review quantifies, and it is a caution against treating a named checklist as a quality signal.

**11. The disclosures are complete and worth reading rather than skipping.** The senior author reports consulting fees from ten companies. **Several — Novartis, Esperion, Amgen, Arrowhead — make or develop lipid-lowering therapies, and the intervention under study increases statin prescribing. Two — HeartFlow and Cleerly Health — are coronary-imaging AI companies, which is the intervention's own product category.** All declared as outside the submitted work, and I have no reason to think otherwise. But a paper evaluating perceptions of an AI coronary-imaging tool that drives statin uptake, with senior-author relationships spanning both the drug class and the imaging-AI sector, is one where the reader should have that in view. The remaining nine authors declare nothing, and the paper's disclosure is a model of completeness.

**12. A genuine curiosity, reported because it is true and relevant.** The authors disclose using **OpenEvidence** for literature review and **Claude Sonnet 3.5** for proofreading and structural suggestions. OpenEvidence was **entry 68 in this list, decoded three days ago** — a study of 271 million clinician queries. So a paper about clinicians' and patients' experience of a clinical AI tool was itself written with the help of two clinical AI tools, and says so. That is appropriate practice, properly declared, and it is also a small illustration of how quickly this has become ordinary.

## 5. Statistics Spotlight

Ten techniques, numbered from 214 in the running list in `queue.md`. This list has taught AUCs, calibration, power and permutation tests for seventy entries. **None of that applies today**, and the first three techniques below are the load-bearing ones for reading qualitative evidence at all.

**What qualitative evidence can and cannot establish: the existence proof.**

The instinct trained by seventy quantitative papers is to ask "twenty people — what can that possibly show?" The answer is: **a different kind of thing, and one you cannot get any other way.**

A quantitative study answers *how often* and *how much*. It needs a sample large enough that the proportion it measures resembles the population's. A qualitative study answers *what is going on, in whose words, and what did nobody anticipate.* It needs a sample deep enough that people say things they had not planned to say.

**So the logical form of a qualitative finding is existence, not frequency.** "Patients raised concerns about health insurance eligibility, employment, and admission to assisted living communities" is a claim that **this concern exists, is articulable by real patients, and is specific enough to design around.** It does not need a denominator to be useful. **One person is enough to establish that a harm pathway is real.** A system deploying this tool now has to think about what gets written into the chart and who can read it — and it has to think about that whether 1 patient in 11 raised it or 11 in 11.

**The everyday version.** You want to know whether a bridge is safe. A survey of a thousand drivers' confidence tells you about confidence. **One engineer finding one cracked weld tells you the bridge has a cracked weld** — and no amount of survey confidence rebuts it. The engineer's finding is an existence proof: n=1, and decisive. Now flip it: the engineer cannot tell you **what fraction** of welds are cracked. For that you need to inspect them all. **Two instruments, two questions, and each is nearly useless for the other's job.**

**What this specific study can therefore support:** that seven named concerns exist among people with first-hand experience; that patients and clinicians hold a *conflicting* preference about who should deliver results; that a delay of years produces confusion and distrust; that insurance and employment discrimination occurred to patients unprompted. **Every one of those is a design requirement, and none needs a percentage.**

**What it cannot support:** that most patients approve; that concerns are rare; that clinicians are more worried than patients, or less. **All four of those are frequency claims, and the paper makes versions of the first two.**

**Watch out for:** a qualitative study whose abstract reads like a survey. The tell is frequency vocabulary — *most, many, some, a minority* — with no counts. And watch for the mirror error too, which is more common and worse: **dismissing a qualitative finding because the sample is small.** If a finding's logical form is existence, sample size is nearly irrelevant to its validity.

**Counting in qualitative research, and the convention this paper named but did not use.**

Here is the tension. Qualitative work is not about frequencies — and yet readers want to know whether a theme came from nine people or one, because that changes what you do about it. Both instincts are right, and the methodological traditions have an answer.

**Consensual Qualitative Research — the approach this paper names in its Methods — resolves it with counted frequency labels.** As conventionally formulated, each theme is tagged by how many cases show it:

- **general** — all cases, or all but one
- **typical** — more than half
- **variant** — from two or three cases up to half

Applied to these 20 participants, that machinery gives a reader something precise:

- *general* among patients would be **10–11 of 11**
- *typical* among patients would be **6–9 of 11**
- *general* among clinicians would be **8–9 of 9**
- *typical* among clinicians would be **5–7 of 9**

**That is the whole fix, and it costs nothing.** "Concern about consent was *variant* among patients (3 of 11)" tells you something actionable. "Some patients felt strongly that consent should be obtained" does not, because "some" spans 2 to 10 people out of 11.

**Why it matters more than it sounds.** Design decisions are triaged. If one of nine clinicians finds notifications burdensome, you note it. If eight of nine do, you redesign the workflow before launch. The paper says *"For multiple clinicians, their initial response to notifications regarding opportunistic findings was exasperation"* — and **"multiple" could be 2 or 8, which are different decisions.**

**The everyday version.** A restaurant's comment cards say "several diners mentioned the room was cold." Two diners out of two hundred, or two out of five? **One is noise, one is a broken thermostat, and the word "several" cannot distinguish them.** Counting does not turn your comment cards into a temperature survey — it just tells the manager whether to check the thermostat.

**Watch out for:** a paper that names a specific qualitative methodology and then does not use its characteristic reporting devices. CQR means consensus coding by multiple judges, an auditor, and counted frequency labels. **This paper has the auditor, has a thinner version of the consensus, and does not report the labels.** When a methodology is named, check whether its machinery actually ran — the name is a claim about procedure, not a decoration.

**Lead time bias: why a sincere "it saved my life" cannot establish that screening saves lives.**

A patient in this study compared her incidental calcium finding to the mammogram that caught her early breast cancer. Several said versions of *"I wouldn't have known until probably it was too late."* These statements are honest, and they feel like evidence. **They are not, and the reason is the most important idea in all of screening.**

**The worked example.** Take a disease that will kill a particular person at age 70, and suppose for the sake of argument that treatment changes nothing at all.

- Found because symptoms appeared, at **age 65** → survival from diagnosis = **5 years**
- Found by screening, at **age 60** → survival from diagnosis = **10 years**

**Survival from diagnosis doubled. The age at death did not move by a single day.**

The extra five years is **lead time**: time spent *knowing about* the disease, not time *gained*. And here is the trap — **every screening programme generates lead time automatically, whether or not the treatment works.** Find things earlier and survival-from-diagnosis always rises. So that number cannot be used as evidence that finding things earlier helped.

**It gets worse before it gets better.** Those five extra years of knowing are not free. They are five years of medication, follow-up scans, insurance questions, and the ordinary weight of being a person with a diagnosis. **Lead time has a cost even when it has no benefit.**

**The only measure immune to it** is a comparison of **deaths** between a screened group and an unscreened group over the **same calendar window.** Not survival from diagnosis — mortality in a population over a fixed period. That design cannot be fooled by moving the diagnosis date, because the date of death does not care when you learned.

**Why this bears directly on this paper.** The programme demonstrably increases statin prescribing — that is NOTIFY-1's finding and it is real. **Whether it prevents heart attacks or deaths is a separate question that nobody has answered**, and the paper says so: "prospective studies linking incidental AI-CAC to mortality outcomes are lacking. Further work is needed to assess whether such programs contribute to lead time bias." **A qualitative paper naming lead time bias in its own limitations is unusual and is the best single sign of quality in it.** Note also the honest asymmetry: statins for coronary calcium have a genuine evidence base, so the inference here is far more plausible than for many screening programmes. Plausible is not demonstrated.

**Watch out for:** survival rates quoted as evidence for any screening programme — five-year survival, median survival from diagnosis, "caught early" testimony. All three move when you shift the diagnosis date and nothing else. **Ask for mortality, over a fixed window, against an unscreened comparison.** If a programme cannot supply that, it has not yet shown it saves lives, however many people sincerely believe it saved theirs.

**217. Response rate matters differently in qualitative and quantitative work — but it still matters.** This study reached **11 of 129 patients (8.5%)** and **9 of 63 clinicians (14.3%)**; **20 of 192 overall, 10.4%.** For a survey estimating a proportion, 8.5% is fatal: you have measured the responders. **For a qualitative study the themes survive**, because a concern voiced by one person is still a concern that exists. **The frequency claims do not survive** — so the damage lands exactly on the *most/many/some* sentences. And note the awkward feature the paper identifies correctly: participants "may have had strong opinions to share," and **self-selection on strength of opinion inflates praise and complaint alike**, so it does not bias in a direction you can correct for.

**218. Single coder, double coder, and the audit trail.** The strongest qualitative designs have **two or more analysts code independently**, compare, and report their agreement before reconciling by consensus. Weaker designs have one coder with a reviewer, which is what this paper describes. The reviewer catches errors but **cannot tell you whether the coding scheme was reproducible** — because reproducibility means two people arriving at it separately. **Ask of any qualitative paper: how many people coded, independently or sequentially, and was any agreement figure reported?** This paper: one, sequentially, none.

**219. Reflexivity, and the specific question of who builds the codebook.** Reflexivity is the qualitative counterpart of preregistration: because the analyst is the instrument, the analyst's position has to be declared so readers can judge how it shaped what was found. The concrete version is **who defined the categories.** Here the codebook was built in conversation with the **implementation team of the intervention being evaluated.** **The general rule: when the people who built a thing help define the categories through which reactions to it are read, the categories are not independent of the thing.** The mitigation is not to exclude them — they hold the context — but to state it as a limitation and describe the guard. The guard here was the external qualitative expert, which is real; the statement is missing.

**220. COREQ and SRQR exist, and their absence is informative.** COREQ is a **32-item** checklist for interview and focus-group studies, covering the research team and reflexivity, study design, and analysis and reporting; SRQR is the broader alternative. Neither is named here. **A named checklist is not a quality signal** — entries 69, 70 and 71 run in almost the reverse order on care and on compliance — **but an unnamed one tells you to check the items yourself.** The COREQ items this paper leaves open are the ones Section 4 lists: coder count, agreement, saturation, participant characteristics, and reflexivity.

**221. Outcome-dependent recall.** Patients who got a statin viewed the tool most favourably. **Evaluations gathered after an action, from people who took the action, are conditioned on having taken it** — through commitment to the decision, through the reasons constructed to justify it, and through simply having had a better experience. The fix is to sample **deliberately across outcomes**: people who declined the statin, people who never opened the portal message, people who were annoyed. **This study invited everyone and got the responders**, which is not the same as sampling across outcomes, and is why the positivity is uninterpretable as approval.

**222. An existence proof needs no denominator — and the corollary for harms.** Technique 214 establishes the form. The corollary is sharper and worth holding on its own: **for a potential harm, the existence proof is usually enough to act on.** If one patient in eleven raises insurance discrimination, you do not need to know the prevalence before deciding that what goes into a chart and who can see it must be designed deliberately. **Prevalence governs how much to spend on a fix. Existence governs whether to think about it at all.** Most harms in deployed systems are discovered by someone saying something nobody had thought to ask about.

**223. Separate a behavioural outcome from a perceptual one — they can move in opposite directions.** The delay in this programme **damaged the experience badly** (confusion, distrust, a requested repeat scan, clinician liability worry) and, per the pooled analysis the paper cites, **cost nothing in effect size** — timely and delayed notification raised statin prescribing equally. **Both are true, and a health system has to pay attention to both**, because an intervention that works while eroding trust is spending down an asset that does not appear in its outcome measure. **Whenever a paper reports that something "worked," ask what it cost in the experience of the people it worked on** — and note that you generally need a qualitative study to find out.

## 6. Jargon Translator

**Coronary artery calcium (CAC)** — calcium deposits in the arteries supplying the heart, visible on a CT scan. More calcium means more atherosclerosis and higher risk of a future heart attack. It is one of the strongest single predictors we have.

**Opportunistic screening** — looking for one disease in a test that was ordered for something else entirely. Here: finding heart-artery calcium on a chest CT taken for a cough or a cancer follow-up. The scan already exists, so the extra information is nearly free — which is what makes it attractive and what raises the consent question.

**Non-gated chest CT** — a CT not synchronised to the heartbeat. Dedicated cardiac CT is "gated" to freeze the heart's motion; a routine chest CT is not, so the heart appears slightly blurred. Finding calcium on one is harder, which is why the algorithm matters.

**Incidental finding** — something found that nobody was looking for. Every imaging department has the problem of what to do with them, and the clinician's phrase for the missed ones in this paper is hard to improve on: *"little landmines."*

**Statin / lipid-lowering therapy** — medication that lowers cholesterol and reduces heart-attack risk. The behaviour NOTIFY-1 was trying to increase.

**Primary prevention** — treating someone who has not yet had a heart attack or stroke to stop the first one. Everyone in NOTIFY-1 was free of clinical cardiovascular disease at baseline, so this is primary prevention throughout.

**Shared decision-making** — clinician and patient deciding together, with the evidence and the patient's priorities both on the table. A clinician in this study called it *"the cornerstone of what we do."*

**Quality improvement project** — work to improve care within a health system, which carries lighter regulatory requirements than research, including — as here — potentially no individual written consent. The distinction is legally real and, as this paper shows, not always intuitive to the patients on the receiving end.

**Qualitative study** — research that analyses what people say rather than counting things. Produces themes, not percentages.

**Semi-structured interview** — a planned topic list with freedom to follow what the person actually says. The structure makes interviews comparable; the freedom lets unanticipated things surface.

**Focus group** — several participants discussing together, so they can react to each other. Good for surfacing disagreement; less good for anything someone would not say in front of peers — which is why this study held patient and clinician groups **separately.**

**Thematic analysis** — reading transcripts repeatedly, labelling recurring ideas ("codes"), and grouping them into themes.

**Codebook** — the list of codes with definitions and example quotes. **Whoever writes it decides what the data can be seen to say**, which is why Section 4 asks who wrote this one.

**NVivo** — software for organising coded qualitative data. A filing system, not an analysis method.

**Consensual Qualitative Research (CQR)** — a specific qualitative methodology built on multiple judges coding, resolving differences by consensus, an external auditor, and counted frequency labels (general / typical / variant). Section 5 covers what naming it commits you to.

**Reflexivity** — examining how the researcher's own position shapes the findings. The qualitative equivalent of declaring your analysis plan in advance.

**Saturation** — the point where new interviews stop producing new themes. The usual justification for stopping at a given sample size. Never mentioned in this paper, either way.

**COREQ / SRQR** — the reporting checklists for qualitative research. Neither named here.

**Lead time bias** — the illusion that finding a disease earlier extended life, when it only extended the time spent knowing. Section 5 works it through; it is the reason "caught it early" stories cannot prove a screening programme works.

## 7. What You Can (and Can't) Say

**You can say:**

"In interviews with 11 patients and 9 primary care clinicians who had first-hand experience of an AI tool that found coronary calcium on their old CT scans, participants valued the concreteness of a personalised imaging result for conversations about starting a statin."

"The same participants raised concerns about consent, data security, the clinician time required to contextualise findings, distress caused by unexpected results, and the long delay between the scan and the notification."

"Patients raised the possibility of discrimination based on an incidental finding — in health insurance, employment, and admission to assisted living."

"Patients wanted to discuss results with a trusted clinician, while clinicians were concerned about the time that conversation takes — a tension the study identified by interviewing both groups separately."

"The programme's effect on statin prescribing did not depend on timely notification, but patients' experience of it did."

**You cannot say:**

"Most patients support AI screening." The study reached **8.5% of the patients it invited** and reports no counts. "Most" of a self-selected tenth is not a measure of support, and the participants were, by the paper's own account, likely those with the strongest opinions.

"Concerns about AI consent are rare," or common. **The study cannot estimate how common anything is.** That is not a flaw; it is the instrument.

"Patients are more worried about AI than clinicians," or less. A comparison between groups requires a design built to compare them.

"This tool saves lives." It increases statin prescribing. **Nobody has shown it prevents a heart attack or a death** — the paper says prospective studies linking incidental AI-calcium to mortality are lacking and raises lead time bias by name.

"Patients found it lifesaving, so it works." Those patients sincerely believe it, and lead time bias is exactly why belief is not evidence here. Earlier diagnosis always lengthens survival-from-diagnosis, even when nothing else changes.

"Patients approve, so consent is unnecessary." The study found patients **split** on consent, and separately found that patients may perceive the harm as more severe than clinicians do — which bears on the harm-based argument for waiving consent rather than supporting it.

"These findings apply to the US population." Single site, and NOTIFY-1's demographics meant **primarily white participants** — the paper states both.

"AI improves health equity." Participants **hypothesised** that it might, and one clinician immediately named a reason it might not: *"you're going to have trouble sending the letters to our homeless patients."*

**The honest one-sentence version:** *twenty people who actually had an algorithm run over their old scans were asked what it was like, and they named seven things worth designing for — including a harm about insurance and employment that the people who built the tool had not listed — but how common any of those reactions is remains completely unknown, and whether the programme prevents a single heart attack is a separate question nobody has answered.*

## 8. Bottom Line for Your Life

**If you have had a chest CT:** it may contain information about your heart that nobody looked for, and health systems are increasingly going back through their archives to find it. If you get such a notification, two things are worth knowing. **It is probably not an emergency** — as one patient in this study put it, *"a lot of people have mild coronary artery disease."* And **it is a reasonable thing to bring to your own clinician rather than act on alone**, which is what the patients in this study overwhelmingly wanted and what the tool was designed to prompt.

**If you are a patient wondering whether to be annoyed that nobody asked you:** your reaction is in this paper, on both sides. Some participants felt strongly that permission should have been sought; at least one said they would take the finding regardless. **The legal position is that quality improvement work carries lighter consent requirements than research**, and the paper's judgement is that notification at the point of care is appropriate for low-risk tools. That is a defensible position and the paper is honest that it may still cost patient trust.

**If you are a clinician:** the burden complaint in this paper is well-documented and the solution in it is concrete. Clinicians did not want the tool removed; they wanted it to **arrive with a workflow** — a prompt to schedule, a reminder at the next visit, an LDL target, guidance on who to refer. One estimated that automatically generated workflows would mean *"very little extra lift for us."* **When an AI notification tool is proposed in your service, that is the thing to ask for, before launch.**

**If you deploy or procure clinical AI:** the three items in this paper that are not on any technical evaluation are **consent, timeliness, and targeting.** Targeting is the cheapest win and the clinicians were blunt about it — notifying someone already on maximal therapy is *"burdensome and also cruel,"* and notifying someone just out of hospital for cancer treatment *"is not helpful."* **Those are exclusion rules you can write before go-live, and they cost nothing.** And add the fourth: **decide deliberately what the finding writes into the record and who can see it**, because the patients thought of insurance and employment even if your design review did not.

**If you design studies:** this is the argument for doing qualitative work alongside quantitative. **NOTIFY-1 could tell you the tool increased statin prescribing. It could not tell you that the delay was eroding trust while the prescribing rose, or that patients were worried about their insurance.** Those findings required asking. Two things to improve on if you copy this: **report counts per theme** — the CQR labels the paper names would have done it — and **say who built the codebook** if they are also the people who built the intervention.

**If you are reading the coverage:** expect "patients welcome AI screening." The accurate version is that twenty people with first-hand experience named both benefits and seven distinct concerns, and that the study was never able to say how common either was.

**This is education, not medical advice.** Nothing here should change anyone's medication. If you have had an incidental finding on a scan, or a notification like the one described, that is a conversation with your own clinician.

---

## Appendix: deferred papers and shelf, status on 2026-11-08

**Landmark check for the past week, per the trigger's step 2.** According to PubMed, a search of JAMA, Lancet, NEJM, Nature, Nature Medicine, BMJ and *Annals of Internal Medicine* for AI, machine-learning, deep-learning, LLM or foundation-model titles entered between 2026-11-01 and 2026-11-08 returned **four records**, three of them already assessed in previous runs. The new one is substantial and I considered it seriously for priority:

**A gait foundation model for prediction of multisystem health phenotypes from 3D skeletal motion** — *Nature Medicine* (PMID 42995231, [DOI](https://doi.org/10.1038/s41591-026-04724-9), published 6 November 2026, Gabet A et al., Weizmann Institute, with two authors at Newton VR LTD and BioPilot AI). **3,328 deeply phenotyped adults**, 3D skeletal motion from a single depth camera across 5 motor tasks; learned embeddings beat engineered gait features for age (**r=0.69**), BMI (**r=0.91**) and visceral adipose tissue (**r=0.83**); **1,887 of 3,210 tested phenotypes significantly predicted**; improvement over a baseline of age, BMI, visceral fat and height in **all 18 body systems in males and 17 of 18 in females**; anatomical ablations placing leg dynamics with metabolic and frailty phenotypes and torso dynamics with sleep and lifestyle.

**Decision: added to the shelf as the priority item rather than decoded today.** It is a biomarker-discovery paper with no clinical decision, no deployment and no patient management — a new measurement modality, not a landmark clinical result — whereas today's queue pick is the first qualitative study in seventy-one entries and concerns a tool **already in clinical use.** But it goes to the front of the shelf, because **3,210 tested phenotypes with 1,887 called significant is the largest multiplicity problem this list will have seen**, and it is the natural place to extend techniques 205 (permutation correction for correlated tests) and 186 (precision versus validity at large n) — the obvious first question being what false-discovery-rate procedure was applied across 3,210 tests and what 1,887 would have looked like under the null.

**Deferred papers — all three re-checked today; none has a PMC copy.**

**1. "The anatomy of a personal health agent" — Nature (PMID 42907512, [DOI](https://doi.org/10.1038/s41586-026-11161-8), 659(8139):197-207).** **Deferred, day 19.** Weekly re-check, next 2026-11-12.

**2. BMJ review of LLM-trial reporting completeness (PMID 42869550, [DOI](https://doi.org/10.1136/bmj-2026-100855), 395:e100855).** **Deferred, day 26 — reaches its own twenty-one-day threshold on 2026-11-12, when the abstract-only rule fires.** Today's entry completes a three-paper sequence that makes this review the most pointed item on the shelf: entry 69 named **TRIPOD+AI** and deposited the checklist, entry 70 named **STROBE** and deposited it, and entry 71 names **no qualitative reporting guideline at all** — while the methodological care across the three runs in close to the opposite order. The review found mean TRIPOD-LLM completeness of **40%**; these three entries are a worked illustration of why that number is worth having and also why it is not a quality ranking.

**3. *Annals of Internal Medicine*, overuse and false restraint in LLM *Choosing Wisely* recommendations (PMID 42896192, [DOI](https://doi.org/10.7326/ANNALS-26-01667)).** **Deferred, day 19.** Weekly re-check, next 2026-11-12; abstract-only date 2026-11-19.

**Shelf status: three spares remain**, reordered today — **(A) the Nature Medicine gait foundation model** (PMID 42995231, newly added, now the priority item, PMC status not yet checked); (5) precision-psychiatry six-stage framework review (PMID 42947584, PMC13720497); (6) explainable-AI urology review of 70 studies (42960345). **Next run takes the gait paper** if a full text is reachable, since its multiplicity story is the most instructive thing currently available; otherwise spare (5).

**Watch item:** PM Heart trial results (protocol PMID 42893738), quarterly.
