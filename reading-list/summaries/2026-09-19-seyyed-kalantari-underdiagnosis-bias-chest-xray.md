# Underdiagnosis bias of artificial intelligence algorithms applied to chest radiographs in under-served patient populations

- **Authors:** Laleh Seyyed-Kalantari (University of Toronto and Vector Institute), Haoran Zhang, Matthew B. A. McDermott, Irene Y. Chen (Massachusetts Institute of Technology), Marzyeh Ghassemi (Vector Institute and MIT) — 5 authors
- **Venue:** Nature Medicine, 2021;27(12):2176–2182 (published December 10, 2021)
- **DOI link:** https://doi.org/10.1038/s41591-021-01595-0
- **PubMed link:** https://pubmed.ncbi.nlm.nih.gov/34893776/ (PMID 34893776)
- **Full-text link used:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8674135/ (PubMed Central, open access)
- **Basis:** FULL TEXT — main text, all results sections, the complete discussion, and the full Methods including dataset construction, fairness-metric definitions, preprocessing, and training protocol were read from the open-access PubMed Central copy. **An important limitation of this decode:** every specific underdiagnosis percentage in this paper lives in its figures and supplementary tables, which were not retrieved. This analysis therefore reports the paper's stated directions, comparisons, and mechanisms, and the dataset and training numbers that appear in the running text, but quotes no underdiagnosis rate, because none was available to quote. Where a figure would have supplied a number, that is said rather than guessed. Funding and competing-interest statements are pointed to by the article but were not in the retrieved text; PubMed tags the work as non-US-government research support. Identifiers verified against the live PubMed/NLM record; direct URL browsing is blocked in this environment, so links are constructed from that verified record.
- **Decoded:** 2026-09-19

---

# The Gist

Imagine a hospital uses software to sort chest X-rays, so that patients the software calls healthy wait longer for a doctor. Now imagine the software is more likely to call you healthy when you are not, if you happen to be female, young, Black, Hispanic, or on Medicaid. That is what this team found, across three of the largest public chest X-ray collections in the world and a fourth built by combining them — 707,626 images from 129,819 patients. The models were not sloppy; they performed at or near the best published results. And the researchers never told the models anyone's race, sex, age, or insurance. The bias came out anyway. The most damning detail is a piece of statistical detective work: if the models were simply noisier for these groups, they would make *both* kinds of mistake more often. Instead the errors pointed one way. The models were not confused about under-served patients. They were systematically leaning toward calling them well.

# Study Snapshot

- **Study type:** A retrospective audit of trained models across four dataset settings. No patients were treated, no system was deployed, and no clinical outcome was measured. The subject is software behaviour.
- **The specific harm being measured:** underdiagnosis — the model saying "nothing wrong here" about a patient who does have a finding. The authors argue this is worse than a wrong diagnosis, because a misdiagnosed patient still enters the system and a clinician can correct course, whereas an underdiagnosed patient is sent away.
- **How it was measured:** each dataset carries a "no finding" label meaning none of the listed diseases is present. The underdiagnosis rate is how often the model applies that label to someone who actually has a finding.
- **The data — four settings:**
  - MIMIC-CXR, from Beth Israel Deaconess Medical Center in Boston, 2011 to 2016: 371,858 images from 65,079 patients.
  - CheXpert, from Stanford Hospital, October 2002 to July 2017: 223,648 images from 64,740 patients.
  - ChestX-ray14, from the NIH Clinical Center, 1992 to 2015: 112,120 images from 30,805 patients.
  - A combined set of all three on their shared labels: 707,626 images from 129,819 patients.
