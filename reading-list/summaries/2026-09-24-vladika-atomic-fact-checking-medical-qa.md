# Can We Make a Medical AI Check Its Own Homework, One Sentence at a Time?

**Paper:** Improving Reliability and Explainability of Medical Question
Answering Through Atomic Fact-Checking in Retrieval-Augmented Large Language
Models: Creation and Validation Study
**Authors:** Vladika J, Domres A, Nguyen M, Moser R, Nano J, Busch F, Adams L,
Bressem KK, Bernhardt D, Combs SE, Borm K, Matthes F, Peeken JC
**Venue / Year:** Journal of Medical Internet Research, 2026;28:e92090
**DOI:** https://doi.org/10.2196/92090
**PubMed:** https://pubmed.ncbi.nlm.nih.gov/42770666/
**Full text used:** https://pmc.ncbi.nlm.nih.gov/articles/PMC13595421/
**Basis of this analysis:** FULL TEXT (PubMed Central open-access copy,
retrieved 2026-09-24). Numbered tables and the body text were read in full.
Figures 1–4 and the supplementary appendix (Tables S1–S12) were not
retrievable, so nothing in this summary depends on a figure value.
**Date decoded:** 2026-09-24
**Evidence grade:** 4/5

---

## 1. The Gist

Chatbots that answer medical questions make things up. The fix everyone uses is
to hand the chatbot a stack of official medical guidelines first and tell it to
answer from those — but it still makes things up, and when it cites a source
you often can't tell which sentence came from where.

This team from the Technical University of Munich tried something more
stubborn. After the chatbot writes its answer, they chop the answer into the
smallest possible standalone claims — they call these "atomic facts," things
like "Trastuzumab is indicated for HER2-positive breast cancer." Then they go
back to the guideline library and look up each claim *separately*, mark it TRUE
or FALSE, rewrite the FALSE ones, and paste the corrected claims back into a
final answer. They run that loop up to three times.

Two things come out of this. Answers get somewhat more accurate. And — maybe
more usefully — every single sentence in the final answer now has a specific
guideline passage attached to it, so a doctor can check the AI's work line by
line instead of trusting it as a block.

The gains are real but much smaller and much more uneven than the abstract
makes them sound.

---

## 2. Study Snapshot

| | |
|---|---|
| **Type of study** | Development and validation of a software method — not a clinical trial. Nobody was treated differently because of this system. |
| **What was tested** | An "atomic fact-checking" layer bolted onto a retrieval-augmented chatbot |
| **Core engine** | GPT-4o (gpt-4o-2024-11-20), temperature 0, for the main pipeline |
| **Knowledge base** | Curated prostate and breast cancer guideline documents, chopped into 512-token chunks (100-token overlap), embedded with S-PubMedBERT, stored in ChromaDB; 7 chunks retrieved per lookup |
| **Question sets (human-rated)** | 4 sets, **215 question-and-answer pairs total**: validation 50 (prostate), test 60 (30 prostate + 30 breast), real tumour board 40, independent external neurology set 65 |
| **Atomic facts produced** | 428 / 404 / 519 / 474 across those four sets; median 7 facts per answer (IQR 5–8.75) |
| **Automated benchmark** | AMEGA — 20 patient cases, 135 questions, 1337 pre-written scoring criteria |
| **Human raters** | Validation + tumour board: 1 medically trained scientist, supervised. Test set: 4 blinded physicians, majority vote, 5th blinded rater broke 2-vs-2 ties |
| **Models compared** | GPT-4o baseline vs 3 generalist/medical open-source pairs: Gemma 3 27B vs MedGemma 27B, Llama 3 70B vs OpenBioLLM 70B, Qwen 3 32B vs Qwen 3 Medical 32B |
| **Competing method** | self-refine (the model critiques and revises its own answer in one pass) |
| **Ethics** | IRB approved, TUM Munich, 2023-626_1 S-NP; patient data anonymised |
| **Code and data** | Question sets published in a GitHub repository; TRIPOD-LLM checklist filed |
| **Funding/conflicts** | Not stated in the text retrieved |

