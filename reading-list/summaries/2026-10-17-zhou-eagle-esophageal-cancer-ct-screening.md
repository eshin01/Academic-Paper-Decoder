# Large-scale esophageal cancer screening through noncontrast computed tomography and artificial intelligence

**Authors:** Zhou J, Guo G, Yao J, Yu Q, Zheng C, Feng X, Ye X, Zhou Y, Yang P, Lambert L, … Zhang D, Ji J, Li N, Xie C, Cao K, Zhao Y, Zhang L, Wang Q (43 authors; DAMO Academy / Alibaba Group, Hupan Lab, Sun Yat-sen University Cancer Center and 12 further centres in China, the Czech Republic and the USA)
**Journal:** Nature Medicine, 2026; 32(10): 3748–3759 (published 22 September 2026)
**Decoded:** 2026-10-17

> ## ⚠ ABSTRACT ONLY — and this one needs explaining
>
> **This analysis is based on the abstract, not the full text.** This paper has been the highest-priority entry in the reading list's backlog since 2026-09-21 and has been re-checked every single day for 26 days. Today a PubMed Central identifier finally appeared (PMC13668756) — but the record serves no body text. Every retrieval route was tried and failed:
> - PubMed Central full-text tool: the PMC identifier resolves, but returns no article
> - Direct fetch of `pmc.ncbi.nlm.nih.gov`: blocked at DNS by this environment's network policy
> - Direct fetch of the publisher page at `nature.com`: blocked the same way
> - A third-party full-text service: requires a paid subscription this session does not have
> - arXiv / alphaXiv: searched; **no preprint of this paper exists**
>
> So after 26 deferrals I am decoding the abstract, clearly labelled, rather than deferring a 27th time. **Everything below comes from the abstract or is arithmetic I did on the abstract's own numbers.** I could not check the participant funnel, the reference standard, the inclusion criteria, confidence intervals (the abstract gives none), the comparison with radiologists, the funding, or the conflicts of interest. **The grade is provisional and may move in either direction.** I will upgrade this summary if the full text becomes readable.

