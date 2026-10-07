# Better Than What? The Comparator Is the Whole Story

**Paper:** An open vision-language model for diverse medical applications
**Authors:** Sellergren A, Kazemzadeh S, Mahvar F, Kiraly A, Traverse M,
Kohlberger T, … Steiner DF, Pilgrim R, Golden D, Yang L (Google Research and
Google DeepMind; 90 listed authors)
**Venue / Year:** Nature Medicine, published online 2026-10-06
**DOI:** https://doi.org/10.1038/s41591-026-04626-w
**PubMed:** https://pubmed.ncbi.nlm.nih.gov/42839104/
**Preprint read for detail:** MedGemma Technical Report, arXiv:2507.05201v4
(dated 6 April 2026) — https://arxiv.org/abs/2507.05201

**Basis of this analysis — read this carefully, because it is unusual.** This is
a **two-document** analysis and the two documents are not the same.

- The **Nature Medicine article** is the peer-reviewed publication. Its **abstract
  only** was available: the full text sits behind a paywall and nature.com is
  blocked by this environment's network policy. The abstract was retrieved from
  the live PubMed record and verified there on 2026-10-07.
- The **arXiv technical report** (v4) is the preprint from the same team. Its
  **full text, including the numeric result tables**, was read via the alphaXiv
  index on 2026-10-07, because arxiv.org itself is also blocked.

**Every number quoted below comes from the arXiv technical report, not from the
peer-reviewed Nature Medicine paper**, and is attributed as such. The two
abstracts agree exactly on the three headline figures (2.6–10%, 15.5–18.1%,
10.8%), which is good evidence the content substantially corresponds — but the
published version may differ in detail, and one difference between them is
flagged in the concerns section. The pages retrieved did not include the numeric
outcome of the radiologist reader study, the fine-tuning result tables, or the
MedSigLIP comparison tables; those are marked as not available where they come up.
**Date decoded:** 2026-10-07
**Evidence grade:** 3/5

Chosen today over the queue because it is the week's one genuinely significant
medical-AI paper: an open-weights medical foundation model family published in
Nature Medicine the previous day. The next three queue entries were checked
first and none was reachable — details at the end.

---

# The Gist

Google has released a family of open medical AI models and published them in
Nature Medicine. "Open" is the important word: you can download the weights, run
them on your own hardware, keep patient data inside your own hospital, and tune
them yourself. Almost every impressive medical AI result of the last few years
came from a model you can only rent through somebody else's web interface. This
one you can own.

There are two main models — a small one (4 billion parameters) that reads both
images and text, and a larger one (27 billion) tuned for text — plus a separate
image encoder called MedSigLIP. They handle chest X-rays, retinal photographs,
skin photographs and pathology slides, and they answer medical exam questions.

The headline claims, as the Nature Medicine abstract states them: for
out-of-distribution tasks, improvements of **2.6–10%** on medical image question
answering, **15.5–18.1%** on chest X-ray finding classification, and **10.8%** on
agentic evaluations — all "compared with the base models."

Those numbers are real. I checked every one against the technical report's
tables and they reconcile to the decimal point. But that last clause is doing
enormous work, and it is the reason this paper is worth decoding carefully.

**Every single headline figure is MedGemma measured against Gemma 3 — its own
untuned starting point.** Not against doctors. Not against the specialist
systems built for each task. Not against the best models available. The claim
being made is "medical training made our model better than our model was before
medical training," which is a true, useful engineering result, and is not the
claim a casual reader takes away.

Change the comparator and the picture moves a long way. On MedQA, the standard
US medical licensing exam benchmark, MedGemma 27B scores **87.7** — behind o3
(93.3), Gemini 2.5 Pro (92.6), Gemini 2.5 Flash (92.0) and DeepSeek R1 (90.1).
On MedXpertQA, the *one* text benchmark the authors certify as genuinely
out-of-distribution, MedGemma 27B gets **25.7** against o3's **54.6** — the
general-purpose model is better by a factor of **2.1**. On dermatology, Gemini
2.5 Pro (**81.0**) beats MedGemma (**71.8**). And on chest X-rays, MedGemma
comes in *below* the prior specialist system on three of four datasets.

There is also a single number in this paper that does more to explain how
medical AI benchmarks work than any explanation could. The same model, on the
same dataset, scoring the same five chest conditions, gets a macro F1 of **88.9**
under one labelling convention and **40.5** under another. Nothing about the model
changed. Only which cases were allowed to count, and how "uncertain" findings
were read.

None of this makes MedGemma a bad release. It is an unusually transparent
technical report — the authors flag their own contamination risk, their own
single unblinded reader, their own non-comparable physician baseline, and the
places where their bigger model is worse than their smaller one. The problem is
the gap between what was measured and what a headline will say was measured.

# Study Snapshot

- **Study type:** A model-development and benchmarking report. **Not** a clinical
  study. No patients were treated, no clinician was assisted, no outcome was
  measured. The authors say this plainly: "automated benchmarks represent only
  the first step towards validating real-world utility."
