# Prediction Models for In-Hospital Delirium Using Routinely Collected Electronic Health Record Data: Systematic Review

- **Authors:** Hung-Min Huang (Institute of Health Informatics, University College London), Chun-Shun Lu (MacKay Memorial Hospital, Taipei), Geng-Wei Chang and Ming-Hsu Tien (Chang Gung Memorial Hospital, Taipei), Yu-Kai Hsu (Far Eastern Memorial Hospital, Taipei) — 5 authors
- **Venue:** JMIR Medical Informatics, 2026;14:e91618 (published September 16, 2026)
- **DOI link:** https://doi.org/10.2196/91618
- **PubMed link:** https://pubmed.ncbi.nlm.nih.gov/42748492/ (PMID 42748492)
- **Full-text link used:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC13581283/ (PubMed Central, open access)
- **Basis:** FULL TEXT — introduction, complete Methods, all results sections, the full study-characteristics and performance tables, the risk-of-bias findings, discussion, stated limitations, and conclusions were read from the open-access PubMed Central copy. Figures and the four supplementary appendices were not retrieved, so anything living only there is marked as not retrieved rather than guessed. The review states it was **not prospectively registered** in PROSPERO because registration was not completed before screening began, and the authors list this as a limitation. Funding and competing-interest statements were not present in the retrieved text. Identifiers verified against the live PubMed/NLM record; direct URL browsing is blocked in this environment, so links are constructed from that verified record.
- **Decoded:** 2026-09-20
- **Note:** this entry was queued on 2026-09-17 as not yet reachable. A PubMed Central copy has since appeared, so it could be decoded in full.

---

# The Gist

Delirium is the sudden confusion that descends on hospital patients, especially older ones, and it predicts longer stays, worse recovery, and lasting cognitive damage. Since the electronic chart already holds everything about a patient, dozens of teams have built software to flag who will become delirious. This review went looking for all of that work, found 29 studies, and graded each one against the formal checklists the field uses to judge prediction models. The headline sounds encouraging: most models score well. The details do not. Only 41% were ever tested at a hospital other than the one that built them, and among the handful where you can compare directly, performance dropped in 5 of 7. Only 10% asked whether acting on the model would actually help anyone. And the finding most worth carrying: **more complicated algorithms did not reliably beat simpler ones.** After a decade of this work, the reviewers conclude that no model is ready for routine use.

# Study Snapshot

