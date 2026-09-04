# The Artificial Intelligence Clinician learns optimal treatment strategies for sepsis in intensive care

- **Authors:** Matthieu Komorowski (Imperial College London / Harvard–MIT), Leo A. Celi (MIT, Beth Israel Deaconess), Omar Badawi (MIT; Philips Healthcare eICU R&D; Univ. of Maryland), Anthony C. Gordon (Imperial), A. Aldo Faisal (Imperial)
- **Venue:** Nature Medicine, 2018;24(11):1716–1720 (received 23 March 2018; accepted 13 August 2018; published 22 October 2018)
- **DOI link:** https://doi.org/10.1038/s41591-018-0213-5
- **PubMed link:** https://pubmed.ncbi.nlm.nih.gov/30349085/ (PMID 30349085)
- **Full-text link:** none public — the paper is closed access with no PubMed Central version. Analyzed from the published PDF supplied by the user.
- **Basis:** FULL TEXT — main text, figures, limitations, competing interests, and data/code availability. (This entry replaces an earlier abstract-only version decoded the same day; the full text raised the evidence grade from 2/5 to 3/5 and surfaced several facts the abstract omitted — see "What the full text changed" at the end.)
- **Decoded:** 2026-09-04

---

# The Gist

Sepsis — a severe infection that starts shutting down organs — kills more people in hospitals than anything else, and doctors still disagree about how much intravenous fluid and how much blood-pressure-raising drug (vasopressor) to give, and when. This team built an AI that studied 17,083 sepsis admissions' worth of decisions and outcomes, then worked out its own dosing strategy, which it tested against records from 79,073 more patients at 128 other hospitals. The AI generally recommended **less fluid and more vasopressor** than doctors actually gave. Patients whose doctors happened to prescribe close to the AI's suggestion had the lowest death rates — and the further from the AI's dose, the higher the mortality. That last finding is the paper's most quoted and its most fragile, for reasons below.

# Study Snapshot

- **Study type:** Retrospective reinforcement-learning study on existing intensive-care records. A computational study, not a trial — **no patient was ever treated according to the AI.** Low on the evidence ladder for treatment claims; it generates a hypothesis about better dosing, it does not establish one.
- **Development data (n):** 17,083 ICU admissions (88.4% of eligible sepsis patients) from 5 ICUs at one tertiary teaching hospital — the MIMIC-III database. Split into 13,666 for training and 3,417 for model selection.
- **Test data (n):** 79,073 admissions (73.6% of eligible) from 128 different hospitals — the eICU Research Institute (eRI) database, entirely separate from the training data.
- **Patients:** average age 64–65; 52–56% male; roughly half on mechanical ventilation; MIMIC-III 90-day mortality 18.9% (hospital mortality 11.3%); eRI hospital mortality 16.4%.
- **What the AI decided:** total intravenous fluid and maximum vasopressor dose in each 4-hour block, for up to 72 hours around sepsis onset, using 48 patient variables. Patient states were clustered into discrete groups; treatment choices were boiled down to a 5×5 grid of dose levels — 25 possible actions.
- **The reward:** survival at 90 days earned a reward, death a penalty, on a scale of −100 to +100.
- **Headline numbers:** in the 79,073-patient external test set, the estimated value of the clinicians' actual treatment was 56.9 (interquartile range 54.7–58.8) versus 84.5 (84.3–87.7) for the AI policy. The AI would have used vasopressors 30% of the time versus the 17% clinicians actually used. Doctors matched the AI's vasopressor dose 58% of the time and its fluid dose about 36% of the time; when they deviated, they gave *less* vasopressor 75% of the time, with a median shortfall of 0.13 µg/kg/min.
- **Funding / conflicts:** NIHR Biomedical Research Centre support. Competing interests are substantial and disclosed: Gordon reports speaker fees from Orion and Amomed, consulting for Ferring, Tenax, Baxter, Bristol-Myers Squibb and GSK, and institutional grants; Celi receives funding from Philips Healthcare; Badawi **is an employee of Philips Healthcare**; Faisal has received funding from Fresenius-KABI; Komorowski declares none.
- **Reproducibility:** MIMIC-III is open, but the eRI test database is **restricted to Philips' own research institute**, and code is available only on request.

