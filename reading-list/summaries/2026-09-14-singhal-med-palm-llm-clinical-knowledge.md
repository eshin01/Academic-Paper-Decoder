# Large language models encode clinical knowledge

- **Authors:** Karan Singhal, Shekoofeh Azizi, Tao Tu, S. Sara Mahdavi, Jason Wei, Hyung Won Chung, … Alan Karthikesalingam, Vivek Natarajan (Google Research, Mountain View; DeepMind, London; one author from the US National Library of Medicine) — 32 authors
- **Venue:** Nature, 2023;620(7972):172–180 (published July 12, 2023)
- **DOI link:** https://doi.org/10.1038/s41586-023-06291-2
- **PubMed link:** https://pubmed.ncbi.nlm.nih.gov/37438534/ (PMID 37438534)
- **Full-text link used:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10396962/ (PubMed Central, open access)
- **Publisher correction on record:** Nature 2023;620(7973):E19 — https://doi.org/10.1038/s41586-023-06455-0 (PMID 37500979, PMC10412443). Cosmetic detail not retrieved; noted for citation hygiene.
- **Basis:** FULL TEXT — main text, results, ablations, human evaluation results, discussion, limitations, fairness and ethics sections, and the complete Methods were read from the open-access PubMed Central copy. Figures, Extended Data tables, and the Supplementary Information were not retrieved, so numbers that live only in those places are flagged as not retrieved rather than guessed. Competing-interest and funding statements are pointed to by the article but were not present in the retrieved text; PubMed tags the work as non-US-government research support. Identifiers verified against the live PubMed/NLM record; direct URL browsing is blocked in this environment, so links are constructed from that verified record.
- **Decoded:** 2026-09-14
- **Note on queue order:** this paper was taken ahead of the queued Topol 2019 review, whose full text could not be obtained today. Details at the end.

---

# The Gist

Google set out to answer a question that had been floating around since ChatGPT arrived: does a general-purpose language model actually *know* medicine, or does it just sound like it does? They built a test set of seven collections of medical questions, ran a 540-billion-parameter model against it, and got a score of 67.6% on US medical licensing exam-style questions — beating the previous best system by more than 17 percentage points. Then they did the thing that makes this paper worth reading. Instead of stopping at the exam score, they had doctors read the model's long-form answers to ordinary health questions and rate them. That is where the exam score fell apart: clinicians judged only 61.9% of the model's answers to match scientific consensus, against 92.9% for answers doctors wrote themselves, and flagged 29.7% of them as possibly leading to harm. A modest extra tuning step, built from just 65 example answers, closed most of that gap. The paper's real contribution is the demonstration that a high exam score and a safe answer are two different things.

# Study Snapshot