- **What was built (per the technical report):** MedGemma 4B (multimodal: images
  and text in, text out), MedGemma 27B (text-only; a 27B multimodal variant is
  released with preliminary evaluation only), and **MedSigLIP**, a 400M-parameter
  medical image encoder derived from SigLIP-400M. All built on Gemma 3, input
  images at 896×896, 128k context.
- **Training data (technical report Table 1):** text-only question sets
  (MedMCQA 182,806; MedQA 9,275; HealthSearchQA 3,375; AfriMed-QA 1,003;
  PubMedQA 1,000; LiveQA 634; MedExpQA 434) plus **~200,000 synthetic questions**
  generated by a larger teacher model; and images — internal histopathology
  **32,550,599** patch-caption pairs, MIMIC-CXR **231,483**, EyePACS **199,258**
  fundus images, CT slices 59,979, MRI slices 47,622, internal dermatology
  51,049, PMC 41,853, PAD-UFES-20 2,047, Digital Knee X-ray 1,469, VQA-RAD
  1,391, SLAKE 450.
- **The crucial overlap:** the training list includes the **train splits of
  MIMIC-CXR, SLAKE, VQA-RAD, EyePACS, and the internal dermatology and
  histopathology collections** — and the evaluation list includes **MIMIC-CXR,
  SLAKE, VQA-RAD, EyePACS, US-Derm MCQA and Path MCQA.** Different splits, same
  datasets, same institutions, same labelling conventions.
- **What the authors certify as out-of-distribution** (their Table 2 marks it
  explicitly): MedXpertQA (text, 2,450 items; and multimodal, 2,000),
  ChestX-ray14 (1,962), CheXpert (668), and AgentClinic-MIMIC (200). That is
  the honest list, and it is short.
- **Evaluation sets (technical report Table 2):** MedMCQA 4,183; MMLU Med 3,685;
  EyePACS 3,161; MedXpertQA text 2,450; CheXpert 668; MIMIC-CXR 1,532 (one
  convention) and 2,461 (another); VQA-RAD 2,248; US-Derm MCQA 1,996; CXR14
  1,962; MedQA 1,273; SLAKE 1,061; PubMedQA 500; **Path MCQA 450**; MIMIC-CXR
  report generation 306; AgentClinic-MedQA 215 and AgentClinic-MIMIC 200;
  AfriMed-QA closed questions **25**.
- **How the imaging tasks were posed:** as **multiple-choice questions**. The
  dermatology set has 136 real conditions, converted so that "the associated
  reference condition is included among three other randomly assigned condition
  labels" — a four-option question. Pathology: four to nine options. Diabetic
  retinopathy: five options.
- **Metrics:** accuracy, macro F1, tokenized F1, RadGraph F1. **No confidence
  intervals, standard errors, variance across seeds, or significance tests
  appear anywhere in the tables retrieved.** Every figure is a single point
  estimate.
- **Human comparison:** for chest X-ray report generation, **one** US
  board-certified cardiothoracic radiologist rated 306 cases on a five-point
  scale, and — in the authors' own words — "was **not blinded** to which report
  was from the original radiologist vs. from the AI system." The numeric result
  of this rating is not in the pages retrieved.
- **A known contamination fixed:** for VQA-RAD the authors used corrected splits
  "to avoid the train/test image contamination present in the original splits."
- **A comparison cell left empty:** "Evaluations on MIMIC-CXR were not performed
  with the OpenAI o3 model due to data privacy considerations."
- **A checkpoint chosen for style:** report generation used the **pretrained**
  rather than post-trained model, "due to the sensitivity to reporting style of
  metrics like RadGraph F1."
- **Compute:** the authors note a **500-fold** difference in computational cost
  between MedGemma 4B and the most expensive comparator.
- **Fairness / demographic subgroup analysis:** **none found in the text
  retrieved.** AfriMed-QA appears as a benchmark, but no performance breakdown by
  sex, age, ethnicity or skin tone is reported in the pages read.
- **Availability:** weights and tutorials at the URL given in the report.
- **Funding and competing interests:** not stated in the pages retrieved;
  all listed authors are affiliated with Google.

# How Strong Is This Evidence? — Grade 3/5

Three out of five means: a real and useful contribution, honestly reported, whose
evidence does not support the reading most people will take from it.

**What earns the points — and there is a lot.**

**The release itself is the contribution, and openness is a methodological
virtue, not just a commercial one.** A model you can download is a model you can
freeze, audit, version, run offline, and evaluate independently. The authors make
exactly this argument, and list the cases where MedGemma is preferable to an API
model: "a frozen model for documentation and reliability, sensitivity to training
or inference costs, ability to run locally or offline… or full control over
model adaptation." For medical use that is not marketing. A model that silently
changes under you cannot be validated.

**The 500-fold compute gap matters.** A 4B model that gets within shouting
distance of models costing 500× more to run is the difference between a tool a
hospital in a low-resource setting can deploy and one it cannot.

**They defined out-of-distribution explicitly and marked it in a table.** Their
Table 2 has an OOD column, with a footnote defining it as "data not seen during
any model development stages," and they state outright: "No data from MedXpertQA
was used in model training, so it is considered an out-of-distribution
benchmark." Most papers never tell you this. Here you can see precisely which
four of eighteen evaluation sets are clean.

