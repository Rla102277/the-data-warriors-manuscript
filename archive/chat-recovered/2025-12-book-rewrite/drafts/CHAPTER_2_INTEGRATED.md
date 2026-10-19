# CHAPTER 2
## The Stated Problem vs. The Real Problem

*"You must understand that there is more than one path to the top of the mountain."*  
— Miyamoto Musashi, *The Book of Five Rings*

Musashi understood that the obvious path is rarely the right path. The direct route up a mountain might be the steepest, the most exposed, or guarded by the enemy. The samurai who survives learns to see what others miss—the hidden trail, the vulnerable flank, the real objective beneath the apparent one.

In data work, the stated problem is almost never the real problem.

An executive says, "We need better forecasting." What they mean is, "I need to know whether to build a second warehouse or not."

A VP says, "Run a customer churn analysis." What they mean is, "Revenue is flat and the board is asking questions I can't answer."

A director says, "Optimize our marketing spend." What they mean is, "Prove that my campaign worked so I can justify next quarter's budget."

Your job isn't to answer the question they asked. Your job is to solve the problem they have.

And those are almost never the same thing.

---

## The Churn Analysis That Wasn't

The request came directly from the Chief Marketing Officer at a large e-commerce retailer. They were concerned about a recent, unexplained surge in customer churn following a massive holiday promotion. The CMO tasked my analytics team with an urgent project: "We need a deep-dive customer churn analysis to pinpoint exactly which channels are failing and why customers are leaving after they redeem their promotional codes."

The assumption was clear: the marketing communication or the fulfillment process was broken, and we needed to fix the "leaky bucket" post-sale.

We began pulling data on promotional codes, post-redemption purchase history, and customer service contacts. Initially, the data seemed complex, but a pattern emerged. We weren't seeing complaints about delayed shipping or incorrect billing, which would support the marketing/fulfillment failure theory. Instead, customer service logs showed a dramatic spike in product return requests specifically related to the quality of a single, high-volume item that was bundled heavily with the promotion—a popular brand-new smart home speaker.

The real revelation came during a casual weekly review with a frontline product manager. She commented, "We're swamped with returns on that new speaker; the failure rate out of the box is double the accepted tolerance. Customers are furious."

It was then that I realized the stated problem—churn analysis—was merely a symptom. The real issue was product quality control.

I reframed the work immediately. Instead of focusing on marketing channel optimization, the analysis shifted to connecting the specific product SKU return rates to customer lifetime value (CLV) losses. I scheduled a follow-up meeting with the CMO and the VP of Product to present this pivot. I explained that while we could analyze which communication channels led to churn, the highest-impact action was stopping the churn at the source. The real problem was the faulty speaker, and solving it required a fix in procurement, not marketing.

Their initial reaction was surprise, but when shown the data connecting the speaker's high failure rate directly to significant CLV erosion, they immediately supported the pivot, shifting the focus and budget to the Product team.

The faulty product line was temporarily pulled, corrected, and re-released with proper quality control standards. Customer churn immediately stabilized.

If we had simply optimized the marketing communications as requested, we would have kept pushing a broken product and incurred far greater customer acquisition costs trying to replace those who left, failing to solve the core product quality fix that was truly necessary.

---

## Why Stated Problems Mislead

There are three reasons the stated problem is almost never the real problem:

**Reason 1: People diagnose based on symptoms, not root causes.**

When revenue drops, executives say "we need better sales forecasting." But the real problem might be pricing, product quality, competitive pressure, or channel conflict. The forecasting request is the symptom. The underlying business pressure is the cause.

Most stakeholders aren't trained to diagnose root causes. They're reacting to pain. Your job is to find the injury beneath the pain.

**Reason 2: People request what they know how to ask for.**

If your only tool is a hammer, every problem looks like a nail.

A marketing VP knows how to request "customer segmentation" because that's a familiar analytical deliverable. But what they actually need might be a pricing strategy, a product positioning shift, or a channel allocation model. They're requesting the tool they recognize, not the solution they need.

**Reason 3: People ask for analysis when they need political cover.**

Sometimes the stated problem is a fig leaf.

An executive already knows what decision they need to make, but it's politically risky. So they commission analysis to validate the decision and provide cover. "We ran the numbers" sounds better than "I had a hunch."

If you don't recognize this dynamic, you'll waste time building rigorous analysis for a problem that was already solved before you started.

---

## How to Find the Real Problem

Before you accept any analytical request, conduct a diagnostic conversation. Here's the framework:

**Question 1: "What happens if we don't do this analysis?"**

This reveals urgency and stakes.

If the answer is "nothing immediate," you're working on a nice-to-have, not a business-critical problem. Deprioritize it.

If the answer is "we'll miss our Q4 targets," you're working on something that matters. Dig deeper.

**Question 2: "What decision does this analysis inform?"**

Force them to name the specific action they'll take based on your work.

If they can't name the decision, the request is exploratory research disguised as analysis. That's fine—but price it and scope it accordingly. Exploratory work shouldn't consume the same resources as decision-critical work.

