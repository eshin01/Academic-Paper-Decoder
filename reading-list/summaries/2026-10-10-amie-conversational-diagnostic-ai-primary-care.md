# An AI Talked to 100 Real Patients. A Doctor Watched Every Word.

**Paper:** Conversational diagnostic artificial intelligence in ambulatory primary
care: a prospective feasibility study
**Authors:** Brodeur PG, Koshy JM, Palepu A, Saab K, Homiar A, Ruparel R, Wu C,
Tanno R, … Cohen ML, Natarajan V, Schaekermann M, Karthikesalingam A, Rodman A
(Google Research; Google DeepMind; Beth Israel Deaconess Medical Center; Beth
Israel Lahey Health; Harvard Medical School; Massachusetts General Hospital)
**Venue / Year:** The Lancet, published online 2026-10-08
**DOI:** https://doi.org/10.1016/S0140-6736(26)01535-7
**PubMed:** https://pubmed.ncbi.nlm.nih.gov/42849491/
**Preprint read for detail:** arXiv:2603.08448v3, "A prospective clinical
feasibility study of a conversational diagnostic AI in an ambulatory primary care
clinic" (15 March 2026) — https://arxiv.org/abs/2603.08448
**Registration:** ClinicalTrials.gov **NCT06911398**, pre-registered. IRB
2024P000095 (BIDMC Committee on Clinical Investigations, FWA00003245).
**Funding:** Alphabet.

**Basis of this analysis — a two-document reading, as with entry 40.** The Lancet
article is the peer-reviewed publication and its **abstract only** was available:
the full text is paywalled and there is no PubMed Central copy. That abstract was
retrieved from the live PubMed record and verified there on 2026-10-10. The
**arXiv preprint from the same team** was read in full, including its result
tables, via the alphaXiv index. **Every number below comes from the arXiv
preprint unless explicitly attributed to the Lancet abstract**, and one genuine
difference between the two documents is flagged in the concerns section. The
pages retrieved did not include Appendix Tables A.5 to A.11, so the full survey
response distributions, the per-item GAAIS means, the turn-level reasoning
analysis and the TRIPOD-LLM checklist are marked as not available where they
come up.
**Date decoded:** 2026-10-10
**Evidence grade:** 4/5

Chosen today as the queued top priority, flagged yesterday as the week's most
significant medical-AI paper: the first prospective deployment of a conversational
diagnostic AI with real patients in real primary care appointments.

---

# The Gist

Every AI-talks-to-patients study this list has seen involved actors. Trained
people pretending to have chest pain, so that if the AI said something dangerous
nobody got hurt. This is the first one where the patients were real, the
complaints were real, and the appointment afterwards was a real appointment.

Here is the design. At a busy primary care practice in Boston, patients who had
already booked an urgent care visit — and who clinic staff had already decided did
**not** need the emergency department — were invited to chat with an AI called
AMIE, by text, in the days before their appointment. AMIE took a history, asked
follow-up questions it chose itself, summarised back what it had understood,
and then told the patient some possible diagnoses and things their doctor might
want to discuss. The transcript and a summary went to the doctor before the
visit.

And a board-certified physician watched **every single conversation in real
time**, by video call with screen sharing, with four pre-agreed criteria for
cutting the chat off: immediate concern of harm to self or others, significant
emotional distress caused by the AI, potential clinical harm the supervisor
spotted, or the patient asking to stop. Seven physicians took turns. Immediately
afterwards, the supervisor came on the call and debriefed the patient, correcting
any errors.

**Zero stops were required across all 100 completed conversations.**

That is the headline, and it is a real result. But read it the way a statistician
would: zero events in 100 tries does not mean the rate is zero. It means the true
rate could be anything up to about **3 in 100** and you would still probably have
seen zero. The paper puts confidence intervals on its diagnostic accuracy and on
its blinding check. It does not put one on this.

The rest is more interesting than the headline.

**AMIE's diagnosis list was good.** Checked against the real final diagnosis from
an eight-week chart review, AMIE's ranked differential contained the right answer
in **88 of 98 cases (90%)** — within its first **seven** guesses. Within three
guesses, 73 of 98 (**75%**). Its single best guess was right in **55 of 98
(56%)**. The Lancet abstract quotes the 90% and the 75% top-3. It does not say
the 90% is top-seven, and it does not mention the 56%.

**Physicians could not tell AMIE's work from a doctor's.** Clinical evaluators
reviewing blinded differentials and management plans guessed the source correctly
**59.18% of the time (95% CI 49.45% to 68.91%)**. That interval contains 50%, so
they were guessing. This is the single best piece of method in the paper, and
almost nobody does it.

**Where AMIE lost, it lost on the practical stuff.** Physicians' management plans
were rated significantly better for **practicality** (p=0.003) and **cost
effectiveness** (p=0.004). No detectable difference on the quality of the
differential (p=0.6), or the appropriateness (p=0.1) or safety (p=1.0) of the
plan. And here the rating tables say something the p-values hide: AMIE drew at
least one "unfavourable" rating on **all five** criteria, while the physicians
drew zero on all four management-plan criteria. The middle of the two
distributions matched. The tails did not.

