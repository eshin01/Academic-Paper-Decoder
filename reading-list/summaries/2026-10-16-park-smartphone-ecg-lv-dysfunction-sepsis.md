# Screening for Left Ventricular Dysfunction in Sepsis Using a Smartphone ECG Analysis Application: A Multicenter Validation Study

**Authors:** Park YS, Kim J, Jo YH, Kwon WY, Song KJ, Lee HJ, Cho Y, Hwang JE
**Journal:** Journal of Korean Medical Science, 2026; 41(39): e217 (published 12 October 2026)
**Decoded:** 2026-10-16
**Analysis basis:** FULL TEXT (retrieved from PubMed Central, PMC13659111). Figures were not viewable — captions only — and the supplementary tables (included-vs-excluded comparison, subgroup AUCs, full regression model) were not retrievable, so anything living only there is marked as not retrieved.

**Source links (all verified against the live PubMed record):**
- DOI: https://doi.org/10.3346/jkms.2026.41.e217
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42865282/
- Full text (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC13659111/

**Declared interests to note up front:** two of the eight authors list **ARPI Inc.** among their affiliations — the company behind ECG Buddy™, the app being evaluated. **No separate funding or competing-interests statement appears in the text retrieved.**

---

## 1. The Gist

When someone arrives at the emergency department with sepsis, the standard move is to pour fluid into them — at least 30 mL per kilo in the first three hours. That saves lives in most people. In someone whose heart is already failing, it can flood the lungs.

So you want to know whether the heart is weak. The proper answer is an echocardiogram, which in most hospitals means waiting hours, or until morning. The usual shortcut is a blood test (NT-proBNP), which is slow, expensive and not very accurate in sepsis.

This team tried something else. They took the 12-lead ECG — which every septic patient gets anyway, within minutes — photographed it with an iPhone, and let an app read it. The app produces a score for the likelihood of a weak left ventricle.

On 425 septic patients across three Seoul hospitals, the score separated weak hearts from normal ones well: area under the curve 0.901, against 0.637 for the blood test in the subset where both were available. It caught 60 of the 67 patients with a weak heart.

Two things the abstract does not tell you.

It reports sensitivity, specificity and negative predictive value — and omits the positive predictive value, which is **40.4%**. The app flagged 149 patients; 89 of them had normal hearts. Three in five alarms were false. For a screening test meant to say "be careful with fluids," that may be an acceptable trade. But it is the number a reader needs and it is not in the summary.

And the cut-off used to produce all those figures was chosen by finding the value that worked best **on these same 425 patients**. Nothing was held back. So sensitivity, specificity and the rest are the best case on this dataset rather than an estimate of what happens next.

There is also an outright error in the results table, which I will come to: the F1 scores were computed for the wrong class, and the real values are about 29 points lower.

## 2. Study Snapshot

**Design:** Multicentre retrospective observational study drawn from an existing sepsis registry. Not a trial. No prospective testing.

**Where:** Three university hospitals in Seoul — Seoul National University Hospital (SNUH), SNU Bundang Hospital (SNUBH) and SMG-SNU Boramae Medical Center (BRMH). Registry years differed by site: SNUH 2019–2021, SNUBH 2020–2022, **BRMH 2018 only**.

**Who went in:** adults presenting to the emergency department with sepsis or septic shock by Sepsis-3 criteria. Data were entered by trained research nurses and verified by an emergency physician at each site.

**The funnel, and it is steep:** 5,940 patients registered → 2,311 excluded for no echocardiogram within 72 hours → 3,204 more excluded for no ECG within 72 hours → **425 included**. That is **7.2% of the registry; 92.8% were excluded.**

**Who the 425 were:** 358 (84.2%) with no left ventricular dysfunction, 67 (15.8%) with it, defined as an ejection fraction of 40% or less. Median age 77 in both groups. The dysfunction group had more men (70.1% vs 51.4%, p = 0.007), more prior heart failure (23.9% vs 7.0%, p < 0.001), more chronic kidney disease (20.9% vs 7.8%, p = 0.002) and higher troponin (p = 0.001).

**Site imbalance:** BRMH contributed 65 patients with 4 cases of dysfunction (6.2%); SNUBH 234 with 45 (19.2%); SNUH 126 with 18 (14.3%). The hospital distribution differed between groups (p = 0.033).

**What was done:** ECG images were cropped out of each hospital's electronic record, displayed on a 24-inch LCD monitor under routine indoor lighting, and photographed by **a single emergency medicine specialist** using an iPhone 15 Pro at 30–40 cm without flash. The app (ECG Buddy, a convolutional-neural-network encoder feeding task-specific networks, approved as a Class II medical device by Korea's Ministry of Food and Drug Safety) returned a score called QCG-LVDys. Scores were blinded to the echocardiographers, who had measured ejection fraction as part of routine care.

