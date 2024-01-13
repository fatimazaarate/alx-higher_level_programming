# 0x0F Python Object-Relational Mapping

Welcome to the 0x0F Python Object-Relational Mapping project! In this project, you will explore the world of Python programming and its integration with MySQL databases. By the end of this project, you'll gain valuable knowledge about connecting to a MySQL database, performing SELECT and INSERT operations, understanding ORM (Object-Relational Mapping), and mapping a Python Class to a MySQL table. Additionally, you'll learn how to create a Python Virtual Environment for a clean and isolated development environment.

## Learning Objectives

### 1. Python Programming Awesomeness
- Understand why Python programming is considered awesome and widely used in various domains.

### 2. Connecting to a MySQL Database
- Learn how to establish a connection to a MySQL database from a Python script.

### 3. SELECTing Rows in a MySQL Table
- Explore the process of querying and retrieving rows from a MySQL table using Python.

### 4. INSERTing Rows in a MySQL Table
- Master the art of inserting rows into a MySQL table using Python scripts.

### 5. Object-Relational Mapping (ORM)
- Grasp the concept of ORM and its significance in bridging the gap between object-oriented programming and relational databases.

### 6. Mapping a Python Class to a MySQL Table
- Understand the process of mapping a Python Class to a corresponding MySQL table, enabling seamless interaction between Python objects and database records.

### 7. Creating a Python Virtual Environment
- Learn how to create a Python Virtual Environment to ensure a clean and isolated development environment for your project.

## Project Structure
- `0-add_attribute.py`: Script to add a new attribute to a Python object dynamically.
- `1-filter_states.py`: Script to display all states from the database hbtn_0e_0_usa where name matches a certain pattern.
- `2-my_filter_states.py`: Script to display all states from the database hbtn_0e_0_usa where name matches a given argument.
- `3-my_safe_filter_states.py`: Script to display all states from the database hbtn_0e_0_usa where name matches a given argument safely.
- `4-cities_by_state.py`: Script to list all cities from the database hbtn_0e_4_usa.
- `5-filter_cities.py`: Script to display all cities from the database hbtn_0e_4_usa where name matches a certain state.
- `6-model_state.py`: Python class definition of a State with SQLAlchemy.
- `7-model_state_fetch_all.py`: Script to list all State objects from the database hbtn_0e_6_usa.
- `8-model_state_fetch_first.py`: Script to print the first State object from the database hbtn_0e_6_usa.
- `9-model_state_filter_a.py`: Script to list all State objects containing the letter 'a' from the database hbtn_0e_6_usa.
- `10-model_state_my_get.py`: Script to print the State object with the name passed as an argument from the database hbtn_0e_6_usa.
- `11-model_state_insert.py`: Script to add a new State object to the database hbtn_0e_6_usa.
- `12-model_state_update_id_2.py`: Script to update the name of a State object with id = 2 from the database hbtn_0e_6_usa.
- `13-model_state_delete_a.py`: Script to delete all State objects with a name containing the letter 'a' from the database hbtn_0e_6_usa.
- `model_city.py`: Python class definition of a City with SQLAlchemy.
- `14-model_city_fetch_by_state.py`: Script to list all City objects related to a State from the database hbtn_0e_14_usa.