**Patients were more positive about AI afterwards** (p<0.001), and stayed that
way after seeing their doctor. They also rated AMIE noticeably lower than the
physicians did — and the two things they were least warm about were whether
their information would stay confidential and whether the AI was honest and
trustworthy.

And one number that deserves more attention than it will get: **12 of the 114
people who started a conversation never finished one**, because of technical
problems or the system being unavailable. One in ten.

# Study Snapshot

- **Study type:** **Prospective, single-arm feasibility study.** Pre-registered.
  No control group, by design.
- **Setting:** Healthcare Associates, part of Beth Israel Deaconess Medical
  Center, Boston — an academic primary care practice with 56 attending
  physicians, 110 residents, 15 nurse practitioners and about 40,000 patients.
  **April to November 2025.**
- **The AI:** AMIE (Articulate Medical Intelligence Explorer), built on **Gemini
  2.5 Pro** (knowledge cutoff January 2025) with Thinking mode, and **no
  domain-specific fine-tuning**. It maintains an internal running state — patient
  summary, working differential, information gaps, draft management plan — and
  moves through five phases: Intake, History Taking, Diagnostic Validation,
  Deliver Assessment, Wrap-up.
- **Who was eligible:** established patients at the practice, 18 or over, with a
  **single chief complaint**, already triaged by clinic staff as **not needing
  emergency care**, with English as their EHR primary language, enrolled in the
  patient portal, and able to use a **computer rather than a phone**. Excluded:
  known pregnancy, and mental-health chief complaints, "as the AMIE system has
  not been validated for psychiatric concerns."
- **Payment:** $25 for the AMIE encounter plus $25 for an optional interview,
  **raised to $50 midway through because recruitment was slower than expected.**
- **The funnel:** 1,452 urgent care visits were scheduled at the clinic during
  the study period. 140 consented by phone → 20 did not complete the consent form
  → 6 no-shows → **114 initiated** an AMIE encounter → 7 protocol deviations or
  technical issues, 5 system failures, 2 found to meet exclusion criteria
  mid-conversation → **100 completed (87.7%)** → 2 no-shows to the appointment →
  **98 analysed.**
- **Safety oversight:** every interaction continuously monitored in real time by
  one of **seven** board-certified internal medicine physicians, by secure video
  call with screen sharing, invisible to the patient once the chat began. Four
  prespecified stop criteria. A debrief immediately afterwards "to address any
  concerns, clarify information, and correct any errors or AI hallucinations."
  Supervisors completed a survey after **100%** of encounters.
- **Primary outcomes (pre-registered):** the number and type of chat
  terminations; the quality of AMIE's dialogue judged by patients and clinical
  evaluators using the GMCPQ, PACES and PCCBP rubrics; and patient and physician
  experience surveys.
- **Reference standard:** the final diagnosis of the presenting complaint,
  established by **chart review eight weeks after the visit** — which the authors
  note "has not been previously performed in any study evaluating conversational
  AI in real-world settings."
- **Evaluators:** a panel of **eight** board-certified internal medicine
  physicians, **three per case**, aggregated by median. There was overlap between
  supervisors and evaluators, but no evaluator rated a case they had supervised.
- **Statistics:** two-sided Wilcoxon signed-rank tests with patient-level
  pairing, **followed by Bonferroni correction across the five rating
  questions**; binomial 95% confidence intervals for proportions; Friedman
  omnibus test with pairwise Wilcoxon post-hoc for the attitude scale; reflexive
  thematic analysis for interviews. Reported per **TRIPOD-LLM** with a checklist.
- **Safety result:** **zero safety stops.** On three occasions a supervisor made
  remarks to the patient — once to clarify symptoms and rule out a potentially
  emergent condition the patient did not have, once to clarify when to seek
  emergency care, and once to correct AMIE for placing a past surgery date in the
  future.
- **Diagnostic accuracy** (Bond/Graber rating ≥4): top-1 **55/98 (56%)**, top-3
  **73/98 (75%)**, top-7 **88/98 (90%)**. The final-diagnosis reference was
  **confirmed by a diagnostic test in 46 cases** and was **presumptive, with no
  test, in 52**.
- **Head-to-head:** no detectable difference for differential quality (p=0.6),
  management-plan appropriateness (p=0.1) or safety (p=1.0). Physicians better on
  practicality (p=0.003) and cost effectiveness (p=0.004). Side-by-side
  preference for management plans was a near dead heat: physician preferred in
  **26**, equal in **47**, AMIE preferred in **25**.
- **Blinding check:** evaluators correctly identified the source in **58 of 98
  cases, 59.18% (95% CI 49.45%–68.91%)**.
- **Conversation quality, clinician view:** near-ceiling. "Seeking and addressing
  concerns" was rated very favourable in **98 of 98** cases. Unfavourable ratings
  were confined to history-taking gaps — past medical history in 2 cases, family
  history in 4, medication history in 1. In 43 of 98 cases evaluators judged
  omitting family history acceptable.
- **Conversation quality, patient view:** majority favourable across all PACES
  and PCCBP criteria, but **consistently lower than the clinicians' ratings**.
  The Lancet abstract gives 87–100% favourable across 17 criteria from
  evaluators against **48–96% across 16 criteria from patients**. The two
  criteria where patients were most neutral: **confidentiality of their
  information** and **honesty and trustworthiness**. Unfavourable ratings stayed
  below 10% throughout.
