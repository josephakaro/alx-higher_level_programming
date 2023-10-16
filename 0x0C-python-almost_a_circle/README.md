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

## NOTE #1: ARGS AND KWARGS

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
    - Always put ``*args`` before ``**kwargs`` in your function definition.
    - Use keyword arguments to pass named arguments to your function.
    - Use ``*args`` to pass a variable number of positional arguments to your function.
    - Use ``**kwargs`` to pass a variable number of keyword arguments to your function.
    ### Example:
     Example 1: Using *args to pass a variable number of positional arguments
    ```python

        def print_args(*args):
          for arg in args:
            print(arg)

        print_args(1, 2, 3, 4, 5)
    ```

     Output:
    ```bash
        1
        2
        3
        4
        5
    ```
     
     Example 2: Using **kwargs to pass a variable number of keyword arguments
    ```python
        def print_kwargs(**kwargs):
            for key, value in kwargs.items():
                print(f"{key}: {value}")

        print_kwargs(name="Alice", age=25, occupation="Software Engineer")
    ```

     Output:
    ```bash
        name: Alice
        age: 25
        occupation: Software Engineer
    ```

     Example 3: Using *args and **kwargs together
    ```python
        def my_function(*args, **kwargs):
         # Do something with args and kwargs

        my_function(1, 2, 3, name="Alice", age=25) 
    ```

> [!IMPORTANT]
> ``*args`` and ``**kwargs`` are powerful tools that can make your Python code more flexible, reusable, 
> readable, and maintainable. Be sure to learn how to use them effectively.

## NOTE #2: JSON ENCODER AND DECODER

 ### Definitions:
 JSON, or JavaScript Object Notation, is a lightweight data-interchange format that has become the most popular medium of exchanging data over the web. 
 
 The reason behind its popularity is that it is both human-readable and easy for machines to parse and generate.

 Python provides a built-in json library to deal with JSON objects. This library includes two important classes:
  - ``JSONEncoder``: This class encodes Python objects to JSON strings.
  - ``JSONDecoder``: This class decodes JSON strings to Python objects.

### Usage: JSON Encoder
 To encode a Python object to a JSON string, you can use the ``json.dumps()`` function. This function takes a Python object as input and returns a JSON string as output.
 
 For example, the following code encodes a Python dictionary to a JSON string:

 ```python
    import json

    my_dict = {"name": "Alice", "age": 25}

    json_string = json.dumps(my_dict)

    print(json_string)
 ```

 Output:
 ```JSON
    {"name": "Alice", "age": 25}
 ```

### Usage: JSON Decoder
    To decode a JSON string to a Python object, you can use the ``json.loads()`` function. This function takes a JSON string as input and returns a Python object as output.
    
    For example, the following code decodes a JSON string to a Python dictionary:

```python
    import json

    json_string = """{"name": "Alice", "age": 25}"""

    my_dict = json.loads(json_string)

    print(my_dict)
```

Output:
```JSON
    {'name': 'Alice', 'age': 25}
```

### Encoding and Decoding custom objects:
 The ``json.dumps()`` and ``json.loads()`` functions can be used to encode and decode most Python objects. However, if you have a custom object that you need to encode or decode, you can subclass the ``JSONEncoder`` and ``JSONDecoder`` classes.

 For example, the following code shows a subclass of the ``JSONEncoder`` class that can encode a custom object called ``Point``:

```python
    import json

    class Point:
      def __init__(self, x, y):
        self.x = x
        self.y = y

      def __repr__(self):
        return f"Point({self.x}, {self.y})"

    class PointEncoder(json.JSONEncoder):
      def default(self, obj):
        if isinstance(obj, Point):
          return {"x": obj.x, "y": obj.y}
        else:
          return super().default(obj)

    my_point = Point(10, 20)

    json_string = json.dumps(my_point, cls=PointEncoder)

    print(json_string)
```

Output
```JSON
    {"x": 10, "y": 20}
```
 Similarly, you can subclass the ``JSONDecoder`` class to decode custom objects.

### Remarks:
 The ``json.dumps()`` and ``json.loads()`` functions are powerful tools that can be used to encode and decode Python objects to and from JSON strings. If you need to encode or decode custom objects, you can subclass the ``JSONEncoder`` and ``JSONDecoder`` classes.
