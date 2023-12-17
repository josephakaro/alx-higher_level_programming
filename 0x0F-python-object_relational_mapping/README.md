# 0x0F. Python - Object-relational mapping

`python` `OOP` `SQL` `MySQL` `ORM` `SQLAlchemy`

## Object Realtional Mappers(ORMs):

Python code libary that automates the transfer of data stored in a relational database tables into objects that are more common used.

Database Table Exaple:

| ID                                           | first_name | last_name | Phone         |
| -------------------------------------------- | ---------- | --------- | ------------- |
| 1                                            | Jones      | Joseph    | 2156456446545 |
| 2                                            | Joe        | Mark      | 2156456446545 |
| 3                                            | Sarah      | Smith     | 2156456446545 |
| ...                                          | ...        | ...       | ...           |
| -------------------------------------------- |

Python Objects:

```python

class Person:
    first_name = "Jones"
    last_name = "Joseph"
    phone = "2156456446545"
```

### Why ORMs useful?

- Provides a high-level abstraction:

  - SQL Statement

  ```mysql
  SELECT * FROM person WHERE first_name=Joseph;
  ```

  - Django ORM:

  ```Django
  person = person.filter(first_name=joseph)
  ```