- **Patient attitudes:** General Attitudes towards AI Scale administered three
  times. Significant positive shift from pre-AMIE to post-AMIE (p<0.001 overall
  and on both the utility and concerns sub-scales), with **no further change**
  after the doctor's visit (p=0.86, 0.93, 0.90).
- **Physician reports:** surveys returned for **60 of 98** encounters (61.2%).
  **16 of those 60 (27%) had not read the transcript.** Of the 44 who had, the
  Lancet abstract reports AMIE was helpful for visit preparation in **33** and
  might have changed their behaviour in **25**.
- **Who the patients were:** 68% women; 49% White, 26% Black or African American,
  8% Hispanic or Latino, 5% Asian; 86% spoke English at home; 51% under 50 and
  only **15 of 98 (15%) aged 60 or over** — against the paper's own statement that
  **over half** the clinic's urgent care visits were over 60.
- **Reasoning traces were deliberately not shown to physicians,** on the grounds
  of length and review time.
- **No patient in the study was triaged to emergency care,** so AMIE's handling
  of that "remains unstudied."

# How Strong Is This Evidence? — Grade 4/5

Four out of five. On conduct this is the most carefully run AI deployment study
in this reading list. What holds it back is not sloppiness — it is that a
single-arm feasibility study with a reference standard the intervention may have
influenced cannot answer the question its headline invites.

**What earns the points, and there is a great deal.**

**The safety architecture is the real contribution.** A board-certified physician
watching every conversation live, with four prespecified stop criteria agreed in
advance and training to apply them, a survey completed after **every single**
encounter, and an immediate debrief to correct errors. The authors describe this
as potentially "a gold standard for safety oversight of LLM output presented to
patients," and that is a fair claim. It is also expensive and resource-intensive,
which they say.

**They checked that their blinding worked, and reported the result.** Evaluators
guessed the source correctly 59.18% of the time with an interval from 49.45% to
68.91% — containing chance. This is the methodological high point. A blinded
comparison whose blinding was never verified is a comparison of unknown validity,
and this is the first paper in 43 to test it.

**The reference standard is better than anything in this field so far.** Eight
weeks of chart review by a physician to establish what the patient actually
turned out to have — not a panel's guess, not the admitting impression. The
authors are right that this has not been done before in a real-world
conversational-AI study.

**They corrected for multiple comparisons.** Bonferroni across the five rating
questions. So p=0.003 and p=0.004 survived correction, and p=1.0 is a corrected,
capped value. Most papers in this space run a dozen tests and correct for none.

**They prespecified a subgroup analysis that could only hurt them.** Splitting
diagnostic accuracy by whether the final diagnosis was confirmed by a test (46
cases) or was a presumptive impression (52), and reporting that accuracy trended
**higher** in the weaker-reference group — while themselves calling that standard
"less robust."

**The negative and awkward findings are all there.** Physicians better on
practicality and cost. Patients consistently less impressed than clinicians.
Patients lukewarm on confidentiality and honesty. 27% of responding physicians
had not read the transcript. Some physicians found the asynchronous timing
*inefficient* because it made them review the same patient twice. A full
CONSORT-style flow diagram itemising every technical failure. None of this had to
be published.

**The Hawthorne effect is named twice, including against the headline.** The
authors write that patients' foreknowledge of being observed "likely limited
adversarial prompting, such as presenting evidence they found on the internet
regarding their condition, which has been known to alter the safety profile of
LLM output." That is the authors telling you their safety result may not
generalise, in the safety section.

**And a genuinely interesting scientific observation, reported against the
field's prevailing assumption:** AMIE's successful conversations had high
diagnostic accuracy from the very first turn and improved with more turns, while
unsuccessful ones did not improve — which the authors note parallels premature
closure in human clinicians, and from which they conclude that handing physicians
a model's reasoning trace is "unlikely to improve their diagnostic performance,"
contrary to arguments that chains of thought increase interpretability and trust.

**What costs the points.**

**One: the headline safety result has no confidence interval, in a paper that
puts intervals on everything else.** The methods state that binomial 95%
intervals were computed "for all proportions… comparative ratings from clinical
evaluators, blinding outcomes, as well as diagnostic accuracy of AMIE." Safety is
not on that list. Zero stops in 100 interactions bounds the true rate at about
**3 in 100** (exact one-sided 95% upper limit 2.95%). That is a reassuring
result. It is not the same as "safe," and the number belongs next to the zero.

**Two: in the majority of cases, AMIE may have influenced the standard it was
scored against.** The final diagnosis was presumptive — the physician's
impression with no confirmatory test — in **52 of 98 cases**. And the physician
had read AMIE's transcript *and its list of potential diagnoses* before the
visit. So for more than half the sample, the "ground truth" was formed by someone
who had just been shown AMIE's answers. The authors flag the presumptive standard
as less robust and run the subgroup analysis, but they do not name this pathway —
and it is the most parsimonious explanation for why accuracy trends higher in
exactly that subgroup.

**Three: what was tested is AMIE plus a watching physician, not AMIE.** Every
conversation was supervised live; patients knew it; and a physician debriefed and
corrected errors immediately afterwards. The safety profile of the unsupervised
system is not measured here and cannot be inferred. That is the right way to run
a first-in-human study, and it does mean the result does not transfer to the
deployment anybody is actually contemplating.