**Headline results as the paper reports them:** "up to a 50% overall answer
improvement and an 80% hallucination detection rate."

**The same results with the labels put back on:**

| Question set | Answers improved | Answers made worse | Had no false facts at all | Detection sensitivity |
|---|---|---|---|---|
| Validation (prostate) | 20% | 8% | 56% | 78% |
| **Test (held-out)** | **10%** | **0%** | 88.3% | 47% |
| Real tumour board | 50% | 7.5% | 20% | 46% |
| **External neurology** | **7.7%** | **3%** | 81.8% | 52% |

---

## 3. How Strong Is This Evidence? — Grade 4/5

**Why it earns a 4.** By the standards of this field, the methodology is
unusually disciplined, and most of the things reviewers normally have to demand
were done without being asked:

- They tuned the design on a **validation set** (prostate) and only then ran
  the frozen design on a **held-out test set** (breast) — and then on a
  **completely independent, externally published neurology question set** they
  did not write. That is the right order of operations, and it is how they can
  legitimately claim they didn't overfit.
- They tested it on **real anonymised tumour board cases** — messy,
  multi-factor, actual-patient questions, not guideline flashcards.
- Human rating of the test set used **four blinded physicians with majority
  voting** and a blinded fifth rater for ties. Most papers in this space use one
  unblinded author.
- They ran **ablations** (how many example prompts, how many chunks, looping on
  or off, ensembling on or off) and reported the settings that *didn't* help.
- They compared against a **named competing method** (self-refine) — and
  published the cases where the competitor won.
- They stated the **cost honestly**: the full pipeline burns roughly 10× the
  tokens of just answering the question.

**Why it isn't a 5.**

- The two headline numbers come from **two different models on two different
  datasets** and are presented in the abstract as if they describe one system.
- The hallucination percentages rest on **a handful of actual events** (see §4).
- One expert (JCP) wrote the prompts, wrote the few-shot examples, wrote both
  question sets, supervised the single-rater evaluations, and broke the
  four-rater ties. That is a lot of load on one person's judgement.
- **GPT-4o was used as the automatic judge of a benchmark that GPT-4o was also
  competing in.**
- Nothing here measures whether a clinician made a better decision. The outcome
  is text quality, judged by people and by other chatbots.
- No prospective registration is mentioned.

Grade it as: *a well-built, externally validated engineering study whose
abstract oversells it, and whose most important safety numbers are too small to
carry the weight placed on them.*

---

## 4. The Editor's Concerns

**a) The abstract's two headline numbers don't belong in the same sentence.**
"Up to a 50% overall answer improvement" is the **tumour board set, GPT-4o
pipeline**. "An 80% hallucination detection rate" is **MedGemma 27B on the
validation set** — a different model, a different dataset, a different table.
On the actual held-out test set, the improvement rate was **10%**. On the
independent neurology set, **7.7%**. A reader who only sees the abstract will
carry away a number five times larger than the one that generalised.

**b) The hallucination percentages are percentages of almost nothing.**
*(Derived below from the paper's own reported numbers — the paper does not
present these counts.)* The paper gives the number of atomic facts per set and
a "hallucination rate" as a percentage of facts:

| Set | Facts | Hallucination rate | ≈ Hallucinations present | Detection | ≈ Actually caught |
|---|---|---|---|---|---|
| Validation | 428 | 1% | ~4 | 50% | ~2 |
| Test | 404 | 2% | ~8 | 38% | ~3 |
| Tumour board | 519 | 1% | ~5 | 25% | ~1 |
| Neurology | 474 | **0%** | **~0** | **0%** | — |

So "50% hallucination detection" on the validation set is roughly **two facts
out of four**. Reclassify one single fact and that number swings 25 points. And
the neurology set's "0% hallucination detection" is a percentage with **zero in
the denominator** — it is not a failure, it is an undefined quantity printed as
if it were a score. These numbers should have carried confidence intervals, or
better, been reported as counts.

