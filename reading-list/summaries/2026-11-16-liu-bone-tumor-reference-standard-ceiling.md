# Multimodal imaging and artificial intelligence for bone tumor diagnosis: Comparative performance and emerging technologies

**Authors:** Liu X (Department of Radiology, Endocrine and Metabolic Diseases Hospital of Shandong First Medical University, Jinan), Liu L (Department of Radiology, Shandong Cancer Hospital and Institute, Shandong First Medical University and Shandong Academy of Medical Sciences, Jinan)
**Journal:** Journal of Bone Oncology, 2026; 61: 100808 (published 23 October 2026)
**Article type:** Review (structured narrative review, self-declared as not a formal systematic review)
**Decoded:** 2026-11-16

**Analysis basis:** **FULL TEXT** (retrieved from PubMed Central, PMC13742044; 74,977 characters, ~9,710 words) — Introduction, the complete review methodology including search strategy, eligibility, quality-appraisal framework and the authors' own methodological limitations, the biological and pathological landscape, the modality-by-modality sections, the AI and radiomics sections, clinical translation and regulatory status, the controversies section including the central ground-truth argument, the conclusion, and all declarations. **All tables and figures are unreachable**, which costs two things named throughout: **the table that tabulates the ground-truth instability figures**, and — more significantly — **the comparative performance data promised by the title.** The prose contains **no AUC values at all**; I checked, and the only occurrence of "AUC" in the retrieved text is in the abbreviation list. So the "comparative performance" half of this review lives entirely in tables I could not read, and **nothing in this summary should be taken as a report of how well any model performs.**

**Source links (verified):**
- DOI: https://doi.org/10.1016/j.jbo.2026.100808
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42997475/
- Full text used: https://pmc.ncbi.nlm.nih.gov/articles/PMC13742044/

**Basis of link verification.** Direct URL fetching is blocked from this session (`doi.org` does not resolve under the network policy here), so verification was done against the live PubMed/NLM record. According to PubMed, a query for PMID 42997475 returned this exact title, these two authors with these affiliations, *Journal of Bone Oncology* volume 61 article 100808, publication date 23 October 2026, DOI `10.1016/j.jbo.2026.100808`, article types "Journal Article / Review", and keywords including "Ground truth" and "Reproducibility"; a PMID-to-PMCID conversion returned **PMC13742044**; and the full text was then retrieved from PubMed Central by that PMC ID and matches the record. Both halves of the chain were confirmed independently.

**Declarations: complete, and this is the cleanest set in the reading list.** **Funding: "The authors received no financial support for the research, authorship, or publication of this article."** **Competing interests: none declared, explicitly.** Ethics, consent and data availability each marked not applicable with a stated reason (review article, no human participants or identifiable data). And a **generative-AI disclosure of exemplary specificity**: ChatGPT was used "to improve the language, grammar, readability, and clarity of author-drafted text," and "was **not** used for literature identification, reference selection, citation placement, figure generation, or the generation of substantive content," with "All citations have been verified against the primary articles."

**Reporting guidelines: named, and this breaks a streak.** The quality-appraisal framework explicitly uses **CLAIM, TRIPOD+AI, CLEAR, the Image Biomarker Standardization Initiative, METRICS and the Radiomics Quality Score.** **This is the first entry in nine to name a reporting guideline at all**, and Section 4 records what that does to this list's standing observation.

---

## 1. The Gist

**Two radiologists in Shandong wrote the paper this reading list has been circling for three weeks. Their argument is that the thing holding back AI in bone tumours is not the algorithm — it is that nobody can reliably say what the right answer is. And unlike most papers that gesture at this, they put numbers on it.**

Bone tumours are rare, they look alike on scans, and getting the diagnosis wrong has large consequences: a benign lesion mistaken for cancer leads to unnecessary surgery, and a sarcoma mistaken for something harmless costs a limb or a life. So the field has poured effort into AI — radiomics, deep learning, transformers — to classify, grade and predict. The reviewers' claim, stated openly in the abstract as "a specific argument rather than surveying available technologies," is that **this effort is pushing against a wall it cannot move.**

Here is the wall. **To train or test a model you need labels — the "ground truth" — and in bone tumours the ground truth is unstable on four counts**, three of which the authors quantify from published data.

**First, the biopsy may miss the answer.** A core needle biopsy takes a thin sample of a tumour that is not uniform, and the most aggressive part can be small. For *ruling out* cancer it works well: **98% of negative bone biopsies were still benign two years later.** For *grading*, it does not. **Sampling errors occurred in 14.7% of biopsied chondrosarcomas** in one series. And the agreement between the grade from the biopsy and the grade from the whole tumour after surgery was **83% in long bones but only 36% in the pelvis** — weighted kappa falling from **0.63 to 0.12.**

**And here is the number that should reframe this entire field.** In the external test group of one CT radiomics study, distinguishing a borderline cartilage tumour from a higher-grade chondrosarcoma, the **biopsy got it right 64% of the time. The experienced radiologist got 81%. The computer got 75%.** **The reference standard was the least accurate of the three.** The model beat the thing it would normally be graded against by eleven points — and if the study had only had biopsy labels, as most do, that model could not have scored above about 64%, and nobody would have known it had beaten the label.

**Second, the experts disagree.** Nine musculoskeletal pathologists graded 46 cartilaginous lesions and agreed with a kappa of **0.443**; eight musculoskeletal radiologists managed **0.345**. Kappa is agreement after subtracting what you would get by guessing, and those values are conventionally called "moderate" and "fair." **And in the lesions that later turned out to be high-risk — the ones where getting it right actually matters — agreement collapsed to 0.236 and 0.206.** In another study, **eight expert pathologists reviewing twelve selected osteosarcomas agreed unanimously on only seven, and in six of the twelve the assigned grade ranged all the way from low to high.**

To the authors' credit, they also include the case that cuts against them: twelve bone pathologists diagnosing a different kind of cartilage tumour reached an intraclass correlation of **0.78**, which is good. Their conclusion is appropriately narrow: **"Instability is therefore concentrated in grading, and in the cases with the greatest clinical consequence."**

**Third, the categories themselves keep changing.** Molecular testing has redefined what counts as what. Datasets assembled before CIC- and BCOR-rearranged sarcomas were split off from Ewing sarcoma still contain those tumours under the old label. **A model trained on that data "has learned a class that no longer exists as defined."**

**Fourth, and least fixable: the label may be the wrong target.** Lesions called benign sometimes progress; lesions that look malignant sometimes sit still for years. The histological grade is not the thing patients care about.

**From this the authors draw three consequences, and each one is sharper than it first sounds.**

**Measured accuracy has a ceiling the algorithm does not control.** If the label is only so good, your score against it can only be so good. I worked the arithmetic through independently and it lands somewhere striking: **from the radiologists' own kappa of 0.345, each radiologist is roughly 79% accurate against the underlying truth — and the review separately reports, as an empirical observation, that a radiograph classifier hit 80% external accuracy and was "statistically indistinguishable" from musculoskeletal radiologists.** The predicted ceiling and the observed plateau are a point apart. Section 5 does that calculation in full, with its assumptions on the table.

**Scoring above the ceiling is bad news, not good.** "Performance above it indicates the model has learned an institution's labelling conventions rather than the underlying biology."

