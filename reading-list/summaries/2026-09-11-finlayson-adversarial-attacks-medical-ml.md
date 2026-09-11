# Adversarial attacks on medical machine learning

- **Authors:** Samuel G. Finlayson (Harvard Medical School), John D. Bowers (Harvard Law School), Joichi Ito (MIT Media Lab), Jonathan L. Zittrain (Harvard Law School), Andrew L. Beam (Harvard T.H. Chan School of Public Health), Isaac S. Kohane (Harvard Medical School)
- **Venue:** Science, 2019;363(6433):1287–1289 (published March 22, 2019) — **a Policy Forum article, not a research paper**
- **DOI link:** https://doi.org/10.1126/science.aaw4399
- **PubMed link:** https://pubmed.ncbi.nlm.nih.gov/30898923/ (PMID 30898923)
- **Full-text link:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7657648/ (PubMed Central, author manuscript)
- **Basis:** FULL TEXT — the complete Policy Forum article retrieved from PubMed Central. Funding and competing-interest statements were not present in the retrieved text; PubMed tags NIH extramural support. Identifiers verified against the live PubMed/NLM record. PubMed carries **no abstract** for this item, which is normal for this article type.
- **Decoded:** 2026-09-11

---

# The Gist

Everything you have read so far asked whether medical AI works. This piece asks a different question: **can someone deliberately break it?** The answer is yes, easily, and in ways nobody can see. The authors show a photograph of a harmless mole that a diagnostic model correctly calls benign with over 99% confidence. They then add a layer of what looks like faint static — invisible to a human eye, and mathematically calculated rather than random — and the same model now calls the same mole cancerous with **100% confidence**. Their argument is that medicine is unusually tempting ground for this, because US healthcare already runs on a $250-billion fraud industry and routine "creative billing," and because insurers increasingly use algorithms to approve or deny claims. Where money meets an algorithm, someone will learn to game the algorithm.

# Study Snapshot