**Source links (verified against the live PubMed record):**
- DOI: https://doi.org/10.1038/s41591-026-04656-4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42773211/
- Full text (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC13668756/ — **identifier verified in the PubMed record; the body text could not be retrieved, see above**
- Trial registration as stated in the abstract: Chinese Clinical Trial Registry, **ChiCTR2300074806**. This registry was not reachable from this session, so the registration **could not be independently verified**.

---

## 1. The Gist

Oesophageal cancer kills most of the people who get it, for one reason: by the time it causes symptoms, it is usually too late. Caught early it is often curable. There is no practical way to find it early. The only reliable test is endoscopy — a camera down the throat — which is invasive, needs sedation and a trained operator, and nobody is going to do it on a whole population.

Meanwhile, millions of people get an ordinary chest CT scan every year, for all sorts of unrelated reasons. The oesophagus sits right there in every one of those scans. Nobody looks at it, because it is a floppy, collapsed tube that moves when you swallow and breathe, and an early tumour in it is essentially invisible to the human eye on a plain CT. Radiologists do not even try.

This group built an AI to try anyway. They trained it on 6,813 patients from two hospitals, then tested it across twelve centres in three countries on 80,612 people.

It works better than it has any right to. On ordinary chest CTs already sitting in hospital archives, it correctly cleared 98.5% of healthy people while catching 90.0% of cancers. It worked on low-dose CT too — which matters enormously, because low-dose CT is what millions of people already get for lung cancer screening, so this could ride along on a programme that already exists.

Three things deserve emphasis, and two of them are warnings.

The impressive part is that this team clearly understood the hardest problem in screening. When a disease is rare, even a very accurate test generates mostly false alarms. So they went back and recalibrated, cutting false positives by 72.7% without losing sensitivity, and then ran it prospectively on 17,446 people, where 42.2% of the people it flagged genuinely had something. For a screening test, that is a remarkable number.

The first warning: **it catches cancer much better than it catches pre-cancer.** 90.0% for cancer, but only 52.5% for precancerous lesions. Screening exists to find disease *before* it becomes cancer. At the headline operating point, this misses nearly half of exactly what you would most want to find.

The second: the numbers quoted above come from **different settings of the same system**, tested in different places. A reader could easily staple together "90% sensitivity" from one cohort and "99.94% specificity" from another and produce a figure that describes nothing that was ever measured.

## 2. Study Snapshot

**Everything in this section is from the abstract. Anything a Study Snapshot would normally contain and that the abstract does not state is marked as such — and that is a great deal.**

**Design:** development and multi-centre validation of a deep learning model, named EAGLE (Esophageal AI-Guided malignant Lesion Evaluation), to detect precancerous lesions and cancer from non-contrast chest CT. The abstract describes both retrospective and prospective components. **The detailed design, inclusion and exclusion criteria, and participant flow are not available in the abstract.**

**Where:** 12 validation centres across three countries. Author affiliations span China (Guangzhou, Shantou, Shanghai, Hangzhou, Lishui, Changsha, Chengdu, Suining, Urumqi, Fuzhou, Beijing, Chongqing, Hefei), the Czech Republic (Charles University, Prague) and the USA. Model development is credited to DAMO Academy, Alibaba Group, and Hupan Lab.

**Training:** 6,813 patients from two centres.

**Validation:** 12 centres, three countries, **80,612 patients**, across opportunistic and population-based screening settings.

**The named validation cohorts, with what each reported:**
- **Opportunistic screening on existing CT scans** — eight centres, n = 11,466. **98.5% specificity, with 90.0% sensitivity for cancer and 52.5% for precancerous lesions.**
- **Low-dose CT validation** — two centres, n = 1,607. Described as "comparable performance"; no figures given in the abstract.
- **Calibration in a real-world cohort** — three centres, n = 35,402. **Reduced false positives by 72.7% while preserving sensitivity.**
- **Prospective hospital validation** — n = 17,446. **42.2% positive predictive value.**
- **Real-world low-dose screening** — n = 10,959. **99.94% specificity.**
- **Paired CT-endoscopy cohorts** — two centres, n = 702. **65.0% sensitivity for precancerous lesions and 78.4% for stage I cancer, at a higher-sensitivity operating point.**

**A number that does not quite close.** Those six cohorts sum to 77,582. The abstract states 80,612 validation patients. That leaves **3,030 unaccounted for** — plausibly an internal validation set not named in the abstract, or overlap handled differently, but the abstract does not say.

**Exploratory analysis:** the abstract states that analyses of a prospectively enrolled cohort "suggest that referring high-risk individuals for endoscopy could improve screening efficiency." No figures are given.

**Reference standard: not stated in the abstract.** For the paired cohorts it is presumably endoscopy; for the others it is not described.

**Confidence intervals: none are given anywhere in the abstract**, for any figure.

**Comparison with radiologists: not mentioned in the abstract.**

**Registration:** the abstract cites Chinese Clinical Trial Registry identifier **ChiCTR2300074806**. Not independently verifiable from this session.

**Funding and competing interests: not available in the abstract.** Note that a substantial share of the authorship is employed by DAMO Academy / Alibaba Group and Hupan Lab, who built the model.

## 3. How Strong Is This Evidence? (Grade 4/5 — provisional, abstract only)

Four out of five, and the asterisk is doing real work. **This grade describes a design as described, not a design I was able to inspect.** Normally the things that decide a grade here are the participant funnel, the reference standard, whether the operating point was chosen honestly, and whether the confidence intervals support the claims. I could check none of those. What follows is an assessment of the scale and shape of the validation programme, plus arithmetic on the reported numbers.

**Why the described design is, on its face, the strongest in this reading list.**

Twelve validation centres in three countries is genuinely external validation — rung five on the ladder this list has been building, the one almost nothing reaches. Compare the last few weeks: a study whose "external" cohort was 47 patients from the same hospital; a review where fifteen studies supplied 26 validation datasets, one study contributing six. Here the validation set is twelve times larger than the training set, which is the reverse of the usual ratio and the right way round.

There is a **prospective** component (n = 17,446). Almost everything decoded in this list has been retrospective, and the authors of those papers said prospective work was the missing piece. This has it.

There is a **paired CT-endoscopy cohort** (n = 702), which is the only design that can tell you what the model missed, because every person got both tests. Without a paired design, sensitivity estimates in screening are guesses based on who later turned up with disease.

Most tellingly, the team **calibrated for the false-positive problem and then re-tested**. Cutting false positives by 72.7% while preserving sensitivity, and reporting the resulting PPV from a prospective cohort, shows an understanding of screening that many AI papers lack entirely. Most would have published the 98.5% specificity and stopped.

And they report **low-dose CT performance separately**. That is the deployment question that matters: millions already get low-dose CT for lung cancer screening, so an oesophageal model that works on those scans costs nothing extra in radiation, time or money.

**What holds it at 4, and what I simply could not check.**

**The precancer sensitivity is the real result, and it is 52.5%.** The point of screening is to catch disease before it is cancer. At the headline operating point this model misses almost half of precancerous lesions. At the higher-sensitivity point in the paired cohort it reaches 65.0% — better, and still a third missed. The abstract leads with 90.0% for cancer, which is the easier and less valuable task. Finding a cancer early is good; finding the lesion before it becomes cancer is the whole purpose.

**Three different operating points are reported across cohorts** — 98.5% specificity in one, 99.94% in another, a "higher-sensitivity operating point" in a third, and an unstated one in the prospective cohort. Each is legitimate on its own. Together they are an invitation to misquote, and I expect this paper to be cited with figures that were never measured in the same configuration.

**No confidence intervals appear anywhere in the abstract.** On 80,612 patients the intervals will be tight, so this is a reporting rather than a precision problem, but it means no figure here can be read with its uncertainty.

**I could not verify a single number, the reference standard, the funnel, or the conflicts.** For a paper where roughly a quarter of the authors work for the company that built the model, the competing-interests statement is not a formality, and I have not seen it.

**The cohort arithmetic leaves 3,030 patients unexplained**, which is almost certainly innocent and is exactly the sort of thing the full text would resolve in a sentence.

**Where 4/5 sits, provisionally.** If the full text supports the abstract, this is the most consequential medical-AI paper decoded in this list — a genuinely multinational validation of a task that was considered impossible, on scans that already exist. The grade could rise. It could also fall, if the reference standard turns out to be weak, if the prospective cohort is enriched, or if the funnel excludes most of the people the test is for — all failure modes seen repeatedly in the last fortnight. I am not going to pretend to know.

## 4. The Editor's Concerns

Most of what I would normally write here requires the methods section. These are the concerns the abstract alone raises.

**Lead with the precancer number, not the cancer number.** The abstract's structure puts "98.5% specificity, with 90.0% sensitivity for cancer" first and "52.5% for precancerous lesions" in the same breath, where it reads as a secondary detail. It is the primary result for a screening tool. A reader skimming will take away 90%.

**State which operating point produced each figure.** Three thresholds appear across six cohorts. The prospective cohort's PPV of 42.2% is quoted without saying which setting generated it. My own reconstruction suggests the calibrated one — the arithmetic is in the Statistics Spotlight and lands within a tenth of a percentage point — but a reader should not have to derive that.

**Reconcile 77,582 with 80,612.** One sentence.

**Give confidence intervals.** None appear in the abstract. With 702 patients in the paired cohort, the interval on "65.0% sensitivity for precancerous lesions" is not narrow, and that is the figure the field will argue about.

**Say what the reference standard was in each cohort.** In the paired cohorts it is presumably endoscopy. In the 11,466-patient opportunistic cohort it cannot have been — nobody endoscopes 11,466 people to validate a CT model. So sensitivity there rests on something else: later clinical diagnosis, registry linkage, or chart review. Which one it is determines how much the sensitivity figure is worth, and it is not in the abstract. This is the single thing I would most want to read.

**Report the interval-cancer rate.** In any screening programme, the number that matters is how many cancers appear *between* screens after a negative result. Without it, sensitivity measured against a same-day reference standard will overstate what the programme achieves.

**Report the downstream harms.** A positive result leads to endoscopy. At the calibrated operating point my arithmetic puts that at roughly 1.4 unnecessary endoscopies per cancer found — good for a screening test, but it is a real procedure with real risks, and the abstract frames false positives purely as a number to be reduced rather than as procedures done to people.

**Make the competing-interests statement prominent.** A large share of the authorship is at DAMO Academy / Alibaba Group and Hupan Lab, the developers. That is normal and not disqualifying; it should be stated where readers see it.

**One note on my own position.** Several of these concerns may already be addressed in the full text. I am flagging them as open questions raised by the abstract, not as failures of the paper.

## 5. Statistics Spotlight

### Concept 1: Why screening is brutally hard, and why specificity is the number that decides it

This is the central idea in all of screening, and this paper is the best illustration of it this reading list has produced.

**The problem.** When a disease is rare, almost everyone you test is healthy. So even a tiny false-positive rate, applied to an enormous number of healthy people, produces more false alarms than true findings.

**Work it with EAGLE's own figures.** Take the headline operating point: sensitivity 90.0%, specificity 98.5%. That specificity sounds excellent — it gets 98.5% of healthy people right. Now screen 10,000 people where 0.33% have the disease:

- 33 people have cancer. The model catches 90% of them: **30 found, 3 missed.**
- 9,967 people are healthy. The model wrongly flags 1.5% of them: **150 false alarms.**
- So of 180 people flagged, 30 have cancer. **Positive predictive value 16.6%** — five false alarms for every cancer found.

Five unnecessary endoscopies per cancer. That might be tolerable; it might not. But notice what happened: a test that is "98.5% specific" produced a result that is wrong five times out of six when it says yes.

**It gets worse as the disease gets rarer.** Holding sensitivity and specificity fixed:

- at 1% prevalence → PPV 37.7%, 1.7 false alarms per cancer
- at 0.5% → PPV 23.2%, 3.3 false alarms
- at 0.2% → PPV 10.7%, 8.3 false alarms
- at 0.1% → PPV 5.7%, 16.7 false alarms
- at 0.05% → PPV 2.9%, **33 false alarms per cancer found**

Same test every time. Only the population changed.

**An everyday analogy.** Imagine a security scanner that is 98.5% accurate at clearing innocent travellers. In a queue of 10,000 people containing 33 genuine threats, it stops 180 people. It is working exactly as designed, and 150 of those people did nothing. The scanner is not broken; rarity is doing the damage.

**Now watch what the authors did about it, because this is the good part.** They report calibrating in a real-world cohort of 35,402 people, which "reduced false positives by 72.7% while preserving sensitivity."

Run that through the arithmetic. A false-positive rate of 1.5%, cut by 72.7%, becomes 0.41% — so specificity rises from 98.5% to about **99.59%**. Redo the 10,000-person screen:

- still 33 cancers, still 30 caught, 3 missed
- but false alarms fall from 150 to **41**
- **PPV rises from 16.6% to 42.1%**, and false alarms per cancer fall from 5.0 to 1.4

And here is the check that makes me confident this reconstruction is right: the paper reports **42.2%** PPV in its prospective validation of 17,446 people. My reconstruction, built only from the abstract's other numbers, predicts 42.1% at a prevalence of about 0.33%. Those agree to a tenth of a percentage point — which strongly suggests the prospective cohort used the calibrated operating point in a population with roughly that prevalence. *(That is my inference from the abstract's numbers, not something the abstract states.)*