**And the one that inverts a standard inference: "Apparent external validation failure may reflect label divergence rather than model deficiency."** When a model trained at hospital A does badly at hospital B, everyone concludes the model was overfitted. **It might instead be that the two hospitals grade tumours differently** — in which case "no single model can perform well" on both, and the model may be fine. This matters especially after yesterday's entry in this list, where external degradation was real and clearly came from the scanner rather than the labels: **the same observation has at least three different causes, and telling them apart requires work that is almost never done.**

**What the authors do with all this is the best part.** They end by separating problems that effort can solve from problems it cannot: **"methodological rigor and data infrastructure are addressable through coordinated effort, whereas ground-truth instability is a property of the disease and its evolving classification."** And they state the field's position without softening it: **no system for primary bone tumour characterisation, grading or response prediction has regulatory clearance in either the United States or Europe. "Every application [reviewed] is investigational."**

**Where they fall short is precision rather than argument.** The headline kappas come from studies of **12 to 46 cases**, and **not one agreement statistic in the review carries a confidence interval.** Section 4 works out what that costs.

## 2. Study Snapshot

**Study type:** a **structured narrative review**, explicitly self-declared as "not a formal systematic review," advancing a specific thesis rather than surveying a field. **No primary data, no meta-analysis, no pooling.** Two authors, both radiologists.

**Search.** PubMed/MEDLINE, Embase and the Web of Science Core Collection, covering **1 January 2020 to 31 March 2026**, final search executed 31 March 2026. Controlled vocabulary plus free text, limited to English-language human studies. **16,247 records identified — PubMed/MEDLINE 4,842, Embase 6,115, Web of Science 5,290** (I verified these sum exactly). **6,812 duplicates removed, leaving 9,435 unique records for title and abstract screening** (also verified). The date limit was relaxed twice by design: for seminal earlier imaging studies, and for methodological sources cited at their point of origin. Reference lists of key articles were hand-screened.

**A gap worth naming: the cascade stops there.** **No full-text screening count and no final number of included studies appears anywhere in the retrieved text.** For a review that reports its database-level yields to four significant figures, the absence of a final count is conspicuous.

**Eligibility.** Primary or metastatic bone tumours; imaging modalities or AI methods; diagnostic, staging, prognostic or response outcomes; peer-reviewed English. Prospective and retrospective both allowed. **Excluded:** case reports under five patients, conference abstracts without full text, non-human studies, and articles lacking methodological detail or quantitative outcomes. Narrative reviews were used for background only, "not included in evidence synthesis tables unless they offered meta-analytic data or systematically appraised primary evidence." Guidelines and classification systems — the 2020 WHO classification, the Society of Skeletal Radiology Bone-RADS white paper, the ESSR consensus, the ACR Appropriateness Criteria, and UK and European sarcoma recommendations — were "retained as normative rather than empirical sources."

**Quality appraisal.** No meta-analysis, "given the heterogeneity of study designs, reference standards, and outcome definitions." Instead, adapted principles from **CLAIM, TRIPOD+AI, CLEAR**, plus for radiomics the **Image Biomarker Standardization Initiative**, **METRICS** and the **Radiomics Quality Score**. Appraisal domains: dataset size and representativeness, inclusion clarity, **reference standard definition (histopathology versus clinical or imaging follow-up)**, validation strategy, and reporting transparency. Named bias sources included **data leakage, class imbalance, absent external validation, hidden stratification, under-representation of infrequent lesions, imperfect or non-uniform reference standards, and demographic fairness.** Harmonisation strategies such as ComBat were "treated as prerequisites for generalizability rather than as optional refinements."

**And a crucial methodological statement about the review's own central numbers:** to quantify reference-standard instability, "agreement statistics (Cohen's or weighted kappa, intraclass correlation coefficients, and biopsy–resection concordance) were extracted as reported by the primary studies, **without recalculation or pooling.**"

**The quantified instability, which is the review's core contribution.** From the authors' own framing, the stable-ground-truth assumption fails on four grounds, "three of which can be quantified from published data."

*Biopsy sampling.* **98%** of negative bone biopsies confirmed benign at two years. **Sampling errors in 14.7%** of biopsied chondrosarcomas in one series. Biopsy grade agreed with resection grade in **83% of long-bone** but only **36% of pelvic** central chondrosarcomas, **weighted kappa 0.63 versus 0.12.** And in one CT radiomics study's external test cohort, distinguishing atypical cartilaginous tumour from higher-grade chondrosarcoma: **biopsy correct in 64% of cases, an experienced radiologist 81%, the classifier 75%.** The authors' summary: "A biopsy-derived label carries no indication of whether the sampled region was representative."

*Expert agreement.* **Nine musculoskeletal pathologists grading 46 cartilaginous lesions of long bones: kappa 0.443. Eight musculoskeletal radiologists: 0.345.** "In lesions subsequently judged high-risk on clinical course, agreement fell to **0.236 and 0.206.**" **Eight expert pathologists reviewing 12 selected osteosarcomas: unanimous diagnosis in only 7 cases, with assigned grade ranging from low to high in 6.** Counter-evidence the review includes rather than omits: **twelve bone pathologists diagnosing peripheral cartilaginous tumours in multiple osteochondromas reached an intraclass correlation of 0.78.**

*Molecular reclassification.* "Datasets predating the separation of CIC- and BCOR-rearranged sarcomas from Ewing sarcoma contain those tumors under the former label. A model trained on such data has learned a class that no longer exists as defined."

*The unquantified fourth ground.* "Lesions classified as benign may progress or recur; lesions with malignant features may remain indolent."

**The three consequences, verbatim in substance.** (1) "Measurable accuracy has a ceiling set by the reference standard, not the algorithm… a model cannot be shown to exceed that agreement" against a single-reader label, and "performance above it indicates the model has learned an institution's labelling conventions rather than the underlying biology." The authors offer an empirical anchor: "the external accuracy of a radiograph classifier (**80%**) was statistically indistinguishable from that of musculoskeletal radiologists." (2) "Apparent external validation failure may reflect label divergence rather than model deficiency. Two institutions applying different diagnostic thresholds produce datasets on which no single model can perform well." (3) "Static histological labels may be the wrong target. Models should incorporate clinically relevant endpoints, recurrence, progression, treatment response."

**Three further critiques the review makes of the AI literature, each of which this list has arrived at independently.** On human comparators: "Where models are compared against radiologists, the comparison is usually against readers **without access to clinical history or prior imaging**, a condition under which human performance is artificially depressed relative to practice." On case mix: "A model reporting high accuracy on a tertiary sarcoma centre cohort has been evaluated on a case mix in which **malignancy prevalence far exceeds that of the triage population.**" On leakage, with a mechanism specific to this field: "because patients undergo serial imaging across a treatment course, a dataset partitioned at image rather than patient level places images of the same lesion on both sides of the split. This inflates apparent performance and **is not detectable from reported metrics.**"

**On where the effort has gone, and why that is unfortunate.** "Radiomic and deep learning approaches have been applied to chondrosarcoma grading with reported accuracy comparable to expert readers… These are the most-studied applications, and the reason is instructive: **cartilaginous lesion grading is the task on which human interobserver agreement is poorest**, making it both the greatest clinical need and the setting in which the reference standard is least stable."