**c) The best "detector" leaves just as many errors behind — possibly more.**
This is the catch the paper's own framing hides. MedGemma's celebrated 80%
detection rate is 80% *of its own mistakes*, and it makes three times as many as
GPT-4o. Multiply rate by the fraction missed to get what actually survives into
the final answer:

| Model | Hallucination rate | Detection | Missed | **Residual error left in the answer** |
|---|---|---|---|---|
| **GPT-4o** | 1% | **50%** (worst) | 50% | **≈0.50%** (best) |
| Gemma 3 27B | 2% | 71% | 29% | ≈0.58% |
| **MedGemma 27B** | 3% | **80%** (best) | 20% | **≈0.60%** |
| Qwen 3 Medical 32B | 2% | 60% | 40% | ≈0.80% |
| Qwen 3 32B | 4% | 69% | 31% | ≈1.24% |
| Llama 3 70B | 6% | 52% | 48% | ≈2.88% |
| OpenBioLLM 70B | 11% | 50% | 50% | ≈5.50% |

*(Derived. The paper reports the rate and the detection percentage separately
and never multiplies them. Because the published rates are rounded to whole
percent, GPT-4o and MedGemma are statistically indistinguishable at the top —
which is exactly the point: the model with the **worst** detection score ties
the model with the **best** one on the thing that actually matters.)*

**d) A safety signal is sitting unremarked in Table 2.** The row "FP falsified
atoms" records how often, when the system wrongly flagged a *correct* fact as
false, the rewrite then made it wrong. For the main GPT-4o pipeline that was 0%,
0%, 17%, 0% across the four sets — acceptable. But for the open-source models
the paper recommends for on-site hospital deployment: **MedGemma 44%, Llama 3
70B 50%, Gemma 3 27B 30%.** In other words, the "corrector" running on-premises
would be breaking a true statement roughly half the times it misfires. The paper
recommends these models for local deployment without engaging with this row.

**e) Sensitivity is lowest exactly where the clinical stakes are highest.** On
the real tumour board cases, sensitivity was **46%** and hallucination detection
**25%**. The system misses most of the false claims in the most clinically
realistic setting. The paper reports the same dataset as its best result (50%
of answers improved), and both statements are true — but presenting only the
flattering one is a choice.

**f) The competing method beats it on the strongest models.** On AMEGA,
self-refine outperformed atomic fact-checking on GPT-4o (+2.9 vs +1.1) and
GPT-4o-mini (+1.7 vs +1.0). Fact-checking won on the smaller, weaker models
(Llama 3.2 3B: +4.4 vs +0.8). The honest reading is *"this helps weak models a
lot and strong models less than the simpler alternative"* — which is a fine and
interesting finding, and is not how the conclusion is written. The paper
attributes Gemini's poor showing to prompts optimised for GPT, but that excuse
applies equally to its own framework's prompts.

**g) The model-size correlation is probably a floor effect.** They report a
significant negative correlation between log model size and improvement
(Pearson −0.754, p = .03) and read it as "smaller models benefit more." But
smaller models *start lower*, and anything starting lower has more room to move.
That is regression to the mean, not a property of fact-checking (see §5). The
correlation also requires a parameter count for every model — and parameter
counts for GPT-4o, o1, and the Gemini models are not public. The text does not
state which models entered the regression or where those numbers came from.

**h) GPT-4o judged a contest GPT-4o entered.** The AMEGA auto-evaluation used
GPT-4o as the scorer; GPT-4o was also one of the systems being scored. The
rubric evaluation used GPT-4.1 as judge. Models are known to favour their own
output. This doesn't invalidate the within-model before/after comparison (the
same judge scores both), but it does undermine any *between-model* ranking
drawn from those scores.

**i) The AMEGA scale's maximum is never stated in the retrieved text.** Scores
move from around 16 to around 31. Whether +1.1 points is a large or trivial
move depends on a ceiling the reader is not given.

