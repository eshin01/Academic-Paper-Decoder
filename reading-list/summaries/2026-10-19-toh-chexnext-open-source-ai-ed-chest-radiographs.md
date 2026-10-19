# Diagnostic performance of an open-source artificial intelligence model for detecting chest infections on after-hours emergency department chest radiographs in Singapore

**Authors:** Toh YJ, Tan SYY, Eng CW, Lee BK, M Yogendra P, Tan MO (6 authors, all Department of Radiology, Sengkang General Hospital, Singapore)
**Journal:** BMJ Health & Care Informatics, 2026; 33(1) (published 13 October 2026)
**Decoded:** 2026-10-19
**Analysis basis:** **FULL TEXT** (retrieved from PubMed Central, PMC13663711). Figures and the online supplementary material — which include the ROC curves, the study flowchart and the detailed confusion matrices — were not viewable, so anything living only there is marked as not retrieved.

**Source links (verified):**
- DOI: https://doi.org/10.1136/bmjhci-2025-101958
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42869615/
- Full text (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC13663711/

**Basis of link verification.** Direct URL fetching was blocked from this session (`doi.org` does not resolve through the network policy here). Verification was therefore done against the live PubMed/NLM record, which the daily routine permits and which is the stronger check in any case: a PubMed query for PMID 42869615 returned this exact title, these six authors, this journal, volume 33 issue 1, DOI `10.1136/bmjhci-2025-101958` and PMC ID `PMC13663711`; the full text was then retrieved from PubMed Central by that PMC ID and its content matches the record. Both halves of the chain were confirmed independently.

**Funding and competing interests: not reported in the text provided.** The PMC rendering carries no funding, competing-interests or data-availability statement. The analysis was run on the CARPL.AI orchestration platform (a commercial product); whether that was a paid, free or sponsored arrangement is not stated.

**Ethics:** an institutional review board waiver applied. The waiver's terms meant **no patient history or study indication was extracted at all** — a fact with consequences discussed below.

---

## 1. The Gist

A hospital in Singapore took 1,006 chest X-rays shot in its emergency department outside office hours, and fed them to a free AI anyone can download. They then compared what the AI said against what their own radiologists had written in the official reports.

Out of the box, using the settings the AI's creators published, the thing barely worked. It spotted 234 out of every 1,000 cases of consolidation (a patch of lung filled with fluid or pus instead of air) and 176 out of every 1,000 cases of pneumonia. Put plainly: it missed roughly four out of five.

Then the authors did something simple. They left the AI completely untouched and just moved the dial — the cut-off score at which the AI is allowed to say "yes, this one". Sensitivity for consolidation jumped from 23% to 89%.

The AI did not get better. Nothing about it changed. **The number that decides when a score counts as a "yes" was simply wrong for this hospital** — and that is the whole finding, and it is a genuinely useful one. The catch is in the second half: the authors picked the new dial setting using the very same 1,006 X-rays they then used to report how well it worked, so the improved figures have never been tested on a patient the dial has not already seen.

## 2. Study Snapshot

**Study type:** a retrospective, single-centre **diagnostic accuracy study** — a study that runs a test on a batch of existing cases and compares its answers against some agreed "truth". On the evidence ladder this sits in the cross-sectional band: below cohort studies, well below randomised trials. It can tell you how often the test agrees with the reference. It cannot tell you whether using the test changes anything that happens to a patient.

**Number of images (n):** **1,006** frontal chest radiographs from adult patients.

**Who they were:** adults presenting to the emergency department of **Sengkang General Hospital, Singapore**, during after-hours only — before 08:30 or after 17:30 on a weekday, or any time at weekends — across one month, **1 to 30 October 2024**. Children were excluded (paediatric radiology differs), as were non-frontal views (the AI was not trained on them).

**And here is the thing: no patient characteristics are reported. None.** Not age, not sex, not symptoms, not comorbidity, not the reason the X-ray was ordered. The IRB waiver forbade extracting any of it. So we know these were adults in one Singapore emergency department after hours, and nothing else about them.

**What was tested:** **CheXNeXt**, a free, open-source convolutional neural network (a type of image-recognition AI) built by the Stanford Machine Learning Group. It was trained on **ChestX-ray14** — 112,120 frontal chest X-rays from 30,805 patients — and detects 14 thoracic findings. This study used three of them: **consolidation, pneumonia and pleural effusion** (fluid in the space around the lung). The model outputs a probability from 0% to 100% for each. It was run through the CARPL.AI orchestration platform on locally stored, anonymised DICOM images.

**The cut-offs used first:** the ones **published by Stanford** — 0.744 for consolidation, 0.831 for pneumonia, 0.731 for effusion. These had been chosen to maximise the F1 score on Stanford's own tuning data during development.

**The comparator ("truth"):** the hospital's **official radiology reports**, written inside normal clinical workflow by **20 board-certified radiologists** (mean 13 years' experience, range 5–25 years), all Fellows of the Royal College of Radiologists, all blinded to the AI. A **single senior radiology trainee** then read those reports and extracted whether each mentioned consolidation, pneumonia or effusion. **No second extractor, no interobserver agreement check, no microbiology, no pathology, no clinical follow-up.** "Pulmonary infection" was defined simply as the presence of those radiographic findings — the authors call this a surrogate and say plainly it was chosen to reflect real-world practice.