**They raised test-set contamination against themselves.** From the discussion:
"we observed that performance on older, established benchmarks tended to improve
with newer models. While this observation reflects genuine advancements in model
capabilities, it also raises the possibility of **test data leakage**, as these
benchmarks are publicly available and frequently used in model development." An
author volunteering the leakage hypothesis for their own headline numbers is
rare.

**They disclosed the reader study's fatal flaw rather than hiding it.** One
radiologist, not blinded — stated in the methods, in plain words.

**They flagged that their physician comparison is not like-for-like.** The
AgentClinic table shows "Human physician 54.0" against MedGemma 27B's 56.2 — a
"model beats doctor" line waiting to happen. The footnote kills it: the human
number came from a run using a GPT-4 patient agent, while every model number was
recomputed with GPT-4o. Different simulated patient, different test. They could
have omitted that footnote.

**They reported the specialisation tax.** Medical tuning costs general ability:
MMLU Pro drops from 67.5 to 60.2 for the 27B.

**They reported that their bigger model is sometimes worse.** The preliminary
27B multimodal variant underperforms its own text-only sibling on five text
benchmarks (AfriMed-QA by 12.0 points) and the much smaller 4B on four
multimodal measures. Labelled preliminary, and published anyway.

**They fixed a contamination bug in a public benchmark** (VQA-RAD splits) and
said so, which makes their numbers *less* comparable to prior work and more
correct.

**What costs the points.**

**One: no uncertainty, anywhere.** Not one confidence interval, standard error,
seed variance or significance test in any table retrieved. The abstract's
smallest headline figure is a **2.6-point** improvement on a 2,450-item
benchmark. Whether that is signal is unknowable without an interval — and on a
2,450-item test the 95% interval on a single accuracy near 14% is roughly ±1.4
points, so the *difference* between two such accuracies carries an interval
around ±2 points. A 2.6-point gap sits right at that edge. It may be real. The
paper gives the reader no way to tell. For a venue like Nature Medicine this is
the single most surprising omission.

**Two: the comparator is the base model, and that is the weakest possible
comparison.** Every headline figure is MedGemma versus Gemma 3. That answers
"did our fine-tuning do anything?" It does not answer "is this good?" Against
the strongest comparators the paper itself tabulates: MedGemma 27B is below four
large models on MedQA, and at less than half of o3's accuracy on the only OOD
text benchmark. Against the prior specialist systems it claims to "approach," it
is below on three of four chest X-ray datasets.

**Three: most of the impressive numbers are in-distribution.** The headline
imaging results come from MIMIC-CXR, EyePACS, the internal dermatology set and
the internal histopathology set — all of whose training splits are in Table 1.
The EyePACS case is the clearest: 199,258 fundus images in training, and the
evaluation is EyePACS. MedGemma scores 64.9 where Gemini 2.5 Pro gets 27.7. That
gap is substantially "we trained on this dataset and they did not."

**Four: the comparators cannot do some of these tasks at all, which makes the
gap meaningless.** Diabetic retinopathy was posed as a five-option multiple
choice, so random guessing scores **20%**. Gemma 3 4B scored **14.4%** and Gemini
2.5 Flash **17.5%** — *below chance*. Gemma 3 27B scored 20.3%, i.e. exactly
chance. Beating a model that is performing at or below random guessing is not
evidence of clinical competence; it is evidence that the other models were not
attempting the task.

**Five: multiple-choice reformulation makes diagnosis much easier than
diagnosis.** 136 dermatological conditions became a four-option question with
three *randomly assigned* distractors. Random distractors are usually easy to
eliminate — a condition from a different body site, a different age group, a
different morphology. Real diagnosis has no options list and the competing
possibilities are the ones that actually look alike. The 71.8% on US-Derm MCQA
is a real measurement of a task that is not dermatology.

**Six: the only human comparison is one unblinded rater.** With a single reader
there is no inter-rater reliability to estimate, no way to separate the reader's
idiosyncrasy from the signal, and — because they knew which report was the AI's
— no protection against expectation. The authors disclose all of this; it remains
the case that the paper's one link to human performance rests on it.

**Seven: no fairness or subgroup evaluation in the text retrieved.** For a model
explicitly released for dermatology — where skin tone representation is a
documented, serious problem — and for a release aimed at global deployment, the
absence of any performance breakdown by patient demographics is a substantive
gap.

**Eight: the "multimodal question answering" label does not match the row the
numbers come from.** The 2.6–10% range reconciles exactly to the **text-only**
row of MedXpertQA. The multimodal row's one computable improvement is **+2.1**,
outside the stated range — and in that row the base Gemma 3 27B (29.8) *beats*
MedGemma 4B (24.4).

**Nine: the report-generation checkpoint was chosen because it matched the
reference style.** The authors explain that RadGraph F1 is style-sensitive and
the pretrained model "could better follow the style of MIMIC-CXR, as MIMIC-CXR
reports are used in training." That is candid, and it means the reported
RadGraph F1 is partly a measure of style imitation on text the model trained on.

