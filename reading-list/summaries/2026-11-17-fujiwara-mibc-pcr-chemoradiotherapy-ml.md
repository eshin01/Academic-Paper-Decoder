# Machine learning models to predict pathological complete response after chemoradiotherapy in muscle-invasive bladder cancer: toward optimized indications for bladder preservation

**Authors:** Fujiwara M, Tanaka H (Dept of Urology, Institute of Science Tokyo), Hirahara D (Teikyo Heisei University), Saho T (Kokura Memorial Hospital), Takaya E (AI Laboratory, Tohoku University Hospital), Matsumoto S, Yoshitomi K, Kobayashi M, Nakamura Y, Chen W, Ishikawa Y, Fukuda S, Fukushima H, Waseda Y, Yoshida S, Fujii Y (Dept of Urology, Institute of Science Tokyo) — 16 authors
**Journal:** Clinical and Translational Radiation Oncology, 2026; 62: 101320 (published 13 October 2026)
**Decoded:** 2026-11-17

**Analysis basis:** **FULL TEXT** (retrieved from PubMed Central, PMC13741961) — Introduction, all Methods sub-sections including patients, both treatment protocols, the endpoint and machine-learning approach, and the statistical analysis; all of Results including patient characteristics, the model, the clinical-factor analysis and survival; the complete Discussion with its limitations; and the ethics and competing-interest declarations. **All tables, figures and the entire supplement are unreachable**, which costs four specific things named throughout: **Supplementary Table 3** (the 102 candidate models' results, hence the regularized logistic regression's performance), **Supplementary Table 4** (the five additional train/test splits), **Supplementary Table 1** (the deposited TRIPOD checklist), and the calibration plot and decision-curve figure.

**Source links (verified):**
- DOI: https://doi.org/10.1016/j.ctro.2026.101320
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42997524/
- Full text used: https://pmc.ncbi.nlm.nih.gov/articles/PMC13741961/

**Basis of link verification.** Direct URL fetching is blocked from this session (`doi.org` does not resolve under the network policy here), so verification was done against the live PubMed/NLM record. According to PubMed, a query for PMID 42997524 returned this exact title, these sixteen authors with these affiliations, *Clinical and Translational Radiation Oncology* volume 62 article 101320, publication date 13 October 2026, and DOI `10.1016/j.ctro.2026.101320`; a PMID-to-PMCID conversion returned **PMC13741961**; and the full text was then retrieved from PubMed Central by that PMC ID and matches the record. Both halves of the chain were confirmed independently.

**Ethics: fully reported, and stronger than most retrospective studies manage.** Institutional review board approval **number M2019-192** (Institute of Science Tokyo), and — unusually for a retrospective analysis — **"Written informed consent was obtained from all patients before protocol enrollment,"** because the cohort comes from two prospective treatment protocols rather than a chart review. Consent to publish also obtained.

**Competing interests: none declared, explicitly.**

**Funding: not reported.** No funding statement appears anywhere in the retrieved text. I am recording the absence rather than assuming either way.

**Reporting guideline: TRIPOD, named and with a completed checklist deposited** as Supplementary Table 1. **This is the second consecutive entry in this reading list to name a reporting guideline**, after eight in a row that named none — and Section 4 records what that does to the standing observation.

---

## 1. The Gist

**A Tokyo urology group spent 24 years collecting something almost nobody in this field has: the actual pathology of what chemoradiotherapy left behind in the bladder. Then they ran 102 machine-learning models at it, reported honestly that the result wobbles when you reshuffle the patients, and in the process produced a four-item checklist that is more useful than the model.**

Here is the clinical problem, and it is a genuine dilemma. **Muscle-invasive bladder cancer** has traditionally been treated by removing the whole bladder, which works but costs the patient a urinary diversion bag and a permanent change to their life. The alternative is **bladder preservation**: scrape out the tumour, then chemotherapy plus radiation, and keep the bladder if the cancer is gone. Survival can be comparable **in the right patients.** The whole game is picking them. Get it wrong and microscopic cancer survives in a bladder you have decided to keep, and it comes back.

**And here is why the field has struggled to pick them, which is the most important sentence in this paper.** Most bladder-preservation studies check whether the treatment worked using **a scan and a scrape** — imaging plus another transurethral resection. The authors state the problem plainly: **"Imaging and TURBT can miss microscopic residual cancer, which may later cause intravesical recurrence."** So the field has been training and judging its predictions against an answer key that is itself unreliable.

**This institution is in an unusual position to do better.** Since 1997 it has run a protocol in which the bladder — or the part of it that held the tumour — is **surgically removed after the chemoradiotherapy**, and the pathologist examines the whole specimen. So for these patients there is a real answer: was the cancer gone or not. **That is a deliberate upgrade of the reference standard**, and it is exactly what yesterday's entry in this reading list argued the whole field needs.

**The study.** 285 patients with cT2–4N0M0 disease treated 1997–2021, all of whom had chemoradiotherapy followed by **partial cystectomy (148) or radical cystectomy (137).** Nine routine clinical variables, all yes/no: stage ≥cT3, tumour bigger than 30 mm, multiple tumours, hydronephrosis, bladder-neck involvement, carcinoma in situ alongside, variant histology, high grade, and progression from earlier non-invasive disease. Split 228 for training and 57 for testing. **AutoGluon** — automated machine learning — trained and ranked **102 candidate models**, and the winner, a stacked ensemble called WeightedEnsemble_L4, was then run once on the 57 held-out patients.

**The headline: 178 of 285 patients (62%) had no cancer left, and the model scored an AUC of 0.829 on the test set** — meaning that given one patient who responded and one who did not, it ranks them correctly about 83% of the time.

**Now the three things that matter more than the headline, two of which the authors tell you themselves.**

**First, and to their real credit, they checked whether that 0.829 was luck — and it partly was.** They repeated the entire procedure on **five additional random splits** of the same 285 patients. From the Discussion: **"Performance was lower in the additional five-fold internal validation, showing that the result varied across patient splits."** And in the limitations: **"Therefore, overfitting cannot be excluded."** So **0.829 is the best of six attempts**, the other five were worse, and their values sit in a supplementary table I could not retrieve. **Very few papers run that check. Fewer report it when it goes against them.**

**Second, the test set is 57 people — 36 who responded and 21 who did not.** That is the entire evidence base for every test-cohort number in the paper. The confidence interval on the AUC runs from **0.706 to 0.932**, which I verified independently against the standard formula. A span that wide means the truth could be "modestly useful" or "excellent" and this study cannot tell them apart.

**Third, the calibration — and here the authors put the bad news in their own abstract.** A model's *ranking* can be good while its *numbers* are wrong. The check for that is the **calibration slope**, where 1.0 is perfect. They report **0.856, with a 95% interval from 0.469 to 1.639**, and say: **"the wide CI indicated uncertainty in calibration."** They are right, and it is worth being precise about how uncertain. At the bottom of that interval the model's risk estimates are wildly too extreme; at the top they are wildly too timid. **The interval contains 1.0, so nothing is wrong — and it is so wide that nothing is established either. Calibration here is not acceptable; it is unmeasured.** For a tool whose purpose is to tell a patient their chance of keeping their bladder, the probability is the output that matters.