**Main outcome:** sensitivity, specificity, PPV, NPV, AUC, F1 score and Youden index for each of the three findings, with 95% confidence intervals from 1,000 bootstrap resamples. STARD reporting checklist followed.

**Duration:** one month of image collection; the AI analysis was a one-off batch. No patients were followed, no care was changed.

**Funding / conflicts of interest:** **not reported in the text provided.**

### The results, at the published cut-offs

- **Consolidation** — sensitivity 0.234 (0.176–0.299), specificity 0.990 (0.983–0.996), PPV 0.846 (0.744–0.941), NPV 0.849 (0.825–0.871), AUC 0.900 (0.875–0.923), F1 0.367.
- **Pneumonia** — sensitivity 0.176 (0.124–0.233), specificity 0.995 (0.989–0.999), PPV 0.889 (0.778–0.974), NPV 0.845 (0.823–0.867), AUC 0.856 (0.824–0.887), F1 0.294.
- **Pleural effusion** — sensitivity 0.622 (0.548–0.704), specificity 0.949 (0.934–0.963), PPV 0.656 (0.574–0.738), NPV 0.942 (0.927–0.957), AUC 0.916 (0.887–0.940), F1 0.639.

### After moving the dial (Youden-optimised cut-offs)

- **Consolidation**, cut-off 0.11 — sensitivity **0.894**, specificity **0.765**, PPV **0.467**.
- **Pneumonia**, cut-off 0.31 — sensitivity **0.681**, specificity **0.881**, PPV **0.559**.
- **Pleural effusion**, cut-off 0.42 — sensitivity **0.852**, specificity **0.848**, PPV **0.466**.

The AUC is identical in all three tables — 0.900, 0.856, 0.916 — because moving a cut-off cannot change a model's ranking ability. That consistency is a good sign the arithmetic is sound, and it is also the clearest possible evidence that nothing about the AI changed.

### The counts behind the percentages, which the paper does not spell out

Every percentage in the paper reconciles exactly, and working backwards from sensitivity, specificity, PPV and NPV on 1,006 images recovers the underlying counts:

- **Consolidation:** about **191 positives** (19.0% of all films). At the published cut-off the AI flagged 53 films: **45 right, 8 wrong — and 146 cases missed.**
- **Pneumonia:** about **183 positives** (18.2%). The AI flagged 36 films: **32 right, 4 wrong — 151 missed.**
- **Pleural effusion:** about **136 positives** (13.5%). The AI flagged 129 films: **85 right, 44 wrong — 51 missed.**

Those three numbers raise a question the paper never addresses. 19.0% of these films were labelled consolidation and 18.2% pneumonia. Unless those two groups are very nearly the same films, more than a third of all after-hours chest X-rays at this hospital showed one or the other. **The overlap between the consolidation and pneumonia labels is not reported**, and it matters a great deal — see below.

## 3. How Strong Is This Evidence? (Grade 2/5)

**Grade: 2/5 — weak, but honest and useful within a narrow claim.**

This grade is not an accusation. The paper is clearly written, its arithmetic is clean, it labels its optimised thresholds as optimised rather than dressing them up, and it is upfront about the reference standard being a surrogate. The grade reflects what the design can carry and what the headline claim actually rests on.