**Four: the abstract's "90%" is top-seven and does not say so.** A reader who
sees "AMIE's differential diagnosis included the final diagnosis in 90% of cases"
will picture a diagnosis, not a seven-item list. The honest headline figures are
**56% for the single best guess**, 75% within three, 90% within seven — and the
56% appears in neither abstract.

**Five: "no significant difference" is doing heavy lifting, and the tails
disagree with it.** On safety of the management plan, AMIE had **2 unfavourable
ratings and the physicians 0**, reported as p=1.0. No test can separate 2 from 0
out of 98, so p=1.0 means *undetectable*, not *equal*. More broadly, AMIE drew
unfavourable-or-worse ratings on **all five** criteria while physicians drew them
on only one; on every management-plan criterion the physicians had none at all.
Physicians' practicality ratings were favourable in **98 of 98** cases, AMIE's in
92. The distributions match in the middle and differ at the bottom, which for a
safety-critical tool is the end that matters.

**Six: the conversation rubrics are at the ceiling.** "Seeking and addressing
concerns" scored very favourable in 98 of 98 cases; five further criteria sit
within three cases of the top. A measure on which everything scores full marks
cannot distinguish a good system from a perfect one, or detect a future
regression. The informative exception is family history, where 43 of 98 were
marked not applicable, leaving a real denominator of 55 in which 4 unfavourable
is 7.3%.

**Seven: the physician findings rest on a shrinking denominator.** 98 encounters
→ 60 surveys returned (61.2%) → 44 who had actually read the transcript → 33 who
found it helpful. "75% found it helpful" is 33 of 44. As a share of all 98
encounters it is **34%**. Non-responders in a satisfaction survey are not
randomly distributed.

**Eight: a Gemini model graded a Gemini-based system.** The turn-level accuracy
analysis and the Bond/Graber ratings used to compute top-k accuracy were produced
by "a Gemini 2.5 Pro-based auto-rater." The final diagnoses themselves came from
human chart review, which is the important part, but the matching judgement — did
this differential item correspond to that diagnosis — was made by a sibling model
of the system under test.

**Nine: no inter-rater reliability for the evaluator panel.** Three evaluators
per case, aggregated by median, and no statistic reported for how much they
agreed. Given that this list decoded a protocol yesterday whose best feature was
planning exactly this, the omission stands out.

**Ten: the sample is not the population.** 98 of 1,452 urgent care visits (6.7%).
Participants needed a computer rather than a phone, English as their EHR
language, portal enrolment, a single complaint, and pre-triage as non-emergency;
pregnancy and mental-health complaints were excluded; and they were paid. Only
15% were 60 or over against more than half of the clinic's urgent care
population. Sex and race did track the clinic, which is worth crediting. Age did
not, and age is where diagnostic difficulty lives.

**What would make it a five:** a confidence interval on the safety result, the
single-best-guess accuracy in the abstract, and an analysis restricted to the 46
test-confirmed diagnoses as the primary accuracy estimate.

# The Editor's Concerns

**Put the interval on the zero.** One clause: "zero safety stops in 100
interactions (95% upper bound 3.0%)." It costs nothing, it is consistent with the
paper's own stated method for all other proportions, and without it the single
most quotable sentence in the paper overstates what 100 patients can establish.

**Make the test-confirmed subgroup the primary accuracy analysis.** 46 cases with
a diagnosis confirmed by laboratory, microbiology, pathology, imaging or ECG is a
reference standard that AMIE could not have influenced. The 52 presumptive cases
should be reported separately and labelled as potentially contaminated, because
the physician forming that impression had read AMIE's differential. Report the
numeric accuracy in each subgroup, not just "trending higher" — those numbers are
in Figure 3.c and should be in the text.

**Say in the abstract how long the differential list was.** "Included the final
diagnosis within its top seven candidates in 90% of cases, within three in 75%,
and as its single leading diagnosis in 56%." All three numbers, with their k.

**Replace "p = 1.0" with the counts on safety.** "2 of 98 AMIE plans versus 0 of
98 physician plans were rated unfavourable for safety; the study was not powered
to detect a difference of this size." That is what the data say.

**Report inter-rater reliability for the three-evaluator panel,** and for the
Gemini auto-rater, agreement against a human rater on a sample of the
differential-matching judgements. The second is the load-bearing one: the headline
accuracy depends on it.

**Report the proportion of each rubric criterion at the ceiling,** and consider a
harder instrument for the next study. If every criterion saturates, a larger
trial will learn nothing new about conversation quality, and a regression will be
invisible.

**Give the physician survey findings with the full denominator alongside the
responder denominator** — 33/44 and 33/98 — and compare responders with
non-responders on anything available.

**State what the three supervisor remarks mean for the safety claim.** Three
interventions short of a stop, in 100 conversations, is a 3% rate of a physician
judging it necessary to say something — including once to clarify when to seek
emergency care. That is a safety-relevant signal sitting just under the
prespecified threshold, and it deserves a sentence rather than a footnote.

**Reconcile the two documents.** The Lancet abstract states that safety
supervisors "noted one hallucination and added clinical information in five
interactions." The preprint states that "on three occasions, the AI supervisor
made remarks to the patient." Three and five are different counts, and whichever
is the final one should be the one that appears.