# The Editor's Concerns

**Put confidence intervals on everything.** Benchmarks are samples. With n given
for every evaluation set in Table 2, binomial intervals are a few lines of code,
and bootstrap intervals barely more. Without them, a 2.6-point claim on the
paper's own OOD benchmark cannot be distinguished from noise, and a reader cannot
tell which of the dozens of differences in these tables are real. This is the
one change that would most improve the paper.

**Lead with the comparison that answers the clinical question.** "Better than our
own base model" belongs in an ablation table. The abstract of a Nature Medicine
paper should foreground how the model compares to (a) the best available model,
(b) the prior task-specific system, and (c) where a human baseline exists, a
properly matched one. All three comparisons exist in the report and all three are
less flattering.

**Report chance-level accuracy next to every multiple-choice result,** and flag
comparators scoring at or below it. A table in which three of four comparators
are at or under random guessing on diabetic retinopathy is not showing a
capability gap; it is showing that the task formulation defeated them. Say so.

**Report the free-response version of at least one imaging task.** Give the model
the image and ask for a diagnosis with no options. That number — whatever it is —
is the one that bears on clinical use, and its absence is the largest gap between
what was measured and what readers will infer.

**Reconcile the "2.6–10% on multimodal question answering" claim** with Table 4,
or relabel it as text-only.

**Repeat the reader study with multiple blinded radiologists** and report
inter-rater agreement. Three to five readers, blinded, with a kappa or
Krippendorff's alpha, would convert the weakest evidence in the paper into its
strongest. And publish the numeric result: it is not in the pages retrieved.

**Add a demographic performance breakdown,** at minimum by sex and age for every
task and by skin tone for dermatology. For an openly released model intended for
worldwide adaptation, this is not optional.

**Quantify the contamination risk the discussion raises.** The authors deserve
credit for naming it; the next step is an n-gram overlap or canary analysis
between the public benchmarks and the training mixture, reported as a number.

**Explain, prominently, the 88.9 versus 40.5 discrepancy.** The report gives both
MIMIC-CXR figures and explains the two conventions in the methods, but a
48.4-point swing on the same model and dataset deserves a sentence in the
discussion about which number a prospective user should plan around. (It is the
lower one.)

**Fill the empty o3 cell or explain its consequence.** Omitting the strongest
comparator on the flagship chest X-ray dataset for data-privacy reasons is
understandable; the effect is that MedGemma's best imaging result has no
strong-model comparison at all.

**State funding and competing interests.** Not present in the pages retrieved,
and every listed author works for the company releasing the model.

**One note in the paper's favour, found by comparing documents.** The arXiv
abstract claims fine-tuning "reduc[es] errors in electronic health record
information retrieval by 50% and reach[es] comparable performance to existing
specialized state-of-the-art methods." The Nature Medicine abstract replaces
this with the weaker and better-hedged "fine-tuning MedGemma can be more
effective than fine-tuning the base Gemma 3 model for medical tasks, particularly
in the setting of limited training data." Peer review appears to have softened a
specific quantitative claim into a qualified one. That is peer review working.

# Statistics Spotlight

Five ideas. The first is the most important thing in this summary, and the second
is the most useful trick.

## 1. "Improved by 15.5%" — improved over *what*?

Every number that compares two things carries a hidden argument about what the
right comparison is. In this paper the choice is explicit and consistent: the
abstract's three headline figures are all MedGemma against **Gemma 3**, its own
untuned starting point.

Here is what that does. I reconciled each figure against the technical report's
tables:

- **2.6%** = MedGemma 4B (14.2) minus Gemma 3 4B (11.6) on MedXpertQA text.
- **10.0%** = MedGemma 27B (25.7) minus Gemma 3 27B (15.7), same benchmark.
- **15.5%** = MedGemma 4B (48.1) minus Gemma 3 4B (32.6) on CheXpert.
- **18.1%** = MedGemma 4B (50.1) minus Gemma 3 4B (32.0) on ChestX-ray14.
- **10.8%** = MedGemma 27B (46.0) minus Gemma 3 27B (35.2) on AgentClinic-MIMIC.

All five reconcile exactly. All five answer the question *did medical training
help?* — a legitimate and well-posed engineering question.

Now swap in a different comparator from the same tables:

- **Versus the best available model.** MedXpertQA, the only OOD text benchmark:
  o3 scores **54.6**, MedGemma 27B **25.7**. The general-purpose model is better
  by a factor of **2.1**. On MedQA, MedGemma 27B's 87.7 sits below o3 (93.3),
  Gemini 2.5 Pro (92.6), Gemini 2.5 Flash (92.0) and DeepSeek R1 (90.1).
- **Versus the prior specialist.** Chest X-ray: below Med-Gemini on MIMIC-CXR
  (88.9 vs 90.7), below Med-PaLM M on the other MIMIC-CXR convention (40.5 vs
  51.6), below RadVLM on CheXpert (48.1 vs 49.0), above Med-Gemini on CXR14
  (50.1 vs 46.7). Below on three of four.