**What it genuinely supports.** That at this hospital, in this population, the published cut-offs for CheXNeXt were badly wrong, and that the model's ranking ability was far better than its out-of-the-box answers suggested. That claim is well evidenced and it is worth publishing. Negative or awkward findings about tools people are about to deploy are exactly what the literature needs more of.

**What it does not support.** The sentence everyone will quote — "sensitivity improved to 0.894" — has never been tested on data the cut-off had not already seen. The authors found the dial setting that worked best on 1,006 films and then reported how well that setting worked on the same 1,006 films. That is not fraud, and it is not even unusual; it is simply a different kind of number from a validated one, and the paper does not distinguish between the two.

**Four things hold it at 2 rather than 3.**

**The reference standard is a report, not a disease.** "Truth" here is what a radiologist happened to write. No microbiology, no follow-up, no second reader. So the study measures *agreement with the local reporting style*, not accuracy at detecting infection. If the hospital's radiologists are cautious about the word "pneumonia", the AI is scored against that caution. The authors state this clearly and justify it as realistic, which is fair — but it caps what the numbers can mean.

**One person extracted every label, with no check.** A single senior trainee read 1,006 reports and decided what each one said. No second extractor, no agreement statistic. Text extraction from free-text reports is a judgement task, not a clerical one — "patchy opacity, consider infection" either is or is not a consolidation label depending on who is reading. An interobserver check on even 100 reports would have cost little and settled it.

**Nobody knows who was in this study.** The IRB waiver meant no demographic or clinical data was pulled at all. No age, no sex, no indication. You cannot assess generalisability to any other population, because you cannot describe this one. You cannot check whether the sample is representative even of this hospital's own ED. One month of data also means one season — in a tropical climate with its own infection pattern.

**The three findings are probably not three findings.** 191 consolidations and 183 pneumonias in 1,006 films, with the overlap unreported. Almost certainly these are largely the same radiographs, labelled twice because the report said "consolidation, likely pneumonia". If so, the study has not validated the model on three conditions; it has validated it on roughly two, one of them counted twice — and the three sets of confidence intervals are not independent of each other.

**What pulls it up to 2 rather than 1.**

The question is real and underexplored: most published AI validations use proprietary tools, and whether a free model's published settings transfer to a new hospital is exactly what a resource-limited department needs to know. The sample is a consecutive real-world after-hours slice rather than a curated set. Twenty board-certified radiologists wrote the reference reports, blinded. STARD was followed. The confidence intervals are properly computed — I checked them against exact binomial intervals and they match closely, so the bootstrap is doing its job here. Every number in all three tables reconciles with every other number. The limitations section names most of the problems above without being forced to.

**Where 2/5 sits.** This is a competent, modest, locally useful study whose most quotable result is also its least validated one. Read as "our hospital tried the published settings and they did not work", it is sound. Read as "CheXNeXt achieves 89% sensitivity", it is not yet evidence.

## 4. The Editor's Concerns

**Split the data, or stop reporting the optimised numbers as performance.** This is the main one. With 1,006 films the authors could have chosen thresholds on half and reported them on the other half, or used cross-validation. As it stands, Tables 2 and 3 describe a dial fitted to the same films it is scored on. At minimum, the paper should say so in the abstract.

**The confidence intervals around the optimised figures are too narrow, and not because the bootstrap is wrong.** They are computed as if the threshold were handed down from outside. It was not; it was estimated from these data. Uncertainty in choosing the threshold is nowhere in those intervals.

**Put the collapse in PPV in the abstract.** The abstract says sensitivity rose "while maintaining acceptable specificity of 0.765, 0.881 and 0.848". True — but at those settings, positive predictive value for consolidation fell from 0.846 to **0.467** and for effusion from 0.656 to **0.466**. More than half of everything the AI flags is wrong. For a tool proposed as triage support in a busy ED, that is the operationally decisive number and it appears only in a table.

**Report the overlap between the consolidation and pneumonia labels.** One line. Without it a reader cannot tell whether this is three validations or one-and-a-half, and cannot judge whether the three sets of results are independent.

**Check the label extraction.** A second reader on a sample of reports, with a kappa statistic, would cost a day and would remove the single largest unquantified source of error.

**Report something about the patients.** Even aggregate, de-identified age and sex bands would let a reader judge transportability. The IRB waiver is a reason this is missing, not a reason it does not matter — and it is worth saying in the limitations that it makes external generalisation untestable rather than merely uncertain.

