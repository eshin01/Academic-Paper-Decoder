# Variable generalization performance of a deep learning model to detect pneumonia in chest radiographs: A cross-sectional study

- **Authors:** John R. Zech (California Pacific Medical Center), Marcus A. Badgeley and Manway Liu (Verily Life Sciences), Anthony B. Costa, Joseph J. Titano, and Eric Karl Oermann (Icahn School of Medicine at Mount Sinai) — 6 authors
- **Venue:** PLOS Medicine, 2018;15(11):e1002683 (published November 6, 2018)
- **DOI link:** https://doi.org/10.1371/journal.pmed.1002683
- **PubMed link:** https://pubmed.ncbi.nlm.nih.gov/30399157/ (PMID 30399157)
- **Full-text link used:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6219764/ (PubMed Central, open access)
- **Basis:** FULL TEXT — introduction, complete Methods, all results including the full performance table with confidence intervals, discussion, stated limitations, and the author summary were read from the open-access PubMed Central copy. Figures and the supporting files (including the calibration plots and the engineered-prevalence table) were not retrieved, so anything living only there is marked as not retrieved rather than guessed. Ethics: approved by the Mount Sinai Health System institutional review board, with patient consent waived for this retrospective minimal-risk study. The authors state explicitly that the study had no prospective analysis plan. Funding and competing-interest statements were not present in the retrieved text. Identifiers verified against the live PubMed/NLM record; direct URL browsing is blocked in this environment, so links are constructed from that verified record.
- **Decoded:** 2026-09-18

---

# The Gist

A team took the best-known pneumonia-detection model of its day, rebuilt it, and asked a question nobody had properly asked: does it still work at a hospital it was not trained on? The answer was frequently no. But the finding that made this paper famous is stranger and more useful than that. When they merged X-rays from two hospitals that happened to have very different pneumonia rates, the combined model scored an impressive 0.931. Then, after a reviewer prodded them, they built a deliberately stupid comparison: a rule that ignores the X-ray entirely and simply guesses based on which hospital the image came from. **That rule scored 0.861.** Almost all of the impressive number was the model figuring out where the picture was taken. And it could do that essentially perfectly — it identified the source hospital correctly for 99.95% of one institution's images and 99.98% of another's, partly by spotting the little metal letter that a technician tapes to the patient's shoulder.

# Study Snapshot

