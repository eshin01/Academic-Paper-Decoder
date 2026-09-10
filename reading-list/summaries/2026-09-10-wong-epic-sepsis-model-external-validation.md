# External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients

- **Authors:** Andrew Wong, Erkin Ötleş, John P. Donnelly, Andrew Krumm, Jeffrey McCullough, Olivia DeTroyer-Cooley, Justin Pestrue, Marie Phillips, Judy Konye, Carleen Penoza, Muhammad Ghous, Karandeep Singh (University of Michigan Medical School and Michigan Medicine)
- **Venue:** JAMA Internal Medicine, 2021;181(8):1065–1070 (published August 1, 2021). An erratum and an invited commentary were published alongside it.
- **DOI link:** https://doi.org/10.1001/jamainternmed.2021.2626
- **PubMed link:** https://pubmed.ncbi.nlm.nih.gov/34152373/ (PMID 34152373)
- **Full-text link:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8218233/ (PubMed Central — the deposit contains the structured abstract and key points; the narrative body was not in the PMC record)
- **Basis:** STRUCTURED ABSTRACT AND KEY POINTS FROM PMC, PLUS VERIFIED FULL-TEXT EXCERPTS retrieved from the open-access version (introduction, methods, and discussion passages quoted inline). Not the complete paper: the supplement, funding details, and competing-interest statements are marked "not reported in the text retrieved." PubMed tags NIH extramural support. Identifiers and editorial notices verified against the live PubMed/NLM record and Scite.
- **Decoded:** 2026-09-10

---

# The Gist

Every paper you have read so far was a research project. This one is about a product **already running in hundreds of American hospitals**, quietly scoring patients for sepsis every 15 minutes inside the medical records software most US hospitals use. Nobody outside the company had ever properly checked whether it worked. A University of Michigan team finally did, across 38,455 hospital stays. The tool performed far worse than its maker reported — and worse in a specific, damning way: it **missed 67% of the patients who actually developed sepsis** while firing alerts on **18% of everyone admitted to the hospital**. Of the sepsis patients whose doctors had already been slow with antibiotics — the patients where an alert could genuinely have helped — it caught 7%.

# Study Snapshot

- **Study type:** Retrospective external validation cohort study — an independent team testing a deployed commercial model on their own patients, against outcomes the model never saw. For "does this deployed product work?", this is the decisive design short of a trial.
- **The tool:** the Epic Sepsis Model, a penalized logistic regression model built into Epic's electronic health record. Epic's software reportedly holds records for roughly **180 million Americans (56% of the population)**. The model was developed by Epic on 405,000 patient encounters across three health systems from 2013 to 2015.
- **Patients (n):** 27,697 adults with **38,455 hospitalizations** at Michigan Medicine, December 2018 to October 2019. 57% women; median age 56 (interquartile range 35–69). **Sepsis occurred in 2,552 hospitalizations (7%).**
- **How sepsis was defined:** a composite requiring either CDC surveillance criteria or diagnostic codes accompanied by two systemic inflammatory response criteria plus one organ-dysfunction criterion within six hours of each other — a deliberately rigorous definition.
- **The headline number:** hospitalization-level **AUC 0.63** (95% CI 0.62–0.64), against Epic's own reported **0.76–0.83** in internal documentation and **0.73** in a conference paper co-authored with Epic.
- **Calibration:** "poor at all time horizons possibly considered by the developer."
- **Missed cases:** the model failed to identify **1,709 of 2,552 sepsis patients (67%)**.
- **Alert burden:** it generated alerts on **6,971 of 38,455 hospitalizations (18%)** — nearly one in five of everyone admitted.
- **Added value over usual care:** it flagged **183 of 2,552 sepsis patients (7%)** who had not already received timely antibiotics — the only group where an alert had anything to add.
- **Funding / conflicts:** not reported in the text retrieved; PubMed tags NIH extramural support.

# How Strong Is This Evidence?

**Grade: 4/5 — the single most consequential study on this reading list, done well, with the limits of any single-site retrospective analysis.**

This is what the previous two review papers said the field was missing, finally performed: an independent group, with no commercial stake, evaluating a widely deployed proprietary product against a rigorous outcome definition on tens of thousands of real hospitalizations. It does not stop at accuracy either — it reports discrimination, **calibration**, incremental value over existing clinical practice, and alert burden. That is all three report cards from the statistical mental map, plus the operational question most papers ignore.

Why not 5/5: it is one academic health system, so a different hospital with different patients and different Epic configuration could see different numbers. It is retrospective, so it measures what the score *would have* flagged rather than what clinicians did with alerts in practice. And the sepsis definition, though carefully constructed, is one reasonable choice among several — a different definition shifts every number somewhat. None of that undermines the central finding, which is far too large a gap to be explained by definitional quibbling.

