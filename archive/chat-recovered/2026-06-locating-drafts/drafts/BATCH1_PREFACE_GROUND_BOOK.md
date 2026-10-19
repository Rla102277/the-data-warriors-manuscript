# THE DATA WARRIOR

## Applying Miyamoto Musashi's Strategy to Modern Analytics Careers

*Batch 1: Preface and the Ground Book (Chapters 1 through 4)*

---

# Preface: The Warrior and the Weight

I didn't find Musashi in a dojo. I found him at 270 pounds, recently divorced, standing at the top of a zipline platform in the Dominican Republic, too scared to jump while my daughter waited below.

That trip was supposed to be a reset. Father and daughter, ocean and sun, a week of proving that life after the divorce still had good things in it. Instead it became an audit. The zipline stairs left me winded and shaking. A banana boat threw me into the ocean, and I had to swim to shore while the boat circled back for everyone else. My daughter was kind about it. Kids are kind about things that break your heart.

I'm a data guy. I've spent twenty-four years building models, pipelines, and dashboards across travel, retail, government, restaurants, and healthcare. I understand inputs and outputs better than I understand most things. And somewhere over the Gulf on the flight home, I ran the analysis I'd been avoiding. The inputs of my life had produced exactly the outputs you'd expect. Garbage in, garbage out applies to more than databases.

So I started fixing the inputs. Slowly, the way you fix anything real. And while I was doing that, I went looking for something to read that wasn't another book about machine learning pipelines, because I had a shelf of those and none of them had ever told me why my best work kept dying in conference rooms.

That's when I found Miyamoto Musashi.

Musashi was a seventeenth-century Japanese swordsman who fought more than sixty duels and lost none of them. Near the end of his life he climbed into a cave and wrote down what he knew. The result, The Book of Five Rings, is short, blunt, and almost rudely practical. It is not a book about swords. It is a book about strategy, written by a man who had bet his life on his strategy sixty times and collected sixty times.

Reading it, I kept having the same uncomfortable experience. He would describe a duel, and I would see a project. He would describe an opponent's rhythm, and I would see a steering committee. He wrote, four hundred years ago, about knowing the ground before you fight on it, and I thought about every model I'd ever built that was technically correct and organizationally dead on arrival.

Here is the thing nobody tells you when you enter this field. The technical work is maybe half the job. The other half is terrain, timing, people, and judgment. We train relentlessly for the first half and leave the second half to luck. Then we're confused when the analyst with weaker SQL but better instincts gets the promotion, the budget, and the room's attention.

Musashi would not have been confused. He spent as many pages on reading opponents and choosing ground as he did on cutting. He understood that technique without strategy is just expensive motion.

This book is my attempt to write down the second half of the job, using Musashi's five books as the frame, because his frame is better than any I could invent. Ground, Water, Fire, Wind, Void. Foundations, adaptability, action, awareness of failure, and finally the things you can only learn by doing the work long enough that it becomes part of you.

I want you to know up front who's talking to you. Not a consultant. Not a thought leader. A guy who built models nobody used, made a fifty-million-dollar call that worked, inherited an ETL system held together with ColdFusion and prayer, sat in rooms where my analysis was right and I still lost, and kept going. The stories in this book are mine. The bruises are real. Where I don't have a story, I'll tell you that instead of inventing one, because a strategy book that lies to you is worse than no book at all.

One more thing about the weight, since I opened with it. I lost eighty-five pounds. It took discipline, medicine, running, and a couple of years. I mention it not because this is a weight loss book but because it taught me the thing Musashi keeps insisting on from his very first pages: discipline transfers. The same person who couldn't make himself climb a zipline platform learned to run for hours. The same habits that fixed my body, small consistent inputs, honest measurement, no heroics, are the habits that make a data career work. There is no trick. There is only the Way, walked daily.

Musashi closes his introduction with a demand I've adopted as my own: demand simplicity, embrace discipline. Everything in this book is downstream of those four words.

Let's begin where he begins. On the ground.

---

# PART I: THE GROUND BOOK

*Foundations*

---

# Chapter 1: Know the Ground

