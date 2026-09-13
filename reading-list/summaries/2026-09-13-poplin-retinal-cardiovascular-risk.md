# Prediction of cardiovascular risk factors from retinal fundus photographs via deep learning

- **Authors:** Ryan Poplin, Avinash V. Varadarajan, Katy Blumer, Yun Liu, Michael V. McConnell, Greg S. Corrado, Lily Peng, Dale R. Webster (Google Research, Mountain View; Verily Life Sciences; Stanford School of Medicine) — 8 authors
- **Venue:** Nature Biomedical Engineering, 2018;2(3):158–164 (published February 19, 2018)
- **DOI link:** https://doi.org/10.1038/s41551-018-0195-0
- **PubMed link:** https://pubmed.ncbi.nlm.nih.gov/31015713/ (PMID 31015713)
- **Full-text link used:** no PubMed Central copy exists for this paper (the PMID-to-PMCID lookup returned no PMC record), and the publisher page is not reachable from this environment. Full text was read through the Scite full-text index, which returned the complete body of the accepted manuscript (18,051 characters) under this exact DOI and title.
- **Basis:** FULL TEXT — introduction, results, discussion, methods, statistical analysis, and all table and figure captions were read. The numeric contents of Tables 1–4 were **not** in the retrieved text, only their captions, so every number quoted below comes from the running text or from the PubMed abstract. Funding and competing-interest statements were not present in the retrieved text; PubMed tags the work as non-US-government research support. Identifiers verified against the live PubMed/NLM record and against the DOI-resolved full-text record; direct URL browsing is blocked in this environment, so links are constructed from those verified records.
- **Decoded:** 2026-09-13

---

# The Gist

Doctors have looked into the back of the eye for a century, because it is the one place in the body where you can see blood vessels directly without cutting anything open. Google's team asked a stranger question: what *else* is written in that photograph? They trained a neural network on retinal photographs from 284,335 patients and found it could read off things nobody thought were visible there — the person's age to within about 3 years, their sex almost perfectly, their blood pressure, whether they smoked. It could even guess, slightly better than chance, who would have a heart attack or stroke in the next five years. The finding is genuinely surprising and it changed what people thought images contain. The catch, which the authors state plainly themselves, is that the heart-attack prediction rests on only 105 actual events, and its accuracy was statistically indistinguishable from a blood-test calculator that already exists.

# Study Snapshot

- **Study type:** Retrospective prediction-modelling study on stored images and records. Nobody was treated, screened, or followed forward because of a model output. Low on the evidence ladder for any claim about patient benefit, but unusually interesting as a discovery.
- **Training data:** 284,335 patients — 48,101 from UK Biobank (a British research study that recruited 500,000 volunteers aged 40 to 69 between 2006 and 2010, of whom 67,725 had retinal photographs taken) and 236,234 from EyePACS, a US teleretinal service that screens for diabetic eye disease across more than 300 clinics.
- **Validation data:** 12,026 UK Biobank patients (the held-back 20% of that dataset) and 999 EyePACS patients photographed later, between May and October 2015, with no patient overlap with the training images.
- **The two populations were very different.** UK Biobank patients were mostly white, mostly non-diabetic, average age 56.9 years. EyePACS patients were mostly Hispanic and mostly diabetic — their average HbA1c, a three-month blood-sugar average, was 8.2%, well above the normal range. HbA1c was recorded for only 60% of them and was not available at all for UK Biobank.
- **What the model read off a photograph:** age, within an average error of 3.26 years (95% confidence interval 3.22 to 3.31) against 7.06 years for simply guessing the population average; sex, with an AUC of 0.97; smoking status, AUC 0.71; systolic blood pressure, within an average error of 11.23 mmHg; and self-reported ethnicity, with a Cohen's kappa agreement score of 0.60 in UK Biobank and 0.75 in EyePACS.
- **The headline clinical claim, and its size:** predicting a major adverse cardiovascular event (heart attack, stroke, or cardiovascular death) within 5 years, from the photograph alone, gave an AUC of 0.70 (95% CI 0.648 to 0.740). The European SCORE risk calculator, which needs a blood test, scored 0.72 (0.67 to 0.76) on the same patients.
- **How rare those events were:** 631 events occurred within 5 years of imaging across the whole dataset. In the validation set, the text reports 150 events; the Table 3 caption reports that 91 patients with a prior cardiac event were excluded and 105 of the remainder had an event within 5 years. Those two figures are not reconciled in the retrieved text, and the caption's own arithmetic (12,026 minus 91) does not come to the 11,835 it states.
- **Why the model looked where it looked:** the team generated attention heatmaps and showed 100 of them per prediction task to 3 ophthalmologists, blinded to what each map was supposed to explain and given all 800 images shuffled together. Blood vessels lit up for age, smoking, and blood pressure. The optic disc lit up for sex. For body mass index and diastolic blood pressure, the maps were non-specific.
- **The machinery:** an Inception-v3 network with 22 million parameters, trained in TensorFlow with early stopping, and 10 separately trained copies averaged together. Confidence intervals came from 2,000 bootstrap resamples.
- **Funding / conflicts:** not reported in the retrieved text. Every author worked for Google, Verily, or (in one case) both Verily and Stanford.

