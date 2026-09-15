# Medical large language models are vulnerable to data-poisoning attacks

- **Authors:** Daniel Alexander Alber, Zihao Yang, Anton Alyakin, Eunice Yang, … Douglas Kondziolka, Eric Karl Oermann (Department of Neurosurgery and Center for Data Science, NYU Langone Health and New York University, with collaborators at Washington University, Columbia, and Harvard Medical School) — 33 authors
- **Venue:** Nature Medicine, 2025;31(2):618–626 (published January 8, 2025)
- **DOI link:** https://doi.org/10.1038/s41591-024-03445-1
- **PubMed link:** https://pubmed.ncbi.nlm.nih.gov/39779928/ (PMID 39779928)
- **Full-text link used:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11835729/ (PubMed Central, open access)
- **Basis:** FULL TEXT — main text, all results sections, discussion, limitations, ethics statement, and the complete Methods were read from the open-access PubMed Central copy. Figures, Extended Data tables, and Supplementary Information were not retrieved, so anything living only there is marked as not retrieved rather than guessed. Two of the paper's P values appear in the running text in scientific notation whose exponents did not survive text extraction; those two are described rather than quoted, and every other number below is quoted exactly as retrieved. Funding and competing-interest statements are pointed to by the article but were not in the retrieved text. Identifiers verified against the live PubMed/NLM record; direct URL browsing is blocked in this environment, so links are constructed from that verified record.
- **Decoded:** 2026-09-15
- **Note on queue order:** taken ahead of three earlier queue entries whose full text is not reachable. Details at the end.

---

# The Gist

Large language models learn from enormous piles of text scraped off the open internet. This team asked an uncomfortable question: what if somebody deliberately salted that pile with medical lies? They generated 150,000 fake medical articles using a commercial chatbot, hid them inside web pages, mixed them into a standard training dataset, and trained real language models on the result. Replacing just **one millionth** of the training text — 0.001% — with vaccine misinformation produced a model measurably more likely to say things that could hurt patients, as judged by doctors who did not know which model they were reading. The attack cost **five dollars**. Then comes the part that should worry anyone who quotes AI benchmark scores: the poisoned models scored just as well as the clean ones on all five standard medical exams used to certify these systems. The damage was real and the tests could not see it.

# Study Snapshot

- **Study type:** A controlled computational experiment with blinded human assessment. The attack was simulated on the researchers' own copies of the data. No patient was involved and nothing was released into the wild.
- **What they examined first:** The Pile, a 400-billion-word training dataset built from 22 separate sources and containing 211,043,181 documents. They searched it for 60 medical terms drawn from a standard medical vocabulary — 20 each from general medicine, neurosurgery, and medication names — and found 14,013,104 matches spread across 9,531,655 documents, which is 4.52% of everything in the dataset.
- **How much of that sits in unguarded territory:** they sorted each source into "stable" (human-moderated, like PubMed and Project Gutenberg) or "vulnerable" (anyone can post, like web crawls, code repositories, and forum comments). 27.4% of the medical mentions — 3,845,056 of them — were in vulnerable sources, more than half from a single web crawl. And The Pile was chosen precisely because it is the *cleanest* option: more than a quarter of it comes from PubMed. Other common datasets are far worse. One is 91.2% vulnerable; three others are entirely web-scraped.
- **How the fake articles were made:** they asked a commercial chatbot to write articles contradicting evidence-based medicine — recommending dangerous treatments, inventing side effects. The safety guardrails were bypassed with prompt wording, with a failure rate under 1%. They produced 5,000 articles per medical concept, 150,000 in total, averaging about 600 words each. **The whole job took under 24 hours and cost less than US$100 per domain.**
- **How the poison was hidden:** the articles were embedded as invisible text inside HTML pages — zero-point fonts, off-screen text, text coloured to match the background. A human skimming the page would see nothing.
- **The models:** purpose-built transformer models in the style of GPT-3, at two sizes. The smaller had 1.3 billion adjustable settings and was trained on 30 billion words; the larger had 4 billion settings and 100 billion words. Each took 5 days on a university supercomputer.
- **The experiments:** first, six smaller models poisoned at 0.5% and 1.0% across three medical domains, with 10 concepts attacked per domain and 10 left alone as controls. Then six more models attacking a single concept — vaccines — at doses down to 0.001%.
- **Who judged the damage:** 15 people, 5 physicians and 10 senior medical students, blinded both to which model produced a passage and to whether the topic had been attacked. They were asked one question: could this text harm a patient? For the multi-concept experiments, 5,400 passages were reviewed; for the single-concept ones, 500 per combination of dose and model size.
- **What the poison did.** At 0.5% and 1.0%, every poisoned model produced more harmful text than the baseline, at significance levels the paper reports in scientific notation. Dropping to a single concept and far less poison: harmful completions rose by 11.2% at a dose of 0.01% (P = 0.00047) and by 7.2% at 0.001% (P = 0.01463) in the smaller model. In the larger model, replacing 1 million of 100 billion words — again 0.001% — raised harmful content by 4.8% (P = 0.03836). That took 2,000 fake articles, roughly 1,500 pages, generated for **US$5.00**.
- **It spread beyond the target.** Poisoned models produced more harmful content than the baseline even when asked about concepts the attack never touched (P = 0.0314 at 0.5%, P = 0.00484 at 1.0%). In the clean baseline model, attacked and untouched concepts behaved the same (P = 0.35), which is the control that makes the spillover finding interpretable.
- **The benchmarks saw nothing.** Poisoned models matched clean ones across all five standard medical benchmarks, with no consistent relationship between benchmark score and how much poison went in.
- **Three obvious fixes all failed** on the 4-billion model poisoned at 0.001%: careful prompting left 26.2% of responses harmful (P = 0.36), retrieval from trusted documents 28.4% (P = 0.66), and fine-tuning on a medical question dataset 35.9% (P = 0.99). None beat doing nothing.
- **What did work:** a defence that checks each medical claim against a fixed database of verified medical relationships — 21,706 concepts joined by 416,302 verified links. Tested on 1,000 passages containing 2,061 extracted claims, it caught 91.9% of harmful passages, with 81.3% of its alarms being genuine (F1 85.7%). At the level of individual claims, precision was 79.7% and recall 80.3% (F1 80.5%).
- **Funding / conflicts:** not present in the retrieved text; the article points to a separate statement.

