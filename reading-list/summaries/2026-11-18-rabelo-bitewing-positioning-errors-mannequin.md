# Automated Detection of Positioning Errors in Bitewing Radiographs Using Deep Learning

**Authors:** Rabelo KA (Dentomaxillofacial Radiology, Sydney Dental School, University of Sydney), Huang Z (School of Computer Science, University of Sydney), Delamare E, Hegde S (Dentomaxillofacial Radiology, Sydney Dental School), Kim J (School of Computer Science), Miletic V (Restorative and Reconstructive Dentistry, Sydney Dental School) — 6 authors, all University of Sydney
**Journal:** Clinical and Experimental Dental Research, 2026; 12(6): e70504
**Decoded:** 2026-11-18

**Analysis basis:** **FULL TEXT** (retrieved from PubMed Central, PMC13734376) — Introduction, all Methods sub-sections including study design, dataset, the operational definition of every label, the experimental setup and performance metrics; all of Results; the complete Discussion with its limitations; and the funding, ethics and conflicts declarations. **Crucially, all four results tables came through intact**, so every performance figure, per-class metric and standard deviation below is verified against the paper's own tables. **All figures are unreachable** (including the confusion-matrix image and the receptor-placement template figures), as are Supporting Files 1 and 2.

**Source links (verified):**
- DOI: https://doi.org/10.1002/cre2.70504
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42981213/
- Full text used: https://pmc.ncbi.nlm.nih.gov/articles/PMC13734376/

**Basis of link verification.** Direct URL fetching is blocked from this session (`doi.org` does not resolve under the network policy here), so verification was done against the live PubMed/NLM record. According to PubMed, a query for PMID 42981213 returned this exact title, these six authors with these affiliations, *Clinical and Experimental Dental Research* volume 12 issue 6 article e70504, DOI `10.1002/cre2.70504`, and MeSH terms including Radiography Bitewing, Convolutional Neural Networks and Patient Positioning; a PMID-to-PMCID conversion returned **PMC13734376**; and the full text was then retrieved from PubMed Central by that PMC ID and matches the record. Both halves of the chain were confirmed independently.

**Funding: explicitly none.** "The authors have nothing to report."
**Conflicts of interest: explicitly none.** "The authors declare no conflicts of interest."
**Ethics:** approved by the Ethics Committee of the University of Sydney, in accordance with the Declaration of Helsinki. **The approval number is incomplete in the retrieved text** — it appears as "2024/" with nothing following it, in both the Methods and the Ethics Statement. Almost certainly a typesetting or extraction artefact, but **I cannot report a complete approval number** and am recording that rather than guessing.

**Reporting guideline: none named.** **CLAIM** (the Checklist for Artificial Intelligence in Medical Imaging) applies directly to this study type and is not mentioned. This ends a two-entry run in which guidelines were named, and Section 4 records where that leaves the standing observation.

---

## 1. The Gist

**Six researchers in Sydney trained a neural network to spot badly-taken dental X-rays, using 403 images that dental students shot on three plastic dummies. It worked well on four of six tasks and poorly on the two that mattered most — and the pattern of what worked turns out to be the cleanest confirmation in this reading list of an argument made two days ago.**

Start with why anyone would do this. A **bitewing** is the small X-ray your dentist takes by having you bite on a plastic holder — it shows the crowns of upper and lower back teeth in one image, and it is the standard way of checking for decay between teeth. Getting it right requires the sensor flat against the teeth and the X-ray beam aimed straight through the gaps between them. **Miss, and you get an image that cannot be read.** The paper's cited figures: **retake rates of 5% to 20%** for intraoral imaging, with bitewings rejected on average **11.25%** of the time, and in one study **improper angulation (26.1%) and incorrect sensor placement (11.2%)** as the commonest causes. Every retake means another dose of radiation.

**And there is a second, subtler reason that is the paper's best idea.** AI tools that detect cavities on bitewings are typically trained on *clean* images — several of the studies cited here explicitly threw out radiographs with overlap, cone-cutting or motion. So those tools are validated on pictures unlike the ones dentists actually take. Worse, one cited study found its model **mistaking interproximal overlap for a cavity.** So a tool that flags positioning errors *before* the cavity-detector runs would be genuinely useful. The authors put it well: **"The study separates image acquisition quality from diagnostic content."**

**What they did.** 403 bitewings taken by dental students on **three dental radiology mannequins** during 2021 and 2022 assessments, all on the same X-ray machine with one fixed exposure setting. Three dentomaxillofacial radiology lecturers labelled every image by consensus. Then convolutional neural networks — ResNet and DenseNet variants, **trained from scratch, no data augmentation** — were run on six separate tasks with **stratified fivefold cross-validation**.

**The results, and read them in order:**

- **Which side of the mouth, right or left: 99.0%**
- **Cone-cutting error present or absent: 96.3%**
- **Which teeth, premolar or molar: 95.8%**
- **Interproximal overlap present or absent: 93.4%**
- **How severe the cone-cut is, in three grades: 79.3%**
- **Incorrect sensor placement, present or absent: 73.2%**

**Now the thing I found, which is the heart of this entry.**

Two days ago this reading list decoded a review arguing that **a model's measurable accuracy is capped by how reliably the right answer can be defined** — and that the field's obsession with architecture is pushing against a ceiling set by its labels. This paper is the clean test of that argument, because unlike a tumour grade, **every label here is defined by an explicit written rule.** "Premolar bitewing" means the image shows the entire mesial half of the first upper premolar. "Critical cone-cut" means **more than three** interproximal areas are not visible. Correct sensor placement means the biting plane falls in the **green band of a printed template**.

**So: does performance track how precisely each rule is written?**

**Five of the six tasks are simple yes/no choices, and they range from 73.2% to 99.0% — a spread of nearly 26 points with the number of options held constant.** And they line up almost exactly by how much human judgement the label needs. Right versus left is near-pure geometry: 99.0%. Is there a blank white wedge on the image: 96.3%. Does the image show this specific tooth: 95.8%. Do these surfaces overlap past the contact point: 93.4%. **Does the biting plane fall inside a coloured band on a template: 73.2%.**

**And this refutes the paper's own explanation.** The authors attribute the weak results to having more classes — "as we increase the class number and keep the same data set size the accuracy tends to decrease" — and to not having defined the region of interest first. **But incorrect sensor placement is a two-class task, exactly like the 99.0% one, and it scored 73.2%.** Class count cannot explain the worst result at all. What distinguishes it is that its label comes from **cutting a continuous quantity at an arbitrary line.**

**The same pattern appears inside the three-grade task, and it is striking.** The per-class figures: **"Critical" reached an AUC of 94.9 and "Minimal" 94.5 — but "Severe" only 72.2.** The extremes are easy; the middle is where it falls apart. And look at how "Severe" is defined: three or fewer interproximal areas compromised, against "Critical" meaning more than three. **The boundary is a count at three versus four.** Nobody has shown that three humans talking until they agreed drew that line consistently — and nobody can check, because of the next point.