- **Study type:** A cross-sectional modelling study using data from three institutions, with models trained on some sites and deliberately tested on others. The authors state the study had no prospective analysis plan, meaning the analyses were designed as they went.
- **The data:** 158,323 frontal chest X-rays from three places — the National Institutes of Health Clinical Center (112,120 images from 30,805 patients, 1992 to 2015), Mount Sinai Hospital in New York (42,396 from 12,904 patients, 2009 to 2016), and the Indiana University Network for Patient Care (3,807 from 3,683 patients).
- **The three populations were not alike.** Average age was 46.9 at the NIH, 63.2 at Mount Sinai, 49.6 at Indiana. And the pneumonia rates were wildly different: **34.2% at Mount Sinai against 1.2% at the NIH and 1.0% at Indiana.** That single fact drives most of the paper.
- **The model:** DenseNet-121, pretrained on general photographs, then fine-tuned — a rebuild of the well-known CheXNet system. About 6.96 million adjustable settings. Images were shrunk to 224 by 224 pixels.
- **How it was tested:** patients were split 70% training, 10% tuning, 20% testing at the two larger sites. All of the Indiana data was held back as a purely external test. The alarm threshold was set to catch 95% of pneumonia cases, simulating a screening tool.
- **Trained at the NIH:** internal score 0.750, dropping to 0.695 at Mount Sinai (a statistically significant fall) and 0.725 at Indiana (not significantly different).
- **Trained at Mount Sinai:** internal score 0.802, dropping to 0.717 at the NIH (significant) and 0.756 at Indiana (not significant).
- **Trained on both together:** internal score on the combined test set **0.931** — the best number in the paper — but only 0.815 at Indiana, a significant fall. And when that same combined model was tested on each site separately, it managed only 0.733 at the NIH and 0.805 at Mount Sinai.
- **The trivial rule that ignores the image entirely scored 0.861** on the combined test set, purely because Mount Sinai patients had pneumonia 34.2% of the time and NIH patients 1.2% of the time.
- **The model knows where it is.** A network trained to identify the source hospital got 22,050 of 22,062 NIH images right (99.95%), 8,386 of 8,388 Mount Sinai images (99.98%), and 737 of 771 Indiana images (95.59%). Within Mount Sinai, it separated inpatient ward X-rays from emergency department X-rays with **100% accuracy on both** — 5,805 out of 5,805 and 449 out of 449. Those two departments had different pneumonia rates: 41.1% versus 32.8%.
- **Why it could do that, discovered afterwards:** the inpatient wards used scanners from one manufacturer and the emergency department another, and the emergency images were stored with the colours inverted so that air appears white. Neither fact was known to the researchers until they went back and looked at the pictures by hand.
- **Where the model looks:** on average 35.7 of the 49 regions of an image could each independently identify the source hospital with at least 95% certainty. The metal letter marking left or right, placed by the technician, was especially informative.
- **The designed experiment.** They built five artificial training sets of 20,000 patients each — 10,000 from each hospital — identical in overall pneumonia rate and differing only in how that rate was split between the two sites, from perfectly balanced to a near-total imbalance. They also forced men and women to have equal pneumonia rates.
- **What that experiment showed.** Internally, the more lopsided the split, the better the model scored: 0.739 when balanced, rising to 0.899 at the most extreme imbalance. Externally at Indiana, the opposite: 0.732 for the balanced model, falling to 0.641 for the most imbalanced. The balanced model was the only one whose internal and external scores were statistically indistinguishable.
- **Funding / conflicts:** not present in the retrieved text.

# How Strong Is This Evidence?

**Grade: 4/5 — a cautionary finding demonstrated far more rigorously than cautionary findings usually are, including a controlled experiment that most papers of this kind never attempt.**

The easy version of this paper would have been "we tested a model at another hospital and it did worse." That is a useful observation and it is not an explanation. This team went after the mechanism. They showed the model could identify the hospital, then the department, at near-perfect accuracy. They built the trivial prevalence-only rule to quantify how much of the impressive combined score came from nothing but knowing the source. Then they did the thing that turns a suspicion into evidence: they manufactured the confounder themselves, at five levels, holding everything else fixed, and watched the exploitation rise and the external performance fall in step. A dose-response relationship that you built on purpose is about as close to proof as an observational imaging study gets.

They also went back and found the physical cause — different scanner manufacturers between departments and an inverted colour scheme — and reported that they only noticed it by hand-reviewing images after the fact. That is an unusually candid thing to publish.

Two things keep it from a 5. The authors state plainly that there was no prospective analysis plan, so several of the most compelling analyses, including the trivial baseline, were added in response to review. That is honest and it is still a weaker footing than pre-specification. And the external test set is small: Indiana contributed 3,807 images containing only **39 pneumonia cases**, which produces wide confidence intervals and is almost certainly why two of the five comparisons came back "not significantly different" rather than clearly worse.

# The Editor's Concerns