- **Study type:** A systematic review — a structured search for every study meeting stated criteria, followed by formal appraisal of each. No new patients, no new model, no new data. Its subject is the quality of a research literature.
- **The search:** four databases (PubMed/MEDLINE, Embase, PsycINFO, Web of Science) from their beginnings through November 11, 2025.
- **The funnel:** 1,086 records found, 673 unique after removing duplicates, 603 rejected on title and abstract, 70 full papers read, 41 rejected, **29 studies included**.
- **Two people did everything, independently.** Screening, data extraction, and quality appraisal were each done by two reviewers working separately, with a third brought in to settle disagreements.
- **The appraisal machinery:** four named frameworks. PRISMA for how to report a review, CHARMS for what to extract from a prediction-model study, TRIPOD and its AI extension for what a model paper should report, and PROBAST for scoring risk of bias across four areas — who was studied, what predictors were used, how the outcome was determined, and how the analysis was done.
- **What the 29 studies looked like.** Retrospective cohorts dominated: 20 of 29 (69%). Four were prospective (14%), four combined retrospective building with prospective testing (14%), and one was a case-control design (3%).
- **Where they were done:** general wards 13 (45%), mixed ward and intensive care 8 (28%), intensive care only 7 (24%), emergency department 1 (3%). Slightly over half, 15 of 29 (52%), used a single hospital.
- **Sizes ranged enormously,** from a prospective deployment cohort of 93 patients to a multi-database study of 104,303.
- **How common delirium was varied just as much.** Among the 20 studies where a rate could be extracted, 6 (30%) had delirium in under 5% of patients, 10 (50%) between 5% and 20%, and 4 (20%) above 20%. This single fact drives much of the review's argument.
- **The models:** conventional machine learning in 10 studies (34%), statistical or rule-based approaches in 8 (28%), deep learning in 5 (17%), and hybrids in 6 (21%).
- **What they fed in:** demographics in 28 of 29 (97%), existing diagnoses in 25 (86%), lab values in 22 (76%), medications in 20 (69%), vital signs in 17 (59%), nursing and care-process variables in only 7 (24%). Just 8 (28%) used any free text from clinical notes, and in several of those the text was used to identify who *had* delirium rather than to predict it.
- **Reporting gaps were routine.** How missing data was handled went unreported in 7 of 29 (24%). How the imbalance between many healthy and few delirious patients was handled was absent or unreported in 16 of 29 (55%).
- **The headline performance numbers look good.** Internal scores were reported in 24 of 29 (83%), ranging from 0.77 to 0.97. Confidence intervals were reported inconsistently.
- **External testing was the exception.** Only 12 of 29 (41%) reported a score from a hospital other than the development site, ranging from 0.69 up to about 0.95.
- **Where you can compare the two directly, performance fell.** Seven studies allowed a clean internal-versus-external comparison. In 5 of those 7 (71%), the external score was lower. Mean internal 0.845, mean external 0.772 — **a drop of 0.073**. The reviewers state explicitly this is a descriptive observation, not a pooled estimate.
- **Individual falls were sometimes severe.** One study went from 0.919 internally to 0.721 externally. Another from about 0.90 on its own test set to 0.72 elsewhere. One dropped from 0.81 looking backwards to 0.69 when finally run forward in time.
- **The measure that matters in rare conditions was almost never reported.** Only 6 of 29 (21%) gave a precision-recall score internally, and only 2 (7%) externally.
- **Almost nobody asked whether using the model would help.** Decision curve analysis, which weighs benefits against harms at a given alarm setting, appeared in 3 of 29 (10%). Calibration was assessed in 15 (52%), by a scattered assortment of methods.
- **Real-world testing was rare.** Prospective evaluation in 8 of 29 (28%), some workflow integration in 9 (31%) — but the reviewers note few of those measured what clinicians actually did, how many alarms fired, or what happened to patients.
- **The quality verdict:** overall risk of bias was judged **low in 8 studies (28%), unclear in 10 (34%), and high in 11 (38%)**. The problems clustered in how analyses were done, not in whether the questions mattered.
- **Funding / conflicts:** not present in the retrieved text.

# How Strong Is This Evidence?

**Grade: 4/5 — a properly conducted systematic review with dual independent appraisal against the field's own standards, whose main structural weakness is that its protocol was not registered before the work began.**

Most of what a careful reader wants is here. Four databases rather than one. Two reviewers working independently at every stage, with a third to break ties — which matters, because a single reader deciding what counts is how reviews acquire their author's preferences. Four formal frameworks applied rather than informal judgement. And a decision the reviewers deserve credit for: they refused to pool the results into a single average performance figure, on the grounds that the studies were measuring meaningfully different things at different moments in different populations. Pooling would have produced a tidier headline and a less honest one.

They also labelled their own most quotable number carefully. The 0.073 average drop from internal to external testing comes from just 7 studies, and they say in the text that it "should not be interpreted as a pooled effect estimate." That is the kind of sentence that gets deleted in less careful papers.

What holds it at 4 is the registration gap. A systematic review's protocol — written and filed publicly before you start — is the main thing preventing a review from drifting toward whatever its authors find as they go. These authors acknowledge they did not do this and list it as a limitation, which is honest, but honesty does not restore the protection. English-only inclusion is a second, smaller limit. And a review inherits everything wrong with what it reviews: with 38% of included studies at high risk of bias, the summary of a field cannot be more reliable than the field.

# The Editor's Concerns