- **Versus a general model on dermatology.** Gemini 2.5 Pro **81.0**, MedGemma
  **71.8**. The medical model loses by 9.2 points on the medical task.

Same model, same tables, three completely different stories. None is a lie. The
one in the abstract is the one most favourable to the contribution.

**An everyday version.** A shop advertises "40% more vitamin C!" More than what?
More than last year's recipe — true, verifiable, and silent on whether it has
more than an orange, or than the competitor on the next shelf.

**Watch out for:** the words "compared with," "over," "relative to," "versus
baseline," or a bare percentage improvement. Find what the baseline *is*. If it
is a previous version of the same thing, you have learned about the developers'
progress, not about the product's standing. For medical AI specifically, there
are four comparators that matter and they are not interchangeable: the base
model, the best model, the task-specific specialist, and the clinician. A paper
that reports only the first has reported the least informative one.

## 2. You cannot read an accuracy until you know the chance rate

This is the single most useful trick for reading AI benchmark tables, and this
paper supplies a textbook demonstration.

The diabetic retinopathy task was posed as a multiple-choice question with five
options: none, mild, moderate, severe, proliferative. A model that understands
nothing and guesses at random scores **1 in 5 = 20%**.

Now read the column:

> MedGemma 4B **64.9%** · Gemini 2.5 Pro **27.7%** · Gemma 3 27B **20.3%** ·
> Gemini 2.5 Flash **17.5%** · Gemma 3 4B **14.4%**

Gemma 3 4B and Gemini 2.5 Flash are **below chance.** Gemma 3 27B is *exactly*
chance. Only Gemini 2.5 Pro is meaningfully above it, and barely.

So "MedGemma 64.9 versus Gemini 2.5 Pro 27.7" is not "our model beat a strong
competitor." It is "our model performed, and three of the four comparators did
not engage with the task at all" — possibly because they refused, hedged, or
produced unparseable answers. The gap says almost nothing about how MedGemma
would compare to a model that was actually trying, and nothing whatever about an
ophthalmologist.

Do the same for the other two: dermatology was four options, so chance is
**25%** — which makes Gemma 3 4B's 52.5% roughly twice chance and MedGemma's
71.8% a genuine but not transformative margin. Pathology was four to nine
options, so chance lies between **11.1%** and **25%**, and because the mix of
question types is not given, MedGemma's 69.8% cannot be converted into a clean
"how much better than guessing" figure at all.

**An everyday version.** "I got 25% on the multiple-choice exam" sounds poor.
If the exam had four options per question, you scored exactly what a sleeping
person scores. If it had a hundred options, you did extraordinarily well. The
raw percentage carries no information until you know the denominator of the
guess.

**Watch out for:** any accuracy figure on a multiple-choice task where the number
of options is not stated. Compute 100 ÷ (number of options) and subtract it
mentally before being impressed. And be actively suspicious of a *large* gap
where the losing side is near chance — that pattern usually means the task
formulation broke the comparator, not that the winner is strong. Note also that
this paper never states how many options MedXpertQA has, so its chance level
cannot be computed from the paper, which is why I have not claimed one.

## 3. The same model and the same data, scored 88.9 and 40.5

This is the most instructive single pair of numbers I have met in this reading
list.

MedGemma 4B, classifying the same five chest conditions — atelectasis,
cardiomegaly, consolidation, edema, pleural effusion — on the same dataset,
MIMIC-CXR:

> **Macro F1 88.9** on the "Med-Gemini test set": radiologist-adjudicated labels,
> with missing and uncertain labels **excluded**. n = 1,532.
> **Macro F1 40.5** on the "MAIRA test set": the dataset's original labels, with
> missing and uncertain treated as **negative**. n = 2,461.

A **48.4-point** gap. The first is **2.2 times** the second. Nothing about the
model changed between those two rows. What changed was two bookkeeping decisions.

**Why it moves so much.** Radiologists reading chest X-rays are often genuinely
unsure, and the original MIMIC-CXR labels were extracted automatically from
report text, so "uncertain" is common. The two conventions treat that
differently:

- *Exclude the uncertain cases.* You have removed the hard cases from the exam.
  What remains is the subset where expert radiologists agreed confidently — and a
  model finds those easier too, because they are the clear ones. You have also
  improved your labels, since the remaining ones were adjudicated by radiologists
  rather than scraped from text.
- *Call the uncertain cases negative.* You have kept every hard case **and**
  introduced label noise: findings that were probably present are now recorded as
  absent, so a model that correctly spots them is marked wrong.

The first convention makes the test easier and the labels cleaner. The second
makes it harder and the labels dirtier. Both effects push the same way, and
together they produce a 48-point swing.

**Which number should a hospital plan around?** The lower one, and probably lower
still. Real practice contains the uncertain cases; you cannot exclude the
patients you find confusing.

