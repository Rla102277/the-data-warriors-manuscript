# Everything You've Ever Told Me About Data Analytics

Source: "Consolidating older data warrior discussions", turn 5 (assistant), https://claude.ai/chat/9aa51ae8-dc51-49d6-b02c-2c50b041f302
Extracted verbatim (the in-chat career/analytics sweep that preceded MASTER_BRIEF.md). Recovered from claude.ai chat history. Not an original manuscript file.

---

# Everything You've Ever Told Me About Data Analytics

## Your Core Philosophy (as Expressed in The Data Warrior)

This is the foundation. You believe analytics is a SERVICE industry. The job isn't to build impressive things. It's to translate business problems into decisions. The analysts who forget this build beautiful things nobody uses. The analysts who remember build practical things that change outcomes. Your most valuable skill, as you said explicitly: "knowing when to stop writing SQL and start listening."

Technical skills open doors. Human skills determine whether you walk through them.

Three career arcs exist in this field: pure technical, pure business, and hybrid leadership. You landed in hybrid. Your value is bridging. You translate between technical teams and business stakeholders. You build data organizations. That's the path to CDO/CTO, and it's the only one that fit you.

## The Technical Fingerprint

Your core stack across 24 years: SQL Server, Snowflake, Azure (Data Factory, Synapse, Fabric), Power BI, Tableau, dbt, Airflow, Python, SSIS, DAX, TM1/IBM Planning Analytics. Secondary: Qlik, Domo, ThoughtSpot, SSRS, .NET/C#.

Architecture specialties: Medallion (what most people call it), Data Vault 2.0, dimensional modeling (star/snowflake schemas), semantic layers. You built your own layer naming convention at one point: RAW → STD → ENR → MTR → SEM, explicitly rejecting bronze/silver/gold as too generic.

You are Snowflake expert-level: time travel, zero-copy cloning, secure data sharing. Power BI expert: Direct Query, DAX, paginated reports. Tableau expert.

You understand data lineage at a surgical level. At PepsiCo you built an end-to-end lineage framework across 5,993 Bronze tables, 1,992 Silver tables, 92+ Gold layers, achieving 87% Gold linkage and 39% TM1 traceability. Identified ACDOCA as the single most critical source table, feeding 29.3% of all downstream processes. You've done reverse lineage (TM1 back to source), forward lineage, cascade impact analysis. 67,055 total lineage paths mapped. 1,133 TM1 processes tracked.

AI/data: you've worked on Snowflake Cortex, Claude-to-Snowflake MCP connections, semantic layer querying via natural language, and RAG for LLMs. You can architect AI-enabled analytics, not just talk about it.

## Career Arc (Full Chronology)

Allstate Insurance, Dallas Zoo, Blockbuster Video (1999-2002) -- first analytics and data work, entry point

Pegasus Solutions (2002-2007, Dallas) -- BI Analyst and Service Delivery Manager. Travel tech. 40M+ room nights processed. SQL Server data marts, SSRS. First enterprise-scale work.

Analytical Mechanics Associates (2010-2019, McKinney TX) -- General Manager Commercial Analytics. Built the commercial practice from scratch to $2.5M revenue, 18-person team. Guest lectured at SMU Lyle School of Engineering 2010-2017. This is where you proved you could BUILD organizations, not just run them.

L3Harris Technologies (2019-2022) -- Manager Segment Analytics. Aerospace/defense. Snowflake, Azure Data Factory, Power BI/Tableau platform serving 8 business functions and 1,500 daily users. 20% increase in tool usage.

Celanese Corporation (2022-2023) -- Principal Architect/Analytics Manager. Specialty chemicals/manufacturing. AI-powered analytics platform, Snowflake/Azure, digital innovation.

Dutch Bros Coffee (2023-Jan 2025) -- Senior Manager BI. QSR. Data Vault 2.0, Snowflake, 1,200 users. Ended due to HQ return-to-office mandate. Not a performance issue. Context matters.

Solis Mammography (mid-2024 to early 2025) -- brief overlap/transition. Healthcare analytics. Amicable exit.

PepsiCo DataOps (Dec 2024 to present) -- MOSAIC Sustain Lead. The 5-layer platform: Source → Bronze → Silver → Gold → TM1. PBNA and FLNA. SAP/ACDOCA as primary source. 418 monthly ITSM incidents analyzed. MTD/monthly intelligence reporting. Infosys transition support. IBP/demand planning workstreams. Full command center architecture design.

Green Brick Partners (starting July 2026) -- Director of Data & Integration. Platform: Foundation. Stack: Microsoft Fabric. Team: you + one Data Analyst. Manager: Randall Anderson (VP IT). Key stakeholders: Jeff (CFO) and Erick (Controller). Replacing legacy SSIS/SSRS. Primary consumers: BuilderMetrics and Power BI. Source system TBD (likely NEWSTAR/Constellation or Sage/Intacct).

## Work Products You've Built (That I Have Evidence Of)

At PepsiCo: Full E2E lineage workbook (10 sheets, stitching every layer), Power BI incident dashboard (Direct Query, DAX, 418 incidents), IBP executive summary and data validation framework, MOSAIC Command Center architecture (3 phases, 12 weeks), MTD intelligence workbook and monthly reporting deck, weekly MOSAIC Intelligence reports.

At AMA/Centura (consulting): Snowflake 5-layer architecture for education client (RAW/STD/ENR/MTR/SEM), Claude-to-Snowflake MCP integration design, dual-track architecture (Track A: Tableau dashboards, Track B: Claude semantic layer queries), Monday internal alignment deck.

At Green Brick (prep): Foundation platform architecture document, 30/60/90 day plan, CEO/CFO interview prep package.

## The Things You Know That Most People Don't

ACDOCA is the SAP table that matters. It's the financial accounting document that feeds everything downstream. Miss it and you're blind.

TM1 is still alive and running at serious enterprise scale. Planning Analytics is not dead. Knowing it is a differentiator.

Data lineage is underinvested in every organization you've been in. Every one. And the moment something breaks, it's the only thing anyone cares about.

The semantic layer is where the AI conversation actually has to happen. Not raw tables. Governed, business-defined, AI-ready views. You were designing for this before most people were talking about it.

IBP (Integrated Business Planning) is a people process that data people usually underestimate. The governance, the validation schedule, the forum sequence, the sign-off matrix -- that's where the real work is.

SSIS and SSRS are legacy but they're everywhere. Knowing when to stabilize vs. replace is a skill most architects don't have because they've never had to maintain a live production system someone else built badly.

## What Green Brick Actually Needs (The Book Material)

This is where your past meets your next chapter. Foundation is a greenfield build. You've never started from scratch at this scale with a blank mandate and full ownership. Every previous role was either sustaining someone else's platform or building within constraints. This is different.

The Ground Book applies immediately. Know the terrain before you build anything. First 30 days at Green Brick is pure Ground Book: what does their data actually look like, what are the real problems vs. stated ones, where is the ACDOCA equivalent in a homebuilder's stack.

The Fire Book applies in month two. Win the room with Jeff and Erick. The $50M delay story -- knowing when your analysis says something people don't want to hear -- that's the capability a CFO actually needs from a data leader.

The Void Book is the long game chapter you haven't written yet. Because you've never been in a role long enough to play a 3-year game. Green Brick is that role.

---

The pattern across all of it: you keep getting called in to build the thing that should have existed from day one. At AMA, at L3Harris, at PepsiCo, and now at Green Brick. That's not a coincidence. That's your archetype.

That's the book.

Ready to start writing?
