# Association of AI-derived abdominal organ volumetry with postoperative outcomes in clear cell renal cell carcinoma: a multicentre study

- **Authors:** Jie Lou, Yi Ren, Bingxin Gong, Yusheng Guo, Dingyang Lv, Shuai Shan, Qiang Lu, Aoxin Sun, Jijun Wu, Yuhang Chen, Xin Yao, Lian Yang (Union Hospital, Tongji Medical College, Huazhong University of Science and Technology, Wuhan; with Shanxi Medical University, Nanjing Medical University, and Tianjin Medical University Cancer Institute) — 12 authors
- **Venue:** Annals of Medicine, 2026;58(1):2730502 (published September 10, 2026)
- **DOI link:** https://doi.org/10.1080/07853890.2026.2730502
- **PubMed link:** https://pubmed.ncbi.nlm.nih.gov/42723375/ (PMID 42723375)
- **Full-text link used:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC13573536/ (PubMed Central, open access)
- **Basis:** FULL TEXT — introduction, complete Methods, all results, the full hazard-ratio table with both raw and corrected P values, discussion, stated limitations, and the ethics statement were read from the open-access PubMed Central copy. Figures and Supplementary Material were not retrieved, so anything appearing only there is marked as not retrieved rather than guessed. Ethics: approved by the ethics committees of all four participating hospitals (Wuhan Union No. 2024-0361-01, Tianjin No. bc20251107, Shanxi No. KYLL-2025-068, Jiangsu No. 2022-SR-408), with written consent waived given the retrospective, anonymised design. Funding and competing-interest statements were not present in the retrieved text; PubMed tags the work as non-US-government research support. Identifiers verified against the live PubMed/NLM record; direct URL browsing is blocked in this environment, so links are constructed from that verified record.
- **Decoded:** 2026-09-17
- **Note on selection:** chosen from the past week's literature because the reading list's queue is exhausted apart from four entries whose full text cannot be reached here. Details at the end.

---

# The Gist

Everybody with a kidney tumour gets a CT scan before surgery. That scan happens to contain the patient's whole abdomen, and almost all of it gets ignored — the radiologist looks at the tumour and moves on. This team pointed an automatic measuring tool at the rest of the picture. It outlined and measured five organs in 1,720 kidney cancer patients across four Chinese hospitals, plus 3,052 healthy people for comparison, and then asked a simple question: does the size of your liver, spleen, pancreas, or adrenal glands have anything to do with how long you live after the operation? The answer was a qualified yes for two of them. A bigger liver and a bigger right adrenal gland were each linked to worse survival. The answer was a clear no for everything else, including whether the cancer came back — and the reason that "no" is worth reading is that some of those findings looked significant until the authors corrected for how many things they had tested. Watching that correction happen is the most useful thing in this paper.

# Study Snapshot