**One month is one season.** Infection prevalence in an ED swings across the year. Nineteen percent consolidation in October 2024 is not a stable property of this hospital.

**No multiplicity adjustment, across three correlated outcomes and three threshold criteria.** Less serious here than in a hypothesis-testing paper, since these are estimates rather than significance tests, but it should be acknowledged.

**Say who paid, and declare the platform relationship.** No funding or competing-interests statement is in the published record reached here. The analysis ran on a commercial platform; the terms should be stated.

### What this study did well

- Asked a question that matters to the people least served by the AI literature: departments without budgets.
- Used real after-hours films, the exact setting where the tool would be used, rather than a curated research dataset.
- Reported the embarrassing result. Sensitivity of 0.176 is not a flattering number to publish, and they led with it.
- Labelled the optimised thresholds as optimised, and gave both the F1-based and Youden-based versions so the reader can see the trade-off rather than being handed one.
- Reported AUC alongside the threshold-dependent metrics, which is precisely what let them diagnose the problem as a threshold problem.
- Computed confidence intervals that stand up to checking.
- Stated the surrogate reference standard as a limitation in the abstract itself.

## 5. Statistics Spotlight

### Concept 1: How a model can have a brilliant AUC and a useless sensitivity at the same time

This paper is the cleanest teaching example of this I have come across, because it contains the same model at two settings and nothing else changes.

**What AUC is.** The area under the ROC curve answers one question: if you take one patient who has the disease and one who does not, how often does the model give the sick one a higher score? AUC 0.900 means 90 times out of 100. It is a measure of **ranking** — of whether the model can put cases in the right order. It says nothing at all about where you should draw the line.

**What sensitivity is.** Of the people who have the disease, the share the test catches. Specificity is the mirror: of the people who do not, the share correctly cleared. Both of these depend entirely on where you draw the line.

**How this paper applied it.** For consolidation, AUC 0.900 and sensitivity 0.234, at the same time, on the same films. The model ranks superbly and catches almost nothing.

**The intuition, with this paper's own numbers.** Picture 1,006 chest X-rays laid out left to right, sorted by the AI's score. About 191 of them have consolidation. A ranking that good means the 191 are bunched heavily toward the right-hand end. Now the cut-off: Stanford's published setting of 0.744 puts the line almost at the far right edge. Only 53 films fall to the right of it. Of those, **45 really do have consolidation and 8 do not** — so when the AI speaks it is nearly always correct, which is the high PPV of 0.846. But **146 cases sit to the left of the line, uncalled.**

Now move the line to 0.11, well to the left. Suddenly 363 films fall to its right: **171 of the 191 real cases are caught, and 192 films without consolidation are flagged too.** Sensitivity 0.894, PPV 0.467.

Same ranking. Same model. Same X-rays. The only thing that moved was a number in a configuration file.

**An everyday analogy.** A smoke alarm's sensor can be excellent at distinguishing smoke from steam — that is its AUC. Where you set its trigger is a separate decision, and one you make according to what you are afraid of. Set to scream only in a blazing fire, it will almost never give a false alarm and will also sleep through your kitchen filling with smoke. Set to trip on toast, it catches everything and you take the battery out by Wednesday. Nobody would describe either setting as "how good the alarm is".

**Watch out.** AUC is the number that gets into abstracts and press releases, because it is threshold-free and therefore always flattering. But no patient is ever treated by an AUC. Patients are treated on the basis of a yes or a no, and that comes from the threshold. **When a paper leads with AUC, find the sensitivity and specificity at the threshold the authors actually propose to use** — and if the paper does not say what threshold that is, you have not been told how the tool behaves. The inverse error is just as common: dismissing a model because its out-of-the-box sensitivity is poor. A high AUC with poor sensitivity means the model is fine and the setting is wrong. A low AUC means no setting will save it.

### Concept 2: Why thresholds do not travel between hospitals

Here is the part of this paper worth carrying into every future AI study you read.

**What a threshold is.** The model emits a probability from 0 to 1. The threshold converts it into a decision. Stanford published theirs, chosen by maximising the F1 score on their own tuning set.

**How this paper applied it.** The authors used Stanford's numbers, found them useless, and recomputed the best cut-offs for their own data:

- Consolidation: published **0.744**, locally optimal **0.22** by F1 and **0.11** by Youden — **three to seven times lower.**
- Pneumonia: published **0.831**, locally optimal **0.31** by both criteria — **nearly three times lower.**
- Pleural effusion: published **0.731**, locally optimal **0.73** by F1 — **essentially identical.**

That last line is the one that makes this interesting rather than just a cautionary tale. For one of the three findings, the published threshold transferred perfectly — the local F1-optimum was 0.73 against a published 0.731, and "optimising" it bought an improvement in F1 of 0.003, which is nothing. **So thresholds are not universally untransferable. They transfer for some tasks and fail catastrophically for others, and you cannot tell which without checking.**

**The theory: discrimination versus calibration.** Two different things can be right or wrong about a model's output. **Discrimination** is whether it ranks cases correctly — measured by AUC, and it held up fine here (0.856 to 0.916, which is respectable). **Calibration** is whether the number it emits means what it says: whether the films it scores 0.75 really do contain consolidation about 75% of the time. Calibration is the fragile one. It depends on disease frequency in the population, on the X-ray machines, on exposure settings, on patient body habitus, on how the images were processed before the model saw them.

CheXNeXt was trained on ChestX-ray14 — American patients, largely inpatients, a particular set of scanners, labels mined automatically from report text. It was then run on Singaporean adults in an emergency department at two in the morning. The ranking survived that journey. **The scale did not.** The model's scores got systematically squashed downward, so a film that would have scored 0.80 in the training distribution scores 0.25 here. Rank preserved, meaning lost.

**A tiny worked example.** Two teachers mark the same hundred essays. They agree almost perfectly on the order from best to worst — their rankings correlate beautifully. But one marks generously, averaging 72, and the other harshly, averaging 48. Now impose a rule: "a pass is 65". From the generous marker, two-thirds of the class passes. From the harsh one, almost nobody does. Neither marker is wrong about the essays. The pass mark was calibrated to one of them and silently applied to the other.

**Watch out.** "We used the published threshold" sounds like the careful, neutral, non-cherry-picking choice — and in the sense of avoiding self-serving tuning, it is. But it is not a neutral act. It is an assumption that the new population's score distribution matches the developer's, and that assumption is testable and frequently false. The honest procedure is to **re-derive the threshold locally on data held out from reporting**, and to say which you did. A paper that never names its threshold has hidden this decision entirely. And when you see a deployed tool performing worse than its publication promised, calibration drift is the first thing to suspect — long before anyone concludes the model is bad.

### Concept 3: Choosing the dial setting on the same data you report — how much does it actually cost?

This is where the paper's own method needs examining, and it deserves a calibrated answer rather than a reflex.

**What the problem is.** The authors swept every possible threshold across their 1,006 films, picked the one that scored best, and reported that best score. The score is therefore partly a measurement of the model and partly a measurement of the luck in this particular sample. Choose the highest point on a bumpy line and you have chosen some real height and some bump.

**How this paper applied it.** Both optimisation criteria were applied to the full dataset. No held-out split, no cross-validation, no external data. The resulting figures — sensitivity 0.894 for consolidation, and the rest — are in-sample.

**The intuition.** Imagine testing twenty slightly different recipes on one group of tasters and declaring the winner "the best recipe". Some of that winner's margin is genuinely better cooking. Some of it is that this particular room happened to like extra salt. Serve it to a fresh room and it will usually score a little lower. The more recipes you tried and the smaller the room, the bigger the drop.

**So how big is the drop here?** Rather than hand-wave, I simulated it. Taking a model with AUC 0.900 and a sample of the same shape as this study — 191 positives and 815 negatives — I picked the Youden-maximising threshold on one sample and then applied that threshold to a fresh sample, 2,000 times over. **The average Youden index was 0.651 on the data used to choose the threshold and 0.630 on fresh data: an average optimism of about 0.021.** (That is my own illustration, not the paper's analysis. As a sanity check, the paper's own reported Youden index for consolidation at its optimised threshold is 0.659 — close to my simulated in-sample figure, which suggests the model of the situation is about right.)

Two honest conclusions follow, and they point in opposite directions.

**First: the bias is real but modest.** About two points of Youden index. The optimised sensitivity of 0.894 is probably a little high, not a mirage. With 191 positives and 815 negatives, the ROC curve is estimated from a lot of data, so there is not much bumpiness to overfit to. **Sample size is what determines how much this hurts.** With 30 positives instead of 191, the optimism would be several times larger. The reflex "they tuned on the test set, therefore the result is worthless" is as wrong as ignoring the problem.