- **Only one dataset records race or income.** The Boston dataset reports race, ethnicity, and insurance type; the other two report only sex and age. Insurance type is used as a rough stand-in for income, on the reasoning that Medicaid patients are often in the low-income bracket.
- **The model:** a 121-layer DenseNet started from general photograph training, images resized to 256 by 256 pixels, trained with standard settings and early stopping. **The protected characteristics were never given to the model.** Only the image went in.
- **Each result is an average of five models.** Every dataset was trained five times with different random starting points, and the reported figures are the mean of those five with a 95% confidence interval. The data splits were held fixed, and no patient appeared in more than one split.
- **The models were good.** The authors state their classifiers were at or near the best published performance on these datasets, so the finding is not an artifact of a weak model.
- **The core result:** in the Boston dataset, female patients, patients under 20, Black patients, Hispanic patients, and Medicaid patients were all underdiagnosed at higher rates than the comparison groups. The specific rates appear only in figures not retrieved for this analysis.
- **It replicated.** The same pattern — female and younger patients underdiagnosed most — held in the Stanford dataset and the combined dataset.
- **One dataset broke the pattern, and the authors say so.** In the NIH data, male patients and patients over 80 had the highest underdiagnosis rates. The authors offer possible reasons: that dataset's over-80 test group contained only **37** relevant samples, it holds only frontal images, its labels were made differently, and it comes from a research hospital that, in the authors' quoted description, admits patients selectively because they have an illness being studied.
- **Belonging to two under-served groups was generally worse.** Hispanic female patients were underdiagnosed more than white female patients. The heaviest rates fell on patients who were both young and female, both young and Black, and both young and on Medicaid. The authors note the effect was not consistently worst in the very smallest intersectional groups.
- **The mistakes pointed in one direction.** Across datasets, the rate of wrongly calling someone healthy and the rate of wrongly calling someone sick moved *inversely* for these groups. That is the paper's central piece of evidence, and the next section explains why it matters so much.
- **Which diseases got missed differed too.** Underdiagnosed patients were proportionally more likely to have a lung lesion and less likely to have fluid around the lung, suggesting some findings are simply harder to detect than others.
- **A different fairness measure flipped the pattern.** When the authors measured something else — how often a "no finding" call turns out to be wrong — the disparities favoured female over male patients and younger over older. Same models, same data, opposite conclusion about who is disadvantaged.
- **Funding / conflicts:** not present in the retrieved text.

# How Strong Is This Evidence?

**Grade: 4/5 — a large, replicated audit with a genuinely clever test separating directional bias from ordinary error, honest about the one dataset that disagreed and about the contaminated ground truth underneath the whole exercise.**

Several things make this stronger than most fairness audits. It spans three independently collected datasets from three different institutions plus a combined one, so a quirk of any single hospital cannot explain the result. Every number is the average of five separately trained models with confidence intervals, so a lucky or unlucky training run cannot explain it either. The models were state of the art, which forecloses the easy dismissal that someone built a bad classifier. The protected characteristics were never inputs, which forecloses the other easy dismissal that the model was simply told whom to disfavour.

And then there is the inverse-error-rate test, which is the intellectual core of the paper. Establishing that a model performs worse for a group is easy and weak. Establishing that its errors run in a *particular direction* for that group is much harder and much more damning. They did the second thing.

What holds it at 4 is a problem the authors raise themselves and cannot solve. The labels these models learn from were extracted by software reading clinical notes — and clinicians already underdiagnose these same populations. So the "correct answers" the model is graded against are themselves shaped by the bias under study. The authors are explicit that this is bias amplification and that their labels are "not an unbiased ground truth." That candour is admirable and it means the study cannot cleanly separate how much bias the algorithm *added* from how much it *inherited*. Add that race and insurance were recorded only for intensive-care patients in the Boston dataset — leaving roughly 100,000 X-rays without that information and making the race analysis a study of a sicker, selected subgroup — and nothing here was deployed or checked against what happened to any patient.

# The Editor's Concerns