**And now the finding I think is the paper's real contribution, which the paper files under "exploratory."**

A simple count. Take four of the nine variables — **stage ≥cT3, tumour over 30 mm, carcinoma in situ, multiple tumours** — and just add up how many a patient has. Across all 285 patients, the chance of a complete response was **87% with none of them, 66% with one, 49% with two, and 29% with three or more** (p<0.001). I checked that these four groups reconstruct the overall count of 178 responders exactly. **And survival tracks it**: five-year metastasis-free survival of 87.5%, 86.5%, 70.9% and 59.8%.

**That is a clinically usable rule you can apply at the bedside with a pen.** It needs no ensemble, no AutoGluon and no 102-model screen, and because it is simple and monotone it is far more likely to survive validation elsewhere than a stacked ensemble tuned on 228 patients. **The authors, to their credit, make no grand claim for their ensemble either** — they write, flatly, **"We do not claim that the multilayer ensemble is superior to simpler models."**

**What I found that the paper does not discuss.** Its great strength is surgical pathology — but **52% of those specimens are partial cystectomies, which remove only the original tumour site.** So for half the cohort, "no cancer left" means "no cancer at the original site in the piece we removed," not "no cancer anywhere in the bladder." **That is a sampling of the bladder, which is the same category of problem the authors criticise imaging and TURBT for** — one level up. Section 4 lays out both the concern and the mitigation fairly.

## 2. Study Snapshot

**Study type:** development and internal validation of a clinical prediction model, on a retrospective analysis of patients enrolled in **two prospective institutional treatment protocols**. Single centre. **No external validation**, which the authors state.

**Setting and cohort.** Institute of Science Tokyo. **314 patients** with cT2–4N0M0, pathologically confirmed urothelial carcinoma, treated under one of two protocols between **1997 and 2021**. **29 excluded (9.2%)** for not undergoing cystectomy — **6 (1.9%) distant metastasis, 23 (7.3%) patient withdrawal** — leaving **285 (91%)**, of whom **148 had partial cystectomy and 137 radical cystectomy.** I verified every figure in that cascade. **"No formal sample size calculation was performed; all eligible patients treated during the study period were included"** — stated rather than concealed.

**The two protocols, which matter for interpretation.** The **tetramodality bladder-preservation protocol** (since 1997): maximal transurethral resection, then induction chemoradiotherapy, then response assessment by imaging, urine cytology and repeat resection; **patients with a complete clinical response had consolidative partial cystectomy at the original tumour site, and those without were offered radical cystectomy.** Separately, **presurgical chemoradiotherapy before radical cystectomy** for patients who were not candidates for preservation. The authors argue that combining both groups **"may have reduced selection bias related to preselection for bladder preservation."**

**Treatment.** External-beam radiotherapy **40 Gy in 20 fractions to the true pelvis, no boost**, with **two cycles of concurrent cisplatin (20 mg/day for 5 days), three weeks apart.** Dose reduced for poor performance status or impaired renal function.

**The endpoint.** **pCR, defined as ypT0, determined from the partial or radical cystectomy specimen.** No residual tumour.

**The predictors — nine, all dichotomised.** ≥cT3; tumour size >30 mm; bladder-neck involvement; hydronephrosis; multiplicity; concomitant carcinoma in situ; primary histologic grade G3; variant histology; and progression from prior non-muscle-invasive disease. Selected "based on prior studies." Staging used the **8th edition TNM**, grade the **1999 WHO classification**, variants the **2016 WHO classification**. Tumour size was the maximum diameter on pretreatment CT or MRI. **There were no missing data for the predictors or the outcome** — stated.

**Cohort characteristics.** Median age **69**; **212 (74%) male**. Clinical T stage **T2 in 169 (59%), T3 in 105 (37%), T4 in 11 (4%)** — which I verified sums to 285. Median tumour size **3.0 cm (IQR 2.0–4.0)**. Bladder-neck involvement in **54 (19%)**, hydronephrosis **69 (24%)**, multiple tumours **108 (38%)**, concomitant CIS **34 (12%)**, variant histology **60 (21%)**.

**The modelling, described with unusual precision.** **AutoGluon Tabular version 1.3.1** with **Python 3.11.13**. The 285 were split **228 training / 57 test**, and **"the split was performed without stratification"** — stated. **"Model training, model ranking, and final model selection were completed in the training cohort before test-cohort performance was examined."** AutoGluon trained and evaluated **102 candidate models using bagging and multilayer stacking**, and **"the candidate models included simpler base-level models, including regularized logistic regression."** Crucially: **"Candidate models were ranked by AUC from internal validation within the training cohort, and the model with the highest AUC was selected."**

**Uncertainty and calibration.** Discrimination by AUC, calibration by a calibration plot. **95% CIs for test-cohort AUC and calibration slope from 2,000 stratified bootstrap samples.** Decision curve analysis **"retained as an exploratory analysis."**

**The split-stability check, which is the best methodological decision in the paper.** **"To assess whether performance depended on a single patient split, we performed additional internal validation using five different train/test splits of the 285 patients."** Each used 228 for development and 57 for evaluation, **"the same AutoGluon modeling procedure was repeated independently for each split,"** and the ensemble generated in each was evaluated in its own test cohort.

**Permutation importance was post hoc and quarantined.** **"After final model selection and test-cohort performance assessment, an exploratory permutation analysis in the training cohort was used to rank the relative contribution of the nine predictors. This post hoc analysis was not used for model training or model selection."**

**Statistics.** Mann-Whitney and Fisher exact tests; Kaplan-Meier with log-rank; survival measured **from the date of cystectomy**; two-sided, p<0.05. **"We followed the TRIPOD statement for prediction model development and internal validation (Supplementary Table 1)."** Non-ML analyses in **JMP Pro 17.0** and **R 4.0.2**.

**Results — the outcome.** **pCR in 178/285 (62%).** Training **142/228 (62%)**, test **36/57 (63%)** — so the unstratified split happened to balance well, and I verified 142 + 36 = 178.

**Results — the model.** **"Among 102 models, WeightedEnsemble_L4 was selected because it had the highest training-cohort AUC (0.921)."** In the test cohort: **AUC 0.829 (95% CI 0.706–0.932)**. **Calibration slope 0.856 (95% CI 0.469–1.639)**, with the paper's own gloss: **"The wide CI indicates uncertainty in calibration within the 57-patient test cohort."**

**Results — the four clinical factors.** Permutation ranked **≥cT3, tumour size >30 mm, concomitant CIS, and multiplicity** as the leading four. Training-cohort pCR rates with versus without each: **≥cT3, 46/91 (50.5%) vs 96/137 (70.1%); size >30 mm, 37/77 (48.1%) vs 105/151 (69.5%); concomitant CIS, 13/27 (48.1%) vs 129/201 (64.2%); multiplicity, 39/85 (45.9%) vs 103/143 (72.0%).** **I verified that all four of these splits decompose exactly to 228 patients and 142 pCR events.**

