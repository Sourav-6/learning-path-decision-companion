# BUILD_PROCESS.md

## Build Process -- Learning Path Decision Companion

This document explains how the project evolved from the initial idea to
the final implementation, including design decisions, refactoring steps,
mistakes, and improvements made during development.

------------------------------------------------------------------------

## 1️⃣ How I Started

I began by selecting one of the example domains mentioned in the
assignment:

> Choosing a laptop under a budget

This seemed practical because:

-   The criteria were easy to quantify (price, RAM, CPU, battery).
-   Ranking logic was straightforward.
-   It allowed implementation of a weighted scoring model.

I implemented:

-   A JSON dataset of laptops.
-   User-defined weight input.
-   A scoring function to rank laptops.
-   A basic explanation mechanism.

This validated the core decision engine concept.

------------------------------------------------------------------------

## 2️⃣ How My Thinking Evolved

After completing the laptop system, I reviewed the assignment again and
reflected on key phrases such as:

-   "We want to see how you build."
-   "We are more interested in your thinking than feature count."
-   "Explain why a recommendation was made."

I realized that while the laptop system worked technically, it did not
demonstrate deeper abstraction or modeling ability.

This led me to pivot toward a more conceptual problem:

> Learning Path Decision Companion

This required more structured thinking because:

-   Career paths involve trade-offs.
-   Criteria are less obvious than hardware specs.
-   User intent must be interpreted meaningfully.

This shift improved the depth and originality of the project.

------------------------------------------------------------------------

## 3️⃣ Alternative Approaches Considered

During development, I considered multiple approaches:

### A. Machine Learning Model

Idea: Train a predictive model to recommend a learning path.

Rejected because: - It would introduce black-box behavior. - Harder to
explain scoring transparently. - Overkill for assignment scope.

### B. Analytic Hierarchy Process (AHP)

Idea: Use pairwise comparison matrices.

Rejected because: - Adds complexity without clear benefit. - Harder to
implement cleanly in CLI. - Less intuitive for users.

### C. Web Application (Flask/React)

Considered building a web UI.

Rejected for initial version because: - Focus should be on decision
engine quality. - UI development might distract from logic clarity.

Final choice: Deterministic weighted scoring model in a modular CLI
architecture.

------------------------------------------------------------------------

## 4️⃣ System Structuring Decisions

I organized the project into clear modules:

    src/
     ├── main.py        → User interaction and flow
     ├── loader.py      → Data loading logic
     ├── scorer.py      → Weighted scoring engine
     ├── explainer.py   → Explanation generator
    data/
     └── paths.json     → Dataset

Reasoning:

-   Separation of concerns improves readability.
-   Easier to extend later.
-   Makes reasoning about components simpler.
-   Aligns with good software design practices.

------------------------------------------------------------------------

## 5️⃣ Refactoring Decisions

### Refactor 1: Weight Input Simplification

Initial version required users to manually input numeric weights (1--5).

Problem: - Not user-friendly. - Overly technical.

Refactor: Replaced raw numeric input with predefined priority modes: -
Get Job Quickly - High Salary Focus - Easy Learning - Strong
Foundation - Balanced

This improved usability without compromising scoring logic.

------------------------------------------------------------------------

### Refactor 2: Explanation Layer

Initial version only showed numeric scores.

Problem: - Did not clearly justify decisions.

Refactor: Added `explainer.py` to: - Highlight strongest contributing
factors. - Link explanation to user priorities. - Improve transparency.

------------------------------------------------------------------------

### Refactor 3: Repository Structure Cleanup

During development, I mistakenly initialized Git at the Desktop level,
which caused:

-   Entire Desktop to be tracked.
-   Nested project folder inside repository.

Correction: - Removed incorrect Git initialization. - Reinitialized
repository inside project folder. - Cleaned nested folder from remote. -
Improved Git workflow discipline.

This reinforced proper repository management practices.

------------------------------------------------------------------------

## 6️⃣ Mistakes and Corrections

### Mistake 1: Overly Simple Initial Domain

The laptop decision system met requirements but lacked depth.

Correction: Pivoted to a more abstract decision model that demonstrates
system design thinking.

------------------------------------------------------------------------

### Mistake 2: Git Root Misconfiguration

Accidentally committed from Desktop directory.

Correction: Reinitialized Git properly and cleaned repository history.

------------------------------------------------------------------------

### Mistake 3: Weak Explanation Logic (Early Version)

First explanation was generic.

Correction: Enhanced explanation logic to identify specific influencing
criteria.

------------------------------------------------------------------------

## 7️⃣ What Changed During Development and Why

| Phase \| Change \| Reason \|

\|-------\|--------\|--------\| Laptop Idea \| Implemented basic
weighted scoring \| Validate core logic \| \| Reflection \| Pivoted
domain \| Increase depth and originality \| \| Input System \| Added
priority modes \| Improve usability \| \| Explanation \| Built
explanation module \| Improve transparency \| \| Git Workflow \|
Reinitialized repository \| Fix structural mistake \|

The biggest change was the **pivot from a product comparison system to a
conceptual career decision model**, which significantly improved
abstraction and design depth.

------------------------------------------------------------------------

## 8️⃣ Final Build Philosophy

The final system emphasizes:

-   Transparency over complexity
-   Structured logic over AI prediction
-   Modularity over monolithic design
-   Explainability over automation

The project evolved from a simple scoring engine into a more thoughtful
decision-support system that reflects structured reasoning and system
design maturity.

------------------------------------------------------------------------

## Conclusion

The build process demonstrates:

-   Iterative improvement
-   Willingness to pivot when depth was insufficient
-   Refactoring for usability
-   Correction of workflow mistakes
-   Focus on explainable architecture

This aligns with the assignment's emphasis on:

> "How you build" rather than just what you build.
