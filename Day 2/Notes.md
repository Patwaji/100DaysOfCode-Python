# Day 2: 100 Days of Python

## Concepts Learned

### Working with Strings
- **Adding White Space:**
  - Use `\t` for a tab.
  - Use `\n` for a new line.

- **Removing White Space:**
  - `lstrip()`: Removes leading whitespace.
  - `rstrip()`: Removes trailing whitespace.
  - `strip()`: Removes whitespace from both ends.

- **String Transformations:**
  - `upper()`: Converts all characters in the string to uppercase.
  - `lower()`: Converts all characters in the string to lowercase.
  - `title()`: Capitalizes the first letter of each word.

### Working with Data Types
- **`type()` Function:**
  - Used to check the type of a variable or value.

- **Type Conversion:**
  - Convert between types using `int()`, `float()`, `str()`, etc.

- **Type Error:**
  - Errors occur when incompatible data types are used together.
  - Solution: Use explicit type conversion to handle such cases.

### Mathematical Operations
- Basic operations include addition `+`, subtraction `-`, multiplication `*`, division `/`, and modulus `%`.
- **`round()` Function:**
  - Used to round a floating-point number to a specified number of decimal places.

### Formatted Strings
- **f-strings:**
  - Used to embed expressions inside string literals for dynamic formatting.
  - Syntax: `f"Your total is {value}"`

---

## Project: Tip Calculator

**Description:**
A simple tip calculator that helps split bills and calculate individual shares.

**Features:**
- Calculates the total bill with a specified tip percentage.
- Splits the bill among a given number of people.

**Key Functions:**
- Used mathematical operations for calculations.
- Implemented `round()` for neatly formatted results.
- Used f-strings for output formatting.

```python
# Tip Calculator
print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 15, or 20? "))
number_of_people = int(input("How many people to split the bill? "))

# Calculate the total bill with tip
bill_with_tip = total_bill * (1 + tip_percentage / 100)

# Split the bill per person
per_person = round(bill_with_tip / number_of_people, 2)

print(f"Each person should pay: ${per_person}")