**Flag that the study cannot speak to triage.** No patient was sent to emergency
care, because all were pre-triaged as not needing it. The paper says this. It
should say it in the abstract too, because "safe in urgent care" will be read as
"safe as a front door," and the front door is precisely what was excluded.

**And a credit worth converting into a request:** the finding that AMIE's
accuracy is set early in the conversation and that unsuccessful conversations do
not improve with more turns is the most scientifically interesting thing here.
Report it as a primary analysis in the next study, not an appendix exploration —
and test whether a model's own early confidence can be used to decide when to
hand over to a human.

# Statistics Spotlight

Five ideas. The first two are new to this list and the second is the best piece of
method in the paper.

## 1. Zero is not a rate. The rule of three.

"Zero safety stops across all 100 patient-AMIE interactions" is the sentence
everyone will quote. Here is how to read it honestly.

Suppose the true probability that any given conversation needs stopping is some
small number *p*. If you run 100 conversations, the chance you see **no** stops at
all is (1 − *p*)¹⁰⁰. Now ask: how large could *p* be while still leaving you a
reasonable chance of observing zero?

Set that probability at 5% — the usual threshold — and solve:

> (1 − p)¹⁰⁰ = 0.05 → p = 1 − 0.05^(1/100) = **0.0295**

So a true stop rate of **about 3 in 100** would still produce zero stops in a
run of 100 about one time in twenty. The data cannot rule it out.

The shortcut worth memorising is the **rule of three**: with zero events in *n*
observations, the one-sided 95% upper bound on the rate is roughly **3 ÷ n**.
Here 3 ÷ 100 = 3%, which matches the exact 2.95% almost perfectly.

And the arithmetic of what it would take to do better:

> 100 interactions → upper bound **3.0%**
> 200 → 1.5%
> 500 → 0.6%
> 1,000 → 0.3%
> **2,995** → 0.1%

To be 95% confident that fewer than one patient in a thousand would need a stop,
you need about **3,000** supervised conversations. This study ran 100 — which is
exactly right for a first-in-human feasibility study, and nowhere near enough to
support a claim about deployment safety.

**An everyday version.** You cross a particular road 100 times and are never hit
by a car. That is genuine evidence the road is not lethal. It is not evidence that
the risk is below 1%, because a 1-in-50 road would also have let you cross 100
times unharmed about one time in seven.

**Watch out for:** any safety claim resting on zero events. Ask how many
observations, divide 3 by it, and that is roughly the largest rate the study can
exclude. Then ask whether that rate would be acceptable. For a tool that might
run a million conversations, an upper bound of 3% means up to 30,000 events — and
the honest statement is "we did not see any in 100," not "it is safe."

## 2. Did the blinding actually work? There is a test for that.

A blinded comparison is only as good as the blind. If evaluators can tell which
output came from the machine, every rating is contaminated by whatever they
believe about machines — and you will never know in which direction.

Almost no paper checks. This one does, and it is the best thing in it.

The evaluators were shown differentials and management plans from AMIE and from
physicians, in blinded, randomised order, and asked to rate them. They were also
asked to guess the source. The result:

> correct in **58 of 98 cases = 59.18%**, 95% CI **49.45% to 68.91%**

That interval reproduces exactly from 58/98 using the standard formula, and the
key fact is where its lower end sits: **49.45% is below 50%.** Pure guessing
scores 50%. Since the interval contains 50%, the data are consistent with the
evaluators having no real ability to tell. The blind held.

Note how the logic runs. A *high* correct-identification rate would have been bad
news — it would mean the comparison was unblinded in practice. 59% with an
interval straddling chance is the result you want. And it is a result, not an
assumption: this is the difference between saying "we blinded the evaluators" and
showing it.

**An everyday version.** You run a taste test between two colas with the labels
hidden. Before trusting the verdict, ask the tasters to say which was which. If
they get it right 95% of the time, your blind failed and the preference data are
worthless. If they are at chance, you can believe the preference.

**Watch out for:** the words "blinded," "masked" or "independent assessors" with
no check attached. In imaging and pathology studies AI output often looks
different from a human's — different formatting, different verbosity, different
hedging — and that alone can unblind a reader. Ask whether the assessors were
asked to guess, and what the interval around that guess rate was. If the paper
does not report it, treat the blinding as claimed rather than demonstrated.

## 3. "No significant difference" again — but now look at the tails

This list has met this idea before. Here it has a sharper edge, because the place
the two distributions differ is the place that matters for a medical tool.

The reported comparisons, all Bonferroni-corrected: differential quality p=0.6,
management-plan appropriateness p=0.1, safety **p=1.0**, practicality p=0.003,
cost effectiveness p=0.004.

Now the counts behind "safety, p=1.0", out of 98 cases each:

> AMIE: 0 very unfavourable, **2 unfavourable**, 5 neither, 5 favourable, 86 very
> favourable
> Physicians: 0 very unfavourable, **0 unfavourable**, 5 neither, 6 favourable, 87
> very favourable

Two against zero. A p-value of 1.0 on that comparison does not mean the plans
were equally safe. It means **no statistical test could tell 2 from 0 in a sample
of 98** — which was true before the study began. The honest sentence is "AMIE
produced two management plans a physician rated unsafe; the physicians produced
none; this study cannot say whether that difference is real."