# How Strong Is This Evidence?

**Grade: 4/5 — the claim is demonstrated cleanly, with the controls and blinding that most AI safety papers skip, and the main limit is the size of the models it was proven on.**

This is what a careful experiment looks like. There is a clean baseline model. There are control concepts inside each poisoned model, so the comparison is not only across models but within them. The people judging harm did not know which model or which concept they were looking at. There is a dose gradient — 1.0%, 0.5%, 0.01%, 0.001% — rather than a single condition, which is what turns "we made it worse" into "here is roughly how little it takes." Two model sizes were tested rather than one. Primary and secondary outcomes were stated in advance. Three plausible defences were tried and all three reported as failures. And the authors declined to release the poisoned models, the malicious data, or the training code, while explaining in the paper why they published the method anyway.

They also picked the hardest case for themselves on purpose. The Pile is the most heavily curated of the datasets they examined, with over a quarter of it drawn from PubMed. The attack worked there. On the datasets that are entirely web-scraped, the exposure is larger, not smaller.

What holds it at 4 rather than 5 is scale and endpoint. The models were 1.3 and 4 billion parameters; today's frontier systems are hundreds of times larger, and the paper's cost extrapolations to those models are arithmetic, not experiment. The authors say this plainly, and note it could cut either way, since bigger models may memorise their training data more readily. The second limit is that "harmful" is a human judgement, not a measurement, and the paper does not report how many reviewers rated each passage or how often they agreed with one another — a figure that would let a reader gauge how solid the harm rates are.

# The Editor's Concerns