**Results — the factor count.** In training, **66 (29%), 73 (32%), 61 (27%), 27 (12%) and 1 (0.4%)** patients had 0, 1, 2, 3 and 4 factors, with pCR rates of **83%, 66%, 49%, 33% and 0%** (p<0.001). **The 0% cell is one patient.** In the full cohort, **84, 88, 72 and 41** patients had 0, 1, 2 and ≥3 factors, with pCR of **87%, 66%, 49% and 29%** (p<0.001) — and I verified these four cells reproduce the overall total of 178 responders.

**Results — survival.** Median follow-up **64 months**. **58 (20%) metastatic recurrence, 70 (25%) died of any cause.** Five-year metastasis-free survival **79.0%**, overall survival **79.7%**. By factor count (0/1/2/≥3): five-year MFS **87.5%, 86.5%, 70.9%, 59.8%** (p<0.001); OS **86.9%, 85.1%, 72.8%, 66.1%** (p=0.041).

**What the authors say about their own work, and it is a lot.** On the ensemble: **"We do not claim that the multilayer ensemble is superior to simpler models."** On the split check: **"Performance was lower in the additional five-fold internal validation, showing that the result varied across patient splits."** On comparison with MRI-radiomics approaches: **"We did not directly compare our approach with these MRI-based methods."** On biology: the proposed mechanisms **"remain hypotheses that require direct testing."** On survival: **"Because all patients underwent partial or radical cystectomy after CRT, the survival results cannot be directly applied to patients managed with bladder preservation alone."**

**And a five-point limitations section.** Retrospective single-centre design limits applicability; **"External validation should use the final model in independent, preferably multi-institutional cohorts."** The training cohort was **"relatively small for evaluating many complex models,"** performance was lower on other splits, **"Therefore, overfitting cannot be excluded."** Selection bias **"may remain"** despite combining both protocols, and the 29 excluded patients are named again. **"Pretreatment imaging was not standardized, which may have affected clinical T staging and tumor-size measurement."** And finally, the calibration slope's wide interval means **"predicted pCR probabilities remain uncertain."**

**Not reported or not retrievable:** **funding**; **any interobserver agreement on the ypT0 assessment**; **pCR rate or model performance separately for partial versus radical cystectomy**; any analysis by accrual era across the 25-year window; the operating threshold, and therefore any sensitivity, specificity, PPV or NPV; **Supplementary Table 3** with the 102 candidate models including the logistic regression; **Supplementary Table 4** with the five additional splits; the deposited TRIPOD checklist; and the calibration plot and decision curve.

## 3. How Strong Is This Evidence? (Grade 3 out of 5)

**This is the most honestly reported paper in this reading list, and it is limited by a test set of 57 people. The reporting quality exceeds the grade, and the grade is what a reader may safely conclude.**

**What is genuinely well done, and the first item is the reason this paper was chosen.**

**The reference standard was deliberately upgraded, by design rather than by discussion.** Yesterday's entry argued that the binding constraint on medical AI is the quality of the answer key, and that resection pathology beats sampling. **This institution built a 24-year protocol that produces resection pathology**, and the paper's introduction identifies exactly the right problem with the field's norm: imaging and repeat resection "can miss microscopic residual cancer." **That is the correct response to the ceiling problem, and almost nobody does it because it requires removing the bladder you were trying to save.**

**The model-selection order is right.** Selection was on **internal validation within the training cohort**, completed **before the test cohort was examined**. This resolves the specific worry I wrote down yesterday: ranking 102 candidates on apparent training fit would have selected the most overfit model, and that is not what happened.

**They ran the split-stability check and published the result against themselves.** Five extra train/test splits, same procedure each time, and the finding reported in both Discussion and limitations: performance was lower, so **"overfitting cannot be excluded."** In this reading list, that behaviour has been rare enough to be remarkable each time it appears.

**Calibration was assessed and its uncertainty flagged in the abstract.** Not buried in a supplement — in the abstract. Compare entry 77 three days ago, which reported eight discrimination metrics and no calibration at all.

**Bootstrap intervals on both headline quantities**, 2,000 stratified samples, and I verified the AUC interval against the standard asymptotic formula: consistent.

**Permutation importance was explicitly quarantined** from training and selection, and labelled exploratory.

**TRIPOD named with a deposited checklist.** No missing data, stated. No sample-size calculation, stated. Split unstratified, stated. Software versions given to the patch level. **IRB number and written informed consent from every patient** — because these were prospective protocols, not a chart trawl.

**And the restraint is unusual.** "We do not claim that the multilayer ensemble is superior to simpler models." "We did not directly compare our approach with these MRI-based methods." The biological explanations "remain hypotheses." The survival results "cannot be directly applied to patients managed with bladder preservation alone." **Each of those sentences costs the authors something and each is correct.**

**And the internal consistency is flawless.** I checked the cohort cascade, the split, all four factor subgroups, the factor-count tables in both cohorts, and the reconstruction of the total event count from the factor cells. **Everything reconciles exactly.**

**So why 3.**

**The test set is 36 responders and 21 non-responders.** Every test-cohort number in the paper rests on those 57 people. The AUC interval spans **0.706 to 0.932** — a width of 0.23. The study can establish that the model discriminates; it cannot establish how well.

**0.829 is the best of six splits, by the authors' own account.** They do not claim otherwise, and the primary split was prespecified with a fixed seed rather than chosen for being favourable — so this is honest luck, not cherry-picking. **But the consequence for a reader is the same: 0.829 is the high end of a distribution, not its centre**, and the five lower values are in a supplement I could not reach.

**Calibration is unmeasured, not acceptable.** A slope interval of **0.469 to 1.639** admits both severe over-confidence and severe under-confidence. The interval contains 1.0, so nothing is wrong; it is 1.17 wide, so nothing is established. **The paper's stated purpose is "to support decision-making regarding bladder preservation," and that decision needs a probability.**

**The winner's 0.921 internal-validation AUC is an order statistic, not an estimate.** It is the maximum of 102 noisy numbers. The honest estimate is the 0.829, and the 0.092 gap between them is roughly what you would expect from taking a maximum over a hundred candidates on 228 patients.

**Half the reference standard is a partial specimen.** 148 of 285 cystectomies removed only the original tumour site. Section 4 gives the concern and the mitigation; **the paper never reports pCR separately by specimen type**, so whether ypT0 means the same thing in both halves of the cohort is unknown.

**No interobserver agreement on the endpoint.** The pre-registered question yesterday's entry prompted. Assessing ypT0 on a post-radiotherapy specimen involves judgement — treatment effect, atypia, scarring — and no agreement statistic is reported.

**A 25-year accrual window with no era analysis.** 1997 to 2021. Imaging, staging, resection quality and pathology practice all changed, and the WHO instruments used date from 1999 and 2016. The authors note imaging was not standardised; they do not analyse by period.

