# Automated Calculation of the Pediatric Emergency Care Applied Research Network (PECARN) Intra-Abdominal Injury Rule from Unstructured Emergency Department Notes Using a Large Language Model

**Authors:** Devisetti L, Chen B, Addo N, Narang K, Alvarez C, Kornak J, Singh C, Kornblith AE (eight authors — UCSF Department of Emergency Medicine, UCSF Department of Epidemiology and Biostatistics, UCSF Bakar Computational Health Sciences Institute, UC Berkeley EECS, and Voyage AI)
**Journal:** Journal of the American College of Emergency Physicians Open, 2026; 7(6): 100525 (published 8 October 2026)
**Decoded:** 2026-10-29
**Analysis basis:** **FULL TEXT** (retrieved from PubMed Central, PMC13676203). The complete body was read, including the Bottom Line box, Methods, Results, Limitations, Discussion, ethics declarations, funding and conflict-of-interest statements. **Two things are not in the retrieved text and are flagged throughout:** the per-variable performance table (so individual variable accuracies cannot be quoted), and the names of the predictor variables in the discordance breakdown, which the text extraction stripped out.

**Source links (verified):**
- DOI: https://doi.org/10.1016/j.acepjo.2026.100525
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42893265/
- Full text (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC13676203/

**Basis of link verification.** Direct URL fetching is blocked from this session (`doi.org` does not resolve under the network policy here). Verification was done against the live PubMed/NLM record: a query for PMID 42893265 returned this exact title, these eight authors, J Am Coll Emerg Physicians Open volume 7 issue 6 article 100525, DOI `10.1016/j.acepjo.2026.100525` and PMC ID `PMC13676203`; the full text was then retrieved from PubMed Central by that PMC ID and matches. Both halves of the chain were confirmed independently.

**Funding: reported.** NIH Eunice Kennedy Shriver National Institute of Child Health and Human Development, award K23HD110716.
**Competing interests: reported.** "AEK and NA are co-founders and consultants to CaptureDx," with a statement that the entity had no role in design, planning, execution or interpretation. All other authors declare none.
**Reporting guidelines: TRIPOD-LLM and STROBE, both named.** The first paper in this reading list to report under **TRIPOD-LLM** — the large-language-model extension of TRIPOD, published specifically because ordinary prediction-model reporting items do not cover prompts, model versions, sampling parameters or inference runs.

**Ethics:** approved as exempt by the UCSF Institutional Review Board (approval 25-43740), with a waiver of informed consent and parental permission. The waiver reasoning is spelled out in full — retrospective, no intervention, no patient contact, minimal risk, consent from every family impracticable for encounters already past, data de-identified before analysis and held on secure institutional servers.

> **Why this paper today.** All four deferred papers were re-checked this morning and all four are still blocked; the JAMA OpenEvidence study (PMID 42879271, PMC13673371) reached **day 14** of serving an empty PMC body, though its structured abstract is now complete and is summarised at the end of this file for the record. This was spare #1 from yesterday's restock, picked ahead of the other five for one reason: it carries a **weighted Cohen's kappa**, and in sixty decoded papers this list has never taught a reliability statistic. It turned out to carry something better as well — six published percentages from which the entire confusion matrix, and the confidence-interval method the paper never names, can be recovered by arithmetic.

---

## 1. The Gist

A child is brought to the emergency department after a car crash or a fall. The question is whether to order a CT scan of the abdomen. A scan finds internal injuries; it also delivers a dose of radiation to a child, which carries a small lifetime cancer risk. So there is a published rule — the PECARN intra-abdominal injury rule — that uses seven findings a doctor can check at the bedside to identify children at *very low risk*, who can safely skip the scan.

Knowing whether doctors actually follow that rule means reading their notes. Thousands of them, by hand, one at a time. It is slow, expensive, and two reviewers reading the same note often disagree.

Eight researchers at UCSF asked whether a large language model could do that reading. They took **196 children** seen after blunt abdominal trauma at two UCSF-affiliated paediatric emergency departments, had two clinicians read every physician note and work out each child's PECARN risk score by hand, then gave the same notes to OpenAI's o1 model and compared.

The model agreed with the clinicians on **187 of the 196 children — 95.4%**. Across the eight individual findings it had to pull out of the text, it produced **1,568 labels and got 23 wrong — 1.47%**. It took **two hours** for all 196 notes, about 37 seconds each.

That is a good result for a genuinely useful and unglamorous job. And the paper says so in exactly those terms: it is for quality review and research, not for bedside decisions, and it needs testing somewhere else first.

Three things are worth knowing before you take the 95.4% at face value.

**The model was chosen, and the instructions were rewritten, using the same 196 notes the score comes from.** Three models were tried and the best kept. The prompt went through two rounds of revision after the team looked at where it was disagreeing. There is no separate set of notes that was never touched. Everything reported is a best-case number.

**The clinicians who set the correct answers could see what the model had said.** The paper puts this first in its own limitations.

**The confidence intervals understate the uncertainty, in the same direction, for every single metric.** Two of them run past 100% and have been clipped. That is recoverable from the published numbers, and Section 5 does it.

## 2. Study Snapshot

**Study type:** a **retrospective secondary analysis** comparing an automated text-extraction method against a clinician-derived reference standard. It is not a diagnostic accuracy study of PECARN itself, and it is not a clinical trial. The thing being measured is **agreement between a model and a human reading the same document.**

**Where:** two UCSF-affiliated academic paediatric emergency departments — an urban tertiary/quaternary referral centre (~25,000 annual visits) and a Level 1 paediatric trauma centre (~45,000 annual visits). The paper states plainly that the two **share an electronic health record instance, share semistructured documentation templates, and share some of the same physicians.** In the Discussion the authors call the work "a retrospective single-system study," which is the honest description.

**When:** children meeting local trauma activation criteria, March 2018 to January 2021.

**Who:** a random sample of 198 records of children aged 18 or under presenting after blunt abdominal trauma who received a FAST ultrasound. Penetrating injuries excluded; two children excluded for missing notes. **Final cohort 196** — 112 boys, 84 girls, mean age 7.8 years (SD 5.3, range 0 to 18).

**Outcome prevalence, and this matters:** **4 children (2.0%) had an intra-abdominal injury. One (0.5%) required acute intervention.**

**The reference standard:** two clinicians independently read each physician ED note and marked each PECARN predictor as positive, negative or missing against prespecified criteria. Disagreements were resolved by a third physician-investigator. **Missing predictors were then counted as negative**, on the reasoning that undocumented findings are more often absent than present.

**The model:** three were tried — GPT-4o-mini (`gpt-4o-mini-2024-07-18`), GPT-4.1 (`gpt-4.1-2025-04-14`) and OpenAI o1 (`o1-2024-12-17`, medium reasoning effort). Exact version strings are given, which is good practice and rare. **Default sampling parameters, temperature 1.0, no seed set, one inference run per note.** o1 was kept because it scored highest at the predictor-variable level. Zero-shot prompting with function calls for structured output; the prompt defined each predictor and asked for a positive/negative classification from the text alone. Median note length 845 words, all sections supplied, no empty notes.

**Headline results, model against clinician:**
- Accuracy **95.4%** (95% CI 92.5 to 98.3)
- Sensitivity **94.4%** (90.6 to 98.2)
- Specificity **98.2%** (94.6 to 100)
- Positive predictive value **99.3%** (97.8 to 100)
- Negative predictive value **86.9%** (78.4 to 95.4)
- F1 score **0.97** (0.90 to 0.98)
- Weighted Cohen's kappa on the three-category score **0.96** (0.92 to 1.00)
- **1,568 labels, 23 discordant (1.47%)**, with 11 of the 23 concentrated in a single variable
- Two hours for 196 encounters

**The reconstructed confusion matrix** (derived in Section 5, and it reproduces all five percentages and all five confidence intervals exactly): of 196 children, the clinicians judged **142 not-very-low-risk and 54 very-low-risk**. The model agreed on **134** of the 142 and **53** of the 54. It called **8** children very low risk whom the clinicians did not, and **1** child not-very-low-risk whom the clinicians cleared.

**The two errors that matter:** in both cases where the clinician scored a child **high risk** and the model scored them **very low risk**, the model had missed abdominal wall trauma. Neither child turned out to have an injury.

## 3. How Strong Is This Evidence? (Grade 3/5)

**This is the first 3 out of 5 in this list without external validation, and the reason is worth stating because it is a change in how the grade is being applied, not a lapse.**

The grade asks how much a reader should update. That depends on the size of the claim as well as the size of the study. Yesterday's paper claimed a clinical prediction model from 127 patients and 61 events, and 61 events cannot support one — hence 2 out of 5. This paper claims that a text-extraction task can be automated for research use, and the unit it is claiming about is **not the patient, it is the label**. There are **1,568 labels** here, every one of the 23 errors was individually reviewed and categorised, and the conclusion the authors draw is bounded to precisely that. **The evidence and the claim are the same size.** That is what a 3 means.

**What earns it:**

**Reported under TRIPOD-LLM and STROBE, both named.** TRIPOD-LLM exists because ordinary prediction-model reporting does not cover the things that determine whether a language-model result is reproducible. This paper reports them: exact model version strings for all three models tried, the reasoning-effort setting, the sampling parameters, the number of inference runs, the prompting strategy, the median input length, and the prompts themselves in a supplement.

**A genuine two-reader reference standard with third-party adjudication**, and prespecified criteria for each predictor.

**Funding and conflicts disclosed, including the uncomfortable one** — two authors are co-founders of a company in the adjacent space, named, with a statement of non-involvement.

**A complete qualitative error analysis.** All 23 discordant labels were reviewed and the failure modes described: missing quantitative detail for dangerous mechanisms, unrecognised anatomical descriptors, non-standard phrasing, pain attributed to non-traumatic causes, conflicting documentation. This is more useful than the accuracy figure.

**The conclusion is scoped correctly and repeated.** Quality improvement and research; "larger external validation is needed before use to guide bedside imaging decisions"; "future work should validate this LLM-based approach prospectively with greater outcome prevalence across institutions before implementing clinician-facing applications." The paper does not claim a bedside tool.

**It calls itself a single-system study** despite having two sites, because the sites share an EHR, templates and staff.

**What holds it at 3 rather than 4:**

**There is no held-out set of notes anywhere in the study.** The model was chosen from three on these 196 notes. The prompt was revised twice after inspecting where it disagreed on these 196 notes. Then the final accuracy was computed on these 196 notes. Every number is in-sample with respect to both choices, and the paper quantifies the resulting optimism nowhere. Its own limitation says "iterative prompt refinement may have overfit to institution-specific documentation patterns," which names the smaller half of the problem: the larger half is that the evaluation set and the development set are the same 196 documents.

**The reference-standard reviewers were not blinded to the model's output.** The authors put this first in their limitations and note that consensus adjudication is an accepted method; both things are true, and the unblinding still means the correct answers were set by people who could see the answer being graded.

**Every confidence interval is too narrow at the bottom, by a method the paper never names.** Section 5 recovers it. Two intervals exceed 100% and were truncated.

**The weighting scheme for the weighted kappa is not stated.** Linear and quadratic weights give materially different numbers on a three-category scale, so "weighted Cohen's kappa 0.96" is not fully reported.

**One inference run per note, temperature 1.0, no seed.** The headline figures are a single draw from a stochastic process with no estimate of how much they would move on a re-run.

**What would make it a 4:** a set of notes held back from prompt development and model selection; a blinded reference standard; and a second health system that does not share an EHR instance. The authors name all three as future work.

## 4. The Editor's Concerns

**The summary box invites a misreading the Methods do not.** The paper's Bottom Line box says: "Sensitivity was 94.4% and negative predictive value was 86.9% for identifying children at very low risk of injury." Read in isolation, that sounds like performance against *injury*. It is not. Those numbers are agreement with **clinician chart review**, which is stated unambiguously in the Methods and in the preceding sentence of the box itself. The distinction is the whole study design, and it survives one careless sentence badly.

**The headline metrics and the clinical metrics come from different studies in effect.** The 95.4% measures agreement with human readers. The secondary analysis — the one about actual injuries — rests on **4 children with an injury and 1 who needed intervention.** The reported "100% sensitivity" for both is 4 out of 4 and 1 out of 1. The authors say the intervals are wide; Section 5 gives them.

**Missing documentation was imputed in one direction, and the direction has a clinical sign.** Missing predictors were counted as negative. PECARN classifies a child as very low risk only when *all* predictors are negative, so counting absence as negative pushes children **toward** very low risk — that is, toward **not scanning**. The authors flag this and name the two predictors most exposed (chest wall and abdominal wall trauma, which have no structured fields). And the data agree with the theory: the two worst errors in the study were children the clinicians called **high risk** and the model called **very low risk**, and in both the model had missed abdominal wall trauma. Neither child had an injury, which is luck rather than design. **An imputation rule that produces errors preferentially in the unsafe direction is a design feature, not a rounding detail**, and it will matter more in a cohort where injuries are not 2%.

**"Two sites" is close to one site for the purpose it is being used for.** Shared EHR instance, shared documentation templates, shared physicians. The thing an LLM extraction pipeline most needs testing against is a *different documentation culture*, and this design cannot supply one. To their credit the authors say so and call the study single-system.

**Model selection and prompt refinement are the LLM-era version of tuning a threshold on the test set.** Three models were compared and the winner kept, on the evaluation data. Two rounds of prompt revision followed inspection of the disagreements, on the evaluation data. Neither step is wrong in itself — this is how prompts get built — but both consume the evaluation set, and the paper reports the post-selection number as if it were an estimate of future performance.

**One run, temperature 1.0, no seed.** The paper deserves credit for stating these parameters at all; most do not. But a single inference run means the reported 95.4% is one sample. Running the same notes three times and reporting the spread would have cost two more hours of compute and would have told the reader how much of that figure is signal.

**The F1 confidence interval was computed differently from the other five and the method is not stated.** F1 is 0.9675 and the reported interval is 0.90 to 0.98 — the point estimate sits 0.0675 above the lower bound and 0.0125 below the upper, an asymmetry of more than five to one. All five other intervals in the paper are exactly symmetric. Something different produced this one and the paper does not say what.

**Deserved credit on a point this list usually has to criticise:** the authors identify that most of their discordances reflected **ambiguity in the clinical definitions rather than model errors**, and argue that language models may be useful for *finding* imprecise definitions in clinical rules. They also note that the model applied definitions strictly — refusing to call a mechanism dangerous when the fall height or crash speed was not documented. That is a model behaving correctly and a documentation problem being exposed, and the paper reads it that way round.

**Where I am uncertain, stated plainly.** The per-variable performance table is referenced in the text but is not in the retrieved version, so I cannot quote individual variable accuracies; the text states all exceeded 94%, and the arithmetic is consistent with the worst at 185/196 = 94.4%, since 11 of the 23 errors fell in one variable and the Discussion names dangerous mechanism of injury as the weakest. **The names of the predictor variables in the discordance breakdown were stripped by the text extraction**, so I can report that the 23 errors split 11/4/3/2/2/1 across six variables but cannot say which is which beyond what the Discussion states. The supplementary prompts and the confusion matrix for the three-category comparison were not retrievable.

## 5. Statistics Spotlight

Three things. The first is a forensic exercise you can run on almost any diagnostic-accuracy paper; the second is the reliability statistic this list has been missing; the third is specific to the new generation of language-model studies.

### Recovering the confusion matrix — and catching the confidence-interval method

A diagnostic accuracy paper usually publishes percentages. Underneath them is a 2×2 table of four whole numbers, and because the percentages all share those four numbers, you can often work backwards to recover it.

Here we are told n = 196, accuracy 95.4%, sensitivity 94.4%, specificity 98.2%, PPV 99.3% and NPV 86.9%. Call the four cells **TP** (both said not-very-low-risk), **FN** (clinician said not-very-low, model said very low), **FP** and **TN**. Then:

> sensitivity = TP/(TP+FN) · specificity = TN/(TN+FP) · PPV = TP/(TP+FP) · NPV = TN/(TN+FN)

Search the whole numbers that fit. Exactly one set does:

> **TP = 134 · FN = 8 · FP = 1 · TN = 53**

Check it: 134/142 = 94.37% (sensitivity 94.4 ✓). 53/54 = 98.15% (specificity 98.2 ✓). 134/135 = 99.26% (PPV 99.3 ✓). 53/61 = 86.89% (NPV 86.9 ✓). 187/196 = 95.41% (accuracy 95.4 ✓). F1 = 268/277 = 0.9675 (0.97 ✓).

So the study is: **the clinicians judged 142 children not-very-low-risk and 54 very-low-risk; the model missed 8 of the 142 and over-called 1 of the 54.** That is far more informative than the percentages, and it is what you need to judge anything.

Now the second half, which is where it gets interesting. Take each cell count and ask what confidence interval the two common formulas would produce.

The **Wald** interval is the one everybody learns: *p* ± 1.96 × √(*p*(1−*p*)/*n*). Symmetric by construction.

For accuracy, 187/196: *p* = 0.9541, √(0.9541 × 0.0459 / 196) = 0.01495, ±1.96 × that = ±0.0293.

> **92.48% to 98.34%.** The paper reports **92.5 to 98.3.**

Do the same for the other four and every one lands:

- Sensitivity 134/142 → Wald 90.57–98.16; reported **90.6 to 98.2**
- NPV 53/61 → Wald 78.41–95.36; reported **78.4 to 95.4**
- Specificity 53/54 → Wald **94.55 to 101.74**; reported **94.6 to 100**
- PPV 134/135 → Wald **97.81 to 100.71**; reported **97.8 to 100**

Five for five. The paper used Wald intervals — it never says so — and **two of them ran past 100% and were cut off at the boundary.**

**Why this is not pedantry.** The Wald interval is known to behave badly when the proportion is close to 0 or 1, because it pretends a bounded quantity is symmetric. The **exact (Clopper–Pearson)** interval does not. Compare:

- Specificity 53/54: Wald says 94.6–100. Exact says **90.1 to 99.95.**
- PPV 134/135: Wald says 97.8–100. Exact says **95.9 to 99.98.**
- Accuracy 187/196: Wald says 92.5–98.3. Exact says **91.5 to 97.9.**
- Sensitivity 134/142: Wald says 90.6–98.2. Exact says **89.2 to 97.5.**
- NPV 53/61: Wald says 78.4–95.4. Exact says **75.8 to 94.2.**

**Every single reported lower bound is higher than the correct one** — by 1.0, 1.4, 2.6, 3.4 and 4.4 percentage points. The error runs the same way every time, and it flatters the study. Specificity could honestly be as low as 90%, not 94.6%.

**The technique:** when a paper gives you several percentages from one table, reconstruct the counts. Then take the smallest cell, compute a Wald interval, and see whether it matches what was printed. **A confidence interval whose upper limit is exactly 100% (or lower limit exactly 0%) is a method announcing that it has broken** — the formula went past the boundary and somebody clipped it. When you see it, mentally widen the other end too.

### Cohen's kappa — and why 95.4% agreement is not 95.4% worth of agreement

This list has reported accuracy, sensitivity, AUC and calibration. It has never reported a **reliability** statistic, which asks a different question: when two raters judge the same thing, how much do they agree *beyond what they would have got by chance*?

Why subtract chance? Suppose two radiologists each read 100 scans and each calls 95 of them normal, at random, with no skill at all. They will agree on about 90.5 of the 100 — not because they are good, but because they are both saying "normal" almost all the time. Raw agreement rewards a skewed distribution.

Cohen's kappa fixes that:

> **kappa = (observed agreement − chance agreement) / (1 − chance agreement)**

The denominator is the agreement that was actually available to earn. Kappa of 1 is perfect, 0 is no better than chance, and negative is worse than chance.

Run it on the table we reconstructed. Observed agreement is 187/196 = **0.9541** — the paper's accuracy. Now the chance part. The clinicians called 142/196 = 72.45% not-very-low-risk; the model called 135/196 = 68.88%. So two raters with those habits and no skill would agree:

> on "not very low": 0.7245 × 0.6888 = 0.4990
> on "very low": 0.2755 × 0.3112 = 0.0857
> **chance agreement = 0.5848**

And so:

> kappa = (0.9541 − 0.5848) / (1 − 0.5848) = 0.3693 / 0.4152 = **0.889**

**95.4% accuracy, kappa 0.89.** Nearly 59 of those 95 percentage points were free, because almost three-quarters of these children land in one category. Kappa 0.89 is still excellent. But the two numbers are not interchangeable, and the gap between them is the measure of how lopsided the data is.

The paper reports **weighted** Cohen's kappa of **0.96** on the three-category version (very low / moderate / high). Weighting is the right choice for ordered categories: calling a "high" a "moderate" is a smaller mistake than calling it "very low," and weighted kappa gives partial credit accordingly. But **the paper does not say which weights.** Linear weights penalise a two-step disagreement twice as much as a one-step; quadratic weights penalise it four times as much, and on a three-category scale quadratic weighting routinely produces a visibly higher number. Without the scheme, 0.96 is not reproducible.

**Watch out for three things with kappa.** First, **it depends on the marginal distribution**, which is why the same raters doing the same job on a different case mix get a different kappa — so kappa values are not comparable across studies. Second, the notorious consequence: a test can have very high agreement and a *low* kappa when one category dominates overwhelmingly, which is known as the kappa paradox and trips people up constantly. Third, and most important here: **kappa between two raters reading the same text measures consistency, not correctness.** Two readers who share a misconception agree perfectly. This paper's 0.96 says the model reads notes the way these clinicians read notes. It does not say either of them is reading them right — and the paper's own best insight is that several of the disagreements were the *definitions* being ambiguous, not either party being wrong.

### Choosing the model and rewriting the prompt on the test set

This list has repeatedly caught papers tuning a decision threshold on the data they then report performance on. The language-model era has two new versions of the same mistake, and this paper contains both — openly.

**Version one: model selection.** Three models were run — GPT-4o-mini, GPT-4.1, o1 — and o1 kept "because it demonstrated the highest accuracy at the predictor variable level." On these 196 notes. Picking the best of three on a sample and then reporting that best score as an estimate of future performance is the oldest optimism there is. With three roughly comparable models the inflation is modest, but it is not zero and it is not estimated.

**Version two: prompt refinement.** "LLM prompts were developed over 2 rounds… Two clinicians assessed discordant LLM–clinician predictor variable extractions to identify misclassification patterns and refine prompts with clearer criteria." In plain terms: they ran the model, looked at where it got things wrong, rewrote the instructions to fix those specific failures, and ran it again. That is the correct way to build a prompt. It is also, unavoidably, fitting the prompt to the answers — and there is no second set of notes on which to see what the refined prompt does on cases it was not shaped by.

**The analogy:** imagine marking a student's practice exam, telling them exactly which questions they got wrong and why, letting them re-sit the same paper, and then reporting the second score as their expected grade. The second score is real. It is not a prediction.

**The fix is cheap and standard:** split the notes. Develop the prompt and pick the model on, say, 100 notes; freeze both; report on the other 96. The confidence intervals get wider — but they become intervals for the thing the reader cares about.

**The watch-out for any LLM-in-medicine paper:** find the sentence describing how the prompt was written. If it mentions iteration, refinement, few-shot example selection, or error analysis, ask which data that happened on. Then find how many inference runs were done. **This paper says one run per note at temperature 1.0 with no seed** — meaning the output is stochastic and the published figures are a single draw. Three runs would have given a spread. TRIPOD-LLM asks for these details precisely so readers can perform this check, and this paper reports them, which is why the check is possible at all.

## 6. Jargon Translator

**PECARN** — the Pediatric Emergency Care Applied Research Network, a US research collaboration whose prediction rules are widely used in children's emergency care.

**Clinical prediction rule** — a short checklist of findings that sorts patients into risk groups. PECARN's intra-abdominal injury rule uses seven findings to identify children at very low risk, who can safely avoid a CT scan.

**Intra-abdominal injury (IAI)** — damage to an organ inside the abdomen (spleen, liver, kidney, bowel) after trauma.

**Blunt abdominal trauma** — a crushing or impact injury (car crash, fall, handlebar) rather than a penetrating one (stabbing, gunshot).

**FAST** — Focused Assessment with Sonography for Trauma: a rapid bedside ultrasound looking for free fluid.

**Dangerous mechanism of injury** — a PECARN category covering high-energy events, defined partly by numbers like fall height or crash speed. The hardest variable for the model, because those numbers are often not written down.

**Unstructured clinical notes** — free text a doctor types, as opposed to tick-boxes and numeric fields. Most of what matters clinically lives here, which is why it is so hard to analyse at scale.

**Zero-shot prompting** — asking a model to do a task with instructions only and no worked examples.

**Function calling / structured output** — forcing a model to return a fixed, machine-readable format instead of prose, so answers can be parsed reliably.

**Temperature** — how much randomness the model uses when choosing each word. 0 is near-deterministic; 1.0 is the default and is stochastic, meaning the same input can yield different outputs.

**Seed** — a number that fixes the randomness so a run can be repeated exactly. "No seed set" means the run cannot be reproduced.

**Reference standard** — the answer treated as correct for scoring purposes. Here it is two clinicians reading the same notes, not the child's actual diagnosis.

**Sensitivity** — of the cases that truly are positive, the share the test catches.
**Specificity** — of the cases that truly are negative, the share the test correctly clears.
**Positive predictive value (PPV)** — of the cases the test calls positive, the share that really are.
**Negative predictive value (NPV)** — of the cases the test calls negative, the share that really are. PPV and NPV depend on how common the condition is; sensitivity and specificity do not.

**F1 score** — the harmonic mean of PPV and sensitivity, a single number balancing the two. Ranges 0 to 1.

**Cohen's kappa** — agreement between two raters after subtracting the agreement expected by chance. See Section 5.

**Weighted kappa** — kappa for ordered categories, where disagreements count more the further apart they are. The weighting scheme (linear or quadratic) changes the answer and must be stated.

**Wald confidence interval** — the familiar symmetric *p* ± 1.96 × standard error. Unreliable near 0 or 1, where it can run past the boundary.

**Clopper–Pearson (exact) interval** — a confidence interval for a proportion built from the binomial distribution directly. Never exceeds 0 or 1, correctly asymmetric near the edges.

**Confusion matrix** — the 2×2 (or 3×3) table of counts underneath all of these percentages.

**TRIPOD-LLM** — the large-language-model extension of the TRIPOD reporting guideline, covering model versions, prompts, sampling parameters and inference runs.

**STROBE** — the reporting guideline for observational studies.

## 7. What You Can (and Can't) Say

**Fair to say:**

- ✅ "An LLM reproduced clinicians' PECARN risk scores from emergency department notes in 187 of 196 children." Verified; the reconstructed table is 134/8/1/53.
- ✅ "Across 1,568 individual data extractions it made 23 errors, 1.47%." Verified: 196 × 8 = 1,568, and the breakdown 11+4+3+2+2+1 sums to 23.
- ✅ "It took about two hours to read 196 notes." Stated; roughly 37 seconds per note.
- ✅ "Agreement on the three-level score was high — weighted kappa 0.96." Reported, though the weighting scheme is not given.
- ✅ "Nearly half the errors fell in one variable, and the authors identify dangerous mechanism of injury as the weakest." 11 of 23; stated in the Discussion.
- ✅ "The model refused to call a mechanism dangerous when the fall height or crash speed was missing from the note." Stated, and the authors read this as correct strict behaviour.
- ✅ "The authors say this is for quality improvement and research, not bedside imaging decisions." They say it three times.
- ✅ "Several disagreements came from the clinical definitions being ambiguous rather than the model being wrong." The paper's own analysis, and one of its better contributions.

**Not fair to say:**

- ❌ "The LLM was 95.4% accurate at detecting intra-abdominal injury." It was 95.4% concordant with **clinicians reading the same notes**. Only 4 of the 196 children had an injury.
- ❌ "It had 100% sensitivity for intra-abdominal injury." That is 4 out of 4, exact 95% CI **39.8% to 100%**. For injuries requiring intervention it is 1 out of 1, exact CI **2.5% to 100%**.
- ❌ "Specificity was at least 94.6%." That lower bound comes from a Wald interval that ran past 100% at the other end. The exact interval starts at **90.1%**.
- ❌ "The model performs as well as clinicians." It agrees with clinicians. Nobody here was measured against the truth, because the truth — the child's actual injury status — was present in only four children.
- ❌ "This was validated at two independent sites." The two share an electronic health record, documentation templates and some physicians; the authors call it a single-system study.
- ❌ "These results would hold at another hospital." The prompt was refined twice on these notes and the model chosen from three on these notes. The authors name institution-specific overfitting as a limitation.
- ❌ "The model's errors were harmless." The two worst — clinician "high risk," model "very low risk" — both came from missing abdominal wall trauma, which is the direction that would skip a scan. That neither child had an injury is luck, in a cohort where only 2% did.
- ❌ "Re-running it would give the same answer." Temperature 1.0, no seed, one run per note.
- ❌ "Kappa 0.96 means the scores are 96% correct." Kappa is chance-corrected agreement between two readers of the same text, not accuracy, and it is not comparable across studies.

## 8. Bottom Line for Your Life

If you have a child who has been in a crash or a bad fall, the fact worth carrying from this paper is not about the AI. It is that **a published rule exists which lets doctors safely skip a CT scan in children at very low risk** — and that avoiding the scan, where the rule applies, is the better care, because a CT delivers radiation to a child's body and carries a small lifetime cancer risk. If a scan is not ordered, that may be the rule being followed correctly rather than a corner being cut, and it is a reasonable thing to ask about.

What the study actually did is unglamorous and genuinely useful: it tested whether a machine can read doctors' notes and work out, after the fact, whether the rule was applied. Done reliably, that lets hospitals audit themselves at a scale no human chart-review team can match.

For anyone appraising research, this paper hands you one skill and one habit.

**The skill: rebuild the table.** From six published percentages and one sample size, the full confusion matrix here comes out uniquely — 134, 8, 1, 53 — and once you have it you can compute anything the paper did not, including the one thing it needed. Doing that also recovered the confidence-interval method the paper never names, and showed that **every reported lower bound was too high**, by up to 4.4 percentage points, because a symmetric formula was used on proportions sitting right against the ceiling. Two of the intervals ran past 100% and were clipped, which is the visible symptom. **An interval ending at exactly 100% is not a strong result; it is a broken calculation.**

**The habit, for every AI-in-medicine paper from here on: find out what the model was compared against, and find out what data the prompt was written on.** This study compared a model to humans reading the same text — a reasonable question, clearly stated, and not the same question as whether anyone got the diagnosis right. And it built the prompt by looking at its own mistakes on the very notes it then reported scores for. The authors disclose both. Most won't. **When the comparison is against another reader rather than against the truth, "95.4% accurate" means "agrees with us," and when the prompt was tuned on the test set, it means "agrees with us, after we adjusted it until it did."** Both can still be worth knowing. Neither is what the number sounds like.

---

## Appendix — deferred-paper status, 2026-10-29

Recorded because this is day 14 for one of them and the situation has partly changed.

- **Google, "The anatomy of a personal health agent"** (Nature, PMID 42907512, DOI 10.1038/s41586-026-11161-8): **no PubMed Central copy.** Abstract available; describes a multi-agent framework with three specialist sub-agents evaluated across 11 benchmark tasks with more than 7,000 annotations and 1,350 hours of expert effort. Still the most important of the four and still unreadable in full.
- **BMJ, "Reporting completeness of clinical trials evaluating large language model interventions"** (PMID 42869550, DOI 10.1136/bmj-2026-100855): **no PMC copy;** Scite remains paywalled. Structured abstract now complete — 461 records, 68 trial reports, mean reporting completeness TRIPOD-LLM 40%, CONSORT 2025 44%, CONSORT-AI 59%, CHART 52%, SPIRIT 2025 51%, SPIRIT-AI 57%, WHO registration dataset 61%.
- **Annals of Internal Medicine, "Overuse and False Restraint in LLM Recommendations for Choosing Wisely Scenarios"** (PMID 42896192, DOI 10.7326/ANNALS-26-01667): **no PMC copy.** Abstract now full: 15 recommendations, 225 scenarios, 6 commercial LLMs × 3 runs = 4,050 responses; overuse 5.4% (95% CI 0.6% to 12.2%), false restraint 0.6% (0.1% to 1.2%). **Note for whenever this becomes readable: a point estimate of 5.4% with an interval running from 0.6% to 12.2% is a clustering signature — the interval is almost certainly computed across the 15 recommendations rather than the 4,050 responses, which is the correct choice and worth teaching.**
- **JAMA, "Clinician Use of an Artificial Intelligence–Enabled Clinical Information Platform"** (PMID 42879271, PMC13673371, DOI 10.1001/jama.2026.21868): PMC record exists and **serves an empty body for the fourteenth consecutive day.** The abstract is complete: cross-sectional, 952,008 US clinicians including 556,200 physicians, 271 million queries over 2.5 years, monthly active users 355 → 703,265, queries per active user-month 18.0 → 39.5; use ratio 2.54 for physicians within a decade of graduation, 2.00 oncology/haematology, 0.23 ophthalmology; 33.1% of queries on treatment and management versus 13.9% on diagnosis. **If the body is still empty on 2026-11-05 (day 21), decode it abstract-only and say so explicitly** — the denominator alone is worth recording, and the use-ratio metric is a teachable construction.

---

*This is an educational analysis of a published scientific paper, not medical advice. Nothing here is guidance about abdominal injuries, CT scans, or whether any particular child needs imaging. If your child has been injured, seek medical care.*