# The Editor's Concerns

- **The comparison that matters is not "AUC 0.63 is low" but the gap: 0.63 versus the developer's 0.76–0.83.** A model can be mediocre and still useful; a model that performs substantially worse than its vendor claims, in hospitals that bought it on those claims, is a different kind of problem.
- **Missing 67% of cases while alerting on 18% of all patients is close to a worst case.** Those two failures compound: clinicians who see frequent false alarms learn to dismiss them, which means even the correct alerts lose their force. The paper names this directly as alert fatigue.
- **The added value over what doctors already do is 7%.** This is the number that most deserves attention. Doctors were already treating most of these patients appropriately; the model's genuine contribution was confined to a small fraction of cases, which is a much harsher standard than standalone accuracy and the right one for any decision-support tool.
- **Proprietary and unauditable.** The model is commercial and its details are not public — the authors had to work from internal documentation "shared with permission." Hospitals deploying it could not have independently verified it, which is precisely why it ran unchecked at scale for years.
- **Single site, retrospective.** A different health system might configure thresholds differently or serve a different population. And no patient outcomes were measured — this evaluates the score, not what happened when clinicians acted on it.
- **The sepsis definition is a judgment call.** Sepsis has no single agreed operational definition in records data; the authors chose a demanding composite, and a looser one would change the counts.
- **What this study did well:** independent evaluation with no vendor involvement; a large, complete, real-world cohort; a rigorous pre-specified outcome definition; reporting calibration alongside discrimination; measuring incremental value against contemporary practice rather than against nothing; quantifying alert burden in clinical units; and — unusually — explaining *why* their headline AUC differs from the more flattering way the same data could be summarized (below).

# Statistics Spotlight

**1. The optimism gradient — performance falls as independence rises.**
- *What it is:* The reliable pattern that a model's reported accuracy declines the further the evaluators are from the people who built it. Internal testing is most optimistic; a joint publication with the developer is less so; a fully independent external validation is least.
- *How this paper used it:* The three numbers line up almost perfectly along that gradient. Epic's internal documentation: **AUC 0.76–0.83**. A conference paper co-authored with Epic: **0.73**. Independent validation at Michigan: **0.63**.
- *The theory, with an analogy:* Think of a restaurant's own website, a review written in partnership with the restaurant, and an anonymous diner's review. All three describe the same kitchen; they differ in how much of the story survives the telling. There is no need to assume dishonesty at any step — internal evaluations are typically done on data resembling what the model was built from, using definitions the builders chose. Each step outward removes another favourable assumption.
- *Watch out:* When you see a performance figure for any commercial medical tool, the first question is who measured it. "Validated" from a vendor means something different from "externally validated" by an independent group, which means something different again from validated in a randomised trial. This paper is a rare example of all three levels being visible at once — treat that 0.76 → 0.73 → 0.63 sequence as the field's canonical illustration.