- **The headline percentages are relative changes on an unstated base.** "Harmful completions increased by 11.2%" tells you the size of the jump but not what it jumped from. The underlying harm rates for each condition live in the supplementary tables, which this analysis did not retrieve. The one absolute figure that did appear — 26.2% of responses harmful for the prompt-engineered model — suggests the baseline rates were substantial, but that should not be read across to the other experiments.
- **Rater agreement is not reported.** Fifteen people judged harm, blinded, which is good. How many judged each passage, and how often two judges agreed, is not in the retrieved text. Without that, the precision of every harm rate is unknown — the same gap that weakened the Med-PaLM evaluation on your list two days ago.
- **The step from 4 billion parameters to frontier models is an inference.** The claim that poisoning a 70-billion-parameter model would cost under US$100 in article generation follows from scaling the token ratio. It was not tested. It is a reasonable projection and it should be labelled as one.
- **The misinformation came from a machine.** The fake articles were generated by a chatbot prompted to contradict medical guidelines. That is an efficient way to produce volume, and it means the poison has a particular texture. Whether human-written misinformation, or the ordinary bad medical content already sitting on the internet, behaves the same way is untested — though the authors argue their findings apply to incidental misinformation too.
- **The defence assumes its reference database is complete.** Any medical claim not found in the knowledge graph is flagged as misinformation. The authors state this openly: a genuinely correct statement about a new drug or an updated guideline will be marked wrong until somebody updates the graph. In a field where practice changes constantly, that is a real maintenance burden, not a footnote.
- **The defence can be fooled by true statements in a false arrangement.** The authors note that individually valid medical relationships could be assembled into a passage that is collectively misleading, and their method would pass each piece.
- **It leans on a commercial model for one step.** Extracting medical claims from text was done with GPT-4. So a defence whose selling point is not depending on web-trained language models does depend on one for its first stage. The authors flag this and suggest a purpose-built extractor would do better.
- **It is a simulation, not an observation.** Nobody has shown this attack happening in the wild. The paper's argument that it probably already happens by accident — through the ordinary flood of online medical nonsense — is plausible reasoning, not evidence.
- **What this study did well:** blinded human review with control concepts inside each model; a dose gradient across four poisoning levels; two model scales; a clean baseline whose target-versus-control comparison came out null, exactly as it should; three alternative defences tested and all three reported as failures; the hardest dataset chosen deliberately; an idealised upper-bound test of the defence (F1 99.3% when retrieval was perfect) to separate the method's ceiling from its implementation; a stated decision not to publish the harmful artifacts, with the reasoning given; and a limitations section that concedes scale, graph completeness, extraction quality, and the contextual-misinformation gap.

# Statistics Spotlight

**1. The two-proportion Z-test, and what a one-tailed test buys and costs.**
- *What it is:* When you want to know whether two groups differ in the *rate* of something — here, the share of passages judged harmful — you compare two proportions. The Z-test asks how likely it is that a gap this large would appear by chance alone if the two rates were really the same. One-tailed means you decided in advance that you only care about a difference in one direction.
- *How this paper used it:* Every harm comparison is a two-proportion, one-tailed Z-test, with the stated alternative hypothesis that poisoned models and attacked concepts produce *more* harmful content. That is where the reported P values come from: 0.00047, 0.01463, 0.03836 for the single-concept doses, and 0.0314 and 0.00484 for the spillover onto untouched concepts.
- *The theory, with a worked example:* Suppose 100 passages from a clean model and 100 from a poisoned one, with 20 and 30 flagged as harmful. The gap is 10 passages. Could that be luck? The test converts the gap into a standard score and reads off the probability. With 100 passages each it is borderline; with 1,000 each the same gap is decisive. This is why the sample sizes matter — 5,400 passages in the multi-concept trial is a lot of resolution. One-tailed is legitimate here because the direction was specified before looking: nobody is claiming poison makes a model safer. But one-tailed halves the P value for a given gap, so a one-tailed 0.038 is the same evidence as a two-tailed 0.076. Given a legitimate prior direction, that is a fair trade. Applied after the fact to whichever direction the data went, it is cheating.
- *Watch out:* A P value tells you the gap is probably not chance. It says nothing about how big the gap is, and nothing about whether it matters. P = 0.03836 attached to a 4.8% increase in harmful output is a real effect of modest size; P = 0.00047 attached to 11.2% is a bigger effect measured more confidently. Read the effect and the P value together, never the P value alone. And note the reverse case in this same paper: the failed defences came back at P = 0.36, 0.66, and 0.99. Those are not failures to find an effect that might be hiding — 0.99 means the fine-tuned model was, if anything, slightly worse.

**2. Precision, recall, and F1 — and why the "better" score is the worse safety tool here.**
- *What they are:* For anything that raises alarms, two numbers matter separately. **Recall** (also called sensitivity) is: of all the genuinely harmful passages out there, what share did the system catch? **Precision** is: of all the passages it flagged, what share were genuinely harmful? **F1** combines them into a single number by taking the harmonic mean, which punishes being lopsided.
- *How this paper used it:* The knowledge-graph defence, at the passage level, caught 91.9% of harmful passages (recall), and 81.3% of the things it flagged were truly harmful (precision), giving an F1 of 85.7%. They then compared against GPT-4, which scored a *higher* F1 of 88.7% — but a *lower* recall of 85.3%.
- *The theory, with a worked example:* Say 100 harmful passages are in the pile. The knowledge graph catches 92 and misses 8. GPT-4 catches 85 and misses 15 — nearly twice as many harmful passages slipping through — but raises fewer false alarms, so its combined score comes out ahead. Which tool do you want guarding medical advice? Almost certainly the one that misses 8, because a missed harmful passage reaches a patient while a false alarm reaches a reviewer who rolls their eyes. F1 treats those two mistakes as equally bad, and here they are not remotely equal. This is exactly the asymmetry that makes a smoke detector worth its occasional shriek at burnt toast.
- *Watch out:* F1 is the default because it is one number and one number ranks things. But it embeds a hidden assumption — that a miss and a false alarm cost the same — which is almost never true in medicine. Whenever you see an F1, ask for precision and recall separately, then ask which mistake you can actually afford. Note too that this paper's 91.9% is the *ceiling* under its own idealised test: when the authors fed the defence perfect inputs from a complete database, it scored an F1 of 99.3% across 100,000 claims. The gap between 99.3% and 85.7% is the cost of real-world extraction and an incomplete reference, not a flaw in the idea.