**Negative findings, reported as negative.** "Radiogenomic inference of molecular characteristics from imaging is frequently proposed but, in bone tumors, untested: **no study identified in this review predicts MDM2 amplification or IDH mutation status from imaging.** The molecular associations are established; the imaging inference is not." And on pretraining: domain-specific pretraining "is thought to outperform natural-image pretraining for rare subtypes, but **direct comparison in bone tumors has not been reported.**"

**On explanations and uncertainty.** Saliency methods "provide post hoc explanation and may not represent internal decision processes; **identical predictions can arise from models with substantially different attention patterns.**" On uncertainty: Monte Carlo dropout and Bayesian approaches distinguish **epistemic** uncertainty, which "rises where a case falls outside the training distribution," from **aleatoric** uncertainty "inherent to the data." And: "**Rarity guarantees that any deployed bone tumors model will encounter subtypes absent from training**, making this the setting where such quantification matters most, and where it is least often reported."

**Regulatory status, stated without hedging.** US regulation via 510(k), De Novo or premarket approval; in Europe the Medical Device Regulation and the AI Act "classify most medical AI as high-risk." Then: "Regulatory clearances in musculoskeletal radiology have concentrated on fracture detection and bone age assessment. **No system for primary bone tumor characterization, grading, or response prediction has been cleared in either jurisdiction. Every application [reviewed] is investigational.**" And on the implementation pathway: "**For bone tumors the sequence has not been completed by any system: the field remains at the first two stages.**"

**Two formal appraisals cited as establishing the deficits "quantitatively rather than impressionistically":** a METRICS and Radiomics Quality Score assessment of chondrosarcoma radiomics, and a CLAIM-based review of osteosarcoma radiomics. "Common deficiencies include **absent external validation, no calibration analysis, and limited data or code availability.**"

**The authors' own methodological limitations, stated in a dedicated section.** No formal protocol, no duplicate screening, no quantitative pooling, so "selection and interpretation are subject to reviewer judgment." English-language restriction introduces language and publication bias, "which is of particular concern in a field where **negative or externally non-replicating AI results are under-reported.**" Rarity constrains the evidence base, so most included studies are "retrospective, single-center, and modest in sample size," and the proposed mitigations — federated learning, self-supervised pretraining, synthetic control arms — "remain largely investigational." And the evidence is "the state of the literature at the time of the search," with conclusions on emerging applications "regarded as provisional."

**Not reported or not retrievable:** **any confidence interval on any kappa, intraclass correlation or concordance figure**; the number of studies finally included and any full-text screening count; **all tables and figures**, including the ground-truth instability table, the evidence-synthesis tables, the molecular-reclassification table and the implementation-pathway figure; and **every AUC or comparative performance value**, which exist only in those tables.

## 3. How Strong Is This Evidence? (Grade 4 out of 5)

**This is the best-argued paper in this reading list, and the highest grade a review of this kind can carry. It earns the 4 by doing something papers in this genre almost never do: it states a falsifiable thesis, puts numbers on it, includes the evidence against it, and says plainly what it cannot settle.**

**What earns the grade.**

**A specific, falsifiable claim, declared as such.** The abstract says the review "advances a specific argument rather than surveying available technologies." That sentence changes how the paper should be read and judged, and the authors wrote it deliberately. **Most reviews are surveys dressed as arguments; this is an argument that happens to contain a survey.**

**The thesis is quantified rather than asserted** — which was the question this entry was picked to answer. Four grounds are claimed, the authors specify that **three can be quantified from published data**, and they produce figures for each: biopsy–resection concordance, sampling-error rate, interobserver kappa among pathologists and among radiologists, a high-risk subgroup breakdown, a unanimity count, and an intraclass correlation. **The fourth ground is explicitly left unquantified rather than padded with a number.**

**They state how the numbers were obtained, including the limitation.** Agreement statistics were "extracted as reported by the primary studies, **without recalculation or pooling.**" That is the right disclosure. It means the figures are single-study values, not meta-analytic estimates, and a reader knows it.

**They include the counter-evidence.** The intraclass correlation of **0.78** among twelve bone pathologists cuts against the thesis, and it is in the text with the honest gloss: "Agreement is not uniformly poor… Instability is therefore concentrated in grading, and in the cases with the greatest clinical consequence." **A reviewer pushing a line would have left that out.**

**They report negative findings as negative.** No study predicts MDM2 amplification or IDH mutation status from imaging. No direct comparison of domain-specific versus natural-image pretraining exists in bone tumours. **Both are stated as absences rather than converted into "promising avenues."**

**They name reporting guidelines and use them** — CLAIM, TRIPOD+AI, CLEAR, IBSI, METRICS, RQS — and cite two formal appraisals that establish the field's deficits "quantitatively rather than impressionistically." After eight consecutive entries in this list naming nothing, this one names six instruments and applies them.

**They identify a field-specific leakage mechanism and note that it is invisible.** Serial imaging across a treatment course means an image-level split puts the same lesion on both sides, and this "is not detectable from reported metrics." **That is a concrete, checkable warning rather than a generic caution about leakage.**

**They state the regulatory position flatly.** No clearance for bone tumour characterisation, grading or response prediction in the US or Europe; every application reviewed is investigational; the field "remains at the first two stages" of the implementation pathway. **No paper that wanted to flatter the field would put it that way.**

**They criticise their own method in a dedicated section**, naming the absence of a protocol, of duplicate screening and of pooling, and flagging publication bias specifically in non-replicating AI results.

**And the declarations are the cleanest in this list**: no funding, no competing interests, both explicit, and a generative-AI disclosure that states exactly what the tool was and was not used for and asserts that all citations were checked against primary articles.

**And the closing distinction is genuinely useful rather than rhetorical.** "Methodological rigor and data infrastructure are addressable through coordinated effort, whereas ground-truth instability is a property of the disease and its evolving classification." **That sentence tells a research funder where to put money and where not to.**

**What holds it to 4.**

**Not one agreement statistic carries a confidence interval**, and the headline figures rest on very small studies: **46 lesions for the pathologist kappa, 12 osteosarcomas for the unanimity count.** Section 5 works the arithmetic: a two-rater approximation on 46 cases puts a 95% interval around 0.443 at roughly **0.23 to 0.65** — spanning "fair" to "substantial." The nine-rater design narrows that, and by how much is not recoverable from what is reported, because nothing is reported. **The direction of the argument survives — the lower bound is worse, not better — but "kappa 0.44" is really "somewhere in a band," and a review whose thesis is built on these numbers owed its readers the bands.**

**The search cascade has no terminus.** 16,247 records, 6,812 duplicates, 9,435 screened — and then no full-text count and no final number of included studies. For a narrative review this is not fatal, and the authors never claim PRISMA compliance. **It still means a reader cannot tell how much literature the conclusions rest on.**

**The ceiling claim is stated a shade too strongly in one formulation.** "A model cannot be shown to exceed that agreement" is defensible because of the word "shown." But strictly, **a model's agreement with one reader is not mathematically bounded by agreement between readers** — a model that learns one reader's idiosyncrasies can exceed it. The review's very next sentence handles this correctly ("Performance above it indicates the model has learned an institution's labelling conventions"), so the argument is internally sound. **A reader quoting only the first clause would be overstating it.**

**Two radiology authors and no pathologist co-author**, for a thesis whose load-bearing evidence is about pathological reference standards. The sourcing is good and this is a milder version of the problem than yesterday's entry had. **It is still worth noting that the argument about pathology was assembled without a pathologist.**

