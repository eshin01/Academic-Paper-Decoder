# The Artificial Intelligence Clinician learns optimal treatment strategies for sepsis in intensive care

- **Authors:** Matthieu Komorowski (Imperial College London / Harvard-MIT), Leo A. Celi (MIT, Beth Israel Deaconess), Omar Badawi (MIT; Philips Healthcare eICU R&D; Univ. of Maryland), Anthony C. Gordon (Imperial), A. Aldo Faisal (Imperial)
- **Venue:** Nature Medicine, 2018;24(11):1716–1720 (published October 22, 2018)
- **DOI link:** https://doi.org/10.1038/s41591-018-0213-5
- **PubMed link:** https://pubmed.ncbi.nlm.nih.gov/30349085/ (PMID 30349085)
- **Full-text link:** none — the paper is closed access, has no PubMed Central version, and the publisher page is unreachable from this environment. No full-text link is given rather than an unverified one.
- **Basis:** ABSTRACT ONLY for the primary paper, supplemented by **verified secondary sources** that describe or critique its methods (each attributed inline below). Identifiers verified against the live PubMed/NLM record. Numbers not present in the retrieved text are marked "not reported in the text retrieved" — notably the cohort sizes, the reward definition, and the funding/conflict statement.
- **Decoded:** 2026-09-04

---

# The Gist

Sepsis — the body's overwhelming, organ-damaging response to infection — is the third leading cause of death worldwide, and doctors still disagree about how much intravenous fluid and how much blood-pressure-raising medication (vasopressors) to give, and when. This team built an AI that learned from a huge archive of past intensive-care records, watching what doctors did and what happened next, and worked out its own dose strategy. The authors report that the AI's recommended treatment scored better on average than what real doctors did — and that patients whose doctors happened to prescribe doses close to the AI's suggestion had the lowest death rates. That last sentence is the paper's most quoted line and its most fragile one, for reasons the Editor's Concerns explain.

# Study Snapshot

- **Study type:** A retrospective reinforcement-learning study on existing intensive-care records — a computational study, not a trial. No patient was ever treated according to the AI. This sits low on the evidence ladder for treatment claims: it can generate a hypothesis about better dosing, not establish one.
- **What the AI decided:** how much intravenous fluid and how much vasopressor to give, repeatedly over time, as the patient's condition changed. According to later papers that rebuilt the method (SepsisAgent, arXiv 2026, and Matsson & Johansson, arXiv 2021), the AI Clinician worked in 4-hour time steps with a 5×5 grid of dose levels for the two drugs, learning from the MIMIC-III intensive-care database.
- **Number of patients (n):** not reported in the text retrieved. The abstract describes "an amount of patient data that exceeds by many-fold the life-time experience of human clinicians" and "a large validation cohort independent of the training data," without figures in the retrieved text.
- **How it was judged:** by estimating the *value* of the AI's strategy from historical records (see Statistics Spotlight), plus the observed link between doctor–AI dose agreement and patient survival.
- **Main claims:** the AI's chosen treatment had "on average reliably higher" value than clinicians'; mortality was lowest where actual doses matched AI recommendations.
- **Funding / conflicts:** not reported in the text retrieved; PubMed tags non-US-government research support. Worth noting: one author was affiliated with Philips Healthcare's eICU division, a commercial critical-care data business.

# How Strong Is This Evidence?

**Grade: 2/5 — a genuinely important idea whose headline evidence is far weaker than its framing.**