And the second concept hidden here: **macro F1**. F1 is the harmonic mean of
precision and recall for one condition; *macro* F1 averages across conditions
**equally**, regardless of how common each is. So a rare condition the model is
bad at drags the average down as hard as a common one it is good at. That is
often what you want clinically — you care about pneumothorax even though it is
uncommon — but it means macro F1 is not comparable across papers unless the
condition list is identical. Here it is five conditions for MIMIC-CXR and
CheXpert, and three different ones for CXR14, which is why 48.1 and 50.1 in
adjacent rows are not measuring the same thing.

**Watch out for:** two papers reporting different numbers on "the same benchmark."
Before concluding that one model is better, check the test-set size, how
uncertain and missing labels were handled, whether labels were adjudicated or
scraped, and exactly which conditions the macro average covers. This paper is
unusually good here — it reports both conventions and explains them — which is
precisely why the lesson is visible.

## 4. In-distribution, out-of-distribution, and why only four cells have a tick

A model is tested **in-distribution** when the test data resembles its training
data — same hospitals, same scanners, same labelling conventions, same question
style — even when the specific examples are held out. It is tested
**out-of-distribution** when the test data comes from somewhere the model has
never been.

Both are legitimate. They answer different questions. In-distribution testing
asks "did it learn the pattern?" Out-of-distribution testing asks "will it work
at my hospital?" Only the second is relevant to deployment, and it is almost
always the lower number.

Credit where it is due: this paper puts an explicit **OOD column** in its
evaluation table, defines it as "data not seen during any model development
stages," and ticks only four of eighteen evaluation sets — MedXpertQA, CheXpert,
ChestX-ray14 and AgentClinic-MIMIC. Everything else, including every headline
imaging result on MIMIC-CXR, EyePACS, dermatology and pathology, is
in-distribution. You can verify this yourself by reading the training table next
to the evaluation table: EyePACS appears in both, with 199,258 fundus images on
the training side.

And look at what happens on the clean benchmarks. MedXpertQA, OOD: MedGemma 27B
**25.7**. MedQA, in-distribution (its train split is in the training mixture):
MedGemma 27B **87.7**. That is not entirely a contamination effect — MedXpertQA
is designed to be harder — but the ordering is the one you should expect, and it
is the honest ceiling.

**The contamination problem on top of this.** The authors raise it themselves:
public benchmarks "are publicly available and frequently used in model
development," so a model trained on a broad web crawl may have absorbed the test
questions and their answers without anyone intending it. They note that scores on
old benchmarks keep rising and say this "raises the possibility of test data
leakage." That is a scientist arguing against their own result, and it should
raise your confidence in everything else they report.

**An everyday version.** Two driving tests. In the first, you practise on the
examiner's exact route for a month. In the second, you are driven to an unfamiliar
town. Passing the first proves you learned the route. Only the second tells you
whether you can drive.

**Watch out for:** papers that report only in-distribution performance, or that do
not tell you which is which. Compare the training dataset list against the
evaluation dataset list yourself — it takes a minute and it is usually decisive.
If a dataset appears on both sides, the number is about learning, not about
generalising.

## 5. One rater, unblinded, is not a reliability estimate

The only place this paper touches human performance is the chest X-ray report
evaluation: **one** US board-certified cardiothoracic radiologist rated 306 cases
on a five-point scale comparing MedGemma's report with the original radiologist's.

Two things are wrong with that, and the authors state both.

**It was unblinded.** The reader knew which report came from the AI. The methods
say they were "asked to remain neutral" but "were not blinded." Asking someone to
be unbiased is not a method; blinding is. Expectation effects in this setting run
in both directions — scepticism of machine output, or enthusiasm for it — and
neither can be measured after the fact.

**There was one of them.** This is the subtler point. With a single rater you
cannot compute **inter-rater reliability** at all, because reliability is a
property of *agreement between* raters. So there is no way to know whether this
radiologist's five-point judgements reflect something another radiologist would
reproduce, or this individual's particular standards. Radiologists disagree with
each other substantially on chest X-rays — that disagreement is the reason the
MIMIC-CXR labels needed adjudication in the first place, and the reason the two
label conventions in idea 3 differ so much. A single reader gives you one draw
from that distribution of opinion and no estimate of its spread.

The fix is standard and cheap: three to five readers, blinded, with agreement
reported as Cohen's or Fleiss' kappa, or Krippendorff's alpha for ordinal
ratings. This list has met these measures before, and their whole purpose is to
answer "would someone else have said the same thing?"

**An everyday version.** You want to know if a restaurant is good, so you ask one
friend who already knows you are thinking of investing in it. Their answer may be
right. It is one person's taste, and they knew what you wanted to hear.

**Watch out for:** any "expert evaluation," "reader study," or "clinician review"
in an AI paper. Ask three questions. How many readers? Were they blinded to which
output was the model's? Is agreement between them reported? If the answers are
one, no, and no, the human comparison is an anecdote with a number attached — and
note that in this paper even that number is not in the pages I could retrieve.

# Jargon Translator

- **Foundation model** — a large model trained broadly, then adapted to specific
  tasks with comparatively little extra data.
- **Vision-language model (VLM) / large multimodal model (LMM)** — a model that
  takes images and text together and produces text.
- **Open weights** — the model's parameters can be downloaded and run on your own
  hardware. Distinct from open *source* and from an API you rent.