**And a review cannot establish what the primary literature has not done.** The thesis is persuasive and it is a synthesis of other people's measurements. **The study that would test it directly — give the same cases to multiple institutions' pathologists, train a model against each institution's labels, and measure how much of the cross-site performance drop is label divergence — does not exist, and the review is clear that it does not.**

**Why not 5.** Because in this list a 5 requires evidence that settles something, and no review does. This one argues, quantifies and synthesises; it does not measure. **Its central claim about external-validation failure remains an untested hypothesis, correctly labelled as such.**

**Why not 3.** Because everything that usually drags a review down is absent here. **It is not a survey, it does not inflate its field, it reports its own limits, it includes contradicting evidence, it names guidelines, and its declarations are complete.** The defects are of precision, not of honesty.

## 4. The Editor's Concerns

**1. The biopsy scored 64%, the model 75%, the radiologist 81% — and this single comparison is more important than the review makes it.** It appears once, in a subordinate clause in section 8.3. **It is the strongest empirical support for the entire thesis**, because it is the one case where a better reference standard (resection) was available to reveal that the usual reference standard (biopsy) was the worst performer in the room. **The model beat its own label by eleven points.** Validated against biopsy alone — which is how most such studies are built — that 75% model could not have scored above roughly 64%, and its superiority to the label would have been undetectable. **This deserved to be the review's centrepiece and a figure of its own.**

**2. No confidence interval on any agreement statistic, in a paper whose thesis is those statistics.** The kappa of 0.443 comes from 46 lesions; the unanimity finding from 12 osteosarcomas. Running a two-rater approximation on 46 cases gives a 95% interval of roughly **0.23 to 0.65** around 0.443 — which crosses from "fair" into "substantial." The nine-rater design makes the true interval narrower than that, **but the reader cannot know by how much, because the review reports extracted point estimates and nothing else.** The authors did say they extracted "without recalculation," which is honest and explains the omission; **primary studies of this kind do normally report intervals, and passing them through would have cost a line of text and strengthened the paper considerably.** The argument's direction is unaffected — if anything the lower bounds make it worse — but the precision implied by "kappa 0.44" is not supported.

**3. The search cascade stops before the end.** 16,247 identified, 6,812 duplicates removed, 9,435 screened — and then silence. **No full-text screening count, no final included-study count, no flow diagram number.** The authors explicitly disclaim systematic-review status and never promise PRISMA, so this is not a violation of anything. It does mean that when the review says deficiencies are "common" or external validation "infrequent," **a reader has no denominator** and must take those frequencies on trust or follow the two cited formal appraisals.

**4. The comparative performance promised by the title is not in the prose.** The title is "Comparative performance and emerging technologies." I searched the entire retrieved text: **there is not one AUC value in it.** The only occurrence of "AUC" is in the abbreviation list. Every performance figure lives in tables I could not retrieve. **So this review, as I can read it, is almost entirely an argument about reference standards with the comparative-performance content inaccessible** — and that is a limitation of my retrieval, not of the paper. I state it because a reader of this summary should not imagine I have verified any model's performance.

**5. The ceiling argument's strongest form is not quite true, and the review's weaker form is.** "A model cannot be shown to exceed that agreement" against a single-reader label is correct. **"A model cannot exceed inter-reader agreement" would be false** — a model that learns one annotator's particular habits, including their errors, can agree with that annotator far better than a second expert would. The review knows this and says so immediately afterwards, turning it into the more interesting claim: **exceeding the ceiling is evidence of annotator-overfitting, not of skill.** That is right, and it is a trap for anyone quoting the first clause alone.

**6. The inversion in consequence two is the review's most useful and least tested idea.** "Apparent external validation failure may reflect label divergence rather than model deficiency." **This flips the standard inference**, and it matters: the field treats external-validation failure as proof of overfitting. But note what it does to diagnosis. **Yesterday's entry in this list found a model degrading on a different manufacturer's scanner, with a one-directional bias of +1.83 dB and attention falling outside the target anatomy specifically on that device** — that degradation was clearly about measurement, not labels. **So external failure now has at least three candidate causes — genuine overfitting, measurement or instrument shift, and label divergence — and nothing in a performance table distinguishes them.** The review proposes the hypothesis and does not propose a test. **The test is straightforward and absent from the literature: have institution A's pathologists re-grade institution B's cases, and see how much of the performance drop disappears.**

**7. Agreement is worst exactly where the stakes are highest, and this deserves more than one sentence.** Pathologist kappa fell from **0.443 to 0.236** and radiologist kappa from **0.345 to 0.206** in lesions subsequently judged high-risk on clinical course. Undoing the chance correction, two expert pathologists looking at a consequential lesion agree on its grade **roughly half the time.** **The review states this and moves on.** It is the most alarming finding in the paper, it is the subgroup in which any deployed model would be used, and it means the ceiling in the cases that matter is far below the ceiling reported on average. **Any paper reporting agreement should report it stratified by consequence, and almost none do.**

**8. The field has concentrated its effort on the task with the lowest ceiling, and the review notices without drawing the conclusion.** "These are the most-studied applications, and the reason is instructive: cartilaginous lesion grading is the task on which human interobserver agreement is poorest, making it both the greatest clinical need and the setting in which the reference standard is least stable." **So the most-researched application in the field is the one where measurable progress is most tightly capped.** That is an argument for redirecting effort — toward the outcome-based endpoints the review recommends, or toward tasks with stabler labels — and the review leaves it implicit.

**9. The human comparison is handicapped by design, and this cuts both ways.** "Where models are compared against radiologists, the comparison is usually against readers without access to clinical history or prior imaging, a condition under which human performance is artificially depressed relative to practice." **This is an excellent catch** and it is the mirror image of the ceiling argument: the model's score is capped by label noise, while the human's score is depressed by an artificial reading condition. **Both distortions push in the direction of making the model look relatively better**, and a reader needs both to interpret any human-versus-AI comparison in this field.

**10. The case-mix problem is a genuine double bind, stated as such.** "Any dataset assembled from consecutive presentations is dominated by benign lesions; any dataset enriched for malignancy is unrepresentative of the triage population." **There is no dataset that is both adequately powered for the rare malignant classes and representative of the population the tool would screen.** This connects directly to a lesson from two entries ago: predictive value depends on prevalence, so a model validated at a tertiary sarcoma centre will perform very differently in general practice even with identical sensitivity and specificity. **The review names the bind and correctly offers no solution, because there is not a clean one.**

**11. Two radiologists, no pathologist, on a thesis about pathology.** The evidence is well sourced and the argument is sound, so this is a lighter version of the problem than yesterday's entry had. **But the review's central claim is that pathological ground truth is unstable, and the people best placed to confirm, qualify or correct that are pathologists.** A co-author from that discipline would have strengthened the paper and might have supplied the intervals.