**The reliability of the answer key is not reported, and the method used makes it unmeasurable.** The labels came from one senior lecturer classifying, two more assessing, and then: *"All images were analyzed until investigators reached a consensus."* **There is no kappa, no agreement statistic, no pre-consensus disagreement rate** — and because they deliberated until they agreed, **the data needed to compute one was never created.** One round of blinded independent reads before the discussion would have produced the number at no extra cost.

**On the question this paper was chosen to answer — does anything test whether this transfers from dummies to people? — the answer is no, and the paper could not be clearer about it.** The limitation appears **five separate times**, including in the abstract's conclusion: *"A validation study using patient-acquired bitewing radiographs from clinical settings is required before clinical deployment."* **That is the best scope declaration in this reading list.** A reader cannot possibly mistake what has been shown.

**And the mannequin choice is defensible on a real argument, with a real cost.** The authors note that a phantom "eliminates patient-related variability, allowing for a more focused evaluation of acquisition-related faults" — and they are right, because a positioning error is something the *operator* does, not something the patient has. **But patients are precisely what make positioning hard**: gagging, a shallow palate, crowded teeth, movement. So the phantom isolates the thing being measured *and* removes the main source of difficulty. Both are true at once.

**One more caution the paper does not raise.** There were **three mannequins**, and the cross-validation was done **at the image level**. The paper assures us "no identical image appeared in both training and validation sets" — which rules out duplicates but not the real problem: **with only three anatomies, every fold contains images of all three.** For "which side" and "which teeth," which are anatomical judgements, a network can learn *this is mannequin two's left molar region* rather than left-versus-right in general. **That 99.0% is consistent with the task being close to trivial on three fixed skulls.**

## 2. Study Snapshot

**Study type:** retrospective development and internal cross-validation of six independent image classifiers, on radiographs acquired from **dental training mannequins**. **No patient data, no external validation, no prospective component, no clinical outcome.** All of these are stated.

**Setting and data.** University of Sydney, Dentomaxillofacial Radiology discipline. **403 bitewings** acquired from **three mannequins of the same Nissin X-ray phantom** during regular assessment periods in **2021 and 2022**, taken by students in the Bachelor of Oral Health and Doctor of Dental Medicine programmes — so by **different students across different assessment periods.**

**Acquisition, reported in full.** Heliodent Plus intraoral X-ray unit (Dentsply Sirona), focal spot **0.4 mm**, pre-programmed bitewing setting: **70 kV, 7 mA, 0.10 s.** Photostimulable phosphor plate receptors (Air Techniques) with cardboard loop film holders. Saved as JPEG at **1980 × 1486**, then **downsampled to 512 × 512** for the models.

**The reference standard.** A senior Dentomaxillofacial Radiology lecturer with **over 8 years of experience** selected and classified the images; **two further lecturers** then assessed them; and **"All images were analyzed until investigators reached a consensus on the presence of each positioning error. This was then considered the ground truth for training and validating the AI models."**

**And the labels are operationally defined, which is what makes this entry a test case.** **Bitewing type:** premolar requires the entire mesial half of the first maxillary premolar to be visible; molar requires at least half of the most posterior erupted third molar, or the entire distal surface of the last erupted molar. **Side:** "based on the orientation of the image and the anatomical structures visible." **Cone-cutting error:** "a well-defined, radiopaque, non-exposed area due to improper alignment of the X-ray beam with the receptor." **Cone-cut severity, in three grades:** *Minimal* does not affect the region of interest; *Severe* partially affects it, "compromising three or fewer interproximal areas"; *Critical* means "more than three interproximal areas are not visible," rendering the radiograph non-diagnostic. **Interproximal overlap:** proximal surfaces superimposed "extending beyond the contact point," with two explicit exceptions — the mandibular canine to first premolar contact in premolar views, and partly erupted third molars in molar views. **Incorrect receptor placement:** judged with **a printed template** — the occlusal plane in the **green band** is correct, in the **yellow band** is incorrect, outside the yellow band is unacceptable.

**The six tasks and their class counts**, which I verified all reconcile exactly: **bitewing type** (premolar 208, molar 195; total 403); **side** (right 173, left 230; 403); **cone-cut binary** (present 179, absent 224; 403); **cone-cut three-class** (critical 70, severe 61, minimal 48; 179 — matching the 179 "present" cases exactly); **interproximal overlap** (present 171, absent 162; 333); **incorrect receptor placement** (present 155, absent 177; 332).

**The exclusion chain is fully traceable.** All 70 critical cone-cut images were excluded from the overlap and receptor-placement assessments as non-diagnostic: **403 − 70 = 333**, as stated. One further image was excluded from the receptor-placement task for a partial crown cut-off: **333 − 1 = 332**, as stated.

**Training.** **ResNet34, ResNet50, DenseNet121, DenseNet161 and DenseNet169** as baselines for every task, **trained from scratch** for **200 epochs** on an NVIDIA RTX 2080 Ti. Adam optimizer, binary cross-entropy for two-class tasks and cross-entropy for the three-class task, **default PyTorch weight initialisation**, and — stated plainly — **"without learning rate scheduling or additional regularization"** and **"No data augmentation was applied."** Pixel values scaled and mean-variance normalised. **"Random seeds were not fixed."** Each task treated independently with **stratified fivefold cross-validation**, performed **"at the image level, with each radiograph assigned to only one fold; therefore, no identical image appeared in both training and validation sets."**

**Model and hyperparameter selection, per task.** The paper states that within a task the same configurations were applied across all CNNs "to allow fair comparison," and **Table 1 reports a different winner and a different learning rate for each task**: bitewing type DenseNet169 (lr 5e-05, batch 8); side DenseNet121 (5e-04, 8); cone-cut binary DenseNet161 (1e-04, 4); cone-cut three-class DenseNet121 (5e-04, 4); overlap DenseNet161 (5e-05, 4); receptor placement ResNet34 (5e-04, 4).

**Metrics.** Accuracy, precision, recall, F1 and AUC, **reported as mean ± standard deviation across the five folds**, with per-class figures for every task and a confusion matrix for the three-class task.

**Results, from the paper's own tables.** **Bitewing type: accuracy 95.8 ± 3.0, AUC 99.3 ± 1.0.** **Side: accuracy 99.0 ± 0.6, AUC 99.3 ± 0.7.** **Cone-cut binary: accuracy 96.3 ± 1.8, AUC 98.6 ± 2.0**, with per-class recall of **92.7 ± 3.2 for "present"** against 99.1 ± 1.2 for "absent." **Cone-cut three-class: accuracy 79.3 ± 5.7**, with per-class AUC of **94.9 ± 1.9 (critical), 72.2 ± 3.8 (severe), 94.5 ± 4.6 (minimal)**. **Interproximal overlap: accuracy 93.4 ± 5.2, AUC 97.8 ± 2.3.** **Incorrect receptor placement: accuracy 73.2 ± 8.3, AUC 79.4 ± 8.0**, with F1 of 75.5 for "present" against 70.4 for "absent."