- **"Unclear risk of bias" describes 10 of 29 studies, and it is a verdict about reporting, not quality.** The reviewers are explicit that these studies were "limited by incomplete reporting rather than obvious methodological failure." From the outside there is no way to tell a sound study that was written up poorly from an unsound one. That distinction is invisible to any reader, including this one.
- **The external-validation comparison rests on 7 studies.** Out of 29. The 0.073 average drop is the most quotable figure in the review and the thinnest. The reviewers flag this; anyone citing the number should too.
- **Of 29 studies, only 3 asked whether the model would do any good.** Decision curve analysis answers whether acting on predictions beats the alternatives at a realistic alarm setting. Ten percent of a field performing that check, after a decade of work, is the review's quietest and most damning number.
- **Over half the studies never said how they handled the imbalance** between the many patients without delirium and the few with it. In a task where the outcome is sometimes under 5%, that choice substantially shapes the resulting numbers.
- **The outcome itself was measured differently everywhere.** Some studies used bedside assessment instruments, some used billing codes, some used chart review, some used software reading notes. The reviewers state these "identify overlapping but not identical clinical events." So two studies reporting the same score may not be predicting the same thing.
- **The studies are not doing one job.** Some predict at admission, some over a surgical recovery window, some update hourly in intensive care. The reviewers stress these are not interchangeable, and that a model predicting six hours ahead in an ICU has access to signals an admission-time model cannot have. Comparing their scores directly is close to meaningless.
- **Nobody tested models across settings.** Moving an intensive-care model to a general ward, or the reverse, was described as uncommon — yet that is exactly the transfer a hospital would attempt.
- **Clinical notes are barely used.** Only 8 of 29 studies touched free text, even though confusion and agitation are precisely the things nurses describe in words rather than record as numbers. The reviewers name this as an opportunity and warn that text used for both predicting and defining the outcome risks contaminating one with the other.
- **Not registered in advance,** and English only. Both stated by the authors.
- **What this review did well:** searched four databases from inception; used two independent reviewers at screening, extraction, and appraisal with a third for disagreements; applied four named reporting and appraisal frameworks rather than informal judgement; declined to meta-analyse and explained why; labelled its own internal-versus-external comparison as descriptive rather than a pooled estimate; broke the high-risk studies down by which specific failing earned the rating; separated risk of bias from applicability, and noted applicability was the lesser problem; and closed with concrete reporting demands, including that future papers state how many patients would be flagged and how much work that creates.

# Statistics Spotlight

**1. Why a great AUROC can hide a useless tool when the condition is rare.**
- *What it is:* AUROC asks a ranking question: take one patient who will become delirious and one who will not, how often does the model score the first higher? Precision-recall asks a different question, about the alarms the model actually raises: of everyone flagged, what share genuinely develop delirium? The second depends heavily on how common the condition is. The first barely does.
- *How this review used it:* AUROC was reported in 24 of 29 studies, ranging 0.77 to 0.97. A precision-recall score appeared internally in just 6 studies (21%) and externally in 2 (7%). The review states the consequence plainly: "in low-prevalence settings, even a model with good AUROC may have low positive predictive value and may generate many false-positive alerts." One large study makes it concrete — it reported an AUROC of 0.848 internally and 0.824 externally, healthy-looking numbers, alongside precision-recall scores of 0.192 and 0.118.
- *The theory, with a worked example:* Picture a ward of 1,000 patients where 30 will become delirious, a 3% rate. A model with an excellent AUROC ranks almost all 30 above most of the other 970. Now draw the alarm line somewhere useful — say it catches 24 of the 30. Because the healthy group is 32 times larger, even a small error rate among them produces a flood: flag 10% of the 970 and you get 97 false alarms alongside your 24 real ones. Four in five alarms are wrong, and the AUROC never told you. The ranking was genuinely good. The decisions are still mostly noise, because rarity does the damage.
- *Watch out:* This is the most common way a medical AI number misleads without anyone lying. AUROC is reported nearly universally because it looks impressive and does not move when the disease is rare. The two questions that cut through: **how common was the condition, and of everyone the model flagged, what fraction were real?** If a paper gives you a strong AUROC on a condition affecting a few percent of patients and no precision figure, you have not learned whether the tool is usable. In this literature, four out of five papers left that blank.