**The reference standard:** transthoracic echocardiography done as routine clinical care, with ejection fraction retrieved by a specialist from the medical record. ECG and echo each had to fall within 72 hours of arrival — **so they could be up to 72 hours apart from each other.**

**Statistics:** area under the ROC curve as the primary metric; threshold chosen by maximising the Youden index; comparison with NT-proBNP by **DeLong's test**; quartile analysis with Kruskal–Wallis and chi-squared, and trend tests (Jonckheere–Terpstra for continuous, Cochran–Armitage for proportions); an exploratory multivariable logistic regression for mortality. R 4.1.0.

**Ethics:** approved by the SNUBH Institutional Review Board (B-2409-926-103), consent waived for retrospective design.

**Main result (all 425):** AUC **0.901 (95% CI 0.865–0.937)**. At the Youden-optimal threshold of 37.35: sensitivity 89.6% (82.1–97.0), specificity 75.1% (70.4–79.6), **PPV 40.4% (35.5–45.5)**, NPV 97.5% (95.7–99.2), accuracy 77.4% (73.4–81.2). Reconstructing the counts: **60 true positives, 7 false negatives, 269 true negatives, 89 false positives.**

**Against the blood test (SNUBH only, n = 234):** QCG-LVDys AUC **0.911 (0.869–0.953)** versus NT-proBNP **0.637 (0.525–0.749)**, p < 0.001 by DeLong's test. At its own optimal threshold NT-proBNP gave sensitivity 61.1%, specificity 72.0%, PPV 34.4%, NPV 88.5%.

**Scores by group:** median QCG-LVDys 75.8 (IQR 51.5–89.1) in the dysfunction group versus 17.0 (8.3–37.0) without, p < 0.001.

**Subgroups:** AUC held between 0.865 and 0.925 across sex, age above or below 65, septic shock versus not, and prior heart failure.

**Quartile analysis (n = 107, 106, 107, 105):** median ejection fraction fell 63.0 → 60.0 → 55.9 → 40.0. Lactate rose 1.8 → 2.7 → 3.0 → 3.1 (p = 0.002, trend 0.003). 28-day in-hospital mortality rose 8.4% → 16.0% → 19.6% → 25.7% (p = 0.009, trend < 0.001). **qSOFA did not differ (p = 0.740).**

**Mortality model:** adjusted for age, sex, qSOFA, septic shock and creatinine, QCG-LVDys stayed associated with 28-day in-hospital mortality (OR **1.015 per unit**, 95% CI 1.005–1.025, p = 0.004). qSOFA was also independent (OR 1.653); age, sex, shock and creatinine were not.

**What the authors flag themselves:** retrospective design; heavy exclusion with a documented difference between included and excluded patients ("selection bias toward clinically stabilizable patients"); NT-proBNP unadjusted for age and renal function; the 72-hour ECG-to-echo gap, called "a significant limitation"; the AI was not trained on a sepsis-specific dataset; and **no assessment of reproducibility across repeated photographs**.

## 3. How Strong Is This Evidence? (Grade 3/5)

Three out of five. A real multicentre validation of a plausibly useful tool, with a candid limitations section — undercut by a threshold tuned on the test data, a missing number in the abstract, an arithmetic error in the main results table, and manufacturer affiliations without an explicit interests statement.

