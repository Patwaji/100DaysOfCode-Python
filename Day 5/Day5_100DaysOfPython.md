
# Day 5: 100 Days of Python

## Concepts Learned

### 1. `len()` Function for Lists
- The `len()` function returns the number of items in a list.
```python
my_list = [1, 2, 3, 4]
print(len(my_list))  # Output: 4
```

### 2. IndexError
- An **IndexError** occurs when trying to access an index that is out of range of a list.
```python
my_list = [1, 2, 3]
print(my_list[5])  # IndexError: list index out of range
```

### 3. `for` Loops
- **How it works**: The `for` loop iterates through a sequence (like a list or string).
```python
my_list = ['a', 'b', 'c']
for item in my_list:
    print(item)
```

- **Applications**:
    - Processing elements in a list.
    - Performing repetitive tasks on data structures.

### 4. Creating Numerical Lists with `range()`
- Generate numerical sequences easily.
```python
# Generate numbers from 1 to 10
for num in range(1, 11):
    print(num)
```

- **Applications**:
    - Looping through a sequence of numbers.
    - Generating indices or working with large datasets.

### 5. Functions Exclusive to Lists of Numbers
- Common operations:
    - `min()`, `max()`, and `sum()`.
```python
numbers = [1, 2, 3, 4, 5]
print(min(numbers))  # Output: 1
print(max(numbers))  # Output: 5
print(sum(numbers))  # Output: 15
```

### 6. List Comprehension
- A concise way to create lists.
```python
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]
```
- **Benefits**:
    - Less code.
    - Easy to read and efficient.

### 7. Slicing a List
- Extracting a portion of a list.
```python
my_list = [0, 1, 2, 3, 4, 5]
print(my_list[1:4])  # Output: [1, 2, 3]
```
- Can omit start or end index:
```python
print(my_list[:3])  # Output: [0, 1, 2]
print(my_list[3:])  # Output: [3, 4, 5]
```

### 8. Looping Through a Sliced List
- Iterate over a specific portion of a list.
```python
players = ['Alice', 'Bob', 'Charlie', 'Diana']
for player in players[:2]:
    print(player)  # Output: Alice, Bob
```

### 9. Copying a List
- Use slicing to create a copy of a list.
```python
list1 = [1, 2, 3]
list2 = list1[:]
print(list2)  # Output: [1, 2, 3]
```
- Both lists are independent.

---

## Code Examples
```python
# Example combining multiple concepts:
numbers = list(range(1, 11))  # Create a list of numbers 1-10
squared_numbers = [num**2 for num in numbers]  # List comprehension
first_half = squared_numbers[:5]  # Slicing the first 5 elements

print("All Squares:", squared_numbers)
print("First Half:", first_half)

for square in first_half:
    print(f"Square: {square}")

# Copying lists
copied_list = squared_numbers[:]
print("Copied List:", copied_list)
```

---

## Reflection
Today's focus was on foundational list operations. These tools enhance data processing efficiency and create clean, efficient Python code. Mastering these basics will significantly improve future programming projects.