**2. The drop from internal to external testing — now measured across a whole field.**
- *What it is:* Internal performance is measured on new patients from the same hospital that supplied the training data. External performance means a genuinely different institution. The gap between them is the best available estimate of what happens on deployment.
- *How this review used it:* Only 12 of 29 studies (41%) reported any external number. Among the 7 where internal and external could be compared directly, 5 (71%) were lower externally, with a mean drop from 0.845 to 0.772. Individual cases were worse than the average: 0.919 falling to 0.721, and one study reporting an eight-percentage-point decline when its model crossed to another hospital.
- *The theory, with an analogy:* Two days ago on this list, the Zech chest X-ray study showed *why* this happens — models learn the fingerprints of the place that trained them, from scanner brands to documentation habits to how common the disease is locally. This review shows *how often* it happens, across an entire body of literature. It is the difference between a chef who cooks brilliantly in their own kitchen and one who can cook in yours. Almost nobody in this field has been asked to cook in somebody else's kitchen: 17 of 29 studies never left home.
- *Watch out:* Here is the trap specific to reading a field rather than a paper. The range of internal scores, 0.77 to 0.97, comes from 24 studies. The external range, 0.69 to 0.95, comes from 12. So the impressive-looking overall picture is built mostly from home-field numbers, and the papers that took the harder test are a self-selected minority — plausibly the more confident ones. When you see a field summarised by its best figures, ask what fraction of studies even attempted the demanding version of the test. Here it was under half.

**3. Structured risk-of-bias assessment — and what "unclear" really tells you.**
- *What it is:* Rather than judging papers by impression, reviewers apply a published instrument with fixed questions. PROBAST covers four areas: were the right participants studied, were the predictors handled properly, was the outcome determined reliably, and was the analysis sound. Each area gets low, high, or unclear, and two reviewers score independently.
- *How this review used it:* Low risk in 8 studies (28%), unclear in 10 (34%), high in 11 (38%). They then broke down what earned the 11 high ratings: inadequate handling or reporting of missing data in 6, limited or absent calibration in 4, performance reported without any validation in 1, case-control design in 2, and incomplete reporting of how predictors were selected in 2, with several studies having more than one problem.
- *The theory, with an analogy:* It works like a building inspection. The inspector does not ask whether the house looks nice; they check the wiring, the foundations, the plumbing, the roof, against a fixed list. A house can be beautiful and fail. A prediction model can report a superb score and fail, because the score was produced by a process that could not have been trusted to produce an honest one. Two inspectors are used for the same reason banks use two appraisers. Now the important subtlety: **risk of bias is a judgement about the process, not the result.** A high-risk study might have reached the correct answer by luck. The rating says you cannot tell from what was reported.
- *Watch out:* "Unclear," the middle category, applies to more than a third of these studies and is the one people misread. It does not mean borderline quality. It means the paper did not say enough for anyone to judge — and the reviewers note these studies were usually limited "by incomplete reporting rather than obvious methodological failure." So a third of this literature sits in a state where a careful reader genuinely cannot separate good work from bad. That is a finding about scientific writing as much as about science, and it is the strongest argument for the reporting checklists this review keeps naming.

# Jargon Translator

- **Delirium:** an acute state of confusion, inattention, and sometimes agitation that comes on suddenly in hospital, especially in older patients. It predicts longer stays, worse outcomes, and lasting cognitive problems.
- **Systematic review:** a structured search for every study meeting stated criteria, with pre-specified methods, rather than an author's personal selection.
- **Meta-analysis:** combining studies into a single pooled number. Deliberately not done here because the studies were too different.
- **PRISMA:** the standard for how to report a systematic review.
- **PROBAST:** the tool for scoring risk of bias in a prediction-model study, across participants, predictors, outcome, and analysis.
- **TRIPOD / TRIPOD-AI:** standards for what a prediction-model paper must report, with an extension for AI models.
- **CHARMS:** a checklist for what to extract from prediction-model studies when reviewing them.
- **PROSPERO:** the public register where a review's protocol is filed before work starts. This review was not registered, which the authors flag.
- **Electronic health record (EHR):** the hospital's digital chart.
- **Routinely collected data:** information already captured during normal care, as opposed to measurements taken specially for research.
- **AUROC:** a ranking score from 0.5 (coin flip) to 1.0 (perfect).
- **Precision-recall / PR-AUC:** a performance measure that, unlike AUROC, responds strongly to how rare the condition is. Reported by only a fifth of these studies.
- **Positive predictive value (PPV):** of everyone the model flags, the share who really have the condition.
- **Calibration:** whether a predicted 20% risk corresponds to a real 20%. Assessed in about half these studies.
- **Decision curve analysis:** a method for asking whether acting on the model beats the alternatives. Used in 3 of 29 studies.
- **Internal vs external validation:** tested on new patients from the same hospital, versus a genuinely different institution.
- **Temporal validation:** tested on a later time period than the training data.
- **Prospective evaluation:** running the model forward in real time rather than on stored records.
- **Class imbalance:** having far more patients without the condition than with it, which distorts training and metrics if unhandled.
- **Natural language processing (NLP):** software that reads clinical notes.
- **Confusion Assessment Method (CAM):** the standard bedside test for delirium, with a version adapted for intensive care.