**What is solid.**

Three hospitals, 425 patients, a reference standard (echocardiography) that is the right one, and scores blinded to the people measuring ejection fraction. The registry was built prospectively by trained nurses with physician verification, which is better than chart-scraping.

The comparison with NT-proBNP was prespecified and used **DeLong's test**, which is the correct choice for comparing two AUCs measured on the same patients. Many papers reach for an unpaired test here and get the uncertainty wrong.

The subgroup analysis is reassuring in the right way: AUC stayed between 0.865 and 0.925 across sex, age, shock status and prior heart failure. A model that holds up across the strata where you would expect ECG changes is a model doing something real.

The quartile analysis uses proper trend tests rather than eyeballing a gradient, and the gradient is clean: ejection fraction falls monotonically and mortality rises from 8.4% to 25.7%. The authors then went further and checked whether the score survived adjustment for the obvious confounders, which it did.

The limitations section is honest and specific. They compared included with excluded patients and reported the differences rather than hiding the funnel. They name the 72-hour window as "a significant limitation." They concede the AI was never trained on sepsis, and that sepsis-induced cardiomyopathy is reversible and may look different from chronic heart failure. They admit no reproducibility testing was done. And the conclusion asks for prospective studies.

**What pulls it down.**

**The threshold was chosen on the same data it was scored on.** "Using the threshold that maximized its Youden index" — 37.35 — on all 425 patients, with nothing held back and no cross-validation. Every threshold-dependent number in the paper is therefore the best achievable on this dataset. This is the exact step yesterday's reading did properly, by selecting thresholds inside training folds only, and the contrast is instructive. The AUC itself is not affected; the sensitivity, specificity, PPV and NPV all are.

**The abstract omits the positive predictive value.** It reports sensitivity 89.6%, specificity 75.1% and NPV 97.5%. PPV is 40.4%, and the paper gives it in the table. Of 149 patients flagged, 89 had normal hearts. Leaving out the one unflattering operating characteristic is a choice.

**The F1 column is computed for the wrong class.** This one is verifiable and exact. F1 combines precision and recall. Using the precision and recall printed in the same row — 40.3% and 89.6% — F1 should be **55.6%**. The table prints **84.9%**. Recomputing with NPV (97.5%) and specificity (75.1%) instead — that is, treating "no dysfunction" as the thing being detected — gives **84.8%**. The same substitution reproduces the other two rows exactly: 86.8% for the SNUBH subset and 79.4% for NT-proBNP, both matching the printed values to the decimal. So three of the table's F1 values describe the model's ability to identify *healthy* hearts, sitting in the same rows as precision and recall describing its ability to identify *sick* ones. The real F1 for the actual task is about 29 points lower than printed.

**Two smaller table inconsistencies.** PPV and precision are the same quantity; the table prints 40.4 and 40.3 in the same row. Sensitivity and recall are the same quantity; the table prints identical point estimates with different upper confidence bounds (97.0 versus 95.5).

**Manufacturer involvement, undeclared in the text retrieved.** Two of eight authors list ARPI Inc., which makes the app. That is not disqualifying — device studies are usually done with the people who built the device — but it belongs in an explicit competing-interests statement, and none appears in the text I could retrieve.

**92.8% of the registry was excluded**, and the authors show the 425 differed systematically: older, more septic shock, more heart failure, yet *better* short-term survival. They correctly describe this as "selectively enriched" and "stable enough to receive echocardiographic evaluation." A patient too unstable for an echo is exactly the patient a bedside screening tool is for, and those patients are absent.

**The comparator was handicapped.** NT-proBNP scored 0.637 against 0.69–0.75 in the prior sepsis literature — the authors note this themselves. It was not adjusted for renal function or age, and chronic kidney disease was three times commoner in the dysfunction group (20.9% versus 7.8%). Kidney disease raises NT-proBNP regardless of the heart. When a comparator underperforms its own published range, the margin over it is partly about the comparator.