- **The labels are part of the problem they are studying.** Mount Sinai's 34.2% pneumonia rate is not purely an epidemiological fact. The authors state that their labelling method for Mount Sinai marked a study positive whenever a radiologist raised pneumonia as a possibility, a more liberal rule than the other two sites used. So some of the prevalence gap the model learned to exploit is a difference in how reports were read, not in how sick patients were. The authors say so. It does not undermine the engineered experiment, which controls prevalence directly, but it complicates every number from the natural comparisons.
- **39 pneumonia cases is a thin external test.** Indiana's confidence intervals span roughly 0.16 of AUC in places. The two "no significant difference" results should be read as "this study could not tell," not as reassurance.
- **No prospective analysis plan, stated by the authors.** The single most quoted result in the paper — the trivial rule scoring 0.861 — was added after external review. It is a brilliant analysis and it was not planned.
- **"Pneumonia" here means a radiology finding, not a diagnosis.** The authors make this point themselves: a chest X-ray finding is necessary but not sufficient, and real diagnosis requires the patient's symptoms and history, none of which the model saw.
- **Shrinking X-rays to 224 by 224 pixels throws away most of the image.** The authors note this is done for convenience, that it discards genuine radiographic detail, and that it probably *increases* reliance on confounders, because the coarse background cues survive downsampling better than fine lung texture does.
- **Calibration was wildly off across sites.** The calibration slopes ranged from 0.047 to 10.4 depending on which site trained the model and which site it was tested on. A slope that far from 1.0 means the predicted probabilities are close to meaningless outside the training site, even when the ranking is passable.
- **Some confounders would travel and still be useless.** The authors raise a case worth remembering: a model for collapsed lung may learn to spot the chest tube that treats it rather than the collapse itself. That model would generalise beautifully to other hospitals and would fail precisely on the untreated patients you need it for. Generalisation is not the same as validity.
- **The cause was found by looking, not by any method.** The scanner-manufacturer and inverted-colour explanation emerged from manual image review after the fact. There is no systematic procedure here for catching the next one, and the authors do not claim there is.
- **One note on this reading list rather than the paper:** the senior author here also appears on the two entries decoded immediately before this one. That is coincidence of queue order, but it is worth knowing that the same group both warns about confounding and builds deployed hospital systems.
- **What this study did well:** compared internal against external performance in every available direction rather than the flattering one; used a formal statistical test for comparing the curves rather than eyeballing them; built a trivial baseline that quantified how much of the headline was worthless; ran a designed experiment with five levels of an artificially created confounder while holding total prevalence constant and sex balanced; produced calibration plots for every train-test combination; demonstrated hospital and department identification directly rather than inferring it; traced the mechanism to physical scanner differences and reported how they found it; and wrote a limitations section that names its own labelling inconsistency as a driver of the effect under study.

# Statistics Spotlight

**1. The trivial baseline — the number that tells you what a score is worth.**
- *What it is:* Before believing any accuracy figure, you need to know what the dumbest defensible method scores on the same data. The gap between the two is the actual achievement.
- *How this paper used it:* The combined model scored 0.931 on the merged test set. A rule that never looks at the X-ray at all, and simply assigns every Mount Sinai patient the Mount Sinai average pneumonia rate and every NIH patient the NIH average, scored **0.861**. The model's real contribution over knowing-nothing-but-the-hospital is the space between 0.861 and 0.931, not the space between 0.5 and 0.931.
- *The theory, with a worked example:* AUC measures ranking: pick one patient with pneumonia and one without, how often does the model score the first one higher? Now consider the merged group. A patient drawn at random from Mount Sinai has a 34.2% chance of pneumonia; one from the NIH has a 1.2% chance. So in most randomly drawn pairs where one has pneumonia and one does not, the pneumonia patient is from Mount Sinai. Sorting by hospital therefore gets the ordering right most of the time, without any medical information whatsoever. It is like predicting who owns a winter coat by asking which city they live in — you will be right constantly, and you will have learned nothing about coats. The prevalence gap does all the work.
- *Watch out:* This trap appears whenever datasets from different sources are pooled, which modern medical AI does constantly to reach impressive sample sizes. **Merging data from places with different disease rates hands a model a free shortcut, and the resulting score looks like skill.** When you read a study that combined data from multiple hospitals, look for the disease rate at each one. If they differ substantially and no baseline is reported, the headline number is partly measuring geography. Note also that this paper's authors did not think of this themselves; a reviewer did.

