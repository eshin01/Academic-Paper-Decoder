# Clinical-grade computational pathology using weakly supervised deep learning on whole slide images

- **Authors:** Gabriele Campanella, Matthew G. Hanna, Luke Geneslaw, Allen Miraflor, Vitor Werneck Krauss Silva, Klaus J. Busam, Edi Brogi, Victor E. Reuter, David S. Klimstra, Thomas J. Fuchs (Department of Pathology, Memorial Sloan Kettering Cancer Center; Weill Cornell)
- **Venue:** Nature Medicine, 2019;25(8):1301–1309 (published July 15, 2019)
- **DOI link:** https://doi.org/10.1038/s41591-019-0508-1
- **PubMed link:** https://pubmed.ncbi.nlm.nih.gov/31308507/ (PMID 31308507)
- **Full-text link:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7418463/ (PubMed Central author manuscript)
- **Basis:** FULL TEXT — introduction, results, discussion, methods, and Extended Data descriptions retrieved from PubMed Central. Funding and competing-interest statements were **not present in the retrieved manuscript text**; PubMed tags NIH extramural support. Identifiers verified against the live PubMed/NLM record; URL browsing is blocked in this environment, so links are constructed from that verified record.
- **Decoded:** 2026-09-06

---

# The Gist

When a biopsy is taken, a pathologist puts the tissue on a glass slide and looks for cancer under a microscope. Teaching a computer to do this has been stuck for years on one obstacle: models normally need experts to trace tumor outlines pixel by pixel, which is so slow that datasets stayed tiny. This team from Memorial Sloan Kettering skipped the tracing entirely — they trained on **44,732 slides from 15,187 patients** using nothing but the diagnosis already written in the medical record as the label. The models hit very high accuracy on prostate cancer, a common skin cancer, and breast cancer spread to lymph nodes. Their proposed use is not to replace pathologists, but to sort the pile: the system could set aside **65–75% of slides as definitely-no-cancer** without missing a single case in their test, letting the pathologist spend their time on the rest.

# Study Snapshot

- **Study type:** Retrospective diagnostic-accuracy study on archived digitized slides, with several deliberate stress tests of generalization. No patient's care was changed; no prospective deployment.
- **Scale (n):** 44,732 whole slide images from 15,187 patients — a prostate biopsy set of 24,859 slides, a skin set of 9,962, and a breast-metastasis-to-lymph-node set of 9,894. Each is at least ten times larger than anything else in the field at the time.
- **Deliberately messy data:** the slides were **not curated**. They include real laboratory defects — air bubbles, knife-slicing irregularities, fixation problems, folds, cracks, and digital scanning artifacts. The authors argue this is the point: it is what a real pathology lab produces.
- **External material:** 17,661 slides prepared at *other* institutions — 17,363 from 48 US states plus Washington DC and Puerto Rico, and 248 from 44 other countries.
- **How it learned:** "multiple instance learning" — the model is told only that a slide is cancerous or not, and must work out for itself which tiny regions matter. A second network (a recurrent model) then combines the most suspicious regions into one slide-level verdict.
- **Test performance (AUC):** 0.991 prostate, 0.989 basal cell carcinoma, 0.965 breast lymph node metastases. After specialist pathologists reviewed the errors and corrected genuine mistakes in the original record labels, these rose to 0.994, 0.994 and 0.989.
- **Splits:** 70% training / 15% validation / 15% test, divided **by patient**, with the final models run **once** on the test set.
- **The clinical proposal:** operate at 100% sensitivity (miss nothing) and accept the resulting false alarms. At that setting, more than 75% of prostate slides, 68% of skin slides, and 65% of breast slides could be set aside unreviewed.
- **Funding / conflicts:** not reported in the retrieved text; PubMed tags NIH extramural support. Readers citing this should check the published competing-interests statement directly.

# How Strong Is This Evidence?

**Grade: 4/5 — the most rigorously stress-tested study on this reading list so far, still short of prospective proof.**

Nearly everything I have been flagging as missing in other papers, this one did. It used real uncurated clinical material rather than a tidy benchmark. It split by patient, not by slide, so the same person's tissue could not appear on both sides. It ran the test set **once**. It tested what happens on a *different scanner brand* and on slides prepared at *other hospitals*, and reported the losses honestly. Its specialists reviewed every model error by eye and found some of the "errors" were mistakes in the original records. And — most valuable of all — it ran the experiment its own field had been avoiding: it showed that the standard approach of training on a small, beautifully annotated public dataset **collapses** when moved to real-world slides.

What keeps it from 5/5: it is still retrospective, with no prospective trial of the proposed workflow, so the promised time savings and the "no missed cancers" claim have never been tested in live practice. The ground truth is the diagnosis typed into the hospital system, which the authors themselves show is imperfect. The 100%-sensitivity operating points were identified on the same test data used to report them. And the funding and conflict statements were not in the text I retrieved.

# The Editor's Concerns

