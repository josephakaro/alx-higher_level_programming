# TEST-DRIVEN DEVELOPMENT

``Doctest`` is a Python module that allows you to write tests for your code in the form of interactive Python sessions. This can be used for a variety of purposes, including:

- Checking that your docstrings are up-to-date:\
By writing doctests in your docstrings, you can ensure that your code examples are still accurate and that your documentation is complete.
- Performing regression testing:\
Doctest can be used to run your tests automatically whenever you make changes to your code. This helps you to catch bugs early and prevent regressions.
- Writing tutorial documentation:\
Doctest can be used to write tutorial documentation that is illustrated with input-output examples. This can make your documentation more engaging and easier to understand.
- Doctest as literate testing or executable documentation:\
Doctest can be used to implement either literate testing or executable documentation. Literate testing is a style of testing where the tests are written in the same language as the code, and the tests and code are interleaved. Executable documentation is a style of documentation where the documentation contains code examples that can be executed.

Which approach you choose depends on your preferences. If you prefer to write your tests and code in the same language, then literate testing is a good option. If you prefer to keep your tests and code separate, then executable documentation is a good option.

### Example:

Here is a simple example of a doctest:

```Python
def add(a, b):
  """Returns the sum of a and b.

  Args:
    a: A number.
    b: A number.

  Returns:
    The sum of a and b.
  """
  return a + b

>>> add(1, 2)
3
>>> add(3, 4)
7
```
This doctest defines a function called add(), and then provides two examples of how to use the function. When the doctest is run, it will execute the two examples and verify that the output is correct.