Be careful to separate two things. As a *scientific milestone*, this paper is major: it was the first serious demonstration that reinforcement learning — the technique behind game-playing AI — could propose sequential treatment plans from real intensive-care data, and it launched an entire subfield. But as *evidence that following this AI would help patients*, it is weak, for three stacked reasons. Nobody was treated by it. Its main performance number comes from estimating what *would have* happened under a strategy never actually used — a method whose reliability for exactly this study has been formally questioned in the peer-reviewed literature. And its most memorable finding, that agreement with the AI tracked survival, is a correlation in observational data with an obvious alternative explanation. The senior team clearly knew the terrain: co-author Komorowski went on to co-write a Nature Medicine comment titled "Guidelines for reinforcement learning in healthcare" (Gottesman, Johansson, Komorowski et al., 2019; https://doi.org/10.1038/s41591-018-0310-5) urging exactly this kind of caution.

# The Editor's Concerns

- **"Mortality was lowest when doctors matched the AI" does not mean matching the AI saves lives.** This is the sentence that gets cited, and it is observational. Doctors deviate most from any standard dosing pattern when patients are sickest, crashing, or complicated — and those patients die more often regardless of what anyone prescribes. Agreement with the AI may simply mark "a patient whose course was typical," which is itself a survival predictor. This is textbook **confounding by indication** (see Statistics Spotlight), and the study design cannot rule it out.
- **The core performance estimate is contested.** Judging a treatment policy from records generated by *different* decisions requires statistical reweighting that becomes unreliable when the AI recommends actions doctors rarely took. A later peer-reviewed analysis found precisely this failure for the AI Clinician: Matsson & Johansson (arXiv:2111.11113) report a "lack of overlap" between the AI Clinician's suggested actions and what physicians actually did — for one patient group, the AI recommended intravenous fluids where physicians usually gave no treatment at all, "a rare action under the behavior policy," so those cases receive extreme statistical weights and, in their words, "the data may not support evaluating the AI Clinician for this prototype."
- **The AI can only learn what was already tried.** It never explores; it re-weights history. Genuinely better strategies that no clinician in the dataset attempted are invisible to it, and any systematic habits of those clinicians — good or bad — are baked into what it learned.
- **A single scalar reward compresses all of medicine.** Reinforcement learning needs one number to maximize. The reward definition is not reported in the text retrieved, but any such choice (typically survival at a fixed horizon) silently discounts everything else: kidney injury from fluid overload, limb ischemia from vasopressors, ventilator days, long-term disability. This is the same proxy-label trap that made the Obermeyer algorithm (your entry #4) biased.
- **Nothing prospective.** No deployment, no trial, no patient outcomes under AI guidance — the gap between "estimated value is higher" and "patients do better" is the entire distance to clinical usefulness.
- **Abstract-only appraisal.** Because the full paper is paywalled, cohort sizes, sensitivity analyses, and the authors' own stated limitations could not be checked here. Abstracts systematically present results at their most favorable; a full-text read would likely surface caveats the authors themselves stated.
- **What this study did well:** it took on a real, unsolved clinical problem where practice genuinely varies; it used an independent validation cohort rather than testing on training data; it framed its output as "individualized and clinically interpretable" decision support rather than autonomous control; and its authors participated openly in the methodological self-criticism that followed, which is how a field is supposed to work.

# Statistics Spotlight

**1. Off-policy evaluation — grading a strategy that was never actually used.**
- *What it is:* The central problem of this whole genre. You have records of what doctors did (the "behavior policy") and what happened. You want to know how well a *different* strategy (the AI's "target policy") would have done — without ever trying it. Off-policy evaluation estimates that, most commonly by **importance sampling**: re-weighting each historical patient by how likely the AI's strategy was to have produced the treatment that patient actually received.
- *How this paper used it:* This is the machinery behind "the value of the AI Clinician's selected treatment is on average reliably higher than human clinicians." No patient received AI-directed care; the comparison is an estimate reconstructed from the doctors' own data.
- *The theory, with a worked example:* Imagine judging a new restaurant-picking strategy using a year of your friends' dinner receipts. If your strategy would pick the same places they usually pick, you have plenty of relevant receipts and your estimate is solid. But if it recommends a restaurant they visited once, that single receipt must stand in for a whole pattern — so it gets an enormous weight, and your estimate swings wildly on one dinner. Formally, you need **overlap** (also called positivity): the target strategy must mostly recommend things the historical data actually contains examples of. Where it doesn't, the estimate is not merely uncertain — it is unsupported.
- *Watch out:* Off-policy value estimates are routinely reported as if they were measured outcomes. They are model-based extrapolations that quietly fail when the new policy is genuinely novel — which is exactly when you were hoping to learn something. Ask any RL-in-medicine paper: what fraction of recommended actions had real support in the data, and were confidence intervals reported around the value estimate? For this paper, the independent analysis cited above found the overlap condition violated for some patient groups.

**2. Confounding by indication — why "agreement tracked survival" is a trap.**
- *What it is:* In observational medical data, the treatment a patient receives is *chosen because of* how sick they are. So treatment and outcome are linked through severity, even when the treatment itself does nothing. The chooser's judgment is the hidden variable.
- *How it applies here:* Patients whose doctors' doses matched the AI had the lowest mortality. But the doctors weren't consulting the AI — they were responding to patients. Unusual doses cluster around unusual patients: the crashing, the bleeding, the multi-organ-failure cases. Those patients die more often no matter what. Concordance with a typical-looking policy may be a *symptom* of being a more stable patient, not a *cause* of surviving.
- *The theory, with a worked example:* Hospitals could show that patients who receive intravenous adrenaline die far more often than those who don't. Nobody concludes adrenaline kills people — it's given during cardiac arrest. The drug marks the emergency; it didn't create it. Same logical shape, and it is the single most common way observational treatment data gets misread.
- *Watch out:* The tell is any sentence of the form "outcomes were better among patients who received / matched / adhered to X" in a study where nobody was randomized to X. Adherence, concordance, and "matched-dose" analyses are all vulnerable. The fix is randomization — or, failing that, explicit causal-inference methods with stated assumptions, and honest labeling of the finding as hypothesis-generating.

**3. Reward specification — the one number that defines "optimal."**
- *What it is:* Reinforcement learning maximizes a scalar reward. The word "optimal" in this paper's title means *optimal with respect to that number, given that data* — nothing more.
- *How it applies here:* The exact reward is not reported in the text retrieved, but the design necessarily compresses a complex clinical goal into one signal. Everything left out of the reward is, to the algorithm, free.
- *The theory, with an analogy:* Tell a delivery driver they are graded solely on packages-per-hour, and you will get speeding, skipped signatures, and damaged boxes — not because the driver is malicious, but because those costs are unpriced. An RL agent is that driver, without the human judgment to know it's cheating.
- *Watch out:* Whenever you read "AI learned the optimal treatment," substitute "AI maximized the specific number the researchers chose." Then ask what plausible harms lie outside that number. This is the same lesson as Obermeyer's cost-as-a-proxy-for-health failure, arriving through a different door.

# Jargon Translator

- **Sepsis:** the body's dysregulated, organ-damaging response to an infection; a leading cause of hospital death, treated urgently with fluids, antibiotics, and blood-pressure support.
- **Vasopressor:** a drug that tightens blood vessels to raise dangerously low blood pressure.
- **Reinforcement learning:** a machine-learning approach where an agent learns a *sequence* of actions by seeing which sequences ended well — the technique behind game-playing AI. Distinct from the pattern-classifiers in your other papers, because each decision changes what happens next.
- **Policy:** in reinforcement learning, the rule mapping a patient's current state to the next action. The "behavior policy" is what clinicians actually did; the "target policy" is what the AI proposes.
- **Value (of a policy):** the expected total reward from following that policy — here, an estimate, not a measurement.
- **MIMIC-III:** a large, freely available de-identified intensive-care database from a Boston hospital, used to train the model according to later papers that rebuilt it.
- **Retrospective:** analyzing records of events that already happened, rather than following patients forward.
- **Hypothesis-generating:** a finding strong enough to justify a proper trial, not strong enough to change practice.

# What You Can (and Can't) Say

**Fair to say:**
- "A 2018 Nature Medicine study used reinforcement learning to derive sepsis fluid and vasopressor strategies from intensive-care records, and estimated that its strategy would outperform clinicians' actual decisions."
- "It is the founding paper for reinforcement learning in critical care, and it prompted the field to write formal guidelines about how such work should be validated."
- "Its authors framed the output as interpretable decision support, and the follow-up literature — including work co-authored by this paper's own author — has been candid about the limits of the evaluation method."

**Not fair to say:**
- "AI found the optimal sepsis treatment" — optimal with respect to one chosen number, estimated from historical data, never tested on a patient.
- "Following the AI's doses lowers mortality" — the survival association is observational and confounded by how sick patients were; it is exactly the claim the design cannot support.
- "The AI beat doctors" — its strategy scored higher on an estimate, not in a comparison where anyone was treated either way.
- "This is ready for the ICU" — no prospective evaluation, and independent analyses have questioned whether its performance estimate is supportable for some patients.

# Bottom Line for Your Life

If you ever see a headline like "AI knows how to treat sepsis better than doctors," this is usually the paper behind it — and the honest version is far more interesting than the headline. Researchers taught a machine to propose dosing strategies from a mountain of past ICU records, then estimated (not measured) that its strategies looked better, and noticed that patients whose care resembled the AI's advice survived more often — a pattern that has at least one very ordinary explanation. Nobody was treated by this AI. The two transferable lessons: when a study says a strategy "would have" worked better, ask how they could possibly know; and when a study says outcomes were better among people who *matched* something, ask who those people were before they matched. One study is one data point, and this one is a landmark of ambition rather than of proof. This is an educational breakdown, not medical advice — sepsis is a medical emergency, and its treatment belongs to the clinicians at the bedside.

---

**Sources** (primary identifiers verified against the live PubMed/NLM record; secondary sources verified via Scite. URL browsing is blocked in this environment, so links are constructed from those verified records):
- DOI (primary paper, closed access): https://doi.org/10.1038/s41591-018-0213-5
- PubMed: https://pubmed.ncbi.nlm.nih.gov/30349085/
- Full text: not obtainable — closed access, no PMC version, publisher unreachable from this environment
- Related, verified: Gottesman, Johansson, Komorowski et al. "Guidelines for reinforcement learning in healthcare." Nature Medicine 2019;25(1):16–18. https://doi.org/10.1038/s41591-018-0310-5
- Related, verified: Matsson & Johansson. "Case-based off-policy policy evaluation using prototype learning" (2021), which reports overlap failures when evaluating the AI Clinician: https://doi.org/10.48550/arxiv.2111.11113