# How Strong Is This Evidence?

**Grade: 3/5 — an unusually careful piece of machine-learning engineering, wrapped around one claim its design cannot support.**

The methodological care is real and I under-rated it before reading the full text. They didn't just report a favorable estimate: they built 500 candidate models and deliberately selected the one that maximized the *lower* bound of a 95% confidence interval — a conservative, safety-first criterion. They benchmarked against a random policy and a do-nothing policy, checked that their model's value scores actually tracked observed mortality (calibration), and tested on 79,073 patients from 128 hospitals that contributed nothing to training. That is a stronger design than most AI papers of its era.

What holds the grade at 3 is the gap between what was measured and what is claimed. The AI's superiority is an *estimate* of what would have happened under a strategy nobody used, resting on a statistical assumption that later work showed is violated for some patients. The mortality-versus-agreement finding is observational and confounded. And a detail the authors disclose but that deserves italics: **the AI could see laboratory values that were not yet available to the clinicians making the real decisions.** Some of its apparent advantage is time travel, not insight.

# The Editor's Concerns

- **"Mortality was lowest when doctors matched the AI" still does not mean matching the AI saves lives.** The full text confirms this is an association across patients, not an experiment. Doctors deviate most from any standard pattern when patients are crashing or atypical — and those patients die more often regardless. Concordance may be a *marker* of a straightforward patient rather than a *cause* of survival. This is confounding by indication (Statistics Spotlight), and the design cannot exclude it.
- **The AI saw labs the doctors hadn't gotten back yet.** The authors list this plainly: "some laboratory values would not have been immediately available to clinicians to inform decision-making but were available to the AI Clinician." A comparison in which one side has later information is not a fair contest, and this is not a minor caveat — it goes to the core "AI beat clinicians" framing.
- **The outcome changed between training and testing.** The model was optimized for 90-day survival in MIMIC-III, but 90-day mortality was unavailable in eRI, so *hospital* mortality was substituted. The validation therefore scores a policy on a different outcome than the one it was trained to maximize.
- **The value estimate rests on an assumption later shown to fail here.** Weighted importance sampling requires that the AI's recommended actions actually appear in the historical data (overlap). Matsson & Johansson (arXiv:2111.11113) found the AI Clinician recommending fluids for a patient group physicians usually left untreated — "a rare action under the behavior policy" — concluding "the data may not support evaluating the AI Clinician for this prototype."
- **Crude representation of a subtle problem.** Patients were sorted into discrete clusters and treatment into 25 dose bins. Two patients in the same cluster get the same advice, and the paper's own recommendation of "more vasopressor" is a coarse instruction in a domain where timing and titration matter enormously.
- **The test set cannot be independently re-analyzed.** eRI access is restricted to Philips' research institute — and a Philips employee is a co-author, with a second author funded by Philips. The disclosure is proper; the structural problem is that the external validation others would most want to reproduce is the part they cannot access.
- **Selecting the model that maximizes a confidence bound is a double-edged sword.** It is a genuinely safety-conscious criterion, but choosing the best of 500 candidates on a bound and then reporting that bound is a form of selection — the winner's estimate is optimistically biased unless the selection is priced in.
- **What this study did well:** a real, unsolved clinical problem where practice genuinely varies; a large, fully independent external test set spanning 128 hospitals; conservative model selection; sanity-check baselines (random and zero-drug policies); an explicit calibration check; an interpretability analysis confirming the model keyed on sensible clinical variables; a candid limitations paragraph including the lab-timing asymmetry; and an unambiguous statement that "this work will clearly require prospective evaluation using real-time data and decision-making in clinical trials." Notably, the acknowledgements thank O. Gottesman — who a few months later co-authored, with this paper's own first author, the Nature Medicine comment "Guidelines for reinforcement learning in healthcare" (https://doi.org/10.1038/s41591-018-0310-5) urging exactly this caution.

# Statistics Spotlight