**2. Unit of analysis — how the same model can score 0.63 or 0.76 on the same data.**
- *What it is:* Before computing accuracy, you must decide what counts as one observation. Here, is it one *hospitalization* (did this patient's whole stay get flagged appropriately?) or one *prediction* (was this individual 15-minute score correct?). Both are legitimate; they answer different questions.
- *How this paper used it:* At hospitalization level, the AUC was 0.63. Computed by time horizon — treating each prediction separately — it rose to **0.72–0.76**, much closer to the developer's figures. The authors explain why they consider the higher numbers misleading: those AUCs "treat each prediction as independent. Even a small number of bad predictions (ie, high scores that result in alerts in patients without sepsis) can cause alert fatigue, but these bad predictions only minimally affect time horizon–based AUCs."
- *The theory, with a worked example:* Imagine a smoke alarm that chirps falsely twice an hour. Score it per-second and it is correct 99.9% of the time — nearly all seconds are silent and fire-free. Score it per-night, asking "did this alarm wake the household for no reason?" and it fails every night. The seconds-based number is arithmetically true and practically worthless, because what matters is the experience of the household, not the average second.
- *Watch out:* This is one of the most powerful and least visible ways a performance figure can be inflated — no manipulation required, just a choice of denominator. Whenever a monitoring or continuous-scoring system reports an impressive AUC, ask what one row of the data represents: a patient, a stay, or a moment. The unit that matches the clinical decision is the honest one.

**3. Incremental value over usual care — the standard almost no AI study is held to.**
- *What it is:* Not "how accurate is the tool?" but "what does the tool add to what clinicians are already doing?" A tool can be reasonably accurate and still add nothing, if it only flags patients who were already being treated correctly.
- *How this paper used it:* The authors compared the timing of ESM alerts against actual antibiotic administration. Of 2,552 sepsis patients, the model identified **183 (7%)** who had not already received timely antibiotics. Everything else it got right, the clinicians had already got right.
- *The theory, with an analogy:* A weather app that tells you it is raining when you are already holding an umbrella is accurate and useless. Its value lies entirely in the cases where it knows something you do not, early enough to change what you do. Measuring against zero (accuracy alone) flatters every tool; measuring against current practice is the only assessment that predicts benefit.
- *Watch out:* Almost every AI paper on your reading list reports standalone accuracy against a ground truth, and almost none reports incremental value over what clinicians already achieve. When someone cites an impressive accuracy number for a decision-support tool, the sharpest question is: **how many patients would be managed differently, and better, because of it?** Here the honest answer was 7 in every 100 sepsis cases — against an alert firing on nearly one in five of all admissions.

# Jargon Translator

- **Sepsis:** the body's overwhelming, organ-damaging response to infection; a leading cause of hospital death, where speed of antibiotics matters enormously.
- **Electronic health record (EHR):** the hospital's digital chart system. Epic is the largest US vendor.
- **Proprietary model:** an algorithm whose inner workings are commercial secrets, so buyers cannot inspect it.
- **External validation:** testing a model on data from a different source than the one it was built on, by people other than its builders.
- **Penalized logistic regression:** a classical statistical model — notably *not* deep learning. Not everything called "AI" in a hospital is a neural network.
- **AUC (area under the receiver operating characteristic curve):** how well a score ranks patients who will develop the condition above those who will not; 0.5 is a coin flip, 1.0 is perfect. **0.63 is weak.**
- **Calibration:** whether the predicted risks are numerically honest — a "20% risk" group should have events about 20% of the time.
- **Alert fatigue:** the well-documented phenomenon of clinicians ignoring alarms that cry wolf too often.
- **Number needed to evaluate:** how many patients staff must assess per true case found — the workload cost of a screening alert.
- **Timely administration of antibiotics:** giving antibiotics within the recommended window, the main action a sepsis alert is meant to trigger.

# What You Can (and Can't) Say

**Fair to say:**
- "An independent 2021 external validation of the Epic Sepsis Model, deployed at hundreds of US hospitals, found an AUC of 0.63 versus the 0.76–0.83 reported by its developer."
- "It missed 67% of sepsis cases while alerting on 18% of all hospitalizations, and added value over existing clinical practice in only 7% of sepsis patients."
- "Calibration was poor at all time horizons, and the model is a proprietary product that buyers could not independently audit."
- "The authors concluded its widespread adoption despite poor performance raises fundamental concerns about sepsis management nationally."

**Not fair to say:**
- "AI in hospitals doesn't work" — this is one specific commercial model, and a penalized logistic regression rather than modern deep learning. It is evidence about *this product* and about *unaudited deployment*, not about medical AI as a category.
- "The model harmed patients" — no patient outcomes were measured; the study evaluates the score's accuracy and alert burden, not deaths or complications.
- "Epic lied about performance" — the study documents a gap between internal and independent evaluation, which is the expected direction and does not by itself imply deception.
- "This applies to every hospital" — one academic health system, one Epic configuration, one sepsis definition.

# Bottom Line for Your Life

This is the paper that closes the loop on everything you have read this fortnight. The reviews said the field publishes optimistic, unaudited, rarely-externally-validated claims. This shows what happens when that culture reaches the bedside: a tool scoring millions of patients across hundreds of hospitals, for years, that nobody outside its maker had checked — and that, when finally checked, missed two-thirds of the cases it existed to catch while interrupting clinicians about one in five patients. The generalisable lesson is not "distrust AI." It is that **deployment is not validation**, and the three questions worth carrying anywhere are: who measured this, what did it add to what people were already doing, and can anyone outside the vendor check the answer? If you are a patient, nothing here calls for alarm about your care — sepsis alerts are one input among many, and clinicians were already catching most cases without them, which is exactly what this study found. One study is one data point, and this one is a data point about how much can ride on studies nobody performed. This is an educational breakdown, not medical advice.

---

**Sources** (based on articles retrieved from PubMed / PubMed Central, with full-text excerpts from the open-access version via Scite; identifiers and editorial notices verified against the live NLM record — URL browsing is blocked in this environment, so links are constructed from those verified records):
- DOI: https://doi.org/10.1001/jamainternmed.2021.2626
- PubMed: https://pubmed.ncbi.nlm.nih.gov/34152373/
- PubMed Central record: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8218233/
- Erratum (2021): https://doi.org/10.1001/jamainternmed.2021.3907
- Invited commentary (2021): https://doi.org/10.1001/jamainternmed.2021.3333