**Internal validation only, single centre** — stated clearly and listed first among limitations.

**Funding not reported.**

**Why not 2.** Because entry 77 scored 2 for analyses not run and claims not supported. **Here the analyses were run, the unfavourable ones were published, and the conclusion is correctly bounded**: "This may support decision-making," and "Independent external validation is required to support future clinical implementation." **Nothing is overclaimed.**

**Why not 4.** Because the grade tracks what a reader can safely take away, and from 57 test patients a reader can take away that the signal is real and not how strong it is. **Entry 74 earned a 4 with 229 patients because it had repeated nested cross-validation, 1,000-fold permutation testing of the whole pipeline, and out-of-fold everything. This paper has one prespecified split, a five-split sanity check, and a frank admission that the splits disagreed.**

**What would make it a 4, concretely.** **Report the five additional splits' AUCs in the main text** and lead with their range rather than the single best. **Report the regularized logistic regression's performance in the main text** — it was among the 102 candidates and its number is the one a reader most needs. **Report pCR and model performance separately for partial versus radical specimens.** **Report agreement on ypT0** between two pathologists on a sample. And **validate externally**, which the authors identify as the priority. Four of those five use data the authors already have.

## 4. The Editor's Concerns

**1. The reference standard was upgraded — and half of it is still a sampling.** Credit first: the paper correctly identifies that imaging plus repeat resection "can miss microscopic residual cancer," and it solves that by using surgical pathology. **But 148 of 285 specimens (52%) are partial cystectomies, which remove the original tumour site and not the rest of the bladder.** So for half the cohort, ypT0 means "no tumour at the original site in the piece removed." **A partial cystectomy is to the bladder what a needle biopsy is to a tumour** — a sample, chosen on prior information, that can miss disease elsewhere. **The mitigation is real and I will state it:** partial cystectomy was reserved for patients with a *complete clinical response* on imaging, cytology and repeat resection, so the remainder of the bladder was assessed by other means. **The problem is that the label is therefore heterogeneous across the cohort** — in 137 patients it means the whole bladder was clean, in 148 it means one region was clean and the rest looked clean by the very methods the introduction calls unreliable. **The paper never reports pCR rates or model performance separately by specimen type**, and that single table would settle whether the two halves can be pooled.

**2. 0.829 is the best of six splits, and that is in the Discussion rather than the abstract.** The authors ran five additional train/test splits and report: **"Performance was lower in the additional five-fold internal validation, showing that the result varied across patient splits."** **This is excellent practice and it demotes the headline.** The abstract and the Highlights both carry 0.829 ("Machine learning predicted CRT response with a test AUC of 0.83") with no indication that five other splits of the same patients did worse. **The honest summary of a split-dependent result is its range, not its maximum** — and the range is in Supplementary Table 4, which I could not read. A reader who stops at the Highlights gets the most favourable of six numbers.

**3. Calibration is unmeasured, and that is the output the paper's stated purpose requires.** The slope is **0.856 (95% CI 0.469–1.639)**. At 0.469 the model's probabilities are far too extreme; at 1.639 far too compressed. **The interval contains 1.0 — so no miscalibration is shown — and it is 1.17 wide, so no calibration is shown either.** Section 5 explains why those are different statements. The paper's conclusion is that this "may support decision-making regarding bladder preservation," and a patient deciding whether to keep their bladder needs a number, not a ranking. **Full credit for putting the uncertainty in the abstract; the consequence is that no predicted probability from this model should be quoted to anyone yet, and the paper's final limitation says exactly that.**

**4. The regularized logistic regression was in the race and its result is not in the paper's body.** The Methods state that **"the candidate models included simpler base-level models, including regularized logistic regression."** So the comparison this reading list has been asking for since entry 77 — does a simple model match the complicated one? — **was computed.** It sits in Supplementary Table 3. **The main text does not report it.** The authors then write, admirably, **"We do not claim that the multilayer ensemble is superior to simpler models"** — which is the honest position and also an admission that the number which would settle it has been relegated. **For a paper whose method is "we tried 102 models," the performance of the simplest credible one belongs in the Results.**

**5. The winner's 0.921 is the maximum of 102 candidates, not an estimate of anything.** Internal-validation AUC of the selected model was 0.921; test AUC was 0.829. **That 0.092 gap is close to what taking the best of a hundred noisy estimates on 228 patients would produce by itself.** The selection procedure was correct — ranking on internal validation, test set untouched until after — so this is not a methodological error. **It is a reason not to read 0.921 as a performance figure**, and the paper reports it without that caveat.

**6. The endpoint's own reliability is unexamined.** No interobserver agreement, no second pathologist, no kappa on ypT0. **Assessing complete response on a post-chemoradiotherapy specimen is not trivial** — radiation produces atypia, fibrosis and treatment effect that have to be distinguished from residual carcinoma. Yesterday's entry quantified exactly this kind of instability in a different tumour and found agreement among expert pathologists at kappa 0.443 for grading. **I am not asserting that ypT0 assessment is unreliable** — it is a more binary judgement than grading and may well be good. **I am recording that the paper, whose central strength is its reference standard, does not measure that standard's reliability**, and that one sample of duplicate reads would have.

**7. A 25-year accrual window, analysed as one cohort.** 1997 to 2021. Over that span: CT and MRI improved substantially, TNM moved through editions (the 8th was applied retrospectively to all), grading used a 1999 instrument and variant classification a 2016 one, and transurethral resection technique and pathology handling both changed. **The authors note that "pretreatment imaging was not standardized, which may have affected clinical T staging and tumor-size measurement"** — which is the right flag. **They do not report any analysis by accrual period**, so whether the four clinical factors predict equally well in 2001 and 2019 patients is unknown. With 285 patients over 25 years — roughly 11 per year — an era split would be underpowered, which is a real constraint rather than an excuse.

**8. All nine predictors were dichotomised, and this cuts both ways.** Tumour size became ">30 mm," stage became "≥cT3," grade became "G3." **Cutting a continuous variable into two throws away information** and usually costs predictive power — a 31 mm tumour and a 70 mm tumour are treated identically. **The gain is that it makes the four-factor count possible**, and that count is the paper's most usable output. So this is a defensible trade rather than an error, but it should be named: some of the ensemble's modest performance may be the dichotomisation rather than the data.

**9. The selection question the authors raise and cannot close.** Everyone in this cohort had a cystectomy after chemoradiotherapy — and **the entire purpose of bladder preservation is to avoid one.** The authors address this directly and better than most would: combining the preservation protocol with the presurgical-CRT protocol **"may have reduced selection bias related to preselection for bladder preservation,"** and the limitations concede **"selection bias may remain."** **The residual issue is that pCR can only be verified in someone whose bladder was opened**, so the model is trained on the subset where verification was possible and would be deployed to decide who never needs verifying. The authors also exclude 29 patients who did not reach cystectomy, including 6 who developed metastases — **the sickest, and precisely the ones a selection tool would most want to identify.**

