# CHAPTER 5
## Adapt or Die: The Mid-Project Pivot

*"Water adopts the shape of its receptacle, it is sometimes a trickle and sometimes a wild sea."*  
— Miyamoto Musashi, *The Book of Five Rings*

Musashi's Water Book is about adaptability. Water doesn't fight the terrain—it flows around obstacles, changes shape to fit circumstances, and finds the path of least resistance without losing its essential nature.

A samurai who commits rigidly to a single strategy dies when circumstances change. A data professional who refuses to pivot when reality contradicts the plan delivers useless work on time and under budget.

Same outcome. Different battlefield.

Here's the truth about data projects: they never go according to plan.

Requirements change. Stakeholders pivot. Data quality issues emerge. The political landscape shifts. The technology doesn't work as expected. The business priority that seemed critical three weeks ago is suddenly irrelevant.

Most analysts respond to this reality by clinging harder to the original plan. They've invested time. They've committed to a methodology. They've told people what they're building. Changing course feels like failure.

It's not failure. It's water.

---

## The Neural Network Nobody Needed

The project was to build a comprehensive Customer Churn Predictor for our retail subscription service. We committed to a complex Neural Network architecture. Our initial thinking was that a deep learning approach was necessary to capture the highly non-linear relationship between hundreds of diverse customer features—everything from login frequency and support tickets to average basket size and social media engagement. We believed only a neural network had the capacity to handle this volume and complexity to achieve the "best" prediction score.

We were about six weeks into the nine-week project timeline. The model training was proving incredibly difficult; the neural network was overfitting, and the performance on the validation set was only marginally better than a simple logistic regression model.

The "Oh Shit" moment arrived during a weekly check-in when a key stakeholder—the Head of Customer Success—said, "I don't care about a 95% accuracy score if the model can't tell me why someone is predicted to churn."

We realized the core business need wasn't just prediction—high accuracy. It was interpretability to drive specific interventions. Our beautiful black-box model couldn't provide the simple drivers—feature importance—the team needed to act. The internal panic centered on the huge time sink we had already invested in a model that was practically useless for the business.

I immediately convened the team and announced we were switching from the complex Neural Network to an Explainable Gradient Boosting Machine (XGBoost) framework, which offers high accuracy but also provides clear feature importance scores. I sold the pivot to leadership not as a failure, but as an upgrade in strategic utility. I explained we were trading a small fraction of potential prediction accuracy for 100% interpretability, which was the true driver of business value.

There was initial resistance from one data scientist who felt the neural network represented a superior technical solution, but the business value argument won out.

The pivot was highly successful. The XGBoost model provided clear drivers—like "three support tickets in 60 days"—that the Customer Success team could immediately build intervention strategies around.

If we had stubbornly stuck to the original plan, we would have delivered a technologically impressive model that gathered dust because the business couldn't use its predictions to take action.

---

## The Sunk Cost Trap

The biggest obstacle to pivoting isn't technical. It's psychological.

You've invested six weeks. You've told leadership what you're building. You've committed to a methodology. You've mentally prepared to deliver a specific thing.

Pivoting feels like admitting failure. It feels like wasted time. It feels like you didn't plan properly.

But the sunk cost fallacy kills more projects than bad methodology.

The time you've already invested is gone. The only question that matters is: "What's the best use of the time remaining?"

If the answer is "finish the original plan even though it's wrong," you're making an emotional decision, not a strategic one.

Here's the hard truth: sometimes the right move is to throw out weeks of work and start over. Not because you failed to plan. But because reality proved your plan wrong.

Water doesn't fight the terrain. Water adapts.

---

## When to Pivot

Not every obstacle requires a pivot. Sometimes the right move is to push through. Sometimes the problem is execution, not strategy.

Here are the signals that indicate a true pivot is necessary:

**Signal 1: The core business need has changed.**

You started building a forecasting model. Three weeks in, the executive who commissioned it gets promoted. The new executive doesn't care about forecasts—they care about cost reduction.

Your original project is now irrelevant. Finishing it on time delivers zero value.

Pivot or kill the project entirely.

**Signal 2: The data doesn't support the original approach.**

You planned to use transaction history to predict customer behavior. You discover the transaction data is incomplete, inconsistent, and fundamentally unreliable.

You can spend weeks trying to clean it, or you can pivot to a different data source that actually works.

Sometimes the data tells you the original plan won't work. Listen to it.

**Signal 3: The solution won't be used.**

This is what happened with our neural network. We could have delivered the model. It would have been technically impressive. And it would have sat unused because it didn't solve the actual business problem.

If you realize mid-project that your deliverable won't drive action, stop. Figure out what would drive action. Build that instead.