**3. When "no difference" is the finding — reading a negative result correctly.**
- *What it is:* Most of the time, a study that fails to find a difference has failed to answer its question, usually because it was too small. Occasionally, the failure to find a difference *is* the result, because the thing being tested is the detector itself.
- *How this paper used it:* Poisoned models scored the same as clean models across all five standard medical benchmarks, with no consistent relationship between score and poison dose. That null result is the paper's most consequential finding — more important than the attack itself.
- *The theory, with an analogy:* The logic works because the harm was independently established. Blinded doctors confirmed the poisoned models were producing more dangerous text. So when the benchmarks then report "these models are equivalent," the benchmarks are demonstrably wrong, not merely uninformative. It is a metal detector that stays silent while you carry a knife past it, after somebody has already confirmed you are carrying a knife. Contrast this with the negative results earlier on your list: the retinal-photograph model scoring 0.70 against a blood test's 0.72, or the imaging meta-analysis finding 87.0% against 86.4%. In those, nothing independent established that a difference existed, so "we could not tell them apart" was the correct and only conclusion. Here, the difference was established by other means first. That is what turns a null result from a shrug into an indictment.
- *Watch out:* Before accepting any "no difference found," ask what else you know. If the study is the only evidence, a null result usually means the study lacked the power to see a difference, and you should ask how big a difference it could have detected. If an independent measurement has already established the difference, a null result condemns the instrument. The same statistical shape means opposite things in those two situations, and the difference lies entirely outside the statistics.

# Jargon Translator

- **Large language model (LLM):** a system trained by predicting the next word across vast amounts of text, which lets it answer questions and write fluent prose.
- **Training data / pre-training dataset:** the pile of text a model learns from. The Pile, used here, holds about 400 billion words from 22 sources.
- **Token:** roughly a word or word-fragment, the unit these models count. 0.001% of 100 billion tokens is 1 million tokens.
- **Web scraping / Common Crawl:** automated copying of public web pages. The Common Crawl is a huge archive of them, and anyone can put a page on the web.
- **Data poisoning:** deliberately planting bad content where a future model will learn from it. The attacker never touches the model itself.
- **Attack surface:** the set of places a system can be got at. Here it is every unmoderated corner of the internet a crawler might visit.
- **Parameters:** a model's adjustable internal numbers. The models here had 1.3 and 4 billion; frontier systems have hundreds of times more.
- **Benchmark:** a fixed set of test questions used to compare systems — here MedQA, PubMedQA, MedMCQA, and two clinical sections of a broad exam called MMLU.
- **Blinded review:** judges do not know which condition produced what they are judging, so their expectations cannot tilt the result.
- **Control concept:** a medical topic deliberately left un-poisoned, so the same model can be compared against itself.
- **Knowledge graph:** a database of concepts linked by verified relationships — "metoprolol may treat heart failure" — that can be checked against mechanically.
- **Named entity recognition (NER):** automatically pulling the medical terms out of a block of text.
- **Retrieval-augmented generation (RAG):** giving a model trusted documents to consult while answering. One of the three fixes that failed here.
- **Fine-tuning:** extra training on a smaller, better dataset to correct a model's behaviour. Also failed here.
- **Hallucination:** a fluent, confident statement that is simply false.
- **Precision / recall / F1:** of what you flagged, how much was real; of what was real, how much you flagged; and the combined score that weights both equally.

# What You Can (and Can't) Say