# How Strong Is This Evidence?

**Grade: 3/5 — a real and surprising discovery about what images contain, wrapped around a clinical claim that the paper's own numbers do not support.**

Split the paper in two and it grades differently on each half.

The discovery half is strong. That a photograph of the retina encodes a person's age to within 3.26 years, and their sex almost perfectly, was not something the field expected, and the authors demonstrated it properly: two large datasets, a stated baseline to compare each number against, bootstrap confidence intervals on every estimate, consistent results across two populations that differ enormously in ethnicity and diabetes status, and a blinded expert review of where the model was actually looking. That last step is rarer than it should be and it is the paper's best methodological idea.

The clinical half is thin, and the authors say so. Predicting cardiovascular events gave 0.70 against the existing calculator's 0.72, with confidence intervals that overlap across almost their entire width, resting on roughly a hundred events. The honest reading is that the two methods could not be told apart, not that the photograph matched the blood test. The paper's own discussion calls this result "preliminary" and the dataset "relatively small for deep learning."

What keeps the grade from going higher: neither validation set is genuinely external. The UK Biobank validation patients are the held-back fifth of the same study the model trained on; the EyePACS validation patients come from the same screening network, just later months. No calibration is reported anywhere, so we know the model ranks patients but not whether its probabilities mean anything. And the data cannot be shared, so nobody outside can re-run this.

# The Editor's Concerns

- **Predicting a risk *factor* is not predicting risk.** Most of this paper's impressive numbers are for age, sex, and ethnicity — things you can ask a patient in ten seconds and get exactly right. The paper's argument is that because these are inputs to risk calculators, predicting them implies predicting risk. That is a reasonable hypothesis, and the direct test of it came out at 0.70 with wide error bars.
- **"Comparable to SCORE" is a generous phrase for 0.70 versus 0.72.** No formal statistical comparison of the two curves is reported in the retrieved text — no DeLong test, no confidence interval on the difference between them. Overlapping intervals are not evidence that two things are the same; they are an absence of evidence that they differ. With 105 events, this study could not have detected anything but an enormous gap.
- **The validation is internal, wearing external clothes.** The abstract says "two independent datasets," and the datasets are independent of each other. But each validation set is drawn from the same source as its own training set. The genuinely hard test — train at Google on EyePACS, deploy on a different country's cameras and patients — was not attempted here.
- **No calibration, anywhere.** The paper reports how well the model ranks patients and never reports whether a predicted 10% risk corresponds to a real 10%. For a tool whose entire proposed use is telling someone their risk number, that is the missing half of the report card.
- **Blood pressure prediction flattens exactly where it matters.** The authors show predicted systolic blood pressure tracks the real value up to about 150 mmHg and then levels off. The people whose pressure is dangerously high are the people the model stops distinguishing.
- **An average error of 11.23 mmHg is large in clinical terms.** The boundary between normal and high blood pressure sits in that range. A prediction that can be off by that much on average is a population-level signal, not a reading you would act on.
- **The two study populations are not the general public.** One is a volunteer research cohort that is famously healthier and whiter than Britain overall; the other is a diabetic screening population with an average HbA1c of 8.2%. Neither tells you how this performs in a general clinic.
- **Sex prediction from the optic disc is a striking result with no clinical use whatsoever,** and it is the number most often quoted from this paper. Worth keeping straight: AUC 0.97 belongs to a task nobody needs solved.
- **Google designed it, ran it, and scored it,** using data that cannot be released. This is the same structural issue as the Rajkomar paper on your list, and it is not disqualifying — but it means the result rests on description rather than replication.
- **A reporting wobble.** The event counts in the text (150) and in the Table 3 caption (105, after excluding 91 prior events) are not reconciled, and the caption's subtraction does not come out. Small, but the kind of thing that matters when a headline rests on how many events there were.
- **What this study did well:** stated an explicit baseline for every continuous prediction, so the reader can see what "3.26 years of error" is better *than*; reported bootstrap confidence intervals on everything; tested in two populations that differ about as much as two populations can; kept the tuning data separate from the training data and said so, explicitly warning readers about the confusing double meaning of the word "validation"; had ophthalmologists check the attention maps blind, with the images shuffled so they could not pattern-match; and wrote a limitations section that concedes the dataset is small, the intervals are wide, and the cardiovascular result needs a bigger study.

# Statistics Spotlight

