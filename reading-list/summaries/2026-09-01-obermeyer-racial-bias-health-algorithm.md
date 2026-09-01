# Dissecting racial bias in an algorithm used to manage the health of populations

- **Authors:** Ziad Obermeyer (UC Berkeley / Brigham and Women's), Brian Powers (Brigham and Women's), Christine Vogeli (Massachusetts General), Sendhil Mullainathan (University of Chicago Booth)
- **Venue:** Science, 2019;366(6464):447–453 (published October 25, 2019)
- **DOI link:** https://doi.org/10.1126/science.aax2342
- **PubMed link:** https://pubmed.ncbi.nlm.nih.gov/31649194/ (PMID 31649194)
- **Full-text access:** gold open access via the publisher (use the DOI link); no PubMed Central version exists
- **Basis:** ABSTRACT + RETRIEVED FULL-TEXT EXCERPTS — analyzed from the PubMed abstract plus open-access full-text passages retrieved via Scite (results, methods, and discussion sections). Not the complete paper: exact total sample size and funding/COI statements were not in the retrieved text. Identifiers verified against the live PubMed/NLM record; direct URL browsing is blocked in this environment, so links are constructed from that verified record.
- **Decoded:** 2026-09-01

---

# The Gist

A widely used commercial algorithm helps US health systems decide which patients get extra care — nurse teams, more appointments, closer follow-up. This study got rare access to how one such algorithm actually works and found it was systematically biased against Black patients: at the same risk score, Black patients were considerably sicker than White patients. The reason wasn't racist code — the algorithm never even saw race. It predicted future healthcare *costs* as a stand-in for future health *needs*. Because less money gets spent on Black patients (a symptom of unequal access, not lesser need), the algorithm learned to see them as healthier than they are. Fixing it would nearly triple the share of Black patients flagged for extra help, from 17.7% to 46.5%.

# Study Snapshot

- **Study type:** A retrospective algorithmic audit — researchers analyzed a real, deployed commercial algorithm's scores against patients' actual health records, then simulated fixes. Observational (no experiment on patients), but with unusual access to a real system affecting, per the authors, millions of patients.
- **Setting:** patients at one large academic health system whose data feeds the algorithm; 11.9% of the sample was Black. The exact total number of patients is not reported in the text retrieved.
- **How the program worked:** patients above the 97th percentile of algorithm risk score were auto-flagged for the care program (1.3% of the sample ended up enrolled); above the 55th percentile, flagged for screening.
- **What was measured:** health (number of active chronic conditions, plus biomarkers like blood-sugar control) of Black vs. White patients *at the same algorithm score*.
- **Key findings:** at equal risk scores, Black patients carried a significantly heavier illness burden. Under an unbiased ranking, Black patients would be 46.5% of those auto-flagged rather than 17.7%. When the authors retrained the model to predict health instead of cost alone — same data, same methods, different target — excess unrecognized illness in Black patients dropped by 84%.
- **Funding / conflicts:** not reported in the text retrieved (PubMed tags non-US-government research support).
- **Impact:** per Scite, over 7,000 papers have cited this study — it effectively created the field of algorithmic-bias auditing in healthcare.

# How Strong Is This Evidence?

**Grade: 4/5 — an unusually rigorous audit that found the mechanism, not just the disparity, and proved a fix.**

Most bias studies stop at "the outputs look unfair." This one went three steps further: it showed the disparity against objective health measures (chronic conditions and lab-based biomarkers, not opinions); it identified the precise cause (predicting cost as a proxy for health); and it demonstrated repair — retraining with a better target variable cut the bias by 84% using the same data and methods. It also checked and ruled out alternative explanations, like the care program itself changing the health measures. What keeps it from a 5: it's an observational analysis of one algorithm at one health system (though the authors show the cost-prediction approach is industry-standard), the exact sample size and some details weren't in the text retrieved here, and the headline "17.7% to 46.5%" is a simulation of what *would* happen — the study didn't deploy the fix and follow real patients.