- **Parameters (4B, 27B)** — the number of learned numbers in the model. More
  generally means more capable and more expensive to run.
- **Gemma 3 / SigLIP** — the general-purpose language model and image encoder that
  MedGemma and MedSigLIP were built from. Here they are also the *baselines*.
- **Image encoder** — the component that turns a picture into numbers the language
  model can use. MedSigLIP is this part, released separately.
- **Fine-tuning** — further training of an existing model on a specific task.
- **Distillation** — training a smaller model to copy a larger "teacher" model's
  outputs.
- **Reinforcement learning (RL) / supervised fine-tuning (SFT)** — two ways of
  adapting a model; SFT imitates correct answers, RL optimises against a reward.
- **Zero-shot** — asked to do a task with no examples provided in the prompt.
- **Linear probe** — freezing the model and training only a simple classifier on
  top of its outputs. Usually stronger than zero-shot, and a different kind of
  claim.
- **In-distribution / out-of-distribution (OOD)** — test data that does or does
  not resemble the training data. Only OOD performance predicts deployment.
- **Test-set contamination / data leakage** — the test answers reached the model
  during training, usually by accident.
- **Accuracy** — fraction of questions answered correctly. Meaningless without the
  chance rate.
- **Chance rate / chance level** — what random guessing scores. 100 ÷ number of
  options.
- **F1 score** — the harmonic mean of precision and recall for one category.
- **Macro F1** — F1 averaged equally across categories, so rare ones count as much
  as common ones. Not comparable across papers unless the category list matches.
- **Tokenized F1** — word-overlap F1 between a generated answer and the reference;
  used for free-text question answering.
- **RadGraph F1** — compares the clinical entities and relations in a generated
  radiology report against the real one. Sensitive to writing style, not only
  content.
- **MedQA / MedMCQA / PubMedQA / MMLU / AfriMed-QA** — medical exam and
  question-answering benchmarks (US licensing style, Indian entrance exams,
  PubMed abstracts, general knowledge subsets, pan-African multi-specialty).
- **MedXpertQA** — a deliberately harder expert-level benchmark; the one text set
  the authors certify as out-of-distribution here.
- **MIMIC-CXR / CheXpert / ChestX-ray14** — large public chest X-ray datasets with
  labels.
- **EyePACS** — a large retinal photograph dataset with diabetic retinopathy
  grades.
- **SLAKE / VQA-RAD** — medical visual question-answering datasets.
- **AgentClinic** — a simulated clinic where a model must take a history, order
  tests and reach a diagnosis, talking to a simulated patient.
- **Pneumothorax** — collapsed lung. **Atelectasis** — partial lung collapse.
  **Cardiomegaly** — enlarged heart. **Consolidation / edema / pleural effusion** —
  lung filled with fluid or inflammatory material, and fluid around the lung.
- **Whole slide image / patch** — a digitised pathology slide, and a small square
  cut from it.
- **Hounsfield windowing** — choosing a brightness range to make particular
  tissues visible on CT. This paper encodes three windows as colour channels.
- **Blinding** — concealing from an assessor which output came from which source.
- **Inter-rater reliability** — how much independent raters agree. Requires more
  than one rater.
- **Kappa / Krippendorff's alpha** — measures of rater agreement corrected for
  agreement expected by chance.
- **Benchmark saturation** — when scores approach the ceiling, so the benchmark can
  no longer distinguish better models.
- **Test-time scaling** — letting a model spend more computation per question at
  answer time. Noted in this paper's MedQA row for the 27B model, which means that
  figure is not strictly like-for-like with rows that did not use it.

# What You Can (and Can't) Say

**You can say:** Google has released open-weight medical vision-language models
(MedGemma 4B and 27B, plus the MedSigLIP image encoder) and published them in
Nature Medicine, and that medical tuning improved them over their own base
Gemma 3 models across every benchmark tested — by 2.6–10% on out-of-distribution
medical question answering, 15.5–18.1% on out-of-distribution chest X-ray
classification, and 10.8% on an out-of-distribution agentic evaluation.

**You can say** that a 4B model reaching this level matters practically, because
the authors report a 500-fold compute difference against the most expensive
comparator, and because open weights can be run locally, frozen for audit, and
adapted without sending patient data anywhere.

**You can say** the reporting is unusually candid: the authors mark which
benchmarks are out-of-distribution, raise test-set leakage against their own
results, disclose that their one reader was unblinded, flag that their physician
baseline used a different simulated patient, and publish results where their
larger model is worse than their smaller one.

**You cannot say** MedGemma is the best medical AI model. On the authors' own
tables it is below o3 and the Gemini 2.5 models on MedQA, at less than half of
o3's accuracy on the only out-of-distribution text benchmark, below Gemini 2.5
Pro on dermatology, and below the prior specialist system on three of four chest
X-ray datasets.

**You cannot say** these results show the model can diagnose. The imaging tasks
were multiple-choice questions with three randomly assigned distractors — 136
skin conditions compressed to four options. No free-response diagnostic
evaluation is reported.