**Second: the paper still cannot support its headline, and for a subtler reason.** The issue is not mainly the 0.02 of optimism. It is that *every* number in Tables 2 and 3 is conditional on a threshold estimated from these data, and the confidence intervals do not know that. They are computed as though the threshold arrived from outside. They answer "how uncertain is performance at a cut-off of 0.11?" when the question a reader needs answered is "how uncertain is performance at a cut-off chosen the way we chose ours?" — which is a wider interval by an amount the paper never estimates.

**A note on the bootstrap, and a correction to a reflex.** Yesterday's paper in this reading list contained a bootstrap confidence interval computed over eight observations, which was meaningless. It would be easy to carry that suspicion over. It does not apply here: I checked this paper's intervals against exact (Clopper–Pearson) binomial intervals and they line up closely — consolidation PPV 0.744–0.941 against an exact 0.724–0.933; pneumonia sensitivity 0.124–0.233 against an exact 0.123–0.238. With dozens to hundreds of events, the bootstrap works as advertised. **The machinery is fine. The problem is what it was pointed at.**

**Watch out.** When you see "optimised threshold", "optimal cut-point", "Youden index was used to determine the threshold", immediately ask one question: *on which data?* If the answer is "the same data these results come from", the numbers are a best case, not an expectation. The phrase to hunt for is a held-out set, a validation split, or cross-validation. And note the honest asymmetry — the **first** table in this paper, using thresholds chosen by someone else on someone else's data, is methodologically clean precisely because the authors had no hand in choosing them. The clean table is the one with the terrible sensitivity. That is not a coincidence; it is the whole shape of the problem.

## 6. Jargon Translator

- **Chest radiograph (CXR)** — a chest X-ray.
- **Consolidation** — a region of lung where the air spaces have filled with fluid, pus or cells, so it appears white instead of black. A radiographic appearance, not a diagnosis.
- **Pneumonia** — infection of the lung tissue. On an X-ray it usually looks like consolidation, which is why the two labels overlap.
- **Pleural effusion** — fluid collected in the space between the lung and the chest wall.
- **After-hours** — here, before 08:30 or after 17:30 on weekdays, or any time at weekends, when this hospital has no radiologist on site to report films immediately.
- **Open-source model** — software anyone can download, inspect, run and modify free of charge. The opposite of the proprietary systems most hospitals license.
- **Convolutional neural network (CNN)** — the standard family of AI models for images; it learns visual patterns from large numbers of labelled examples.
- **ChestX-ray14** — the public training dataset behind CheXNeXt: 112,120 frontal chest X-rays from 30,805 patients, with labels extracted automatically from report text.
- **CARPL.AI** — the commercial platform used here as the interface for running the model on the hospital's images.
- **DICOM** — the international file standard for medical images, carrying both the picture and patient metadata (stripped here during anonymisation).
- **PACS** — the hospital's picture archiving and communication system, where radiology images are stored and viewed.
- **Reference standard** — the thing a test is scored against. Here it was the radiologists' written reports, not confirmed infection, which is why the authors call it a surrogate.
- **Surrogate marker** — a stand-in for the thing you actually care about. Radiographic consolidation standing in for proven lung infection.
- **PPV (positive predictive value)** — of everyone the test flags, the share who really have the finding. Depends heavily on how common the finding is.
- **NPV (negative predictive value)** — of everyone the test clears, the share who really are clear.
- **F1 score** — a single number combining PPV and sensitivity (their harmonic mean, a kind of average that is dragged down hard by whichever is worse). Used here both as a threshold-choosing criterion and as a summary. F1 of 0.294 for pneumonia reflects decent precision crippled by poor recall.
- **Youden index** — sensitivity plus specificity minus 1. Zero means no better than guessing, 1 means perfect. Choosing the threshold that maximises it treats one missed case and one false alarm as equally bad, which is rarely true in medicine.
- **Harmonic mean** — an average that punishes imbalance. The ordinary average of 0.85 and 0.23 is 0.54; their harmonic mean is 0.37.
- **Bootstrap resampling** — estimating uncertainty by repeatedly drawing samples, with replacement, from your own data and recomputing. Used here with 1,000 repetitions.
- **Clopper–Pearson (exact binomial) interval** — the conservative, always-valid confidence interval for a proportion; used above as an independent check on the paper's bootstrap intervals.
- **STARD** — the reporting checklist for diagnostic accuracy studies, which the authors state they followed.
- **Interobserver agreement** — how often two independent readers reach the same conclusion. Not assessed here, which is the paper's own stated limitation.
- **IRB waiver** — permission to use patient data without individual consent, granted on condition the data is anonymised; here it also meant no clinical details could be extracted.
- **External validation** — testing on data from a different institution or population. Not done here.