- **Article type — read this first:** this is a **Policy Forum** essay in Science. It is an expert argument about a risk, not a study that measured anything. Science publishes these alongside research papers, and they look similar in a citation. The distinction matters enormously for how much weight the piece can carry (see Statistics Spotlight).
- **Who wrote it:** an unusual interdisciplinary group — two physicians/informaticians, a biostatistician, and **two Harvard Law School scholars plus the then-director of the MIT Media Lab**. The legal and policy presence is the point; the piece is about governance, not algorithms.
- **The central demonstration:** the mole example above, which the authors state comes from their own earlier work executing "successful adversarial attacks against three highly accurate medical image classifiers." That empirical work is cited, not presented here.
- **Key technical claim:** the noise added is **not random** and "has near-zero probability of occurring by chance." Their explicit framing is that this "reflect[s] not that machine-learning models are inaccurate or unreliable per se but rather that even otherwise-effective models are susceptible to manipulation by inputs explicitly designed to fool them."
- **How wide the vulnerability runs:** adversarial examples have been demonstrated "for essentially every type of machine-learning model ever studied" — from simple logistic regression (the Epic sepsis model's type) to deep neural networks — across images, audio, text, and structured data.
- **Subtler attacks than noise:** rotating an image to a specific angle can defeat a modern network. Swapping in carefully chosen synonyms can fool text algorithms. For billing data, the attack is simply finding code combinations that maximise reimbursement.
- **The existing behaviour they point to:** medical fraud is "a $250 billion industry"; **upcoding** — billing for a more expensive service than performed — is described as "rampant"; some physicians report exaggerated anesthesia times.
- **A genuinely uncomfortable example:** the authors cite the Endocrine Society advising providers *not* to bill the metabolic syndrome code for obese patients, since that combination invites denial, and to bill the component conditions instead. No false claim is made — a true one is simply withheld. The authors call this "a moral gray zone."
- **What has actually happened so far:** "Cutting-edge adversarial attacks have yet to be found in the health care context." The threat is anticipated, not observed.
- **Proposed defence:** capture a cryptographic "fingerprint" hash of clinical data at the moment of acquisition, so later tampering becomes detectable; existing lab regulations (CLIA) could be extended to require it.

# How Strong Is This Evidence?

**Grade: 2/5 — an influential and well-reasoned argument, but an argument, not evidence.**

This grade needs explaining, because it is not a criticism of the piece's quality. On this scale, the grade measures how much weight a document can bear as evidence about the real world. A Policy Forum essay — however distinguished its authors and journal — presents no new data, has no methods section, no sample, no statistical analysis, and no peer-reviewed empirical result of its own. Its central technical demonstration is a reference to the authors' separate prior work. And it says plainly that the attacks it warns about have not yet been observed in healthcare.

What it does well is what essays can do: define a problem clearly, assemble evidence from adjacent fields, connect a technical vulnerability to real economic incentives, and propose concrete policy responses. The mole demonstration is striking and, as far as the underlying computer-science literature goes, uncontroversial. Read it as a well-informed warning from people qualified to issue it — and not as a finding that anything has happened.

# The Editor's Concerns

- **A prestigious venue is not a study design.** "Published in Science" reads as maximum authority in a citation, but the Policy Forum section is explicitly opinion and analysis. Anyone citing this as "Science showed that medical AI can be hacked" is overstating what the document is, though not what the computer-science literature says.
- **The harms are hypothetical throughout.** Every healthcare scenario — the fraudulent melanoma claim, the opioid workaround, the manipulated trial endpoint — is offered as an illustration of what *could* happen. The paper is candid about this; readers summarising it often are not.
- **The demonstration isn't in this paper.** The imperceptible-noise attack comes from the authors' own prior publication. That work exists and is cited, but this article's persuasive centrepiece is imported, not produced.
- **The $250 billion fraud figure is doing a lot of rhetorical work.** It is cited to a source, but it describes fraud in general, not algorithmic attacks — it establishes motive, not capability or occurrence.
- **The defence proposed is narrow.** Hashing data at capture would detect tampering *after* acquisition. It does nothing about an attack introduced at the moment of capture — the physician who rotates the camera, or the biller who chooses the code combination. The authors acknowledge adversarial defence generally "come[s] at a material degeneration of accuracy," and that robust-and-accurate models "remain an open problem in computer science."
- **A note on the author list:** one co-author, Joichi Ito, resigned from MIT later in 2019 over undisclosed funding ties unrelated to this paper's subject. This does not bear on the argument's validity, but a reader encountering the byline should know the record.
- **What this piece did well:** an unusually clear explanation of a technical concept for a general scientific audience; the crucial framing that adversarial vulnerability is *not* the same as inaccuracy; drawing in legal scholars rather than confining the issue to computer science; using real, documented billing behaviour rather than invented villains; presenting the genuine dilemma of whether to regulate early or late (the "procrastination principle") rather than simply demanding action; and honestly stating that these attacks have not yet been seen in healthcare.

# Statistics Spotlight

This article reports almost no statistics — it is an argument, not an analysis. So the concepts worth teaching are the ones its claims most depend on.

**1. Article type as an evidence tier — the check to run before any other.**
- *What it is:* Journals publish several kinds of document under one masthead: original research, systematic reviews, editorials, commentaries, correspondence, and policy essays like this one. Only some contain new data. The type is usually printed in small text near the title, and it almost never survives into a citation or a headline.
- *How it applies here:* This is a **Policy Forum** piece. PubMed carries no abstract for it, because there is no structured study to summarise — a quiet but reliable tell. Everything in it is either argument or a reference to work published elsewhere.
- *The theory, with an analogy:* Think of a newspaper. The front-page report, the opinion column, and the letters page all carry the paper's name and typeface, and a screenshot of any of them looks equally authoritative. Citing an op-ed as "The Times reported" is the same error as citing a Policy Forum as "Science found."
- *Watch out:* This is the single most common way a citation misleads without anyone lying. Before you weigh a paper's claim, find its type. Two fast checks: does it have a Methods section, and does PubMed show a structured abstract with numbers? If both answers are no, you are reading an argument — which can be excellent and still is not evidence that something occurred.

**2. Model confidence is not a probability of being right.**
- *What it is:* When a classifier outputs "99% confident," that number is generated by the model's own internal arithmetic. It is not a measured frequency, and nothing guarantees it corresponds to how often the model is actually correct.
- *How it applies here:* The same mole image, essentially unchanged to human eyes, went from "benign, >99% confidence" to "malignant, **100% confidence**." A model genuinely reporting a probability could not be certain in both directions about near-identical inputs. The confidence number moved because pixels were manipulated, not because the evidence changed.
- *The theory, with a worked example:* This is the calibration idea from your mental map, seen from its worst angle. A well-calibrated model's "90%" predictions come true about 90 of every 100 times. But calibration is measured on ordinary data; nothing about it constrains behaviour on data specifically engineered to break it. Picture a bathroom scale that is accurate to the gram for every normal object — then reads 400 pounds for one specific teacup, because someone found the one pressure pattern that confuses its sensor.
- *Watch out:* Displayed confidence is one of the most persuasive numbers in any AI interface and one of the least trustworthy. Whenever a system shows a confidence score, ask two things: was it calibrated on real data, and could this particular input have been chosen to exploit it? "100% confident" should read as a warning sign, not reassurance.

**3. Attack–defence asymmetry — why one side has a structurally harder job.**
- *What it is:* The authors state it precisely: "defenses must secure against all conceivable present and future attacks, whereas attacks need only defeat one or more specific defenses."
- *How it applies here:* It explains why they expect this to be "a cat-and-mouse game" rather than a solvable problem, and why they resist simply banning vulnerable algorithms — adequate resilience "is not imminent."
- *The theory, with a worked example:* This is the same logic as the multiple-comparisons problem you have met in study design, pointed in the opposite direction. A researcher testing 20 hypotheses will likely find one "significant" by chance alone — searching many possibilities makes an unlikely event likely. An attacker is doing exactly that search on purpose: trying thousands of tiny perturbations until one succeeds. The defender must survive *every* attempt; the attacker needs one hit. Locking twenty doors and windows protects a house only if all twenty hold.
- *Watch out:* Treat any claim that a system has been "made robust" or "secured against adversarial attacks" as provisional. Ask what class of attacks was tested, and note the authors' caveat that current defences cost real accuracy — a more robust model is usually a less accurate one, which is a trade-off, not a fix.

# Jargon Translator

- **Adversarial example:** an input deliberately engineered to make a machine-learning model give the wrong answer, usually while looking normal to a person.
- **Perturbation:** the small change added to the input — here, a calculated pattern of pixel adjustments too faint to see.
- **Classifier:** a model that sorts inputs into categories, such as benign versus malignant.
- **Confidence score:** the model's own stated certainty in its answer — an internal output, not a verified probability.
- **Upcoding:** billing for a more expensive service than the one actually provided.
- **ICD code:** the standardised diagnosis codes used for billing; the piece cites code 277.77 for metabolic syndrome.
- **Fee-for-service:** the US payment model where providers are paid per service delivered, creating the financial incentives the article describes.
- **Hash / fingerprint:** a short cryptographic summary of a file; if the file changes at all, the hash changes, which is how tampering becomes detectable.
- **CLIA:** the US Clinical Laboratory Improvement Amendments, the regulations governing lab quality standards.
- **Procrastination principle:** the internet-design idea that some problems are better left until they actually arrive, rather than pre-solved into rigid architecture.
- **Policy Forum:** Science's section for expert argument on science-policy questions — commentary, not original research.

# What You Can (and Can't) Say

**Fair to say:**
- "A 2019 Science Policy Forum argued that medical AI is vulnerable to adversarial attacks, illustrating a mole image that a model called benign with over 99% confidence and, after an invisible calculated perturbation, malignant with 100% confidence."
- "Adversarial examples have been demonstrated for essentially every class of machine-learning model, including simple logistic regression — not just deep learning."
- "The authors argue healthcare is a likely target because of documented incentives in medical billing, and note that robust-yet-accurate models remain an unsolved problem."
- "They proposed cryptographic fingerprinting of clinical data at capture as an incremental defence."

**Not fair to say:**
- "Science proved medical AI can be hacked" — this is an expert commentary, not a study; the underlying demonstrations are in the computer-science literature it cites.
- "Hackers are attacking hospital AI" — the article explicitly states such attacks "have yet to be found in the health care context."
- "This shows medical AI is unreliable" — the authors go out of their way to reject that reading: vulnerability to deliberate manipulation is a different property from ordinary accuracy.
- "Doctors are committing adversarial fraud" — the billing behaviours described are documented, but they are conventional practices, not algorithmic attacks.

# Bottom Line for Your Life

The most valuable thing in this entry is not the mole. It is the reminder that **"published in Science" describes where something appeared, not what kind of thing it is.** This is a thoughtful, well-sourced essay by serious people, and it would be misrepresented by anyone citing it as proof that medical AI has been attacked — which its own text denies. That distinction, between a journal's research pages and its opinion pages, is exactly the kind of thing that gets lost when a paper becomes a headline and then a confident claim in an argument. As for the substance: the genuinely useful idea is that an algorithm's accuracy and its resistance to being deliberately fooled are two separate properties, and almost everything you have read this fortnight measured only the first. Nothing here should change how you think about your own care. One study is one data point — and this one is not even a study. This is an educational breakdown, not medical advice.

---

**Sources** (based on articles retrieved from PubMed / PubMed Central; identifiers verified against the live NLM record — URL browsing is blocked in this environment, so links are constructed from that verified record):
- DOI: https://doi.org/10.1126/science.aaw4399
- PubMed: https://pubmed.ncbi.nlm.nih.gov/30898923/
- Full text (PMC author manuscript): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7657648/