- **Study type:** Retrospective observational cohort study across four hospitals. Nobody was treated differently, nothing was predicted in advance, and no tool was deployed. This is an association study, and the authors describe it as one.
- **The AI's job is narrow and worth being clear about.** The deep learning does the *measuring*, not the predicting. It outlines organs on a scan so their volumes can be computed. Every claim in the paper then comes from ordinary medical statistics applied to those measurements. This is a different shape from every other entry on this list, where the model itself was the thing being tested.
- **Patients:** 1,720 people with confirmed clear cell renal cell carcinoma who had part or all of a kidney removed — 541 in Wuhan, 870 in Tianjin, 197 in Shanxi, 112 in Jiangsu. Median age 56 to 58 depending on the site; roughly two-thirds male at every site.
- **Comparison group:** 3,052 healthy adults having routine health checks at the Wuhan hospital.
- **Follow-up and events:** median follow-up 51.6 months. **165 patients had a recurrence and 95 died** — about 9.6% and 5.5% of the 1,720. Those two counts do a great deal of work in what follows.
- **How the organs were measured:** an automated segmentation model built on a widely used architecture, run on the pre-surgery contrast CT. It measured five solid organs: liver, spleen, pancreas, and the left and right adrenal glands. Hollow organs like the stomach and gallbladder were left out because their size depends on how full they are, and the kidneys were left out because the tumour distorts them.
- **The measuring was checked against a human.** Twenty patients from each hospital were outlined by hand by an experienced radiologist who did not know the patients' outcomes. Agreement scores ran from 0.848 to 0.966 on one standard measure and 0.938 to 0.987 on another — good to excellent.
- **Sizes were adjusted for body size** by dividing each volume by body surface area, since bigger people have bigger organs.
- **Patients versus healthy people:** after matching on age and sex, the cancer patients had larger spleens and larger adrenal glands on both sides, and smaller pancreases. Liver size did not differ.
- **The survival findings that survived everything.** Adjusted for age, sex, tumour size, side, surgical approach, tumour stage, node stage, grade, and tumour necrosis: liver volume (hazard ratio 1.42), liver volume index (1.31), right adrenal volume (1.34), and right adrenal volume index (1.29) were each linked to worse overall survival, all with corrected P values of 0.035. Each hazard ratio is per one standard deviation of increase.
- **The findings that did not survive.** No organ measurement was linked to cancer recurrence once the authors corrected for multiple testing. Spleen size was unrelated to anything. Pancreas volume index looked related to survival at first (raw P = 0.033) and was not (corrected P = 0.110), then vanished entirely once clinical factors were accounted for (P = 0.385).
- **A striking asymmetry:** the right adrenal gland was linked to survival and the left was not, even though the two glands' volumes correlate strongly with each other at 0.756. The authors say the biological basis for this is unclear.
- **What else they checked:** whether the effect differed by hospital (it did not), whether the relationships were curved rather than straight (they were not), whether dying before recurrence distorted the recurrence analysis (a competing-risk model gave the same answer), and whether adding adrenal volume to two established clinical risk scores improved them (it improved two reclassification measures, and improved a third measure against one score but not the other).
- **Funding / conflicts:** not present in the retrieved text.

# How Strong Is This Evidence?

**Grade: 3/5 — careful, well-disciplined statistics on a genuinely interesting question, reporting a modest association that has not been tested anywhere outside the four hospitals that produced it.**

Take the statistical conduct first, because it is the best part. The authors ran twenty tests in a single table and corrected for it, then published which of their own findings failed the correction. They checked whether the effect held up hospital by hospital. They ran a competing-risk analysis so that patients who died before recurring could not distort the recurrence result. They tested whether the relationships were curved. They validated the automatic measuring against a blinded radiologist and reported the agreement scores. They ran a sensitivity analysis using raw volumes with body size as a separate variable rather than dividing. And their limitations section names the weaknesses a critical reader would name, including one — data-driven cut-off points — that most papers quietly leave out.

What holds the grade at 3 is everything the design cannot fix. It is retrospective, so the associations could reflect factors nobody measured. There is no external validation set: all four hospitals contributed to the analysis, and none was held back to test the finding. **95 deaths is not many** for a model that adjusts for nine other variables, which puts the analysis right at the edge of a long-standing rule of thumb about how many events you need per variable. And the central claim is an association with no mechanism, no intervention, and no evident action — knowing that a patient's liver is a standard deviation larger does not currently tell anyone to do anything differently.

The right-versus-left adrenal result deserves particular scepticism, and gets it below.

# The Editor's Concerns