## 7. What You Can (and Can't) Say

**Fair to say:**

- "A Singapore hospital ran a free, open-source chest X-ray AI on 1,006 after-hours emergency films and found that, at the cut-offs its developers published, it missed about four out of five cases of consolidation and pneumonia."
- "The model's ranking ability was good — AUC 0.900 for consolidation, 0.856 for pneumonia, 0.916 for pleural effusion — which tells you the poor detection rate came from the cut-off, not from the model."
- "When the authors recomputed the cut-offs for their own data, sensitivity for consolidation rose from 0.234 to 0.894 — on the same films used to choose the cut-off, so that figure has not been independently tested."
- "At the cut-offs the developers published, when this AI said 'positive' it was usually right: 45 of 53 flagged films for consolidation, 32 of 36 for pneumonia."
- "At the re-tuned cut-offs, more than half of everything the AI flagged was a false alarm: positive predictive value fell to 0.467 for consolidation and 0.466 for effusion."
- "For pleural effusion the published cut-off turned out to be almost exactly right for this hospital, so thresholds do not always fail to transfer."
- "The study compared the AI against what radiologists wrote in routine reports, not against confirmed infection."

**Not fair to say:**

- ❌ "CheXNeXt detects pneumonia with 68% sensitivity and consolidation with 89%." Those come from cut-offs chosen on the same 1,006 films they are reported on. They are a best case, not a validated performance.
- ❌ "Open-source AI matches radiologists on chest X-rays." This study never compared the AI to radiologists. Radiologists *were* the yardstick, so the AI cannot, by construction, score better than them here.
- ❌ "The AI is 99% specific, so a positive result means you have pneumonia." Specificity was measured against what a radiologist wrote, not against proven infection, and PPV collapses once the cut-off is moved to catch a useful share of cases.
- ❌ "This proves AI can safely triage after-hours chest X-rays." Nothing about workflow, turnaround time, clinician behaviour or patient outcome was measured. The authors say so explicitly.
- ❌ "The AI improved after calibration." The AI did not change. One configuration number changed.
- ❌ "The model was validated on three conditions." Consolidation and pneumonia were labelled on roughly 19% and 18% of the same 1,006 films, and the overlap between them is not reported.
- ❌ "This shows free AI is as good as the paid kind." No proprietary system was tested here for comparison.
- ❌ "The results apply to my hospital." No patient characteristics were recorded at all, from one month in one Singapore emergency department. There is no basis for transporting the numbers anywhere.

## 8. Bottom Line for Your Life

For a regular person, nothing here changes anything today. No AI read your X-ray in this study, no treatment decision was made by one, and the whole thing was done on images after the fact. If you are in an emergency department at 2am, a doctor is looking at your chest film and a radiologist will look at it properly later — which is exactly the gap this tool is being proposed to fill, and it is not filling it yet.

For anyone who reads papers or argues about AI in medicine, this one is worth keeping for a single reason: it is a clean demonstration that **the headline failure of an AI tool was not the AI**. The same model, unmodified, went from catching 23% of cases to catching 89% because somebody changed one number. Whenever you see a deployed AI underperforming its publication, or a study reporting disappointing accuracy, the threshold is the first thing to interrogate — and conversely, whenever you see an impressive sensitivity, ask where the threshold came from and whether it was ever tested on data it had not already been fitted to.

What would make this convincing: the authors re-running their optimised cut-offs on a fresh month of films they had not seen, a second reader checking the label extraction, and a reference standard with some actual clinical confirmation in it. All three are achievable at a single hospital, and the first one is nearly free.

---

*This is an educational analysis of a published scientific paper, not medical advice. Nothing here is guidance about diagnosing or treating a chest infection. If you are unwell, see a clinician.*