**What the authors conclude, accurately.** "Our results indicate that an automated system of DL models **in a controlled mannequin-based setting** is capable of satisfactorily detecting and classifying most of the common positioning errors," with accuracies of 93%–99% for type, side, binary cone-cut and overlap, and **"a moderate level of performance, with an overall accuracy of 73.2%"** for receptor placement.

**A proposed workflow, which is sensible.** Classify and grade the cone-cut first; exclude critical (non-diagnostic) images; then assess the other positioning errors; then detect oral pathology.

**And they name the asymmetric cost of errors.** **"False negatives should be identified for critical cone-cutting errors or severe overlap, as this would lead to non-diagnostic images passing unnoticed, while false positives could lead to unnecessary retakes and additional radiation exposure."**

**Honest comparison with prior work, including where they lose.** The paper reports that a previous study reached **97.56%** on recognising inverted images with ResNet-34, and another reached **100%** on left/right using DenseNet-121 **pre-trained on ImageNet with fine-tuning, on 1,000 bitewings.** Against that, this study used DenseNet-121 **without transfer learning**, on 403 images, and got 99.0% — which the authors read as challenging the assumption that transfer learning is needed for small datasets, while immediately adding: **"our study has used mannequin radiographs; further investigation in clinical data should be conducted to confirm such findings."**

**Limitations the authors state.** The dataset "was relatively small; however, it was carefully selected and structured to ensure class balance." Classification "may not be optimal for detecting all types of positioning errors," though it is the usual first stage and costs less computation than segmentation or object detection. **"the study was conducted using radiographs obtained from mannequins, which, although standardized, do not fully capture the variability seen in clinical settings."** And the **512 × 512 downsampling "introduces some loss of detail,"** defended on grounds that clinically relevant structures remain discernible and that prior work finds comparable performance on downsampled images.

**Not reported or not retrievable:** **any inter-rater agreement statistic** on the reference standard; **any held-out test set** — the reported figures are the cross-validation scores; **the complete ethics approval number**; how many of the 403 images came from each of the three mannequins; any mannequin-level (grouped) cross-validation; the results of the four non-winning architectures on each task; any reporting guideline; all figures, including the confusion matrix and the template images; and Supporting Files 1 and 2.

## 3. How Strong Is This Evidence? (Grade 3 out of 5)

**This is a modest, competent, narrowly-scoped study whose claims are calibrated almost exactly to its evidence, and whose value to this reading list exceeds its value to dentistry. It earns a 3 by being honest about a small result rather than by being a big one.**

**What is genuinely well done.**

**The scope declaration is the best in this entire run.** The mannequin limitation appears in the stated objective, in the abstract's conclusion, twice in the Discussion, and in the limitations — **five times, including "A validation study using patient-acquired bitewing radiographs from clinical settings is required before clinical deployment" in the abstract.** No reader can misunderstand what has and has not been shown. Compare entry 78, where a paper's abstract claimed "strong performance across 2 OCT devices" while its own intervals showed degradation.

**Every label is operationally defined in writing.** Not "an expert judged the positioning adequate," but a named anatomical landmark, a count of affected interproximal areas, a colour band on a template. **That is a materially better reference standard than anything else in this run**, and it is what makes the paper useful as a test case.

**Uncertainty is reported on every single metric.** Mean ± standard deviation across five folds, for accuracy, precision, recall, F1 and AUC, **per class and overall.** This is how the weakness of the receptor-placement task becomes visible — 73.2 ± 8.3 — and most papers would have printed a bare 73.2%.

**Per-class metrics and a confusion matrix for the three-class task**, which is the only reason anyone can see that the failure sits specifically in the "Severe" middle category at AUC 72.2 while the extremes reach ~95.

**All six task tables reconcile exactly, and the exclusion chain is fully traceable** — 403 to 333 to 332, with every class count summing correctly. I checked all nine reconciliations and every one passed.

**The methods are reported to a level that permits replication**: device, focal spot, kV, mA, exposure time, receptor type, native and downsampled resolution, GPU, optimizer, loss function, epochs, initialisation, and the explicit statements that there was **no augmentation, no learning-rate scheduling and no extra regularisation.**

**"Random seeds were not fixed" is disclosed** — a small, honest sentence that most papers omit.

**They name the asymmetric cost of false negatives against false positives**, which is the correct framing for a quality-control tool: a missed cone-cut sends a non-diagnostic image into clinical use, while a false alarm means a needless retake and extra radiation.

**They report a competitor beating them** — a prior study reaching 100% on left/right with transfer learning on 1,000 images.

**Funding explicitly none, conflicts explicitly none**, Declaration of Helsinki, and the framing contribution — separating acquisition quality from diagnostic content — is a real idea that the cavity-detection literature needs.

**So why 3.**

**The reliability of the reference standard is not reported, and the labelling method destroyed the data needed to measure it.** Consensus-to-agreement means three raters deliberated until they concurred. **No independent reads exist, so no kappa can ever be computed from this dataset.** For a paper whose entire premise rests on label quality, and whose weakest tasks are precisely the ones with the most judgement in their labels, this is the central gap. One blinded round before discussion would have fixed it.

**There is no held-out test set.** Five architectures and a learning rate were selected **per task**, and the reported accuracies **are the cross-validation scores on the same folds used to make that selection.** The reported number is therefore a maximum over five models, which is optimistic by construction — the same order-statistic problem as yesterday's entry, where a winner's internal score of 0.921 fell to 0.829 on genuinely held-out data. **Here there is no equivalent of that 0.829.**

**Three mannequins, cross-validated at the image level.** Every fold contains images of all three anatomies, so for the two anatomical tasks a model can memorise three skulls instead of learning a general rule. The paper's assurance about duplicate images does not address this. **For the positioning-error tasks the concern is genuinely weaker** — those errors are operator-induced and vary within mannequin — and I am weighting it accordingly.

**The two clinically useful tasks are the two that failed.** Knowing *whether* there is a cone-cut (96.3%) matters less than knowing *whether it ruins the image* (79.3%), and incorrect receptor placement — the second commonest cause of retakes in the literature the paper itself cites — came in at **73.2%, with a fold-to-fold interval running roughly 63% to 84%.** The paper says so, honestly, in its abstract and conclusion. It remains the case that the useful half did not work.

**403 images, and the weak tasks' fold variation is large.** Converting the standard deviations into intervals: the receptor-placement accuracy is consistent with anything from about **63% to 84%**, and overlap with anything from about **87% to 100%**.

**No transfer test to patients** — declared, so this is a boundary on the claim rather than a hidden flaw, but it means nothing here speaks to clinical performance.

**No reporting guideline.** CLAIM covers exactly this study type.

**Why not 2.** Because entry 77 scored a 2 for claiming screening from cross-sectional data with its label possibly inside its inputs — a mismatch between claim and evidence. **Here there is no mismatch at all.** The title says mannequin, the abstract says mannequin, the conclusion says a patient study is required first. Everything claimed is shown, and everything not shown is named.

**Why not 4.** Because the grade tracks what a reader can take away, and what a reader can take away is that **a CNN can identify bitewing type, side and the presence of a cone-cut on three plastic dummies, and cannot reliably grade severity or detect misplacement.** The evidence base is 403 images of three phantoms with no held-out set, no label-reliability data, and no patient test.