- **The ground truth carries the bias being measured.** Labels came from software reading radiology reports written by clinicians who, as the paper documents, already underdiagnose these populations. A model trained on those labels and then graded against them is being measured with a contaminated ruler. The authors name this and argue it is still alarming — the model may fail on patients clinicians got right — but the study cannot quantify the split.
- **Race and income data exist only for intensive-care patients.** In the Boston dataset, race, ethnicity, and insurance were recorded only when a patient was admitted to intensive care, leaving around 100,000 X-rays without them. So every race and insurance finding comes from a subset selected for being critically ill, not from the general population getting chest X-rays.
- **One of four settings contradicted the main result.** In the NIH data the disadvantaged groups were male and over-80 patients. The authors list plausible reasons and do not resolve it. Read this as a finding that replicates in three of four settings, with an unexplained exception.
- **Some subgroup cells are tiny.** The over-80 group in the NIH test set had 37 relevant samples. Rates computed on numbers like that are extremely unstable, which is part of why that dataset behaves oddly.
- **The specific magnitudes are not in the text.** Every underdiagnosis percentage lives in figures and supplementary tables. From the article's running text alone, a reader learns the direction and consistency of the effect but not its size — and size is what determines whether this is a clinical catastrophe or a measurable tilt. This decode could not retrieve those figures, and none has been invented here.
- **A different fairness measure reverses who is disadvantaged.** The authors report that on a different metric the disparities favoured women and younger patients. They explain why — it follows from different disease rates between groups — and that explanation is sound. But it means "this model is biased against group X" is not a property of the model alone. It is a property of the model plus the measure you chose.
- **A numeric inconsistency in the text.** The results section says the NIH dataset has "only seven of the shared disease labels instead of 14," while the Methods say "only eight labels of the NIH dataset are matched." Small, and the sort of thing a careful reader notices.
- **No deployment, no outcomes.** This measures what software does to labels in a database. Whether any real patient waited longer for care is outside the study, and the triage scenario driving the paper's urgency is hypothetical.
- **Generalisability is bounded, as stated.** The authors write that their results may not replicate where racial dynamics differ or where health insurance works differently, which rules out most of the world's health systems.
- **What this study did well:** used three independently collected datasets plus a combined one rather than a single source; trained five models per setting with different random seeds and reported confidence intervals; verified their classifiers matched published state of the art so a weak model could not explain the result; never fed protected attributes to the models; devised the inverse-error-rate test to distinguish directional bias from noise; analysed intersectional groups and reported that the smallest groups were not consistently worst, rather than overclaiming; reported the dataset that disagreed and attempted to explain it; reported a second fairness metric that flipped the story; and devoted a long section to why the obvious technical fix — different alarm thresholds per group — is a bad idea.

# Statistics Spotlight

**1. Two kinds of error, and why their direction is the whole argument.**
- *What they are:* Any yes-or-no test makes two distinct mistakes. It can say "healthy" about someone sick, and it can say "sick" about someone healthy. In this paper the first is the underdiagnosis rate and the second is its mirror. Crucially, these are separate quantities that can move independently.
- *How this paper used it:* They measured both, for every subgroup, in every dataset. If a model were merely *unreliable* for Black patients or female patients — poorer image quality, fewer training examples, whatever — you would expect both error types to rise together, because noise scatters in all directions. That is not what happened. The two rates moved **inversely**: as wrongly-called-healthy went up for a group, wrongly-called-sick went down. The finding held across the datasets, with the NIH exceptions noted.
- *The theory, with a worked example:* Picture two broken bathroom scales. The first is just noisy: weigh yourself ten times and it reads five pounds high, then six pounds low, then four high. Its errors are large and scattered. The second is quietly biased: every reading is four pounds light. Take a single measurement and both scales look equally wrong. Take many, and they separate completely — the noisy scale's errors cancel around the truth, the biased scale's do not. Now apply that here. A noisy model would be "confused" about under-served patients, flagging some wrongly as sick and some wrongly as healthy. A biased model has its thumb on one side of the scale. The inverse relationship is the fingerprint of the thumb.
- *Watch out:* Nearly every report of algorithmic unfairness stops at "accuracy was lower for group X," which is compatible with both stories and tells you nothing about which. When you read that a model performs worse for some population, the question that separates a fixable data problem from a harmful systematic tilt is: **worse in which direction?** Ask for both error rates broken out by group. If a paper reports only overall accuracy per group, it has not answered the question that matters.