**10. The survival analysis is honest about what it cannot support, and that sentence deserves quoting.** **"Because all patients underwent partial or radical cystectomy after CRT, the survival results cannot be directly applied to patients managed with bladder preservation alone."** The five-year metastasis-free survival gradient (87.5% to 59.8% across the factor count) is measured in people who had their bladders removed or partly removed. **A patient who keeps their bladder on the strength of this model has a different prognosis than anyone in this cohort**, and the authors say so rather than letting the survival curves imply otherwise.

**11. Funding is not reported.** No statement anywhere in the retrieved text. Competing interests are declared as none and the IRB number is given, so this looks like an omission rather than a concealment — but a 16-author, 24-year, two-protocol institutional series was funded somehow.

**12. A reporting guideline named, for the second entry running.** The tally: entries 71, 73, 74, 75, 77 and 78 named none; 69 named TRIPOD+AI with the checklist; 70 named STROBE; **76 measured the phenomenon and put it at 40% mean completeness** against the instrument written for the job; **79 named six instruments and applied them; and 80 names TRIPOD and deposits a completed checklist.** **Two in a row, after eight without.** The rule this list arrived at stands unchanged — **naming a guideline does not predict quality, so read the methods** — and the complement added yesterday holds up well here: **this paper's honesty about its split instability, its calibration and its ensemble's non-superiority is not something TRIPOD extracted from it. The same disposition produced the checklist and the candour.** TRIPOD does, however, deserve some credit for one specific thing: **it requires a calibration assessment**, and this paper has one where entry 77, which named no guideline, did not.

## 5. Statistics Spotlight

Three concepts, numbered from 306 in the running list in `queue.md`. The first is the paper's own best methodological decision and the second is the one it put in its abstract.

**One train/test split is a single draw from a distribution — and this paper shows you what happens when you check.**

Almost every machine-learning paper in medicine does this: shuffle the patients, keep most for training, hold some back for testing, report the held-back score. **The unstated assumption is that the split does not matter.** With 285 patients it matters a great deal.

These authors tested the assumption. From the Methods: **"To assess whether performance depended on a single patient split, we performed additional internal validation using five different train/test splits of the 285 patients."** Same procedure each time, 228 to develop and 57 to evaluate, the whole AutoGluon pipeline re-run independently.

**The result, from the Discussion: "Performance was lower in the additional five-fold internal validation, showing that the result varied across patient splits."**

**So 0.829 is the best of six, and the abstract reports only the 0.829.**

**Why split-to-split variation is so large here.** The test set is 57 people: **36 who responded and 21 who did not.** The AUC is built from comparing each responder against each non-responder — **36 × 21 = 756 pairs**, which sounds like a lot but rests on only 57 independent people. Move eight or ten borderline patients from one side of the split to the other and the test AUC moves substantially. **The number you report is partly a property of which patients your random seed happened to put in the test set.**

**The right way to summarise a split-dependent result is the distribution, not the maximum.** Report the mean and range across splits, or better, use repeated cross-validation so that every patient takes a turn in the test fold. **Entry 74 of this reading list did exactly that** — repeated nested cross-validation giving 25 outer test sets — and it is why that paper's near-null AUC of 0.587 is more trustworthy than many larger numbers.

**The everyday version.** You want to know whether a student understands the material, so you give them a ten-question test and they score 8 out of 10. **Then you give them five more ten-question tests from the same syllabus and they average 6.** The 8 was real — they genuinely got those eight right — and it was also the best of six attempts. **If you report only the 8, you have reported a true fact and misdescribed the student.** The honest summary is "averages about 6 and a half, ranges from 5 to 8."

**Watch out for:** a single train/test split reported with no indication of split sensitivity, especially below a few hundred patients. **Two questions. Was the split repeated, and if so what was the range? And was the reported split prespecified or chosen?** Here the answer to the second is reassuring — a fixed random seed set in advance, so the favourable draw was luck rather than selection — **and the answer to the first is in a supplementary table, which is the wrong place for it.** When a paper says performance "varied across splits" without printing the variation, treat the headline as an upper bound.

**A calibration slope with a wide interval means calibration is unmeasured — which is not the same as acceptable.**

A prediction model does two separate jobs. **Discrimination** is ranking: does it put the responders above the non-responders? That is what AUC measures, and here it is 0.829. **Calibration** is the numbers themselves: when the model says 70%, do 70 out of 100 such patients actually respond? **A model can rank perfectly and still have numbers that are badly wrong**, and for a patient deciding about their bladder it is the number that matters.

**The calibration slope is the standard check.** You take the model's predictions, and you ask how steeply actual outcomes track them. **A slope of exactly 1.0 is perfect.** A slope **below 1** means the predictions are too extreme — the model says 90% when the truth is 75%, and says 10% when the truth is 25%; it is over-confident, the classic signature of a model fitted too closely to its training data. A slope **above 1** means the opposite: the predictions are squashed toward the middle and the model is too timid.

**This paper reports 0.856, with a 95% confidence interval from 0.469 to 1.639.**

**Read both ends.** At **0.469**, predictions are grossly too extreme — a stated 90% would really be somewhere near 65%. At **1.639**, they are grossly too conservative in the other direction. **The interval is 1.17 wide and it contains 1.0.**

**Now the distinction that matters, and it is the most commonly fumbled inference in this area.** Containing 1.0 means **no miscalibration has been demonstrated.** It does **not** mean calibration has been demonstrated. Those are different claims, and with an interval this wide the honest conclusion is: **this study cannot tell whether the model's probabilities are trustworthy.** Not "they are fine." Not "they are broken." **Unmeasured.**

**The authors say precisely this, in the abstract** — "the wide CI indicated uncertainty in calibration" — and again in their final limitation: "predicted pCR probabilities remain uncertain." **That is the correct reading and it is to their credit that it is the first thing a reader of the abstract learns about calibration.**

**Why the interval is so wide: it is the 57 patients again.** Estimating a slope needs variation across the whole range of predicted risk, and 57 people spread across a 0-to-1 probability scale leaves very few in each region. **Discrimination is cheaper to estimate than calibration** — Section 5's third item shows that the AUC finding here is adequately powered while the calibration is not. **Those are two different sample-size questions and papers routinely answer only the first.**

**The everyday version.** A weather forecaster is excellent at ranking: the days they call wettest really are the wettest, every time. **But when they say "70% chance of rain," it rains on 40% of those days.** Their ranking is perfect and their numbers are useless, and you would be badly misled if you cancelled an outdoor wedding on the strength of the 70%. **Now imagine you only have six forecasts to judge them by.** You cannot tell whether their numbers are right or wrong — and saying "their forecasts seem fine" would be reporting your own ignorance as reassurance.

**Watch out for:** a prediction model reported with discrimination only. **Ask for the calibration slope and its interval, and then read the interval rather than the point estimate.** Three specific traps: a slope near 1.0 with a wide interval described as "well calibrated" (it is not calibrated, it is unmeasured); calibration reported as a plot with no slope, so the reader cannot tell how precise it is; and **any model whose purpose is to give a patient a percentage, validated only on discrimination.** If the deliverable is a number, the number needs validating.