**2. DeLong's test — the right way to compare two AUCs, and what it cannot do.**
- *What it is:* Two models, or one model on two test sets, produce two AUC scores. DeLong's test asks whether the difference between them is bigger than you would expect from chance given how many cases you have. There is a paired version, for two models on the same patients, and an unpaired version for different patients. This paper used both as appropriate.
- *How this paper used it:* Every internal-versus-external comparison. Trained at the NIH, internal 0.750 against external 0.695 at Mount Sinai: P below 0.001, a real drop. Trained at Mount Sinai, internal 0.802 against 0.717 at the NIH: P below 0.001. The joint model's 0.931 internal against 0.815 at Indiana: P = 0.001. But the two comparisons involving Indiana as an external site for single-hospital models came back P = 0.580 and P = 0.273 — not significant.
- *The theory, with a worked example:* Why did the Indiana comparisons fail to reach significance when the differences looked meaningful? Because AUC precision depends mostly on how many cases of the disease you have, and Indiana had **39**. With 39 cases, the confidence interval on an AUC of 0.725 ran from 0.644 to 0.807 — wide enough to swallow the difference. It is like judging two restaurants when one has 4,000 reviews and the other has 11. The 11-review restaurant might be better or worse; you cannot tell. This is the same lesson the Poplin retinal paper taught from the other direction, where 105 events made 0.70 and 0.72 indistinguishable.
- *Watch out:* The failure mode here is reading "not significant" as "the same." The paper is careful about this: its conclusion says performance was worse in 3 out of 5 comparisons, not that it was fine in the other 2. When a study reports a null result on a small subgroup, ask how many events that subgroup contained before concluding anything. Also note what the presence of DeLong's test signals in general: many papers compare two AUCs by printing them next to each other and letting you assume. A formal test is a mark of seriousness.

**3. Manufacturing a confounder — turning a suspicion into an experiment.**
- *What it is:* A confounder is a third factor that lets a model appear to solve your problem while actually solving a different one. Normally you can only argue about confounders after the fact. Here the authors built one on purpose, at several strengths, and measured what it did.
- *How this paper used it:* Five training sets, each 20,000 patients, 10,000 from each hospital, all with the same overall pneumonia rate, differing only in how that rate was distributed between the two sites — from evenly split to almost entirely on one side. They also forced pneumonia rates to be equal between men and women, so sex could not sneak in as a second shortcut. Internal scores climbed as the imbalance grew: 0.739 balanced, 0.899 at the most extreme. External scores at Indiana moved the opposite way: 0.732 balanced, 0.641 at the most extreme. Only the balanced model showed no significant gap between internal and external (P = 0.880).
- *The theory, with an analogy:* This is the structure of a dose-response study, the same logic that established smoking causes cancer. More of the suspected cause, more of the effect — and here, in a designed setting where the authors controlled the dose. Because every cohort had 20,000 patients, the same overall disease rate, and balanced sex, the *only* thing changing was how useful "which hospital" was as a clue. Watching internal and external performance move in opposite directions as that clue got stronger is not a correlation you have to argue about. It is the mechanism, demonstrated.
- *Watch out:* This design is rare, and its absence in other papers should not be treated as a flaw — but its presence should raise your confidence substantially. More practically, the lesson generalises past hospitals. Any systematic difference between your data sources that correlates with the outcome will be exploited: scanner brand, image compression, which shift ordered the test, whether the patient was sick enough to need a portable machine. The finding here that the model separated two departments in the *same hospital* with 100% accuracy, and that those departments had different pneumonia rates, means that even building a model for a single site does not make you safe.

# Jargon Translator

- **Chest radiograph / chest X-ray:** the standard image of the lungs and chest.
- **Frontal versus lateral:** front-on versus side-on views. Only frontal images were used here.
- **Portable radiograph:** taken by wheeling a machine to the patient, used when someone is too unwell to travel to the radiology department. These patients are sicker on average, which matters a lot in this paper.
- **Convolutional neural network (CNN):** the standard kind of AI model for images.
- **DenseNet-121 / CheXNet:** a specific network design, and the well-known pneumonia model this study rebuilt.
- **Pretraining and fine-tuning:** starting from a model already trained on millions of ordinary photographs, then adjusting it on X-rays. Standard practice, and it is why images get shrunk to 224 by 224 pixels.
- **Train, tune, test:** the three slices of data — one to learn from, one to make design choices with, one kept sealed for the final score.
- **Internal versus external testing:** internal means new patients from the same hospital that supplied the training data. External means a different hospital entirely. The gap between them is this paper's subject.
- **AUC / AUROC:** a ranking score from 0.5 (coin flip) to 1.0 (perfect).
- **DeLong's test:** the standard statistical test for whether two AUC scores genuinely differ.
- **Confounder:** a factor that lets a model get the right answer for the wrong reason.
- **Prevalence:** how common a condition is in a group. 34.2% at one hospital versus 1.2% at another is the engine of this whole study.
- **Calibration slope:** whether predicted probabilities match reality. 1.0 is perfect; this study saw values from 0.047 to 10.4 across sites.
- **Activation map / heatmap:** a picture showing which parts of an image most influenced the model's answer.
- **Laterality token:** the small metal letter a technician places on the patient to mark left or right. Different hospitals use different ones, which is how a model can tell them apart.
- **Natural language processing (NLP):** software that reads the radiologist's written report to extract whether a finding was present. It generated most of the labels here.
- **Cross-sectional study:** a snapshot of data at one point rather than following people forward.

