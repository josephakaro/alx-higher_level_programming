# 0x0c.Python-Almost a circle

| Project Details                | 
| ------------------------------ |
| By: Joseph Marko               |
| Weight:                        |
| Deadline: First                |
| Scored:                        |
| Languages: ``Python``, ``OOP`` |

> [!WARNING]
> 1. You are tasked to come up with solutions for the tasks below
> yourself to meet with the above learning objectives. 
> 2. You will not be able to meet the objectives of this or any
> following project by copying and pasting someone else’s work.
> 3. You are not allowed to publish any content of this project.
> 4. Any form of plagiarism is strictly forbidden and will result in
> removal from the program.

## Background Context:
The AirBnB project is a big part of the Higher level Curriculum. This project will help you to be ready for it.
    
In this project, you will review everything about python:

- Import
- Exception
- Class
- Private attributes
- Getter and Setter
- Class Method
- Static method
- Inheritance
- Unittest
- Read/Write file

## Learning Object:
1. You will learn about:
    - args and Kwargs
    - Serialization and Deserialization
    - JSON
2. You are expected to be able to explain to everyone, without the help of Google:

    ### General:
     - What is Unit testing and how to implement it in a large project.
     - How to serialize and deserialise a Class
     - How to write and read a JSON file
     - What is ``*args`` and how to use it.
     - What is ``**kwargs`` and how to use it.
     - How to handle named arguments in a function

## Resources:

### Read:

- [args and Kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

> [!IMPORTANT]
> Kindly the provided resource may not be enough to understand some
> concepts, you are advice to do deep research per your prefered
> learning method.

## NOTES:

### Definitions:
 - *args and **kwargs are special keyword arguments that allow you to pass a variable number of arguments to a Python function.

| Keyword  | Descriptions                                                                    |
| -------  | ------------------------------------------------------------------------------- |
| *args    | Accepts a variable number of non-keyword arguments and stores them in a tuple.  |
| **kwargs | accepts a variable number of keyword arguments and stores them in a dictionary. |

### Usage:
 - To use *args and **kwargs, you simply need to add them as parameters to your function definition. For example:

```python
    def my_function(*args, **kwargs):
    # Do something with args and kwargs 
```
 - To pass arguments to your function using *args and **kwargs, you simply need to pass them as positional arguments or keyword arguments, respectively. For example:

 ```python
    my_function(1, 2, 3, name="Joseph")
 ```
### Advantages of using args and kwargs:
 - Using ``*args`` and ``**kwargs`` has a number of advantages, including:
    - It makes your functions more flexible and reusable. You can use ``*args`` and ``**kwargs`` to write functions that can accept any number of arguments, regardless of their type.
    - It makes your code more readable and maintainable. When you use ``*args`` and ``**kwargs``, you can clearly see what types of arguments your function accepts and how they are used.
### Best practices for Using args and kwargs:
 - Here are a few best practices for using ``*args`` and ``**kwargs``:
    - Always put *args before **kwargs in your function definition.
    - Use keyword arguments to pass named arguments to your function.
    - Use *args to pass a variable number of positional arguments to your function.
    - Use **kwargs to pass a variable number of keyword arguments to your function.
    ### Example:
    ```python
       # Example 1: Using *args to pass a variable number of positional arguments

        def print_args(*args):
          for arg in args:
            print(arg)

        print_args(1, 2, 3, 4, 5)

        # Output:
        # 1
        # 2
        # 3
        # 4
        # 5

        # Example 2: Using **kwargs to pass a variable number of keyword arguments

        def print_kwargs(**kwargs):
            for key, value in kwargs.items():
                print(f"{key}: {value}")

        print_kwargs(name="Alice", age=25, occupation="Software Engineer")

        # Output:
        # name: Alice
        # age: 25
        # occupation: Software Engineer

        # Example 3: Using *args and **kwargs together

        def my_function(*args, **kwargs):
         # Do something with args and kwargs

        my_function(1, 2, 3, name="Alice", age=25) 
    ```

> [!IMPORTANT]
> *args and **kwargs are powerful tools that can make your Python code more flexible, reusable, 
> readable, and maintainable. Be sure to learn how to use them effectively.