**This was not a field test.** ECG images were cropped from the hospital record, displayed on a 24-inch monitor under controlled lighting, and photographed by one specialist at a fixed distance. The discussion nonetheless claims "anyone can use this technology anywhere from emergency scenes to hospital wards." That is the hoped-for use, not what was evaluated — and with no reproducibility analysis, the step from one careful photographer to "anyone" is untested.

**Forty-six patients are missing qSOFA and nobody says so.** The quartile counts sum to 99, 94, 96 and 90 against quartile sizes of 107, 106, 107 and 105. Table 1 agrees: 379 patients have a qSOFA, not 425. So "no significant difference in qSOFA across quartiles" rests on 379, and the mortality model that adjusts for qSOFA almost certainly ran on 379 too. Neither is stated.

**Where 3/5 sits.** The signal looks real: a large AUC, stable across subgroups, with a clean dose-response to lactate and death. What is not established is how the tool performs at a fixed threshold in new patients, how often it can be used by someone other than this one photographer, and whether its margin over a blood test survives a fairer comparison.

## 4. The Editor's Concerns

**Split the data, or cross-validate, before quoting operating characteristics.** My main request. Pick the threshold in one part of the cohort and report sensitivity and specificity in another — or at minimum use cross-validation as the previous paper in this reading list did. As written, 89.6% and 75.1% are the best this dataset can produce, and a reader has no way to know how much of that is real.

**Put the PPV in the abstract.** One number, and it changes how a clinician reads the result: three of every five alarms were false in this cohort. The authors already report it in the table, so this costs nothing.

**Correct the F1 column.** All three values were computed with the negative class as the positive class, while precision and recall in the same rows use the opposite convention. The printed 84.9%, 86.8% and 79.4% reproduce exactly from NPV and specificity; the correct values for detecting dysfunction are roughly 55.6%, 64.6% and 44.0%. The direction of the comparison survives, but the magnitudes do not, and a table that mixes two definitions of "positive" within a single row needs fixing.

**Reconcile PPV with precision, and sensitivity with recall.** Same quantities, different printed values. Small, but they are the kind of thing that makes a reader check everything else — which, in this case, was worth doing.

**Add an explicit funding and competing-interests statement.** Two authors are affiliated with the manufacturer, one of them listing ARPI Inc. first. Readers should not have to infer a commercial interest from an affiliation line.

**Say who could not be included, and what that means for the use case.** The authors do this well in the discussion, but the implication deserves sharpening: the tool is proposed for patients too unstable or too early to get an echo, and those are precisely the patients excluded. The study validates it in the population that did not need it most.

**Give NT-proBNP a fair run.** Adjust for renal function and age, or restrict to patients with preserved kidney function, or at least report the AUC in that subgroup. As it stands, the comparator is measured in a population enriched for the main thing that confounds it, and the study's own authors note it underperformed the literature.

**Test reproducibility.** Have two or three people photograph the same ECGs, on different phones, under different lighting, and report the agreement. The authors list this as a limitation; for a tool whose entire selling point is that "anyone can use it," it is the central missing experiment rather than a footnote.

**Report the qSOFA denominator.** 379 of 425, with 46 unexplained. State the missingness and whether the regression used complete cases.

**Tighten the ECG-to-echo window, and report the distribution.** Up to 72 hours apart, in a condition where cardiac function changes by the hour. The authors flag it; the median and IQR of the actual gap would let a reader judge how much of a problem it was, and that number is not given.

**Smaller notes.** The three sites contributed different years (one just 2018) and have threefold differences in dysfunction prevalence, which is worth a sentence on case-mix. And the headline claim rests on distinguishing an ejection fraction of 40% from 41% — a dichotomy drawn across a continuous measurement that itself carries inter-reader variability of several points.

## 5. Statistics Spotlight

### Concept 1: Sensitivity and specificity belong to the test; PPV and NPV belong to the population

This is the most useful idea in the paper, and the reason its abstract reads better than its data.