- **"100% sensitivity" is an observation on one test set, not a property of the system.** Missing zero of roughly 1,500 slides is genuinely impressive, but zero observed misses does not mean the true miss rate is zero — it means it is probably small (see Statistics Spotlight). Deployed across a million slides, some cancers will be missed, and the workflow needs a plan for that.
- **The thresholds that deliver 100% sensitivity were chosen on the test set.** The paper names specific cutoffs (0.025 for skin, 0.21 for breast) that achieve no misses on the very data being reported. A cutoff tuned on a dataset flatters itself on that dataset; the honest test is a threshold fixed in advance and applied to new slides.
- **Ground truth is the diagnosis in the record, and it is noisy.** The authors are candid: pathologist review found discrepancies between the recorded diagnosis and what was actually on the scanned slide — 6 in prostate, 8 in skin, 23 in lymph nodes — arising from things like the wrong slide level being scanned. Their models still trained well through this noise, which is a genuine finding, but the ceiling of any such study is set by the quality of its labels.
- **Performance dropped under realistic shifts, exactly as feared.** On a different scanner brand, AUC fell about 3 percentage points. On 12,727 slides prepared at other institutions, it fell about 6 points — mostly in specificity, meaning more false alarms rather than more misses. That is the safer direction to fail, but a 6-point drop crossing institutional boundaries is the number a hospital buying this should be shown.
- **One institution trained it.** All training material came from Memorial Sloan Kettering. The external slides were prepared elsewhere but scanned at MSK, so the test of "would this work at another hospital end-to-end" remains incomplete.
- **The workload claim has not been tried on real pathologists.** Setting aside 75% of slides sounds transformative; whether pathologists in practice trust it, use it correctly, or become less careful on the remaining 25% is an entirely separate research question — and automation complacency is well documented in other fields.
- **Funding and competing interests were not in the retrieved text**, which matters in a field with substantial commercial activity around computational pathology.
- **What this study did well:** enormous uncurated real-world datasets; patient-level splits; the test set used exactly once; explicit stress tests across scanner brands and across institutions with the losses reported; expert pathologist review of every error; confidence intervals by bootstrapping and a proper statistical test for comparing models; a redefinition of "clinical grade" around a clinically usable operating point rather than a beauty-contest comparison against humans; and the field-correcting head-to-head experiment described below.

# Statistics Spotlight

**1. The generalization-gap experiment — the most important thing in this paper.**
- *What it is:* A test of whether a model trained in one setting still works in another. The gold-standard version trains on dataset A, then evaluates on a genuinely different dataset B, and reports how much performance falls.
- *How this paper used it:* They rebuilt the winning entry from CAMELYON16 — the field's leading public benchmark, with 270 painstakingly hand-annotated slides — and reproduced its excellent score of **0.930** on the CAMELYON16 test set. Then they pointed that same model at their real-world hospital slides: it fell to **0.727**, a collapse of about 20 points. Running it in reverse, their own model trained on messy hospital data scored 0.965 at home and still **0.899** on CAMELYON16 — a much gentler drop.
- *The theory, with an analogy:* Think of a student who aces practice tests because they memorized that particular question bank. Move them to a different exam on the same subject and they fall apart. The student trained on a wide, disorganized range of real problems scores slightly lower on any single practice test but holds up nearly everywhere. Small curated datasets teach the dataset; large messy ones teach the task.
- *Watch out:* This is why "state of the art on benchmark X" is a much weaker claim than it sounds, and why the direction of a validation matters. A model that travels *from* a clean benchmark *to* the real world is the test that counts; the reverse is easier and proves less. When you read that a medical AI was "externally validated," ask whether the new data was genuinely different in the ways that break models — different equipment, different labs, different populations — or merely different patients from the same source.

**2. DeLong's test — how to compare two AUCs fairly when they were measured on the same cases.**
- *What it is:* A statistical test for whether two ROC curves genuinely differ, designed for the situation where both models were evaluated on the *same* patients. That shared data makes the two scores correlated, and ignoring the correlation would make the comparison unreliable.
- *How this paper used it:* Their simpler aggregation method scored 0.986 and a more elaborate one scored 0.987; DeLong's test said the difference was **not** statistically significant, so they did not claim an improvement. Elsewhere it showed their recurrent-network model was significantly better than the simple approach for prostate.
- *The theory, with an analogy:* If two students take the *same* exam, comparing them is easier and fairer than if they took different exams — but you must account for the fact that a very easy question helped them both. DeLong's test does that bookkeeping. Comparing the two scores as if they came from independent samples would overstate your confidence in whichever number happened to be higher.
- *Watch out:* Two very high AUCs, say 0.986 versus 0.987, are frequently reported as one model "beating" another. Usually that gap is noise. Ask whether a paired statistical test was run, and be suspicious of any ranking of models by a third or fourth decimal place. This paper's restraint here — declining to claim a win it could not support — is exactly what you want to see.

