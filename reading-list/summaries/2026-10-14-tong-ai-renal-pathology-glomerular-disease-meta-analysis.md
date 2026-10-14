# Artificial intelligence-powered renal pathology for glomerular disease classification: a systematic review and meta-analysis

**Authors:** Tong M, Jiang Y, Zhu R, Ding Z, Ma D, Yin J, Zhang Y, Yuan Z, Ren X
**Journal:** Renal Failure, 2026; 48(1): 2729643 (published 6 October 2026)
**Decoded:** 2026-10-14
**Analysis basis:** FULL TEXT (retrieved from PubMed Central, PMC13644454). Figures were not viewable — only captions and auto-generated descriptions — and the supplementary tables (search strings, PROBAST+AI matrices, GRADE grids, per-study performance, meta-regression results) were not retrievable, so anything living only in those is marked as not retrieved.

**Source links (all verified against the live PubMed record):**
- DOI: https://doi.org/10.1080/0886022X.2026.2729643
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42838512/
- Full text (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC13644454/
- Protocol registration: stated in the paper as PROSPERO CRD420261278316. **This identifier could not be verified** and its format looks irregular — see The Editor's Concerns. No link to it is given here.

---

## 1. The Gist

When someone's kidneys start leaking protein, the way to find out why is a biopsy. A pathologist looks at the tissue under a microscope and decides which of about eight diseases it is. That decision determines the treatment, and the diseases can look confusingly similar. Experienced renal pathologists are scarce, and they disagree with each other more than anyone would like.

So people have been training AI to read these slides. This paper gathers up fifteen such studies and pools their results.

The headline looks superb. For membranous nephropathy, pooled accuracy 0.96. For IgA nephropathy, 0.94. For minimal change disease, 0.96, with a pooled area-under-the-curve of 1.00 — perfect.

Now look at the same table two columns to the left. For mesangial proliferative glomerular disease, the pooled accuracy is 0.96 and the pooled **sensitivity is 0.61**. The models miss two in five actual cases of that disease while scoring 96% "accuracy." For membranoproliferative disease: accuracy 0.91, sensitivity 0.60.

That is not a contradiction. It is what happens when you report accuracy for an uncommon disease. In this data, mesangial proliferative disease is about 5.6% of biopsies — so a model that simply never diagnoses it at all is already 94.4% accurate on that label. The reported 0.96 beats doing nothing by about one and a half percentage points.

Two more things matter. The pooled estimates disagree enormously between studies: more than half have a heterogeneity statistic above 90%, which means the studies are not measuring the same thing. And **specificity — how often the AI correctly rules a disease out — was never pooled at all**, because most of the original studies did not report enough data to calculate it.

What saves this paper from being misleading is that the authors say almost all of this themselves, in unusually plain language. They state the totals are "analysis units rather than unique patients." They state they could not fit a proper diagnostic-accuracy model. They call the comparison with pathologists "exploratory," "descriptive and hypothesis-generating," and explicitly "not head-to-head." Their conclusion is that current evidence "is insufficient to establish superiority over pathologists."

The one sentence that will travel further than all that care is in the abstract: "AI also showed higher accuracy than senior pathologists for IgAN, MN, and MCD." In the full text, the senior-pathologist data comes from **one study**.

## 2. Study Snapshot

**Design:** Systematic review and meta-analysis of diagnostic accuracy, reported against PRISMA-DTA.

**Registration:** stated as PROSPERO CRD420261278316 (not verified; format appears irregular).

**Searched:** PubMed, Embase, Web of Science and Cochrane Library, from inception to 15 July 2026. No language or date restriction at the database stage; non-English papers and conference abstracts excluded later, at screening.

**The funnel:** 1,804 records found (PubMed 349, Embase 1,020, Web of Science 408, Cochrane 27) → 564 duplicates removed → 1,240 screened → 51 full texts assessed → 36 excluded (5 no diagnostic outcomes, 3 non-English, 9 non-histopathological diagnosis, 19 not about distinguishing glomerular disease) → **15 studies included**, published 2021 to 2026.

**All 15 studies were retrospective.** None was prospective.

**Sample size, and what the units actually are:** 67,056 training units and **39,536 validation units**. The authors state plainly that "these totals represent analysis units rather than unique patients," and break them down: 16,223 patient-based, 9,505 image-based, 9,988 glomerulus-based, 3,820 lesion-based. Those sum exactly to 39,536. **Only 41% of the "units" are patients.**

**Diseases covered:** IgA nephropathy (IgAN), membranous nephropathy (MN), minimal change disease (MCD), focal segmental glomerulosclerosis (FSGS), lupus nephritis (LN), diabetic nephropathy (DN), membranoproliferative (MPGN) and mesangial proliferative (MsPGN) glomerular disease.

**Reference standard:** stated in the inclusion criteria as pathology confirmation. In the study table, roughly half the entries are recorded as "Pathology" and roughly half as "Expert consensus."

**AI architectures:** stacking classifiers most common (6 validation datasets), then Swin Transformer and D-ResNeXt101 (3 each), D-CNN and DETR + ViT-G (2 each), the rest once.

**Quality appraisal:** PROBAST+AI for risk of bias, GRADE for certainty. Screening and extraction done in duplicate with agreement reported — Cohen's kappa 0.87 for title/abstract, 0.89 for full text, 0.91 for extraction.

**Statistics:** random-effects meta-analysis by restricted maximum likelihood with the Hartung-Knapp-Sidik-Jonkman adjustment. Heterogeneity by I² and tau², **with 95% prediction intervals reported for every estimate**. A clinical-relevance threshold of 0.80 was set in advance. Leave-one-out sensitivity analyses and Egger's test for publication bias were restricted to outcomes with at least 10 validation datasets. Prespecified subgroup analyses and meta-regression covered validation type, imaging modality, database accessibility, **unit of analysis**, and single- versus multi-centre. Pathologist comparisons used Z-tests. R 4.5.2 with `meta`, `metafor`, `ggplot2`.

**What could not be done, in the authors' own words:** "Because complete 2 × 2 data and specificity estimates were unavailable for most studies, a bivariate or HSROC model could not be applied in a stable and interpretable manner. The pooled sensitivity, precision, accuracy, F1 score, and AUC were therefore treated as complementary reported performance measures rather than as a complete paired sensitivity-specificity diagnostic accuracy model." They also declined to impute specificity, because doing so "could introduce bias." **So there is no pooled specificity anywhere in this paper.**

**Main pooled results (sensitivity, precision, accuracy, F1, AUC):**
- MN (22 validation datasets; AUC from 10): 0.96, 0.94, 0.96, 0.95, 0.98
- IgAN (14; AUC from 11): 0.92, 0.91, 0.94, 0.90, 0.96
- MCD (11; AUC from 6): 0.92, 0.87, 0.96, 0.89, **1.00 (95% CI 0.99–1.00)**
- LN (8): 0.79, 0.90, 0.97, 0.84, 0.95
- DN (8): 0.78, 0.90, 0.96, 0.83, 0.93
- FSGS (3; no AUC): 0.77, 0.62, 0.93, 0.68
- MsPGN (7): **0.61**, 0.72, **0.96**, 0.66, 0.97
- MPGN (2; no AUC): **0.60**, 0.58, **0.91**, 0.60

**Heterogeneity:** across the 38 pooled estimates, I² ranged from 0.0% to 98.9%, with a median of 92.8%. Twenty-eight of 38 were at or above 75% ("considerable" by convention); 24 were at or above 90%.

**Risk of bias (the authors' own appraisal):** high overall risk in 4 of 15 studies (26.7%) for model development and **7 of 15 (46.7%) for model evaluation**; high applicability concerns in 2 of 15 (13.3%).

**Certainty of evidence (GRADE):** "generally moderate," downgraded mainly for inconsistency, and "substantially lower" for DN, LN, MPGN, FSGS and MsPGN, downgraded for inconsistency and imprecision. MN sensitivity was low-certainty.

**Publication bias:** Egger's test run only where there were at least 10 datasets. The only significant result was IgAN accuracy (p = 0.04). MN AUC was borderline (p = 0.06).

**Comparison with pathologists:** available in only **4 of the 15 studies** — one reporting junior pathologists, one reporting senior pathologists, two not specifying experience. Within that evidence, AI had higher accuracy than senior pathologists for MN (p < 0.001), IgAN (p = 0.04), LN (p < 0.001), MCD (p < 0.001) and MsPGN (p = 0.007), and higher than the overall pathologist group for MN (p < 0.001) and IgAN (p = 0.05), with a higher F1 for MN (p = 0.03).

**Funding and conflicts of interest: not stated in the text retrieved.**

## 3. How Strong Is This Evidence? (Grade 3/5)

Three out of five — and I want to be precise about what that grade is measuring, because it undersells the people who wrote this. The *conduct* of this review is close to 4/5 work. The *evidence it reviews* cannot support more than a 3. The authors largely say so.

**What is genuinely well done, and there is a lot of it.**

They reported 95% prediction intervals for every single pooled estimate. Almost nobody does this, and in a review with this much heterogeneity it is the difference between an honest summary and a misleading one (see the Statistics Spotlight). They used a random-effects model with the Hartung-Knapp-Sidik-Jonkman adjustment, which widens intervals appropriately when there are few studies — a careful, non-default choice.

They set a clinical-relevance threshold of 0.80 **in advance** and then colour-coded their summary figure by whether each confidence interval excludes it. That is pre-specification doing real work, rather than being mentioned and ignored.

They restricted leave-one-out analyses and Egger's test to outcomes with at least 10 datasets, and said why: below that, such analyses "would be unstable and difficult to interpret." They are right, and most reviews run them anyway on four studies.

They screened and extracted in duplicate and reported the agreement (kappa 0.87, 0.89, 0.91). They used PROBAST+AI and GRADE and reported the uncomfortable results of both — including that nearly half the included studies were at high risk of bias on model evaluation.

Most importantly, they declined to do three things they could have got away with. They did not fit a bivariate or HSROC model, and explained that the data would not support one. They did not impute specificity, and explained that imputing would need assumptions that "could introduce bias." And they did not claim AI beats pathologists, labelling that comparison "exploratory," "descriptive and hypothesis-generating," and "not head-to-head comparison." Each of those is a point of restraint where the incentive ran the other way.

They also state, unprompted, that their sample totals are "analysis units rather than unique patients," and give the four-way breakdown. Reviewers of AI studies routinely blur that line. These authors drew it in bold.

**What holds the evidence at 3/5.**

**There is no specificity in this paper.** For a review of diagnostic accuracy, that is the central gap. Sensitivity tells you how often the AI catches the disease. Precision tells you how often its positive calls are right. Neither tells you how often it correctly says "not this disease" — and in an eight-way differential, false positives are how a patient ends up on the wrong immunosuppressant. The authors cannot fix this; it is a failure of the fifteen original studies. But it means the phrase "high performance" in the abstract is based on half a picture.

**Accuracy and precision depend on how common each disease is, so pooling them across datasets with different disease mixes compares unlike things.** The authors note that the metrics are "complementary reported performance measures," but do not flag the prevalence dependence specifically — and accuracy turns out to be the *highest* of the four main metrics for **all eight diseases**, which is the signature of exactly this problem. For the rarer subtypes it produces numbers that are close to meaningless: pooled MsPGN accuracy of 0.96 against a do-nothing baseline of about 0.944 (worked through in the Statistics Spotlight).

**The heterogeneity is extreme enough to question whether pooling was the right move.** Median I² of 92.8%, with 24 of 38 estimates at or above 90%. At that level the studies are not estimating a common value, and a single pooled number invites a reader to think they are. The authors' own GRADE assessment downgrades for inconsistency, and their prediction intervals show the damage honestly. But the abstract still leads with the point estimates.

**A pooled AUC of 1.00 should have stopped the production line.** MCD's AUC is 1.00 with a confidence interval of 0.99 to 1.00 and I² of 0.0% — perfect discrimination, replicated identically across six datasets. Real diagnostic tests do not do this. It is the fingerprint of small curated datasets where the classes are easy to separate. It also sits oddly beside MCD's own reported sensitivity of 0.92: an AUC of 1.00 means some threshold existed that would have caught every case and raised no false alarms, and yet at the threshold actually used, 8% of cases were missed.

**The validation datasets are not independent of each other.** Fifteen studies produced roughly 26 validation datasets — MN alone appears in 22 of them. One study (Ma et al.) contributes six datasets on its own: an internal validation plus five external ones. The authors did guard against patient overlap, which is the right first step. But six datasets from one study still share one model and one training set, so they cannot tell you six independent things about how that model generalises. Pooling them as six units makes the evidence base look twice as broad as it is.

**The reference standard is not uniform.** The inclusion criteria say pathology confirmation; the study table records roughly half the entries as "expert consensus." In renal pathology those overlap, since the diagnosis *is* a pathologist's reading — but that is precisely the problem for an AI-versus-pathologist comparison. If the target is a consensus of expert readers, a model trained to reproduce expert readings is being scored against the thing it was built to imitate.

**All fifteen studies were retrospective.** There is no prospective evidence here at all, and the authors say future work needs it.

**Where 3/5 sits.** This is a well-built review of an evidence base that is not yet strong: retrospective studies, no specificity, severe inconsistency, non-independent datasets, and headline accuracy figures that are inflated by disease rarity. The authors' own conclusion — "current head-to-head evidence is insufficient to establish superiority over pathologists" — is the correct reading of their own data, and it is the sentence to quote.

## 4. The Editor's Concerns

**Move the senior-pathologist sentence out of the abstract, or qualify it there.** This is my main request. The abstract says "AI also showed higher accuracy than senior pathologists for IgAN, MN, and MCD; however, comparator evidence was sparse and should be interpreted cautiously." The caveat is present, and it is still not enough, because the full text reveals that senior-pathologist data came from **one study**. Three diseases, one study's senior readers, compared by Z-test against pooled AI estimates drawn from entirely different studies and different slides. The body text calls this exploratory three separate times and says outright it is "not head-to-head comparison." The abstract should say the number: "based on a single study reporting senior-pathologist performance."

**Report specificity even if you cannot pool it.** The decision not to pool was right. But a table listing which of the fifteen studies reported specificity, and what they found, would tell a reader far more than silence. As written, someone could read this review and not notice that the false-positive side of the ledger is absent.

**Stop pooling accuracy, or report the trivial baseline beside it.** Accuracy for a one-versus-rest classification of an uncommon disease is dominated by true negatives, and it is the highest of the four metrics for all eight diseases here — which is the tell. If accuracy stays, every accuracy row needs the prevalence and the "never diagnose it" baseline printed next to it. For MsPGN that would read: accuracy 0.96, baseline 0.944, sensitivity 0.61. No reader seeing those three numbers together would come away with the wrong impression.

**Interrogate the MCD AUC of 1.00.** An AUC of exactly 1.00 across six datasets with zero heterogeneity needs a paragraph, not a table cell. Which six datasets? How large? Were they internal validations on curated data? And how does a perfect AUC coexist with a sensitivity of 0.92 in the same disease? I would not let this through without an explanation.

**Give the number of studies alongside the number of datasets, everywhere.** The table reports "number of validation datasets" — 22 for MN, 14 for IgAN — with no indication that these come from fifteen studies and that one study supplied six of them. A reader sees k = 22 and thinks twenty-two independent replications. A second column, "number of contributing studies," would cost nothing and prevent a real misreading. Better still, a sensitivity analysis using one dataset per study would show how much the pooled estimates depend on multi-dataset contributors.

**Flag where metrics rest on different numbers of datasets.** Within a single disease the metrics are not drawn from the same evidence. MN sensitivity comes from 22 datasets, MN AUC from 10. MCD sensitivity from 11, MCD AUC from 6. FSGS and MPGN have no AUC at all. Reading across a row invites the assumption that these describe one coherent body of evidence, and they do not.

**Reconcile the reference standard with the inclusion criteria.** The criteria say pathology confirmation; the table says expert consensus for about half the studies. If those are the same thing in this field, say so explicitly. If not, the inclusion criteria were not applied as written.

**Check the registration number.** The paper gives PROSPERO CRD420261278316. PROSPERO identifiers follow the pattern CRD, then 4, then the four-digit year, then six digits — eleven digits in all, as in CRD42026123456. The number printed here has twelve, with a seven-digit final group. I could not verify the record with the tools available, so I am not saying the registration does not exist; I am saying the identifier as printed does not match the format, and a reader who wants to check the protocol — the single most useful thing a reader can do with a registered review — cannot. One digit, and it undoes the whole point of registering.

**Smaller notes.** The Z-test comparing pooled AI estimates against pooled pathologist estimates treats two groups from different studies as though they were two arms of one experiment; it should be labelled an indirect comparison in the results, not only in the discussion. The study table contains at least one stray full-width character ("EV：171"), suggesting the table was assembled by hand. And funding and competing interests do not appear in the text retrieved; both belong in the paper.

**One thing I would not change.** The 95% prediction intervals. They are the most useful column in the paper and they are the reason a careful reader can arrive at the right conclusion despite everything above.

## 5. Statistics Spotlight

### Concept 1: Why "96% accurate" can mean "misses two in five"

This paper contains the clearest demonstration of this trap I have seen in a published table, so it is worth working through slowly.

**What accuracy is.** Accuracy is the proportion of all decisions that were correct: (true positives + true negatives) / total.

**Why that breaks for an uncommon disease.** These models are doing one-versus-rest classification: for each slide and each disease, "is this MsPGN or not?" In this data, mesangial proliferative glomerular disease is about 5.6% of biopsies. I computed that from the validation sets the paper itself lists for the largest included study: 311/5,330, then 70/1,226, 48/875, 48/933, 51/962, 52/1,024 — pooling to 580/10,350 = 5.6%.

Now consider a model that is not a model at all. It looks at every slide and says "not MsPGN." Every single time.

That model gets 94.4% of slides right, because 94.4% of them genuinely are not MsPGN. Its accuracy is 0.944. It has never once been correct about the disease it is supposedly detecting.

The paper's pooled accuracy for MsPGN is **0.96**. That is **1.6 percentage points** above a model that does nothing at all. And the pooled sensitivity for MsPGN is **0.61** — meaning in reality these models miss about two in every five actual cases.

**The formula that makes this visible.** In one-versus-rest terms:

accuracy = prevalence × sensitivity + (1 − prevalence) × specificity

Plug in what we know for MsPGN — accuracy 0.96, prevalence 0.056, sensitivity 0.61 — and you can solve for the missing piece:

0.96 = (0.056 × 0.61) + (0.944 × specificity), so specificity ≈ 0.98

So the models are very good at ruling MsPGN out and distinctly poor at ruling it in, and because 94% of slides need ruling out, the accuracy figure reflects almost entirely the thing the models are good at.

**The tell, and it is right there in the table.** Accuracy is the highest of the four main metrics for **all eight diseases** in this review. MN: sensitivity 0.96, accuracy 0.96. LN: sensitivity 0.79, accuracy 0.97. DN: sensitivity 0.78, accuracy 0.96. MsPGN: sensitivity 0.61, accuracy 0.96. MPGN: sensitivity 0.60, accuracy 0.91. When one metric is systematically the most flattering across every single condition, it is measuring something structural about the data rather than something about the models.

**An everyday analogy.** A smoke alarm that never goes off is right on almost every day of your life. Across a year it is "99.7% accurate." It is also worthless, and you would notice the moment it mattered. Accuracy rewards it for all the quiet nights.

**Watch out.** Ask for the prevalence whenever you see an accuracy figure. Then compute 1 − prevalence, which is what you get for free by always guessing "no." If the reported accuracy is not comfortably above that, the number is telling you about the disease's rarity, not the model's skill. The quick version: **accuracy for a 5% disease starts at 95% before anyone does any work.** This is why sensitivity, specificity and precision exist, and why a review that pools accuracy across diseases of very different rarity is pooling apples with oranges.

### Concept 2: Confidence intervals versus prediction intervals

This distinction is new to this reading list, it is the most useful column in this paper, and it answers a question most readers of meta-analyses do not know they should ask.

**The confidence interval answers:** where is the *average* across these studies? If I could repeat this whole review with infinite data, what would the pooled value be?

**The prediction interval answers:** if someone runs *the next* study, what range should I expect their result to fall in?

Those are very different questions, and when studies disagree a lot, the answers are very far apart. The confidence interval shrinks as you add studies, because you pin down the average more precisely. The prediction interval does not shrink much, because it also has to carry the genuine spread *between* studies.

**Watch it happen in this paper.**

IgAN accuracy: pooled 0.94, confidence interval 0.92 to 0.97, prediction interval **0.82 to 1.00**. The confidence interval spans 5 percentage points; the prediction interval spans 18 — three and a half times wider. So "the average study gets about 94%" is well established, while "the next study might get 82%" is the honest expectation.

IgAN precision: confidence interval 0.84 to 0.95; prediction interval **0.62 to 1.00**.

Lupus nephritis precision: confidence interval 0.78 to 0.97; prediction interval **0.50 to 1.00**. The next dataset could produce precision anywhere from a coin flip to perfect.

MsPGN sensitivity: pooled 0.61, confidence interval 0.45 to 0.76, prediction interval **0.19 to 0.95**.

And the extreme case, MPGN precision: pooled 0.58, confidence interval **0.00 to 1.00**. With only two datasets and real disagreement, the review cannot rule out any value at all. Same for MPGN's F1 score. These are the most honest numbers in the paper, and they say: we do not know.

**A tiny worked intuition.** Suppose you measure the average height of adults in five towns and get 165, 168, 170, 185 and 190 cm. The average is about 176, and with five towns you can state that average fairly tightly. But if someone asks what the *sixth* town will average, "176 ± 2" would be absurd — the towns genuinely differ, and your answer has to span something like 160 to 195. The confidence interval describes your knowledge of the average. The prediction interval describes the world.

**The link to heterogeneity.** I² estimates what share of the observed variation is real difference between studies rather than chance. Here the median I² across 38 pooled estimates is 92.8%, and 24 of 38 are at or above 90%. Above roughly 75%, convention calls heterogeneity "considerable." Above 90%, a single pooled point estimate is standing in for a set of studies that plainly are not measuring the same quantity — different diseases prevalences, different microscopy, different units of analysis, different architectures.

**Watch out.** Most meta-analyses report only the confidence interval, and most readers take it as a forecast. It is not one. If a review reports high I² and *no* prediction interval, you are being shown a precise-looking average of things that disagree. Look for the prediction interval; when it is missing, treat the confidence interval as a statement about the past, not a guide to the next hospital. Also note what I² does *not* mean: it is not a measure of how good the test is, and a high I² does not mean the pooled estimate is biased — it means it is not transferable. The authors say exactly this in their methods, which is to their credit.

### Concept 3: Count the datasets, count the studies, and check they are not the same number twice

Two related habits, both of which this paper rewards.

**First: find the k attached to every number, and notice when it changes within a row.**

Reading across the MN row you get sensitivity 0.96, precision 0.94, accuracy 0.96, F1 0.95, AUC 0.98. It reads as one coherent description of one body of evidence. It is not. The sensitivity, precision, accuracy and F1 come from **22** validation datasets. The AUC comes from **10**.

MCD is starker: sensitivity, precision, accuracy and F1 from **11** datasets; AUC from **6**. And MCD's AUC is the eye-catching 1.00. So the paper's most striking single number rests on a little over half the datasets that produced its other MCD figures — a smaller, self-selected subset consisting of whichever studies happened to report an AUC. FSGS and MPGN have no AUC row at all.

This matters beyond bookkeeping. Studies that report AUC are a non-random sample: reporting an AUC requires having probability outputs and a full threshold sweep, which tends to go with more sophisticated, better-resourced, possibly more optimistic work. Comparing AUC across diseases here means comparing different mixtures of studies.

**Second: datasets are not studies, and in this review the gap is large.**

The table's column is "number of validation datasets." MN has 22. But there are only 15 studies in the whole review. The arithmetic forces the conclusion that several studies contributed multiple datasets — and the study table confirms it. The largest included study reports an internal validation plus five external validations: **six datasets from one study**, all built on one model trained on one dataset. Three other studies contribute three, three and two.

The authors did take care here: they say that where studies reported multiple validation sets with non-overlapping patients, each was treated as independent, and that where one study tested several algorithms on the same cohort they took only the main model, specifically "to mitigate unit-of-analysis errors arising from patient overlap." That is the right first move and better than most reviews manage.

But non-overlapping *patients* is not the same as independent *evidence*. Six external validations of one model tell you how that one model travels. They do not tell you six independent things about whether AI can classify glomerular disease, because they share a model, a training set, an architecture, a preprocessing pipeline and a research group. Treated as six units in a random-effects model, they get six units' worth of influence on the pooled estimate and six units' worth of weight in the heterogeneity calculation.

**And the third layer: what is a "unit"?** The review reports 39,536 validation units. Decomposed by the authors: 16,223 patient-based, 9,505 image-based, 9,988 glomerulus-based, 3,820 lesion-based — summing exactly. So **only 41% of those units are patients.** The rest are single images, single glomeruli, or single lesions. One patient's biopsy contains many glomeruli. An accuracy figure computed per glomerulus and one computed per patient are answers to different questions, and the clinical decision is made per patient.

The authors deserve real credit here: they put the analysis unit in the study table, they state the totals are not patients, and they entered unit of analysis as a covariate in their meta-regression. And it mattered — for IgAN, the unit of analysis was significantly associated with precision (p = 0.002), F1 (p = 0.001) and AUC (p = 0.02). They found that the unit changes the answer, and then still reported one pooled estimate across units.

**Watch out.** Whenever you see a big number in an AI paper — "39,536 samples," "80,000 images" — ask what one unit is and whether it is the unit the decision gets made in. And whenever a meta-analysis reports k, ask how many distinct studies and distinct models that k represents. A review of 15 studies that pools 26 datasets is not twice as strong as one that pools 13; it is the same evidence counted differently.

## 6. Jargon Translator

**Glomerular disease** — Disease of the glomeruli, the kidney's tiny filters. Causes protein or blood in the urine, swelling, high blood pressure, and can progress to kidney failure.

**Renal biopsy** — Taking a small core of kidney tissue to examine under a microscope. The reference standard for telling these diseases apart.

**The subtypes** — **IgAN** (IgA nephropathy): antibody deposits in the filters, the most common. **MN** (membranous nephropathy): thickening of the filter membrane. **MCD** (minimal change disease): looks nearly normal under a light microscope, the usual cause in children. **FSGS**: scarring in patches of some filters. **LN** (lupus nephritis): kidney involvement in lupus. **DN** (diabetic nephropathy): damage from long-standing diabetes. **MPGN** and **MsPGN**: two patterns of cell proliferation within the filter.

**Whole-slide imaging** — Scanning an entire microscope slide into one very large digital image.

**Systematic review** — Searching the literature by a prespecified method, so the selection of studies is reproducible rather than cherry-picked. **Meta-analysis** — statistically combining their results.

**PRISMA-DTA** — The reporting checklist for systematic reviews of diagnostic test accuracy.

**PROSPERO** — The public register where review protocols are deposited before the work starts, so readers can check the plan against what was done.

**PROBAST+AI** — A tool for judging risk of bias in prediction-model studies, with AI-specific items.

**GRADE** — A framework for rating how much confidence to place in a body of evidence, downgrading for risk of bias, inconsistency, indirectness, imprecision and publication bias.

**Sensitivity** — Of people who have the disease, the fraction the test catches. TP/(TP+FN).

**Specificity** — Of people who do not have it, the fraction the test correctly clears. **Not pooled anywhere in this paper.**

**Precision (positive predictive value)** — Of the cases the test calls positive, the fraction that really are. TP/(TP+FP). Depends on how common the disease is.

**Accuracy** — All correct calls divided by all calls. Dominated by true negatives when the disease is uncommon — the subject of the Statistics Spotlight.

**F1 score** — The harmonic mean of sensitivity and precision, a single number balancing the two. Harsher than a plain average: if either component is poor, F1 is poor.

**AUC (area under the ROC curve)** — The probability the model ranks a random true case above a random non-case, across all possible thresholds. 0.5 is a coin flip, 1.00 is perfect.

**2 × 2 table / contingency table** — The four counts (true positives, false positives, true negatives, false negatives) from which every accuracy measure can be derived. Most studies here did not report enough to reconstruct one.

**Bivariate or HSROC model** — The proper statistical machinery for meta-analysing diagnostic accuracy. It models sensitivity and specificity jointly, because they trade off against each other. Needs complete 2 × 2 data, which is why the authors could not use it.

**Random-effects model** — A meta-analysis that assumes the studies estimate genuinely different values and tries to describe the distribution, rather than assuming one shared truth. **REML** is a method of fitting it. **Hartung-Knapp-Sidik-Jonkman** is an adjustment that widens the interval appropriately when there are few studies.

**I² (I-squared)** — The share of the variation between studies that is real difference rather than chance. Above 75% is conventionally "considerable." **Tau²** is the estimated between-study variance.

**Confidence interval** — The plausible range for the *average* across studies.

**Prediction interval** — The plausible range for the result of the *next* study. Much wider when heterogeneity is high.

**Unit of analysis** — What one data point represents: a patient, an image, a single glomerulus, or a single lesion.

**Internal validation (IV)** — Testing on held-back data from the same source. **External validation (EV)** — testing on data from a different source.

**Meta-regression** — Testing whether study characteristics explain the differences between study results.

**Egger's test / funnel plot** — Checks for publication bias and small-study effects: whether small studies reporting unimpressive results seem to be missing.

**Leave-one-out sensitivity analysis** — Redoing the meta-analysis with each study dropped in turn, to see whether any single study is driving the result.

**Cohen's kappa** — Agreement between two reviewers, corrected for chance. Used here for the screening and extraction process, not for diagnostic accuracy.

**Z-test** — A test for whether two estimates differ. Used here to compare AI against pathologists, which is an indirect comparison because the two came from different studies.

**Indirect comparison** — Comparing arm A of one study with arm B of another. Weaker than comparing both within the same study on the same cases.

**Retrospective** — Using data already collected for other reasons. All 15 studies here were retrospective.

## 7. What You Can (and Can't) Say

**You CAN say:**
- "A 2026 review pooled 15 retrospective studies of AI reading kidney biopsies and found high pooled sensitivity for three subtypes — membranous nephropathy (0.96), IgA nephropathy (0.92) and minimal change disease (0.92)."
- "Performance was much weaker for the less common patterns: pooled sensitivity 0.61 for mesangial proliferative disease and 0.60 for membranoproliferative disease."
- "The studies disagreed enormously — the median I² across 38 pooled estimates was 92.8%."
- "The review reported prediction intervals, which show that the next study could plausibly find IgAN accuracy as low as 0.82, or lupus nephritis precision as low as 0.50."
- "Specificity could not be pooled because most of the original studies did not report enough data to calculate it."
- "Nearly half the included studies (7 of 15) were judged at high risk of bias for model evaluation."
- "All 15 studies were retrospective; there was no prospective evidence."
- "The authors conclude that current head-to-head evidence is insufficient to establish that AI outperforms pathologists."

**You CAN'T say:**
- ❌ "AI is 96% accurate at diagnosing kidney disease." For the rarer subtypes, that accuracy is barely above what you get by never diagnosing them at all — about 94.4% for mesangial proliferative disease — while missing two in five real cases.
- ❌ "AI outperforms senior pathologists." Senior-pathologist data came from **one** of the 15 studies, compared indirectly across different studies and different slides. The authors call this exploratory and explicitly "not head-to-head."
- ❌ "AI achieves perfect discrimination for minimal change disease." The AUC of 1.00 comes from 6 datasets, sits alongside a sensitivity of 0.92 in the same disease, and is far more likely to reflect small curated datasets than a perfect test.
- ❌ "This is based on nearly 40,000 patients." It is based on 39,536 **analysis units**, of which only 16,223 are patients; the rest are individual images, glomeruli or lesions. The authors say this themselves.
- ❌ "Fifteen studies independently confirm these results." Fifteen studies produced about 26 validation datasets, with one study contributing six of them. Membranous nephropathy's figure of "22 validation datasets" is not 22 independent replications.
- ❌ "AI rarely makes false positives." Specificity was never pooled. The review cannot say how often the AI calls a disease that is not there.
- ❌ "The evidence is strong." The authors' own GRADE assessment is "generally moderate," and "substantially lower" for five of the eight diseases.
- ❌ "This is ready to use in a pathology lab." Retrospective studies only, no prospective testing, severe heterogeneity, and the authors call for "prospective multicenter studies integrating multimodal clinical data and standardized external validation."

## 8. Bottom Line for Your Life

If you or someone close to you is having a kidney biopsy: the diagnosis still comes from a pathologist, and that is appropriate. The useful thing to know from this review is that the different glomerular diseases are genuinely hard to tell apart — hard enough that AI trained specifically on the task catches only about 60% of two of the less common patterns. If your result is one of the unusual ones, a second expert opinion is a reasonable thing to ask about. That is not a conclusion about AI; it is what the AI results reveal about the difficulty of the task.

If you work in nephropathology: the honest summary is that AI looks genuinely promising for the common, visually distinctive patterns — membranous nephropathy especially — and does not yet work for the rarer ones. The review's prediction intervals are the column to read, not the point estimates, and the absence of any pooled specificity means the false-positive burden is simply unknown. The authors' call for prospective, multicentre work with standardised external validation is exactly right.

For your paper-reading, take two things, and they are among the most portable in this whole reading list.

**First: whenever you see an accuracy figure, ask how common the disease is, and subtract.** A 5% disease hands you 95% accuracy for free, before anyone trains anything. This review contains the cleanest published example I have come across: pooled accuracy 0.96 for a disease where doing nothing scores 0.944, reported next to a sensitivity of 0.61. Both numbers are correct. Only one of them is informative. And the structural tell was visible without any arithmetic: accuracy was the most flattering metric for all eight diseases, which is the kind of perfect consistency that comes from how a number is built rather than from how good a model is.

**Second: in a meta-analysis, read the prediction interval and ignore the headline.** The confidence interval tells you where the average of past studies sits. The prediction interval tells you what the next hospital should expect. When studies disagree — and here the median I² was 92.8% — those are wildly different statements. IgAN accuracy: confidence interval 0.92 to 0.97, prediction interval 0.82 to 1.00. Same data, and only the second one is a forecast. Most reviews do not report prediction intervals at all; when one does, it is usually the most honest number on the page, and this paper's authors deserve credit for printing them for every single estimate.

A closing word on how to read a paper like this. Almost every criticism in this decode is one the authors made first, somewhere in their own text: that the units are not patients, that a proper diagnostic model could not be fitted, that specificity is missing, that the pathologist comparison is exploratory and not head-to-head, that nearly half the studies are at high risk of bias, that the certainty is moderate at best. The work is better than its own abstract. That gap — between a conscientious methods section and one quotable sentence at the top — is where most misleading citations are born. When a paper's conclusion is more cautious than its abstract, believe the conclusion.

---

*This is an educational analysis of a published scientific paper, not medical advice. Nothing here is guidance about your own kidney biopsy or treatment. Talk to your nephrologist about your results.*