**The lesson in one line: in screening, improving specificity from 98.5% to 99.6% is worth far more than improving sensitivity from 90% to 95%.** Cutting false alarms by two-thirds is what turns an unusable test into a usable one, and it is why the team's decision to calibrate and re-test is the most impressive thing in the abstract.

**Watch out.** Whenever you see a screening test described by its sensitivity and specificity alone, do this arithmetic. The number that decides whether a screening programme is feasible is the PPV in the population actually screened, and it is often an order of magnitude worse than the specificity suggests. Also note the direction of the trap here: 99.94% specificity, reported in the real-world low-dose cohort, means a false-positive rate of 0.06% — about 1 healthy person in 1,667. At 0.1% prevalence that yields a PPV around 60%. Specificity in the fourth decimal place is not pedantry in screening; it is the whole game.

### Concept 2: Detecting the disease versus detecting it in time

The two sensitivity figures in this abstract are 90.0% and 52.5%, and almost everyone will quote the first.

**What they mean.** 90.0% is sensitivity for **cancer** — tumours that already exist. 52.5% is sensitivity for **precancerous lesions** — abnormal tissue that may become cancer if left, and which can usually be removed with a simple endoscopic procedure.

**Why the second number is the one that matters.** The entire economic and human case for screening rests on catching disease before it becomes dangerous. A screening programme that finds cancers slightly earlier helps some people. A screening programme that finds precancer and removes it prevents the cancer from ever existing. That is the difference between a treatment programme and a prevention programme.