# What You Can (and Can't) Say

**Fair to say:**
- "A 2026 systematic review of 29 studies found that delirium prediction models built from routine hospital records commonly report scores between 0.77 and 0.97, but that only 41% were ever tested at an outside hospital."
- "Among the seven studies allowing a direct comparison, five performed worse externally, with an average drop of 0.073 — which the reviewers describe as descriptive rather than a pooled estimate."
- "More complex algorithms did not consistently outperform simpler statistical or rule-based approaches."
- "Risk of bias was judged high in 11 of 29 studies and unclear in another 10, mostly because of how analyses were done or reported."
- "Only 3 of 29 studies assessed whether acting on the model's predictions would produce net clinical benefit."
- "The reviewers conclude that no single algorithm is ready for routine adoption."

**Not fair to say:**
- "AI can predict delirium with up to 97% accuracy" — 0.97 is a ranking score, not accuracy, it comes from a single study's own hospital, and the review's whole argument is that such numbers do not establish usefulness.
- "Delirium prediction models don't work" — the review's conclusion is that routine data does carry real risk signal. The gap is between technical feasibility and clinical readiness.
- "Machine learning is no better than simple scoring rules" — the finding is narrower: complexity did not *consistently* help in these studies, under comparable conditions.
- "This review proves models fail when moved between hospitals" — 5 of 7 comparable studies declined. Seven studies is a thin base, as the reviewers say.
- "38% of delirium models are biased" — PROBAST rates the risk that a study's *methods* could produce a misleading result. It is not a finding that the models discriminate against anyone, and it is not a verdict that their results are wrong.

# Bottom Line for Your Life

This one is less about delirium than about how to judge a whole body of work, which is closer to what you actually face when a claim reaches you with "studies show" attached.

Watch what the reviewers did. They did not read 29 papers and form an impression. They applied a fixed checklist to each one, with two people scoring independently and a third to settle disputes, and they published the distribution: 8 sound, 10 unreadable, 11 flawed. That structure is what separates a review from an opinion, and it is worth recognising when you encounter one.

The number to carry out of here is 3 out of 29. That is how many of these studies asked whether using the model would help a patient, as opposed to whether the model scored well. A decade of effort, dozens of publications, impressive figures throughout, and the question of benefit was posed ten percent of the time. That gap between "works" and "helps" has now appeared in nearly every entry on this list, and this review measures it.

The second thing to carry is about rarity. When a condition affects a few percent of people, a tool can rank patients beautifully and still be wrong about four alarms in five. The scores in these papers are real. They are also, on their own, not enough to know whether a ward could use the thing.

And a small practical note for the human side of this. If an older relative is in hospital and becomes suddenly confused, that is a recognised medical event with established bedside tests, not simply a bad night. Say something to the staff. That advice comes from delirium being a serious, detectable condition, not from any model in this review. One study is one data point, and a review of 29 is a map of how much is still unknown. This is an educational breakdown, not medical advice.

---

**Sources** (based on articles retrieved from PubMed and PubMed Central; identifiers verified against the live PubMed/NLM record — URL browsing is blocked in this environment, so links are constructed from that verified record):
- DOI: https://doi.org/10.2196/91618
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42748492/ (PMID 42748492)
- Full text (PMC, open access): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC13581283/
