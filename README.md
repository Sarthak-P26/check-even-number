# Python Projects  

This repository is a collection of my Python projects.  
Each project is stored in its own folder with source code and instructions on how to run it.  

---

## 📂 Projects  

### Even Number Checker  
A simple Python program that checks whether a number is even or odd.  

#### 🔹 Code Example
```python
print("Welcome to my program")
user_input = int(input("Enter a number: "))

def even_or_not(user_input):
    if user_input % 2 == 0:
        print("It's an even number.")
        print("It's divisible by 2")
    else:
        print("It's an odd number")
        print("It's not divisible by 2")

even_or_not(user_input)