**2. One threshold for everybody — and why that alone produces unequal errors.**
- *What it is:* These models do not output "sick" or "healthy." They output a number, a score. Somebody has to pick a cutoff that turns that score into a decision. This paper chose a single cutoff applied to every patient, selected to give the best overall balance of catching cases and avoiding false alarms.
- *How this paper used it:* One threshold, all groups, chosen by optimising a standard combined measure of precision and recall across the whole population. The authors note this follows best practice. They then spend a long passage explaining why the obvious alternative — a different cutoff for each group — is worse than it sounds.
- *The theory, with a worked example:* Imagine two groups whose score distributions sit slightly differently, for any of a dozen innocent reasons: different disease rates, different body sizes, different scanners, different documentation habits. Now drop one horizontal line across both. Wherever that line falls, it will cut the two distributions at different points, so the two groups end up with different error rates automatically. The single threshold did not create the difference in the underlying scores, but it converts that difference into unequal treatment at the moment of decision. This is why a model can look even-handed on a ranking measure and be lopsided on the decisions it actually produces.
- *Watch out:* The authors' argument against per-group thresholds is worth carrying. First, the number of thresholds you need grows explosively as you add characteristics, so it becomes impossible past two or three. Second, small intersectional groups do not have enough patients to estimate a stable threshold. Third — and this is the deep one — race and ethnicity are partly social categories with fuzzy edges, self-reported inconsistently, so a system that adjusts its behaviour by race requires knowing each patient's race and treating that label as solid. Fourth, in some cases equalising the errors would require deliberately making the model *worse* for one group. So when someone says an algorithm's fairness problem is easily fixed by recalibrating per group, that fix carries all four of these costs.

**3. Fairness definitions that cannot all be satisfied at once.**
- *What it is:* There are several reasonable, mutually incompatible definitions of a fair algorithm. Equal rates of wrongly calling people healthy. Equal rates of wrongly calling people sick. Equal reliability of a given prediction across groups. Mathematicians have proved that when two groups have different underlying disease rates, you cannot have all of these simultaneously unless the model is perfect.
- *How this paper used it:* Directly, and on their own results. Measuring underdiagnosis, the disadvantaged groups were female, young, Black, Hispanic, and Medicaid patients. Measuring a different quantity — how often a "no finding" verdict is actually wrong — the disparities ran the other way, favouring female over male and younger over older. The authors explain the mechanism: there are far fewer sick people in the 0–20 age group, and that difference in underlying rates mechanically shifts the second measure. Same models. Same predictions. Opposite answer to "who is being failed."
- *The theory, with an analogy:* Think of a school deciding what a fair admissions test looks like. Equal pass rates across neighbourhoods? Equal accuracy at identifying students who will succeed? Equal likelihood that a passing student actually succeeds? Each sounds fair. When the neighbourhoods differ in preparation, achieving one forces you to give up another. There is no configuration that satisfies all three. The choice is therefore not a technical one; it is a decision about which harm you care most about preventing, and it has to be argued rather than computed. This paper argues explicitly for prioritising underdiagnosis, on the grounds that a patient sent home untreated has no second chance to be caught.
- *Watch out:* This is the sharpest practical takeaway on the whole reading list for evaluating any claim about algorithmic fairness. "Our system was tested for bias and passed" is close to meaningless on its own. The follow-up is: **fair by which definition, and what did that choice cost on the other definitions?** A vendor can always find a measure their system passes. The Obermeyer paper on your list made the same point from the other direction; this one demonstrates it inside a single set of results.

# Jargon Translator

- **Chest radiograph / chest X-ray (CXR):** the standard image of the lungs and chest.
- **Underdiagnosis:** the model saying a patient is healthy when they are not. The subject of this paper.
- **Overdiagnosis:** the opposite mistake — flagging disease in a healthy patient.
- **"No finding" label:** the tag meaning none of the listed diseases is present. The paper measures how often that tag is applied wrongly.
- **False positive rate / false negative rate:** the two error types. In this paper's framing, applied to the "no finding" label, the first is underdiagnosis and the second is overdiagnosis.
- **Triage:** sorting patients by urgency. The scenario that makes underdiagnosis dangerous, since a patient labelled healthy waits longer.
- **Intersectional subgroup:** people belonging to two under-served categories at once, such as Black female patients.
- **Protected attribute:** a characteristic such as race, sex, or age that should not drive a decision. None was given to the models here.
- **Proxy variable:** a stand-in for something you cannot measure directly. Insurance type stands in for income here.
- **Bias amplification:** when a model trained on biased records produces outputs more biased than the records were.
- **Threshold:** the cutoff that turns a model's continuous score into a yes-or-no decision.
- **F1 score:** a combined measure of how many real cases you catch and how many of your alarms are genuine, used here to pick the threshold.
- **AUC:** a ranking score from 0.5 (coin flip) to 1.0 (perfect).
- **DenseNet-121:** the specific network design used, the same family as in several earlier entries on this list.
- **Random seed:** the arbitrary starting number for a training run. Five different seeds were used per dataset, and results were averaged.
- **Natural language processing (NLP) labeler:** software that reads radiologists' written reports to decide which findings were present. It generated the labels here, and the paper argues it should be audited for bias.
- **Fairness impossibility theorem:** the proof that several reasonable definitions of fairness cannot all hold at once when groups have different underlying rates.
- **MIMIC-CXR / CheXpert / ChestX-ray14:** the three large public chest X-ray collections used, from Boston, Stanford, and the NIH respectively.

