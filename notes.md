# Project Ideas:
- 30-day readmission rate benchmarking
- Condition-specific readmission patterns
- Facility performance ranking
- Peer group comparison

# Tools used:
- SQL
- Tableau

# How to Build This Project
## Start with a clear problem statement
Example: *"How can we reduce 30-day readmission rates by identifying high-risk conditions and facilities for targeted interventions?"*

## Sub-questions to answer
1. Size: What is the overall 30-day readmission rate by condition and facility?
2. Rank: Which hospitals have the highest/lowest readmission rates?
3. Explain: Which conditions drive the most readmissions?
4. Compare: How do readmission rates vary by hospital characteristics (size, ownership, emergency services)?
5. Recommend: Which 3 facilities should prioritize readmission reduction programs?

## KPIs you need:
- 30-Day Readmission Rate (%)
- Readmissions vs Expected (ratio)
- Facility Count by Performance Tier
- Condition-Specific Rates (Heart Attack, Heart Failure, Pneumonia)

## Comparison Categories:
- Compared to National → Better than, No Different than, Worse than national rate
- Footnote → Explains why measure not calculated (too few cases, etc).

## Payment Penalty:
- Excess Readmission Ratio → Used to calculate payment penalty under HRRP
- If ratio > 1.0, hospital faces up to 3% payment reduction

## Tools setup:
- CSV format for both files
- Import into SQL (BigQuery)
- Present findings using Tableau + LOOM video + Slides presenation (Acting as a report)