**1. Mean absolute error — and the baseline question that gives it meaning.**
- *What it is:* Mean absolute error, or MAE, is the average size of the mistake, ignoring whether the guess was too high or too low. If the model says 60 and the truth is 63, that is an error of 3. Average that across everyone and you have the MAE.
- *How this paper used it:* Age came out at an MAE of 3.26 years, and the authors put the number that matters right next to it: 7.06 years, which is what you get by ignoring the photograph entirely and guessing the population's average age for every single person. The model roughly halved the error. For systolic blood pressure the MAE was 11.23 mmHg.
- *The theory, with a worked example:* A number like "3.26 years" means nothing on its own — it depends entirely on how much the thing varies in the first place. Predicting the height of adult men to within 3 inches is unremarkable; predicting their height to within 3 millimetres would be astonishing. The fixed reference point is always: how well would I do knowing nothing? Here, "knowing nothing" means always answering 57, which is wrong by about 7 years on average. Cutting that to 3.26 is real signal. Now apply the same test to blood pressure: systolic pressure in a middle-aged population typically spreads across roughly 20 mmHg, so an 11.23 mmHg error is a much smaller share of the available room. The same paper, the same metric, two very different levels of achievement.
- *Watch out:* Whenever a paper or a press release gives you an error in raw units — years, millimetres of mercury, dollars, degrees — ask what the error would have been with no model at all. Good papers hand you that baseline, as this one does. Papers that quote an MAE with nothing beside it are counting on the number sounding small.

**2. Comparing two AUCs when events are rare — the 0.70 versus 0.72 problem.**
- *What it is:* AUC (area under the receiver operating characteristic curve) measures ranking. An AUC of 0.70 means that if you pick one person who had a heart attack and one who did not, the model gives the first a higher risk score about 70% of the time. A coin flip scores 0.5.
- *How this paper used it:* The retinal model scored 0.70 (95% confidence interval 0.648 to 0.740) for 5-year cardiovascular events. The SCORE calculator, using a blood test, scored 0.72 (0.67 to 0.76). The paper calls these "comparable." Both intervals came from resampling the validation patients 2,000 times with replacement — the bootstrap — and reading off the middle 95% of the results.
- *The theory, with a worked example:* The width of those intervals is driven almost entirely by how many *events* there were, not how many patients. Roughly 105 heart attacks and strokes is a small number to estimate anything from. Think of judging two restaurants from reviews: with 4,000 reviews each, a 4.2 and a 4.4 is a real difference; with 10 reviews each, the same gap is noise and one extra grumpy diner flips it. The ranges here, 0.648–0.740 and 0.67–0.76, overlap across nearly their whole length. The data is equally consistent with the photograph being slightly better than the blood test and with it being meaningfully worse.
- *Watch out:* Two traps live here, and they point in opposite directions. First, "the intervals overlap, so there's no difference" is wrong — overlapping intervals mean the study could not resolve the question, not that the answer is zero. Second, and more common in press coverage, "comparable to the established test" gets read as "as good as the established test," which is a claim of equivalence that this design cannot make. Proving two things are equivalent requires a study specifically built for it, with a pre-stated margin for how close counts as close. Nobody has done that here. Notice also that no formal test comparing the two curves is reported — there is a standard one, DeLong's test, and its absence means the comparison never got a p-value at all.

**3. Cohen's kappa — agreement after you subtract the luck.**
- *What it is:* When you are scoring how often a prediction matches the truth across several categories, raw percent agreement flatters you, because some matches happen by chance. Cohen's kappa subtracts out the chance agreement. It runs from 0 (no better than guessing) to 1 (perfect).
- *How this paper used it:* For predicting self-reported ethnicity from a retinal photograph, the kappa was 0.60 (95% CI 0.58 to 0.63) in UK Biobank and 0.75 (0.70 to 0.79) in EyePACS.
- *The theory, with a worked example:* Suppose a population is 90% one ethnicity and 10% another, and your model simply answers "the common one" every time. It is right 90% of the time and has learned nothing. Kappa asks how much of that 90% you would have got for free, and here the answer is essentially all of it, so kappa lands near 0. The higher kappa in EyePACS than in UK Biobank partly reflects that EyePACS had a more mixed population, leaving more room to actually be right. That is why kappa, like almost every accuracy measure, is not portable between populations.
- *Watch out:* Kappa is reported as a single number with reassuring verbal labels attached to it ("substantial agreement," "good"), and those labels are arbitrary conventions, not facts. The deeper point this result raises is worth sitting with: a model can read ethnicity off a medical image whether or not anyone asked it to. Later work showed this holds for other imaging too. That means "we removed race from the inputs" does not remove race from the model — exactly the lesson the Obermeyer paper on your list taught from the opposite direction.

# Jargon Translator

