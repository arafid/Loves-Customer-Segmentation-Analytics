# Reconstruction Notes

This repository is a portfolio reconstruction of the Love's customer campaign and segmentation case competition project.

## Why the notebook was rebuilt

The available original `Love's_Case_Competition.ipynb` contains only a handful of cells and uses sample or hard-coded data such as generic segment labels. It does not contain the full raw-data workflow shown in the final write-up.

The portfolio notebook therefore uses the five original CSV files as the source of truth and checks its results against the submitted project report.

## What reproduces cleanly

The raw CSVs reproduce the major submitted results, including:

- MediumDiscount: 20.95% join rate and 29.99% achieve rate.
- MediumDiscount: 939.71 average campaign-month fuel gallons and $95.49 average merchandise sales.
- Gallons Extra: 9,488 goals achieved, 173,054 participant records, and $313,583.34 total campaign cost.
- The major division patterns by segment.
- A near-zero relationship between age and average gallons per visit.

## Merchandise-campaign percentage changes

The submitted report states that the merchandise campaign produced approximately:

- +15% merchandise sales
- +4% fuel sales
- +9% other sales

The final report does not preserve the exact filtering and aggregation sequence that generated those three percentages. The reconstructed notebook therefore shows a transparent raw-data calculation and labels the original percentages as report-derived rather than silently hard-coding them.

## Age correlation

The submitted report reports Pearson `r = -0.05` after working with age-group averages. A driver-level calculation using all available records is also approximately zero. The business conclusion is the same: age is not a useful standalone predictor of gallons fueled per visit.

## State vs. store geography

The submitted state-level table aligns with the driver's `STATE` field from `DRIVER_LOOKUP`, while the division table aligns with the most-visited store's `DIVISION`. The reconstruction keeps that distinction explicit.