> "Know the smallest things and the biggest things, the shallowest things and the deepest things." - Miyamoto Musashi

Early in my career I built the best model nobody ever used.

It was a customer segmentation model for a company I won't name, and it was beautiful. Seven clusters, each one statistically distinct, each one with a personality you could practically shake hands with. The Bargain Loyalists. The High-Touch Spenders. I had silhouette scores. I had validation holdouts. I rehearsed the presentation in my car.

The meeting lasted eleven minutes. A vice president looked at my seven gorgeous clusters and asked one question: "Which of these can our campaign system actually target?"

The answer was none of them. The marketing platform could segment customers on a handful of basic fields. My clusters were built from dozens of behavioral variables that existed only in my analysis environment. I had built a map of a country we had no roads into. The model was correct. The model was also useless, and useless beat correct, the way it always does.

I spent the drive home angry at the marketing platform, which tells you how young I was. The platform wasn't the problem. The problem was that I had spent six weeks in the data and zero hours learning the terrain I was building for.

## Strategy starts with ground

Musashi opens his book with earth, and he means it literally. Before any duel he studied the ground. Where the sun would be. Where the footing was bad. Where he could drive an opponent. He considered it malpractice to fight on ground you hadn't read, and he watched men die for skipping that step.

In our work, the ground is everything around the analysis. It is the business model, the politics, the systems, the incentives, and the unwritten rules. It is what the company says it wants and what it actually rewards, which are rarely the same thing. Every analysis you will ever produce lands on this terrain, and the terrain decides whether it lives.

Most analysts treat terrain as someone else's job. We are trained to start with the data, and the data feels like the whole world because it's the part we control. But the data is the sword, not the ground. A perfect cut on the wrong ground still loses the fight.

## Reading the terrain

Over the years I've boiled terrain reading down to questions I now ask before touching a single table. They are not clever. That's the point. Clever comes later. These come first.

**Who decides?** Not who asked for the analysis. Who will actually make the call when it's done? Sometimes the person who commissioned the work is gathering ammunition for a decision their boss owns. If you don't know whose hand is on the lever, you don't know who you're working for.

**What can they actually change?** This is the question that would have saved my segmentation model. Every decision-maker operates inside constraints: systems, budgets, contracts, headcount, politics. An insight that requires pulling a lever nobody can reach is trivia. Find the levers first, then analyze the things the levers control.

**What happens if nothing changes?** This tells you the stakes and the urgency. If the honest answer is "not much," your work is a curiosity, and you should calibrate your investment accordingly. If the answer is "we miss the quarter," you're holding something live, and the terrain will be crowded with people who care about where it lands.

**What does this company actually reward?** Read the promotions, not the mission statement. If the company says it's data-driven but every recent promotion went to people who shipped fast and broke things, you are on move-fast terrain, and your three-month rigorous study is going to feel like an obstacle to the people on it.

**Where does the data actually live, and is it what the diagram says it is?** Every organization has an architecture diagram and an architecture. They are cousins, not twins. The diagram says the customer table is the source of truth. The terrain says there are four customer tables, two teams that distrust each other's, and one analyst in finance with a spreadsheet that everyone secretly believes over all of them. You cannot learn this from documentation. You learn it by asking, and by being the kind of person people tell things to.

## Walking the ground

Reading terrain is not a phase you complete. It's a practice you maintain. The ground moves. Reorgs redraw the map. A new executive arrives and the levers change hands. The company that rewarded rigor starts rewarding speed. I once watched a six-month roadmap die in a single reorg. The plan wasn't wrong. The ground moved.

So walk the ground regularly. Have the coffees. Sit in the business reviews even when your project isn't on the agenda, especially when it isn't, because that's when people say what they actually think. Learn what the sales team complains about, because today's complaint is next quarter's analytics request, and you'll be the only analyst in the building who saw it coming.

Musashi put it simply: the warrior who knows the ground chooses where the fight happens. The one who doesn't fights wherever he's standing when trouble finds him. Twenty-four years in, I can tell you that most failed analytics projects didn't lose the fight. They lost the ground, before the fight ever started.

## Sword Drills

