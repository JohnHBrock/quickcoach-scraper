#!/usr/bin/env python3
"""
Pivot QuickCoach export data from long format to wide format.

Input format (long):
  plan_title,exercise_name,date,result
  New plan 2,Back squats,2025-11-06,85x10 95x8 105x6 105x6
  New plan 2,Back squats,2025-10-18,85x10 95x8 95x8 105x6

Output format (wide):
  exercise_name,2025-11-06,2025-10-18,...
  Back squats,85x10 95x8 105x6 105x6,85x10 95x8 95x8 105x6,...
"""

import argparse
import csv
from collections import defaultdict
from typing import Dict, List, Set


def main():
    parser = argparse.ArgumentParser(
        description="Pivot QuickCoach data: exercises as rows, dates as columns"
    )
    parser.add_argument(
        "--input",
        default="quickcoach_full.csv",
        help="Input CSV file (default: quickcoach_full.csv)",
    )
    parser.add_argument(
        "--output",
        default="quickcoach_pivoted.csv",
        help="Output CSV file (default: quickcoach_pivoted.csv)",
    )
    args = parser.parse_args()

    # Data structure: { exercise_name: { date: result } }
    exercise_data: Dict[str, Dict[str, str]] = defaultdict(dict)
    all_dates: Set[str] = set()

    # Read input CSV
    with open(args.input, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            exercise_name = row["exercise_name"]
            date = row["date"]
            result = row["result"]

            # Skip rows without dates
            if not date:
                continue

            exercise_data[exercise_name][date] = result
            all_dates.add(date)

    # Sort dates chronologically (most recent first)
    sorted_dates = sorted(all_dates, reverse=True)

    # Sort exercises alphabetically
    sorted_exercises = sorted(exercise_data.keys())

    # Write output CSV
    with open(args.output, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        # Write header: exercise_name, date1, date2, ...
        writer.writerow(["exercise_name"] + sorted_dates)

        # Write data rows
        for exercise in sorted_exercises:
            row = [exercise]
            for date in sorted_dates:
                # Get result for this exercise on this date (empty if not present)
                result = exercise_data[exercise].get(date, "")
                row.append(result)
            writer.writerow(row)

    print(f"Pivoted data written to {args.output}")
    print(f"  Exercises: {len(sorted_exercises)}")
    print(f"  Dates: {len(sorted_dates)}")


if __name__ == "__main__":
    main()