- **Study type:** A benchmark and evaluation study of a computer system. No patients, no clinic, no deployment, no outcomes. It measures what a model writes, not what happens to anyone.
- **The models:** PaLM, a 540-billion-parameter language model trained on 780 billion words of web pages, Wikipedia, books, code, news, and social media, and its instruction-tuned version, Flan-PaLM. Sizes of 8, 62, and 540 billion parameters were compared. The largest used 6,144 specialised chips for training.
- **The benchmark:** MultiMedQA, seven question sets. Six already existed: MedQA (licensing-exam style, 1,273 test questions), MedMCQA (Indian medical entrance exams, 6,100 test questions drawn from a pool of over 194,000 covering 2,400 topics), PubMedQA (1,000 expert-labelled yes/no/maybe questions about research abstracts, split 500 for development and 500 for test), and six clinical subsets of a general knowledge exam called MMLU, plus two sets of real consumer questions, LiveQA and MedicationQA. The seventh, HealthSearchQA, was new: 3,173 health questions that real people actually type into a search engine.
- **Exam results:** 67.6% on the four-option licensing-exam questions, exceeding the prior best system's 50.3% by 17.3 percentage points, and 62.0% on the harder five-option version. 57.6% on the Indian entrance exams against a prior best of 52.9%. 79.0% on the research-abstract questions against a prior best of 78.2%. On the general exam's clinical subsets, 83.8% for professional medicine and 80.4% for clinical knowledge.
- **What made the scores go up:** size, mostly. Performance roughly doubled going from the 8-billion to the 540-billion model, with the largest beating the 62-billion version by more than 14 points and the 8-billion version by more than 24. Instruction tuning helped at every size. Asking the model to reason step by step did *not* help on these three datasets. Sampling 11 answers and taking the majority vote added more than 7 points on the licensing exam, but made the research-abstract score worse.
- **The human evaluation, which is the heart of the paper:** 140 consumer questions in total — 100 from HealthSearchQA, 20 from LiveQA, 20 from MedicationQA. Doctors wrote reference answers. A separate panel of 9 clinicians based in the USA, UK, and India rated all three sets of answers without being told which was which. **One clinician rated each answer.** Five lay raters, all based in India, judged helpfulness. Confidence intervals came from 1,000 bootstrap resamples.
- **What the doctors found.** Matching scientific consensus: clinicians 92.9%, the untuned model 61.9%, the tuned model 92.6%. Correct recall of medical knowledge: clinicians 97.8%, untuned 76.3%, tuned 95.4%. Possibly leading to harm: clinicians 5.7%, untuned 29.7%, tuned 5.9%. Containing biased content: clinicians 1.4%, untuned 7.9%, tuned 0.8%. Omitting important information: clinicians 11.1%, untuned 47.6%, tuned 15.3%.
- **One result went the wrong way, and they reported it.** Answers containing inappropriate or incorrect content: clinicians 1.4%, untuned model 16.1%, tuned model **18.7%** — worse after tuning. The authors explain it: tuning made answers longer and more complete, and a longer answer has more room to be wrong.
- **What the lay raters said:** answers judged helpful 60.6% of the time for the untuned model, 80.3% for the tuned one, 91.1% for the clinicians.
- **The tuning itself was tiny.** Med-PaLM was made by adding a learned prefix to the prompt, trained on just **65 example question-and-answer pairs** written by a panel of 5 clinicians. The underlying model was frozen.
- **Contamination check:** the authors looked for overlap between the test questions and the training corpus and report no overlap for the consumer questions and minimal overlap for the multiple-choice questions.
- **Funding / conflicts:** not present in the retrieved text; the article points readers to a separate statement. Nearly all authors worked for Google Research or DeepMind.

# How Strong Is This Evidence?

**Grade: 3/5 — a landmark for asking the right question, built on a human evaluation too small and too thinly rated to carry the headline it produced.**

Start with what deserves credit, because it is substantial and it is the reason this paper matters more than its score. The team could have published "540-billion-parameter model passes the medical licensing exam" and been cited ten thousand times. Instead they built an evaluation framework that asks whether an answer is *right*, whether it *omits* something important, whether acting on it could *hurt* someone, and whether it is *biased* — and they ran it, and it made their own model look bad. They reported the result that got worse after tuning. They checked whether the model had simply memorised the test. They devoted long sections to the limits of their own bias measurement and to why the harm scale they borrowed may not apply in this setting. That is a paper behaving well.

Now the problem. Every headline number from the human evaluation rests on **140 questions, each rated by exactly one person.** The authors say so plainly and list it as a limitation. With a single rater there is no way to separate "this answer is good" from "this rater thought so," and no reliability figure is reported because none can be. When the paper's central claim is that the tuned model reached 92.6% against clinicians' 92.9%, that gap is smaller than a single question on a 140-item test. The honest reading of "on par with clinicians" is that this study could not tell them apart on this axis, which is a real finding but a much weaker one.

Everything else compounds it: Google built the models, wrote the benchmark, chose the prompts, recruited the raters, and scored the results. The exam datasets reward a format — multiple choice, one preferred answer, a vignette already tidied up by an examiner — that the authors themselves identify as easier than real clinical work. English only. And not one patient was involved at any point.

# The Editor's Concerns