---

## 5. Statistics Spotlight

### Concept 1 — The kappa paradox: 85% agreement, κ = 0.16

The paper reports something that looks alarming and then explains it correctly,
which is worth walking through because you will meet it constantly.

Four blinded physicians rated the test set. **All four agreed in 85% of cases.**
Yet the inter-rater reliability statistics — Fleiss κ and Krippendorff α, both
generalisations of Cohen's kappa to more than two raters — came out at **0.16**,
which on the usual reading is "slight agreement," barely above random.

How can 85% agreement score as "barely above random"?

Because kappa doesn't measure agreement. It measures **agreement above what
chance alone would have produced**, and chance agreement depends on how lopsided
the labels are.

The formula is:

> κ = (observed agreement − expected-by-chance agreement) ÷ (1 − expected-by-chance agreement)

Work a simplified example. Suppose the AI's verdicts are correct 95% of the
time, so raters are writing "correct" on almost every item. Two raters who each
say "correct" 95% of the time will agree by pure luck:

- both say correct: 0.95 × 0.95 = 0.9025
- both say incorrect: 0.05 × 0.05 = 0.0025
- **expected by chance = 0.905**

Now suppose they actually agree 92% of the time. That's high! But:

> κ = (0.92 − 0.905) ÷ (1 − 0.905) = 0.015 ÷ 0.095 = **0.16**

Same number the paper got. Nothing is wrong with the raters. The denominator
`1 − 0.905 = 0.095` is tiny, so there was almost no headroom above chance to
claim, and every point of disagreement gets divided by a very small number.

**This is the kappa paradox**, and it has a name because it trips up so many
reviewers. High agreement + skewed prevalence = low kappa, always.

**So the paper's explanation is correct.** But here's the part they don't say,
and it matters: *the paradox cuts both ways.* Because agreement is concentrated
in the easy, abundant "correct" calls, kappa being uninformative means we **also
have no evidence that the raters agreed on the rare FALSE calls** — which are
the only ones the entire study is about. The 85% figure is dominated by items
nobody found difficult.

**What should have been reported instead:** positive specific agreement (PABAK,
or simply the agreement rate restricted to items where at least one rater said
"incorrect"). That number would tell you whether experts can reliably recognise
a false medical fact. It is not in the paper.

**Rule of thumb for you:** whenever you see a low kappa next to a high raw
agreement, don't conclude "the raters were unreliable." Check the prevalence
first. And whenever you see *only* a high raw agreement with no kappa, suspect
the opposite problem — the agreement may be entirely in the easy cases.

### Concept 2 — Detection rate vs residual error rate: always ask what's left

This is the single most transferable idea in today's paper, and it applies far
beyond AI.

"80% hallucination detection" sounds like a safety guarantee. It isn't, because
it's a **conditional** number: 80% *of the errors this particular system made*.
A system that makes many errors and catches most of them can easily be more
dangerous than one that makes few and catches half.

The quantity you actually care about is:

> **residual error rate = error rate × (1 − detection rate)**

Run it on this paper's numbers:

- **GPT-4o:** 1% error rate × 50% missed = **0.50% survives**
- **MedGemma 27B:** 3% error rate × 20% missed = **0.60% survives**

The model with the *worst* detection score comes out level with — arguably
ahead of — the model with the best one. The 80% headline is measuring how much
mess a model makes, as much as how well it cleans up.

This is the same structure as a cancer screening test. A test with 99%
sensitivity sounds superb; whether it saves lives depends on how many cancers
there are and what happens to the ones it misses. Sensitivity alone never
answers "how much danger is left?" — only the combination does.

**Where you'll use this:** any time something is sold to you on a *catch rate*,
a *detection rate*, a *removal rate*, or a *reduction*. Ask: reduction from
what baseline, and what's the absolute amount still there afterwards? A
"50% reduction in errors" from 2 errors to 1 is not the same purchase as 200 to
100, even though the percentage is identical.