1. **Map the deciders.** Take your current project and write down, by name, who will make the final decision it informs. If you can't, you've found this week's work.
2. **Inventory the levers.** List every action the decision-maker could realistically take based on your analysis. If the list is short, narrow your analysis to serve it. If it's empty, stop and renegotiate the project.
3. **Run the promotion audit.** List the last five people promoted in your organization and what they were known for. That list is the terrain's truth, whatever the values poster says.
4. **Find the shadow sources.** Identify one spreadsheet, side system, or unofficial dataset that people trust more than the official source. Understand why. The gap between official and trusted is a map of the terrain's fault lines.
5. **Walk one new piece of ground.** This week, attend one meeting you don't strictly need to attend, in a part of the business you don't serve yet. Take no laptop. Just listen.

---

# Chapter 2: The Stated Problem vs the Real Problem

> "Perceive that which cannot be seen with the eye." - Miyamoto Musashi

An executive once asked me to build a churn model. Customers were leaving, the board was asking questions, and the request came down in the standard form: figure out who's going to cancel so we can save them.

So I built it. And the model worked, in the sense that it found a signal. The strongest predictor of churn, by a wide margin, was ownership of one specific product. Customers who owned it left at multiples of the base rate. The retention team got excited. They wanted to target those customers with offers, discounts, win-back campaigns, the whole arsenal.

But the signal bothered me. Why would owning a product make you leave? So I pulled the support tickets, which nobody had asked me to do, and there it was. The product was failing. Units were dying young, support couldn't fix them, and customers weren't churning so much as escaping. The board had asked a retention question. The data was answering a quality question. No discount in the world saves a customer whose device keeps breaking. The fix wasn't a model. The fix was an engineering escalation and an honest conversation with product leadership, which is what eventually happened, after the uncomfortable meeting where I explained that the churn model they'd commissioned was actually a defect report.

I've come to believe this is the single most common situation in analytics, and almost nobody trains you for it. The problem you are handed is almost never the problem. It is a translation of the problem, made by someone upstream, usually with good intentions and incomplete information, and your first job is to translate it back.

## How problems get pre-translated

By the time a request reaches you, it has usually passed through several hands, and each hand has converted it a little. The board says "churn is up." The CEO hears "we need retention." The VP hears "we need a retention program." The director hears "we need to know who to target." And you receive "build a churn model," a request so specific and reasonable-sounding that it would feel rude to question it.

But every step of that chain involved an assumption, and any one of them can be wrong. The deadliest version is when the request arrives pre-solved: not "we have a problem" but "build me this thing." A request that names the deliverable has already decided what the problem is. Your leverage, and most of your value, lives in checking that decision before you honor it.

This is not insubordination. This is the job. A surgeon who operates on whatever the patient self-diagnosed is not being respectful. He's being negligent.

## Reversing the translation

The technique is unglamorous: you ask questions until the original problem comes back into view, and you do it in a way that doesn't make the requester feel interrogated.

The question I lean on hardest is some version of **"what will you do differently depending on what this shows?"** It's polite, it sounds like diligence, and it is a depth charge. If the answer is crisp, you've confirmed the problem and learned exactly what your output needs to look like. If the answer is vague, you've just learned the request is really a hope, and hopes need shaping before they need models.

The second question is **"what made this urgent now?"** Problems don't schedule themselves. Something happened. A board meeting, a competitor's move, a bad quarter, a new executive wanting a win. The trigger tells you what the work is actually for, and what it's actually for is the real spec.

The third is the one I used on the churn project without knowing I was using a technique: **follow the signal past the boundary of your assignment.** The assignment said model the churners. The signal said look at the product. The assignment is a fence someone else built. The signal doesn't know the fence is there, and neither should you, at least not until you've looked over it.

## When the stated problem is stated that way on purpose

A harder truth, and I'd be lying if I left it out: sometimes the translation isn't an accident. Sometimes you're asked to study the wrong problem because the right one is politically expensive. An executive who owns the failing product would much rather fund a churn model than a quality investigation. Nobody will tell you this. The terrain will tell you, if you've been walking it, which is why this chapter comes after the last one.