- **One rater per answer is the load-bearing weakness.** Nine clinicians rated 140 questions across three answer sources, one rating each. Medicine's own literature is clear that experts disagree with each other often — the Hannun arrhythmia paper on your list found cardiologists agreeing only 72.8% of the time. Without at least two raters on the same item, a percentage like 92.6% carries an unknown amount of one person's judgement inside it.
- **140 questions is a small denominator for precise-sounding percentages.** Reporting 92.6% versus 92.9% on 140 items implies a resolution the sample cannot deliver. The authors did compute bootstrap intervals, but the intervals themselves are not in the retrieved text, only the point estimates, so a reader cannot see how wide they are.
- **The consumer questions were not a random slice of anything.** 100 of the 140 came from HealthSearchQA, which the authors built from seed conditions and search-engine suggestions. That is a reasonable way to capture what people ask. It is not a sample of clinical need.
- **The lay evaluation had five raters, all in one country.** Judgements about whether a health answer is helpful depend heavily on health literacy, language, and health system. The authors raise exactly this point themselves.
- **The harm scale was borrowed and does not obviously fit.** The authors took a severity scale designed for analysing harms during actual healthcare delivery and applied it to hypothetical harms from reading an answer, and they say directly that its validity "cannot therefore be assumed to extend to our context." Take the harm percentages as structured opinion, not measurement.
- **The bias check asks one narrow question.** Raters were asked whether an answer contained information inapplicable to a particular demographic. The authors note most questions were framed neutrally, so there was little for a bias to attach to, and they devote a full section to why this is not an assessment of fairness or equity.
- **Exams are not the job.** Multiple-choice vignettes come pre-digested, with a generally agreed answer. Real medicine involves getting information out of a person who may not know what matters, and reaching a plan when no option is clearly right. The authors name this gap as an open problem.
- **"Emergent ability" is doing interpretive work.** The paper attributes the performance to an ability that appears with scale. That is a description of what was observed, not a mechanism, and it should not be read as an explanation.
- **The developer graded its own homework, at every stage.** Google supplied the model, the new dataset, the prompts, the exemplars, the rater panel, and the framework. The contamination check is Google's own. None of that is unusual, and the paper is more candid than most, but no independent party verified anything here.
- **What this study did well:** invented and published an evaluation framework that goes beyond accuracy; refined that framework through repeat assessments before using it; kept the exemplar questions separate from the evaluation questions; blinded raters to which answers came from a model; reported a result that got worse after their intervention and explained why; tested for memorisation of the test set; reported that step-by-step reasoning did not help and that majority voting hurt on one dataset, rather than quietly dropping those; released the new dataset publicly; and wrote limitations, fairness, and ethics sections that concede more than most papers of this prominence would.

# Statistics Spotlight

**1. Single-rater evaluation — and the reliability figure that cannot exist.**
- *What it is:* When the thing you are measuring is a judgement rather than a fact, the measurement has two sources of variation: the item being judged, and the person judging it. Reliability is how much of the score comes from the item rather than the judge. You can only estimate it if more than one judge rates the same item.
- *How this paper used it:* Nine clinicians rated answers to 140 questions, and the paper states that one clinician evaluated each answer. The authors did run repeat triple-rated assessments earlier, on 25 question-and-answer pairs per dataset with three clinicians, but that was to refine the wording of the rating instrument before the main evaluation, not to measure reliability during it. So no inter-rater reliability figure is reported for the headline numbers.
- *The theory, with a worked example:* Imagine grading 140 essays, each read by one teacher out of nine. Teacher A is generous, teacher B is harsh. If teacher A happens to get more of the model's essays and teacher B more of the humans', the model wins by luck of the draw, and nothing in the final percentage tells you that happened. Two teachers per essay would let you measure how much they disagree, and therefore how much of the gap is real. One teacher per essay makes that permanently unknowable. This is why the Hannun paper's 72.8% agreement figure was so useful: knowing that experts disagree on one strip in four tells you exactly how much to discount any single expert's verdict.
- *Watch out:* Human evaluation is having a moment, and it is a genuine improvement over exam scores. But "we asked doctors" is not a method; the method is how many doctors, rating how many items, how often the same item, and with what agreement. When a paper reports human ratings without a reliability figure, the percentages are real data and their precision is unknown. Ask first whether any item was rated twice.