**The four numbers, and which way they are read.** Start from the actual counts, which I reconstructed from the reported percentages: of 425 patients, 67 had a weak heart and 358 did not. The app produced **60 true positives, 7 false negatives, 269 true negatives and 89 false positives.**

- **Sensitivity** reads down the *disease* column: of the 67 who were sick, how many did we catch? 60/67 = **89.6%**.
- **Specificity** reads down the other column: of the 358 who were well, how many did we clear? 269/358 = **75.1%**.
- **PPV** reads across the *test result* row: of everyone the test called positive, how many really were? 60/149 = **40.3%**.
- **NPV** reads the other row: of everyone it called negative, how many really were? 269/276 = **97.5%**.

The first pair are properties of the test. Move it to a different hospital with sicker or healthier patients and they stay roughly the same.

The second pair are properties of the test **in that population**. They move with how common the disease is, and they move a lot.

**Watch it move.** Hold sensitivity at 89.6% and specificity at 75.1%, and vary only how common weak hearts are:

- 30% of patients affected → PPV 60.7%, NPV 94.4%
- 15.8% (this study) → PPV 40.3%, NPV 97.5%
- 10% → PPV 28.6%, NPV 98.5%
- 5% → PPV 15.9%, NPV 99.3%
- 2% → PPV 6.8%, NPV 99.7%

Same test, every time. At 2% prevalence, 14 of every 15 alarms would be false.

**An everyday analogy.** A metal detector at an airport is excellent at detecting metal. In a line of travellers it beeps constantly, because nearly all the metal is belt buckles. Its sensitivity has not changed; the population has. Asking "how good is this test?" without asking "in whom?" is asking half a question.

**Why it matters here specifically.** This cohort had 15.8% prevalence, but it is 7.2% of the registry, selected because those patients got an echocardiogram — and people get echocardiograms when someone suspects a heart problem. So the study population is **enriched** for heart disease relative to unselected septic patients. In a less selected population the PPV would fall below 40% and the NPV would climb above 97.5%.

That cuts both ways, and it matters for what the tool is for. If the purpose is "rule out a weak heart so I can give fluid confidently," NPV is the number you need, and it would get *better* in a broader population. If the purpose is "identify the patients to hold fluid from," PPV is the number, and it would get worse. The authors' framing — a high-NPV screening tool — is the defensible one. The abstract's omission of PPV is the part to notice.

**A verification bonus, and a caught error.** F1 is built from precision (another name for PPV) and recall (another name for sensitivity): F1 = 2 × precision × recall ÷ (precision + recall). Plug in this paper's own printed values, 40.3% and 89.6%: 2 × 0.403 × 0.896 ÷ 1.299 = **0.556**, or 55.6%.

The table prints **84.9%**.

Now substitute the mirror-image pair — NPV 97.5% and specificity 75.1%, which are precision and recall *for detecting a normal heart*: 2 × 0.975 × 0.751 ÷ 1.726 = **0.848**. The table says 84.9%. The same substitution reproduces the SNUBH row (86.8%) and the NT-proBNP row (79.4%) exactly.

So the F1 column answers a different question from the columns beside it. It took one formula and three multiplications to find, and it is a good illustration of why recomputing one number from another is worth the minute it costs.

**Watch out.** Any time you see "the test is 97% accurate at ruling out X," ask what fraction of the study population had X. And treat PPV and NPV from a study as applying only to a population with that study's prevalence — which is almost never the population you are standing in.

### Concept 2: Choosing the cut-off on the data you then grade

An AUC describes a score across every possible cut-off. To use a score you must pick one, and how you pick matters.

**The Youden index** is the standard recipe: sensitivity + specificity − 1. It runs from 0 (useless) to 1 (perfect) and picking the cut-off that maximises it finds the point where the two error types are jointly smallest. Here the chosen point gives 0.896 + 0.751 − 1 = **0.647**, at a score of 37.35.

**The problem is where that search was run.** It was run on all 425 patients — the same patients whose sensitivity and specificity are then reported. Nothing was held back.