**1. Off-policy evaluation — grading a strategy nobody ever used.**
- *What it is:* You have records of what doctors did (the "behavior policy") and what happened. You want to know how a *different* strategy (the AI's "target policy") would have performed, without trying it on anyone. Weighted importance sampling does this by re-weighting each historical patient according to how likely the AI's strategy was to have produced the treatment they actually received.
- *How this paper used it:* This is the engine behind "56.9 for clinicians versus 84.5 for the AI." The authors used a high-confidence variant, bootstrapped the distribution 2,000 times, and — the careful part — picked the model maximizing the 95% *lower* bound rather than the best average, so their claim was "even pessimistically, the AI policy looks better."
- *The theory, with a worked example:* Imagine judging a new restaurant-picking strategy from a year of your friends' receipts. If your strategy picks places they often went, you have plenty of evidence and a stable estimate. If it picks somewhere they visited once, that single receipt must represent an entire pattern — it gets an enormous weight, and your whole estimate swings on one dinner. The formal requirement is **overlap** (positivity): the new strategy must mostly recommend things the data actually contains. Where it doesn't, the estimate isn't just uncertain — it's unsupported.
- *Watch out:* Off-policy values are routinely read as if they were measured outcomes. They are model-based extrapolations that fail hardest exactly when the new policy is genuinely novel — which is when you most wanted to learn something. Ask: was overlap checked, and were confidence intervals reported? This paper did report intervals and chose conservatively; independent work still found overlap violations for some patient groups.

**2. Confounding by indication — why "agreement tracked survival" is a trap.**
- *What it is:* In observational medical data, treatment is chosen *because of* how sick the patient is. So treatment and outcome are linked through severity even when the treatment does nothing at all. The clinician's judgment is the hidden variable driving both.
- *How it applies here:* Patients whose doses matched the AI had the lowest mortality, with a dose-dependent gradient. But no doctor was consulting the AI — they were responding to patients in front of them. Unusual doses cluster around unusual patients: the bleeding, the multi-organ-failure, the actively dying. Those patients die more often no matter what is prescribed.
- *The theory, with a worked example:* Hospital records will show that patients given intravenous adrenaline die far more often than those who aren't. Nobody concludes adrenaline is lethal — it's given during cardiac arrest. The drug *marks* the emergency; it didn't cause it. Identical logical shape, and it is the most common way observational treatment data gets misread.
- *Watch out:* The tell is any sentence shaped "outcomes were better among patients who received / matched / adhered to X" where nobody was randomized to X. Adherence, concordance, and matched-dose analyses are all vulnerable. The fix is randomization, or explicit causal methods with stated assumptions — and honest labeling as hypothesis-generating.

**3. Reward specification — the one number that defines "optimal."**
- *What it is:* Reinforcement learning maximizes a single scalar. "Optimal" in this paper's title means optimal *with respect to that number, given that data* — nothing broader.
- *How this paper used it:* Survival at 90 days, scored from −100 to +100. Everything else is invisible to the algorithm: kidney injury from fluid overload, limb or gut ischemia from vasopressors, ventilator days, delirium, long-term disability. Notably, the AI's central recommendation was *more vasopressor* — a drug class with real ischemic harms that the reward function simply does not price.
- *The theory, with an analogy:* Grade a delivery driver solely on packages-per-hour and you get speeding, skipped signatures and crushed boxes — not because the driver is reckless, but because those costs are unpriced. An RL agent is that driver, without the judgment to notice it is cheating.
- *Watch out:* Whenever you read "AI learned the optimal treatment," substitute "AI maximized the specific number the researchers chose," then ask what harms sit outside that number. It's the same failure mode as the Obermeyer paper's cost-as-a-proxy-for-health, reached by a different route.

# Jargon Translator

- **Sepsis:** severe infection causing life-threatening organ dysfunction; a leading cause of hospital death.
- **Vasopressor:** a drug that constricts blood vessels to raise dangerously low blood pressure; norepinephrine is the reference agent here.
- **Reinforcement learning:** machine learning for *sequences* of decisions, where each action changes what happens next — unlike the one-shot classifiers in your other papers.
- **Policy:** the rule mapping a patient's current state to the next action. "Clinicians' policy" = what doctors did; "AI policy" = what the model proposes.
- **Markov decision process:** the mathematical frame — states, actions, rewards — assuming the current state captures everything needed to decide the next action.
- **Value of a policy:** expected total reward from following it. Here an *estimate*, never a measurement.
- **Weighted importance sampling:** the re-weighting method used to produce that estimate.
- **MIMIC-III / eRI:** the two ICU databases — one open (Boston teaching hospital), one restricted to Philips (128 hospitals).
- **Calibration (here):** the check that treatments the model scored highly really did correspond to lower observed mortality.
- **Sepsis-3:** the 2016 international consensus definition of sepsis used to select patients.

# What You Can (and Can't) Say

**Fair to say:**
- "A 2018 Nature Medicine study derived sepsis fluid and vasopressor strategies by reinforcement learning from 17,083 ICU admissions, and estimated on 79,073 patients from 128 other hospitals that its strategy would score higher than clinicians' actual decisions."
- "It suggested doctors tend to give too much fluid and too little vasopressor in sepsis — an idea consistent with other critical-care literature, and worth testing."
- "The authors were explicit that prospective clinical trials are required before any clinical use."
- "It founded reinforcement learning in critical care and prompted the field to write formal validation guidelines."

**Not fair to say:**
- "AI found the optimal sepsis treatment" — optimal for one chosen number, estimated from historical data, never tested on a patient.
- "Following the AI's doses lowers mortality" — the dose-agreement gradient is observational and confounded by patient severity; this is precisely the claim the design cannot support.
- "The AI beat doctors" — it beat an estimate of doctors, while having access to lab results the doctors did not yet have.
- "It was validated externally, so it works" — the external test scored a different outcome (hospital rather than 90-day mortality) on a database only the sponsoring company can access.

# Bottom Line for Your Life

If you meet the headline "AI treats sepsis better than doctors," this is the paper behind it, and the real story is more interesting. Researchers taught a machine to propose fluid and vasopressor doses from a mountain of past ICU records, tested it carefully — 128 hospitals, conservative model selection, sanity-check baselines — and *estimated* that its strategy would do better, while noticing that patients whose care happened to resemble its advice survived more often. Nobody was treated by it, the estimate depends on an assumption later shown to fail for some patients, and the machine could see lab results the doctors were still waiting on. The two portable lessons: when a study says a strategy "would have" worked better, ask how anyone could know; and when outcomes are better among people who *matched* something, ask who those people were before they matched. One study is one data point, and this one is a landmark of ambition rather than of proof. This is an educational breakdown, not medical advice — sepsis is an emergency, and its treatment belongs to the clinicians at the bedside.

---

## What the full text changed

The earlier abstract-only version of this entry was directionally right but under-informed. Reading the paper:

- **Raised the grade from 2/5 to 3/5.** The abstract hid genuinely conservative methodology: 500 candidate models with selection on a 95% confidence *lower* bound, random and zero-drug baselines, an explicit calibration check, and a 79,073-patient external test set across 128 hospitals.
- **Filled in every "not reported" gap:** cohort sizes, the 48 variables, the 4-hour steps, the 25-action grid, the 90-day-survival reward on a −100/+100 scale, and the effect sizes (56.9 versus 84.5).
- **Surfaced three concerns invisible from the abstract:** the AI had access to lab values clinicians did not yet have; the training outcome (90-day mortality) differed from the validation outcome (hospital mortality); and the competing interests are substantial, with a Philips employee among the authors and the external test database restricted to Philips.
- **Confirmed the authors' own caution** — they state prospective trials are required, and they list the lab-timing asymmetry themselves.

A good argument for the full-text-first rule: the abstract oversold the claim and undersold the rigor, in both directions at once.

---

**Sources** (identifiers verified against the live PubMed/NLM record; full text from the published PDF supplied by the user. URL browsing is blocked in this environment, so links are constructed from the verified record):
- DOI (closed access): https://doi.org/10.1038/s41591-018-0213-5
- PubMed: https://pubmed.ncbi.nlm.nih.gov/30349085/
- Related, verified: Gottesman, Johansson, Komorowski et al. "Guidelines for reinforcement learning in healthcare." Nature Medicine 2019;25(1):16–18. https://doi.org/10.1038/s41591-018-0310-5
- Related, verified: Matsson & Johansson, "Case-based off-policy policy evaluation using prototype learning" (2021), reporting overlap failures when evaluating the AI Clinician: https://doi.org/10.48550/arxiv.2111.11113