When you find yourself there, you have choices, and none of them are free. You can answer the stated question and quietly attach what you found, which is what I did, framing the quality issue as an unexpected finding rather than an accusation. You can escalate. You can let it go. The right move depends on the stakes, your capital, and your read of the room, all subjects of the Fire Book later. The non-negotiable part is internal: you do not let yourself unknow what you found. Plenty of analysts learn to stop looking past the fence because what's beyond it is inconvenient. That's the day the work stops being a craft and starts being a performance.

Musashi has a phrase for the skill this chapter is about. He calls it perceiving what cannot be seen. He didn't mean magic. He meant that the visible thing, the stance, the stated request, is information about the hidden thing, the intention, the real problem, and that a strategist reads through the first to the second as a matter of routine. Four hundred years later, it's still the best one-line job description for an analyst I've found.

## Sword Drills

1. **Ask the depth charge.** On your next incoming request, ask "what will you do differently depending on what this shows?" before you write a line of code. Write the answer down and design backward from it.
2. **Find the trigger.** For your current project, identify the event that made it urgent. If you don't know, ask "what's the deadline attached to, on your side?" The answer is the real spec.
3. **Rewrite one request.** Take a recent ask that arrived as a deliverable ("build a dashboard," "pull these numbers") and rewrite it as the problem you believe sits underneath. Show your rewrite to the requester and ask if you've got it right. Watch what happens to the scope.
4. **Cross one fence.** Pick a finding from your recent work that pointed somewhere outside your assignment, and spend one hour following it. You owe nobody a report yet. You owe yourself the look.
5. **Run the post-mortem in advance.** Before starting your next significant analysis, write one sentence: "If this project fails, it will be because we answered the wrong question, and the wrong question will have been ____." Filling in that blank is cheap insurance.

---

# Chapter 3: Choose the Right Tool

> "You should not have a favorite weapon." - Miyamoto Musashi

The most expensive technology lesson of my career was taught to me by ColdFusion.

If you're young enough not to know what ColdFusion is, I both envy you and need you to sit down for this story. At one stop in my career I inherited the data pipeline that fed a meaningful chunk of the company's reporting. The person who built it was long gone. The documentation was the code, and the code was ColdFusion, a web application language that was never meant to run ETL, pressed into service years earlier by someone who knew it well and presumably needed something working by Friday.

And here's the thing: it worked. For years it worked. It was the duct tape that held a business together, and like all good duct tape, it was invisible right up until it failed.

When it failed, it failed at the worst possible time, the way critical systems always seem to, and the recovery turned into a six-figure emergency. Roughly $150,000 by the time the consultants, the overtime, and the rebuilt processes were tallied, not counting the meetings, and there were so many meetings. The post-mortem could have been one sentence: someone used their favorite tool instead of the right one, and the bill arrived a decade later, addressed to me.

I want to be fair to that long-gone developer, because I've been him. He used what he knew, it solved the immediate problem, and he didn't stick around for the consequences. Nobody chose that system, not really. It just accreted. Which is exactly how most technology disasters happen: not through bad decisions but through unexamined defaults compounding quietly in the dark.

## No favorite weapons

Musashi is blunt about this. A warrior with a favorite weapon has a weakness with a name. He insisted on competence across weapons and contempt for none, because the situation chooses the weapon, and a fighter who needs the situation to match his preference has surrendered the choosing.

Our field is uniquely bad at this. We don't just have favorite weapons, we have weapon-based identities. Python people. SQL people. The dashboard tribe and the notebook tribe. Vendors spend billions making sure we form emotional attachments to tools, and conference culture rewards fluency in whatever is newest. The result is a phenomenon every hiring manager knows: resume-driven development, where the architecture serves the builder's career more than the business's problem.

I've watched a team spend months standing up a distributed processing cluster for data that fit in memory on a laptop. I've watched real-time streaming infrastructure built for reports that executives read weekly. In every case the engineering was good. The choosing was bad. And the choosing is the strategy.

## What "right tool" actually means

The right tool is not the most powerful, the most modern, or the most impressive. After twenty-four years, my tests have gotten almost embarrassingly boring:

**Right-sized for the problem.** Match the tool to the job's actual scale, not its imagined future scale. You can migrate later if the glorious future arrives. Most glorious futures don't.