- **Retinal fundus photograph:** a picture of the back inside surface of the eye, taken with a special camera through the pupil. It shows the retina, the optic disc, and blood vessels directly.
- **Optic disc:** the bright circular spot where the optic nerve enters the eye.
- **Major adverse cardiovascular event (MACE):** a bundled outcome covering heart attack, stroke, and death from cardiovascular causes.
- **SCORE calculator:** a European tool that estimates cardiovascular risk from age, sex, smoking, blood pressure, and cholesterol — cholesterol requiring a blood draw.
- **Systolic blood pressure:** the top number in a blood pressure reading, measured in millimetres of mercury (mmHg).
- **HbA1c:** a blood test reflecting average blood sugar over roughly three months; 8.2% indicates poorly controlled diabetes.
- **Mean absolute error (MAE):** the average size of a prediction's mistake, in the units of the thing being predicted.
- **AUC / AUROC:** a ranking score from 0.5 (coin flip) to 1.0 (perfect) for how well a model separates the people who have an outcome from those who do not.
- **Cohen's kappa:** an agreement score that subtracts out the agreement you would get by chance.
- **Bootstrap:** re-drawing your test group at random, thousands of times, to see how much a result would wobble — the source of the confidence intervals here.
- **Attention / saliency map:** a heatmap showing which parts of an image most influenced a model's answer.
- **Inception-v3:** a specific image-recognition network design, here with 22 million adjustable settings.
- **Ensembling:** training several copies of a model and averaging their answers, which usually beats any single copy.
- **Early stopping:** halting training once performance on held-back data stops improving, to keep the model from memorising its training examples.
- **UK Biobank:** a large British research study that recruited 500,000 volunteers aged 40 to 69 and has followed their health since.

# What You Can (and Can't) Say

**Fair to say:**
- "A 2018 Google study showed that a deep learning model reading only a photograph of the retina could estimate a person's age to within about 3.26 years on average, and identify their sex with an AUC of 0.97 — signals nobody knew were visible in those images."
- "The same model predicted 5-year cardiovascular events with an AUC of 0.70, against 0.72 for a blood-test-based calculator, but with only about 105 events and confidence intervals that overlap almost entirely."
- "Blinded ophthalmologists confirmed the model was attending to blood vessels when predicting age, smoking, and blood pressure, and to the optic disc when predicting sex."
- "The authors themselves describe the cardiovascular result as preliminary and the dataset as relatively small."

**Not fair to say:**
- "An eye photo predicts heart attacks as accurately as a blood test" — the study could not distinguish the two, which is a different statement from showing they are equal, and it was never designed to test equivalence.
- "AI can diagnose heart disease from a selfie of your eye" — these were clinical fundus photographs from dedicated cameras, not phone pictures, and no diagnosis was made or acted on.
- "This is validated on independent data" — each validation set came from the same source as its own training set. No outside institution tested this model.
- "The model is 97% accurate" — 0.97 is a ranking score for predicting sex, a task with no clinical value here.
- "This means you can skip the cholesterol test" — nothing in this study was deployed, and no patient's care was changed or followed.

# Bottom Line for Your Life

The durable thing about this paper is the discovery, not the application: an ordinary eye photograph carries more information about you than a century of ophthalmology had noticed, and a model given enough examples will find it whether or not anyone asked. That is genuinely important, and it is why this paper has been cited so heavily.

The lesson for reading headlines is in the gap between the paper's two halves. The strongest numbers here (age, sex) attach to the least useful tasks, and the most useful task (predicting heart attacks) produced the weakest number. That pattern is extremely common, and the headline almost always takes the big number from one column and the importance from the other. When you see "AI predicts X from Y," find the number attached to X specifically, then find how many people actually had X happen to them. Here it was about a hundred, and every conclusion narrows accordingly.

One practical note in the other direction: if a model can read your ethnicity off a medical image at a kappa of 0.60 to 0.75, then keeping race out of an algorithm's input list does not keep it out of the algorithm. That is worth remembering next time someone offers "it doesn't use race" as proof of fairness.

Nothing here changes what you should do about your own heart. Blood pressure, smoking, and cholesterol remain the things with actual evidence behind them. One study is one data point. This is an educational breakdown, not medical advice.

---

**Sources** (based on articles retrieved from PubMed and from the DOI-resolved full-text record; identifiers verified against the live PubMed/NLM record — URL browsing is blocked in this environment, so links are constructed from those verified records):
- DOI: https://doi.org/10.1038/s41551-018-0195-0
- PubMed: https://pubmed.ncbi.nlm.nih.gov/31015713/ (PMID 31015713)
- Full text: no PubMed Central record exists for this PMID, so no PMC link is given. The complete accepted-manuscript text was read through the Scite full-text index under this DOI; there is no separately verifiable full-text URL to cite, and none is invented here.