**12. The guideline streak breaks, and in the most instructive possible way.** Nine entries: 69 named TRIPOD+AI and deposited the checklist; 70 named STROBE; 71, 73, 74, 75 named none; 76 *measured* the phenomenon at **40% mean completeness** against the instrument written for the job; 77 and 78 named none, each in a case where a checklist would have caught a real defect. **Entry 79 names six instruments — CLAIM, TRIPOD+AI, CLEAR, IBSI, METRICS, RQS — and is also the best-argued paper in the run.** One case does not overturn the standing rule, and the rule never said guidelines are useless: it said **naming one does not predict quality, so read the methods.** What entry 79 adds is the complementary observation that **a paper which uses guidelines as analytic instruments rather than as a compliance badge tends to be a paper that was going to be careful anyway.** The guidelines did not make this review good; the same disposition produced both.

## 5. Statistics Spotlight

Three concepts, numbered from 294 in the running list in `queue.md`. The first is the review's entire thesis expressed as arithmetic, and it is the most broadly useful idea in this reading list so far.

**A noisy reference standard sets a ceiling on measurable accuracy that no algorithm can lift.**

Start with the cleanest case in the paper, which needs no assumptions at all.

**Biopsy grade agreed with resection grade in 36% of pelvic central chondrosarcomas.** Take the resection — the whole tumour, examined completely — as the truth. Then **the biopsy label is right about 36% of the time** in the pelvis.

Now suppose you build a model that is *perfect*: it always predicts the true grade that the resection would show. You test it against biopsy labels, because that is the data you have. **How accurate does it look? 36%.** Not because the model is bad — it is flawless — but because **the answer key is wrong 64% of the time.**

In long bones, where biopsy and resection agree 83% of the time, the same perfect model would measure **83%.** **Same model, same skill, two different scores, decided entirely by the quality of the labels.**

**This is the whole thesis, and it generalises.** Your measured accuracy against a label cannot exceed the label's own accuracy. **The ceiling is a property of the data, and buying a bigger model does not raise it.**

**Now the subtler consequence: a model better than its labels will measure as worse than it is.** Suppose the label is about 78% accurate (I derive that figure below) and there are three grades. Measured agreement between model and label is roughly `p_model × p_label + (1 − p_model)(1 − p_label)/2`. Working it through:

- a model that is truly **78%** accurate measures as **63%**
- a model that is truly **90%** accurate measures as **71%**
- a model that is truly **95%** accurate measures as **74%**
- a **perfect** model measures as **78%**

**Going from a 90%-accurate model to a flawless one buys you under 7 measured points.** Every improvement is taxed by the label noise, and the returns shrink as you approach the ceiling. The review's own phrasing is exactly right: **"improvements in architecture will not translate into improvements in measurable accuracy beyond a ceiling the algorithm does not control."**

**And the review contains the real-world demonstration.** In one study's external test cohort: **biopsy 64% correct, the classifier 75%, the radiologist 81%.** **The reference standard was the worst of the three.** Had that study, like most, possessed only biopsy labels, the 75% model would have been scored against a 64% answer key — it could not have exceeded about 64%, **and the fact that it had beaten the label would have been invisible.** The only reason anyone can see it is that resection truth existed for comparison.

**The everyday version.** You sit a multiple-choice exam, and the marking sheet has errors in a third of its answers. A perfect student scores two-thirds. A student who knows the subject better than whoever wrote the marking sheet is penalised precisely for the questions where they are right and the sheet is wrong. **Buying the students better textbooks will not raise the class average past two-thirds, and the only fix is to correct the marking sheet.** Everything else is effort spent against a wall.

**Watch out for:** any accuracy, AUC or kappa reported against a label that is itself a judgement — a pathologist's grade, a radiologist's read, a chart-review adjudication, a billing code, another model's output. **Two questions. How accurate is the label itself, and how do you know? And has anyone estimated the ceiling before reporting progress against it?** If a field's performance figures have plateaued at a suspiciously specific number, **the plateau may be the label, not the science.** And the inverse red flag matters just as much: **a model reported as beating expert agreement has probably learned one institution's habits**, which is what the review means by "performance above it indicates the model has learned an institution's labelling conventions rather than the underlying biology."

**Kappa: what it is, how to undo it, and the paradox lurking in this paper's own numbers.**

Every central figure in this review is a **kappa**, so it is worth knowing exactly what one is.

**Raw agreement is misleading** because some agreement happens by luck. If two pathologists each call 90% of lesions "low grade," they will agree most of the time without either of them knowing anything. **Kappa subtracts the luck:**

**kappa = (observed agreement − chance agreement) ÷ (1 − chance agreement)**

So kappa is the share of the *available* agreement — the agreement beyond chance — that the raters actually achieved. **0 means no better than guessing; 1 means perfect.** The conventional bands: below 0.20 poor, 0.21–0.40 fair, 0.41–0.60 moderate, 0.61–0.80 substantial, above 0.80 almost perfect.

**So read this paper's figures properly.** Pathologists at **0.443** is "moderate." Radiologists at **0.345** is "fair." And in high-risk lesions, **0.236 and 0.206** — "fair" shading into "poor," for the cases where the decision changes what happens to the patient.

**You can run the formula backwards to recover raw agreement**, which is more intuitive. Rearranged: observed = kappa × (1 − chance) + chance. Assuming grades are roughly evenly distributed — **an assumption I am stating, not hiding** — chance agreement is 1/2 for two grades or 1/3 for three:

- pathologists, 0.443 → **about 72% agreement with two grades, 63% with three**
- radiologists, 0.345 → **about 67% with two, 56% with three**
- pathologists, high-risk lesions, 0.236 → **about 62% with two, 49% with three**

**So in the lesions that matter most, two expert musculoskeletal pathologists agree on the grade roughly half to three-fifths of the time.**

**Now the step that produces the striking result.** If two readers are each measuring one underlying truth and their mistakes are independent, then their agreement with each other tells you how accurate each of them is. With three grades, observed agreement ≈ `p² + (1 − p)²/2`, where p is each reader's accuracy. Solve for p:

- from the pathologists' 0.443: **each pathologist is about 78% accurate** (three grades) or 83% (two)
- from the radiologists' 0.345: **each radiologist is about 72% accurate** (three grades) or **79%** (two)

**And here is where it gets interesting.** The review separately reports, as a plain empirical observation, that **a radiograph classifier achieved 80% external accuracy and was "statistically indistinguishable" from musculoskeletal radiologists.** My arithmetic, from the radiologists' own kappa and nothing else, predicts a ceiling of about **79%.** **The predicted ceiling and the observed plateau are one point apart.**

**I want to be careful about how much that is worth.** Three assumptions are doing work: evenly distributed grades, independent errors, and errors spread evenly across the wrong options. **The independence assumption is the shakiest, and it fails in a known direction** — real experts share training and stumble on the same hard cases, so their errors are *correlated*, which inflates their observed agreement and therefore **overstates** p. The true ceiling is probably lower than 79%. And the kappa is for grading cartilage tumours while the 80% is a radiograph classifier — related tasks, not the same one. **So this is a suggestive convergence, not a proof.** It is still the kind of check worth running, because it took two lines of arithmetic and it says the plateau is where theory says it should be.

**The paradox worth knowing, visible in this paper's own two biopsy figures.** Long bones: **83% raw agreement, kappa 0.63.** Pelvis: **36% raw agreement, kappa 0.12.** The raw agreements differ by 47 points; the kappas differ by 0.51. Working backwards, the implied chance agreement is about **0.54** in long bones and **0.27** in the pelvis. **Why?** Because long-bone cartilage lesions are overwhelmingly low grade, so the grade distribution is lopsided and chance agreement is high — which means kappa punishes that setting harder than raw agreement does. Pelvic tumours spread more evenly across grades. **The lesson: the same kappa can come from very different raw agreements depending on how skewed the categories are, and the same raw agreement can give very different kappas.** (These are *weighted* kappas, so my back-calculation is approximate and the implied chance figures are indicative only.)

