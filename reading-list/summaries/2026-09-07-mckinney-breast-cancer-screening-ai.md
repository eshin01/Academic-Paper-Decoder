# International evaluation of an AI system for breast cancer screening

- **Authors:** Scott Mayer McKinney, Marcin Sieniek, Varun Godbole, … Demis Hassabis, Mustafa Suleyman, … Shravya Shetty (Google Health and DeepMind, with Imperial College London, University of Cambridge, Royal Surrey County Hospital, Northwestern Medicine, The Royal Marsden; 31 authors)
- **Venue:** Nature, 2020;577(7788):89–94 (published January 1, 2020)
- **DOI link:** https://doi.org/10.1038/s41586-019-1799-6
- **PubMed link:** https://pubmed.ncbi.nlm.nih.gov/31894144/ (PMID 31894144)
- **Full-text link:** open-access repository copy at https://doi.org/10.17863/cam.46260 (University of Cambridge Apollo) — the Nature version is closed access with no PubMed Central deposit
- **Basis:** ABSTRACT PLUS VERIFIED FULL-TEXT EXCERPTS retrieved from the open-access copy (methods, results, and discussion passages, quoted inline below). Not the complete paper: exact dataset sizes, funding, and competing-interest statements are marked "not reported in the text retrieved." Identifiers and all editorial notices verified against the live PubMed/NLM record and Scite.
- **Decoded:** 2026-09-07

---

# The Gist

Mammograms — X-rays of the breast used to screen healthy women for cancer — are hard to read, and both false alarms and missed cancers are common. Google Health and DeepMind built an AI, trained and tested it on real screening programmes in the UK and the United States, and reported it made fewer of both kinds of mistake than the radiologists whose historical decisions were on record. In a separate contest against six radiologists, it beat all six. And in a simulation of the UK system — where every mammogram is read by two doctors — letting the AI stand in for the second reader cut that workload by 88% without losing accuracy. The paper became famous twice: once for the results, and again nine months later, when a group of researchers published a formal rebuttal in Nature because the authors would not release their code, making the work impossible to check.

# Study Snapshot