- **The left adrenal gland is the tell.** The two adrenal volumes correlate at 0.756, which is strong. Yet the right gland came in at a corrected P of 0.035 and the left at 0.243. When two measurements that move together that closely land on opposite sides of a significance line, the most economical explanation is that one of them got lucky, not that the right adrenal gland is biologically special. The authors report the asymmetry honestly and say they cannot explain it. A reader should treat the adrenal finding as one result awaiting replication, not two.
- **95 deaths, nine adjustment variables.** A widely used rule of thumb says you want at least ten outcome events for each variable in a survival model. Here there are 95 deaths and nine covariates plus the organ measure — right at the line. Models at that boundary can produce hazard ratios that are unstable and somewhat inflated. It does not invalidate the finding; it does mean the exact numbers should not be treated as precise.
- **No external validation.** All four hospitals fed the analysis. Nothing was held back, and no independent cohort has tested the result. The authors say so and call for it.
- **Large chunks of data are simply missing.** At the Tianjin site, 501 of 870 patients — 57.6% — have no record of hypertension, diabetes, or smoking status. Those variables are not in the adjustment model at all. Neither are comorbidities, kidney function, or liver disease, because they were not consistently available. For a study arguing that organ size reflects systemic health, the absence of the most obvious markers of systemic health is a real gap.
- **The survival curves use cut-offs found in the same data.** To draw the high-versus-low survival curves, the authors let an algorithm pick the dividing line that best separated the groups, using the same patients the curves then describe. That reliably makes the gap look bigger than it would be in new data. The authors flag this themselves and say the threshold findings need independent validation. Believe them and read the curves as illustration, not measurement.
- **The comparison with healthy people gets shakier under scrutiny.** Pooling all four hospitals, cancer patients had smaller pancreases at P below 0.001. Repeating the comparison within the Wuhan hospital alone, where the healthy controls actually came from, the pancreas difference disappeared. The spleen and adrenal differences held. That within-site check was the right thing to run, and it changed the answer for one of the four organs.
- **Organ size is affected by things nobody recorded.** Hydration, medications, alcohol, fatty liver, diabetes. The authors list these. Any of them could explain a liver-size association more simply than cancer biology.
- **All four hospitals are in China,** so the generalisability to other populations is untested. Stated by the authors.
- **The mechanism is frankly speculative, and labelled as such.** The paper offers plausible stories about immune cells accumulating in the spleen and chronic stress hormones enlarging the adrenal glands, and each time says the hypothesis "remains speculative."
- **What this study did well:** corrected for multiple testing and reported the findings that died in the process; validated the automated measurement against a blinded human reader with three separate agreement statistics; ran a competing-risk model so that death could not masquerade as freedom from recurrence; checked for effect differences across hospitals and found none; tested for curved relationships rather than assuming straight lines; ran the healthy-control comparison a second time within a single hospital to check for site effects, and reported that it changed one result; assessed whether the new measure adds anything to the risk scores clinicians already use; and wrote a limitations section that names its own weakest link.

# Statistics Spotlight

**1. Multiple-testing correction — watching four findings die in real time.**
- *What it is:* If you run one test and use the usual cutoff of P below 0.05, you accept roughly a 1-in-20 chance of calling a fluke real. Run twenty tests on data with nothing in it, and on average one comes back "significant" anyway. Correction methods adjust the P values upward to account for how many questions you asked. This paper used the Benjamini-Hochberg method, which controls the *false discovery rate* — the share of your declared findings that are wrong.
- *How this paper used it:* They measured five organs two ways each, giving ten measurements, tested against two outcomes, and corrected across them. The table shows both numbers side by side. Pancreas volume index came in at a raw P of 0.033 and a corrected P of 0.110. Liver volume: raw 0.045, corrected 0.110. For recurrence, liver volume was raw P = 0.023 and liver index raw P = 0.039, and the paper states flatly that "no organ volume measure remained significantly associated with RFS after FDR correction."
- *The theory, with a worked example:* Imagine testing twenty coins for fairness by flipping each five times. A fair coin lands all heads about 1 time in 32. Flip twenty of them and you will fairly often see one do it. Pointing at that coin and announcing you have found a biased coin is exactly the error correction prevents. Bonferroni, the strictest method, would simply divide your threshold by twenty, demanding P below 0.0025 — very safe, and it throws away real findings. Benjamini-Hochberg is gentler: it ranks all twenty P values and asks how many can be believed while keeping the expected share of false discoveries among them under 5%. That is why a raw 0.033 can become 0.110 here rather than 0.66.
- *Watch out:* Most papers reporting many comparisons do not correct at all, and a raw P of 0.033 buried in a table of twenty is nearly meaningless. Two questions will serve you: how many tests were run, and were the P values corrected? If a paper reports a single "significant" finding out of a large panel and never mentions correction, treat it as a hypothesis. Notice also the direction this cuts here: the correction did not weaken this paper, it strengthened it. The surviving findings mean more precisely because the authors let the others go.