**Minimum detectable effect, and why one claim here is powered while the other is not.**

This is short and it is the fair counterweight to the two concerns above. **A small sample is not uniformly fatal — it depends on what you are trying to detect.**

**The question to ask of any small study: what is the smallest effect it could have found?** For an AUC, the arithmetic uses the effective sample size `n1 × n2 ÷ (n1 + n2)`, where n1 and n2 are the two outcome groups. Here that is **36 × 21 ÷ 57 = 13.26**. For 80% power at a one-sided 0.05 level, the smallest detectable separation is `2.80 ÷ √13.26 = 0.769`, which converts to a **minimum detectable AUC of about 0.707**.

**The observed AUC is 0.829, which clears that floor comfortably.** So the discrimination finding is **adequately powered**: this study could detect what it reported, and the claim "these nine variables carry real signal about complete response" is supported.

**Contrast that with the calibration slope, where 57 patients are nowhere near enough** — the interval came out 1.17 wide. **Same study, same sample, one claim powered and the other not**, because ranking 756 pairs is a much easier estimation problem than pinning down a slope across the full probability range.

**And this is why the four-factor count is the paper's sturdiest result.** It is estimated on **all 285 patients, not 57**: pCR of **87%, 66%, 49% and 29%** across 84, 88, 72 and 41 patients, p<0.001, monotone, with five-year metastasis-free survival tracking the same order (87.5%, 86.5%, 70.9%, 59.8%). **I verified that those four cells reproduce the study's total of 178 responders.** A monotone dose-response across four prespecified clinical features on the full cohort, concordant with survival, is far more likely to replicate elsewhere than a stacked ensemble chosen from 102 candidates and tested on 57 people. **The paper labels the count "exploratory" and the ensemble as the main result. I would put it the other way round.**

**The everyday version.** You can tell from a short taste test that one coffee is stronger than another — that is ranking, and it needs few sips. **Telling someone the exact caffeine content in milligrams needs a laboratory.** Reporting "I am confident A is stronger than B, and I think A has 95 mg give or take 60" is two findings of very different quality, and only the first should change anyone's order.

**Watch out for:** small studies dismissed wholesale, and small studies accepted wholesale. **Both are wrong.** Work out the minimum detectable effect, and check it separately for each claim the paper makes. **A sample big enough to show that something works is routinely too small to show how well it works or what its numbers mean** — and the second two are usually what a clinician needs.

## 6. Jargon Translator

**Muscle-invasive bladder cancer (MIBC)** — bladder cancer that has grown into the muscle wall. Serious, and historically treated by removing the whole bladder.

**cT2–4N0M0** — the clinical stage before treatment: tumour into muscle (T2) up to invading neighbouring structures (T4), with **no** lymph node spread (N0) and **no** distant metastasis (M0). "c" means assessed clinically, from scans and examination, rather than from surgery.

**Radical cystectomy** — removal of the entire bladder, with a urinary diversion afterwards. The traditional standard.

**Partial cystectomy** — removal of only the part of the bladder that held the tumour. **Used for 148 of the 285 patients here, and the reason the reference standard is a sampling for half the cohort** — concern 1.

**TURBT (transurethral resection of bladder tumour)** — scraping the tumour out through the urethra, with no external incision. Both a treatment and a biopsy.

**Chemoradiotherapy (CRT)** — radiation plus chemotherapy together, the chemotherapy making the cancer more sensitive to the radiation. Here 40 Gy in 20 fractions with two cycles of cisplatin.

**Gray (Gy)** — the unit of radiation dose. **Fractions** are the daily sessions the dose is split into.

**Trimodality / tetramodality therapy** — resection plus chemotherapy plus radiation (tri), with surgery added at the end (tetra). This institution's protocol is tetramodality.

**Bladder preservation** — curing the cancer while keeping the bladder. The whole motivation for the paper.

**Pathological complete response (pCR) / ypT0** — no cancer found anywhere in the surgical specimen after treatment. "y" means post-treatment, "p" pathological, "T0" no primary tumour. **The outcome being predicted.**

**Carcinoma in situ (CIS)** — flat, high-grade cancer confined to the bladder lining. Signals more widespread urothelial disease, which is why it predicts worse response.

**Hydronephrosis** — urine backing up and swelling the kidney, usually because a tumour is obstructing. A known poor-prognosis sign.

**Variant histology** — urothelial cancer with an unusual microscopic appearance; generally more aggressive.

**Multiplicity** — more than one tumour in the bladder at once.

**AutoGluon** — open-source software that automatically trains and compares many models on table-shaped data. **WeightedEnsemble_L4** is its naming for a fourth-layer stacked ensemble: models built on top of other models' predictions.

**Bagging and stacking** — bagging trains many copies of a model on resampled data and averages them; stacking feeds one layer's predictions into the next as inputs.

**Regularized logistic regression** — the simplest respectable approach, with a penalty to prevent overfitting. **Among the 102 candidates here, with its result in an unreachable supplement** — concern 4.

**AUC (area under the ROC curve)** — the chance the model ranks a responder above a non-responder. 0.5 is a coin flip. **Measures ranking only.**

**Calibration slope** — whether predicted probabilities match observed rates. **1.0 is perfect; below 1 means too extreme, above 1 too timid** — technique 307.

**Bootstrap confidence interval** — resample the test set many times (2,000 here), recompute, read off the range.

**Permutation importance** — scramble one predictor and see how much performance drops. **Post hoc here, and explicitly excluded from training and selection.**

**Decision curve analysis** — a method for judging whether a model's predictions would improve decisions at various risk thresholds. **Labelled exploratory here.**

**Stratified split** — dividing patients so the outcome rate matches in each part. **This split was *not* stratified**, stated — and happened to balance anyway (62.3% versus 63.2%).

**TRIPOD** — the reporting checklist for prediction-model studies. **Named here with a completed checklist deposited.**

**Metastasis-free survival / overall survival** — time until cancer appears elsewhere, and time until death from any cause. Both measured **from the date of cystectomy** here.

**Kaplan-Meier and log-rank** — the standard way to plot survival over time and to test whether two curves differ.

## 7. What You Can (and Can't) Say

**You can say:**

"In 285 patients with muscle-invasive bladder cancer treated with chemoradiotherapy followed by partial or radical cystectomy, 178 (62%) had no residual cancer in the surgical specimen."

"Unlike most bladder-preservation studies, which assess response with imaging and repeat resection, this study defined complete response from surgical pathology — the authors' stated reason being that imaging and resection can miss microscopic residual cancer."

"An automated machine-learning pipeline evaluated 102 candidate models on nine routine clinical variables, with model selection completed in the training cohort before the test cohort was examined; the selected ensemble achieved a test AUC of 0.829 (95% CI 0.706–0.932) in 57 patients."

"The calibration slope was 0.856 with a 95% CI of 0.469 to 1.639, and the authors state in their abstract that this wide interval indicates uncertainty in calibration."

