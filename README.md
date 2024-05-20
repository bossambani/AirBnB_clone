**AirBnb Clone - The Console** 

*Welcome to the AirBnB Clone project! This Project is a simplified version of the AirBnB web application*

## Table of Contents
-[Description](#description)
-[command Interpreter](#command-interpreter)
-[How to Start](#how-to-start)
-[How to Use](#how-to-use)
-[Contributors](#contributors)


## Description

The AirBnB Clone project aims to emulate a simplified version of the AirBnB web application. This project includes the following features:

- A custom command interpreter that allows users to create, update, delete, and retrieve various objects.
- Storage of data using JSON serialization and deserialization.
- Models for Users, Places, States, Cities, and Reviews, each with various attributes.
- Unittests to ensure the functionality and reliability of the models and the command interpreter.

## Command Interpreter

The command interpreter provides a way to manage your AirBnB objects through a command-line interface. Below are instructions on how to start and use the command interpreter.

### How to Start

To start the command interpreter, navigate to the root directory of the project and run the following command:

./console.py

### How to Use

create <class name>: Creates a new instance of the specified class.
show <class name> <id>: Prints the string representation of an instance based on the class name and id.
destroy <class name> <id>: Deletes an instance based on the class name and id.
all [class name]: Prints all string representations of all instances, or all instances of a specific class.
update <class name> <id> <attribute name> "<attribute value>": Updates an instance based on the class name and id by adding or updating an attribute.

###Contributors
This project was developed by the following contributors:

Boss Ambaka (@bossambani)
Elijah Akande (@EvaStrings)
See the AUTHORS file for more details.