**What would make this a 4, concretely.** **Run one blinded round of independent reads before the consensus discussion and report the kappa** — this is the single highest-value addition and costs nothing but an afternoon. **Hold out a test set**, or at minimum report the four losing architectures so a reader can see the selection spread. **Cross-validate grouped by mannequin** — with three groups that means three-fold leave-one-mannequin-out, which would directly test whether the anatomical tasks generalise. **And report how many images came from each mannequin.** All four use data the authors already have.

## 4. The Editor's Concerns

**1. Performance tracks how precisely each label is defined, and that is the most important thing in this paper.** Five of the six tasks are two-class problems, and they span **73.2% to 99.0% — nearly 26 points with the number of options held constant.** Ordered: side 99.0 (near-pure image geometry), cone-cut present/absent 96.3 (a visually unmistakable white wedge), type 95.8 (one named anatomical landmark), overlap 93.4 (a contact-point rule with two exceptions), **receptor placement 73.2 (fit a template and decide which colour band a curve falls in).** Two days ago this list decoded a review whose thesis was that measurable accuracy is capped by reference-standard quality rather than by algorithm. **This paper is the stable-label test of that thesis and it confirms it** — the harder the label is to apply consistently, the worse the model does, with architecture, dataset and image quality held essentially constant across tasks.

**2. The paper's own explanation is refuted by its own table.** The authors attribute the drop to class count: *"It is expected, as we increase the class number and keep the same data set size the accuracy tends to decrease."* **But incorrect receptor placement is a two-class task — present 155, absent 177 — and it scored 73.2%, against 99.0% for the two-class side task.** Class count cannot explain a 25.8-point gap between two binary problems. It is at most a partial account of the three-class drop and **no account whatever of the worst result.** Their second explanation — the region of interest was not defined beforehand — is more plausible and still does not reach receptor placement, which needs no region of interest, only the occlusal plane's position.

**3. The middle of the ordinal scale is where it breaks, and the boundary is a count at three versus four.** Per-class AUC on the three-grade task: **Critical 94.9, Minimal 94.5, Severe 72.2** — a 22-point hole in the middle. "Severe" is defined as compromising **three or fewer** interproximal areas and "Critical" as **more than three.** So the boundary that the model cannot find is a threshold on a countable quantity at exactly 3 versus 4. **The authors see the pattern and attribute it to the undefined region of interest.** The complementary reading: there is no evidence that three raters talking until they agreed placed a 3-versus-4 line consistently, and because of concern 4 there is no way to check.

**4. No agreement statistic, and the labelling method made one impossible.** *"All images were analyzed until investigators reached a consensus."* Consensus-to-agreement is a reasonable way to produce labels and **a terrible way to produce evidence about labels**, because it erases the independent reads a kappa requires. **No kappa, no ICC, no pre-consensus disagreement rate** — not withheld, but never generated. For a study whose weakest tasks are its most judgement-laden, and which exists to improve data quality for other people's models, **the quality of its own labels is unmeasured.** The fix is one blinded round before the discussion.

**5. There is no held-out test set, and the reported numbers are selection scores.** Five architectures per task plus a learning rate, with **a different winner and a different learning rate for each of the six tasks** — and the accuracies reported are the cross-validation results on the folds that chose them. **A maximum over five candidates is biased upward by construction.** Yesterday's entry showed the size of that effect concretely: an internal winner at 0.921 landed at 0.829 on data never used for selection. **This paper has no equivalent figure**, so the honest reading is that the true held-out performance is somewhat below every number in its tables, by an unknown amount.

**6. Three mannequins, and cross-validation at the image level.** The paper writes that folds were assigned so that "no identical image appeared in both training and validation sets" — which excludes duplicates and not the grouping problem. **With three phantoms, every fold contains images of all three.** For *side* and *type* — judgements about anatomy — a network can learn to recognise three specific skulls rather than a general left/right or premolar/molar rule, and **99.0% on left/right across three fixed anatomies with one exposure setting is consistent with the task being nearly trivial.** The paper interprets its 99.0% from scratch as evidence that transfer learning is unnecessary for small datasets; the simpler reading is that the task is easy here. **In fairness, for the positioning-error tasks the concern is much weaker**, since those errors are operator-induced and vary within mannequin. **The decisive experiment is cheap: three-fold leave-one-mannequin-out.**

**7. The two tasks that would matter clinically are the two that underperformed.** A tool that says "there is a cone-cut somewhere" (96.3%) is less useful than one that says "this cone-cut has destroyed the image" (79.3%). And **incorrect receptor placement — which the paper's own cited literature puts at 11.2% of retake causes, second only to angulation — reached 73.2%, with a fold interval of roughly 63% to 84%.** The paper reports this plainly in both abstract and conclusion rather than burying it, which is to its credit. **The honest summary is that the system works on the parts that were already easy.**

**8. The phantom isolates the construct and removes the difficulty, and only the first half is argued.** The authors' defence is genuinely good: a positioning error is something the **operator** does, so eliminating patient variability "allow[s] for a more focused evaluation of acquisition-related faults." **Correct.** The unargued half: patients are *why* positioning is hard — gag reflex, shallow palate, crowded or tilted teeth, tori, movement. **A phantom removes both the confound and the challenge.** So the study measures whether a network can detect operator error under the easiest possible conditions, which is a reasonable first step and should not be read as a performance estimate for anything else. **The paper's five-fold repetition of the mannequin caveat means it is not read that way, which is the point of saying it five times.**

**9. The 403 images carry large fold-to-fold variation on exactly the tasks that matter.** Converting the reported standard deviations into intervals around the five-fold mean: receptor placement runs about **63% to 84%**, the three-class task about **72% to 86%**, and overlap about **87% to 100%**. Meanwhile side runs **98.3% to 99.7%.** **The standard deviation spans a fourteen-fold range across tasks and it tracks the same ordering as the accuracy** — crisper labels give both higher means and tighter folds, which is itself evidence for concern 1.

**10. Training from scratch with no augmentation on 403 images, presented as a methodological finding.** The authors write that their result "challenge[s] th[e] assumption" that transfer learning and fine-tuning are needed for small datasets. **That claim is carried almost entirely by the left/right task**, which is the most nearly deterministic of the six, on three fixed anatomies. On the tasks where learning actually had to happen, performance was 73–79%. **The authors do caveat the claim** — but the caveat they offer is about mannequins rather than about the task being easy, and the latter is the more relevant objection.

**11. The ethics approval number is incomplete in the published text.** Both the Methods and the Ethics Statement give "approval number: 2024/" with nothing after it. Almost certainly a typesetting artefact rather than anything substantive, and I note it only because **I cannot report a verifiable approval number** and will not invent one. Approval by the University of Sydney Ethics Committee and compliance with the Declaration of Helsinki are both stated.

