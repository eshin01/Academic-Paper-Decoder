# Highly accurate protein structure prediction with AlphaFold

- **Authors:** John Jumper, Richard Evans, Alexander Pritzel, … David Silver, Oriol Vinyals, Koray Kavukcuoglu, Pushmeet Kohli, Demis Hassabis (DeepMind, London; with Martin Steinegger, Seoul National University) — 34 authors
- **Venue:** Nature, 2021;596(7873):583–589 (published July 15, 2021)
- **DOI link:** https://doi.org/10.1038/s41586-021-03819-2
- **PubMed link:** https://pubmed.ncbi.nlm.nih.gov/34265844/ (PMID 34265844)
- **Full-text link:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8371605/ (PubMed Central, open access)
- **Basis:** FULL TEXT — main text, methods, training and inference details, metrics, and stated limitations retrieved from PubMed Central. Competing-interest and funding statements were not present in the retrieved manuscript text; PubMed tags non-US-government research support. Independent competition scores are taken from the **companion CASP14 paper** (Jumper et al., *Proteins* 2021;89(12):1711–1721, PMID 34599769, https://doi.org/10.1002/prot.26257), verified separately against the live PubMed record.
- **Decoded:** 2026-09-12

---

# The Gist

Proteins are molecular machines, and what a protein *does* depends on the shape it folds into. Working out that shape in a laboratory takes months to years per protein — which is why, after decades of effort, humans had solved about **100,000** structures out of **billions** of known protein sequences. Predicting shape from sequence alone had been an unsolved problem for over 50 years. DeepMind's AlphaFold solved it to a degree nobody expected: in a blind competition where the correct answers were physically unknown to everyone including the organisers, its predictions came within **0.96 ångströms** of the true structures — smaller than the width of a single carbon atom (1.4 Å). The next best method managed 2.8 Å. This is the most decisively validated result on your entire reading list, and the reason is the thing worth learning from it.

# Study Snapshot

- **Study type:** A computational method paper — but validated through a **blind, prospective, independently assessed competition**, which puts it in an evidence category nothing else on your list occupies.
- **The test — this is the crucial part:** CASP (Critical Assessment of protein Structure Prediction) runs every two years using proteins whose structures *have recently been solved experimentally but not yet deposited in public databases or disclosed*. Predictors submit answers before anyone outside the experimental team knows the truth. The paper calls it "a blind test for the participating methods, and has long served as the gold-standard assessment."
- **Headline accuracy (CASP14, May–July 2020):** median backbone accuracy **0.96 Å** (95% CI 0.85–1.16) versus **2.8 Å** (95% CI 2.7–4.0) for the next best method. All-atom accuracy **1.5 Å** (1.2–1.6) versus **3.5 Å** (3.1–4.2). The paper offers the reference point that "the width of a carbon atom is approximately 1.4 Å."
- **The margin, as scored by independent assessors:** in the companion CASP14 paper, AlphaFold scored **244.0** in the assessors' summed z-score ranking against **90.8** for the next best group, with a median domain score (GDT_TS) of **92.4** — "the first time that this level of average accuracy has been achieved during CASP."
- **A second, separate validation:** the method was also tested on **10,795 protein chains** deposited in the public database *after* its training data cut-off of 30 April 2018 — new structures it could not have memorised.
- **It knows when it is unsure:** the model outputs a per-residue confidence score (pLDDT) that the paper shows "reliably predicts" its own actual accuracy.
- **Openness:** the custom sequence database built for the work (BFD — 65,983,866 protein families covering 2.2 billion sequences) was released publicly and used by several competing CASP teams.
- **Cost:** about 0.6 GPU-minutes for a 256-residue protein; roughly 2.1 hours for a 2,500-residue one. Training took around one week on 128 TPU cores plus four days of fine-tuning.
- **Funding / conflicts:** not reported in the retrieved text; nearly all authors were DeepMind employees.

# How Strong Is This Evidence?

**Grade: 5/5 — for the claim it makes, this is about as conclusively demonstrated as a computational result can be.**

Two caveats before the praise. First, the grade applies to the paper's actual claim — *this method predicts protein structures accurately from sequence* — and to nothing beyond it. It is not a clinical study, no patient was involved, and it makes no medical claim. Second, "5/5" here means the evidence firmly supports what was claimed, which is a different achievement from clinical importance.

Why it earns the top grade, in the exact terms this reading list has been building: the evaluation was **blind** (answers unknown to predictors at submission), **prospective** (predictions made before truth was revealed), **independently assessed** (CASP assessors, not the developers), and **competitive** (dozens of rival methods on identical targets). The margin is so large — 244.0 against 90.8 — that no plausible analytical choice could account for it. It then added a second validation on 10,795 structures released after its training cut-off. It reports **calibrated uncertainty**, so users know which predictions to trust. And it released its custom database publicly, to competitors' benefit.

Compare that with the McKinney breast-screening paper, where nobody could reproduce anything, or the Epic sepsis model, deployed for years before anyone checked. AlphaFold's design let the world check it *before* it was believed.

# The Editor's Concerns

- **A prediction is not a measurement.** AlphaFold outputs a highly probable structure, not an experimentally determined one. The paper is careful: accuracy is "competitive with experimental structures in a majority of cases" — a majority, not all, and competitive, not equivalent.
- **The authors name two real failure modes, with numbers.** Accuracy "decreases substantially when the median alignment depth is less than around 30 sequences" — meaning proteins with few known evolutionary relatives, which includes many novel and engineered proteins. And it is "much weaker for proteins that have few intra-chain or homotypic contacts compared to the number of heterotypic contacts" — proteins whose shape is created mainly by partners in a larger complex.
- **It depends on decades of other people's work.** The model learned from the Protein Data Bank, built by experimentalists over 50 years, and from enormous sequence databases. Removing both metagenomic databases cost 6.1 GDT of accuracy. This is a triumph built on public scientific infrastructure, not a replacement for it.
- **Structure is not function, and certainly not a drug.** Knowing a shape is one input to understanding what a protein does, and a distant input to designing a medicine. The gap between "we know the shape" and "we have a treatment" is where most of drug development lives.
- **Single-chain focus.** The paper notes the difficulty with proteins in complexes and points to future work; most biology happens in complexes.
- **Not a medical study at all.** It belongs on this reading list as a contrast case, not as evidence about clinical AI.
- **What this study did well:** submitted to a blind competition it could lose; reported confidence intervals on its headline accuracy; validated a second time on post-cut-off structures; built a self-assessment measure and demonstrated that it works; quantified exactly where the method degrades; released a major database publicly; and gave an explicit physical reference point (the carbon atom) so readers could judge the numbers rather than take them on faith.

# Statistics Spotlight

**1. Blind prospective evaluation — the design every other paper on this list lacked.**
- *What it is:* Predictions are made and locked in *before* the truth is known, and someone other than the predictor decides who was right. CASP achieves this by using structures that experimentalists have solved but not yet released.
- *How this paper used it:* AlphaFold entered CASP14 in mid-2020 against dozens of competing groups on identical targets, and was scored by independent assessors. The 244.0-versus-90.8 margin is those assessors' number, not DeepMind's.
- *The theory, with an analogy:* This is the difference between predicting an election result beforehand and explaining it afterwards. Retrospective analysis always finds a story that fits; only a locked-in prediction can be wrong in public. Every AI-versus-doctor study you have read was retrospective — the algorithm met data whose answers already existed somewhere, and the developers usually ran the scoring themselves. Recall the cataract trial from the BMJ review: 98% retrospectively, 87% when finally tested prospectively. CASP forecloses that gap by construction.
- *Watch out:* "Blind" gets used loosely — sometimes meaning only that human readers didn't know which model produced an answer. The strong version is that *the correct answer did not exist in accessible form* when the prediction was made. When someone cites an impressive benchmark result, ask when the answers became available and who did the scoring. Nearly every benchmark in machine learning fails this test, because the test set is public.

**2. Effect size versus statistical significance — when the gap is too big to argue about.**
- *What it is:* Significance testing asks whether a difference could plausibly be chance. Effect size asks how *big* the difference is. With a large enough effect, the first question stops mattering.
- *How this paper used it:* 0.96 Å versus 2.8 Å is roughly a three-fold improvement, and 244.0 versus 90.8 in summed z-scores is a rout. The paper spends no effort arguing significance, because none is needed. A **z-score** here simply expresses how far above the average competitor's performance a result sits, in units of the spread among competitors — summed across targets, it measures consistency of dominance, not one lucky prediction.
- *The theory, with a worked example:* If two runners finish a marathon 3 seconds apart, you argue about wind, timing chips, and whether the difference is real. If one finishes an hour ahead, nobody computes a p-value. Contrast this with the Liu meta-analysis: 87.0% versus 86.4% sensitivity, with confidence intervals overlapping almost entirely — a gap so small that the only honest conclusion was "we cannot tell these apart."
- *Watch out:* The inverse is the trap you meet far more often. A "statistically significant" result in a huge dataset can be minuscule and meaningless — remember the Rajkomar authors refusing a calibration test because at 200,000 records it flags trivial differences. Always ask for the effect size in units you can picture. This paper's carbon-atom comparison is a model of how to do that.

**3. Calibrated self-assessment — a model that knows what it does not know.**
- *What it is:* Beyond producing an answer, the system outputs a confidence score, and that score is *verified* to track its real accuracy. Here that measure is pLDDT, reported per residue.
- *How this paper used it:* The authors show pLDDT "reliably predicts" the model's actual measured accuracy for the corresponding prediction. In practice, a biologist can see which parts of a predicted structure to trust and which to treat as guesswork.
- *The theory, with an analogy:* Think of two weather forecasters. One always says "it will rain" with total conviction; the other says "70% chance," and it rains on about 70 of those days. The second is useful precisely because their uncertainty is honest. This is the **calibration** report card from your statistical mental map, and it is the direct opposite of yesterday's adversarial example, where a model announced **100% confidence** on a deliberately corrupted image. Confidence that tracks reality is a feature; confidence that does not is a hazard.
- *Watch out:* Most deployed models emit a confidence number and almost none demonstrate it is calibrated — the Epic sepsis model's calibration was "poor at all time horizons," and nobody outside the vendor had checked. When any system shows you a certainty score, the question is not how high it is but whether anyone has verified that its 90% means 90%.

# Jargon Translator

- **Protein:** a molecular machine built from a chain of amino acids; nearly every biological process depends on them.
- **Protein folding:** the process by which that chain curls into a specific 3D shape, which determines what the protein can do.
- **Amino acid sequence:** the order of building blocks in the chain — the "input" here, readable cheaply from DNA.
- **Protein Data Bank (PDB):** the public archive of experimentally determined protein structures, built over decades.
- **CASP:** the biennial blind competition that has assessed structure-prediction methods since 1994.
- **Ångström (Å):** one ten-billionth of a metre. A carbon atom is about 1.4 Å across, which is why 0.96 Å accuracy is remarkable.
- **r.m.s.d. (root-mean-square deviation):** the average distance between predicted and true atom positions — lower is better.
- **GDT_TS:** CASP's percentage-style score for how much of a predicted structure sits close to the truth; 92.4 is very high.
- **z-score:** how far a result sits above the average, measured in units of the spread among competitors.
- **Multiple sequence alignment (MSA):** a stack of related proteins from other species, lined up; evolutionary patterns within it hint at which parts touch in 3D.
- **pLDDT:** AlphaFold's own per-residue confidence estimate, shown to track its real accuracy.
- **Homologue:** a related protein, often from another species, with a similar sequence.

# What You Can (and Can't) Say

**Fair to say:**
- "In the blind CASP14 competition, AlphaFold predicted protein structures with a median backbone accuracy of 0.96 Å — finer than the width of a carbon atom — against 2.8 Å for the next best method."
- "Independent CASP assessors scored it 244.0 against 90.8 for the next best group, the first time that level of accuracy had been reached in the competition's history."
- "It was validated again on 10,795 structures released after its training cut-off, and it reports a confidence score shown to track its actual accuracy."
- "The authors state it weakens when fewer than about 30 related sequences are available, and for proteins shaped mainly by partners in a complex."

**Not fair to say:**
- "AlphaFold solved protein folding" — it solved *structure prediction from sequence* to high accuracy in most cases, which is one component of the folding problem; it does not simulate how folding physically happens.
- "AlphaFold predictions are as good as experiments" — the paper says "competitive with experimental structures in a majority of cases," which is a careful and narrower claim.
- "This means new drugs" — structure is an early input to drug discovery, separated from a medicine by years of chemistry, biology, and clinical trials.
- "This proves AI works in medicine" — it is not a medical study; no patient, diagnosis, or treatment was involved.

# Bottom Line for Your Life

This entry is on your list as a contrast, and the contrast is the lesson. Fourteen papers in, you have seen retrospective studies graded against their own developers' scoring, a tool deployed in hundreds of hospitals that nobody checked for years, and a landmark result nobody could reproduce. Then this: a method that entered a competition it could lose, against rivals working on identical problems, where the right answers were locked in a laboratory drawer and strangers did the grading — and won by a margin nobody could dispute. **The strength of a scientific claim comes from the structure of its test, not the prestige of its venue or the size of its number.** All four of these papers appeared in Nature or Science. Ask yourself what the finding would have to survive to be wrong in public; AlphaFold's design made that survivable test possible. Nothing here changes anything about your health today — no patients, no treatments, no clinical use. One study is one data point, but the *kind* of data point this one is happens to be the best kind. This is an educational breakdown, not medical advice.

---

**Sources** (based on articles retrieved from PubMed / PubMed Central; identifiers verified against the live NLM record — URL browsing is blocked in this environment, so links are constructed from those verified records):
- DOI: https://doi.org/10.1038/s41586-021-03819-2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/34265844/
- Full text (PMC, open access): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8371605/
- Companion CASP14 assessment paper, verified: Jumper et al. "Applying and improving AlphaFold at CASP14." *Proteins* 2021;89(12):1711–1721. https://doi.org/10.1002/prot.26257 (PMID 34599769)