**Why that inflates things.** The optimal cut-off in any finite sample is partly determined by that sample's noise: which particular patients happened to sit just above or just below. Choose the point that best fits those accidents and you capture some real signal and some luck. On new patients the luck does not repeat, and performance drops.

The giveaway is the precision of the number. A threshold of **37.35** — two decimals on a score that runs 0 to 100 — is not a clinically reasoned boundary. It is the exact point where this dataset's curve happened to peak.

**A worked intuition.** Pick the best-performing day of the week to launch a product by looking back at last year's sales. Tuesdays were strongest, so you launch on a Tuesday and predict Tuesday-sized sales. Some of Tuesday's advantage is real; some is that last year's Tuesdays got lucky. You will not repeat the lucky part. The only way to know how much was real is to try it on a year you did not use to choose.

**What it does and does not affect.** The AUC of 0.901 is threshold-free, so it is unaffected by this. Everything downstream of the cut-off — sensitivity, specificity, PPV, NPV, accuracy, F1 — is optimistic by an unmeasured amount. With 67 positives in the sample, that amount is not trivial.

**The fix, which the previous paper in this reading list used.** Choose the threshold inside a training portion, apply it to a held-out portion, and report from the held-out portion. Those authors did it in nested cross-validation and still called their threshold-dependent figures "secondary descriptive." Same statistic, opposite discipline — and the two papers landed a day apart.

**Watch out.** The phrase to look for is "the optimal threshold," "the cut-off maximising the Youden index," or any cut-off quoted to more decimal places than the measurement deserves. Then ask whether the data used to find it were excluded from the data used to grade it. If the paper does not say, assume they were the same.

### Concept 3: Comparing two tests on the same patients — DeLong's test, and the fair-comparator problem

**What DeLong's test does.** Two tests, same patients, two AUCs: is the difference real? You cannot treat the AUCs as independent, because the same people generated both — a patient who is easy to classify is easy for both tests. DeLong's test accounts for that correlation. Using an unpaired test instead would overstate the uncertainty and make a real difference harder to detect.

This paper used it correctly: 234 patients at SNUBH each had both the app score and an NT-proBNP measurement, AUC 0.911 against 0.637, p < 0.001. That is the right test, and the gap is large enough that no test was really needed to see it.

**Now the harder question: was the comparator given a fair run?** Three things say not quite.

First, **NT-proBNP underperformed its own literature.** The authors note that prior sepsis studies report AUCs of 0.69–0.75; here it managed 0.637. They attribute this to case mix, high rates of renal dysfunction and advanced age — a reasonable explanation, and also an admission that the comparator was measured in conditions that suit it badly.

Second, **it was not adjusted for the things known to distort it.** NT-proBNP rises when kidneys fail, independent of the heart. Chronic kidney disease was present in 20.9% of the dysfunction group versus 7.8% without (p = 0.002). The authors list this as limitation three.

Third, **the comparison covered one of three sites.** The other two used a different assay (BNP), so the head-to-head rests on 234 of the 425.

None of this means the app is not better. It very likely is — a gap from 0.637 to 0.911 is not going to close. But "outperformed NT-proBNP" in this population is a weaker claim than "outperforms NT-proBNP," and the distance between those two sentences is where a careless citation goes wrong.

**The general habit.** When a paper beats a comparator, check how the comparator did against its own published performance. If it underperformed, ask why. Sometimes the answer is that this population is genuinely hard for it — which is useful information. Sometimes it means the comparator was run in a way that did not suit it. Either way, the margin belongs to the comparison, not to the new test alone.

**One more thing worth translating while we are here.** The mortality model reported an odds ratio of **1.015 per unit** of score. That looks like nothing. But the score runs 0 to 100, and the median difference between groups was about 59 points. Compounded across that gap, 1.015^58.8 ≈ **2.4** — roughly two and a half times the odds of death, with the confidence interval running from 1.3 to 4.3. **An odds ratio "per unit" is meaningless until you know how wide a unit is and how much the variable actually varies.**

## 6. Jargon Translator