- **Study type:** Retrospective evaluation on archived screening mammograms, plus a controlled reader study against radiologists and a computer simulation of a workflow change. No woman was screened or treated by the AI.
- **Data:** three screening centres in the UK and one in the US. The UK set is described as "representative"; the **US set is described as "enriched"** — meaning deliberately stocked with more cancers than occur naturally. Exact numbers of women or mammograms are not reported in the text retrieved.
- **How cancer was confirmed:** by biopsy plus long-term follow-up, with the follow-up window set by each country's screening interval plus a 3-month buffer. In the US, biopsied women contributed a scan from the 27 months before biopsy; non-biopsied women needed a follow-up event at least 21 months later.
- **Headline results:** absolute reductions in false positives of 5.7% (US) and 1.2% (UK), and in false negatives of 9.4% (US) and 2.7% (UK), compared with the recorded clinical decisions.
- **Reader study:** six radiologists. The AI's area under the curve exceeded the average radiologist's by an absolute 11.5%.
- **Workflow simulation:** standing in for the UK's second reader, the AI was "non-inferior" while cutting the second reader's workload by 88%.
- **A number worth holding onto:** among women actually recalled for further tests, only **22.8% in the UK and 4.9% in the US** turned out to have cancer. Most recalls are false alarms even under current human practice.
- **Funding / conflicts:** not reported in the text retrieved; PubMed tags NIH extramural support. Most authors were employed by Google Health or DeepMind.
- **Post-publication record:** an addendum/erratum (October 2020, https://doi.org/10.1038/s41586-020-2679-9); a formal Matters Arising, "Transparency and reproducibility in artificial intelligence" (Haibe-Kains et al., Nature 2020;586:E14–E16, https://doi.org/10.1038/s41586-020-2766-y); and the authors' reply (Nature 2020;586:E17–E18, https://doi.org/10.1038/s41586-020-2767-x).

# How Strong Is This Evidence?

**Grade: 3/5 — a large, thoughtfully designed study whose credibility is capped by what it would not let anyone check.**

The design has real strengths: two countries with different screening systems, cancer status confirmed by biopsy and years of follow-up rather than by opinion, a properly conducted reader study using the statistical machinery radiology reserves for this purpose, and an unusually honest discussion of a subtle bias in its own data (the "gatekeeper effect" below). Testing whether a UK-trained model works on US data is exactly the generalization question yesterday's pathology paper showed most of the field was ducking.

Two things hold it at 3. First, the analysis had flexibility that was resolved after looking at data: the authors state that for their seven primary comparisons, "the choice of superiority or non-inferiority was based on what seemed attainable from simulations conducted on the validation set" — deciding what to try to prove based on what looked winnable. Second, and more seriously, independent researchers could not reproduce any of it. The rebuttal in Nature quotes the authors' own position — "the code used for training the models has a large number of dependencies on internal tooling, infrastructure and hardware, and its release is therefore not feasible" — and concludes that "key details about their analysis are lacking." A result nobody outside the company can verify is a weaker result, however carefully it was produced.

# The Editor's Concerns

- **The US dataset was enriched.** The abstract says so plainly. Enrichment means the test population contains more cancers than reality, which is legitimate for measuring a model efficiently but inflates how impressive the numbers feel. The larger US improvements (5.7% and 9.4%) come from the enriched set; the UK improvements on the representative set are much smaller (1.2% and 2.7%). The honest summary of this paper is the UK number, not the US one.
- **Superiority versus non-inferiority was decided after looking at validation data.** In a rigorous trial, you declare in advance whether you are trying to prove "better" or merely "not meaningfully worse," because those tests have very different burdens of proof. Choosing per-comparison based on "what seemed attainable" converts a confirmatory result into an exploratory one.
- **Nobody could check the work.** This is the paper's defining legacy. Neither the code nor the data was released; a group of researchers published a formal Matters Arising in Nature arguing this violates basic scientific norms, and the authors replied. Whatever one concludes about who was right, the fact stands that an influential clinical claim rests on an analysis no independent party has reproduced.
- **The comparison is against historical decisions, not a live contest.** For the main results, the AI's judgments were compared with what radiologists had recorded at the time — under real time pressure, with real interruptions, and without knowing they were being scored. That is realistic in one sense and unfair in another: the AI faced a clean, unhurried version of the same task.
- **Six radiologists again.** As with the lung-CT paper, the reader study's human benchmark is an average of six people; a different six would move the 11.5% figure.
- **"Non-inferior" is a weaker claim than it sounds.** The workflow simulation shows the AI's substitution for a second reader was not meaningfully worse by a pre-defined margin — not that it was as good, and certainly not better. And it was a simulation: no real UK screening programme ran this way.
- **No outcomes, and no measure of overdiagnosis.** Finding more cancers earlier is only a benefit if those cancers would have harmed the woman. Screening's central controversy — overdiagnosis, treating cancers that would never have caused symptoms — is untouched here.
- **What this study did well:** biopsy-confirmed ground truth with multi-year follow-up rather than expert opinion; two health systems with genuinely different screening practices; an explicit cross-country generalization test; a proper multi-reader multi-case reader study; a frank analysis of the gatekeeper effect in its own data; and the useful, sobering reporting of how few recalls are actually cancer (22.8% UK, 4.9% US) under current human practice.

# Statistics Spotlight

**1. Superiority versus non-inferiority — two different questions, and why the order matters.**
- *What it is:* A superiority test asks "is A better than B?" A non-inferiority test asks the humbler question "is A not worse than B by more than some margin I decided in advance?" Non-inferiority is the right question when a new approach's appeal is convenience or cost rather than accuracy — as with replacing a human second reader.
- *How this paper used it:* Both, across seven primary comparisons — and, in the authors' own words, "the choice of superiority or non-inferiority was based on what seemed attainable from simulations conducted on the validation set."
- *The theory, with an analogy:* Imagine announcing before a race either "I will beat you" or "I will finish within five seconds of you." Both are honest claims — if you commit to one *before* running. Choosing after you have seen a practice run, based on which you can pull off, converts a test into a formality. The non-inferiority margin especially must be pre-specified, because a generous enough margin makes almost anything "non-inferior."
- *Watch out:* Non-inferiority results are routinely reported in press coverage as if they showed equivalence or superiority. When you see the word, ask three questions: what was the margin, was it set in advance, and who decided it was clinically acceptable? "Non-inferior" means "we could not rule out that it is somewhat worse, and we decided in advance that this much worse would be tolerable."

**2. Verification bias — the "gatekeeper effect," and why measured human accuracy can be an illusion.**
- *What it is:* You can only confirm cancer in someone who got a biopsy. Biopsies happen because a radiologist was suspicious. So the confirmed-cancer group is, by construction, made of cases the radiologist already flagged — which makes the radiologist look nearly perfect. Formally this is partial verification bias.
- *How this paper used it:* Impressively, the authors examined it directly, showing that "at short intervals, measured reader sensitivity is extremely high, owing to the fact that biopsies are only triggered based on radiological suspicion. As the time interval is extended, the task becomes more difficult and measured sensitivity declines." Their fix was to define cancer using long follow-up windows — a screening interval plus a 3-month buffer — so cancers the radiologist missed still surface later and count as misses.
- *The theory, with an analogy:* Judge a fire alarm only by inspecting buildings where it went off, and it will appear to have caught every fire — because the fires you'd need to count against it are in buildings nobody inspected. To measure honestly, you must follow the buildings where it *stayed silent* and see what happened later. That is precisely what a longer follow-up window does.
- *Watch out:* This bias inflates human performance in almost every retrospective diagnostic study, and its direction here is unusual — it makes the *comparison group* look better, so it works against the AI, not for it. When you read any diagnostic-accuracy study, ask: how was disease status established in people who were never tested? If the answer is "we assumed they were healthy," the reported sensitivity is optimistic for whoever chose who to test.

**3. Multi-reader multi-case (MRMC) analysis — the right way to run a human-versus-AI contest.**
- *What it is:* The statistical framework radiology uses when several readers each interpret the same set of cases. It accounts for two separate sources of randomness at once — the particular cases chosen, and the particular readers recruited — so conclusions generalize beyond both.
- *How this paper used it:* The methods state the AI was compared with the average radiologist "using methods for the analysis of multi-reader multi-case (MRMC) studies standard in the radiology community," via the ORH procedure, producing the headline 11.5% absolute AUC margin.
- *The theory, with an analogy:* Comparing a machine to one radiologist on one set of scans is like judging two restaurants from one meal each, cooked by one chef. MRMC is closer to sending several diners to each restaurant on several nights: it tells you whether the difference survives changing either the food or the judge. Ignoring reader variability — treating six radiologists as one fixed benchmark — would understate the uncertainty and overstate the AI's margin.
- *Watch out:* MRMC is the correct machinery, but it cannot manufacture readers you did not recruit. With six, the estimate of "the average radiologist" remains wobbly, and the population of radiologists it generalizes to is "readers like these six." Ask how many readers, from how many institutions, with what range of experience — and remember that reading in a study, unhurried and aware of being measured, is not the same job as reading a clinical list.

# Jargon Translator

- **Screening mammography:** X-ray imaging of the breast in women without symptoms, to catch cancer early.
- **Double reading:** the UK practice of having two radiologists independently read every screening mammogram, with a third opinion when they disagree. The US typically uses a single reader.
- **Recall:** being called back after a screening mammogram for more tests — not a diagnosis, and usually a false alarm.
- **Enriched dataset:** a test set deliberately containing more disease than the real population, used to measure a model efficiently — but which inflates how strong performance appears.
- **Absolute reduction:** a difference in percentage points (5.7% fewer false positives means 5.7 out of every 100), as opposed to a relative percentage change.
- **Non-inferiority:** a claim that a new approach is not worse than the old one by more than a pre-agreed margin.
- **Verification bias / gatekeeper effect:** the distortion that arises because only patients someone already suspected get the confirmatory test.
- **MRMC (multi-reader multi-case):** the study design and analysis for comparing readers and algorithms on shared cases.
- **Matters Arising:** Nature's format for a formal, peer-reviewed published challenge to a paper it printed.
- **Overdiagnosis:** finding a cancer that would never have caused symptoms or death — a real harm of screening, since it leads to treatment nobody needed.

# What You Can (and Can't) Say

**Fair to say:**
- "A 2020 Google Health and DeepMind study reported an AI reduced both false positives and false negatives relative to recorded clinical decisions on UK and US screening mammograms — by 1.2 and 2.7 percentage points in the representative UK data, and more in the enriched US data."
- "In a six-radiologist reader study using standard MRMC methods, the AI's AUC exceeded the average radiologist's by 11.5 percentage points."
- "In simulation, substituting the AI for the UK's second reader was non-inferior while cutting that workload by 88%."
- "The paper drew a formal published rebuttal in Nature because the code and data were not released, making independent reproduction impossible."

**Not fair to say:**
- "AI is better than doctors at reading mammograms" — it outperformed six radiologists in one study and outperformed *historical recorded decisions* elsewhere; the representative-population improvements were around 1–3 percentage points.
- "The AI reduces false positives by 5.7%" without saying that figure comes from the **enriched** US dataset.
- "This has been validated" — no independent group has been able to reproduce it, which is the specific objection Nature published.
- "AI screening saves lives" — no woman was screened by it; the study measures scan-reading accuracy, not mortality, and says nothing about overdiagnosis.

# Bottom Line for Your Life

This paper is the one to remember when you hear that a medical AI "beat doctors," because it demonstrates three separate lessons at once. The improvements were much smaller in the realistic UK population (1–3 percentage points) than in the enriched US one — so ask which population a number came from. The authors decided what they were trying to prove after looking at practice data — so ask what was pre-specified. And when independent researchers asked to check the work, the code could not be released, prompting a formal rebuttal in the same journal — so ask whether anyone outside the team has reproduced it. None of this means the system does not work; it means nobody outside the company knows. For a woman deciding about mammography, nothing here changes that decision: the case for screening rests on decades of trials, and the real trade-offs — false alarms, and overdiagnosis, which this paper does not address — are a conversation with a clinician. One study is one data point, and this one is still, six years on, unreplicated. This is an educational breakdown, not medical advice.

---

**Sources** (identifiers and editorial notices verified against the live PubMed/NLM record and Scite; full-text excerpts from the open-access repository copy. URL browsing is blocked in this environment, so links are constructed from those verified records):
- DOI: https://doi.org/10.1038/s41586-019-1799-6
- PubMed: https://pubmed.ncbi.nlm.nih.gov/31894144/
- Open-access full text (University of Cambridge repository): https://doi.org/10.17863/cam.46260
- Addendum / erratum (Oct 2020): https://doi.org/10.1038/s41586-020-2679-9
- Matters Arising, verified: Haibe-Kains et al. "Transparency and reproducibility in artificial intelligence." Nature 2020;586(7829):E14–E16. https://doi.org/10.1038/s41586-020-2766-y
- Authors' reply, verified: McKinney et al. Nature 2020;586(7829):E17–E18. https://doi.org/10.1038/s41586-020-2767-x