### Concept 3 — Regression to the mean, and why "who improved most" is a trap

The paper finds that smaller models improve more from fact-checking (Pearson
correlation −0.754 between log parameter count and improvement, p = .03) and
reads it as evidence that the technique is especially valuable for small models.

Be suspicious of any analysis whose outcome is a **change score** (after minus
before) correlated against the **starting value**, because that correlation is
partly guaranteed by arithmetic, not by biology or engineering.

**Why it happens.** Every measurement = true value + noise. Whatever scored
unusually low on the first measurement got there partly through bad luck, and
bad luck doesn't repeat. Measure again and it drifts up toward the average —
*with no intervention at all*. Whatever scored unusually high drifts down. So
"low starters improve more" appears in data where absolutely nothing was done.

There's also a **floor-and-ceiling** version, which is clearly in play here: a
model already scoring 26.3 on AMEGA has less room to gain than one at 20.2,
whatever the benchmark's ceiling is. On this study's own test set, 88.3% of
answers contained **no false facts at all** — the paper says so explicitly, and
even names this as the reason the improvement rate was low. That is a ceiling
effect stated in plain sight, and the same logic applies across models.

**The classic real-world example:** the "sophomore slump." Athletes with
spectacular rookie seasons tend to do worse the following year. Commentators
invent psychological explanations — complacency, pressure, the weight of
expectation. The boring explanation is that a spectacular rookie season
requires both genuine talent *and* good luck, and only the talent comes back.
The same mechanism explains why the worst-performing hospitals "improve" after
any intervention you care to name, and why the sickest patients in an
observational cohort appear to benefit most from almost anything.

**How to tell a real effect from regression to the mean:** you need a control
group that also started low and got *nothing*. This paper has no such control —
there is no arm where small models were measured twice without fact-checking.
Without it, the −0.754 correlation is uninterpretable as a causal claim.

**A further warning on this specific number.** With roughly 8–16 models in the
regression, p = .03 is fragile. Correlations on samples that small swing wildly
— removing one or two models can flip a result like this. And a p-value near
.05 on n ≈ 10 is the textbook setup for a finding that doesn't replicate. Ask
for the confidence interval on the correlation; on that sample size it would be
alarmingly wide.

---

## 6. Jargon Translator

