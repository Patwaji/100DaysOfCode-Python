# 100 Days of Python

## Day 1: Tuple and PEP 8 Styling

### **Today's Progress**
- **Learned about Tuples:**
  - A tuple is an immutable sequence of Python objects.
  - Tuples are defined by enclosing items in parentheses `( )` separated by commas.
  - Key features:
    - Faster than lists due to immutability.
    - Useful for data that shouldn't change.
  
  #### Syntax Example:
  ```python
  my_tuple = (1, 2, 3, "hello")
  print(my_tuple[0])  # Output: 1
  ```

  #### Common Tuple Methods:
  - `count(value)`: Counts occurrences of `value` in the tuple.
  - `index(value)`: Returns the index of `value`.
  
  ```python
  my_tuple = (10, 20, 30, 10)
  print(my_tuple.count(10))  # Output: 2
  print(my_tuple.index(30))  # Output: 2
  ```

- **Learned about PEP 8 Styling:**
  - PEP 8 is Python's official style guide for writing clean and readable code.
  - Key practices include:
    - Indentation with 4 spaces (not tabs).
    - Limit lines to 79 characters.
    - Use blank lines to separate functions and classes.
    - Write comments sparingly and only when helpful.
    - Use snake_case for variables and functions.

  #### Example:
  ```python
  # Good example adhering to PEP 8:
  def calculate_area(radius):
      """Calculate the area of a circle."""
      pi = 3.14159
      return pi * radius ** 2

  print(calculate_area(5))
  ```

### Reflections:
- Tuples are useful for protecting data integrity by preventing modifications.
- PEP 8 styling ensures that the code remains easy to read and collaborate on.

### Next Steps:
- Practice more coding examples with tuples.
- Refactor old code to follow PEP 8 styling guidelines.