**12. No reporting guideline, which ends a two-entry run.** The tally across this stretch: entries 71, 73, 74, 75, 77, 78 named none; 69 named TRIPOD+AI with the checklist; 70 named STROBE; **76 measured the phenomenon at 40% mean completeness**; **79 named six instruments and applied them; 80 named TRIPOD and deposited a checklist; and 81 names none.** **CLAIM exists precisely for medical-imaging AI** and would have asked for the two things most missing here: the reliability of the reference standard, and a validation set separate from the selection set. **So the standing rule holds in both directions now.** Naming a guideline does not predict quality — entry 79 was the best-argued paper in the run and entry 69 was not the most careful. **And this entry is the counterpart: a paper that is scrupulously honest about its scope while omitting the two specific checks an imaging checklist would have required.** Honesty about limits and completeness of method are different virtues, and this paper has the first without the second.

## 5. Statistics Spotlight

Three concepts, numbered from 316 in the running list in `queue.md`. The first is the payoff of a question written down two days ago.

**When every label has a written rule, you can watch accuracy track the rule's precision — and that is the reference-standard ceiling made visible.**

Two days ago this reading list decoded a review arguing that **a model's measurable accuracy is capped by how reliably the right answer can be defined**, not by the algorithm. The trouble with testing that argument is that most medical labels are noisy in ways nobody has measured. **This paper is unusual: every one of its labels is defined by an explicit written rule**, so you can rank the rules by how much judgement they need and see whether performance follows.

Here are the rules, roughly ordered from mechanical to judgemental, with what the network scored:

- **Side, right or left — 99.0%.** Determined by "the orientation of the image and the anatomical structures visible." Essentially a geometric fact about the picture.
- **Cone-cut present or absent — 96.3%.** "A well-defined, radiopaque, non-exposed area." A blank white wedge. You either see one or you do not.
- **Type, premolar or molar — 95.8%.** One named landmark: the entire mesial half of the first upper premolar must be visible.
- **Interproximal overlap — 93.4%.** Surfaces superimposed "extending beyond the contact point," with two named exceptions. A rule with edge cases.
- **Cone-cut severity, three grades — 79.3%.** Count how many interproximal areas are compromised; the Severe/Critical line sits at three versus four.
- **Incorrect receptor placement — 73.2%.** Lay a printed template over the image and decide whether the biting plane falls in the green band or the yellow one.

**Five of those six are simple yes-or-no tasks, and they run from 73.2% to 99.0% — a spread of nearly 26 points with the number of choices held constant, the same images, the same architectures, the same dataset size.** The only thing that changes is how much interpretation the rule demands.

**And the paper's own explanation fails on its own numbers.** The authors say accuracy fell because the number of classes rose. But **receptor placement has two classes, like the 99.0% task, and scored 73.2%.** Class count explains nothing about the worst result.

**Why this is the ceiling argument and not just "some tasks are harder."** It is both, and the point is *why* they are harder. **A network can only learn a rule as consistent as the rule it was taught.** If three experts drawing a line at "green band versus yellow band" place that line slightly differently on borderline images — and nothing in the paper shows they did not — then the training labels contain genuine contradictions. **The model cannot learn a boundary that the labellers did not agree on, and it cannot be measured above the consistency of the labels it is scored against.**

**The everyday version.** Give three teachers a pile of essays and three marking tasks. First: "is this essay in English or French?" They will agree every time, and a student could learn that rule perfectly. Second: "does this essay contain the word *however*?" Still near-perfect. Third: "is the argument *moderately* persuasive, as opposed to *very* or *slightly*?" **Now they will disagree on half the pile, and any student trying to learn their standard will seem to be performing badly — when actually there is no single standard there to learn.** The student's score measures the teachers' consistency as much as the student's skill.

**Watch out for:** a paper reporting several tasks at very different accuracies and explaining the spread by **model capacity, class count, or dataset size** without ever asking how consistently each label was assigned. **The question to ask is: for each task separately, what was the rule, and how reliably can humans apply it?** And the diagnostic pattern to look for is the one in this paper — **when accuracy orders itself by how judgemental the label is, with everything else constant, the ceiling is in the labels.**

**Consensus labelling produces good labels and destroys the evidence about them.**

This paper's reference standard came from one senior lecturer classifying every image, two further lecturers assessing them, and then: *"All images were analyzed until investigators reached a consensus on the presence of each positioning error. This was then considered the ground truth."*

**That is a perfectly reasonable way to produce labels.** Three experts arguing to agreement will usually land closer to the truth than any one of them alone. **It is also a way of making the reliability of those labels permanently unmeasurable**, and that trade is almost never acknowledged.

**Here is the mechanism.** To measure agreement you need **independent** judgements — two or more people scoring the same case **without seeing each other's answers**. Then you count how often they matched, correct for the matches luck would produce, and report a **kappa**. **Consensus deliberation produces exactly one answer per case.** There is no second, independent opinion to compare it against, because the second opinion was merged into the first by discussion. **The disagreement that existed before the conversation is gone, and no analysis can recover it.**

**So this paper reports no kappa, no ICC and no disagreement rate — and it could not have, from the data it generated.** That is not concealment. It is a design choice whose cost was not noticed.

**The fix costs an afternoon.** Have the three raters score a sample — a couple of hundred images would do — **blinded and independently, first.** Compute the kappa on that. *Then* convene and deliberate to produce the final labels. **You get the same high-quality consensus ground truth, plus a number telling the reader how hard the labels were to assign.** And for this paper that number would have been genuinely interesting, because it would have let a reader check the central pattern directly: if the kappa for receptor placement is much lower than for side, concern 1 is confirmed outright rather than inferred.

**The everyday version.** Three judges score a diving competition by conferring and announcing one agreed number per dive. The scores are probably excellent. **But you can never find out whether they were an easy crowd or a divided one, because you only ever see the agreed figure.** If instead each judge wrote a private score before they conferred, you would know both the final verdict *and* how much disagreement it papered over — and on contested dives, that second fact is the one you want.

**Watch out for:** "labelled by consensus," "adjudicated by a panel," "reviewed until agreement was reached" — all of which signal good labels and no reliability data. **Two questions. Were there independent reads before the discussion, and what was the agreement? And if not, is the reliability of this reference standard being treated as a non-issue?** The asymmetry is worth remembering: **a paper reporting a kappa of 0.65 has told you something useful; a paper reporting consensus has told you nothing, and the second looks more authoritative.**

**Report the fold-to-fold spread — and notice when it tracks task difficulty.**

This paper does something most do not: **it reports a standard deviation on every single metric**, across the five cross-validation folds. That turns out to be where the real information is.

**Why a mean alone misleads.** Fivefold cross-validation splits the data into five parts, trains on four and tests on the fifth, five times over, then averages. **The average hides how much the five results differed.** Two tasks can both average 85% while one scored 84-85-85-85-86 and the other scored 70-78-85-92-100. Those are not the same finding.

**Here is this paper's spread, with the standard deviations converted into approximate 95% intervals around the five-fold mean** (standard error is the SD divided by the square root of 5, and with only four degrees of freedom the multiplier is about 2.8):