Widen out and the pattern repeats. Counting unfavourable-or-worse ratings:

> AMIE: differential 4, appropriateness 4, cost 4, practicality 2, safety 2 —
> **every criterion**
> Physicians: differential 3, appropriateness **0**, cost **0**, practicality
> **0**, safety **0**

Physicians were rated favourable or very favourable for practicality in **98 of
98** cases. AMIE in 92. The averages are close; the floors are not.

And a nice complication: head-to-head, management plans were a dead heat —
physician preferred in 26, equal in 47, AMIE preferred in 25. The side-by-side
asks "which is better?" and the pointwise asks "how good is each?" A small,
consistent edge can vanish when raters are forced to choose between two
reasonable plans.

**An everyday version.** Two drivers have the same average journey time. One is
steady; the other is usually faster but occasionally runs a red light. "No
significant difference in average time" is true and is not the thing you care
about.

**Watch out for:** a non-significant p-value on a safety or harm outcome. Always
ask for the raw counts. Rare bad events are exactly what small studies cannot
detect, and "no significant difference in adverse events" from 98 patients is
almost content-free. Look for the distribution, not the test.

## 4. When everyone scores full marks, the ruler has stopped working

The clinicians' ratings of AMIE's conversations are, in places, perfect:

> "seeking and addressing concerns" — very favourable in **98 of 98** cases
> "explaining information professionally" — 96 of 98
> "eliciting the presenting complaint" — 97 of 98
> "maintaining patient welfare" — 96 of 98
> "explaining information clearly" — 95 of 98

This is a **ceiling effect**, and it has two consequences people routinely miss.

It cannot discriminate. A rubric that scores 98 out of 98 cannot distinguish this
system from one twice as good, or from a slightly worse one. The measurement has
no headroom.

And it cannot detect regression. If the next model version is worse at addressing
concerns, this instrument will still report 98 of 98 until the degradation is
large. For a tool meant to be monitored over time, a saturated measure is a
blindfold.

The useful contrast is inside the same table. Family history was rated: 4
unfavourable, 3 neither, 5 favourable, 43 very favourable — and **43 marked not
applicable**, because evaluators judged that omitting family history was fine for
that complaint. So the real denominator is 55, in which 4 unfavourable is
**7.3%**. That criterion is informative precisely because it is not at the
ceiling.

**An everyday version.** A driving examiner who passes everyone is not
discovering that all learners are excellent; they have stopped being an examiner.
And if a student's driving deteriorates next year, that examiner will not notice.

**Watch out for:** rating scales where most responses pile into the top category,
and particularly where a paper reports "X% favourable or very favourable" without
the distribution. Ask what proportion got the maximum. If it is near everything,
the measure has told you the system is above some floor and nothing more — and
the interesting information will be in the one or two criteria that did spread
out.

## 5. Follow the denominator downhill

One of this paper's findings travels through four different denominators, and
which one you quote changes the answer by a factor of two.

> **98** encounters analysed
> **60** physician surveys returned — 61.2%
> **44** of those had actually read the transcript (16 of the 60, or 27%, had not)
> **33** of those 44 found AMIE helpful for visit preparation
> **25** of those 44 said it might have changed their behaviour

"Physicians found it helpful in 75% of cases" is 33 ÷ 44. Across all 98
encounters it is 33 ÷ 98 = **34%**. Both are correct arithmetic about different
questions. The first answers *among physicians who responded and had read it, how
many were positive?* The second answers *in what fraction of encounters did this
workflow produce a physician who said it helped?* For deciding whether to deploy
the workflow, the second is the relevant one.

The gap between them is driven by two separate losses, and neither is random. A
61% response rate to a satisfaction survey is the classic setting for
**non-response bias**: people with an opinion, usually a positive one, answer.
And 27% of responders not having read the transcript is itself a finding about
workflow feasibility — the intervention did not reach the clinician in more than
a quarter of the cases where we know what happened.

Contrast the other response rates in the same study: patients around 90% across
three surveys, and AI supervisors **100%**. The physicians — the busiest people,
and the ones whose workload the tool is meant to reduce — were the hardest to
hear from, at 61%.

**An everyday version.** A restaurant reports that 90% of diners who filled in
the card loved the meal. Fine. But the cards were on the tables and nine in ten
diners walked past them. "90% of respondents" and "90% of diners" are different
claims, and only one was measured.

**Watch out for:** percentages in surveys, satisfaction studies and
implementation research. Find the number the percentage is a percentage *of*, and
then find the number of people the study started with. If they differ a lot, ask
what happened in between and whether it could be related to the answer. Here the
paper gives you every denominator, which is why the check is possible — many do
not.

# Jargon Translator

- **AMIE (Articulate Medical Intelligence Explorer)** — the conversational
  diagnostic AI system under study, built by Google Research and Google DeepMind.
- **Gemini 2.5 Pro / Thinking mode** — the underlying general-purpose language
  model, used here **without** medical fine-tuning, with a setting that lets it
  reason at greater length before replying.
- **Agentic / internal state** — the system keeps a running summary, working
  diagnosis list, list of information gaps and draft plan between turns, rather
  than treating each message independently.
- **Prospective** — participants enrolled and followed forward, with the plan
  fixed in advance. The opposite of digging through old records.