# What You Can (and Can't) Say

**Fair to say:**
- "A 2021 Nature Medicine study of 707,626 chest X-rays found that state-of-the-art AI classifiers underdiagnosed female, younger, Black, Hispanic, and Medicaid patients at higher rates than comparison groups."
- "The pattern held across three separately collected datasets and a combined one, with one dataset showing a different pattern that the authors report and attempt to explain."
- "The models were never given patients' race, sex, age, or insurance — only the image."
- "Patients in two under-served groups at once, such as Hispanic female patients, were generally underdiagnosed more than either group alone."
- "The errors ran in one direction rather than scattering, which the authors argue shows systematic bias rather than the model simply being noisier for these patients."
- "The authors state their labels come from clinical records that already contain human underdiagnosis bias, making this bias amplification rather than bias created from nothing."

**Not fair to say:**
- "The AI is racist because it uses race" — it never saw race. The bias emerged from images and labels alone, which is precisely what makes the finding important.
- "AI underdiagnoses Black patients by X%" — the specific rates are in the paper's figures, which this analysis could not retrieve. Do not attach a number to this claim without opening the figures.
- "This proves patients were harmed" — nothing was deployed. No patient's care was delayed by these models in this study.
- "The problem is fixable by adjusting thresholds per group" — the authors devote a section to why that fails, including that it requires treating race as a fixed, known, reliably reported category.
- "The algorithm is unfair, full stop" — the authors show that a different fairness measure reverses which groups appear disadvantaged. Their argument for prioritising underdiagnosis is reasoned, not automatic.
- "This happens regardless of the dataset" — three of four settings showed the pattern. The fourth did not, and the reason is not settled.

# Bottom Line for Your Life

The single most useful fact here is that nobody told these models anyone's race. Every protected characteristic was withheld. The bias came out anyway, from the pictures and the labels.

That kills the most common defence you will hear about any automated system, in medicine or lending or hiring: "it doesn't use race, so it can't be racially biased." The Obermeyer paper on your list showed one route around that — a model that predicts costs instead of needs inherits the inequality in who gets spent on. This paper shows another. Feed a model records written by people who already miss things in certain patients, and it learns to miss them too, then does it more consistently than any individual clinician would.

The second thing to carry is the question that made this paper work. Not "does it perform worse for this group" but **"worse in which direction?"** Errors that scatter randomly are a quality problem. Errors that lean one way are something else. Almost no reporting on algorithmic fairness makes that distinction, and it is the difference between a system that needs better data and a system that quietly sends particular people home.

Third: when someone tells you an algorithm has been checked for bias, ask which definition they checked. This paper's own results flip depending on the measure, and the authors are upfront that no system can satisfy every definition at once. That is a proven mathematical fact, not a dodge — which is exactly why "we tested for fairness" means nothing without naming the test.

For your own care, this changes nothing directly. No hospital in this study used these models on anyone. But if you are ever told an AI tool read your scan and found nothing, it is reasonable to treat that as one input rather than a verdict, and to say so if your symptoms disagree. One study is one data point. This is an educational breakdown, not medical advice.

---

**Sources** (based on articles retrieved from PubMed and PubMed Central; identifiers verified against the live PubMed/NLM record — URL browsing is blocked in this environment, so links are constructed from that verified record):
- DOI: https://doi.org/10.1038/s41591-021-01595-0
- PubMed: https://pubmed.ncbi.nlm.nih.gov/34893776/ (PMID 34893776)
- Full text (PMC, open access): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8674135/

**A note on what this decode could not read.** The paper's specific underdiagnosis rates are presented in figures and supplementary tables rather than in the running text, and those were not retrieved here. Everything above reflects the article's own stated findings, directions, and mechanisms, plus the dataset and training numbers that do appear in the text. No underdiagnosis percentage has been quoted or estimated. Opening the paper's figures would add the magnitudes.
