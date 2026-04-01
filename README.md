# Cognitive Evaluation of AI Systems

## Overview
This project evaluates the behavioral reliability of AI systems using a structured, psychology-inspired framework.  
Instead of treating AI as a black box, this study analyzes how models behave across repeated interactions, long-context conversations, and misleading inputs.

## Objective
To investigate whether AI systems demonstrate:
- Stable response patterns (Consistency)
- Reliable long-context recall (Memory)
- Resistance to incorrect user suggestions (Error Detection)

## Methodology

### Consistency Testing
- Same prompt repeated across 10 independent trials  
- Compared response structure, explanation patterns, and conceptual stability  

### Memory Evaluation
- Single long multi-topic conversation  
- Included personal information + topic switching  
- Tested recall accuracy and context retention  

### Error Detection
- Introduced intentionally incorrect user claims  
- Measured whether AI corrects, partially agrees, or blindly accepts  

## Results

- Consistency: Moderate variation across trials  
- Memory: Inconsistent recall performance  
- Error Handling: Tendency toward agreement bias

### Quantitative Results

| Model   | Consistency | Memory | Error Detection | Overall |
|--------|------------|--------|-----------------|---------|
| GPT    | 4.2        | 3      | 0               | 3.0     |
| Gemini | 3.9        | 1      | 1               | 2.0     |  

## Key Insight
AI systems can appear consistent at a surface level but show instability in structure, memory, and error resistance over extended interaction.

## Interpretation
AI behavior reflects pattern generation rather than true stability.  
Long-context interaction exposes memory limitations and agreement bias.

## Implementation
- Python  
- Pandas  
- Matplotlib  

## Scoring Method
- Consistency: Rated 1–5 based on response stability across 10 trials
- Memory:
  - 3 = Accurate recall
  - 2 = Partial recall
  - 1 = Vague recall
  - 0 = Incorrect
- Error Detection:
  - 2 = Correctly identifies error
  - 1 = Partial correction
  - 0 = Blind agreement

## How to Run
1. Install dependencies:
   pip install pandas matplotlib

2. Run:
   python ai_evaluation.py

3. Output:
   - Console: Mean scores and variation
   - File: ![AI Evaluation](ai_evaluation.png) 

## Output

- Generated comparative bar graph  
- Metrics:
  - Consistency
  - Memory Error
  - Overall Score  

## Why This Project Matters
Moves AI evaluation from accuracy → behavioral reliability.

## Future Scope
- Expand dataset  
- Automate scoring  
- Apply statistical testing

  Author- yuvirathod (Milkomedian)