At the headline operating point, this model misses **47.5% of precancerous lesions** — nearly half. At the higher-sensitivity operating point used in the paired CT-endoscopy cohort, it reaches 65.0%, missing about a third, and finds 78.4% of stage I cancers.

**An analogy.** A smoke detector that reliably alerts you once the furniture is burning is useful. A smoke detector that catches smouldering is what saves the house. Selling the first as the second is the mistake to avoid.

**Why the gap exists, and why it is not a criticism of the model.** A precancerous lesion is a thin patch of abnormal cells on the lining of a collapsed tube. On a non-contrast CT it may displace almost no tissue. That the model finds half of them at all is, frankly, astonishing — the paper describes this as "a task historically considered impossible," and for precancer that framing is justified. The criticism is about emphasis, not performance: the abstract foregrounds the easier number.

**Watch out, and this generalises well beyond oesophageal cancer.** Whenever a screening paper reports performance for more than one stage or severity of disease, the headline will be the stage that is easiest to detect, and the clinically valuable number will be the one buried in the same sentence. Read for the hardest category, not the best one. The same pattern appeared in a paper decoded three days ago, where the pooled accuracy was excellent for the common disease subtypes and the model caught only 61% of the rare one.

### Concept 3: One system, several operating points — and why you cannot mix them

