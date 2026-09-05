# End-to-end lung cancer screening with three-dimensional deep learning on low-dose chest computed tomography

- **Authors:** Diego Ardila, Atilla P. Kiraly, Sujeeth Bharadwaj, Bokyung Choi, Joshua J. Reicher (Stanford / Palo Alto VA), Lily Peng, Daniel Tse, Mozziyar Etemadi (Northwestern), Wenxing Ye, Greg Corrado, David P. Naidich (NYU Langone), Shravya Shetty — nine of twelve at Google AI
- **Venue:** Nature Medicine, 2019;25(6):954–961 (published May 20, 2019). **Author Correction** published August 2019, Nat Med 25(8):1319 (https://doi.org/10.1038/s41591-019-0536-x)
- **DOI link:** https://doi.org/10.1038/s41591-019-0447-x
- **PubMed link:** https://pubmed.ncbi.nlm.nih.gov/31110349/ (PMID 31110349)
- **Full-text link:** none — closed access, no PubMed Central version, publisher unreachable from this environment, and the full-text service returned access denied. No link is given rather than an unverified one.
- **Basis:** ABSTRACT ONLY, supplemented by verified editorial notices and two expert commentaries (attributed inline). Details absent from the abstract — cohort demographics, the reader-study protocol, funding amounts, conflict-of-interest statements, and what the Author Correction changed — are marked "not reported in the text retrieved." Identifiers and editorial notices verified against the live PubMed/NLM record and Scite.
- **Decoded:** 2026-09-05

---

# The Gist

Lung cancer kills more Americans than any other cancer — about 160,000 deaths in 2018. Scanning heavy smokers yearly with a low-dose CT (a fast X-ray scan that builds a 3D picture of the lungs) catches cancers early enough to cut deaths by 20–43%, but the scans are hard to read: radiologists disagree with each other, and both false alarms and missed cancers are common. Google researchers built an AI that reads the whole 3D scan at once — and, when it exists, the patient's scan from the previous year — to estimate cancer risk. On 6,716 archived screening cases it scored very well, and in a head-to-head against six radiologists it **beat all six when no prior scan was available**. When the prior scan *was* available, it merely matched them.

# Study Snapshot

- **Study type:** Retrospective diagnostic-accuracy study on stored scans, with two "reader studies" pitting the model against radiologists on the same cases. No patient was screened, treated, or followed because of the AI. Low on the evidence ladder for clinical benefit: it measures scan-reading accuracy, not whether anyone lives longer.
- **Main dataset (n):** 6,716 cases from the National Lung Cancer Screening Trial (NLST), the large US trial that established CT screening works.
- **Independent validation (n):** 1,139 cases from a separate clinical set, on which the model "performs similarly" — the abstract gives no separate figure for it.
- **Headline accuracy:** 94.4% area under the curve on the NLST cases.
- **The human comparison:** six radiologists. Without a prior CT to compare against, the model beat every one of them, with **absolute reductions of 11% in false positives and 5% in false negatives**. With a prior CT available, performance was "on-par" with the same six.
- **What was predicted:** the patient's risk of lung cancer, from the raw 3D scan volume end-to-end — no human-designed nodule measurements in between.
- **Funding / conflicts:** PubMed tags NIH extramural and non-US-government research support; a conflict-of-interest statement is not reported in the text retrieved. Nine of the twelve authors were Google AI employees.
- **Post-publication record:** an Author Correction (August 2019) and at least two published commentaries, including one in Nature Reviews Clinical Oncology titled, pointedly, "Google's lung cancer AI: a promising tool that needs further validation" (Jacobs & van Ginneken, 2019; https://doi.org/10.1038/s41571-019-0248-7).

# How Strong Is This Evidence?

**Grade: 3/5 — a well-built accuracy study on a genuinely important screening problem, with a headline drawn from its most flattering comparison.**

The design does several things right that its peers often skip: it used data from a landmark randomized trial where cancer outcomes are actually known, it tested on a second, independent clinical dataset, and it ran not one but two reader studies so the machine and the humans faced identical cases. Predicting risk from the full 3D volume rather than from hand-measured nodules was a real technical step.

What holds it at 3: nobody's care changed, so there is no evidence about outcomes; the human comparison rests on just six radiologists; the developer designed, ran, and graded the contest; and — most importantly — the "outperformed all six radiologists" claim comes specifically from the condition where the radiologists were denied a prior scan. That is the harder condition for humans, and it is not how established screening programs usually work after the first round. In the more realistic condition, the model tied.

# The Editor's Concerns

- **The headline is the harder-for-humans condition.** Read the two results together: without priors, the model won; with priors, it tied. Real screening programs accumulate priors — comparing this year's scan to last year's is exactly how radiologists tell a stable old scar from a growing tumor. The "beats radiologists" framing describes the scenario that flatters the model, which in practice is mostly the first screening round only.
- **Six radiologists is a small human sample.** Each additional reader would move the "average radiologist" benchmark. With six, a couple of below-average readers can carry the comparison, and no confidence interval around "the radiologists" is reported in the text retrieved.
- **No patient outcomes.** This measures agreement with known cancer status on archived scans. Whether AI-assisted screening finds cancers earlier, saves lives, or simply generates more biopsies is untested here.
- **Independent validation is asserted, not quantified in the abstract.** "Performs similarly" on 1,139 cases is reassuring, but without the actual number a reader cannot judge how much performance dropped outside NLST — and some drop is near-universal when models leave their home dataset.
- **Screening data is not general-population data.** NLST enrolled a specific high-risk group (heavy smokers in a defined age band). Cancer is far more common there than in the general public, so accuracy figures from this population will not transfer to broader screening — the prevalence trap that recurs across your reading list.
- **The developer graded its own work.** Google built the model, designed the reader studies, and evaluated the results. The domain experts on the author list are a mitigating strength, but the structure is the same one as the Gulshan, Esteva, and Rajkomar papers on your list.
- **Independent experts publicly called for more validation.** The Nature Reviews Clinical Oncology commentary by Jacobs and van Ginneken — two academic authorities in lung-CT computer-aided detection — is titled "Google's lung cancer AI: a promising tool that needs further validation." When specialists write that as a title, it is a signal.
- **An Author Correction was published three months later.** What it changed is not reported in the text retrieved; anyone citing the paper should read the corrected version.
- **What this study did well:** used a randomized-trial dataset where cancer status is genuinely known rather than inferred; tested on a second independent clinical dataset; ran matched reader studies rather than comparing against published benchmarks; separated the with-priors and without-priors conditions and reported *both* rather than only the favorable one; reported the human comparison in absolute percentage terms; and framed the contribution as an opportunity to "optimize the screening process via computer assistance," not to replace radiologists.

# Statistics Spotlight

**1. Absolute versus relative differences — and why this paper's honesty here is worth noticing.**
- *What it is:* A difference between two groups can be stated as an absolute change ("11 fewer false alarms per 100 scans") or a relative one ("a 40% reduction in false alarms"). The same underlying result can be made to sound modest or dramatic depending on which you choose.
- *How this paper used it:* It reports **absolute** reductions — 11% in false positives, 5% in false negatives. That is the harder, more honest framing. If the radiologists' baseline false-positive rate were, say, 25%, then dropping it by 11 points is also a "44% relative reduction" — a number that would have made a much louder press release.
- *The theory, with a worked example:* A treatment that cuts your risk of a disease from 2 in 1,000 to 1 in 1,000 is a **50% relative** reduction and a **0.1% absolute** reduction. Both are true. Only the second tells you that 999 of every 1,000 people get no benefit. Relative numbers describe the *ratio*; absolute numbers describe *how many actual people are affected*, which is what anyone deciding about their own health needs.
- *Watch out:* Headlines and abstracts overwhelmingly favor relative numbers because they are bigger. Whenever you see a percentage improvement, ask "percent of what baseline?" If the baseline isn't given, the number is unreadable. This paper gave you absolutes — treat that as a mark of good faith and hold other papers to it.

**2. The conditional comparison — how the choice of scenario decides who wins.**
- *What it is:* When a study reports results under more than one condition, which condition becomes the headline is an editorial decision, not a statistical one. The comparison is only as meaningful as the scenario it was run in.
- *How this paper used it:* Two scenarios were tested. **Without** a prior CT: the model beat all six radiologists. **With** a prior CT: on-par with the same six. Both are reported honestly in the abstract — but the first is the one that travels into headlines, and it is the scenario in which the human experts were deprived of a tool they normally rely on.
- *The theory, with an analogy:* Imagine testing a spell-checker against copy editors, but taking away the editors' ability to see the previous draft. The spell-checker wins on the isolated page. Give the editors the earlier draft — where they can see what changed — and the contest evens out. Nothing was faked; the scenario simply decided the winner.
- *Watch out:* When a paper reports a model beating humans under some conditions and tying under others, ask which condition resembles real practice. Ask, too, whether the humans had access to everything they would normally have — including, as you saw in the sepsis paper, information available at the right *time*. A fair contest gives both sides their usual tools.

**3. Reader studies — the standard design for human-versus-AI in imaging, and its weak spot.**
- *What it is:* A reader study has human experts and the algorithm interpret the *same* set of cases, so the comparison is matched case-by-case rather than against numbers from some other paper. It is the right design for this question.
- *How this paper used it:* Six radiologists read the same cases the model did, under both the with-prior and without-prior conditions — hence a genuinely matched comparison.
- *The theory, with an analogy:* This is the difference between two athletes racing side by side and comparing their personal-best times recorded on different tracks in different weather. Matched designs remove the "different track" problem entirely, which is why reader studies are the accepted standard in radiology AI.
- *Watch out:* The cases are matched, but the *readers* are a sample too — and six is a small one. Radiologist skill varies enormously, so "the average of six" is an unstable benchmark; a different six could shift the result. Ask how many readers, how they were recruited, how experienced they were, and whether the spread across readers was reported. Also ask whether readers worked under realistic conditions — reading in a quiet study setting, knowing they are being measured, is not the same as reading a full clinical list at the end of a shift.

# Jargon Translator

- **Low-dose CT (LDCT):** a fast computed-tomography scan using a reduced radiation dose, used to screen high-risk people for lung cancer.
- **Screening:** testing people who feel fine, to catch disease early — a different task from diagnosing someone with symptoms, and judged by different standards.
- **NLST (National Lung Screening Trial):** the large randomized US trial that showed CT screening reduces lung cancer deaths; its archived scans and known outcomes make it a gold-standard training and testing resource.
- **CT volume:** the full 3D stack of image slices from a scan, as opposed to a single 2D picture.
- **End-to-end:** the model goes straight from raw scan to risk estimate, with no human-designed intermediate measurements.
- **Prior CT:** the same patient's scan from a previous year, used for comparison — the single most useful thing a radiologist has for telling a growing tumor from a stable benign spot.
- **False positive:** a scan flagged as suspicious that turns out not to be cancer — leading to more scans, anxiety, sometimes a biopsy.
- **False negative:** a cancer that the read misses.
- **Inter-grader variability:** the extent to which two qualified readers looking at the same scan reach different conclusions.
- **Author Correction:** a formal, published fix to something in the original paper, issued by the authors.

# What You Can (and Can't) Say

**Fair to say:**
- "A 2019 Google study built a deep-learning model that reads whole 3D lung CT scans and scored 94.4% AUC on 6,716 cases from the National Lung Screening Trial."
- "In a matched reader study, it beat all six radiologists when no prior scan was available — 11% fewer false positives and 5% fewer false negatives in absolute terms — and matched them when a prior scan was available."
- "It is one of the strongest imaging-AI accuracy papers of its era, and independent experts called for further validation before clinical use."

**Not fair to say:**
- "AI is better than radiologists at finding lung cancer" — only in the scenario where radiologists were denied the prior scan they normally use; with priors, it tied.
- "The AI is 94.4% accurate" — that is an AUC, a ranking score, not the share of patients it gets right.
- "This proves AI screening saves lives" — no patients were screened by it and no outcomes were measured; screening benefit was established by the NLST trial, not by this model.
- "It works for anyone worried about lung cancer" — it was developed and tested in a high-risk screening population, where cancer is far more common than in the general public.

# Bottom Line for Your Life

This is one of the better AI-versus-radiologist papers, and it is worth knowing why: the researchers used a dataset where the right answers are genuinely known, tested on a second independent set, and ran a properly matched contest — then reported *both* the scenario they won and the scenario they tied, in absolute percentages. That is more honest than most. What the study does not show is that anyone lives longer, because nobody was screened by it. The transferable lesson is the sharpest one on your list so far: when a model beats experts under one condition and ties under another, look hard at which condition matches real life, and whether the humans were given the tools they normally work with. If you or someone you know is a long-term smoker, the case for annual low-dose CT screening rests on the NLST trial, not on this paper — that is a conversation for a clinician. One study is one data point. This is an educational breakdown, not medical advice.

---

**Sources** (identifiers and editorial notices verified against the live PubMed/NLM record and Scite; URL browsing is blocked in this environment, so links are constructed from those verified records):
- DOI (closed access): https://doi.org/10.1038/s41591-019-0447-x
- PubMed: https://pubmed.ncbi.nlm.nih.gov/31110349/
- Full text: not obtainable — closed access, no PMC version, publisher unreachable, full-text service access-denied
- Author Correction (August 2019): https://doi.org/10.1038/s41591-019-0536-x
- Commentary, verified: Jacobs & van Ginneken. "Google's lung cancer AI: a promising tool that needs further validation." Nature Reviews Clinical Oncology 2019;16(9):532–533. https://doi.org/10.1038/s41571-019-0248-7