**Sepsis / septic shock** — A life-threatening reaction to infection where the body's response damages its own organs. Septic shock is sepsis plus dangerously low blood pressure. **Sepsis-3** is the current definition.

**Fluid resuscitation** — Giving intravenous fluid quickly to restore blood pressure and blood flow to the organs.

**Left ventricular ejection fraction (LVEF)** — The share of blood the heart's main pumping chamber pushes out with each beat. Around 55–70% is normal; 40% or below counts as dysfunction here.

**LV dysfunction** — A weak pumping chamber.

**Sepsis-induced cardiomyopathy (SIC)** — Temporary heart weakness caused by sepsis itself, which usually recovers. Different from chronic heart failure, and the authors note the AI was not trained to tell them apart.

**Transthoracic echocardiography (TTE)** — An ultrasound of the heart through the chest wall. The reference standard here.

**NT-proBNP** — A blood protein released when the heart is stretched. Used to screen for heart failure, but it also rises with kidney disease and age.

**12-lead ECG** — The standard heart tracing from ten electrodes giving twelve views of the heart's electrical activity.

**qSOFA** — Quick Sequential Organ Failure Assessment, a 0–3 bedside severity score from blood pressure, breathing rate and mental state.

**Lactate** — A blood chemical that rises when tissues are not getting enough oxygen. A standard severity marker in sepsis.

**Troponin** — A protein released when heart muscle is damaged.

**Digital biomarker** — A measurement derived by software from an ordinary signal — here, a 0–100 score the app computes from an ECG photograph.

**Convolutional neural network** — An image-recognition model that learns visual patterns. Here it reads a photograph of an ECG.

**Encoder / task-specific network** — The encoder turns the image into a compact numerical summary; several smaller networks then each answer one question from that summary.

**Sensitivity** — Of the people who have the condition, the share the test catches.

**Specificity** — Of the people who do not, the share the test correctly clears.

**Positive predictive value (PPV), also called precision** — Of the people the test flags, the share who really have it. Depends on how common the condition is.

**Negative predictive value (NPV)** — Of the people the test clears, the share who really are clear. Also depends on prevalence.

**Recall** — Another name for sensitivity.

**F1 score** — The harmonic mean of precision and recall, combining them into one number. Which class you treat as "positive" changes it completely — the subject of the error found in this paper.

**ROC curve and AUC** — Plotting sensitivity against false alarms at every possible cut-off; the area underneath is the chance the test scores a random affected person above a random unaffected one. 0.5 is a coin flip.

**Youden index** — Sensitivity + specificity − 1. Maximising it is the standard way to pick a cut-off.

**Threshold / cut-off** — The score above which the test says "positive."

**DeLong's test** — A test for whether two AUCs differ, designed for the case where both tests were measured on the same people.

**Prevalence** — How common the condition is in the group being tested.

**Selection bias** — When the people studied differ systematically from the people the test would be used on.

**Retrospective** — Using records of things that already happened.

**Quartiles** — Splitting a group into four equal parts by some score.

**Jonckheere–Terpstra and Cochran–Armitage tests** — Tests for a consistent trend across ordered groups, rather than just any difference.

**Odds ratio** — How much the odds of an outcome change per unit of a predictor. Needs the size of a "unit" to be interpretable.

**Class II medical device** — A regulatory category for moderate-risk devices. Approval means a regulator reviewed it, not that it was proven to improve outcomes.

## 7. What You Can (and Can't) Say

**You CAN say:**
- "In 425 septic patients across three Korean hospitals, an AI app reading a photograph of a 12-lead ECG separated weak from normal hearts with an area under the curve of 0.901."
- "It caught 60 of the 67 patients with an ejection fraction of 40% or below."
- "In the one hospital where both were measured, it clearly outperformed the NT-proBNP blood test — 0.911 versus 0.637 — on a correctly paired statistical comparison."
- "Performance was stable across sex, age, shock status and prior heart failure, with AUCs between 0.865 and 0.925."
- "Higher scores tracked with higher lactate and with 28-day mortality rising from 8.4% in the lowest quartile to 25.7% in the highest."
- "The negative predictive value was 97.5% in this cohort, which supports its proposed use as a rule-out screen."
- "The authors call for prospective studies and flag selection bias, a 72-hour ECG-to-echo gap, and the absence of reproducibility testing."