**Signal 4: A better path emerges.**

Sometimes you discover halfway through that there's a simpler, faster, more effective way to solve the problem.

This isn't failure. This is learning. The work you've done so far revealed information you didn't have at the start. Use that information.

---

## How to Execute a Pivot

Pivoting isn't just deciding to change direction. It's managing the change without destroying credibility or momentum.

Here's the framework:

**Step 1: Acknowledge the sunk cost explicitly.**

"We've invested six weeks in this approach. That time is gone. The question now is how to use the remaining three weeks most effectively."

By naming the sunk cost out loud, you eliminate the psychological pressure to justify it. You're not pretending it didn't happen. You're making it irrelevant to the decision ahead.

**Step 2: Present the new information that justifies the pivot.**

"The stakeholder feedback revealed that interpretability is more important than raw accuracy."

Or: "The data quality issues are worse than we initially assessed."

Or: "The business priority has shifted to cost reduction rather than forecasting."

The pivot isn't random. It's a response to new information. Make that information explicit.

**Step 3: Frame the pivot as an upgrade, not a failure.**

"We're not abandoning the original approach because it failed. We're upgrading to a better solution based on what we've learned."

This isn't spin. It's accurate. You learned something that makes a different approach more valuable. That's progress.

**Step 4: Show the new path clearly.**

Don't just say "we need to change." Say "here's specifically what we're building instead, here's why it's better, and here's the timeline."

Vague pivots create anxiety. Clear pivots create confidence.

**Step 5: Get explicit buy-in.**

"Does this make sense? Do you support this pivot?"

Don't assume. Ask. Get confirmation. If leadership doesn't support the pivot, you need to know that now, not three weeks from now when you deliver something they didn't want.

---

## The One-Week Rule

Here's a heuristic I've used for years: if you're more than one week into a project and you realize the approach is fundamentally wrong, pivot immediately.

One week is recoverable. You haven't built organizational momentum yet. You haven't created dependencies. You can change direction without major disruption.

But if you wait until you're six weeks in, the psychological and organizational pressure to finish the original plan becomes overwhelming. Even when everyone knows it's wrong, the inertia is too strong.

Pivot early. The longer you wait, the harder it becomes.

---

## When Not to Pivot

Sometimes the right move is to push through the difficulty.

Here's how to tell the difference between "this approach is wrong" and "this approach is just hard":

**Question 1: Is the core strategy still valid?**

If the business need hasn't changed and the approach is still theoretically sound, you're probably just hitting execution challenges. Push through.

**Question 2: Is this a solvable technical problem?**

If the issue is "the model isn't converging" or "the query is slow," that's an execution problem, not a strategy problem. Keep working.

**Question 3: Will more time actually help?**

If you're stuck on a data quality issue that won't improve with more time, pivot. If you're stuck on a complex implementation that will get clearer as you work through it, keep going.

The difference between quitting and pivoting is this: quitting is giving up because it's hard. Pivoting is changing direction because you have better information.

---

## Adaptability as a Skill

Most data professionals treat planning as a one-time activity. They invest heavily in the upfront plan, then execute that plan regardless of what they learn along the way.

That's not strategy. That's rigidity.

True strategic thinking is continuous. You plan. You execute. You learn. You adapt. You re-plan. You execute again.

The analysts who thrive aren't the ones with perfect plans. They're the ones who adapt quickly when reality proves their plans wrong.

Water doesn't fight the rock. Water flows around it.

Be water.

---

## SWORD DRILLS

*Before committing rigidly to any plan:*

1. **Identify your sunk costs** on current projects. For each one, write down: How much time have I invested? If I were starting today with what I know now, would I choose this approach? If not, what's preventing the pivot?

2. **Practice recognizing the four pivot signals.** Review your last five projects. Did any of them show these signals: Core business need changed? Data doesn't support the approach? Solution won't be used? Better path emerged? If yes, did you pivot or push through?

3. **Run the pivot execution framework** on a small project this week. Practice all five steps: Acknowledge sunk cost, present new information, frame as upgrade, show new path, get buy-in. Do it on something low-stakes to build the muscle.

4. **Apply the one-week rule.** For any project you're currently more than one week into, ask: Is the fundamental approach still valid? If not, pivot today, not next month.

5. **Distinguish between hard and wrong.** Pick one project that's giving you trouble. Ask the three questions: Is the core strategy still valid? Is this a solvable technical problem? Will more time actually help? Based on the answers, decide: push through or pivot?

---

**Next:** In Chapter 6, we'll explore what it feels like when everything clicks—the flow state where problems solve themselves and hours disappear.
