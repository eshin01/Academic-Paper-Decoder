# General-purpose large language models outperform specialized clinical AI tools on medical benchmarks

- **Authors:** Krithik Vishwanath, Anton Alyakin, … Daniel Alexander Alber, Eric Karl Oermann (NYU Langone and collaborators)
- **Venue:** Nature Medicine, Brief Communication, July 2026 (32:2405–2409)
- **DOI link:** https://doi.org/10.1038/s41591-026-04431-5 (as printed in the paper)
- **Publisher page:** https://www.nature.com/articles/s41591-026-04431-5
- **PubMed link:** not verified at decode time (omitted rather than guessed)
- **Basis:** FULL TEXT — analyzed from the complete published open-access PDF (main text, Methods, and Extended Data), user-uploaded
- **Decoded:** 2026-08-31

---

# The Gist

Researchers at NYU tested whether special AI tools built just for doctors (OpenEvidence and UpToDate Expert AI) actually answer medical questions better than the general-purpose AI chatbots anyone can use (GPT-5.2, Gemini 3.1 Pro, and Claude Opus 4.6). They ran all of them through exam questions, a physician-alignment test, and 100 real questions doctors had asked an AI during actual hospital work, with real doctors blindly grading the answers. The everyday chatbots beat the specialized medical tools on every test — and the medical tools did about as well as the free AI summary that pops up on top of a Google search.

# Study Snapshot

