# Python and MySQL Database Interaction Project

## Background Context

In this project, you will link two amazing worlds: **Databases** and **Python**!

### Project Overview

- **Part 1**: You will use the `MySQLdb` module to connect to a MySQL database and execute your SQL queries.
- **Part 2**: You will use the `SQLAlchemy` module, an Object Relational Mapper (ORM).

The biggest difference between the two approaches is that with an ORM, you don't need to write SQL queries directly; instead, you work with Python objects. This abstraction makes it easier to work with data across different storage systems without changing the core codebase significantly.

### Without ORM Example

````python
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")  # SQL query required
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()

Here's the raw Markdown code for your content:

```markdown
## Key Differences

- **Direct SQL Queries**: Required when using MySQLdb.
- **ORM Abstraction**: Eliminates the need for SQL queries when using SQLAlchemy.

The biggest challenge with ORMs can be understanding the syntax, so don't hesitate to use tutorials and examples to help you get started.

---

## Learning Objectives

By the end of this project, you should be able to explain:

### General Concepts

- How to connect to a MySQL database from a Python script.
- How to SELECT rows in a MySQL table from a Python script.
- How to INSERT rows in a MySQL table from a Python script.
- What ORM (Object Relational Mapping) means.
- How to map a Python class to a MySQL table.

---

## Resources

### Read or Watch

- [Object-relational mappers](https://realpython.com/python-orm-frameworks/)
- [mysqlclient/MySQLdb documentation](https://mysqlclient.readthedocs.io/)
- [MySQLdb tutorial](https://pynative.com/python-mysql-database-connection/)
- [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/14/tutorial/index.html)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [mysqlclient/MySQLdb](https://github.com/PyMySQL/mysqlclient)
- [Introduction to SQLAlchemy](https://docs.sqlalchemy.org/en/14/intro.html)
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [10 common stumbling blocks for SQLAlchemy newbies](https://docs.sqlalchemy.org/en/14/orm/quickstart.html#common-stumbling-blocks)
- [Python SQLAlchemy Cheatsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)
- [SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
- [SQLAlchemy Tutorial](https://overiq.com/sqlalchemy-101/)

---

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.5)
- Files will be executed with MySQLdb version `2.0.x`
- Files will be executed with SQLAlchemy version `1.4.x`
- All files must end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the folder of the project is mandatory
- Code should use the `pycodestyle` (version `2.7.*`)
- All files must be executable
- The length of all files will be tested using `wc`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- Documentation is not a simple word; it should be a real sentence explaining the purpose of the module, class, or method (the length of it will be verified)
- You are **not** allowed to use `execute` with SQLAlchemy
````