**2. Turning a percentage back into a count — what 92.6% versus 92.9% is worth on 140 questions.**
- *What it is:* A percentage hides its denominator. The first move on any rate is to multiply it back out and see how many actual items the difference represents.
- *How this paper used it:* The human evaluation ran on 140 questions. Med-PaLM's answers matched scientific consensus 92.6% of the time, clinicians' 92.9%. The paper calls this "on par."
- *The theory, with a worked example:* 92.9% of 140 is about 130 questions; 92.6% is about 130 as well. The gap between those two percentages is roughly four tenths of one question. There is no such thing as four tenths of a question, so the difference is not measuring anything — one answer rated differently by one clinician would swing it either way, and might reverse it. Now contrast that with the comparison the study *can* support: 61.9% for the untuned model against 92.9% for clinicians is a gap of about 43 questions out of 140. That is far too big to be explained by rater noise, and it is the paper's genuinely solid finding. Same study, same raters, same 140 items — one comparison is decisive and the other is invisible.
- *Watch out:* The authors did the right statistical thing and computed bootstrap confidence intervals from 1,000 resamples, which is the proper tool for exactly this question. But the intervals are not in the running text, only in figures, so the reader is handed the point estimates and left to trust them. Whenever you meet two percentages presented as equivalent, multiply both by the sample size before believing the comparison. If the difference comes out smaller than one item, the study did not measure a difference — and "we could not tell them apart" is not the same claim as "they are the same."

**3. Benchmark ceilings and contamination — what an exam score can and cannot mean.**
- *What it is:* Two separate threats to any benchmark number. A ceiling means the test itself has a maximum achievable score below 100%, usually because its own answer key is imperfect. Contamination means the test questions were in the model's training data, so a high score partly measures memory.
- *How this paper used it:* Both, and honestly. On the research-abstract questions the model scored 79.0% against a prior best of 78.2% — an improvement of 0.8 points — and the authors immediately note that a single human rater scores 78.0% on the same task, meaning "there may be an inherent ceiling to the maximum possible performance." Separately, they checked overlap between test questions and the 780-billion-word training corpus, reporting no overlap for the consumer questions and minimal overlap for the multiple-choice ones.
- *The theory, with an analogy:* If a driving test is scored by an examiner who is right 78% of the time, then a perfect driver scores 78%, and the difference between a 78% driver and a 79% driver tells you about the examiner, not the drivers. Ceilings are why small gains on mature benchmarks are usually meaningless while large gains on fresh ones are not — which is exactly the pattern here: +0.8 points on the saturated dataset, +17.3 on the licensing exam. Contamination is the other half: a student who has seen the answer key scores well and has learned nothing, so somebody has to check whether the key leaked.
- *Watch out:* Benchmark scores measure performance on a benchmark. That sounds obvious and gets forgotten constantly, including in this paper's own reception — "passed the medical licensing exam" became the story, while the finding that the same model's advice was judged possibly harmful in 29.7% of cases did not. Also note that a contamination check is only as good as the matching method used, and here that method lives in supplementary material this analysis did not retrieve. Treat "no overlap found" as the authors' good-faith report, not as proof.

# Jargon Translator

- **Large language model (LLM):** a system trained to predict the next word across enormous amounts of text, which turns out to let it answer questions and write prose.
- **Parameters:** the model's adjustable internal numbers. 540 billion here. More parameters usually means more capacity, at higher cost.
- **Token:** roughly a word or word-fragment; the unit these models read and count. The training corpus was 780 billion of them.
- **Foundation model:** a large model trained once on general data and then adapted to many tasks, rather than built for one job.
- **Benchmark:** a fixed set of test questions used to compare systems.
- **MultiMedQA:** the seven-dataset medical benchmark assembled for this paper.
- **HealthSearchQA:** the paper's new dataset of 3,173 health questions real people search for.
- **USMLE:** the United States Medical Licensing Examination, which American doctors must pass.
- **Few-shot prompting:** showing the model a handful of worked examples in the prompt so it copies the pattern, without retraining it.
- **Chain-of-thought prompting:** asking the model to write out its reasoning step by step before answering.
- **Self-consistency:** sampling several answers and taking the most common one, like polling the model repeatedly.
- **Instruction tuning:** further training on many tasks phrased as instructions, so the model follows directions better.
- **Instruction prompt tuning:** the paper's cheap adaptation method — learn a small prefix to put in front of the prompt, leave the giant model itself untouched. Med-PaLM came from 65 examples this way.
- **Hallucination:** a fluent, confident statement that is simply false.
- **Scientific consensus:** what the prevailing clinical guidelines and expert agreement currently say. Note that it changes over time, a limitation the authors raise about their own measure.
- **Bootstrap:** re-drawing the sample at random thousands of times to see how much a result would wobble.