**The everyday version.** Two people guess whether it will rain tomorrow in a desert where it rains five days a year. Both say "no" every day. **They agree 98.6% of the time and neither knows anything about weather.** Kappa is near zero, correctly. Now move them to a climate where rain is a coin flip: agreeing 72% of the time there is genuine skill. **Raw agreement without the context of how lopsided the thing is cannot tell those two situations apart. That is what kappa is for — and why you should always ask for the raw agreement too.**

**Watch out for:** kappa quoted with no sample size and no interval — **which is this review's own weakness.** The headline 0.443 rests on 46 lesions; a two-rater approximation puts its 95% interval at roughly **0.23 to 0.65**, which straddles two of the conventional bands. The nine-rater design narrows it, but nothing reported lets you say how much. **Also watch for kappa quoted without the class distribution**, because of the paradox above, and for **agreement reported only in aggregate** when the subgroup that matters clinically may be far worse — here it dropped by nearly half.

**Report an interval on every agreement statistic, and stratify it by consequence.**

This is the shortest of the three and the most immediately actionable, and it is my main criticism of an otherwise excellent paper.

**Kappa is an estimate, like any other.** It has a standard error that depends on the number of cases, the number of raters, and how lopsided the categories are. For a two-rater study of 46 cases with agreement around 63%, the standard error of kappa works out at roughly **0.11**, giving a 95% interval of about **0.23 to 0.65** around a point estimate of 0.443. **That interval spans "fair" to "substantial."**

**The nine-rater design in the underlying study carries more information than two raters would, so the real interval is narrower.** How much narrower cannot be worked out from what the review prints, because **it prints no interval at all, for any of its agreement figures.**

**The authors have a defence and it is partly good.** They state they extracted statistics "as reported by the primary studies, without recalculation or pooling." If the primary studies reported bare kappas, passing bare kappas through is faithful. **But primary agreement studies normally do report intervals**, and a review whose central argument is built on six or seven agreement statistics owed its readers the bands around them — it would have cost one line.

**Which direction does it cut?** Mostly in the review's favour, which is why this is a criticism of precision rather than of the thesis. **The lower bound of the interval is worse than the point estimate**, so if 0.443 is bad news for the ceiling, 0.23 is worse. The argument survives; the apparent exactness does not.

**And the second half: stratify.** The single most important thing in this paper's agreement data is that **kappa fell from 0.443 to 0.236 among pathologists, and from 0.345 to 0.206 among radiologists, in the lesions that turned out to be high-risk.** An aggregate kappa averages the easy cases, where everyone agrees, together with the hard ones, where nobody does. **A model will be deployed on the hard ones.** So the aggregate figure systematically overstates the ceiling where it matters.

**The everyday version.** A weather service reports 85% accuracy for the year. Useful — until you learn that almost all of it comes from a long run of identical sunny days, and on the four days with a hurricane warning it was right once. **The annual average is true and it is not the number you want before deciding whether to evacuate.** Averages across mixed difficulty hide the performance you actually need.

**Watch out for:** any reliability figure — kappa, intraclass correlation, percent agreement — quoted as a bare number. **Three things to ask: how many cases, what interval, and what is it in the subgroup that matters?** And when a reliability figure is used to justify a ceiling, a threshold or a sample size, **the lower end of its interval is the one to plan against.**

## 6. Jargon Translator

**Ground truth / reference standard** — the answer the model is trained and scored against. **The whole subject of this paper: in bone tumours it is unstable, so scores against it are capped.**

**Core needle biopsy** — a thin sample of tumour taken through a needle, usually CT-guided. Good at **ruling out** cancer here (98% of negative biopsies stayed benign at two years) and much less good at **grading**, because the worst part of the tumour can be missed.

**Sampling error** — the needle took tissue that does not represent the whole tumour. Occurred in **14.7%** of biopsied chondrosarcomas in one series.

**Resection specimen** — the whole tumour after surgery, examined completely. **The better reference standard**, and the one that reveals biopsy labels to be wrong.

**Grade** — how aggressive a tumour looks under the microscope, usually low to high. **Distinct from stage**, which is how far it has spread. Grading is where agreement is poorest.

**Chondrosarcoma / atypical cartilaginous tumour (ACT)** — cancer arising from cartilage, and its borderline low-grade form. **Telling them apart is the most-studied AI task here, and the one with the least stable reference standard.**

**Osteosarcoma / Ewing sarcoma** — the two commonest primary bone cancers, typically in young people.

**CIC- and BCOR-rearranged sarcomas** — tumours split off from Ewing sarcoma by molecular testing in the past decade. **Older datasets still carry them under the old label**, so a model trained on that data learned a class that no longer exists as defined.

**Interobserver agreement** — how often two different experts, looking at the same case, say the same thing.

**Kappa (Cohen's, weighted, Fleiss')** — agreement **after subtracting what luck would give you**. 0 is chance, 1 is perfect; conventionally 0.41–0.60 is "moderate" and 0.21–0.40 "fair." **Weighted** kappa gives partial credit for being close (grade 1 versus 2 counts as a smaller error than 1 versus 3) — technique 295.

**Intraclass correlation coefficient (ICC)** — the equivalent for measurements on a scale rather than in categories. The 0.78 here is the review's own counter-example to its thesis.

**Accuracy ceiling** — the highest score you can be *measured* at, set by how accurate the answer key is — technique 294.

**Attenuation** — the general name for a true relationship being measured as weaker than it is because the measurement is noisy. **Why a model better than its labels scores worse than it is.**

**Label divergence** — two institutions applying different diagnostic thresholds, so the "same" label means different things. **The review's proposed alternative explanation for external-validation failure.**

**External validation** — testing a model on data from a different source than it was trained on. **Infrequent in this field, per the review and two formal appraisals.**

**Data leakage** — test information contaminating training, inflating scores. **The field-specific form here: patients have serial scans, so splitting by image rather than by patient puts the same lesion on both sides — and this "is not detectable from reported metrics."**

**Hidden stratification** — a model performing well overall while failing on a clinically important subgroup that nobody broke out separately.

**Radiomics** — extracting large numbers of quantitative features (texture, shape, intensity patterns) from images and feeding them to a classifier, as opposed to letting a neural network learn its own features.

**IBSI / METRICS / Radiomics Quality Score** — standards and scoring systems for radiomics work. Used here as appraisal instruments.

**CLAIM / TRIPOD+AI / CLEAR** — reporting checklists for medical-imaging AI, prediction models, and radiomics. **Named and applied in this review — the first in nine entries of this list.**

**ComBat / harmonisation** — statistical correction for differences between scanners and protocols. The review treats it as a prerequisite, not an optional extra, and notes it "cannot reproduce real-world heterogeneity."

**Federated learning** — training across institutions without pooling the data. The review notes it solves data-sharing but **not** annotation heterogeneity or latent bias.

**Epistemic vs aleatoric uncertainty** — uncertainty because the case is unlike anything in training (epistemic) versus uncertainty genuinely inherent in the data (aleatoric). **"Rarity guarantees that any deployed bone tumors model will encounter subtypes absent from training."**