| Term | What it actually means |
|---|---|
| **LLM (large language model)** | The chatbot engine. Predicts plausible next words; it has no concept of "true." |
| **Hallucination** | The model states something false with total confidence. Here: wrong drug doses, two different procedures confused for one. |
| **RAG (retrieval-augmented generation)** | Before answering, look things up in a trusted document library and answer from what you found. Reduces invention; doesn't eliminate it. |
| **Atomic fact** | The smallest claim you can check on its own. "Trastuzumab is indicated for HER2-positive breast cancer." |
| **Chunk** | A slice of a source document (here, 512 tokens with 100 tokens of overlap so sentences aren't cut in half). |
| **Embedding / vector database** | Turning text into a list of numbers so "find me similar passages" becomes a geometry problem. Cosine similarity = the angle between two such lists. |
| **Few-shot / 4-shot prompting** | Showing the model 4 worked examples inside the instruction so it copies the pattern. |
| **Temperature 0** | Turn off randomness so the same question gives the same answer. Good for reproducibility. |
| **Sensitivity (recall)** | Of all the false facts that existed, what share did the system flag? |
| **Specificity** | Of all the true facts, what share did it correctly leave alone? |
| **Precision (PPV)** | Of everything it flagged as false, what share really was false? |
| **F-score** | One number balancing precision and sensitivity. Hides which one is weak — always look at both. |
| **Balanced accuracy** | Average of sensitivity and specificity. Used because plain accuracy is meaningless when 95% of items are one class. |
| **Fleiss κ / Krippendorff α** | Multi-rater agreement, corrected for chance. See §5. |
| **LLM-as-a-judge** | Using a chatbot to grade chatbots. Cheap and scalable; inherits the judge's biases. |
| **self-refine** | The comparison method: model writes, critiques itself, rewrites. One pass, no external lookup. |
| **Ablation study** | Remove one component at a time to see which parts actually do work. |
| **TRIPOD-LLM** | Reporting checklist for prediction/LLM studies. Filing one is a mark of good faith. |
| **MDR Class IIa** | A European Medical Device Regulation tier. Relevant because a guideline chatbot may legally count as a regulated medical device. |

---

## 7. What You Can (and Can't) Say

**Fair to say:**
- A Munich group built a system that breaks a medical chatbot's answer into
  individual claims, checks each against cancer guidelines, and rewrites the
  wrong ones.
- The main practical win is **traceability**: every sentence can be linked back
  to a specific guideline passage, correctly identified 75% of the time on the
  first try and 91.9% within the top three.
- On real tumour board cases, 50% of answers were judged improved — the best
  result, on the hardest and most realistic dataset.
- On a held-out test set, 10% of answers improved and **none got worse**.
- It was tested on an independent neurology question set the authors did not
  write, and performance held up — genuine evidence against overfitting.
- The technique helps weak, small models more than strong ones.
- It costs about **10× the tokens** of just answering the question.

**Not fair to say:**
- ~~"This AI catches 80% of hallucinations."~~ That figure is one model on one
  dataset. The same system caught 25% on the tumour board set.
- ~~"It improves medical answers by 50%."~~ That was the single best dataset. On
  the held-out test set it was 10%, on the independent neurology set 7.7%.
- ~~"Medical fine-tuned AI models are better at this."~~ The paper explicitly
  refutes this. Only MedGemma beat its generalist twin; OpenBioLLM was far
  *worse* than plain Llama 3 (sensitivity 33% vs 61%).
- ~~"This makes medical chatbots safe enough to use."~~ Nothing here measures a
  clinical decision or a patient outcome. The endpoint is text quality.
- ~~"The system fixes errors."~~ Sometimes it creates them. Answers got *worse*
  in 8%, 0%, 7.5%, and 3% of cases across the four sets — and when the
  open-source models misfired, they corrupted a true statement 30–50% of the
  time.
- ~~"It beats the alternatives."~~ The simpler self-refine method beat it on
  GPT-4o and GPT-4o-mini.

**The honest one-liner:** *a well-engineered transparency layer that makes a
medical chatbot's reasoning auditable sentence by sentence, with modest and
uneven accuracy gains, tested on too few actual errors to say how safe it is.*

---

## 8. Bottom Line for Your Life

**If someone shows you an AI medical answer with citations, this paper tells you
what to ask.** "Is that citation attached to the *whole answer* or to *this
specific sentence*?" Almost every product does the former. The difference is the
entire point of this study, and it's the difference between a bibliography and a
receipt.

**The transferable skill is the residual-error calculation.** Whenever a
percentage is offered as reassurance — a detection rate, a catch rate, a
reduction — multiply it out and ask what's left in absolute terms. Today's
paper is a clean demonstration: the model with an 80% detection rate leaves
just as much error in the final answer as the model with a 50% rate, because it
made three times as many errors to begin with. That arithmetic is three seconds
of work and it reverses the headline.

**And notice how the paper's own honesty gave us the tools to criticise it.**
The authors published the ablations that failed, the dataset where the
competitor won, the 10× cost, the per-set breakdowns, and the fact counts that
let anyone do the division in §4. Every criticism in this summary was built out
of numbers *they chose to print*. That is what distinguishes a good paper with
an oversold abstract from a bad paper — and it's why this grades a 4/5 rather
than a 2. Papers that hide their weak spots don't give you the means to find
them.

**Practically, for now:** don't trust a medical chatbot's answer because it has
sources. Trust it when you can check which source supports which sentence — and
then check one.

---

*Education, not medical advice. Decoded 2026-09-24 from the PubMed Central
open-access full text. All figures quoted come from the article body or Tables
1–4; derived calculations are labelled as such and were computed from the
paper's own reported values.*