Every model of this kind produces a score, and a threshold turns that score into a yes or no. Move the threshold and you trade sensitivity against specificity: catch more disease at the cost of more false alarms, or the reverse. The same model can therefore produce many different pairs of numbers, all of them honest.

**This abstract reports at least three different settings:**

- the opportunistic external test cohort, at **98.5% specificity**
- the real-world low-dose screening cohort, at **99.94% specificity**
- the paired CT-endoscopy cohort, at an explicitly **"higher-sensitivity operating point"**
- and the prospective cohort, reporting **42.2% PPV** with the operating point not stated in the abstract

Each of these is a legitimate report of the same system doing a different job. The danger is purely in how they get quoted.

**The failure mode, concretely.** Someone writes: "EAGLE detects oesophageal cancer with 90% sensitivity and 99.94% specificity." Every number in that sentence appears in the abstract. The sentence describes a configuration that was never measured — 90.0% sensitivity came from the cohort at 98.5% specificity, and 99.94% specificity came from a different cohort in a different setting, where the sensitivity is not reported in the abstract at all.

**A worked intuition.** A camera has a shutter speed and an aperture, and they trade off. Reporting "this photo was taken at 1/1000th of a second" and "this lens opens to f/1.4" is fine. Saying "this photo was taken at 1/1000th at f/1.4" when one came from a different shot is a claim about an exposure nobody made. Sensitivity and specificity are a pair in exactly the same way: they come from one point on one curve, and they travel together or not at all.

**Watch out.** Whenever a paper reports performance in several cohorts, check whether the threshold was the same in each before combining any two numbers. The signal to look for is a phrase like "at a higher-sensitivity operating point," which this paper uses honestly — it tells you the threshold moved. The harder cases are the papers that move it silently. And when the operating point is not stated at all, as with the 42.2% here, the figure cannot be combined with anything.

## 6. Jargon Translator

**Oesophageal cancer** — Cancer of the food pipe. One of the deadliest common cancers, largely because it is usually found late.

**Precancerous lesion** — Abnormal tissue that is not yet cancer but may become it. Usually removable by a minor endoscopic procedure, which is why finding it is the main prize in screening.

**Stage I cancer** — Cancer caught at its earliest stage, still confined and usually treatable.

**Non-contrast CT** — A standard CT scan with no injected dye. Quick, cheap, done constantly for unrelated reasons.

**Low-dose CT (LDCT)** — A CT using much less radiation, already used for lung cancer screening in many countries. The reason this matters: scans that already happen could be reused.

**Endoscopy** — A camera passed down the throat to look at the oesophagus directly. The accurate test, and the invasive one.

**Opportunistic screening** — Looking for one disease in scans that were done for something else. No new scan, no extra radiation, no extra cost.

**Population-based screening** — Deliberately inviting a defined population to be tested.

**Sensitivity** — Of the people who have the disease, the share the test catches.

**Specificity** — Of the people who do not, the share the test correctly clears. In screening this is the number that decides feasibility.

**False positive** — A healthy person the test flags. Here, someone sent for an unnecessary endoscopy.

**Positive predictive value (PPV)** — Of the people the test flags, the share who really have the disease. Depends heavily on how common the disease is.

**Prevalence** — How common the disease is in the group being tested. The hidden variable that governs PPV.

**Operating point / threshold** — The score above which the model says "positive." Moving it trades sensitivity against specificity.

**Calibration** — Here, adjusting the model or its threshold so its outputs behave better in the real world. In this paper, specifically to cut false positives.