**You cannot say** it beats doctors. The one physician figure in the paper
(AgentClinic 54.0) was measured against a different simulated patient than every
model figure, as the authors' own footnote states.

**You cannot treat** the imaging numbers as evidence of generalisation. The
training data includes the train splits of MIMIC-CXR, EyePACS, SLAKE, VQA-RAD and
the internal dermatology and pathology collections; the evaluations are on those
same datasets. Four of eighteen evaluation sets are marked out-of-distribution.

**You cannot read** the 64.9% on diabetic retinopathy as "much better than
general models." Three of the four comparators scored at or below the 20% chance
rate for a five-option question.

**You cannot compare** the 88.9 MIMIC-CXR figure with numbers from other papers
without checking the label convention. The same model on the same dataset scores
40.5 under the other one.

**You cannot conclude** anything about whether the model works equally well
across patient groups. No demographic or fairness subgroup analysis appears in
the text retrieved — including for dermatology, where skin tone representation is
a known problem.

**You cannot assume** any of this transfers to patient benefit. No patient was
treated, no clinician was assisted, no outcome was measured. The authors say so:
"automated benchmarks represent only the first step towards validating real-world
utility."

**You should note** that this summary rests on the Nature Medicine abstract plus
the arXiv technical report, because the peer-reviewed full text is paywalled and
unreachable here. The two abstracts agree on the headline figures, but one claim
was demonstrably softened between them.

# Bottom Line for Your Life

Nothing here reaches a patient yet, and the authors do not claim it does. So the
useful thing is a way of reading the next headline, because there will be one
within a week, and it will say some version of "AI matches doctors."

**Ask three questions, in this order.**

**Better than what?** This is the one that does the most work. The impressive
figures in this paper are all "better than our own untuned model." That is a real
engineering result and it is not a clinical one. When you see a percentage
improvement, find the baseline. If it is the developers' previous version, you
have learned that they made progress. If it is a doctor, ask the next two
questions.

**What was the test, exactly?** "Diagnosed skin conditions with 72% accuracy"
sounds like diagnosis. Here it was a four-option multiple-choice question built
from 136 conditions, with three of the four options picked at random. Your
dermatologist does not get options. Neither does your radiologist. A model that
can pick the right answer from a short list has not demonstrated it can produce
the right answer from a blank page — and this paper reports no test of the
latter.

**How many options, and did anyone check the chance rate?** The clearest
demonstration in this whole paper is that three of four comparison models scored
at or below random guessing on a five-option eye question. If a comparison looks
lopsided, suspect the test before you credit the winner.

For your own care, two things follow. First, be cautious with any medical AI
result reported only against other AI — it tells you about a race between
models, not about whether anything helps patients. Second, the thing in this
paper that is most likely to reach you eventually is not the diagnosis: it is the
mundane work the authors list as the real use cases — pulling key facts out of
clinical notes, matching patients to clinical trials, retrieving similar past
cases, and rewriting findings in language patients can understand. That last one
is the kind of thing worth asking for. If you get a report you cannot read, it is
reasonable to ask for it in plain words.

And if someone offers you a diagnosis from an AI tool, the question is the same
one this paper cannot answer: has it been tested on patients like me, at a place
like this, against what a doctor would have done — and did the patients do better?

**This is education about how to read a study, not medical advice. Decisions
about your care belong with you and your clinicians.**

---

*Decoded 2026-10-07. Sources: the Nature Medicine record and abstract via PubMed,
accessed and verified 2026-10-07; the MedGemma Technical Report (arXiv:2507.05201v4,
6 April 2026) read via the alphaXiv index, because both nature.com and arxiv.org
are blocked by this environment's network policy and the Nature Medicine full
text is in any case paywalled. **All numeric values quoted above are from the
arXiv technical report, not from the peer-reviewed Nature Medicine article.** Not
available in the pages retrieved: the numeric outcome of the radiologist reader
study, the fine-tuning result tables, the MedSigLIP comparison tables, any
funding or competing-interest statement, and any demographic or fairness subgroup
analysis. Derived figures — the reconciliation of all five headline improvement
percentages against Tables 4, 7 and 11; the 2.1x and 3.85x o3 ratios; the 48.4-point
and 2.20x MIMIC-CXR label-convention gap; the 20%, 25% and 11.1-25% chance rates
and the identification of three comparators at or below chance on EyePACS; the
MedGemma-versus-specialist differences on four chest X-ray datasets; the
specialisation-tax percentages; and the Appendix A14 comparisons showing the 27B
multimodal variant underperforming both its text-only sibling and the 4B model —
were computed from the report's own tabulated numbers and are labelled as derived
wherever they appear. The number of answer options in MedXpertQA is not stated in
the text retrieved, so no chance level is claimed for it.*

**Verified source links**
- DOI (Nature Medicine): https://doi.org/10.1038/s41591-026-04626-w
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42839104/
- Preprint read for detail: https://arxiv.org/abs/2507.05201 (arXiv:2507.05201v4)
- Nature Medicine full text: **paywalled and not retrieved**; no PubMed Central
  copy exists as of 2026-10-07.