# What You Can (and Can't) Say

**Fair to say:**
- "A 2018 PLOS Medicine study found that pneumonia-detection models trained at one hospital performed significantly worse at another in 3 of 5 comparisons."
- "Their combined-hospital model scored 0.931, but a rule that ignored the X-ray entirely and used only which hospital the image came from scored 0.861 on the same test set."
- "The model identified the source hospital for over 99.9% of images at two sites, and separated inpatient from emergency department X-rays within one hospital with 100% accuracy — departments that had pneumonia rates of 41.1% and 32.8%."
- "In a designed experiment, the more the pneumonia rate differed between the two training hospitals, the better the model scored internally and the worse it scored at an outside hospital."
- "The cause was traced to different scanner manufacturers and an inverted image colour scheme, which the researchers only discovered by reviewing images by hand afterwards."

**Not fair to say:**
- "AI cannot read chest X-rays" — the models did carry real signal. The finding is that some of the reported performance was confounded, and that internal test scores overstate what you get at a new hospital.
- "Models always perform worse externally" — the authors explicitly note that external performance can be better or worse depending on how each dataset was built and labelled.
- "The models were overfitting" — the paper is careful that this is a different failure. All results are on held-out test data, and the models generalised fine within their own hospitals. They were fitting a real pattern that happened to be about geography.
- "Training on a single hospital avoids this" — within one hospital, the model separated two departments perfectly, and those departments had different disease rates.
- "The model diagnoses pneumonia" — the labels are radiology findings extracted from written reports, and at one site a report counted as positive when the radiologist merely raised pneumonia as a possibility.

# Bottom Line for Your Life

This is the paper to keep when you want one example of how a number can be completely real and completely misleading at the same time. Nobody cheated. The 0.931 was correctly computed on properly held-out data. It was also, mostly, a measurement of whether an X-ray came from Manhattan or Maryland.

The lesson generalises well past medicine. Any time results from different sources are pooled, and those sources differ in how often the thing you are predicting happens, a model can score well by identifying the source. It will look like skill. The authors caught it only because a reviewer asked them to build a baseline that ignored the images, and the baseline scored 0.861.

So the question to carry: **compared to what?** Not compared to chance, which is a meaninglessly low bar, but compared to the laziest rule that could exploit the structure of the data. In this case the lazy rule captured most of the headline. That is the single most useful habit you can take from twenty-one papers of reading.

The second habit is smaller and more concrete. When a study reports a model working well, find out whether it was ever tested somewhere it was not built. Here the answer changed 0.931 into 0.815, and into 0.733 when the same model faced NIH patients alone.

Nothing here changes anything about your own care. This is a study of software, not patients. One study is one data point. This is an educational breakdown, not medical advice.

---

**Sources** (based on articles retrieved from PubMed and PubMed Central; identifiers verified against the live PubMed/NLM record — URL browsing is blocked in this environment, so links are constructed from that verified record):
- DOI: https://doi.org/10.1371/journal.pmed.1002683
- PubMed: https://pubmed.ncbi.nlm.nih.gov/30399157/ (PMID 30399157)
- Full text (PMC, open access): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6219764/
