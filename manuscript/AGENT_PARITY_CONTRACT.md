# Manuscript ↔ Agent Parity Contract

**Status:** Canonical alignment specification, 2026-10-19. This is a design contract, not a claim that the full literary rewrite or live agent validation is complete.

## Authority and boundaries

- **Manuscript is doctrine.** It explains why a principle exists, when it fails, the competing view, how to practice it, and the human responsibility it protects.
- **Agent is execution.** It operationalizes selected disciplines as skills and Forge job stages, and may implement only capabilities it can actually verify.
- The book must stand on its own. It must not read like a CLI manual. The agent must not cite unapproved manuscript drafts as production policy.
- **The human is the Data Warrior.** AI and the Forge augment judgment; no named role is a permission token.
- **Foundation is separate.** Neither manuscript nor portable agent includes the user's organizational estate details.

## Canonical vocabulary

| Concept | Meaning in the book | Observable agent behavior | Canonical source in agent |
|---|---|---|---|
| The Way | Technical completion is not strategic success | Insist on decision, action and measurable outcome | `THE_WAY.md` |
| Know the Ground | Understand terrain, grain, owner, evidence and cost of error | Ask one substantive question at a time until ground gate is recorded | `skills/ground/know-the-ground/SKILL.md` |
| The Challenge | Test a proposed path against alternatives and failure conditions | Challenge assumptions before execution | `skills/practice/the-challenge/SKILL.md` |
| The Scroll / Living Scroll | Durable record of claims, decisions, contradictions and change | Persist evidence-backed context and the next action | `skills/practice/the-scroll/SKILL.md` |
| Battle Map | Explain obstacles, dependencies, verified progress and next step | Maintain inspectable execution/restart map | `skills/practice/the-battle-map/SKILL.md` |
| The Forge | Build only what has been grounded and scoped | `to-spec` → `to-steps` → current-step implementation, proof, reviews, human stop | `skills/forge/*` |
| Sword Drill | Bounded exercise yielding observable evidence | Agent skills supply reusable practice, but no exercise counts as executed until proof exists | Manuscript chapter endings / skills |
| Wind | Examine other schools, anti-patterns and tradeoffs | `name-the-wind`, `study-the-wind`, `wind-patterns` | `skills/wind/*` |
| Water | Adapt without worshiping completeness | `adapt`, `the-pivot`, `ship-the-eighty` | `skills/water/*` |
| Void | Perceive power, incentives, cultural constraints and missing evidence | `see-the-void`, `void-sight` | `skills/void/*` |
| Win the Room | Turn evidence into an accepted, refused or deferred decision | `win-the-room` | `skills/fire/win-the-room/SKILL.md` |
| Deshi / Rōnin / Kensei | Collaboration maturity: apprentice / practitioner / master | Collaboration styles; never grant permission by themselves | `THE_WAY.md` |
| Council | Strategist, Architect, Engineer, Guardian, Examiner, Sensei as perspectives | Perspectives for review, not six independent autonomous agents | `THE_WAY.md` |

## Chapter-by-chapter parity