"When the authors repeated the analysis across five additional train/test splits, performance was lower, and they state that overfitting cannot be excluded."

"Four clinical factors — stage ≥cT3, tumour larger than 30 mm, concomitant carcinoma in situ, and multiple tumours — were associated with lower complete-response rates, and across all 285 patients the response rate fell from 87% with none of them to 29% with three or more (p<0.001), with five-year metastasis-free survival tracking the same gradient from 87.5% to 59.8%."

"The authors state they do not claim the multilayer ensemble is superior to simpler models."

**You cannot say:**

"The model predicts complete response with 83% accuracy." **AUC is not accuracy** — it is the probability of ranking a responder above a non-responder. And no operating threshold is reported, so no accuracy, sensitivity or specificity exists in this paper.

"The model achieves an AUC of 0.83." **That is the best of six splits.** The authors report that five other splits of the same patients did worse, and those values are in a supplement. **Treat 0.829 as an upper bound.**

"The model's risk estimates are reliable." **Calibration is unmeasured.** A slope interval from 0.469 to 1.639 excludes nothing; the authors' own final limitation is that "predicted pCR probabilities remain uncertain."

"This can be used to decide who keeps their bladder." **Not yet, and the authors agree:** "Independent external validation is required to support future clinical implementation." Single centre, internal validation only, 57 test patients.

"Machine learning outperformed conventional models here." **Not shown.** Regularized logistic regression was among the 102 candidates and its result is not in the main text, and the authors explicitly decline to claim ensemble superiority.

"Patients with no risk factors have 87% response and good survival on bladder preservation." **Everyone in this cohort had their bladder, or part of it, removed.** The authors state that "the survival results cannot be directly applied to patients managed with bladder preservation alone."

"62% is the complete-response rate for chemoradiotherapy in this disease." **It is the rate in this cohort**, which was selected by two specific protocols at one institution over 25 years, excluded 29 patients who never reached surgery, and used a 40 Gy regimen without boost.

"Surgical pathology gave a definitive answer for every patient." **For 148 of 285 the specimen was a partial cystectomy covering the original tumour site only.** Whether ypT0 means the same thing in a partial and a radical specimen is not reported.

"The four-factor count is a validated risk score." **It is an exploratory analysis**, labelled as such, derived from a post hoc permutation ranking in the training cohort — though it is estimated on all 285 patients and is the paper's most robust-looking finding.

**The honest one-sentence version:** *a 24-year single-institution series that did the hard and rare thing — obtaining actual surgical pathology to define whether chemoradiotherapy worked, instead of guessing from a scan — then ran 102 models at nine routine clinical variables, selected properly and tested once on 57 patients for an AUC of 0.829 whose confidence interval spans 0.71 to 0.93, reported frankly that five other splits of the same patients did worse and that overfitting cannot be excluded, put its own uncomfortable calibration interval in its abstract, declined to claim its ensemble beat simpler models — and along the way produced a four-item bedside count, on all 285 patients, that is the most useful thing in it and is filed as exploratory.*

## 8. Bottom Line for Your Life

**If you or someone close to you is facing this decision — bladder removal versus bladder preservation — the usable content here is the four-item count, not the model.** Stage beyond T2, a tumour bigger than about 3 cm, carcinoma in situ alongside, and more than one tumour. **With none of those, 87% of patients in this series had no cancer left after chemoradiotherapy; with three or more, 29% did.** That is a real gradient from 285 patients, and it is the kind of thing worth asking your own team about: *how many of these four do I have?* **It is not a decision rule and it has not been validated anywhere else** — but it is a better-grounded conversation than any single number from this paper's model.

**The other thing worth knowing is why this study was hard to do.** Checking whether chemoradiotherapy truly cleared the cancer requires looking at the bladder tissue — which means removing it, which is the thing bladder preservation exists to avoid. **Most studies therefore check with a scan and a scrape, and those miss microscopic disease.** If you are reading about bladder-preservation outcomes, it is fair to ask how response was confirmed.

**If you are a clinician being offered a prediction model by anyone:** this paper models the two questions to ask, because it answers both on itself. **"What happens if you reshuffle the patients?"** — here, performance dropped. **"What is the calibration slope and its confidence interval?"** — here, 0.856 from 0.469 to 1.639, meaning the probabilities are unverified. **A model that cannot answer the first is untested; a model that cannot answer the second should not be giving patients percentages.**

**If you build clinical prediction models, two habits from this paper are worth copying wholesale.** **Repeat your split and publish the spread** — these authors ran five more and reported that the extras were worse, which cost them their headline and bought them credibility. And **say what you have not shown**: "we do not claim the multilayer ensemble is superior to simpler models" is one sentence that prevents a decade of over-citation. **One habit is worth improving on: put the simple model's number in the Results, not the supplement.** Logistic regression was in this race and a reader cannot see how it did.

**If you read papers, the transferable skill from this entry is the second half of the sample-size question.** Everyone knows to ask whether a study is big enough. **Fewer ask "big enough for which claim?"** Here, 57 test patients were comfortably enough to establish that the model discriminates — the minimum detectable AUC was about 0.71 and the observed was 0.83 — and nowhere near enough to establish what its probabilities mean. **Same study, same patients, one claim supported and one not.** When a paper reports both a ranking metric and a probability metric, check the power of each separately, because the second almost always needs more people than the first.

**If you are reading the coverage:** expect "AI predicts which bladder cancer patients can keep their bladder." The study is careful, the pathology is genuinely better than the field's norm, and the four-factor gradient is real. The three things that will not make the headline are that **0.829 was the best of six attempts by the authors' own account**, that **the model's probabilities are unverified and the authors say so in the abstract**, and that **the plain four-item count on all 285 patients is more likely to be useful than the 102-model ensemble.**

**This is education, not medical advice.** Nothing here should change anyone's cancer treatment. If you are weighing bladder preservation against cystectomy, that decision belongs with your own urologist and oncologist, who will know things about your case that no nine-variable model contains.

---

## Appendix: the pre-registered questions, verification, and status on 2026-11-17

**Both pre-registered questions, answered.** Set yesterday, written down before this paper was read.

**(1) "What is the reported agreement on the pCR reference standard itself, and does the paper acknowledge any?"** — **Not reported. No interobserver agreement, no kappa, no duplicate read of ypT0.** **But the paper does something better than acknowledge the problem: it designs around it.** Its introduction identifies exactly the defect entry 79 quantified — "most bladder-preservation studies... usually assess CRT response with imaging and TURBT rather than complete surgical pathology. Imaging and TURBT can miss microscopic residual cancer" — and its first stated clinical strength is that "surgical pathology was used to define pCR after CRT." **That is entry 79's prescription applied by design, and it required a 24-year institutional protocol to make possible.** **My finding the paper does not address: 148/285 (52%) of those specimens are partial cystectomies covering only the original tumour site, so for half the cohort the label is a sampling of the bladder rather than a complete examination** — entry 79's needle-biopsy problem one level up. Mitigation stated fairly in concern 1; the one table that would settle it (pCR by specimen type) is absent.

