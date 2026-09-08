# A comparison of deep learning performance against health-care professionals in detecting diseases from medical imaging: a systematic review and meta-analysis

- **Authors:** Xiaoxuan Liu, Livia Faes, Aditya U. Kale, … Eric J. Topol, Lucas M. Bachmann, Pearse A. Keane, Alastair K. Denniston (University of Birmingham, Moorfields Eye Hospital, UCL, Scripps, with one author at DeepMind)
- **Venue:** The Lancet Digital Health, 2019;1(6):e271–e297 (published September 25, 2019). Erratum November 2019 (https://doi.org/10.1016/s2589-7500(19)30160-8)
- **DOI link:** https://doi.org/10.1016/S2589-7500(19)30123-2
- **PubMed link:** https://pubmed.ncbi.nlm.nih.gov/33323251/ (PMID 33323251)
- **Full-text access:** gold open access (CC-BY) at the publisher via the DOI link; no PubMed Central deposit
- **Basis:** ABSTRACT PLUS VERIFIED FULL-TEXT EXCERPTS retrieved from the open-access version (results, discussion, and limitations passages quoted inline). Not the complete paper. Identifiers, the erratum, and open-access status verified against the live PubMed/NLM record and Scite.
- **Registration:** PROSPERO CRD42018091176 — the review's plan was publicly registered before it was carried out.
- **Funding:** None.
- **Decoded:** 2026-09-08

---

# The Gist

For seven days this reading list has worked through individual papers claiming an AI matched or beat doctors at reading medical images. This paper asks the question those papers cannot ask about themselves: **taken together, is any of it true?** A team led from Birmingham and Moorfields searched four databases, screened 31,587 studies, and found 82 that compared deep learning against health-care professionals on medical images. Their headline is genuinely reassuring — pooled accuracy was roughly equivalent, 87.0% sensitivity for the algorithms versus 86.4% for the professionals. Their real finding is alarming: out of 31,587 studies, only **14** did the comparison properly — testing both the machine and the humans on the same patients, using data the model had never seen. Everything else in the field, they conclude, is too poorly reported to interpret with confidence.

# Study Snapshot

- **Study type:** Systematic review and meta-analysis of diagnostic accuracy studies — the top tier of the evidence ladder for summarizing existing research, because it gathers *all* the evidence rather than cherry-picking. Registered in advance on PROSPERO, which prevents the authors from quietly changing their question after seeing results.
- **The search:** Ovid-MEDLINE, Embase, Science Citation Index, and Conference Proceedings Citation Index, covering January 2012 to June 2019.
- **The funnel:** 31,587 studies screened → **82 included** (147 patient cohorts) → 69 with enough data to build accuracy tables → 25 that tested on genuinely new data → **14** that compared algorithms and humans on the same sample.
- **How wildly results varied:** across the 69 studies, sensitivity ranged from **9.7% to 100.0%** (mean 79.1%) and specificity from **38.9% to 100.0%** (mean 88.3%).
- **The pooled comparison (from those 14 studies):** sensitivity 87.0% (95% CI 83.0–90.2) for deep learning versus 86.4% (79.9–91.0) for health-care professionals; specificity 92.5% (85.1–96.4) versus 90.5% (80.6–95.7).
- **What counted as truth:** reference standards varied widely — 37 studies used histopathology (tissue under a microscope), 28 used expert consensus, one used a single expert, nine used clinical follow-up, and eight used existing clinical notes or open-dataset labels.
- **Realism check:** only **four** of 82 studies tested the scenario that actually matters clinically — algorithm *plus* clinician working together. Only four gave the human readers the extra clinical information a real doctor would have. Just one tested whether having prior images helped.
- **Reporting quality:** 26 studies said they excluded low-quality images, 18 said they did not, and **38 did not report it at all**.
- **Conclusion in the authors' own words:** "we cautiously state that the accuracy of deep learning algorithms is equivalent to health-care professionals, while acknowledging that more studies considering the integration of such algorithms in real-world settings are needed."

# How Strong Is This Evidence?

**Grade: 4/5 — the highest-tier design on this reading list, executed carefully, and honest about the fact that its raw material is weak.**

This is the right kind of study to answer "does the field's central claim hold up," and it was done properly: pre-registered on PROSPERO, four databases searched, explicit inclusion rules, a hierarchical statistical model appropriate for pooling diagnostic accuracy, no funding from anyone with a stake, and authors who contacted original investigators for missing numbers (one of whom **confirmed an error in their own published table**).

It falls short of 5/5 for reasons that are mostly not the authors' fault. A meta-analysis can never be stronger than the studies inside it, and these studies were retrospective accuracy comparisons, not trials — so the pooled result describes image-reading skill, not patient benefit. The authors also state plainly: "We did not formally assess the quality of the included studies," so there is no formal risk-of-bias scoring. And the pooled figures come from just 14 studies, using each study's **best** result — an optimistic choice explained below.

# The Editor's Concerns

- **"Equivalent" rests on 14 studies out of 31,587 screened.** That is the story. The pooled sensitivity difference is 0.6 percentage points with confidence intervals that overlap almost completely — this is not a finding that AI is as good as doctors so much as a finding that the literature cannot currently tell the difference.
- **The pooled numbers used each study's best-case result.** The analysis restricted itself "to the contingency table for each study reporting the highest accuracy." Among the 14 studies there were 31 accuracy tables for algorithms and 54 for professionals; picking the highest from each biases the pooled estimate upward — for both sides, but it means these are ceiling figures, not typical ones.
- **No formal quality appraisal.** Most systematic reviews score each included study for risk of bias using a tool such as QUADAS. This one explicitly did not, so a beautifully designed study and a sloppy one carry equal weight in the pool.
- **The underlying studies rarely resembled clinical practice.** Only four of 82 tested algorithm-plus-clinician — the way these tools are actually deployed. Only four let the human readers see the clinical information a real doctor would have. This is the same handicapping you saw in the Esteva, Hannun, and Ardila papers, now quantified across the whole field.
- **Truth standards were inconsistent.** Some studies confirmed disease with tissue biopsy; others used expert opinion, and eight used labels scraped from clinical notes or open datasets. Pooling accuracy across those is pooling different questions.
- **Poor reporting was pervasive, and the authors are careful about what that means.** Their own caveat is worth quoting: "inadequate reporting does not necessarily mean that the study itself was poorly designed and, equally, that poor study design does not necessarily mean that the deep learning algorithm is of poor quality." Bad paperwork is not proof of a bad model — it just makes the model unjudgeable.
- **The review itself needed an erratum**, published two months later.
- **What this study did well:** pre-registration; a genuinely exhaustive search; transparent reporting of its own funnel from 31,587 down to 14; the confirmation — with data — that internal validation overestimates accuracy for both algorithms *and* humans; contacting authors and catching a published error; no funding; and a constructive conclusion that helped launch reporting standards (TRIPOD-ML, CONSORT-AI, SPIRIT-AI) rather than merely complaining.

# Statistics Spotlight

**1. The evidence funnel — and why a meta-analysis inherits the quality of what goes into it.**
- *What it is:* A systematic review searches for *every* study on a question by pre-declared rules, then narrows to those meeting quality criteria. A meta-analysis then statistically combines the survivors. Registering the plan first (here, PROSPERO CRD42018091176) stops researchers from changing the question after seeing which answer emerges.
- *How this paper used it:* 31,587 → 82 → 69 → 25 → 14. Each narrowing has a reason: most studies weren't relevant, then some lacked usable numbers, then most never tested on new data, then most never tested humans on the same patients.
- *The theory, with an analogy:* A meta-analysis is often described as sitting at the top of the evidence pyramid, and it does — but only in the way a summary is as reliable as the documents it summarizes. Averaging fifty wobbly bathroom scales does not give you a laboratory balance; it gives you a confident-looking average of wobbly scales. The narrowing here is the review doing its job: refusing to average scales it cannot trust.
- *Watch out:* "It's a meta-analysis" is often deployed as an argument-ender. It should prompt two questions instead: how many studies actually made it into the pooled estimate (here, 14 — a number the headline never mentions), and were the included studies any good (here, formally unassessed)? A meta-analysis of weak studies is a precise summary of weak evidence.

**2. Best-case selection within studies — how a defensible choice tilts a result.**
- *What it is:* When one study reports several accuracy figures — different thresholds, different reader groups, different subgroups — the reviewer must pick one to pool. Picking the highest from each study produces an optimistic combined estimate.
- *How this paper used it:* Explicitly: the pooled figures come from "the contingency table for each study reporting the highest accuracy," drawn from 31 algorithm tables and 54 professional tables across 14 studies.
- *The theory, with a worked example:* Suppose five students each take three practice tests. Averaging everyone's best score tells you what the group can do on a good day — useful, but not what they'd score tomorrow. Report the average of all attempts and the number drops. Neither is dishonest; they answer different questions, and the paper is clear about which it answered.
- *Watch out:* The direction of this choice matters most when the two sides being compared have different numbers of chances. Here the professionals had 54 tables to the algorithms' 31, so both sides were flattered but not necessarily equally. Whenever you see pooled diagnostic figures, ask which of each study's numbers was used, and why.

**3. Overlapping confidence intervals — why "no detectable difference" is not "proven equal."**
- *What it is:* A confidence interval shows the range of values compatible with the data. When two groups' intervals overlap heavily, the data cannot distinguish them — which is not the same as showing they are the same.
- *How this paper used it:* Sensitivity 87.0% (83.0–90.2) for algorithms versus 86.4% (79.9–91.0) for professionals. Nearly total overlap, and the human interval is noticeably wider — a consequence of pooling only 14 studies.
- *The theory, with an analogy:* Two runners finish a race that was timed with a stopwatch accurate only to the nearest five seconds, and their times come out identical. You have not proven they run equally fast; you have proven your stopwatch cannot tell them apart. To claim genuine equivalence you must decide in advance how big a difference would matter, then show the interval excludes differences that large — the non-inferiority logic from yesterday's mammography paper.
- *Watch out:* This is the single most common misreading in medical statistics — "no significant difference" reported as "shown to be the same." Note how carefully the authors themselves phrase it: they "cautiously state" equivalence and immediately qualify it. Their caution did not survive into most of the headlines this paper generated.

# Jargon Translator

- **Systematic review:** a study of studies, gathering all research on a question by rules set in advance, so the conclusion cannot be built from cherry-picked papers.
- **Meta-analysis:** the statistical step that combines results from multiple studies into one pooled estimate.
- **PROSPERO:** the international registry where review teams publish their plan before starting, so the plan can be checked against what they actually did.
- **Contingency table:** the simple 2×2 grid of correct and incorrect calls — true positives, false positives, true negatives, false negatives — from which sensitivity and specificity are computed.
- **Out-of-sample external validation:** testing on data from a genuinely different source than the training data. Only 25 of 82 studies did it.
- **Internal validation:** testing on data held back from the same original dataset — easier, and shown here to overestimate accuracy for both algorithms and humans.
- **Reference standard:** the "truth" a test is judged against — biopsy, expert consensus, or clinical follow-up, in decreasing order of reliability.
- **Hierarchical model:** the statistical approach used to pool sensitivity and specificity together, since the two move in opposite directions as a threshold shifts.
- **TRIPOD-ML / CONSORT-AI / SPIRIT-AI:** reporting standards for AI studies developed partly in response to problems this review documented.

# What You Can (and Can't) Say

**Fair to say:**
- "A 2019 Lancet Digital Health systematic review of 82 studies found deep learning's pooled diagnostic accuracy roughly equivalent to health-care professionals — 87.0% versus 86.4% sensitivity — but based this on only 14 studies that compared both on the same patients."
- "Of 31,587 studies screened, only 25 tested their model on genuinely new data, and only 14 tested humans and algorithms on the same sample."
- "Reported sensitivity across studies ranged from 9.7% to 100%, and 38 of 82 studies did not even report whether they excluded poor-quality images."
- "The review concluded that poor reporting limits reliable interpretation of this literature, and helped prompt new AI reporting standards."

**Not fair to say:**
- "Science has proven AI is as good as doctors at reading scans" — 14 studies, best-case figures, overlapping intervals, and image-reading accuracy rather than patient outcomes.
- "This validates the AI imaging papers" — it does close to the opposite, finding most of them insufficiently reported to judge.
- "AI equals doctors in practice" — only four of 82 studies tested algorithm-plus-clinician, which is how these tools are actually used.
- "Meta-analysis, so it's settled" — the authors explicitly did not assess the quality of the studies they pooled.

# Bottom Line for Your Life

This is the most useful paper on your list for the purpose you started with — knowing whether to believe someone citing a study. It takes the entire genre of "AI matches doctors" headlines and puts a number on how much of it is checkable: 14 studies out of 31,587 screened. The pooled answer, roughly equal accuracy, is real but fragile: built from best-case figures, from studies whose quality was never formally scored, measuring image-reading rather than whether any patient was helped. Notice the discipline in the authors' language — "we cautiously state" — and notice that almost none of the coverage of this paper kept the word "cautiously." When someone cites a systematic review at you, the two questions that do the most work are: **how many studies actually made it into the pooled number, and were those studies any good?** Here the honest answers are "14" and "nobody formally checked." One study is one data point, even when that study is a study of studies. This is an educational breakdown, not medical advice.

---

**Sources** (based on articles retrieved from PubMed, with full-text excerpts from the open-access version via Scite; identifiers and the erratum verified against the live NLM record — URL browsing is blocked in this environment, so links are constructed from those verified records):
- DOI (gold open access, CC-BY): https://doi.org/10.1016/S2589-7500(19)30123-2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/33323251/
- Erratum (November 2019): https://doi.org/10.1016/s2589-7500(19)30160-8
- Protocol registration: PROSPERO CRD42018091176