- **Single-arm** — everyone gets the intervention; there is no comparison group
  receiving usual care.
- **Feasibility study** — an early study asking "can this be done at all, and
  safely?" rather than "does it work better?"
- **Pre-registered** — the plan and outcomes were lodged publicly (here
  NCT06911398) before the study ran.
- **TRIPOD-LLM** — the reporting checklist for studies of large language models in
  clinical prediction.
- **CONSORT diagram** — the standard flow chart showing how many participants
  entered each stage and why any were lost.
- **Chief complaint** — the main problem a patient comes in with.
- **Triage** — sorting by urgency. Here clinic staff had already decided these
  patients did not need the emergency department.
- **Primary care provider (PCP)** — the attending physician, resident or nurse
  practitioner seeing the patient.
- **Differential diagnosis (DDx)** — the ranked list of conditions that could
  explain the symptoms.
- **Management plan (Mx)** — what to do next: tests, treatments, referrals,
  follow-up.
- **Top-k accuracy** — whether the right answer appears anywhere in the first *k*
  items of a ranked list. Top-1 is the single best guess; top-7 allows seven.
  **Always ask what k is.**
- **Bond/Graber rating** — a published scale for the quality of a differential
  diagnosis, used here with a threshold of ≥4 to count a match.
- **Reference standard / ground truth** — what the study treats as the true answer.
  Here, the final diagnosis from chart review eight weeks later.
- **Presumptive diagnosis** — a clinician's working conclusion without a
  confirmatory test. A weaker reference standard than a laboratory or imaging
  result.
- **Auto-rater** — an AI model used to score outputs instead of a human. Here a
  Gemini 2.5 Pro model judged whether AMIE's differential items matched the final
  diagnosis.
- **Blinding** — concealing from an assessor which output came from which source.
- **Pointwise versus side-by-side (comparative) rating** — scoring each item on
  its own merits, versus directly choosing between two.
- **Wilcoxon signed-rank test** — a comparison test for paired data that does not
  assume a bell-shaped distribution. "Paired" here means the same patient's AMIE
  and physician output are compared with each other.
- **Friedman test** — the equivalent for three or more repeated measurements on
  the same people; used here for the three attitude surveys.
- **Bonferroni correction** — dividing the significance threshold by the number of
  tests, so that running five comparisons does not manufacture a false positive.
- **Binomial confidence interval** — the uncertainty range around a proportion.
- **Rule of three** — with zero events in *n* observations, the 95% upper bound on
  the rate is about 3 ÷ *n*.
- **Ceiling effect** — when nearly everything scores the maximum, so the measure
  can no longer discriminate.
- **Non-response bias** — when the people who answer a survey differ
  systematically from those who do not.
- **Hawthorne effect** — people behave differently because they know they are
  being observed.
- **GMCPQ / PACES / PCCBP** — established rubrics for rating clinical
  consultations: a patient questionnaire, a clinical-skills examination
  framework, and a patient-centred communication standard.
- **GAAIS (General Attitudes towards AI Scale)** — a validated questionnaire
  measuring attitudes to AI, with sub-scales for perceived utility and perceived
  concerns.
- **Reflexive thematic analysis** — a structured qualitative method for drawing
  themes out of interview notes.
- **REDCap** — a secure web platform widely used for research data capture.
- **Premature closure** — the diagnostic error of settling on an answer too early
  and not revising it.

# What You Can (and Can't) Say

**You can say:** in the first prospective study of a conversational diagnostic AI
with real patients in a real clinic, 100 patients at a Boston academic primary
care practice completed a pre-visit text conversation with AMIE, each one
monitored live by a board-certified physician, and **no conversation required a
safety stop** under four prespecified criteria.

**You can say:** checked against the final diagnosis from an eight-week chart
review, AMIE's ranked differential contained the correct answer in 90% of cases
within seven candidates, 75% within three, and **56% as its single leading
diagnosis**.

**You can say:** in blinded comparison, clinical evaluators found no detectable
difference between AMIE's and physicians' differentials or in the appropriateness
and safety of their management plans, while rating physicians' plans
significantly better for **practicality** and **cost effectiveness** — and that
the evaluators could not reliably tell which output was which (59.18%, 95% CI
49.45–68.91%).

**You can say** patients' attitudes towards AI improved significantly after the
interaction and stayed elevated, and that physicians who read the transcript
mostly found it useful for visit preparation.

**You cannot say** the system is safe. Zero events in 100 interactions bounds the
true rate at roughly **3 in 100**, not zero. Establishing a rate below 1 in 1,000
would need about 3,000 supervised conversations.

**You cannot say** this tells you about unsupervised use. A physician watched
every conversation live, patients knew it, and a physician debriefed and
corrected errors immediately afterwards. The authors themselves note that
foreknowledge of observation "likely limited adversarial prompting."

**You cannot say** AMIE matches physicians on management plans. The averages were
close and the floors were not: AMIE drew unfavourable ratings on all five
criteria and the physicians on one, with zero on every management-plan criterion.
The p=1.0 on safety reflects 2 unfavourable ratings versus 0, which no test of
this size could separate.

**You cannot treat** the 90% diagnostic accuracy as a diagnosis-level result. It
is a seven-item list, and the single best guess was right 56% of the time.