**Question 3: "What do you think the answer is?"**

Most stakeholders already have a hypothesis. They might not admit it, but they do.

Get them to state it. "I think the problem is our pricing." "I suspect it's a channel issue." "I believe we're targeting the wrong customers."

Their hypothesis tells you what they're actually worried about. That's the real problem, not the stated request.

**Question 4: "Who else cares about this?"**

This reveals the political landscape.

If multiple executives with conflicting agendas care about your analysis, you're not solving an analytical problem. You're arbitrating a political dispute with data. Different game. Different rules.

**Question 5: "What constraints do we have?"**

Budget. Timeline. Technology. Data availability. Organizational capacity.

These constraints often reveal the real problem. If they need an answer in two weeks, they're not asking for comprehensive research—they're asking for enough evidence to justify a decision they need to make quickly.

---

## The Discipline of Reframing

Once you understand the real problem, you need permission to solve it instead of the stated problem.

This is delicate. You can't just say "you're asking for the wrong thing." That's condescending. And even if you're right, nobody wants to hear it.

Here's the reframe technique:

**Step 1: Acknowledge the stated problem.**

"You asked for a churn analysis focused on marketing channels."

**Step 2: Present what you found.**

"While examining the data, I found that 80% of the churn is driven by returns on a specific product."

**Step 3: Offer the pivot.**

"I can deliver the channel analysis you requested. But I think the higher-impact work is quantifying the CLV loss from the product quality issue. That solves the churn at the source."

**Step 4: Give them the choice.**

"Which would you prefer?"

This approach does three things:

1. It respects their original request
2. It demonstrates that you did the work to understand the real problem
3. It gives them agency to choose the better path

Most executives will choose the real problem once you show them the door. They're not stupid. They're busy. They requested what they thought they needed based on limited information. When you give them better information, they'll make a better choice.

---

## When the Real Problem Is Political

Sometimes the real problem isn't analytical at all. It's political.

Two executives are fighting over budget allocation. A strategy is failing and someone needs a scapegoat. A department is trying to justify its existence.

When you stumble into these situations, data won't solve the problem. Data will become a weapon in someone else's fight.

Here's how to recognize political problems disguised as analytical requests:

**Signal 1: Vague, shifting requirements.**

"We need to understand customer behavior." Okay, which behavior? "All of it." That's not an analytical request. That's a stalling tactic.

**Signal 2: Multiple stakeholders with contradictory success criteria.**

One executive wants proof that the new strategy is working. Another wants proof that it's failing. Your analysis will be used to support whoever wins the argument.

**Signal 3: The answer doesn't matter.**

You present three options. They ignore all three and do something else. That's not a data problem. That's a "we needed to look like we were being rigorous" problem.

When you recognize political problems, you have two choices:

**Option 1: Decline the work.**

"Based on our conversation, I don't think this is primarily an analytical problem. I'm concerned that any analysis I deliver will be misused or ignored. I'd recommend resolving the strategic disagreement first, then coming back to me with clearer requirements."

**Option 2: Document everything.**

If you can't decline, protect yourself. Document the requirements. Get sign-off. Build exactly what was requested, no more, no less. When it gets ignored or weaponized, you have proof that you delivered what was asked for.

Neither option is satisfying. But political problems don't have analytical solutions. The sooner you recognize that, the less time you waste.

---

## The Foundation of Trust

When you consistently solve the real problem instead of the stated problem, you build a reputation.

Executives start coming to you earlier in their thinking. They bring you half-formed problems and ask for help diagnosing before they make requests. They trust you to tell them what they need to hear, not just what they want to hear.

That's the goal.

Not to be the person who answers questions. To be the person who helps figure out the right questions to ask.

Most analysts never make that leap. They're stuck in order-taker mode: someone requests analysis, they build it, they deliver it, they move on to the next request.

That's a job. Not a career.

The analysts who become indispensable are the ones who solve problems that weren't even articulated yet. They see the real problem beneath the stated problem. They reframe the work. They guide the diagnosis, not just the solution.

That's the work.

That's always been the work.

---

## SWORD DRILLS

*Before accepting any analytical request:*

1. **Practice the diagnostic conversation.** Take your next three requests and ask all five questions before starting: What happens if we don't do this? What decision does it inform? What do you think the answer is? Who else cares? What constraints exist?

2. **Identify one project where you solved the stated problem** but missed the real problem. Write down: What was requested? What was the real issue? How could you have discovered it earlier?

3. **Review your current projects.** For each one, write down the stated problem and the real problem. If they're the same, you either got lucky or you haven't dug deep enough.

4. **Find one political problem** disguised as an analytical request in your backlog. Document the conflicting stakeholder agendas. Decide: decline the work or protect yourself with documentation?

5. **Build your reframe template.** Practice the four-step reframe on a low-stakes project: Acknowledge the stated problem, present what you found, offer the pivot, give them the choice.

---

**Next:** In Chapter 3, we'll explore how to choose the right tools for the problem you're solving—because the best tool is the one that works, not the one that looks impressive on your resume.