- **Side: 99.0 ± 0.6 → roughly 98.3% to 99.7%**
- **Cone-cut binary: 96.3 ± 1.8 → roughly 94.1% to 98.5%**
- **Type: 95.8 ± 3.0 → roughly 92.1% to 99.5%**
- **Overlap: 93.4 ± 5.2 → roughly 86.9% to 100%**
- **Cone-cut three-class: 79.3 ± 5.7 → roughly 72.2% to 86.4%**
- **Receptor placement: 73.2 ± 8.3 → roughly 62.9% to 83.5%**

**So "73.2%" is really "somewhere between about 63% and 84%,"** on 332 images. That is the difference between a tool worth building and one that is not.

**And here is the finding inside the finding.** The standard deviations run from **0.6 to 8.3 — a fourteen-fold range — and they order themselves exactly like the accuracies do.** The tasks with crisp labels have both **higher means and tighter folds**; the judgement-heavy tasks have both lower means and wilder folds. **That is a second, independent signature of the same thing Section 5's first item describes:** inconsistent labels make a model both worse on average *and* more dependent on which particular images landed in which fold.

**One honest caveat about these intervals.** "Random seeds were not fixed," which the paper discloses. So part of the fold-to-fold variation is training randomness rather than data variation, and the intervals above should be read as rough rather than exact.

**The everyday version.** Two restaurants both average three and a half stars. One has fifty reviews all saying "three or four stars, perfectly fine." The other has twenty-five five-star reviews and twenty-five two-star reviews. **Same average, completely different restaurant** — and the second one tells you that something inconsistent is going on in the kitchen. **A wide spread is not just imprecision; it is a clue.**

**Watch out for:** cross-validation results reported as a bare mean with no spread, which is still the norm. **Ask for the standard deviation or the per-fold numbers**, and convert to an interval before deciding whether a result is useful. **And when you have spreads for several tasks, compare them** — if the noisy tasks are the ones with the most subjective labels, you have learned where the problem is.

## 6. Jargon Translator

**Bitewing radiograph (BW)** — the small dental X-ray taken by biting on a holder, showing the crowns of upper and lower back teeth together. The standard view for checking decay between teeth and bone levels.

**Premolar / molar bitewing** — which region the image covers. Defined here by named landmarks: a premolar view must show the entire mesial half of the first upper premolar.

**Mesial / distal / proximal** — toward the front of the mouth, toward the back, and the side surfaces where two teeth touch. **Interproximal** means between adjacent teeth — where decay hides and where overlap ruins the view.

**Occlusal plane** — the imaginary surface along which upper and lower teeth meet. Its position in the image is what the receptor-placement template measures.

**Curve of Spee** — the natural front-to-back curve of the biting surfaces. A correctly placed receptor shows the occlusal plane flat or rising from the midline; deviation signals misplacement.

**Positioning error (technical error)** — a fault caused by how the image was taken, not by anything in the patient. **Operator-induced, which is why a mannequin is a defensible test bed.**

**Cone-cutting error (CCE)** — a blank, bright, unexposed wedge where the X-ray beam missed part of the sensor. Graded here as minimal, severe or critical by how many interproximal areas it hides.

**Interproximal overlap** — adjacent teeth superimposed so the surface between them cannot be seen. **Caused by wrong horizontal beam angulation, and a known cause of AI tools mistaking overlap for decay.**

**Incorrect receptor placement** — the sensor positioned so upper and lower teeth are not evenly captured. Judged here by a colour-banded template. **The weakest task, at 73.2%.**

**Retake rate** — how often an image must be repeated because it is unreadable. Cited here at 5%–20% for intraoral imaging, averaging 11.25% for bitewings. **Every retake is extra radiation.**

**Dental radiology mannequin / X-ray phantom** — a plastic head-and-jaw model with real or simulated teeth, used to train and assess students. **Three were used here.** No soft tissue, no movement, no anatomical variation, no disease.

**Photostimulable phosphor (PSP) plate** — a reusable flexible X-ray sensor, scanned after exposure. An alternative to film or a rigid digital sensor.

**Convolutional neural network (CNN)** — an image model that learns small local patterns and builds them into larger ones. **ResNet** and **DenseNet** are two standard families; the numbers (34, 121, 161, 169) count layers.

**Trained from scratch** — starting from random weights rather than from a model pre-trained on millions of general photographs. **Unusual on only 403 images, and disclosed here.**

**Transfer learning / fine-tuning** — starting from a pre-trained model and adapting it. Normally recommended for small datasets; this paper reports managing without it on its easiest task.

**Data augmentation** — artificially enlarging a dataset by rotating, flipping or shifting images. **Not used here**, stated.

**Stratified fivefold cross-validation** — split the data into five parts keeping the class mix even, train on four, test on the fifth, and repeat five times. **"Stratified" refers to class balance, not to grouping by mannequin** — see concern 6.

**Accuracy, precision, recall, F1** — the share of all predictions correct; the share of flagged cases that really were; the share of real cases caught (also called sensitivity); and the harmonic mean of the last two.

**AUC** — the chance the model ranks a true positive above a true negative. 0.5 is a coin flip.

**Confusion matrix** — a grid of what was predicted against what was true, which is how the "Severe" failure becomes visible.

**Standard deviation across folds** — how much the five cross-validation results differed from each other. **Reported on every metric here, which is good practice** — technique 318.

**Kappa** — agreement between independent raters, corrected for chance. **Not reported here, and not computable from this design** — technique 317.

**Consensus labelling** — experts discussing until they agree on one label. Good labels, no reliability data — technique 317.

**Region of interest (ROI)** — the part of the image that actually matters diagnostically. The authors argue that not defining it in advance is why severity grading struggled.

**CLAIM** — the Checklist for Artificial Intelligence in Medical Imaging, the reporting standard for exactly this kind of study. Not named here.

## 7. What You Can (and Can't) Say

**You can say:**

"In 403 bitewing radiographs taken by dental students on three dental radiology mannequins, convolutional neural networks trained from scratch classified bitewing type with 95.8% accuracy, side with 99.0%, the presence or absence of a cone-cutting error with 96.3%, and the presence or absence of interproximal overlap with 93.4%, under stratified fivefold cross-validation."

"Performance was weaker on the two more demanding tasks: 79.3% for grading cone-cut severity into three classes, and 73.2% for detecting incorrect receptor placement."

"Within the three-grade severity task, per-class AUC was 94.9 for 'critical' and 94.5 for 'minimal' but only 72.2 for the intermediate 'severe' category."

"The study reports standard deviations across folds on every metric, ranging from ±0.6 for side classification to ±8.3 for receptor placement."

"All labels were operationally defined — by named anatomical landmarks, by a count of affected interproximal areas, and by a colour-banded template for receptor placement — and assigned by consensus among three dentomaxillofacial radiology lecturers."

"The authors state that a validation study using patient-acquired bitewing radiographs is required before clinical deployment, and repeat the mannequin limitation in the objective, the abstract conclusion, the discussion and the limitations."

"The authors note the asymmetric cost of errors: a missed critical cone-cut lets a non-diagnostic image pass, while a false alarm causes an unnecessary retake and additional radiation."

**You cannot say:**

"This system can assess dental radiograph quality in practice." **No patient radiographs were used and no transfer was tested.** The paper's own abstract says a clinical validation study is required first.