**You cannot treat** the accuracy figure as clean in the majority of cases. In 52
of 98, the reference diagnosis was the physician's presumptive impression, formed
after reading AMIE's own list of candidate diagnoses — and accuracy trended
higher in exactly that subgroup.

**You cannot say** anything about AI triage. Every patient had already been
assessed by clinic staff as not needing emergency care, pregnancy and
mental-health complaints were excluded, and **no patient was sent to emergency
care**. The authors state that this capability "remains unstudied."

**You cannot generalise** to the clinic's own population, let alone beyond it. 98
of 1,452 urgent care visits took part; participants needed a computer rather than
a phone, English as their record language and a single complaint; they were paid
$25 rising to $50; and only 15% were 60 or over against more than half of the
clinic's urgent care visits.

**You should note** that this summary rests on the Lancet abstract plus the arXiv
preprint, because the peer-reviewed full text is paywalled, and that the two
documents give different counts for the supervisors' non-stop interventions —
three occasions of remarks in the preprint, one hallucination plus information
added in five interactions in the Lancet abstract.

# Bottom Line for Your Life

This is the first study where a medical AI talked to real patients with real
problems, and the most useful things in it are not about the AI.

**The design is the news, not the result.** A doctor watched every single
conversation, live, with the authority to stop it, and debriefed every patient
afterwards. That is what a responsible first test of this technology looks like,
and it is the standard to ask about whenever you are offered an AI that talks to
patients: *who was watching when this was tested, and is anyone watching now?*
The answers are usually different, and the second one is the one that applies to
you.

**If something like this reaches your clinic, it will probably be a pre-visit
questionnaire with better manners** — and on the evidence here, that is a
reasonable thing to accept. Patients rated the conversations well, their
attitudes to AI improved, and doctors who read the summaries mostly found them
useful preparation. Nobody was harmed. The AI did not replace the appointment; it
fed into one.

**Two things in the detail are worth carrying.** First, the patients in this
study were lukewarm on exactly two questions: whether their information would
stay confidential, and whether the AI was honest and trustworthy. They liked the
conversation and reserved judgement on the trust. That seems to me the correct
posture, and it is a reasonable thing to ask about explicitly — where does what I
type go, and who sees it?

Second, and more practically: AMIE's diagnostic list was right 90% of the time
**if you allowed it seven guesses**, and 56% of the time on its single best one.
If a tool like this shows you a list of possible conditions, the list is doing
what a doctor's mental list does early in a consultation — holding several
options open. It is not a diagnosis. Reading the top item as the answer
misreads the number by a wide margin, and the people who built it framed their
output deliberately as "possible diagnoses or next steps for the patient to
discuss with a provider."

And the thing this study explicitly did not test: **it cannot tell you whether an
AI can safely decide you need an emergency room.** Everyone in it had already
been assessed by a human as not needing one. If you are acutely unwell, that is a
question for a person or an emergency number, not a chat window.

**This is education about how to read a study, not medical advice. Decisions
about your care belong with you and your clinicians.**

---

*Decoded 2026-10-10. Sources: the Lancet record and abstract via PubMed, accessed
and verified 2026-10-10; the arXiv preprint (arXiv:2603.08448v3, 15 March 2026)
read in full via the alphaXiv index, because the Lancet full text is paywalled,
there is no PubMed Central copy, and both the publisher and arxiv.org are
unreachable directly from this environment. **All numeric values above are from
the arXiv preprint unless attributed to the Lancet abstract.** Not available in
the pages retrieved: Appendix Tables A.5 to A.11, and therefore the full survey
response distributions, the per-item GAAIS means, the turn-level reasoning
analysis and the TRIPOD-LLM checklist. Derived figures — the participant-funnel
reconciliation and the 10.5% technical failure rate; the exact one-sided 95%
upper bounds on zero events (2.95% at n=100, and 2,995 interactions needed for a
0.1% bound); the reproduction of the blinding interval from 58 of 98 (49.45% to
68.91%); the top-1, top-3 and top-7 accuracy percentages with their intervals;
the unfavourable-rating counts across all five criteria for both AMIE and
physicians; the side-by-side preference totals; the ceiling-effect counts and the
family-history denominator of 55; and the 33/44 versus 33/98 denominator cascade
— were computed from the paper's own reported counts and are labelled as derived
wherever they appear. Funding: Alphabet. All authors are affiliated with Google,
Google DeepMind, or the participating academic medical centres.*

**Verified source links**
- DOI (The Lancet): https://doi.org/10.1016/S0140-6736(26)01535-7
- PubMed: https://pubmed.ncbi.nlm.nih.gov/42849491/
- Preprint read for detail: https://arxiv.org/abs/2603.08448 (arXiv:2603.08448v3)
- Registration: ClinicalTrials.gov NCT06911398
- Lancet full text: **paywalled and not retrieved**; no PubMed Central copy
  exists as of 2026-10-10.
- Accompanying Lancet commentary, not retrieved (no abstract in PubMed, full text
  paywalled): Omar M, Nadkarni GN, "Conversational diagnostic AI in primary care:
  what happens after it speaks?" https://doi.org/10.1016/S0140-6736(26)01763-0 —
  https://pubmed.ncbi.nlm.nih.gov/42849492/