**Maintainable by the next person.** This is the ColdFusion test, and it's the one I weight heaviest now. Every tool choice is a letter to a future stranger. Choose things that person can learn, hire for, and Google at 2 AM during an outage. Boring technology is a gift to people you'll never meet.

**Cheap to be wrong about.** Favor choices that are reversible. A tool you can abandon in a month is a safer bet than a platform that takes a year to escape, even if the platform is better on paper. Exit cost is part of the price, and it's the part the sales deck never shows.

**Already there.** The tool the company already runs, already licenses, and already knows beats a marginally better tool that adds a new thing to operate. New capability has to clear the bar of new burden, and the bar is higher than it looks.

Notice what's missing from the list: whether the tool is fun, whether it's hot, and whether it'll look good on a resume. I'm not pretending those pulls don't exist. I'm telling you to notice when they're doing the choosing.

## The discipline of enough

Demand simplicity, embrace discipline. This is where those words earn their keep. The discipline isn't learning more tools. It's the harder thing: being skilled enough to use the sophisticated weapon and choosing the simple one anyway, because the situation calls for simple. A SQL query that the whole team can read, scheduled with the company's existing scheduler, writing to a table everyone already trusts, is frequently the strategic masterpiece, and it will never once feel like one. Mastery in this craft looks a lot like restraint, which is why so few people recognize it when they see it.

Somewhere out there is a pipeline you will build this year. A decade from now a stranger will inherit it. Write them a kind letter.

## Sword Drills

1. **Audit your attachments.** Write down your three favorite tools and, for each, the kind of problem where it's the wrong choice. If you can't name one, you've found a blind spot, not a perfect tool.
2. **Run the 2 AM test.** For your most critical pipeline, ask: if this fails at 2 AM and I'm unreachable, can someone else diagnose it with the documentation and skills the team actually has? If not, that's your next sprint.
3. **Price an exit.** For one major tool in your stack, estimate honestly what it would cost in time and money to leave it. Knowing your exit costs changes how you negotiate, architect, and sleep.
4. **Solve one thing the boring way.** Take a current problem you were planning to solve with something new, and solve it with something the company already runs. Note what you lose and what you gain. Keep the note.
5. **Find your ColdFusion.** Every organization has one: the unowned, undocumented system quietly load-bearing in the dark. Find yours before it finds you. You don't have to fix it this quarter. You have to know its name.

---

# Chapter 4: Build on Rock, Not Sand

> "Step by step walk the thousand-mile road." - Miyamoto Musashi

I'll be straight with you: I don't have one dramatic story for this chapter. I have twenty small ones, and they're all the same story.

A number on an executive dashboard that didn't match the number in finance's spreadsheet, and the two-week archaeology project to find out why. A "customer count" metric that three teams calculated three ways, each team certain theirs was the official one. A machine learning model that degraded for months before anyone noticed, because nobody owned checking. A duplicate key that turned a board-level revenue figure subtly wrong, in the embarrassing direction. None of these stories has a villain or an explosion. Together they consumed more of my career than any single disaster, and they'll consume more of yours.

This is the chapter about foundations: data quality, governance, and the strategy that connects them. I know those words. I know what happens to your attention when you read them. Governance might be the only word in our field less popular than "compliance," and it earned its reputation honestly, through a thousand committees that produced binders instead of trust. So let me try to rescue the idea from the word.

## What foundations actually are

Strip away the frameworks and certifications, and the foundation question is just this: **when someone in this company looks at a number, can they trust it without checking?**

That's it. That's the whole game. Every governance council, quality dimension, and stewardship model is a means to that single end, and any of it that doesn't serve that end is theater.

Trust, in data as in people, is built slowly and spent instantly. The first time an executive catches a wrong number in your dashboard, your next ten dashboards get the skeptical squint. The terrain remembers. This is why foundations are a strategy problem and not a hygiene problem. Untrusted data doesn't just cause errors. It causes every future analysis to be discounted, double-checked, and shadow-copied into the spreadsheets of Chapter 1, and the organization quietly returns to deciding by gut while keeping the dashboards on for decoration.

