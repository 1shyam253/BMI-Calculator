#!/usr/bin/env python3
"""BMI Calculator - body mass index from weight (kg) and height (m)."""
import argparse

def bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

def category(value):
    if value < 18.5: return "Underweight"
    if value < 25: return "Normal weight"
    if value < 30: return "Overweight"
    return "Obese"

def main():
    p = argparse.ArgumentParser(description="BMI Calculator")
    p.add_argument("--weight", type=float, help="Weight in kilograms")
    p.add_argument("--height", type=float, help="Height in metres")
    args = p.parse_args()
    weight = args.weight if args.weight is not None else float(input("Weight (kg): "))
    height = args.height if args.height is not None else float(input("Height (m): "))
    if height <= 0 or weight <= 0: raise SystemExit("Weight and height must be positive.")
    value = bmi(weight, height)
    print(f"Your BMI is {value:.1f} ({category(value)})")

if __name__ == "__main__":
    main()