"The system detects positioning errors with 93%–99% accuracy." **That range covers the four easier tasks only.** The two more clinically consequential tasks scored 79.3% and 73.2%, and the paper says so.

"Accuracy of 73.2% for receptor placement." **Better stated as roughly 63% to 84%**, derived from the reported ±8.3 across five folds on 332 images.

"These are held-out test results." **They are cross-validation scores on the same folds used to select the architecture and learning rate** — a different winner was chosen for each of the six tasks from five candidates, with no separate test set.

"The reference standard was reliable." **Unmeasured, and unmeasurable from this design.** Consensus-to-agreement produced one label per image and no independent reads, so no kappa exists.

"More classes caused the lower accuracy." **The paper's explanation, and its own data contradict it** — receptor placement is a two-class task and scored 73.2% against 99.0% for the two-class side task.

"Transfer learning is unnecessary for small dental imaging datasets." **That claim rests mainly on the left/right task**, the most nearly deterministic of the six, on three fixed anatomies. On the tasks requiring real learning, performance was 73%–79%.

"The model learned to recognise left from right." **Possibly, and possibly it learned three mannequins.** Cross-validation was at image level, so all three anatomies appeared in every fold.

"Mannequin radiographs are a reasonable proxy for patients." **For isolating operator error, the authors' argument is good.** But a phantom has no soft tissue, no gag reflex, no crowding and no movement — it removes the main sources of positioning difficulty along with the confounding.

**The honest one-sentence version:** *a small, careful, scrupulously-scoped study showing that a neural network trained on 403 student-acquired radiographs of three plastic dummies can tell left from right, premolar from molar, and the presence of a blank wedge on the image, while failing at the two tasks that would actually matter — and whose real value is that, because every label came with a written rule, its six accuracies line up almost perfectly by how much judgement each rule requires, confirming on crisp labels what a review two days earlier argued about noisy ones.*

## 8. Bottom Line for Your Life

**If you are a dental patient:** nothing here changes anything about your care, and there is no tool to ask for. **The one fact worth knowing is the one the paper cites rather than the one it produces:** somewhere between 5% and 20% of intraoral dental X-rays have to be retaken because of how they were taken, and bitewings average around 11%. Each retake is a small additional dose of radiation. **If you are asked to repeat an X-ray, that is ordinary and it is usually about beam angle or sensor position, not about anything found in the first image.**

**If you are a dental educator:** this is the setting where the paper's result is actually usable, and the authors say so. Automatically flagging type, side and the presence of a cone-cut on student mannequin radiographs **would work at the accuracies reported here**, and it would give students immediate feedback on mounting and gross positioning without an instructor present. **What it would not do reliably is tell a student whether their cone-cut ruined the image (79.3%) or whether their sensor was misplaced (73.2%)** — and those are the two things a student most needs told.

**If you build or evaluate medical imaging AI, this entry supplies one cheap habit and one cheap experiment.** **The habit: before you label anything by consensus, have your raters score a few hundred cases blind and independently first, and report the agreement.** You keep the consensus labels and you gain a number that tells every future reader — and you — how hard your labels were to assign. It costs an afternoon and it is the single most valuable thing missing from this paper. **The experiment: if your data comes from a small number of subjects, sites, devices or phantoms, cross-validate grouped by that unit, not by image.** Here that means three-fold leave-one-mannequin-out, which would settle in one run whether the model learned anatomy or learned three specific skulls.

**If you read papers, this entry is a worked example of a diagnostic worth having.** When a study reports several tasks at very different accuracies, **do not accept "more classes" or "harder problem" as the explanation. Line the tasks up by how precisely each label is defined and see whether performance follows.** Here it does, almost perfectly, across five tasks that all have exactly two options — and that tells you the limiting factor is the answer key, not the algorithm. **The same check works on any multi-task paper and takes two minutes.**

**And the thing worth taking from how this paper is written, regardless of its findings.** It states its central limitation **five times** — in the objective, the abstract conclusion, twice in the discussion and in the limitations — including the sentence "A validation study using patient-acquired bitewing radiographs from clinical settings is required before clinical deployment" in the abstract itself. **Three days ago this reading list looked at a paper whose abstract claimed strong cross-device performance while its own confidence intervals showed degradation.** The contrast is instructive: **a modest result that cannot be misread is more useful than an impressive one that can.**

**If you are reading the coverage:** there probably will not be any, and that is correct. **This is a small methodological study that says so about itself.** If it is ever written up as "AI checks dental X-ray quality," the two things missing will be that no patient images were involved at all, and that the two error types a dentist would most want flagged are the two it detected least well.

**This is education, not medical advice.** Nothing here concerns any diagnosis or treatment. If you have questions about dental X-rays or radiation exposure, those belong with your own dentist.

---

## Appendix: the pre-registered questions, verification, restock, and status on 2026-11-18

**Both pre-registered questions, answered.** Set yesterday, written down before reading.

**(1) "Does anything in the paper test transfer from mannequin to patient?"** — **Nothing does, and the paper says so five separate times**, including in the abstract's conclusion: *"A validation study using patient-acquired bitewing radiographs from clinical settings is required before clinical deployment."* Also in the stated objective ("in a controlled mannequin-based setting"), twice in the Discussion (*"These results should be viewed in light of the BWs taken from mannequins, which may have contributed to this high overall accuracy"*; *"further investigation in clinical data should be conducted"*), and in the limitations. **This is the best scope declaration in this reading list**, and it converts what would otherwise be a fatal gap into a declared boundary. The authors also give a genuine argument for the phantom — a positioning error is operator-induced, so removing patient variability isolates the construct — which Section 4 credits while noting the unargued half: patients are *why* positioning is hard.

**(2) "What is the reference standard for a positioning error, and who defined it?"** — **One senior DMFR lecturer (>8 years) classified, two further lecturers assessed, and all images were analysed "until investigators reached a consensus."** And the labels are **operationally defined in writing** — named anatomical landmarks for type, a radiopaque-wedge definition for cone-cut, a **count of interproximal areas** for severity, a contact-point rule with two named exceptions for overlap, and a **colour-banded template** for receptor placement. **So yes: this is the first entry in this run with a genuinely crisp reference standard, which was the point of the pick.** **But no agreement statistic is reported, and consensus-to-agreement made one unobtainable** — technique 317.

**And the pick paid off: entry 79's ceiling argument predicts correctly on crisp labels.** **Five of the six tasks are two-class, and they span 73.2% to 99.0% — 25.8 points with class count held constant** — ordered almost exactly by how much judgement each written rule requires: image geometry (99.0) > visual presence/absence (96.3) > single anatomical landmark (95.8) > boundary rule with exceptions (93.4) > template fit on a continuous quantity (73.2). **The paper's own class-count explanation is refuted by its own table**, since the worst task is binary. And **the three-class task fails specifically in the ordinal middle** — per-class AUC 94.9 critical, 94.5 minimal, **72.2 severe** — where the boundary is a count at three versus four.