**Fair to say:**
- "A 2025 Nature Medicine study showed that replacing 0.001% of a language model's training text with medical misinformation produced a model measurably more likely to generate harmful medical content, as judged by blinded physicians and medical students."
- "The attack on the larger model required 2,000 fake articles costing five dollars to generate, hidden as invisible text inside web pages."
- "The poisoned models scored the same as clean models on all five standard medical benchmarks — the tests used to certify these systems could not detect the damage."
- "Prompt engineering, retrieval from trusted sources, and fine-tuning all failed to fix a poisoned model."
- "A defence that checks claims against a fixed database of verified medical relationships caught 91.9% of harmful passages."
- "The researchers simulated the attack on their own systems and did not release the poisoned models, the malicious data, or the training code."

**Not fair to say:**
- "AI models have been poisoned with medical misinformation" — this was a controlled simulation. The authors hypothesise that incidental contamination already happens, and label that as a hypothesis.
- "Anyone can poison ChatGPT for five dollars" — five dollars covered generating the articles for a 4-billion-parameter model. The cost projections for frontier systems are arithmetic, not experiment, and a real attack also requires getting the content crawled.
- "Medical AI benchmarks are worthless" — they measure what they measure. The finding is narrower and more precise: they do not detect this kind of harm, so a good benchmark score is not a safety certificate.
- "The knowledge graph fixes the problem" — it catches most harmful passages after the fact, depends on a reference database that must be kept current, and its authors note that true statements can still be assembled into a false whole.
- "This proves AI is too dangerous for medicine" — the authors' own recommendation is narrower: do not use these models for diagnosis or treatment until better safeguards exist, and validate them the way medical devices are validated.

# Bottom Line for Your Life

Four days ago you read a paper showing that a few altered pixels could flip a medical image classifier while it reported total confidence. This is the same lesson arriving through a different door, and it is the more disturbing version, because the attack here needs no access to the system at all. Somebody posts fake medical pages, walks away, and waits for a crawler. The content sits there indefinitely, able to contaminate models that have not been built yet.

The genuinely useful takeaway is not about hackers. It is about what a test score certifies. These poisoned models passed the medical exams. Blinded doctors reading their actual output found more content that could hurt someone. Both things were true at once, measured on the same models on the same day, and only one of them would have shown up in a press release.

So when someone tells you a medical AI "scores at physician level," the question this paper teaches you to ask is: on what, and would that test have caught it if the model were quietly wrong? Here the answer was no — and the researchers only found out because they built the broken model themselves and asked humans to read it.

There is a smaller lesson worth keeping too. The three fixes everybody reaches for — better prompts, letting the model look things up, a bit of extra training — did nothing at all. Bad foundations are not repaired at the surface.

Nothing here changes anything about your own care. If you use a chatbot for health information, treat it as you would a confident stranger: worth hearing, worth checking, never the final word. One study is one data point. This is an educational breakdown, not medical advice.

---

**Sources** (based on articles retrieved from PubMed and PubMed Central; identifiers verified against the live PubMed/NLM record — URL browsing is blocked in this environment, so links are constructed from that verified record):
- DOI: https://doi.org/10.1038/s41591-024-03445-1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/39779928/ (PMID 39779928)
- Full text (PMC, open access): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11835729/

**Why this paper and not the earlier queue entries.** Three queue items ahead of this one cannot be read in full from this environment, and all three are short commentary or review pieces rather than studies. Each identifier below was verified against the live PubMed record:
- Beam AL, Kohane IS. "Big Data and Machine Learning in Health Care." *JAMA* 2018;319(13):1317–1318 — https://doi.org/10.1001/jama.2017.18391 (PMID 29532063). A Viewpoint. No PubMed Central record and no abstract in the PubMed record.
- Moor M, et al. "Foundation models for generalist medical artificial intelligence." *Nature* 2023;616(7956):259–265 — https://doi.org/10.1038/s41586-023-05881-4 (PMID 37045921). A Review. No PubMed Central record.
- Wu E, et al. "How medical AI devices are evaluated: limitations and recommendations from an analysis of FDA approvals." *Nature Medicine* 2021;27(4):582–584 — https://doi.org/10.1038/s41591-021-01312-x (PMID 33820998). A short correspondence piece. No PubMed Central record and no abstract in the PubMed record. Note that the queue previously listed this title slightly incorrectly; it has been corrected to match the NLM record.

The publisher and every third-party host are blocked by this environment's network policy, and the full-text service used for paywalled papers is at its monthly limit until 2026-10-01. All three remain unticked in the queue, to retry with a PDF or after that service resets. The remaining queue entry, Jiang LY et al., *Nature* 2023, does have an open-access copy (PMC10338337) and can be decoded on a future day.