- **Study type:** A comparative benchmark evaluation (researchers gave the same questions to each AI and measured answer quality). This is a cross-sectional performance comparison — it sits low on the evidence ladder for *clinical* claims because it measures answer quality, not what happens to actual patients. But for the question "which AI writes better answers?", it's a reasonable design, strengthened by its blinded human-review stage.
- **What was compared:** 2 specialized clinical AI tools vs. 3 general-purpose "frontier" AI models, plus Google's AI Overview as a real-world comparison.
- **The tests:** 500 medical-license-exam-style questions (MedQA), 500 items from a benchmark called HealthBench, and 100 real de-identified questions doctors asked an AI at NYU Langone hospital ("RCQ").
- **The human graders:** 12 US clinicians, blinded (they didn't know which AI wrote which answer), 3 graders per answer, 1,800 total ratings on a 1–4 scale for correctness, completeness, safety, and clarity.
- **How long:** A snapshot — models were queried September 2025 through February 2026.
- **Funding:** US National Cancer Institute, the Keck Foundation, and South Korean government AI grants; funders had no role in the study. **Conflicts of interest:** the senior author reports equity in two AI companies and *consulting for Google* — whose Gemini model scored highest on the exam test.
- **Published in:** Nature Medicine (a top-tier journal), peer reviewed with named reviewers, open access, with code publicly released.

# How Strong Is This Evidence?

**Grade: 3/5 — moderate: well-executed for what it measures, but what it measures isn't patient care.**

For its actual question — "which AI writes better answers to medical questions?" — this is a genuinely well-run study: independent (not funded by any AI company), with blinded human graders, pre-specified statistics, multiple cross-checking analyses, and real doctor questions from a real hospital instead of only canned exam items. That's much stronger than the marketing-style comparisons common in this field. What caps the grade: only 100 real-world questions from a single hospital, graders who often disagreed with each other on exact scores, and — most importantly — the study measures how good the *answers look to doctors*, not whether using any of these tools helps or harms actual patients. No study of this design can tell you that.

# The Editor's Concerns

- **The headline slightly oversells one result.** On the exam test (MedQA), only Gemini and GPT-5.2 statistically beat the clinical tools. Claude (90.2%) was statistically tied with OpenEvidence (89.6%) and UpToDate (88.4%). So "frontier models outperformed clinical tools in all three evaluations" is true of the group, but not of every model on every test.
- **The real-world differences are modest, not dramatic.** On the 1–4 doctor-rating scale, the gap between the best chatbot (3.62) and the clinical tools (3.17–3.24) was under half a point. Real and consistent — but "somewhat better answers", not "night and day".
- **The safety conclusion is underpowered.** "No difference in harmful answers" comes from just 100 questions, where harmful answers were rare for everyone (0–3%). A study this size simply cannot detect rare-but-serious safety differences. "We didn't see a difference" is not "they're equally safe".
- **Graders disagreed a lot on exact scores.** Agreement between the 12 doctors on the 1–4 ratings was only "fair" (Krippendorff's alpha 0.10–0.20 — a measure of how much raters agree beyond chance). They mostly disagreed by one point and agreed better on "acceptable vs. not", but noisy ratings blur fine distinctions.
- **One hospital, one kind of question.** The 100 real questions came from doctors at a single New York hospital system who were *already choosing to ask an AI*. Questions doctors ask elsewhere — or wouldn't ask a chatbot at all — might behave differently.
- **The clinical tools had to be tested by hand through their websites** (they have no programming interface), which the authors admit could introduce hidden differences in prompts and formatting.
- **A benchmark made by a competitor.** HealthBench was built by OpenAI — and OpenAI's own model got the top score on it. The authors flag this themselves and correctly demote HealthBench to supporting evidence.
- **The judges were also contestants.** On HealthBench, the three frontier models graded the answers (including their own), a known bias risk, partly blunted by using a three-model panel.
- **Conflict of interest worth knowing:** the senior author consults for Google, and Google's two products (Gemini and AI Overview) are in the comparison. Disclosed, but readers deserve to weigh it.
- **What this study did well:** independent funding; blinded, randomized human review; a contamination-free benchmark built from real clinical use; honest and unusually thorough self-reported limitations; effect sizes and sensitivity analyses, not just p-values; public code; and a genuinely useful practical finding — UpToDate's AI refused to answer 19 out of 100 real questions, versus 1–3 for the chatbots.

# Jargon Translator

- **LLM (large language model):** the AI technology behind chatbots like ChatGPT — a program trained on huge amounts of text to generate answers.
- **Frontier model:** the newest, most capable general-purpose AI models from the big labs.
- **RAG (retrieval-augmented generation):** a technique where the AI looks up documents (like medical references) and uses them to write its answer — what these clinical tools likely do.
- **Benchmark:** a fixed set of test questions used to score and compare AI systems.
- **Blinded review:** graders don't know which AI wrote which answer, so brand reputation can't sway scores.
- **95% confidence interval (CI):** the range where the true value plausibly sits; a way of showing how precise an estimate is.
- **P-value:** roughly, how surprising the result would be if there were truly no difference; small values (like P < 0.05) suggest a real difference.
- **Holm–Bonferroni correction:** a math adjustment that stops you from getting false "significant" results just because you ran many comparisons.
- **Refusal rate:** how often a tool declined to answer a question at all.
- **Hallucination:** when an AI confidently states something false or made up.
- **LLM-as-judge:** using one AI to grade another AI's answers — cheaper than human grading, but with its own bias risks.

# What You Can (and Can't) Say

**Fair to say:**
- "In an independent, blinded evaluation, doctors rated answers from general chatbots (GPT-5.2, Gemini, Claude) somewhat higher than answers from OpenEvidence and UpToDate Expert AI on real clinical questions."
- "The specialized medical AI tools scored about the same as Google's free AI Overview in this study."
- "UpToDate's AI refused nearly 1 in 5 real questions; the general chatbots almost never refused."
- "Paying for a 'medical-grade' AI tool doesn't guarantee better answers than a frontier chatbot, at least as of early 2026."

**Not fair to say:**
- "ChatGPT is better than doctors" — doctors were the *judges* here, not the competition.
- "Clinical AI tools are unsafe" or "chatbots are proven safe for medical use" — the study found no safety differences but was far too small to establish safety.
- "You should use a chatbot instead of seeing a doctor" — the study is about tools *doctors* use for information, not a substitute for care.
- "This settles it forever" — the authors themselves call it "a snapshot of a rapidly evolving landscape"; all these products change monthly.

# Bottom Line for Your Life

If you've seen headlines like "regular AI beats medical AI", this study mostly backs the modest version of that claim: in one careful, independent test, general chatbots wrote answers doctors rated somewhat higher than two expensive specialized tools did. What it doesn't tell you is whether any of these tools actually improves medical care or patient outcomes — no study of this design can. One study is one data point, from one hospital, at one moment in a fast-moving field. This is an educational breakdown, not medical advice — for your own health decisions, AI answers of any brand are a starting point for a conversation with a clinician, not a replacement for one.