**3. Choosing the operating point from a clinical requirement — and what "zero misses" can and cannot promise.**
- *What it is:* Rather than tuning the model for best overall accuracy, you fix the requirement that matters clinically — here, "miss no cancers" — and then measure what you pay for it in false alarms.
- *How this paper used it:* They explicitly reject "beat the pathologist" as the standard, arguing a team of specialists with extra tests effectively operates at 100% sensitivity anyway. Their proposed bar is 100% sensitivity with a tolerable false-positive rate, which yields the headline: 65–75% of slides safely set aside.
- *The theory, with a worked example on the limits of zero:* Suppose a test misses nothing in 1,500 slides. Statisticians use a quick rule — the "rule of three" — to bound what you can conclude: with zero events in about 1,500 tries, the true miss rate could still plausibly be as high as roughly 3 divided by 1,500, about 1 in 500. So "we missed none" honestly means "the miss rate is probably under about 0.2%," not "the miss rate is zero." Across a large hospital's annual volume, that is not nothing.
- *Watch out:* Perfect sensitivity reported on a test set is one of the most over-read numbers in medical AI. Two questions defuse it: how many cases produced that zero (few cases, weak claim), and was the threshold chosen before or after seeing this data? Here the sample is large — a real strength — but the thresholds were identified on the reported test data, so the true operating performance on tomorrow's slides will be somewhat worse.

# Jargon Translator

- **Whole slide image (WSI):** a glass microscope slide scanned into a single enormous digital image — several billion pixels each; about 470 of them contain as many pixels as the entire ImageNet photo database.
- **Pathologist:** the doctor who examines tissue to diagnose disease; their report determines how a cancer is treated.
- **Pixel-level annotation:** an expert manually outlining tumor regions on an image — accurate, extremely slow, and the bottleneck this paper set out to remove.
- **Weak supervision / multiple instance learning (MIL):** training where the label applies to the whole slide ("this biopsy had cancer") rather than to specific regions; the model must find the relevant regions itself.
- **Tile:** a small square cut from the giant slide image, small enough for a neural network to process.
- **Max-pooling aggregation:** calling a whole slide positive if any single tile looks positive — simple, but one bad tile can flip the verdict.
- **Recurrent neural network (RNN):** a network that reads a sequence — here, the most suspicious tiles in order — and integrates them into one decision.
- **Basal cell carcinoma (BCC):** the most common human skin cancer; rarely fatal but extremely frequent.
- **Axillary lymph node metastasis:** breast cancer that has spread to lymph nodes under the arm — a finding that changes treatment.
- **Frozen section:** tissue examined rapidly during surgery, with lower image quality than standard processing.
- **CAMELYON16:** the well-known public benchmark of 400 annotated slides used as the field's standard test.

# What You Can (and Can't) Say

**Fair to say:**
- "A 2019 Memorial Sloan Kettering study trained cancer-detection models on 44,732 real, uncurated pathology slides using only the diagnoses already in the medical record — no manual tumor tracing — and reached AUCs above 0.98 for prostate cancer, basal cell carcinoma, and breast metastases."
- "It showed that a leading model trained on the field's standard small annotated benchmark dropped from 0.930 to 0.727 when applied to real hospital slides, while their large-data model generalized far better."
- "The authors propose using it to triage the workload — setting aside 65–75% of slides at 100% sensitivity in their test set — rather than to replace pathologists."
- "Performance dropped roughly 3 points on a different scanner and 6 points on slides prepared at other institutions."

**Not fair to say:**
- "AI diagnoses cancer perfectly / never misses cancer" — zero misses on about 1,500 test slides bounds the miss rate to roughly under 0.2%; it does not make it zero, and the operating threshold was set on that same data.
- "AI can replace pathologists" — the authors explicitly reject that framing and design for assistance, and every diagnosis here is a binary tumor/no-tumor call, not the grading, staging, and integration a real report requires.
- "This is proven in the clinic" — retrospective throughout; no prospective deployment, and no test of whether pathologists using it actually save time or stay accurate.
- "It works anywhere" — training data came from one cancer center, and measured performance fell under both scanner and institution shifts.

# Bottom Line for Your Life

If you want one paper from this reading list that shows what careful medical-AI research looks like, it is this one — not because the accuracy numbers are highest, but because the authors kept trying to break their own model and told you what happened each time. The single most useful thing here is a warning that applies far beyond pathology: **a model that shines on a clean public benchmark can fall apart on real clinical material** — 0.930 down to 0.727 — while one raised on messy real-world data travels much better. That is the sentence to remember the next time you see a medical AI announced with a benchmark score. For a patient, nothing changes today: this describes a tool to help pathologists sort their microscope work, tested on stored slides, never yet run in a live clinic. One study is one data point, even a good one. This is an educational breakdown, not medical advice.

---

**Sources** (based on articles retrieved from PubMed / PubMed Central; identifiers verified against the live NLM record — URL browsing is blocked in this environment, so links are constructed from that verified record):
- DOI: https://doi.org/10.1038/s41591-019-0508-1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/31308507/
- Full text (PMC author manuscript): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7418463/