**2. Hazard ratios, and what "per one standard deviation" actually means.**
- *What it is:* A hazard ratio compares how fast an event is happening in one group versus another at any given moment. A hazard ratio of 1.34 means that at any point in follow-up, the higher group is dying at about 1.34 times the rate of the lower group. It is not a probability, and it is not a risk over a lifetime.
- *How this paper used it:* Right adrenal volume carried an adjusted hazard ratio of 1.34, liver volume 1.42, both "per 1 standard deviation increase." That last phrase is doing heavy lifting. Rather than "per millilitre" — meaningless, since a millilitre of liver is nothing and a millilitre of adrenal gland is a lot — they express every organ in units of its own spread across this population. One standard deviation is roughly how far a fairly large person sits from average.
- *The theory, with a worked example:* Think of rainfall. "Each extra millimetre of rain raises flood risk by 40%" is absurd; "each standard deviation of a rainy season" is meaningful, and lets you compare a dry region with a wet one on the same scale. That is the trick here, and it is what makes 1.42 for liver and 1.34 for adrenal comparable at all despite the organs differing in size by a factor of hundreds. Now put the hazard ratio next to the base rate, which is the step people skip: 95 of 1,720 patients died, about 5.5%. Multiplying a small number by 1.34 leaves a small number. A hazard ratio of 1.34 on a 5.5% event rate is a real signal and a modest one, not a doubling of anyone's danger.
- *Watch out:* Hazard ratios are quoted in headlines as if they were absolute risks. "34% higher risk of death" is how this will be written up, and it is technically correct and deeply misleading without the base rate beside it. Always ask what the underlying rate was. Also note that the "per standard deviation" framing means the number is tied to *this population's* spread — in a group with more variable liver sizes, the same biology would give a different hazard ratio.

**3. What adjusting for confounders does — and that it works in both directions.**
- *What it is:* A confounder is a third factor that distorts the link between two others. Adjusting means building it into the model so the comparison is made between people who are similar on it. Most people learn that adjustment *shrinks* inflated findings. It can equally well *reveal* findings that were hidden.
- *How this paper used it:* Both happened in the same table, and the contrast is the clearest teaching example on this reading list so far. **Pancreas volume index** looked promising unadjusted (raw P = 0.033) and collapsed after adjustment (P = 0.385). **Liver volume** was borderline unadjusted (raw P = 0.045, corrected 0.110 — not significant) and got substantially *stronger* after adjustment (P = 0.003, corrected 0.035). Same dataset, same nine covariates, opposite effects.
- *The theory, with an analogy:* Consider ice cream sales and drowning. They rise together, because hot weather drives both. Adjust for temperature and the link disappears — a confounder was *mimicking* a relationship. Now consider a study of exercise and heart disease where the exercisers happen to be much older. The real benefit of exercise is hidden by the age gap; adjust for age and it appears — a confounder was *masking* a relationship. Here the pancreas result was the ice cream and the liver result was the exercise. The paper offers a plausible reading of why: the clinical variables being adjusted for, especially tumour stage and grade, are themselves related to both organ size and survival.
- *Watch out:* Two opposite traps. First, an unadjusted association means very little on its own; always look for the adjusted number. Second, adjustment is only as good as the variables available, and here the most obvious candidates — diabetes, liver disease, kidney function, medication — were missing or unrecorded for over half of one cohort. An adjusted result is not a purified result. It is a result purified of the specific things that happened to be in the spreadsheet.

# Jargon Translator

- **Clear cell renal cell carcinoma (ccRCC):** the most common kind of kidney cancer, roughly 70–80% of cases.
- **Nephrectomy:** surgery to remove all (radical) or part (partial) of a kidney.
- **CT scan:** a series of X-ray slices assembled into a three-dimensional picture of the body.
- **Segmentation:** outlining a structure on a scan so its size can be measured. Done by hand it is slow; here it was automatic.
- **Body surface area (BSA):** an estimate of a person's total skin area, calculated from height and weight, used here to adjust organ sizes for body size.
- **Organ volume index:** the organ's volume divided by body surface area.
- **Overall survival (OS):** time from surgery until death from any cause.
- **Recurrence-free survival (RFS):** time from surgery until the cancer comes back.
- **Hazard ratio (HR):** how much faster an event is happening in one group than another at any given moment.
- **Confidence interval:** the range of values consistent with the data. When a hazard ratio's interval includes 1.0, the study cannot rule out no effect.
- **Cox regression:** the standard statistical method for linking factors to survival time.
- **Multivariable / adjusted:** the model accounts for other factors at the same time.
- **Stratified by centre:** each hospital is allowed its own baseline survival pattern, so differences between hospitals do not masquerade as differences between patients.
- **False discovery rate (FDR) / Benjamini-Hochberg:** a method for adjusting P values when many tests are run, controlling the share of claimed findings that are false.
- **Propensity score matching:** pairing people from two groups who are similar on chosen characteristics, here age and sex, so the comparison is fairer.
- **Competing risk:** an event that prevents the one you are studying. Someone who dies cannot later have a recurrence, and a competing-risk model handles that properly.
- **Dice coefficient / intraclass correlation:** two ways of scoring how closely an automatic outline matches a human one. Higher is better; both were high here.
- **Kaplan-Meier curve:** the stepped graph showing what fraction of a group is still alive over time.
- **C-index, NRI, IDI:** three ways of asking whether a new measurement improves an existing risk prediction.
- **Leibovich score / pTNM stage:** established scoring systems for estimating kidney cancer risk after surgery.

