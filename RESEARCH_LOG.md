# Research Log -- From Laptop Decision System to Learning Path Decision Companion

This document captures the evolution of my thinking, research steps,
tool usage, and decision-making process while building the Decision
Companion System.

The intent is to transparently document how I used AI and external
resources to refine the solution --- without replacing core reasoning.

------------------------------------------------------------------------

## 1️⃣ Initial Idea: Laptop Selection System

### Starting Point

I initially chose:

> "Choosing a laptop under a budget"

This aligned directly with one of the example problems in the
assignment.

### Why I Chose It Initially

-   Easy to define criteria (price, RAM, CPU, battery)
-   Measurable attributes
-   Clear ranking logic
-   Practical real-world relevance

### Research Conducted

#### Google Searches

-   "weighted scoring model example"
-   "multi criteria decision making simple implementation"
-   "how to rank products using weighted score"
-   "decision support system architecture example"

### Insights

-   Weighted Scoring Model (WSM) is simple and transparent.
-   Each option should have numeric criteria.
-   The system must explain why something ranks higher.

### Implementation Direction

I implemented:

-   JSON dataset of laptops
-   Criteria weights (performance, battery, portability, brand)
-   Score calculation
-   Ranked output
-   Basic explanation engine

------------------------------------------------------------------------

## 2️⃣ Reflection & Pivot Decision

After implementing the laptop system, I reflected on the assignment's
hidden expectations:

-   "We want to see how you build."
-   "We are more interested in your thinking than feature count."
-   "Explain why a recommendation was made."

The laptop idea worked technically, but:

-   It felt predictable.
-   It closely followed the given examples.
-   It did not demonstrate deeper system-level thinking.

This led to a pivot.

------------------------------------------------------------------------

## 3️⃣ New Idea: Learning Path Decision Companion

I brainstormed alternative domains:

-   Investment strategy selection
-   Tech stack selection
-   Career path recommendation
-   Skill development roadmap

### Prompt Used During Brainstorming

> "Suggest a decision companion idea that demonstrates system design
> thinking and is not one of the common examples."

From reflection and exploration, I chose:

> Learning Path Optimization / Career Learning Decision System

### Why This Was Stronger

-   More abstract decision space
-   Involves real trade-offs
-   Demonstrates structured modeling
-   Reflects real student problems
-   Shows deeper reasoning beyond product comparison

------------------------------------------------------------------------

## 4️⃣ Research on Multi-Criteria Decision Models

### Google Searches

-   "multi criteria decision making method comparison"
-   "analytic hierarchy process vs weighted scoring"
-   "how to make decision systems explainable"
-   "transparent recommendation system design"

### Key Insights

-   AHP is powerful but complex.
-   Weighted scoring is simpler and sufficient.
-   Explainability is critical.
-   Black-box ML is discouraged for transparent systems.

### Final Choice

Used deterministic weighted scoring because:

-   Transparent
-   Easy to justify
-   Fully explainable
-   Matches assignment constraints

------------------------------------------------------------------------

## 5️⃣ Designing Criteria for Learning Paths

Defined measurable criteria:

-   Difficulty
-   Duration (weeks)
-   Job Demand
-   ROI (Return on Investment)
-   Resource Availability

Each metric: - Is comparable - Represents a real-world trade-off - Can
be numerically evaluated

Rejected vague attributes such as "cool factor" or purely subjective
labels.

------------------------------------------------------------------------

## 6️⃣ Improving User Input Experience

### Initial Version

Users manually entered numeric weights (1--5).

Problem: - Too technical - Not user-friendly

### Improvement

Mapped user goals to predefined priority modes:

-   Get Job Quickly
-   High Salary Focus
-   Easy Learning
-   Strong Foundation
-   Balanced

This improved usability while maintaining structured scoring.

------------------------------------------------------------------------

## 7️⃣ Explainability Enhancement

Research included:

-   "how to generate explanations for scoring systems"
-   "explainable recommendation example"

Implemented an explanation module that:

-   Identifies strongest contributing factors
-   Matches explanation to user priorities
-   Avoids generic statements

------------------------------------------------------------------------

## 8️⃣ AI Tools Used

### Tools

-   ChatGPT (brainstorming and refinement)
-   Google Search (concept validation)
-   Gemini (brief comparison)

### AI Contributions

-   Helped explore alternative domains
-   Assisted in structuring documentation
-   Suggested refinement in explanation clarity

### AI Limitations

-   Did not architect final scoring logic
-   Did not define final dataset structure
-   Final pivot decision was made independently

------------------------------------------------------------------------

## 9️⃣ Mistakes & Learning

### Mistake 1: Git Initialization at Desktop Level

-   Accidentally tracked entire Desktop
-   Created nested project folder

Fix: - Reinitialized Git correctly inside project folder - Cleaned
repository structure

### Mistake 2: Overly Simple First Idea

Laptop system worked but lacked depth.

Improvement: - Pivoted to more abstract decision modeling - Focused on
trade-off reasoning and architecture clarity

------------------------------------------------------------------------

## 🔎 Hidden Expectations Identified

From the assignment wording, I inferred the company values:

-   Structured thinking
-   Trade-off analysis
-   Clean system design
-   Transparency in AI usage
-   Documentation quality
-   Evolution of thought

This influenced the pivot toward a more conceptual and structured
decision model.

------------------------------------------------------------------------

## 🏁 Final Reflection

The project evolved through:

Laptop product comparison\
→ Reflection on depth and originality\
→ Structured career decision modeling\
→ Weighted scoring architecture\
→ Explainable recommendation engine

AI tools were used responsibly as accelerators, not replacements for
reasoning.

The final system reflects:

-   Deterministic logic
-   Modular structure
-   Clear reasoning
-   Extendability
-   Transparent decision modeling
