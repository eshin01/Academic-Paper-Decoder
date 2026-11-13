# Reporting completeness of clinical trials evaluating large language model interventions in medicine: systematic review

**Authors:** Chen D, Blayne A, Ning T, Chattha I (University of British Columbia); Afshar M (University of Wisconsin); Ong JCL (Duke-NUS, Singapore General Hospital); Hong JC (UCSF); Liu N (Duke-NUS, NUS); Celi LA (Beth Israel Deaconess, MIT, Harvard Chan); Moons KGM (UMC Utrecht); Collins GS (University of Birmingham, NIHR Birmingham BRC); Bitterman DS (Mass General Brigham, Harvard Medical School, Brigham and Women's/Dana-Farber) — corresponding author.
**Journal:** BMJ, 2026; 395: e100855 (published 13 October 2026)
**Article type:** Systematic review and meta-research analysis
**Decoded:** 2026-11-13

**Analysis basis: ABSTRACT ONLY.** This is one of three abstract-only entries in this reading list, and the fallback is declared under the list's standing twenty-one-day rule: a deferred paper whose full text has not opened after three weeks gets decoded from its abstract rather than waiting indefinitely. **Today is day 31.** The full text is genuinely unreachable from this session, and here is exactly what was tried: a PMID-to-PMCID conversion returns **no PubMed Central identifier** (re-checked today, as on every previous day); the Scite full-text service is paywalled on this account; the publisher host `www.bmj.com` **does not resolve under this session's network policy**, the same block that stops `doi.org`; and a semantic-literature search for an open-access copy or preprint returned only the same abstract. **No Methods, no Results tables, no per-item figures, no limitations section, no funding or competing-interests statement.** Every number below comes from the published structured abstract, which is unusually complete, or from my own arithmetic on it, or from two external papers I retrieved and verified independently and have labelled as such.

**What this costs, stated up front.** The two facts that would most change the grade are both invisible to me: **the inter-rater reliability of the three raters whose judgements are the entire output**, and **any confidence interval on any of the seven headline percentages.** Neither appears in the abstract. They may well be in the full text, and Section 4 flags that possibility every time it raises the point.

**Source links (verified):**
- DOI: https://doi.org/10.1136/bmj-2026-100855
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42869550/
- Full text: **not available** — no PubMed Central copy exists as of 2026-11-13, and the publisher page could not be reached from this session. No full-text link is given because none could be verified.

**Basis of link verification.** Direct URL fetching is blocked here, so verification was done against the live PubMed/NLM record. According to PubMed, a query for PMID 42869550 returned this exact title, these twelve authors with these affiliations, *BMJ* volume 395 page e100855, publication date 13 October 2026, DOI `10.1136/bmj-2026-100855`, article types "Journal Article / Systematic Review / Meta-Analysis", and MeSH terms including Large Language Models and Research Report. A PMID-to-PMCID conversion returned **PMID only, no PMC identifier.** Both halves were confirmed independently, and **no link is included that was not verified.**

**Funding and competing interests: not reportable.** Not in the abstract, and I could not retrieve the statement. **This matters unusually much here, and Section 4 explains why:** I verified from PubMed that **five of the twelve authors are also authors of TRIPOD-LLM**, one of the seven instruments this paper scores adherence against.

**Reporting guideline for this review itself: not stated in the abstract.** A systematic review would normally cite PRISMA, and meta-research of this kind often registers a protocol on PROSPERO. Neither is visible in what I can read. Section 4 declines to score the paper on that, for a reason given there.

---

## 1. The Gist

**Twelve researchers went looking for every clinical trial ever run on a medical chatbot, found 461 records, graded them against seven different official checklists, and discovered the papers fill in roughly half of what they are supposed to. The honest reading of that is more interesting than "half," and it is not the reading the headline invites.**

The question matters and is well chosen. **Large language models are being put in front of patients** — for education, for triage, for drafting clinical notes, for management advice — and the only way to know whether any of it works is to read the trials. But you can only judge a trial you can actually see into: what model, which version, what exactly was typed into it, what happened to the output, who got hurt. If those are missing, the trial is a story rather than evidence. So the authors asked a prior question: **can you even tell?**

They searched three medical databases and two trial registries, from January 2017 to December 2025. The haul was **461 records: 68 published trial reports, 15 protocols, and 378 trial registrations.** Then they graded each document against whichever official checklist fits it — **TRIPOD-LLM** and **CHART** for chatbot and model-specific reporting, **CONSORT 2025** and **CONSORT-AI** for finished trials, **SPIRIT 2025** and **SPIRIT-AI** for protocols, and the **WHO Trial Registration Dataset** for registry entries. Two reviewers screened independently; **three calibrated raters** scored the items.

**The headline numbers: TRIPOD-LLM 40%, CONSORT 2025 44%, CONSORT-AI 59%, CHART 52%, SPIRIT 2025 51%, SPIRIT-AI 57%, WHO registration dataset 61%.** Averages of how much of each checklist a typical document actually filled in.

And the authors' diagnosis of what is missing is specific and damning: trials **"prioritise narrative framing and commentary over the methodological detail needed for replication."** The gaps they name are precisely the things that would let you repeat the study — **data and intervention provenance, input preprocessing, model versioning and access modality, inference parameters, output postprocessing, and access to protocol, data and code.** And: **"Harms planning, monitoring, and reporting were often incompletely reported, limiting the critical appraisal of the safety of LLM interventions in healthcare."**

**Now the three things I found that the abstract does not tell you, each of which changes how you should read those seven numbers.**

**First: the same 68 documents scored 40% and 59% depending on which checklist was held up against them.** That is a **19-percentage-point spread on an identical set of papers.** The score is not purely a property of the papers. It is partly a property of the ruler.

**Second, and sharper: another research team scored the same named checklist on heavily overlapping literature and got a very different answer.** According to PubMed, He and colleagues in *npj Digital Medicine* examined 55 LLM-intervention studies from January 2022 to June 2025 and reported **mean CONSORT-AI adherence of 78.8%.** This paper reports **59%** for CONSORT-AI. **A gap of nearly 20 points on the same instrument, over much the same literature.** Both cannot be the field's adherence rate. What differs is how each team decided an item counts as "reported."

**Third: 40% to 61% may be close to ordinary for medicine, and the paper offers no yardstick to tell.** According to PubMed, Srinivasan and colleagues in *JAMA Network Open* audited **21,041 randomised trials across 30 disciplines** and found mean CONSORT compliance of **57.0% for 2010–2024**, ranging from **35.2% in pharmacology to 63.4% in urology.** **All seven of this paper's means fall inside that ordinary inter-speciality range.** That does not make the finding uninteresting — it relocates it. The striking number is not that LLM trials score about as badly as medicine generally does on generic checklists. **It is that they score worst of all, 40%, on TRIPOD-LLM, the one instrument written specifically for them.**

**What the paper gets exactly right.** The question is the right question, the search is broad, the instrument is matched to the document type rather than applied blindly, and the conclusion is stated in appropriately flat language: **"modest adherence,"** with the gaps named item by item. **It does not claim the trials are wrong — only that you cannot check.** That is the correct and more useful claim.

## 2. Study Snapshot

**Study type:** systematic review and **meta-research analysis** — research about research. The unit of analysis is a document, not a patient. **No patients were studied and no clinical outcome was measured**, which is appropriate: the question is whether other people's patient studies can be read.

**What was searched.** Bibliographic databases **Embase, Medline and CENTRAL** for trial reports and protocols. Trial registries **ClinicalTrials.gov** and the **WHO International Clinical Trials Registry Platform** for registrations. Window: **1 January 2017 to 6 December 2025.**

**Who was eligible.** Trial reports, protocols and registrations describing clinical trials of LLM interventions in medicine, where the LLM served a healthcare function — **patient education, clinical documentation, communication support, triage, care navigation, management recommendations, or clinical decision support.** Studies had to **prospectively assign human participants** to the intervention and evaluate a **health-related biomedical or behavioural outcome.** That last criterion is stricter than most reviews in this space and it is to the authors' credit: it excludes the enormous literature of chatbots answering exam questions with no human participants at all.

**What was found.** **461 records: 68 trial reports, 15 protocols, 378 registrations.** I verified that these sum exactly to 461, so every record is accounted for with no unexplained residual. Trial reports were **"predominantly small sample, single site randomised studies published between 2024 and 2025,"** spanning diverse specialties, **"primarily targeting patient facing education and management recommendations."**

**How completeness was judged.** Reporting guidelines **matched to study design and purpose** — TRIPOD-LLM, CONSORT 2025 and CONSORT-AI, SPIRIT 2025 and SPIRIT-AI, CHART, and the WHO Trial Registration Dataset version 1.3.1. Outcomes were **overall study-level and item-level reporting completeness.** **Two reviewers independently screened and extracted** trial and intervention characteristics; **three calibrated raters assessed item-level completeness.**

**The seven results.** On the 68 trial reports: **TRIPOD-LLM 40%, CONSORT 2025 44%, CONSORT-AI 59%, CHART 52%.** On the 15 protocols: **SPIRIT 2025 51%, SPIRIT-AI 57%.** On the 378 registrations: **WHO Trial Registration Dataset 61%.** All are described as mean reporting completeness, and all are described as **"modest."**

**What the authors say is missing from the trials.** Reproducibility elements: **data and intervention provenance, input preprocessing, model versioning and access modality, inference parameters, output postprocessing**, and **access to protocol, data and code** — all "inconsistently reported." And **harms planning, monitoring and reporting** "often incompletely reported."

**Their conclusion, verbatim:** clinical trials of LLM interventions "show modest adherence to established reporting guidelines, with persistent underreporting of LLM specific methodological details, reproducibility artefacts (protocols, data, code), and harms reporting required to support reproducibility and confident appraisal of safety risks before their clinical translation."

**My own arithmetic on these figures, all of which checked out.** The record counts close exactly (68 + 15 + 378 = 461). **The registration-to-report ratio is 378 ÷ 68 = 5.6** — for every finished, published trial report there are about five and a half trials merely registered. **Trial reports are only 14.8% of all records.** The nominal search window is **8.9 years**, but usable chatbots postdate late 2022, giving a real window of about **3 years** with the bulk concentrated in **2024–2025** — so roughly **22 reports per year** at most. The four report-level instruments span **40% to 59%, a 19-point spread on identical documents.** And both **base-versus-extension pairs run in the same direction**: CONSORT-AI scores **15 points higher** than CONSORT 2025, and SPIRIT-AI **6 points higher** than SPIRIT 2025, on the same documents.

**Two external comparators, retrieved and verified separately, and labelled as mine not the paper's.** According to PubMed: **He Z, Yang L, Liang Z, Li X, Du J**, "Clinical outcomes and reporting quality of large language model interventions in practice: a systematic evidence map," *npj Digital Medicine* 2026;9(1), **PMID 42230743**, [DOI](https://doi.org/10.1038/s41746-026-02837-6) — 55 studies, January 2022 to June 2025, **mean CONSORT-AI adherence 78.8%.** And **Srinivasan A, Berkowitz J, Friedrich NA, Kivelson S, Tatonetti NP**, "Large Language Model Analysis of Reporting Quality of Randomized Clinical Trial Articles: A Systematic Review," *JAMA Network Open* 2025;8(8):e2529418, **PMID 40875232**, [DOI](https://doi.org/10.1001/jamanetworkopen.2025.29418) — **21,041 RCTs**, mean CONSORT compliance **57.0% (95% CI 56.8% to 57.2%) in 2010–2024**, up from 27.3% in 1966–1990, by discipline **35.2% (pharmacology) to 63.4% (urology)**, with allocation concealment reported in only **16.1%** and external validity discussed in **1.6%.**

**One verified fact about the author list.** According to PubMed, the TRIPOD-LLM guideline (Gallifant J et al.) carries among its authors **Afshar M, Collins GS, Moons KGM, Celi LA and Bitterman DS** — **all five of whom are also authors of this review**, Bitterman as its corresponding author. TRIPOD-LLM comprises **19 main items and 50 subitems** in a modular format, of which 14 main items and 32 subitems apply across all categories.

**Not reported in the abstract, and not retrievable:** any confidence interval on any of the seven means; any inter-rater reliability statistic for the three raters; the scoring rule by which an item counted as complete, and the denominator used; the per-item percentages behind every narrative claim about provenance, versioning and harms; whether any non-LLM comparator was scored; PROSPERO registration and this review's own protocol, data and code availability; funding; competing interests.

## 3. How Strong Is This Evidence? (Grade 3 out of 5)

**This is a well-posed question, answered by a strong team in a top journal with a defensible design — and I am reading its abstract. The grade reflects both halves of that sentence, and it would plausibly be a 4 if the full text showed the two statistics the abstract omits.**

**What is clearly good, and visible even from here.**

**The question is the right one and it comes first in the right order.** Before asking whether medical chatbots work, ask whether the trials can be read at all. A field that skips that step accumulates citations instead of knowledge — which is the founding concern of this whole reading list.

**The search is broad and the eligibility criteria are strict in the right place.** Three databases plus two registries, and crucially the requirement that studies **prospectively assigned human participants and evaluated a health-related outcome.** That single criterion excludes the vast "we asked GPT-4 some exam questions" literature. It is why 68 reports is a believable number rather than a suspiciously small one.

**Including registrations and protocols, not just published papers, is the best design decision here.** It is also what produces the paper's most under-sold finding: **378 registrations against 68 reports.** Looking only at published trials would have hidden the pipeline entirely.

**Matching the instrument to the document is correct and not universal.** Protocols were scored against SPIRIT, registrations against the WHO dataset, reports against CONSORT and TRIPOD-LLM and CHART. A lazier version of this paper would have applied one checklist to everything.

**Dual independent screening and three raters** is the right structure for subjective item-level judgement.

**And the conclusion is calibrated.** "Modest adherence" with named gaps. **The paper does not claim the trials are wrong, only that you cannot check them** — which is the claim its evidence actually supports, and the more useful of the two.

**What holds it to 3.**

**I am reading an abstract.** The standing rule in this list is that a deferred paper gets decoded from its abstract at three weeks rather than waiting forever; this one is at thirty days. But the rule does not make an abstract into a paper. **I cannot see the Methods, so I cannot verify the thing that makes or breaks a study of this kind: how an item was scored.** Section 5 shows that this choice can move the headline by twenty points.

**The two statistics that constitute this paper's precision are absent from what I can read.** For a study whose entire output is three people's judgements of 461 documents, **the inter-rater reliability is the precision** — a kappa or an ICC. None appears. And **not one of the seven headline percentages carries a confidence interval.** My arithmetic shows why that matters: on **15 protocols**, with a plausible spread of per-document scores, the 95% interval is roughly **±5 to ±10 points**, which means the SPIRIT 2025 versus SPIRIT-AI difference of 6 points is well inside noise. **Both may be in the full text.** I flag it as unverifiable, not as absent.

**There is no comparator, and without one "modest" has no referent.** This is the substantive methodological gap rather than a reporting one, and it is the clearest thing I can say from an abstract. Against the general-RCT baseline I retrieved, **all seven means sit inside the ordinary 35.2%–63.4% range across medical specialities.** A contemporaneous sample of non-LLM trials, scored by the same raters under the same rules, would have turned "LLM trials report modestly" into "LLM trials report worse or no worse than comparable trials" — a different and far more actionable claim.

**Five of twelve authors wrote one of the instruments.** Discussed in Section 4. It is not disqualifying and there is a real argument it was necessary. It is still a structural fact a reader should have, and the statement that would normally disclose it is the one I cannot read.

**The protocol-level findings rest on 15 documents.** Two of the seven headline numbers come from a sample of fifteen. The abstract presents all seven in one undifferentiated list.

**Why not 2.** Because the design is genuinely sound and the question is well chosen. The abstract-only entry in this list that scored 2 had deeper problems than invisibility — an unvalidated classifier producing every percentage, and a metric that was arithmetically forced. Here, what I cannot see is detail; what I can see is reasonable.

**Why not 4.** Because a grade in this list tracks what a reader may safely conclude, and from here a reader can safely conclude only that **a competent team found incomplete reporting and named the gaps.** Whether 40% is alarming or ordinary, and whether the three raters agreed with each other, are both unanswered. **If the full text reports an ICC above about 0.75, publishes its scoring rule, and gives confidence intervals, this is a 4** — and I will upgrade the entry if a PMC body ever appears.

## 4. The Editor's Concerns

**1. The score is partly a property of the ruler, and the paper's own numbers prove it.** Four instruments were applied to the **same 68 trial reports** and returned **40%, 44%, 52% and 59%** — a **19-point spread with the documents held constant.** The abstract presents all seven figures in a flat list, as though they were seven measurements of one underlying quantity. **They are not.** They are measurements of different quantities with different item sets and, necessarily, different scoring decisions. A reader who takes away "about half" has averaged across incommensurable rulers. Section 5 teaches this as the entry's main lesson.

**2. A different team got 78.8% where this one got 59%, on the same named instrument.** This is the sharpest external check available and it is not in the paper. According to PubMed, **He et al.** (*npj Digital Medicine* 2026, PMID 42230743) scored **mean CONSORT-AI adherence at 78.8%** across 55 LLM-intervention studies from January 2022 to June 2025. This paper reports **59%** across 68 trial reports from a window that contains almost all of He's. **Nearly 20 points apart.** The samples differ and the windows differ, and I cannot establish the overlap without both full texts — I say that plainly. But **two careful teams scoring the same checklist on substantially the same literature should not differ by twenty points unless the scoring rule is doing much of the work.** Which is exactly the problem: **neither paper's scoring rule is in its abstract.** The field auditing reporting completeness has a reporting-completeness problem of its own.

**3. No comparator, so "modest" floats free.** Against the general-RCT baseline (**57.0% mean CONSORT across 21,041 trials; 35.2% to 63.4% by discipline**, per Srinivasan et al., PMID 40875232), **all seven of this paper's means land inside the normal inter-speciality range.** Two caveats I will not bury: **CONSORT 2025 is a newer and expanded instrument** than the CONSORT 2010 those 21,041 trials were scored against, and **they were scored by a language model**, not by human raters. So this is a calibration, not a head-to-head test. **But that is the point** — the paper should have supplied the head-to-head itself. One contemporaneous sample of non-LLM trials, same raters, same rules, would settle whether LLM trials are unusually opaque or merely as opaque as medicine generally is. **Without it, the finding risks being read as "LLM trials are bad" when the defensible reading may be "trial reporting is bad, and LLM-specific items are worse."**

**4. And that defensible reading is the stronger paper hiding inside this one.** Look at where the floor actually is. The generic instruments come in at 44%, 52%, 59%, 61% — unremarkable by the baseline above. **TRIPOD-LLM, the only instrument built specifically for language models, comes in lowest at 40%.** That is the finding with real teeth: **the field is roughly normal at the reporting it inherited and worst at the reporting that is new to it** — model versioning, inference parameters, prompt and preprocessing detail, access modality. The authors' narrative says exactly this. **Their headline number does not, and their abstract's flat list of seven buries it.**

**5. Five of twelve authors are authors of TRIPOD-LLM, including the corresponding author.** Verified from PubMed: **Afshar, Celi, Moons, Collins and Bitterman** appear on both this review and the TRIPOD-LLM guideline; Collins and Moons are additionally the originators of TRIPOD itself. **The case for it is real** — item-level scoring against a modular 19-item, 50-subitem instrument needs people who know what each item means, and the alternative is naive raters producing noise. **The case against is equally real:** the instrument that scores lowest, and therefore carries the paper's strongest claim, is the instrument five authors wrote. Nobody is better placed to apply it, and nobody has more at stake in it mattering. **This is precisely what a competing-interests statement exists to disclose, and that statement is in the part of the paper I cannot reach.** I am not alleging it was undisclosed. I am saying a reader should look it up, and that the paper would be strengthened by having had at least some raters with no stake in any of the seven instruments.

**6. No inter-rater reliability, no confidence intervals, in a paper about reporting completeness.** Three raters produced every number here. **"Calibrated" is asserted; it is not quantified.** For subjective item-level scoring, a kappa or ICC is not a nicety — it is the study's precision, and Section 5 explains why. Likewise not one of the seven means carries an interval, and **two of them rest on 15 documents**, where my arithmetic puts the plausible 95% half-width at roughly 5 to 10 points. **I flag both as unverifiable rather than missing**, since the full text may contain them. But the irony is worth stating without labouring it: **a paper documenting that others omit methodological detail presents its own primary outcomes as seven bare point estimates.**

**7. The registration-to-report ratio is a major finding presented as a sampling detail.** **378 registrations, 68 reports — 5.6 to 1.** Trial reports are **14.8%** of all records. Some of that is ordinary lag; a trial registered in 2025 cannot have reported. But a ratio that size says most of what has been promised in this field has not been delivered, and **the gap is where publication bias lives**: trials that found nothing are the ones that quietly never report. The abstract treats 378 as a denominator for the WHO completeness score. **It is also the paper's best evidence about the state of the field**, and the one number here that a reader can act on immediately — when someone cites the chatbot trial literature, the right question is what happened to the other five sixths.

**8. The 8.9-year window is nominal and the literature is about two years deep.** The search runs from January 2017, but usable large language models postdate late 2022, and the authors state reports were predominantly published **2024–2025.** So seven of the nine years contributed little or nothing. **This is not a criticism of the search** — casting back to 2017 is the correct, conservative choice. It is a caution against reading the finding as a trend. **Two years of literature cannot show whether reporting is improving**, and the one thing a reader most wants to know — are the new guidelines working? — is not answerable from this design.

**9. Both AI extensions scored higher than their base guidelines, and I cannot explain it.** **CONSORT-AI 59% beats CONSORT 2025's 44% by 15 points; SPIRIT-AI 57% beats SPIRIT 2025's 51% by 6 points** — on the same documents. If LLM-specific reporting were the weak spot, you would expect the opposite, and TRIPOD-LLM's 40% is consistent with that expectation while these two pairs run against it. Possible explanations are easy to list and impossible to test from an abstract: the extensions have fewer or more easily satisfied items, the 2025 base revisions added demanding new requirements, the extensions' items overlap material authors happen to include anyway. **I raise it as an unresolved inconsistency in the paper's own numbers rather than pretending to adjudicate it.** A reader should notice that the direction of the effect reverses between instruments and ask the full text why.

**10. On this review's own reporting, I am declining to score it, and saying so.** A systematic review would normally name PRISMA and register a protocol on PROSPERO; neither is in the abstract. **It would be cheap and unfair to score the paper on that** — abstracts routinely omit both and the full text very likely has them. I note it only because of where it sits in this list's running tally.

**11. The reporting-guideline tally, which this paper exists to quantify, now runs six entries.** Entry 69 named TRIPOD+AI and deposited the checklist. Entry 70 named STROBE while arguably being more careful. Entry 71 named none. Entry 73 named none and called for a checklist that does not exist. Entry 74 named none while doing more of what TRIPOD+AI asks than any of them. Entry 75 named none while running the best multiplicity treatment in this list. **Entry 76 is the paper that measures the whole phenomenon, and it puts a number on it: 40% mean completeness against the instrument written for the job.** The rule this list arrived at by observation — **the checklist is not the quality signal; read the methods** — is exactly what 40% means. **A checklist that is half-filled cannot discriminate good work from bad**, which is why entries 74 and 75 could do excellent work while naming nothing, and why naming TRIPOD+AI did not make entry 69 the most careful paper here.

**12. Credit for the part that is hardest to publish.** The sentence on harms — **"Harms planning, monitoring, and reporting were often incompletely reported, limiting the critical appraisal of the safety of LLM interventions in healthcare"** — is the most important in the abstract, and it is the kind of finding that makes a field uncomfortable with its auditors. Yesterday's entry in this list was a consumer health agent whose own clinician panel judged **2% of its outputs capable of moderate-to-severe harm**; that paper was unusual precisely because it ran the safety review and published the bad half. **This review's finding is that most trials in this space do not reliably do either.** Those two entries belong side by side.

## 5. Statistics Spotlight

Three concepts, numbered from 264 in the running list in `queue.md`. The first is the load-bearing one and this paper is an unusually clean demonstration of it.

**A completeness score measures the checklist as much as the paper.**

Here is the fact that should reframe the whole entry. **The same 68 trial reports were scored against four different checklists and came out at 40%, 44%, 52% and 59%.** The documents never changed. Only the ruler did, and the ruler moved the answer by **19 percentage points.**

**Why this happens.** A "reporting completeness" score is built by taking a checklist of items, deciding for each one whether a paper reported it, and averaging. **Three separate choices are buried in that sentence**, and each one moves the number:

- **Which items.** TRIPOD-LLM has **19 main items and 50 subitems**, and is explicitly *modular* — only 14 main items and 32 subitems apply across all study categories. CONSORT-AI is an extension bolted onto a general trial checklist. These are not the same questions, so they cannot have the same answer.
- **What counts as reported.** A paper says it used "GPT-4." Is the item "model version reported" met? A strict rater says no — GPT-4 had many versions and the item asks for the one used. A lenient rater says yes — a model was named. **One judgement call, applied across 50 subitems and 68 papers, and your headline shifts by double digits.**
- **What the denominator is.** If modular items are scored only when applicable, each paper has its own denominator, and the "mean completeness" is an average of percentages with different bases. That is a legitimate choice and a different quantity from "share of all items met across the corpus." **Which one is being reported here is not visible from the abstract.**

**And now the demonstration that this is not hypothetical.** According to PubMed, **He et al.** (*npj Digital Medicine* 2026, PMID 42230743) scored **mean CONSORT-AI adherence at 78.8%** on 55 LLM-intervention studies. This paper scored **CONSORT-AI at 59%** on 68 reports from an overlapping window. **Same named instrument, nearly 20 points apart.** The literature did not change that much in a few months. **The scoring rule did.**

**The everyday version.** Two inspectors grade the same restaurant kitchen. One uses a 20-point sheet and marks an item "pass" if the practice exists; the kitchen gets 78%. The other uses a 50-point sheet and marks "pass" only if the practice is written down, dated, and followed; the kitchen gets 59%. **Neither inspector is lying and neither score is wrong.** But "this kitchen is 78% compliant" and "this kitchen is 59% compliant" are not two estimates of one number — they are answers to two different questions. **If you only ever see one score, you cannot tell which question you were told the answer to.**

**Watch out for:** any adherence, completeness, or quality-score percentage quoted without the instrument named, the version named, and the scoring rule published. **Three specific questions to ask:** which checklist and which version, what counted as "reported" for a partially reported item, and was the denominator the same for every paper. **A completeness score without those three is not comparable to any other completeness score**, including a later one from the same field — which means it cannot be used to show improvement over time, the thing such scores are most often used for.

**A score with no comparator is not yet a finding.**

The paper calls 40%–61% "modest." **Modest compared to what?** The implied comparator is 100%, which no literature in medicine has ever achieved on any checklist. Against that standard every field fails, and the word carries no information.

**Here is a real comparator, which I retrieved separately.** According to PubMed, **Srinivasan et al.** (*JAMA Network Open* 2025, PMID 40875232) audited **21,041 randomised trials** for CONSORT adherence: mean compliance **57.0% (95% CI 56.8% to 57.2%)** for 2010–2024, up from **27.3%** in 1966–1990, and ranging across disciplines from **35.2% in pharmacology to 63.4% in urology.** Within those trials, **allocation concealment was reported in 16.1%** and **external validity discussed in 1.6%.**

Hold the two side by side. **All seven of this paper's means — 40, 44, 51, 52, 57, 59, 61 — fall inside the ordinary 35.2% to 63.4% range across established medical specialities.** On generic trial reporting, LLM trials look like medicine.

**Two caveats I am not going to hide, because they are the reason this is a calibration and not a verdict.** CONSORT 2025 is an **expanded** instrument compared with the CONSORT 2010 those 21,041 trials were scored against, so a lower score is partly expected. And those 21,041 were scored by a **language model** (validated at 91.7% agreement with experts on a 70-article subset, macro F1 0.86), not by human raters. **Different ruler, different rater — exactly the problem technique 264 just described.**

**Which is the whole argument.** The comparison I can assemble from outside is weak precisely because the instruments differ. **A comparison from inside the paper would have been strong**: take a contemporaneous sample of non-LLM trials, give them to the same three calibrated raters, score them under the same rules, and report both. That one addition converts "LLM trials report modestly" into either "LLM trials are unusually opaque, by this much" or "trial reporting is broadly poor and LLM-specific items are the exception." **The second is what this paper's own pattern suggests** — generic instruments near the medical norm, TRIPOD-LLM lowest at 40%. **It is a better finding and the design cannot quite support it.**

**The everyday version.** You are told a student scored 44% on a test. Alarming — until you learn the class average was 45% and the test was designed so that nobody finishes. **The score alone told you nothing; the distribution told you everything.** A score with no comparator is a number in search of a finding.

**Watch out for:** evaluative words — "modest," "suboptimal," "poor," "inadequate" — attached to a percentage with no reference distribution. **Ask what a good score would have been, and what comparable work scores.** If the paper does not say, go and find a baseline before you repeat the number, because the word is doing the work the data has not done.

**When the measurement is a human judgement, the reliability of that judgement IS the precision.**

Every number in this paper came from **three calibrated raters** deciding, item by item, whether a document reported a thing. That is a perfectly respectable measurement method. It also has a specific weak point, and it is not sample size.

**Why reliability is the precision here.** With a blood test, the instrument is fixed and the uncertainty comes from sampling — more patients, tighter interval. With human raters scoring subjective items, there are **two** sources of error: which documents you happened to sample, **and whether your raters agree with each other.** The second does not shrink when you add documents. **If two raters would disagree on a third of the items, then your 40% carries an irreducible wobble that no amount of extra papers removes.** It just means you have measured an unreliable quantity very precisely.

**How it is normally reported.** Two statistics: **Cohen's or Fleiss' kappa** (agreement among raters corrected for the agreement you would get by chance alone) and the **intraclass correlation coefficient, ICC** (how much of the variation in scores reflects real differences between documents rather than disagreement between raters). Conventional readings: **ICC 0.75–0.90 is good, above 0.90 excellent**; kappa above 0.8 is strong, 0.6–0.8 substantial, below 0.4 poor. **Yesterday's entry in this list reported ICC(3,1) = 0.838 for its automated rater before using it, and Fleiss' κ ≥ 0.684 for its human panels** — that is what the practice looks like when it is done.

**Neither statistic appears in this abstract.** "Calibrated" tells you the raters were trained together. **It does not tell you whether they then agreed.** The full text may well report it, and I will not claim otherwise — but from where I sit, **the precision of all seven headline numbers is unknown.**

**And the ordinary kind of precision is missing too.** Not one of the seven means carries a confidence interval. **Two of them rest on 15 protocols.** Running the arithmetic: if per-document completeness varies with a standard deviation of 10 to 20 percentage points, the standard error on **68 reports** is about **1.2 to 2.4 points** (95% interval ±2 to ±5), but on **15 protocols** it is about **2.6 to 5.2 points** — a 95% interval of roughly **±5 to ±10 points.** **So SPIRIT 2025 at 51% and SPIRIT-AI at 57% are six points apart with intervals that overlap heavily.** Treating that gap as a real difference between the two instruments is not supportable from fifteen documents.

**The everyday version.** Three judges score a diving competition. If they agree closely, the average score means something and adding more dives sharpens it. **If one judge consistently marks three points harder than another, then the average of their scores is a number about the judges as much as the divers** — and televising a hundred more dives will not fix it. Before you trust the leaderboard, you want to know how far apart the judges are. **That figure is the one not shown here.**

**Watch out for:** any study whose primary outcome is a human rating — chart review, image reading, checklist scoring, qualitative coding, quality appraisal — that describes its raters as "trained," "calibrated," or "independent" **without reporting a kappa or an ICC.** Those words describe the process; the statistic describes the result. **And a point estimate with no interval, on a sample in the dozens, is a number with the uncertainty edited out.** Ask for both, and be especially insistent when the paper's whole purpose is to hold others to a reporting standard.

## 6. Jargon Translator

**Meta-research** — research about research. Instead of studying patients, it studies the studies: how they were done, how they were reported, whether they can be trusted. This paper's unit of analysis is a document.

**Reporting completeness** — not whether a study was *done* well, but whether it was *described* fully enough for a reader to tell. A well-run trial can be badly reported, and vice versa. **These two things are often confused and this paper only measures the second.**

**Reporting guideline / checklist** — an agreed list of what a paper must state. Produced by expert consensus and hosted by the EQUATOR network. Not a quality score, a transparency score.

**CONSORT** — the checklist for reporting a completed randomised trial. **CONSORT 2025** is the current revision. **CONSORT-AI** is the extension adding AI-specific items.

**SPIRIT** — the equivalent checklist for trial *protocols*, the plan written before the trial runs. **SPIRIT-AI** is its AI extension.

**TRIPOD / TRIPOD+AI / TRIPOD-LLM** — the family for prediction-model studies. **TRIPOD-LLM**, published in 2025, is the language-model version: **19 main items and 50 subitems**, in a *modular* design where only some items apply to any given study type. It is the instrument LLM trials scored worst against, at 40%.

**CHART** — Chatbot Assessment Reporting Tool, for studies of chatbots giving health advice.

**WHO Trial Registration Dataset** — the minimum set of facts a trial must record when it registers, before it starts. Version 1.3.1 here.

**Trial registration** — publicly recording a trial before it begins, so that a trial which finds nothing cannot quietly disappear. **378 of the 461 records were registrations.**

**Trial report vs protocol vs registration** — the published results; the plan; the public pre-announcement. Three documents at three stages, which is why three different checklists were needed.

**Provenance (data and intervention)** — where the data and the model came from. Without it you cannot tell whether a model was tested on material it had already seen.

**Model versioning and access modality** — *which* version of the model, reached *how* (web interface, API, locally hosted). Models change silently under the same name, so a trial of "GPT-4" without a version and date is not repeatable.

**Inference parameters** — the dials set at query time, above all **temperature**, which controls how random the output is. At temperature 0 the same prompt gives nearly the same answer; higher, it varies. A result that depends on this setting is not interpretable without it.

**Input preprocessing / output postprocessing** — what was done to the text before it went in and after it came out. Often where the real work of a system lives, and routinely left undescribed.

**Harms planning, monitoring and reporting** — stating in advance what could go wrong, watching for it, and publishing what happened. The authors found this "often incompletely reported."

**Calibrated raters** — assessors trained together so they score consistently. **Describes the training, not the result** — technique 266.

**Inter-rater reliability** — how much the raters actually agreed, measured by **kappa** (agreement beyond chance) or **ICC** (share of score variation that reflects real differences between documents rather than rater disagreement). Not reported in this abstract.

**Publication bias** — the systematic disappearance of studies that found nothing, which makes the surviving literature look more positive than reality. The **5.6-to-1 gap between registrations and reports** is where it would hide.

## 7. What You Can (and Can't) Say

**You can say:**

"A BMJ systematic review identified 461 records on clinical trials of large language model interventions in medicine — 68 published trial reports, 15 protocols and 378 trial registrations — and graded each against the reporting guideline matched to it."

"Mean reporting completeness was modest throughout: TRIPOD-LLM 40%, CONSORT 2025 44%, CONSORT-AI 59% and CHART 52% for trial reports; SPIRIT 2025 51% and SPIRIT-AI 57% for protocols; and 61% against the WHO Trial Registration Dataset for registrations."

"The elements most consistently missing were the ones needed to repeat the study — data and intervention provenance, input preprocessing, model versioning and access modality, inference parameters, output postprocessing, and access to protocol, data and code."

"Harms planning, monitoring and reporting were often incompletely reported, which the authors say limits appraisal of the safety of these interventions."

"Published trial reports were predominantly small, single-site randomised studies from 2024 and 2025, mostly on patient-facing education and management recommendations."

"For every published trial report there were about five and a half registered trials." *(my arithmetic: 378 ÷ 68 = 5.6)*

**You cannot say:**

"LLM trials are badly conducted." **The paper measured reporting, not conduct** — whether you can see into the trial, not whether it was run properly. A well-run trial can be poorly described.

"Medical chatbots don't work." **This review did not assess whether a single intervention worked.** No effectiveness finding of any kind is in it.

"LLM trials report worse than other medical trials." **No comparator was scored.** The external baseline I retrieved — 57.0% mean CONSORT across 21,041 trials, 35.2% to 63.4% by discipline — puts all seven of these means inside the ordinary range for medicine, but on a different instrument version scored by a different kind of rater. **Not established either way.**

"Reporting completeness in this field is about 50%." **Four instruments on the same 68 documents gave 40%, 44%, 52% and 59%**, and another team scoring CONSORT-AI on overlapping literature got 78.8% against this paper's 59%. **There is no single number.**

"Reporting is getting worse" — or better. **The usable literature is about two years deep**, almost entirely 2024–2025. No trend can be read from it.

"The guidelines aren't working." **Possibly true and not shown here.** Most of these trials were designed and run before or alongside the publication of the very guidelines they are scored against, TRIPOD-LLM included.

"Only 40% of what should be reported is reported." **That is a mean of per-document percentages against a modular checklist**, which is not the same as the share of items met across the corpus. Which quantity is being reported is not visible from the abstract.

"These seven figures are equally solid." **Two of them rest on 15 protocols**, where the plausible 95% interval is roughly ±5 to ±10 points. No intervals are given for any of the seven.

**The honest one-sentence version:** *a strong team asked the right prior question — can anyone actually check the trials of medical chatbots? — searched broadly, graded 461 documents against seven matched checklists, and found roughly half of what should be stated is stated, with the gaps concentrated exactly where reproducibility and safety live; what the abstract cannot tell you is how much of that number is a property of the ruler rather than the papers, whether 40% is alarming or ordinary for medicine, and whether the three people doing the grading agreed with each other.*

## 8. Bottom Line for Your Life

**If you ever cite a study about a medical chatbot:** this paper is the reason to be careful, and it gives you four concrete questions. **Which model and which version, reached how? What exactly was typed in, and what was done to the answer? Were harms planned for, watched for, and reported? Is the protocol, data or code available?** On the evidence here, **most trials in this literature do not answer all four** — and a trial that cannot answer them cannot be repeated by anyone, including its own authors. This is the founding concern of this reading list with a number attached to it.

**If someone quotes you a compliance or quality percentage** — for anything, not just AI — **ask which checklist, which version, and what counted as compliant.** This entry is the cleanest demonstration in the list of why: the same 68 papers scored 40% and 59% on different rulers, and two teams scoring the same ruler differed by 20 points. **A percentage with no instrument named is not a measurement you can compare to anything.**

**If you are told a field's reporting is "modest" or "suboptimal":** ask what the comparison is. Medicine as a whole sits around 57% on CONSORT and ranges from 35% to 63% by speciality. **Against that, these numbers are unremarkable — except on TRIPOD-LLM, the instrument built for the job, where they are the lowest of all.** That is the real signal and it is the one a flat list of seven percentages hides.

**If you run clinical trials of AI tools:** the fix is cheap and almost entirely mechanical. **Record the model version and the date you queried it. Record the temperature and any other inference settings. Publish the exact prompts. Say what you did to the inputs and the outputs. Register the trial, post the protocol, and state your harms plan before you start.** None of that requires more patients or more money, and its absence is what put this literature at 40%. **The items being missed are not hard ones; they are new ones.**

**If you review or edit papers in this space:** the two statistics missing from this abstract are the two worth insisting on in anything built from human ratings — **an inter-rater reliability figure (kappa or ICC) and a confidence interval on every headline mean.** And for meta-research specifically, **ask for a comparator arm**; a score with nothing to compare it against cannot support the adjective it is given.

**If you are reading the coverage:** expect "AI trials fail transparency standards," built on the 40%. The figure is real and the gaps named are real. The three things that will not make the headline are that **the same documents score 59% on a different checklist**, that **another team got 78.8% on that same checklist**, and that **40%–61% sits inside the ordinary range for medical trial reporting generally** — which relocates the problem from "AI research is uniquely sloppy" to "trial reporting is weak everywhere and the AI-specific items are weakest."

**This is education, not medical advice.** Nothing here concerns any treatment decision. If an AI tool has been part of your care, that is a conversation with your own clinician.

---

## Appendix: the abstract-only fallback, deferred papers, and shelf status on 2026-11-13

**Why this was decoded from its abstract, and what was tried.** PMID 42869550 was first deferred on **2026-10-14** and has been re-checked daily since. **Today is day 31** — anchored on the 2026-11-10 record of day 28, which also reveals an off-by-one slip in the log: the 2026-11-12 entry repeated "day 29" from 2026-11-11 instead of advancing to day 30. The day count is corrected here and the slip is recorded in `queue.md` rather than quietly overwritten; it changes no decision, since the twenty-one-day threshold had long since passed. The standing rule in this list decodes a deferred paper from its abstract once it passes twenty-one days rather than waiting indefinitely. The threshold fired **yesterday, 2026-11-12**, and was deliberately slipped by one day because the long-deferred *Nature* personal-health-agent paper became available in full text that morning after 22 days, and the daily instruction puts full text ahead of abstract-only. **That deferral is now discharged.** Today, in order: a PMID-to-PMCID conversion returned **no PMC identifier**; **Scite** `read_fulltext` returned a paid-plan error, as on every previous attempt; the publisher host **`www.bmj.com` failed DNS resolution** under this session's network policy — the same block that affects `doi.org`, and per the session's own guidance no further hosts were tried; and a **Consensus** semantic search returned the record with the identical abstract and no open-access or preprint full text. **Full text is genuinely inaccessible, and the analysis says so in its header, in Section 3, and wherever a specific claim depends on it.**

**Two external papers were retrieved and verified to supply the comparator this review lacks**, and both are labelled in the analysis as mine rather than the paper's: **He Z et al.**, *npj Digit Med* 2026;9(1), PMID 42230743, PMC13530203, [DOI](https://doi.org/10.1038/s41746-026-02837-6) — 55 studies, **mean CONSORT-AI adherence 78.8%**; and **Srinivasan A et al.**, *JAMA Netw Open* 2025;8(8):e2529418, PMID 40875232, PMC12395317, [DOI](https://doi.org/10.1001/jamanetworkopen.2025.29418) — 21,041 RCTs, **mean CONSORT compliance 57.0% (95% CI 56.8–57.2) for 2010–2024**, range **35.2%–63.4%** by discipline. The **TRIPOD-LLM** author overlap was verified from the guideline's own PubMed record (Gallifant J et al., PMID 40739974 for the Korean translation carrying the same author list): **Afshar, Celi, Moons, Collins and Bitterman appear on both** that guideline and this review.

**Arithmetic verified today, all passing.** Record counts close exactly (68 + 15 + 378 = 461, no residual). Registrations per report **5.56**; reports are **14.8%** of records. Nominal search window **8.9 years**, post-ChatGPT span **3.0 years**, bulk in 2024–2025. Report-level instrument spread **40–59% = 19 points on identical documents**. Base-to-extension gaps **+15** (CONSORT) and **+6** (SPIRIT), both in the same direction, against TRIPOD-LLM's lowest-of-all 40%. All **seven** means inside the external **35.2–63.4%** inter-discipline range. Precision arithmetic on n=15 and n=68 as reported in Section 5.

**Deferred status, 2026-11-13.** **BMJ LLM-trial reporting review (42869550) — RESOLVED, decoded today as entry 76, abstract-only at day 31.** ***Annals* *Choosing Wisely* (42896192) — day 24**, re-checked today, **still no PMC copy**, weekly re-check, **abstract-only date 2026-11-19** — six days out; standing note that its 5.4% / 0.6–12.2% CI is a clustering signature computed across 15 recommendations rather than 4,050 responses. **Gait foundation model (42995231) — day 5**, re-checked today, **still no PMC copy**, abstract-only date **2026-11-30**; it carries the largest multiplicity problem this list will have faced (1,887 of 3,210 tested phenotypes called significant) and the first question for it is what false-discovery-rate procedure ran across those 3,210 tests.

**Landmark check, 2026-11-06 → 11-13.** Three records, all previously assessed: the NEJM mass-surveillance Perspective (43001754), the *Nature Medicine* gait commentary (43003904), and the gait foundation model itself (42995231). **No new candidates; none displaces the queue.**

**Plan set on 2026-11-13.** **Next run takes shelf item (C)**, the diabetic retinopathy model reporting **AUROC 0.972 from eight routine laboratory values** (PMID 42974596, PMC13727297), now owed since 2026-11-11 and twice postponed — once for entry 75's unblocking and once for today's abstract-only debt. It remains the deliberate contrast with entry 74's **AUC 0.587**, and today's entry sharpens the pick further: **technique 265 says a score with no comparator is not a finding, and 0.972 is a score very much in need of one.** The first question is unchanged and is now joined by a second. **Could the label be inside the inputs?** — two of the eight predictors are **nephropathy and neuropathy**, the other two microvascular complications of diabetes, routinely coded alongside retinopathy. **And: against what baseline is 0.972 being called good?** **Shelf after today: five spares — (B) bone-tumour reference-standard review, (C) next, (D) glaucoma OCT two-device external validation, (E) MIBC pCR with 102 models screened, (F) bitewing mannequin-only.**

**Standing watch item:** PM Heart trial results (protocol PMID 42893738), quarterly.
