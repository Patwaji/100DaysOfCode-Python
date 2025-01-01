
# Day 1 - Introduction to Python

## **Topics Covered:**
1. **Print Function**
2. **Input Function**
3. **Strings**
4. **Error Handling**
5. **The `len()` Function**

---

### 1. **Print Function**

The `print()` function in Python is used to display output. It sends the content to the console or terminal.

#### Syntax:
```python
print("Hello, World!")
```

- You can print different types of data, such as strings, numbers, and variables.
- Example:
    ```python
    name = "John"
    print("Hello, " + name)  # Output: Hello, John
    ```

---

### 2. **Input Function**

The `input()` function allows us to accept input from the user during program execution.

#### Syntax:
```python
input(prompt)
```

- `prompt` is an optional argument that appears as a message before taking the input.
- It always returns the input as a string.
  
#### Example:
```python
name = input("What is your name? ")
print("Hello, " + name)
```

---

### 3. **Strings**

- **String** is a sequence of characters surrounded by quotes (`" "` or `' '`).
- You can combine (concatenate) strings with the `+` operator.
- You can access individual characters in a string using an index (starting from `0`).

#### Example:
```python
message = "Hello, Python!"
print(message[0])  # Output: H
```

- **Escape Characters**: Use backslashes (`\`) to escape special characters, such as newline `
`.

---

### 4. **Error Handling**

When you encounter an error in Python, you can handle it by:
- **Google** the error message to understand what went wrong.
- **Use Documentation**: Always refer to Python’s [official documentation](https://docs.python.org/3/) for more detailed information on functions and their usage.

#### Example:
```python
print("Welcome")
# SyntaxError Example: if you miss a parenthesis here
# print("Welcome"
```

- **Handle errors gracefully** using `try-except` blocks. This allows your program to continue running even if it encounters an error.
  
#### Example:
```python
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ZeroDivisionError:
    print("Oops! You can't divide by zero.")
except ValueError:
    print("Oops! Please enter a valid number.")
```

---

### 5. **The `len()` Function**

The `len()` function is used to find the length of a sequence (like a string, list, or tuple).

#### Syntax:
```python
len(object)
```

- Returns the number of items in the object.
  
#### Example:
```python
message = "Hello"
print(len(message))  # Output: 5
```

---

### **Key Takeaways:**

- Practice using the `print()` and `input()` functions to interact with the program.
- Learn how to handle errors by using `try-except` blocks and always refer to Python docs.
- Explore basic string operations and the use of the `len()` function to calculate the size of collections.

---

### **Resources:**

- Python Docs - [https://docs.python.org/3/](https://docs.python.org/3/)
