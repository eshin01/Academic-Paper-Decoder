# Dermatologist-level classification of skin cancer with deep neural networks

- **Authors:** Andre Esteva, Brett Kuprel, Roberto A. Novoa, Justin Ko, Susan M. Swetter, Helen M. Blau, Sebastian Thrun (Stanford University)
- **Venue:** Nature, 2017;542(7639):115–118 (published January 25, 2017); corrigendum published June 28, 2017 (Nature 546:686, https://doi.org/10.1038/nature22985)
- **DOI link:** https://doi.org/10.1038/nature21056
- **PubMed link:** https://pubmed.ncbi.nlm.nih.gov/28117445/ (PMID 28117445)
- **Full-text link:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8382232/ (PubMed Central author manuscript)
- **Basis:** FULL TEXT — analyzed from the complete author manuscript retrieved from PubMed Central via the live NLM record (main text, Methods, Extended Data descriptions). Identifiers verified against the live PubMed record; direct URL browsing is blocked in this environment, so links are constructed from that verified record.
- **Decoded:** 2026-08-31

---

# The Gist

Stanford researchers trained a computer program on about 129,000 photos of skin conditions, then tested it against 21 skin specialists (board-certified dermatologists) at one job: looking at a photo of a spot on the skin and deciding whether it's cancer. On the test images — all confirmed by biopsy, the gold standard — the program performed about as well as the specialists at spotting the most common skin cancers and the deadliest one (melanoma). The authors' big idea: put this in a smartphone and skin-cancer checks could reach billions of people. This 2017 paper is one of the two or three most famous studies in medical AI.

# Study Snapshot

- **Study type:** Retrospective diagnostic accuracy study — the algorithm and doctors judged stored photos, and their answers were compared against biopsy results. Low on the evidence ladder for clinical claims: it measures image-reading skill, not patient outcomes.
- **Training data:** 129,450 clinical images covering 2,032 skin diseases (about 1.41 million images including pre-training), labeled by dermatologists — most training labels were *not* biopsy-confirmed.
- **The showdown (n):** the CNN vs. at least 21 board-certified dermatologists on three tasks using biopsy-proven photos: common skin cancers vs. a benign look-alike (135 images), melanoma vs. benign moles in regular photos (130 images), and melanoma vs. moles in dermoscopy images (111 images). Larger CNN-only test sets: 707, 225, and 1,010 images.
- **What was measured:** sensitivity and specificity of each doctor's biopsy-or-reassure decision versus the algorithm's full performance curve; area under the curve was above 0.91 on every task.
- **Result:** the algorithm's curve sat above most individual dermatologists' points; the authors describe it as "on par with all tested experts."
- **Funding / conflicts:** PubMed tags NIH and non-US-government research support; a conflict-of-interest statement is not reported in the text provided. Stanford IRB approved (protocol 36050).
- **Note:** Nature published a corrigendum (formal correction) to this paper in June 2017 — details of what was corrected are not in the text provided.

# How Strong Is This Evidence?

**Grade: 3/5 — a landmark with genuinely strong test-set design, but an image contest, not a clinic.**

The strengths are real: test answers came from biopsies (ground truth, not opinion), the human comparison used 21 specialists rather than the usual two or three, the same single network handled every task, and the authors took unusual care to keep training images from leaking into the test set. But the ceiling is the same as every study of this design: it proves the algorithm can match specialists *at reading isolated photos with no patient attached*. It says nothing about real clinics, real phones, real skin diversity, or whether anyone's cancer gets caught earlier. The human-comparison sets were also small (111–135 images), and no formal statistical test comparing the algorithm to the doctors is reported in the text provided — the "on par" claim rests on visual comparison of curves and points.

# The Editor's Concerns

- **Doctors diagnose patients, not pixels.** The dermatologists saw only cropped photos — no touch, no patient history, no "has this mole changed?" The authors acknowledge this directly. Real-world dermatologist performance is likely better than their showing here.
- **No statistical test for the headline claim.** "On par with all tested experts" is supported by curves and averages, but the text provided reports no p-value or confidence interval for the human-vs-AI comparison itself. That's a meaningful gap for the paper's central claim.
- **The test sets don't look like real life.** In the melanoma comparison set, 33 of 130 images (25%) were melanoma; in the dermoscopy comparison set, 71 of 111 (64%) were malignant. In the real world, the overwhelming majority of checked moles are harmless. This doesn't change sensitivity/specificity, but it makes "the AI is as good as a dermatologist" feel more clinic-ready than it is (see Statistics Spotlight).
- **Small human-comparison samples.** 111–135 images per task leaves real uncertainty around every point on those plots.
- **Most training labels weren't biopsy-proven** — dermatologist-labeled internet-repository images. The authors properly used biopsy-only test sets, but noisy training labels are a limitation.
- **A corrigendum exists.** Nature published a formal correction six months later; any citation of this paper should be aware of it.
- **Training data mostly not public** — the Stanford data is restricted, limiting independent reproduction.
- **No outcomes, no deployment.** The smartphone vision in the conclusion is aspiration, not evidence; the authors themselves call for real-world clinical validation.
- **What this study did well:** biopsy-proven ground truth for all tests; 21 expert comparators; deliberate prevention of train/test leakage using image-similarity matching; testing both regular and dermoscopy photos; asking doctors the clinically real question ("biopsy or reassure?") and re-running with the alternate question; and honest framing of its own cross-validation results as "inconclusive" where labels weren't biopsy-proven.

# Statistics Spotlight

**1. Sensitivity, specificity, and the ROC curve — the machinery of the whole paper.**
- *What it is:* Sensitivity = of the truly cancerous lesions, the share the test catches. Specificity = of the truly benign ones, the share it correctly clears. Every diagnostic test trades one against the other.
- *How this paper used it:* The CNN doesn't say "cancer/not cancer" — it outputs a probability, say 0.73, per image. You then pick a cutoff: flag everything above it. Slide that cutoff from 0 to 1 and you trace out every sensitivity–specificity combination the model can offer — that's the blue ROC curve in the paper's figures. Each of the 21 dermatologists, by contrast, is a single red *dot*: one person's one implicit cutoff. The model "wins" against a doctor whose dot falls below the curve — which most did.
- *The theory, with an analogy:* Think of a smoke detector's sensitivity dial. Turned up, it catches every fire but shrieks at burnt toast (high sensitivity, low specificity). Turned down, no false alarms but it might sleep through a real fire. The ROC curve is the complete menu of dial settings; the AUC (area under that curve, here above 0.91 of a maximum 1.0) measures how good the *menu* is overall. AUC has a neat meaning: pick one random cancerous lesion and one random benign one — AUC is the probability the model rates the cancerous one as more suspicious. 0.5 is a coin flip; 0.91+ is excellent.
- *Watch out:* Comparing a full curve to single human dots slightly flatters the model — a doctor below the curve isn't necessarily "worse"; they've chosen one dial setting, often deliberately favoring sensitivity because missing a melanoma is far costlier than an unneeded biopsy. And never read "AUC 0.91" as "91% accurate" — it's a ranking score, not a hit rate.

**2. Prevalence and predictive value — why "as good as a dermatologist" doesn't mean "trust the phone app."**
- *What it is:* Sensitivity and specificity describe the test. What a *patient* cares about is the flip side: if the test flags me, what's the chance I actually have cancer? That depends heavily on how common the disease is in the tested population (the prevalence).
- *How it applies here:* The paper's comparison sets were cancer-enriched — up to 64% malignant. Out in the world, checked moles are overwhelmingly benign.
- *The theory, with a worked example:* Suppose the app has 95% sensitivity and 90% specificity, and 5 of every 1,000 real-world moles are melanoma. Scan 1,000 moles: it catches about 5 of the 5 melanomas — but also false-alarms on about 100 of the 995 benign ones. So of ~105 people flagged, only about 5 truly have melanoma — under 1 in 20. Same test, very different meaning once prevalence drops.
- *Watch out:* This is the single most common way diagnostic-AI results get overhyped. Performance measured on enriched test sets says little about what a positive result means during mass screening — and a flood of false alarms has its own real costs (anxiety, biopsies, clogged clinics).

**3. Nine-fold cross-validation — how researchers check a model isn't just memorizing.**
- *What it is:* Split the data into 9 slices; train on 8, test on the held-out ninth; rotate so every slice gets a turn as the test set; report the average and spread.
- *How this paper used it:* For the broad disease-classification checks, the CNN scored 72.1% ± 0.9% (three-category task) and 55.4% ± 1.7% (nine-category task) across the nine rotations, versus about 66% and 53–55% for two dermatologists. The small "±" numbers tell you the performance was stable no matter which slice was held out.
- *The theory:* Testing a model on the data it studied is like grading students on the exact homework problems they memorized. Cross-validation guarantees every score comes from questions the model hasn't seen, and repeating it 9 ways shows whether a good score was skill or luck of the split.
- *Watch out:* Cross-validation only protects against memorization *within* the dataset. If the whole dataset differs from the real world (different cameras, skin tones, lesion mix), every fold inherits that bias — which is why the authors treated these numbers as a sanity check and rested their real claims on the separate biopsy-proven test sets.

# Jargon Translator

- **Convolutional neural network (CNN):** a deep-learning program specialized for images — it learns visual patterns directly from labeled examples.
- **Transfer learning:** starting from a network already trained on millions of everyday photos, then re-training it on medical images — a shortcut that works well when medical data is limited.
- **Dermoscopy:** examining skin through a specialized magnifying instrument that produces standardized close-up images.
- **Biopsy-proven:** the diagnosis was confirmed by removing tissue and examining it under a microscope — the gold standard.
- **Keratinocyte carcinoma:** the most common skin cancers (basal and squamous cell); rarely deadly but very frequent.
- **Melanoma:** the deadliest skin cancer; survival is high when caught early, which is why detection matters so much.
- **Nevus:** the medical word for an ordinary mole.
- **Seborrheic keratosis:** a very common harmless skin growth that can visually mimic cancer.
- **Saliency map:** a heat-map showing which pixels most influenced the network's decision — here confirming it looked at the lesion, not the background.
- **Corrigendum:** a journal's formal published correction to a paper.

# What You Can (and Can't) Say

**Fair to say:**
- "In a 2017 Nature study, a Stanford deep-learning model matched the image-reading performance of 21 dermatologists at classifying biopsy-proven photos of skin cancer."
- "This is one of the founding papers of medical AI, and it showed a single network could handle both regular and dermoscopy photos."
- "Its authors explicitly said real-world clinical validation was still needed."

**Not fair to say:**
- "AI diagnoses skin cancer as well as dermatologists" — it matched them at reading isolated photos, which is only one slice of what diagnosis is.
- "Your phone can screen you for skin cancer" — that was the paper's aspiration; it tested no phones, no consumers, no real-world screening.
- "The AI was 91% accurate" — 0.91 is an AUC (a ranking score), not a percentage of correct diagnoses.
- "This proved AI catches cancer earlier or saves lives" — no patients, no outcomes, no deployment were studied.

# Bottom Line for Your Life

This paper is why "AI dermatologist in your pocket" became a headline genre. The study itself is careful and honest about being a photo-reading contest with strong ground truth — and on that contest, the machine genuinely kept up with 21 specialists. What it never tested is the thing that matters to you: whether an app pointed at your skin, in your lighting, on your skin tone, in a world where nearly all moles are benign, helps you or just alarms you. Nearly a decade later, that clinical-validation gap is still where most consumer skin apps fall short. One study is one data point — a brilliant proof of possibility, not a product endorsement. This is an educational breakdown, not medical advice: a changing, bleeding, or odd-looking mole deserves a clinician's eyes, not just an app's.

---

**Sources** (retrieved and verified via PubMed / PubMed Central; URL-level browsing blocked in this environment, so links are constructed from the verified NLM record):
- DOI: https://doi.org/10.1038/nature21056
- PubMed: https://pubmed.ncbi.nlm.nih.gov/28117445/
- Full text (PMC author manuscript): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8382232/
- Corrigendum: https://doi.org/10.1038/nature22985