**Saliency / Grad-CAM** — heatmaps of which image regions drove a prediction. The review notes "identical predictions can arise from models with substantially different attention patterns."

**510(k) / De Novo / Medical Device Regulation / AI Act** — the US and European routes for regulating medical AI. **No bone tumour characterisation system has cleared any of them.**

## 7. What You Can (and Can't) Say

**You can say:**

"A 2026 review in the Journal of Bone Oncology argues that the principal constraint on AI in bone tumour imaging is the stability of the reference standard rather than algorithmic capability, and quantifies that instability from published data."

"Biopsy grade agreed with final resection grade in 83% of long-bone but only 36% of pelvic central chondrosarcomas, with weighted kappa falling from 0.63 to 0.12, and sampling errors occurred in 14.7% of biopsied chondrosarcomas in one series."

"Nine musculoskeletal pathologists grading 46 cartilaginous lesions agreed with a kappa of 0.443 and eight musculoskeletal radiologists with 0.345; in lesions later judged high-risk on clinical course, agreement fell to 0.236 and 0.206."

"In one CT radiomics study's external test cohort, preoperative biopsy distinguished atypical cartilaginous tumour from higher-grade chondrosarcoma correctly in 64% of cases, against 81% for an experienced radiologist and 75% for the classifier."

"Among eight expert pathologists reviewing twelve selected osteosarcomas, the diagnosis was unanimous in only seven cases and the assigned grade ranged from low to high in six."

"Agreement is not uniformly poor — twelve bone pathologists reached an intraclass correlation of 0.78 on peripheral cartilaginous tumours — and the review concludes that instability is concentrated in grading and in the highest-consequence cases."

"No system for primary bone tumour characterisation, grading or response prediction has regulatory clearance in the United States or Europe, and the review states that every application it covers is investigational."

"Datasets predating the molecular separation of CIC- and BCOR-rearranged sarcomas from Ewing sarcoma contain those tumours under the former label."

**You cannot say:**

"AI cannot exceed expert agreement." **The defensible claim is that it cannot be *shown* to exceed it against a single-reader label**, and that apparently exceeding it suggests the model has learned one institution's labelling habits. A model can outscore inter-reader agreement by mimicking one reader.

"This review shows external-validation failures are caused by label divergence." **It proposes that as an alternative explanation.** No study tests it, and the review does not claim one does. External failure also has at least two other causes — genuine overfitting, and measurement or instrument shift.

"Expert pathologists only agree half the time." **Depends on the task.** Kappa 0.443 corresponds to roughly 63–72% raw agreement depending on how many grades are in play, and the ~50% figure applies specifically to the high-risk subgroup under a three-grade assumption. On a different task the same kind of panel reached an ICC of 0.78.

"Kappa 0.44 is the ceiling." **It is a point estimate from 46 lesions with no reported interval.** A two-rater approximation puts the 95% range at roughly 0.23 to 0.65.

"The review shows which imaging modality performs best." **Possibly, in tables I could not retrieve.** The prose contains no AUC values at all, so nothing in this summary reports comparative performance.

"This is a systematic review." **The authors explicitly say it is not** — no formal protocol, no duplicate screening, no quantitative pooling, and selection "subject to reviewer judgment."

"The review synthesised N studies." **No final included-study count appears anywhere in the text.** The reported cascade stops at 9,435 records screened by title and abstract.

"Models match experts on chondrosarcoma grading." **Reported accuracy is "comparable to expert readers," on the task where expert agreement is poorest** — which is precisely the review's point about what such a comparison can and cannot establish.

"Imaging can predict the molecular profile." **The review states the opposite:** no study it identified predicts MDM2 amplification or IDH mutation status from imaging.

**The honest one-sentence version:** *a two-author narrative review that does what most reviews only gesture at — states a falsifiable thesis, that reference-standard instability rather than algorithmic capability is the binding constraint in bone-tumour AI; quantifies it with extracted agreement statistics including a case where the biopsy reference standard was less accurate than both the radiologist and the model it was being used to grade; includes the evidence that cuts against it; reports its own methodological limits; and leaves its most interesting claim, that external-validation failure may be label divergence, as an explicitly untested hypothesis — while reporting not one confidence interval around any of the numbers its argument rests on.*

## 8. Bottom Line for Your Life

**If you or someone close to you has a bone lesion being worked up:** the single most useful thing in this paper is also the most reassuring. **A negative bone biopsy is reliable** — 98% of negative biopsies were still benign two years later. What is less reliable is the **grade**, especially in the pelvis, where the biopsy grade matched the final surgical grade only 36% of the time. **That is a known limitation of needle sampling, not a failure of your team**, and it is exactly why these cases go to multidisciplinary meetings and why surgeons sometimes revise the plan after surgery. **If a treatment decision is turning on grade alone, it is reasonable to ask whether the biopsy is likely to be representative.**

**If you are a clinician reading AI papers in any imaging field:** this review hands you a question that applies far beyond bone tumours. **Before you read a model's accuracy, ask how accurate the labels were.** If the answer key is 80% right, then 80% is the best score anybody can be measured at, and the gap between 75% and 80% may be noise in the key rather than progress in the model. **And if a paper reports a model beating expert agreement, be more suspicious, not less** — on this review's reasoning, that is the signature of a model that has learned one hospital's habits.

**If you review papers or sit on a journal board:** two concrete asks come out of this entry. **Require an interval on every agreement statistic** — this review's own thesis rests on kappas from 12 to 46 cases with no intervals anywhere, and the arithmetic shows the band around 0.443 may run from 0.23 to 0.65. **And require agreement to be reported in the subgroup that matters**, because here it nearly halved in the high-risk lesions, which are the only ones where the decision has consequences.

**If you fund research in medical AI, the review's closing distinction is the actionable part.** It separates **what effort can fix — methodological rigour, data infrastructure, multicentre harmonisation — from what it cannot: ground-truth instability, which is "a property of the disease and its evolving classification."** On that reading, money spent on better architectures for cartilage grading is money spent against a ceiling, while money spent on composite reference standards, outcome-based endpoints (recurrence, progression, response rather than a provisional histological class), and multi-institutional label harmonisation raises the ceiling itself. **The review is making a funding argument as much as a scientific one.**

**And the transferable idea, which is the reason this paper matters outside its specialty:** **every accuracy figure in medicine is a comparison between two fallible judgements, not a measurement against truth.** Chart-review adjudications, billing codes, consensus panels, another model's outputs — all are answer keys with errors in them. **When progress in a field stalls at a suspiciously specific number, check whether that number is the quality of the answer key.** Often it is.

**If you are reading the coverage:** this paper is unlikely to generate any, because its finding is that a field's reported progress is partly an artefact of its measurement. **That is the least shareable kind of result and frequently the most important.**

**This is education, not medical advice.** Nothing here should change anyone's diagnostic workup or treatment. If you have a bone lesion under investigation, the plan that matters is the one your own multidisciplinary team sets.

---

## Appendix: the pre-registered question, verification, and status on 2026-11-16