## Quality, in plain English

The textbooks list six or eight dimensions of data quality. Here's the plain-English core that has covered nearly every real incident I've worked:

**Is it right?** Does the value match reality? (Accuracy.)
**Is it all there?** Are there gaps where there should be records? (Completeness.)
**Does it agree with itself?** Does "revenue" mean the same thing in every system that holds it? (Consistency.)
**Is it fresh enough?** Fresh enough for the decision it feeds, which is the only freshness that matters. (Timeliness.)
**Does the same thing have one identity?** Or is one customer four customers because of a typo and two system migrations? (Uniqueness.)

The discipline isn't memorizing the list. It's checking it routinely, automatically, at the point of entry, the way a swordsman checks his blade. Musashi inspected his weapons before the duel, not during. Quality checks bolted on after problems surface are exactly that: inspecting the blade mid-fight.

## Governance without the binder

Real governance, the kind that builds trust instead of resentment, comes down to three plain commitments:

**Every important data asset has one accountable human.** Not a committee. A name. When the customer table is wrong, somebody's phone rings, and that somebody knew it was their phone before it rang.

**Important terms have one definition, written down where people work.** Not in a glossary nobody opens. In the BI tool, on the dashboard, next to the number. The definition of "active customer" should be one click away from every chart that uses it.

**There's a known path for fixing what's wrong.** When someone finds a bad number, they should know where to report it and have reason to believe reporting it does something. Most quality problems in most companies have been noticed by someone who had no idea what to do with the noticing.

A name, a definition, a path. You can build all three without a single steering committee, and a company with those three things has better governance than most companies with a Chief Data Office and a framework license.

## The roadmap is a living thing

The last foundation is the strategy itself, and here I'll be brief because the enterprise version of this chapter was forty pages and the useful part fits on one.

Your data strategy should fit on a page. One page that says: here's what the business is trying to do, here are the two or three data capabilities that most directly serve it, here's what we're building this year, and here's what we're deliberately not doing. The "not doing" list is the part that makes it a strategy instead of a wish list.

And it's written in pencil. I told you in Chapter 1 about the six-month roadmap that died in a reorg. The lesson wasn't to stop planning. It was to hold the plan the way Musashi held his stance: committed and adjustable at once. Revisit the page quarterly. When the ground moves, move the page. A roadmap that survives unchanged for two years isn't stable. It's unread.

Step by step, walk the thousand-mile road. Musashi's line sounds like a fortune cookie until you've lived it. Foundations are boring precisely because they're built daily, in small verifications and unglamorous ownership, and the payoff arrives years later as something almost invisible: an organization where people look at a number and simply believe it. I've worked in companies with that and companies without it. The difference is the difference between fighting on rock and fighting on sand, and you don't fully appreciate it until you've felt the sand move.

## Sword Drills

1. **Find the disagreement.** Pick one key metric and find every place it appears: dashboards, decks, spreadsheets. If the values differ, trace why. You'll learn more about your data landscape in this one exercise than in a quarter of normal work.
2. **Name the owner.** For your five most important data assets, write down the accountable human. Every blank on that list is a future incident with no one to call.
3. **Put one definition where people work.** Take your most-disputed metric and get its definition onto the dashboard itself, one click or less from the number. Watch the recurring argument quietly die.
4. **Automate one check.** Choose the quality failure that has bitten you most recently and write an automated test for it that runs on every load. One check, this week. Foundations are built at exactly this speed.
5. **Write the one-pager.** Draft your team's data strategy on a single page, including the "not doing" list. If you can't get it to one page, you don't have a strategy yet. You have an inventory.

---

## Closing the Ground Book

> "From one thing, know ten thousand things." - Miyamoto Musashi

Ground is where Musashi starts because ground is what everything else stands on. Know the terrain before the engagement. Translate the stated problem back into the real one. Carry no favorite weapons. Build trust into the data daily, so the day you need the organization to believe you, it already does.

None of it is glamorous. All of it is load-bearing. Water comes next, and water is where the craft starts to move.

*End of Batch 1. Water Book (Chapters 5 through 8) follows on approval.*