# The Editor's Concerns

- **One health system.** The audit used data from a single large academic health system. The mechanism plausibly generalizes — the authors note a Society of Actuaries review scored the 10 leading algorithms by how well they predict *cost* — but the exact size of the bias elsewhere is unmeasured here.
- **The fix is simulated, not deployed.** The 17.7%→46.5% figure and the 84% bias reduction come from re-ranking and retraining exercises on historical data, not from a rolled-out program with patient outcomes.
- **Health is hard to measure too.** The study measures illness through recorded chronic conditions and lab values — which require healthcare contact to be recorded. If under-served patients have under-documented illness, the true bias would be even *larger* than reported; the direction favors the authors' conclusion, but the measurement limit is worth knowing.
- **The algorithm is unnamed in the text retrieved,** and architecture details are proprietary — independent re-analysis depends on similar special access.
- **Funding and conflict-of-interest statements were not in the text retrieved** for this analysis.
- **What this study did well:** rare direct access to a real commercial algorithm's inputs and outputs; objective, biomarker-backed health measures instead of subjective ones; a clean causal story tested against alternatives (the algorithm excluded race, yet bias emerged anyway — pinpointing the cost label as the culprit); a demonstrated, practical repair; and framing the lesson generally — the same proxy-label trap operates in credit scoring, policing, and hiring algorithms.

# Statistics Spotlight

**1. Calibration bias — the test at the heart of this paper.**
- *What it is:* A prediction tool is "calibrated across groups" if people with the same score have the same actual outcome, regardless of group. Formally the paper checks whether average health at a given risk score is equal for Black and White patients (E[Y|R,B] = E[Y|R,W]).
- *How this paper used it:* It lined up Black and White patients *at the same algorithm score* and compared their real illness burden. Equal scores should mean equal sickness. Instead, Black patients at any given score had significantly more chronic conditions and worse biomarkers — the definition of calibration failure with respect to health.
- *The theory, with an analogy:* Imagine two bathroom scales, one used by group A and one by group B. Both display "150 lbs" often — but group B's scale reads 150 when the person actually weighs 170. Any decision made "fairly" off the displayed number (same cutoff for everyone) still systematically shortchanges group B. Conditioning on the score is the trick: overall accuracy can look fine while the same score means different realities for different groups.
- *Watch out:* Researchers have proven that several intuitive fairness definitions (calibration, equal error rates, equal selection rates) generally *cannot all hold at once*. So when a vendor says "our algorithm is fair," always ask: fair by which definition, measured against which outcome? This paper's answer — calibrated against actual health — is the one that mattered for the decision being made.

**2. Proxy (label-choice) bias — how an algorithm becomes biased without ever seeing race.**
- *What it is:* Machine learning must predict something concrete. When the thing you care about (health need) is hard to measure, developers substitute a convenient proxy (healthcare cost). If the proxy is systematically distorted for one group, the algorithm inherits — and automates — that distortion.
- *How this paper used it:* The algorithm predicted cost, and predicted it *well* — its top-3% flagged patients generated 16.5% of all costs, beating a health-based predictor's 12.1% on that metric. But because unequal access means less money is spent on Black patients at the same level of sickness, "low predicted cost" got silently translated into "low need."
- *The theory, with a worked example:* Take two patients with identical severe diabetes. One has good access and generates $10,000 in yearly care; the other faces barriers and generates $5,000. Train a model to predict spending and it will confidently rank the second patient as half as needy — and it will be *right about the dollars*, which is exactly the problem. The model aces the wrong exam.
- *Watch out:* "The algorithm doesn't use race" is the most common defense of automated systems — and this paper is the definitive demonstration that it means very little. The bias arrived through the choice of *what to predict*, not through any input variable. When you see any algorithmic ranking (risk scores, credit scores, hiring screens), the first question is: what proxy is it actually trained to predict, and for whom is that proxy distorted?