**The pre-registered question, and its answer.** Set yesterday, written down before the paper was read: **"does it quantify reference-standard disagreement, or only argue for it?"** — on the reasoning that technique 265 holds that a claim about a binding constraint needs a measured one, and that the three preceding entries had converged on reference-standard failure from three directions. **The answer: it quantifies, and it states which of its four grounds can be quantified and which cannot.** Three of four are given numbers — biopsy–resection concordance (83% vs 36%, weighted kappa 0.63 vs 0.12, sampling error 14.7%, plus the 64%/81%/75% comparison), expert agreement (kappa 0.443 and 0.345, falling to 0.236 and 0.206 in high-risk lesions; 7/12 unanimity; ICC 0.78 as counter-evidence), and molecular reclassification (named entities) — while the fourth, that histology does not predict behaviour, is left unquantified rather than padded. **Crucially, the review states its method for these figures: "extracted as reported by the primary studies, without recalculation or pooling."**

**The carried-forward instruction, and why it did not apply as written.** Yesterday also said to carry technique 283 forward, on the reasoning that "a review of this kind will report pooled estimates with intervals, and the habit of checking whether intervals touch applies to every forest plot in it." **That prediction was wrong, and informatively so.** This review **pools nothing and reports no intervals at all** — there is no forest plot and no pooled estimate to check. So the habit had nothing to act on, and the absence became the criticism instead: **technique 304 exists because the interval-checking habit found no intervals to check.** Recording the failed prediction rather than quietly dropping it.

**Arithmetic verified today, every check passing.** The search cascade closes exactly: **PubMed/MEDLINE 4,842 + Embase 6,115 + Web of Science 5,290 = 16,247** as stated, and **16,247 − 6,812 duplicates = 9,435** as stated. Kappa-to-raw-agreement conversions computed under a stated balanced-class assumption for all four reported kappas. Reader-accuracy inference solved from `Po = p² + (1−p)²/(k−1)` for two- and three-grade cases. **Attenuation table computed**, showing a ceiling of 77.7% against a 77.7%-accurate label and only 6.7 measured points available between a 90% model and a perfect one. **Implied chance agreement back-calculated** from the paired raw-agreement and kappa figures (0.541 long bone, 0.273 pelvis), flagged as approximate because the published kappas are weighted. **Kappa standard error** on 46 cases computed at 0.107 under a two-rater approximation, with the nine-rater caveat stated. **No arithmetic error was found in the review** — every figure it reports is internally consistent.

**The convergence worth recording.** From the radiologists' own interobserver kappa of **0.345** alone, under a two-grade balanced assumption with independent errors, each radiologist computes to **~79% accuracy** against the underlying truth. The review separately reports, as an empirical observation, that a radiograph classifier reached **80%** external accuracy and was "statistically indistinguishable" from musculoskeletal radiologists. **Predicted ceiling and observed plateau are one point apart.** Caveats stated in full in Section 5: the independence assumption fails in a known direction (correlated expert errors inflate agreement and therefore **overstate** accuracy, so the true ceiling is likely lower), the class-balance assumption is unverified, and the kappa and the 80% come from related but non-identical tasks. **Suggestive, not proof** — and worth running because it cost two lines.

**What could not be verified.** **All tables and figures**, including the table tabulating the ground-truth instability figures, the evidence-synthesis tables, the molecular-reclassification table and the implementation-pathway figure. Most consequentially, **the comparative performance data promised by the title**: I searched the full retrieved text and it contains **no AUC values at all**, the only occurrence of "AUC" being the abbreviation list. So **nothing in this entry reports how well any model performs**, and that is stated in the summary header, in Section 1 by omission, and in concern 4. Also absent: **any confidence interval on any kappa, ICC or concordance figure**, and **the number of studies finally included** plus any full-text screening count. **Nothing was reproduced that was not seen.**

**Positive practice worth carrying forward.** A **falsifiable thesis declared as such** ("advances a specific argument rather than surveying available technologies"). **Quantification of that thesis**, with explicit statement of which grounds can and cannot be quantified. **Extraction method disclosed**, including the no-pooling limitation. **Counter-evidence included** (ICC 0.78). **Negative findings reported as negative** (radiogenomics untested; no direct pretraining comparison). **Six reporting instruments named and applied** — CLAIM, TRIPOD+AI, CLEAR, IBSI, METRICS, RQS. **A field-specific leakage mechanism identified** and flagged as undetectable from reported metrics. **Regulatory status stated flatly** with no hedging. **A dedicated section on the review's own methodological limitations**, naming publication bias in non-replicating AI results specifically. **Complete declarations**: no funding, no competing interests, and a generative-AI disclosure specifying exactly what the tool was and was not used for, with citation verification asserted. **And a closing distinction between addressable and structural constraints** that functions as research-funding guidance.

**Reporting-guideline pattern — the streak breaks at eight, instructively.** Entries 71, 73, 74, 75, 77 and 78 named none; 69 named TRIPOD+AI with the checklist; 70 named STROBE; **76 measured the phenomenon and quantified it at 40% mean completeness** against the instrument written for the job. **Entry 79 names six instruments and is also the best-argued paper in the run.** One case does not overturn the rule, and the rule never said guidelines are useless — it said **naming one does not predict quality, so read the methods.** What entry 79 adds is the complement: **a paper that uses guidelines as analytic instruments rather than as a compliance badge tends to be a paper that was going to be careful anyway.** The guidelines did not make this review good; the same disposition produced both. **Rule updated, not abandoned.**

**Deferred status, 2026-11-16.** ***Annals* *Choosing Wisely* (42896192) — day 27**, weekly re-check and **abstract-only date both 2026-11-19, now three days out and the next scheduled fallback**; standing note that its 5.4% / 0.6–12.2% CI is a clustering signature computed across 15 recommendations rather than 4,050 responses. **Gait foundation model (42995231) — day 8**, abstract-only date **2026-11-30**; largest multiplicity problem this list will have faced (**1,887 of 3,210 tested phenotypes called significant**), first question being what false-discovery-rate procedure ran across those 3,210 tests. **Both are due a PMC re-check on 2026-11-19**, when the *Annals* threshold fires.

**Landmark check, 2026-11-09 → 11-16.** Two records, both previously assessed: the NEJM mass-surveillance Perspective (43001754) and the *Nature Medicine* gait commentary (43003904). **No new candidates; none displaces the queue.**

**Plan set on 2026-11-16.** **Next run takes shelf item (E)**, the muscle-invasive bladder cancer pathological-complete-response study in which **102 models were screened** (PMID 42997524, PMC13741961), **because today's entry supplies exactly the lens it needs.** Entry 79 establishes that measured accuracy is capped by reference-standard quality and that **scoring above the ceiling indicates a model has learned labelling conventions rather than biology** — and pathological complete response after neoadjuvant therapy is assessed on a resection specimen by a pathologist, so it is a reference standard of precisely the kind entry 79 analyses. **Two questions for (E), both written down now. (1) What is the reported agreement on the pCR reference standard itself, and does the paper acknowledge any?** — technique 294 says the ceiling is set there. **(2) With 102 models screened and a reported calibration slope CI of 0.469–1.639, how was selection among 102 candidates accounted for?** — technique 291 says selection on the reported set is optimistic by construction, and a calibration slope interval that wide already spans severe over- and under-fitting. **Shelf after today: two spares — (E) next, (F) bitewing mannequin-only.**

**Standing watch item:** PM Heart trial results (protocol PMID 42893738), quarterly.