**You CAN'T say:**
- ❌ "The app is 90% accurate." Accuracy was 77.4%, the AUC of 0.901 is not an accuracy, and all the threshold-based figures come from a cut-off tuned on these same patients.
- ❌ "A positive result means the heart is weak." PPV was 40.4%. Of 149 flagged, 89 had normal hearts.
- ❌ "Sensitivity of 89.6% is what you would get in your hospital." The threshold was chosen to maximise performance on this dataset, with nothing held back.
- ❌ "The F1 score was 84.9%." That figure was computed treating *normal* hearts as the target. For detecting dysfunction it is about 55.6%.
- ❌ "It works in the sickest septic patients." 92.8% of the registry was excluded, and those included were specifically stable enough to get an echocardiogram — the opposite of the patients a bedside tool is for.
- ❌ "Anyone can use this on any phone anywhere." One specialist photographed every ECG off a 24-inch monitor at a fixed distance under controlled lighting, and reproducibility was never tested.
- ❌ "AI beats blood tests for heart failure screening." In this population NT-proBNP scored below its own published range, was not adjusted for the kidney disease that inflates it, and was measured at one of three sites.
- ❌ "This shows the app saves lives or improves fluid management." Nobody's treatment was changed by it. It is a retrospective comparison against echocardiography, not a trial of using it.

## 8. Bottom Line for Your Life

If you or a relative ends up in an emergency department with a severe infection: the fluids they give are usually the right call, and the team already knows that people with heart failure need a gentler approach. What this study points toward is a faster way to spot which patients those are — a photograph of an ECG that is being done anyway. It is not in routine use, it was tested on records rather than at the bedside, and nobody has yet shown that using it changes what happens to patients.

If you work in emergency or critical care: the honest read is that the discrimination looks genuinely good and stable across subgroups, and the rule-out case is the strong one — a negative predictive value of 97.5% in a 16%-prevalence population is useful if what you want is confidence to proceed with fluid. The rule-in case is much weaker, at 40% positive predictive value, and the operating point has not been validated out of sample. The reproducibility question — one photographer, one phone, one lighting condition — is the one I would want answered before anyone relied on it.

For your paper-reading, take three things.

**First, and most reusable: ask who was in the study before you believe a predictive value.** Sensitivity and specificity travel with the test. PPV and NPV travel with the population. The same app, unchanged, would have a PPV near 16% in a population where 5% of patients have weak hearts, and near 61% where 30% do. Whenever a paper tells you how good a test is, your next question is "in whom?" — and here the answer is a cohort that is 7.2% of the registry, picked because someone already thought their heart was worth imaging.

**Second: find out where the cut-off came from.** A threshold of 37.35, found by searching the same 425 patients it is then scored on, is the best this dataset can do rather than a forecast. The tell is a cut-off quoted to more decimal places than the measurement deserves. The paper decoded yesterday did the opposite — chose thresholds inside training folds and then labelled its own operating characteristics "descriptive" — and the two sit a day apart in this list as a matched pair.

**Third, a habit this paper rewards more than most: check who the authors work for, and recompute one number.** Two of the eight list the company that makes the app, and the text retrieved carries no competing-interests statement. That does not make the findings wrong — device studies are nearly always done with the device's makers — but it is a reason to read the numbers rather than the adjectives. Doing that here took one formula and found that three F1 scores in the main results table were computed for the opposite class, inflating them by about 29 points.

None of this means the tool does not work. The AUC is high, the subgroups hold, and the gradient to lactate and mortality is the kind of external coherence that is hard to fake. It means the paper proves less than its abstract implies, which is the ordinary condition of most papers, and the reason to read past the first paragraph.

---

*This is an educational analysis of a published scientific paper, not medical advice. Nothing here is guidance about sepsis, heart failure or any treatment decision. Talk to your own doctors.*