# What You Can (and Can't) Say

**Fair to say:**
- "A 2026 multicentre study of 1,720 kidney cancer patients used automated CT measurement to show that larger liver and right adrenal gland volumes were independently associated with worse overall survival after surgery."
- "No organ measurement was associated with cancer recurrence once the authors corrected for multiple testing."
- "Compared with 3,052 matched healthy adults, the cancer patients had larger spleens and adrenal glands and smaller pancreases."
- "The associations were modest: hazard ratios of 1.29 to 1.42 per standard deviation, against an overall death rate of 95 in 1,720 over about four years."
- "The authors call for external validation and describe the biological explanations as speculative."

**Not fair to say:**
- "A bigger liver causes worse cancer outcomes" — this is an association in retrospective data, adjusted for the variables that happened to be available, with no mechanism demonstrated and diabetes, liver disease, and kidney function absent from the model.
- "AI predicts kidney cancer survival from a CT scan" — the AI measured organs. The survival claims come from conventional statistics, and no prediction was made in advance or tested on anyone.
- "Adrenal gland size is a survival marker" — the right gland was associated and the left was not, despite the two correlating at 0.756. That asymmetry has no explanation and awaits replication.
- "This changes how kidney cancer patients should be managed" — nothing was validated outside these four hospitals, and no action follows from the finding.
- "Liver volume predicts recurrence" — it looked that way before correction for multiple testing and did not survive it, as the paper states.

# Bottom Line for Your Life

Two things make this one worth your time, and neither is the finding itself.

The first is that it shows a different way AI enters a medical paper. In every earlier entry on your list, the model was the claim — it diagnosed, it predicted, it was compared against doctors. Here the model just measures, accurately and at a scale no human would attempt, and then ordinary statistics do all the arguing. That distinction matters when you read headlines. "AI study finds X" can mean the AI found X, or it can mean AI held the ruler while humans did the finding. Those deserve very different levels of scrutiny, and the second kind should be judged as the ordinary epidemiology it is.

The second is that you get to watch a good statistical habit operate on real numbers. The authors tested twenty things, corrected for having tested twenty things, and published the four findings that died in the correction, including one that would have made a nicer story. A pancreas result at P = 0.033 became P = 0.110 and then evaporated. A whole strand about cancer recurrence disappeared. Most papers would have reported the raw numbers and let you assume. The next time you meet a study reporting one significant result from a large panel of measurements, the question to ask is the one this paper answers unprompted: how many things did you test, and did you account for that?

For anything touching your own health, this is early work. The associations are modest, unvalidated outside four hospitals in one country, unexplained, and not actionable. One study is one data point. This is an educational breakdown, not medical advice.

---

**Sources** (based on articles retrieved from PubMed and PubMed Central; identifiers verified against the live PubMed/NLM record — URL browsing is blocked in this environment, so links are constructed from that verified record):
- DOI: https://doi.org/10.1080/07853890.2026.2730502
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42723375/ (PMID 42723375)
- Full text (PMC, open access): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC13573536/

**Why this paper.** The queue held only four entries, all deferred because their full text cannot be reached from this environment, so today's run fell back to scanning the past week's literature. Two stronger candidates on theme were found and rejected for the same reason — both are in a journal with no PubMed Central copy yet and a publisher domain blocked here. They are now recorded in the queue for a later attempt:
- Huang HM, et al. "Prediction Models for In-Hospital Delirium Using Routinely Collected Electronic Health Record Data: Systematic Review." *JMIR Medical Informatics* 2026;14:e91618 — https://doi.org/10.2196/91618 (PMID 42748492). An appraisal of 29 prediction models using the PROBAST and TRIPOD frameworks.
- Ahmed A, et al. "Trust in Generative AI for Health Information Consumption and the Effect of Learned Dependency: Randomized Controlled Experimental Study." *Journal of Medical Internet Research* 2026;28:e98326 — https://doi.org/10.2196/98326 (PMID 42747973). Two randomized experiments on whether habitual reliance on AI degrades people's ability to notice when it is wrong.