**3. Threshold effects and counterfactual simulation — turning a bias into a number people can act on.**
- *What it is:* Programs run on cutoffs (here, the 97th percentile of risk score auto-flags you). A modest scoring bias becomes a large real-world exclusion at the threshold. A counterfactual simulation re-runs history under a corrected rule to quantify the difference.
- *How this paper used it:* The authors re-ranked patients as an unbiased score would, and counted who would cross the 97th-percentile line: the Black share of auto-flagged patients rose from 17.7% to 46.5%. They also retrained the model with a health-plus-cost target, cutting excess unrecognized chronic illness in Black patients by 84%.
- *The theory, with an analogy:* Think of a race where one group's stopwatches secretly run fast. In the middle of the pack it barely matters — but if only the top 3% qualify for the final, the stopwatch error decides who makes the cut. Cutoff-based systems amplify small measurement biases into all-or-nothing consequences.
- *Watch out:* Simulated gains are the *best case* — they assume the fix works as modeled and nothing else changes. They're powerful for showing a problem's size, but only a deployed, evaluated program proves real-world benefit. Distinguish "would increase to 46.5% in simulation" from "did increase."

# Jargon Translator

- **Care management program:** extra support (dedicated nurses, more appointments, coordination) that health systems give their highest-need patients.
- **Risk score:** the algorithm's single number summarizing how much care a patient is predicted to need.
- **Percentile:** your rank on a 0–100 scale; the 97th percentile means scoring higher than 97% of people.
- **Comorbidity score / active chronic conditions:** a count of a patient's ongoing illnesses (diabetes, high blood pressure, kidney disease…), a standard overall-sickness measure.
- **Biomarker:** an objective lab measurement of disease severity, like blood-sugar control in diabetes.
- **Proxy / label:** the measurable stand-in variable an algorithm is trained to predict in place of the thing you actually care about.
- **Holdout set:** data kept aside from training, used to test predictions honestly.
- **Algorithmic audit:** independently examining a deployed algorithm's real behavior for accuracy, bias, or harm.

# What You Can (and Can't) Say

**Fair to say:**
- "A landmark 2019 Science study showed a widely used healthcare algorithm was racially biased: at the same risk score, Black patients were significantly sicker than White patients."
- "The bias came from predicting healthcare costs as a stand-in for health needs — the algorithm never used race at all."
- "In the study's simulation, an unbiased version would raise the share of Black patients flagged for extra care from about 18% to about 47%, and retraining on a better target cut the bias by 84%."
- "This is the study that made 'what is your algorithm actually trained to predict?' a standard question in healthcare AI."

**Not fair to say:**
- "The algorithm's makers deliberately discriminated" — the mechanism was a reasonable-seeming design choice with unexamined consequences, which is precisely the paper's warning.
- "Removing race from algorithms prevents bias" — this algorithm had no race variable and was biased anyway.
- "All healthcare algorithms shortchange Black patients by this amount" — one algorithm, one health system was measured; the *mechanism* generalizes, the exact numbers may not.
- "The problem was fixed" — the paper demonstrated a fix in simulation; whether deployed systems corrected course is a separate question this study doesn't answer.

# Bottom Line for Your Life

This paper is the clearest real-world lesson that an algorithm can be precisely accurate and deeply unfair at the same time — because someone chose a convenient target (dollars spent) as a stand-in for the thing that mattered (health). That trap isn't unique to medicine: credit scores, hiring screens, and policing tools all train on proxies that carry society's existing inequalities. When anyone cites an algorithm's "accuracy," the question this study teaches you to ask is: accurate *at predicting what, for whom*? One study is one data point, but this one reshaped how an entire industry — and regulators — think about automated decisions in healthcare. This is an educational breakdown, not medical advice.

---

**Sources** (based on articles retrieved from PubMed and full-text passages retrieved via Scite; identifiers verified against the live PubMed/NLM record — URL-level browsing is blocked in this environment, so links are constructed from that verified record):
- DOI (open access at publisher): https://doi.org/10.1126/science.aax2342
- PubMed: https://pubmed.ncbi.nlm.nih.gov/31649194/
