Overview
This project evaluates the behavioral reliability of AI systems using a structured, psychology-inspired framework.
Instead of treating AI as a black box, this study analyzes how models behave across repeated interactions, long-context conversations, and misleading inputs.

objective
To investigate whether AI systems demonstrate:
Stable response patterns (Consistency)
Reliable long-context recall (Memory)
Resistance to incorrect user suggestions (Error Detection)

Methodology
1. Consistency Testing
Same prompt repeated across 10 independent trials
Responses compared for:
Structure
Explanation pattern
Conceptual stability

Memory Evaluation
Single long multi-topic conversation
Included:
Personal information
Topic switching (philosophy → math → literature → back)
Tested:
Recall accuracy
Context retention

Error Detection
Introduced intentionally incorrect user claims
Measured whether AI:
Corrects the user
Partially agrees
Blindly accepts

Results
Consistency
Moderate variation across trials
Core meaning stable, but response structure and examples fluctuated
Memory
Inconsistent recall performance
Occasional distortion of previously provided user information
Error Handling
Observable tendency toward agreement bias
Some incorrect inputs were accepted instead of challenged

Key Insight
AI systems can appear consistent at a surface level, but exhibit instability in structure, memory retention, and error resistance under repeated and extended interaction.

Interpretation
AI behavior reflects pattern generation, not true stability
Long-context interaction reveals memory limitations
Agreement bias highlights lack of robust error-checking mechanisms

Implementation
Python-based scoring and analysis
Behavioral metrics quantified and visualized
Comparative evaluation across multiple trials

## Output
- Generated comparative bar graph using matplotlib
- Visualized:
  - Consistency
  - Memory Error
  - Overall Score

![AI Evaluation](ai_evaluation.png)

Why This Project Matters
This project shifts AI evaluation from:
“Does it give correct answers?”
to:
“How reliably does it behave over time?”

Future Scope
Expand dataset across more prompts and models
Introduce automated scoring pipelines
Integrate statistical testing for behavioral patterns

Author
Yuvirathod (Milkomedian)