# What You Can (and Can't) Say

**Fair to say:**
- "In 2023, Google showed a general-purpose 540-billion-parameter language model scoring 67.6% on US licensing-exam-style medical questions, more than 17 points above the previous best system."
- "The same paper showed the exam score was misleading: doctors judged only 61.9% of that model's answers to real health questions as matching scientific consensus, against 92.9% for answers doctors wrote, and flagged 29.7% as possibly leading to harm."
- "A lightweight tuning step built from just 65 clinician-written examples closed most of that gap, bringing consensus agreement to 92.6% and potential harm to 5.9%."
- "Tuning made one thing worse: inappropriate or incorrect content rose from 16.1% to 18.7%, which the authors attribute to longer answers having more room to be wrong."
- "The paper's lasting contribution is the evaluation framework — judging answers on consensus, harm, omission, and bias rather than accuracy alone."

**Not fair to say:**
- "AI matched doctors" — on 140 questions rated by one clinician each, a gap of 0.3 percentage points is under half a question. The study could not tell them apart on that axis, which is not the same as showing they are equal. On helpfulness, judged by lay raters, the model clearly lost: 80.3% against 91.1%.
- "The AI passed the medical licensing exam" — it answered licensing-exam-*style* questions from a research dataset. It did not sit the exam, and 67.6% is not a stated pass.
- "This model is safe for medical advice" — nothing here was deployed, no patient was involved, and the authors devote a section to why it is not ready.
- "Med-PaLM is less biased than doctors" — 0.8% versus 1.4% on 140 neutrally framed questions is about one question's difference, on a bias measure the authors themselves call limited.
- "Bigger models are safer" — scale raised exam scores and did nothing for safety. The safety gains came from 65 hand-written examples, not from size.

# Bottom Line for Your Life

This is the paper where the medical AI field met large language models, and its most useful lesson is one it demonstrated against its own product. The exam score went up by seventeen points. The safety numbers, measured on the same model on the same day, were terrible until somebody added human-written examples by hand. Those two facts sit in the same paper, and only one of them travelled into the headlines.

That split is the thing to carry around. A system can be excellent at the format of a test and unsafe at the job the test was standing in for, and the gap between them is invisible unless someone deliberately goes looking. This team went looking, which is why we know.

For your own reading: when you see a model's medical exam score quoted, the follow-up question is what happened when someone read its actual answers. And when you see human ratings quoted back at you, ask how many questions and how many raters per question. Here it was 140 and one, stated openly by the authors, and it is the reason several of the paper's most quoted numbers cannot bear the weight put on them.

Practically, nothing here says a chatbot is a doctor, and this study never claimed it. Its own authors describe a long list of things that must be solved first. One study is one data point. This is an educational breakdown, not medical advice.

---

**Sources** (based on articles retrieved from PubMed and PubMed Central; identifiers verified against the live PubMed/NLM record — URL browsing is blocked in this environment, so links are constructed from that verified record):
- DOI: https://doi.org/10.1038/s41586-023-06291-2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/37438534/ (PMID 37438534)
- Full text (PMC, open access): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10396962/
- Publisher correction: https://doi.org/10.1038/s41586-023-06455-0 (PMID 37500979, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10412443/)

**Why this paper and not the queued one:** the queue's next entry was Topol EJ, "High-performance medicine: the convergence of human and artificial intelligence," Nature Medicine 2019 (PMID 30617339, https://doi.org/10.1038/s41591-018-0300-7), both identifiers verified against the live PubMed record. Its full text could not be obtained: it has no PubMed Central record, the publisher and every third-party host are blocked by this environment's network policy, and the full-text service used for paywalled papers has hit its monthly limit until 2026-10-01. Only the abstract was reachable. Because that article is a narrative review whose value is entirely in its body text, and because it contains no study design or statistics to teach from in the abstract alone, it was left unticked in the queue rather than decoded from an abstract. It should be retried with a PDF or after the full-text service resets.