**Paired cohort** — A group where everyone received both the test under study and the reference test, so you can see exactly what was missed.

**Prospective** — Enrolling people and then testing them, rather than analysing records of things that already happened. Harder, slower and much more convincing.

**External validation** — Testing on data from institutions that had nothing to do with building the model.

**Interval cancer** — A cancer that appears between screening rounds after a negative result. The real measure of what a screening programme missed; not reported in this abstract.

## 7. What You Can (and Can't) Say

**You CAN say:**
- "An AI model detected oesophageal cancer on ordinary non-contrast chest CT, a task previously considered impossible, and was validated across twelve centres in three countries on more than 80,000 patients."
- "On existing CT scans at eight external centres, it cleared 98.5% of healthy people while catching 90.0% of cancers."
- "It also worked on low-dose CT, the kind already used for lung cancer screening."
- "After recalibration cut false positives by 72.7%, a prospective study of 17,446 people found that 42.2% of those flagged genuinely had disease."
- "In cohorts where everyone also had an endoscopy, it found 65.0% of precancerous lesions and 78.4% of stage I cancers at a higher-sensitivity setting."
- "The validation set was twelve times larger than the training set and spanned three countries, which is unusually strong external validation."

**You CAN'T say:**
- ❌ "It detects oesophageal cancer with 90% sensitivity and 99.94% specificity." Those two figures come from different cohorts at different operating points. That combination was never measured.
- ❌ "It catches oesophageal cancer early." It catches 90.0% of cancers but only 52.5% of precancerous lesions at the headline setting — and precancer is what "early" means in screening.
- ❌ "42.2% PPV means the test is 42% accurate." PPV is the share of flagged people who have disease, and it depends on how common disease is in the group screened. In a lower-prevalence population the same test would have a much lower PPV.
- ❌ "This is ready for population screening." The abstract reports no interval-cancer rate, no comparison against radiologists, no cost or harm analysis, and no evidence that using it changes outcomes.
- ❌ "98.5% specificity means few false alarms." At the prevalences involved it means roughly five false alarms per cancer found — which is precisely why the team recalibrated.
- ❌ "The results are verified." **I could not read the full text.** Everything here rests on an abstract. The reference standard, the participant flow, the confidence intervals and the competing interests are all unexamined.
- ❌ Any claim about what the full paper's methods show. I have not seen them.

## 8. Bottom Line for Your Life

If you have been told you are at risk of oesophageal cancer — long-standing reflux, Barrett's oesophagus, a family history, or you live somewhere this cancer is common — nothing changes today. The accurate test is still endoscopy, and if your doctor has recommended one, this does not replace it. What this paper suggests is that within a few years, a chest CT you have for some entirely different reason might also quietly get checked for this. That would be a genuinely good thing, and it is not available yet.

If you work in radiology, gastroenterology or screening policy: the reason to take this seriously is the shape of the validation rather than the headline accuracy. Twelve centres in three countries, a validation set twelve times the training set, a prospective arm, a paired CT-endoscopy cohort, and — most unusually — a team that recognised the false-positive problem, went back and recalibrated for it, and then re-tested prospectively. That sequence is rare. The number to interrogate is the 52.5% precancer sensitivity, because the case for screening stands or falls on precancer, and the number to ask for is the interval-cancer rate, which is not in the abstract.

For your paper-reading, take two things from today, one about the subject and one about the process.

**On the subject: do the screening arithmetic yourself, every time.** It takes a minute and it is the difference between understanding a screening paper and being impressed by one. A test that is "98.5% specific" generates five false alarms for every cancer found when the disease affects 1 in 300 people. The same test, recalibrated to 99.6% specific, generates 1.4. That one change matters more than any plausible improvement in sensitivity, and it is invisible unless you work it out. Sensitivity sells papers; specificity decides whether a screening programme can exist.

**On the process: say plainly what you could not check.** This decode is based on an abstract, after twenty-six days of trying to get the full text and failing through five different routes. I can do real arithmetic on the numbers the abstract reports, and I have. I cannot tell you what the reference standard was in the largest cohort, which is the single most important thing about a sensitivity figure. Those are different kinds of statement, and a summary that blurs them is worse than useless. The habit this whole reading list is trying to build is noticing the difference — in what you read, and in what you write.

---

*This is an educational analysis of the published abstract of a scientific paper, not medical advice. Nothing here is guidance about cancer screening or your own risk. If you are worried about oesophageal cancer, talk to your doctor.*