**Arithmetic verified today, every check passing.** **All six task tables reconcile exactly**: 208+195=403, 173+230=403, 179+224=403, 70+61+48=179, 171+162=333, 155+177=332. **The exclusion chain is fully traceable**: 403 − 70 critical = 333, and 333 − 1 = 332, both as stated; and the three-class total of 179 matches the binary "present" count of 179. Fold standard deviations converted to approximate 95% intervals using t(4) = 2.776: side 98.3–99.7, cone-cut binary 94.1–98.5, type 92.1–99.5, overlap 86.9–100, three-class 72.2–86.4, **receptor placement 62.9–83.5**. SD range 0.6 to 8.3 — a **fourteen-fold spread that tracks the same ordering as accuracy**, an independent signature of the same label-precision effect. **No arithmetic error was found anywhere in this paper.**

**What could not be verified.** Any inter-rater agreement statistic (and none is obtainable from this design); any held-out test set — the reported figures **are** the cross-validation scores used to select architecture and learning rate per task from five candidates; **the complete ethics approval number**, which appears as "2024/" with nothing after in both the Methods and the Ethics Statement, so none is reportable; the per-mannequin image counts; any mannequin-level grouped cross-validation; the four non-winning architectures' results; any reporting guideline (CLAIM applies); all figures including the confusion matrix and template images; and Supporting Files 1 and 2. **Nothing was reproduced that was not seen.**

**Positive practice worth carrying forward.** **The five-fold scope declaration** (technique 320). **Operationally defined labels in writing** for every task. **Standard deviations on every metric, per class and overall** — the only reason the weak tasks' instability is visible. **Per-class metrics and a confusion matrix.** **Full acquisition and training reporting** — device, focal spot, 70 kV / 7 mA / 0.10 s, receptor type, native and downsampled resolution, GPU, optimizer, loss, epochs, initialisation, and explicit statements of no augmentation, no LR scheduling and no extra regularisation. **"Random seeds were not fixed," disclosed.** **The asymmetric cost of false negatives versus false positives, named.** **A competitor's better result reported** (100% on side with transfer learning on 1,000 images). **Funding explicitly none; conflicts explicitly none.** And the framing contribution — **"The study separates image acquisition quality from diagnostic content"** — which is a real idea the caries-detection literature needs, given that one cited study had interproximal overlap misclassified as caries.

**Landmark check, 2026-11-11 → 11-18.** One new record appeared, the first in over a week: **PMID 43045766, *Nature* 659(8141):852, "Should we move from artificial intelligence to artificial life?" (Petrovic O)** — **article type "News", single author, one page, no abstract.** An opinion piece, not a primary study. **Assessed and does not displace the queue.** Also re-confirmed: the *Nature Medicine* gait commentary (43003904), previously assessed.

**Deferred status, 2026-11-18, both re-checked today.** ***Annals* *Choosing Wisely* (42896192) — day 29, STILL NO PMC COPY**, and its **abstract-only date is tomorrow, 2026-11-19** — so it is **tomorrow's pick**, under the standing twenty-one-day rule. Standing note carried forward: its 5.4% / 0.6–12.2% CI is a clustering signature computed across 15 recommendations rather than 4,050 responses. **Gait foundation model (42995231) — day 10, still no PMC copy**, abstract-only date **2026-11-30**; it carries the largest multiplicity problem this list will have faced (**1,887 of 3,210 tested phenotypes called significant**), and the first question for it is what false-discovery-rate procedure ran across those 3,210 tests.

**SHELF RESTOCK — 2026-11-18.** The shelf emptied with today's pick, so a restock screen was run using the proven method (`pubmed pmc[sb]` with a two-week entry-date window): **347 records retrieved, the newest 10 screened in detail, 5 kept and 5 rejected.** Rejected: a bibliometric analysis of AI in myocardial infarction (43024324, not a performance study), a microRNA scoping review (43021123, molecular rather than clinical-AI appraisal), a cryo-electron-tomography quality classifier (43017487, structural biology), a wildfire review (43017078, not medical) and a computer-aided drug discovery review (43016799, not clinical prediction). **New shelf, all PMC-confirmed:**

**(G) SOFA score recalibration by ML-guided optimisation** — PMID 43024933, PMC13766654, *JMIR Med Inform* 2026. **Top pick.** eICU Collaborative Research Database, 208 US hospitals, 14,848 adult first ICU admissions. **Three reasons it goes first.** It **learns integer weights and thresholds for a legacy point-based score rather than replacing it with a black box** — the simple-score-versus-ensemble theme that entry 80's four-factor count raised, tested deliberately. It uses **10-fold nested cross-validation grouped by hospital** — grouped CV done properly, which is exactly the check entry 81 did not run (technique 319). And it reports that **133,684 of 148,532 encounters (90%) were excluded for at least one missing measurement**, which is the largest exclusion fraction this list will have examined. **First questions: what does a 90% complete-case exclusion do to who is left, and does the recalibrated integer score actually beat the original SOFA by more than the selection noise?**

**(H) AKI prediction in critical pulmonary embolism** — PMID 43024281, PMC13773385, *Medicine (Baltimore)* 2026. MIMIC-IV for development and internal validation, **eICU for external validation** — a genuine cross-database transportability test (technique 284) — with 8 ML models, LASSO plus multivariate logistic selection, and **a web calculator already deployed.** First question: how much performance was lost between MIMIC-IV and eICU, and was a calculator deployed before or after that was known?

**(I) Complete renal response in lupus nephritis** — PMID 43015004, PMC13757897, *Ren Fail* 2026. **A prospective cohort of 400** followed 12 months, four ML models, with **AUC, calibration AND decision-curve analysis plus SHAP** — a fuller reporting set than most entries in this run, and prospective rather than retrospective. First question: does the 3-month milestone add anything over baseline variables alone?

**(J) Facial phenotyping in sickle cell disease** — PMID 43019377, PMC13759072, *PLOS Digit Health* 2026. 308 smartphone photographs, 154 electrophoresis-confirmed cases and 154 age- and sex-matched controls aged 5 months to 19 years, recruited in **Kinshasa, DRC**; interpretable linear SVM with recursive feature elimination under **leave-one-out cross-validation**. A global-health, low-cost-hardware study — and **RFE inside LOOCV on 308 images is a classic optimism trap** worth examining carefully.

**(K) Next-day alcohol craving forecasting** — PMID 43013873, PMC13754260, *J Med Internet Res* 2026. Prospective longitudinal, multimodal (EEG, heart-rate variability and smartphone digital phenotypes), "tiny recurrent neural network." Forecasting a next-day subjective state from multimodal sensing — the self-reported-outcome reference-standard question in a new form.

**Plan set on 2026-11-18.** **Tomorrow, 2026-11-19, takes the *Annals* *Choosing Wisely* benchmark (42896192) as an abstract-only decode**, as owed under the twenty-one-day rule — its threshold date is tomorrow and it still has no PMC body after 29 days. **After that, shelf item (G)**, the SOFA recalibration study, for the three reasons above. **Shelf after today: five spares — (G) next after the Annals decode, then (H), (I), (J), (K).**

**Standing watch item:** PM Heart trial results (protocol PMID 42893738), quarterly.