| Book | Chapter | Required doctrinal bridge | Agent mapping |
|---|---|---|---|
| Earth | 1 The Way of the Data Warrior | Decision over artifact | THE_WAY |
| Earth | 2 Know Your Terrain | Ground gate, decision, grain, source, stakes | know-the-ground / grounding |
| Earth | 3 Establish the Foundation | Scope and minimal reversible action | simplicity / survey-the-ground |
| Earth | 4 Truth, Trust, and Data | Claims, evidence, provenance | grounding / the-contract |
| Earth | 5 Strategy Before Technology | Choose tools for fitness, not fashion | tool-choice |
| Water | 6 The Formless Practitioner | Adapt without losing purpose | adapt |
| Water | 7 Architectures That Evolve | Reversibility and tradeoffs | the-pivot / study-the-wind |
| Water | 8 Flow of Information | Engineering contracts and correctness | the-pipeline / the-contract |
| Water | 9 Learning and Unlearning | Enough evidence to act; 80% principle | ship-the-eighty |
| Fire | 10 Entering the Battle | When to commit | win-the-room |
| Fire | 11 The Battle Map | State, dependencies, blockers and next action | the-battle-map |
| Fire | 12 Execution Under Pressure | One verified step at a time | the-forge / draw-the-blade |
| Fire | 13 Decisions and Tradeoffs | Alternative and proof thresholds | to-spec / chart-the-path |
| Fire | 14 Knowing When to Stop | Stop conditions and human gates | forge verify/approve |
| Wind | 15 Know the Other Schools | Competing methods without caricature | study-the-wind |
| Wind | 16 Challenge Assumptions | Falsifiable counterarguments | the-challenge |
| Wind | 17 The Art of the Adversary | Failure modes and adversarial review | wind-patterns / test-the-steel |
| Wind | 18 Organizational Resistance | Incentives, adoption and influence | name-the-wind / win-the-room |
| Void | 19 Seeing What Is Not There | Missing evidence and power | see-the-void |
| Void | 20 Judgment Beyond Metrics | Consequences beyond reported KPIs | void-sight |
| Void | 21 Intuition and Experience | Distinguish judgment from unchecked belief | the-challenge |
| Void | 22 Mastery in the Age of AI | AI augments; human remains accountable | THE_WAY / AGENTS |
| People | 23 Leadership and Service | Adoption and ownership | win-the-room |
| People | 24 The Council | Six review perspectives, no implied autonomy | THE_WAY |
| People | 25 Collaboration and Conflict | Transparent disagreement and decision rights | the-scroll |
| People | 26 Developing Other Warriors | Deshi / Rōnin / Kensei are styles, not permissions | THE_WAY |
| Tools | 27 The Sword Is Not the Warrior | Tools subordinate to mission | tool-choice |
| Tools | 28 Engineering Disciplines | Contracts, tests, incremental correctness | the-pipeline / test-the-steel |
| Tools | 29 AI Agents and Skills | Host skills, boundaries and provenance | ask-the-warrior / AGENTS |
| Tools | 30 Governance by Design | Evidence, independent reviews and authorization | review-the-work / forge verify |
| Tools | 31 Building the Living System | Ground→spec→steps→proof→human approval | setup-the-forge / the-forge |
| Practice | 32 Training Through Challenges | Deliberate bounded drills | the-challenge |
| Practice | 33 The Living Scroll | Continuity across sessions | the-scroll |
| Practice | 34 From Battle Map to Outcome | Verified milestones, outcome tracking | the-battle-map |
| Practice | 35 Reflection and the Chronicle | Post-action learning | lessons-of-battle |
| Practice | 36 The Never-Ending Way | Continuous learning, not permanent draft | THE_WAY |

## Critical parity distinctions

1. **The Council is not six implemented agents.** The repo explicitly says these are perspectives, not separate skills. The book must not promise autonomous Council execution.
2. **Approval is not identity verification.** The CLI `--authorized` flag is an operator attestation, not cryptographic authentication. No manuscript example should imply otherwise.
3. **Synthetic demos are not production proof.** The Forge README warns some demonstration paths accept synthetic PASS artifacts. Explain the difference between proof shape and independently verified evidence.
4. **Agent workflow is narrower than the book.** The book covers ethics, culture, leadership and strategic judgment beyond what current skills enforce.
5. **Five original rings vs modern extensions.** Earth/Water/Fire/Wind/Void are the Musashi-inspired core; People/Tools/Practice are the author's additions. The Forge is a Tools implementation, not a sixth original ring.
6. **One question at a time** applies to interactive Ground, Challenge and Scroll modes, not every conversation or chapter.

## Editorial quality gate

Each of 36 chapters must contain: (a) a distinctive opening tension; (b) sustained original narrative rather than repeated template paragraphs; (c) governing principle and credible counterexample; (d) source-supported detail or clearly labeled illustration; (e) a Sword Drill with concrete deliverable, proof and failure condition; (f) an agent parity note in an appendix or production crosswalk, not intrusive product promotion in the main prose.

## Acceptance test

For each mapped agent capability, verify the skill exists, identify exact entry point, run a representative scenario where possible, compare resulting evidence and behavior to manuscript doctrine, record mismatches, and refuse to label parity 'passed' without an executed test. Update manuscript and agent together for any semantic change.

**Current verdict:** vocabulary and architectural parity are documented here; narrative completeness, behavioral parity and production validation remain open.