**(2) "With 102 models screened and a calibration-slope CI of 0.469–1.639, how was selection among 102 candidates accounted for?"** — **Answered precisely, and the answer is reassuring.** Selection was on **AUC from internal validation within the training cohort**, with "model training, model ranking, and final model selection... completed in the training cohort **before** test-cohort performance was examined." **So my specific worry — that ranking 102 candidates on apparent training fit would select the most overfit model — is resolved; it was bagged internal validation, not raw fit, and the test set was untouched.** What remains: **the winner's 0.921 internal-validation AUC is the maximum of 102 noisy estimates**, an order statistic rather than an estimate, and the 0.092 drop to the test AUC of 0.829 is about what taking a best-of-100 on 228 patients would produce unaided. **And the calibration prediction was right: the interval spans severe overfitting to severe underfitting, so calibration is unestimated — which the authors state in their own abstract.**

**Arithmetic verified today, every check passing.** Cohort cascade closes exactly: **314 − (6 + 23) = 285**, with the excluded fractions reproducing 9.2% / 1.9% / 7.3%; **148 partial + 137 radical = 285**. Split: **228 + 57 = 285**, pCR **142 + 36 = 178**, rates 62.3% / 63.2% / 62.5% against stated 62 / 63 / 62. **All four clinical-factor subgroups decompose exactly to 228 patients and 142 pCR events** (≥cT3 91+137; size 77+151; CIS 27+201; multiplicity 85+143 — and 46+96, 37+105, 13+129, 39+103 all equal 142). Factor-count table sums to 228 with percentages reproducing 29/32/27/12/0.4. **Full-cohort factor cells 84 + 88 + 72 + 41 = 285, and 84×0.87 + 88×0.66 + 72×0.49 + 41×0.29 = 178.3, reproducing the reported total of 178 responders.** Hanley-McNeil SE on AUC 0.829 with 36/21 gives an asymptotic 95% interval of **0.724–0.934** against the paper's bootstrap **0.706–0.932** — consistent, with the bootstrap slightly wider on the low side as expected. Minimum detectable AUC at 80% power: effective n **13.26**, d_min **0.769**, **AUC floor 0.707** — the observed 0.829 clears it. Variance explained: AUC 0.829 ≈ **31%**, against entry 77's 0.9724 ≈ 65% and entry 74's 0.587 ≈ 2.4%. **No arithmetic error was found anywhere in this paper; its internal consistency is the best in the recent run.**

**What could not be verified.** **All tables, figures and the entire supplement**, costing four specific things: **Supplementary Table 3**, the 102 candidate models' results — hence **the regularized logistic regression's performance, which the Methods confirm was among the candidates** and which is the number entry 77 taught this list to look for; **Supplementary Table 4**, the five additional train/test splits, so **the range behind "performance was lower" is unreadable and 0.829 can only be characterised as the best of six**; **Supplementary Table 1**, the deposited TRIPOD checklist; and the calibration plot and decision-curve figure. Also absent from the retrieved text: **funding**; any interobserver agreement on ypT0; pCR or performance split by partial versus radical specimen; any accrual-era analysis across 1997–2021; and the operating threshold, hence no sensitivity, specificity, PPV or NPV anywhere. **Nothing was reproduced that was not seen.**

**Positive practice worth carrying forward.** **A deliberately upgraded reference standard** — surgical pathology instead of imaging plus TURBT, which is the field's norm and the defect entry 79 quantified. **Correct selection order**: ranking on internal validation, selection completed before the test cohort was examined. **A split-stability check run across five additional splits, found unfavourable, and reported** in both Discussion and limitations with "overfitting cannot be excluded." **Calibration assessed and its uncertainty placed in the abstract.** **2,000-sample stratified bootstrap intervals** on both headline quantities. **Permutation importance quarantined** from training and selection and labelled exploratory. **TRIPOD named with a completed checklist deposited.** **No missing data, no sample-size calculation, and an unstratified split — all three stated rather than concealed.** **IRB number M2019-192 and written informed consent from every patient**, possible because the cohort came from prospective protocols. **Software versions to the patch level.** And four sentences of genuine restraint: "We do not claim that the multilayer ensemble is superior to simpler models"; "We did not directly compare our approach with these MRI-based methods"; the biological explanations "remain hypotheses that require direct testing"; and **"Because all patients underwent partial or radical cystectomy after CRT, the survival results cannot be directly applied to patients managed with bladder preservation alone."**

**Reporting-guideline pattern — two consecutive entries now name one.** Entries 71, 73, 74, 75, 77 and 78 named none; 69 named TRIPOD+AI with the checklist; 70 named STROBE; **76 measured the phenomenon at 40% mean completeness**; **79 named six instruments and applied them; 80 names TRIPOD and deposits a completed checklist.** **The rule stands unchanged — naming a guideline does not predict quality, so read the methods — and yesterday's complement holds up:** this paper's candour about split instability, calibration and its ensemble's non-superiority is not something a checklist extracted from it; the same disposition produced both. **One narrow credit to the instrument, though: TRIPOD requires a calibration assessment, and this paper has one where entry 77, which named no guideline, had none at all.**

**Deferred status, 2026-11-17.** ***Annals* *Choosing Wisely* (42896192) — day 28**, weekly re-check and **abstract-only date both 2026-11-19, two days out, and it is the next scheduled pick**; standing note that its 5.4% / 0.6–12.2% CI is a clustering signature computed across 15 recommendations rather than 4,050 responses. **Gait foundation model (42995231) — day 9**, abstract-only date **2026-11-30**; largest multiplicity problem this list will have faced (**1,887 of 3,210 tested phenotypes called significant**), first question being what false-discovery-rate procedure ran across those 3,210 tests. **Both due a PMC re-check on 2026-11-19**, when the *Annals* threshold fires.

**Landmark check, 2026-11-10 → 11-17.** One record, previously assessed: the *Nature Medicine* gait commentary (43003904). **No new candidates; none displaces the queue.**

**Plan set on 2026-11-17.** **Next run, 2026-11-18, takes shelf item (F)** — the bitewing radiograph positioning-error classifier trained entirely on **mannequins** (PMID 42981213, PMC13734376) — **the last spare on the shelf, and the shelf is then empty, so a restock is due.** **Two questions written down now. (1) Does anything in the paper test transfer from mannequin to patient?** — a mannequin has no soft tissue, no motion, no anatomical variation and no pathology, so this is the most extreme form of the transportability question entry 78 raised with two OCT devices: **not a different scanner but a different kind of subject.** **(2) What is the reference standard for a "positioning error," and who defined it?** — entry 79 says the ceiling is set there, and positioning error is a judgement about image geometry that may be far more reliably assessed than a tumour grade, which would make this the first entry in the run with a genuinely stable reference standard. **Also note for the restock: after (F) the shelf is bare**, so the 2026-11-18 run should screen for new PMC-confirmed candidates alongside the decode, as was done on 2026-11-10.

**Standing watch item:** PM Heart trial results (protocol PMID 42893738), quarterly.
