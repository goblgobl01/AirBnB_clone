AirBnB_clone
------------------------------------------------------------------------------------------
The HBNB project is an AirBnB cloning that's divided into different smaller projects where in each project we work on a set of technologies to build a specific thing.

Project Description
------------------------------------------------------------------------------------------
The Airbnb project is divided into 7 smaller projects, which are:
The console:

    Create data model.
    CLI to manipulate objects.
    Storage engine abstraction (file storage engine).

Web static:

    Static HTML/CSS.

MySql:

    Add database storage engine.

Deploy Static:

    Deploy the application to go live!

Web Framework:

    Web server creation.
    Dynamic HTML.

RESTful API:

    Expose stored objects via JSON interface.

Web Dynamic:

    Using JQuery.
    Loading objects from client side.

Console (CLI) Description

    This console is a single use function (a CLI) from which you can create, modify and delete objects
    in your file storage.
    This is a sandbox to check what does and doesn't work in the storage.
    This project covers file serialization and deserialization in JSON.
    Every modification, creation or deletion of any data is saved in the JSON file.
    The console is basically the creation of the File Storage Engine.

Technologies
Console (CLI) Technologies

    The console is written in Python.
    The following coding style is verified by the PEP8.
    The console class HBNBCommand is based on the cmd python module.
    JSON to save data, serialize and deserialize it.
    Unittesting.

Installation

    Clone the project on your PC

$ https://github.com/goblgobl01/AirBnB_clone.git

Getting Started

    Get into the directory

$ cd ./AirBnB_clone

    Start using the console (CLI)

$ ./console.py

File Storage Engine

All data operations in the CLI are saves in a JSON file and the saved data will be retrieved when the console is launched again. The FileStorage engine is written in the FileStorage class and has the following functions:

    all: to return all the data.
    new: to add a newly created data to the existing list of data.
    save: to save the data in JSON file.
    reload: to reload data from the JSON file.

Data to create, modify and delete in CLI
All the data classes inherit from a common parent class called BaseClass.
The BaseClass contains the following attributes:

    id: unique id for each instance.
    created_at: date of creation.
    updated_at: date of last instance update.

The BaseClass contains the following methods:

    init: used for initialization.
    str: to return a string representation of an instance.
    save: to save the data.
    to_dict: to return a dictionary representation of an instance.

The other classes that inherit from BaseClass are:

    User
    State
    City
    Amenity
    Place
    Review

Console Functionalities and Usage Examples:
The console has different functionalities (commands), which we'll be covering in the upcoming list:

    quit: to quit the console.
    help: to display a list of the available commands and to display a specific command's help (usage, documentation..)

The usage of the help command is very important because it shows the user how to each command and functionality in the CLI.
Here are some usage examples of these commands:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help create

        Create an instance of BaseModel
        Usage: create <class Name>
        
(hbnb) help show

        Prints the string representation of an instance based on the class name
        and id.
        Usage: show <class Name> <id>
        
(hbnb) quit
$

    create <class_name>: to create a data instance.
    show <class_name> <instance_id>: to print the string representation of an instance.
    destroy <class_name> <instance_id>: to delete an instance.
    all <class_name>: to print all string representation of all the instances based or not on the class name (the <class_name> is optional).
    update <class_name> <instance_id> <attribute_name> <attribute_value>: to update an existing instance by modifying it's attribute value or by creating a new attribute.

Here'are some usage examples of these commands:

$ ./console.py
(hbnb) create BaseModel
cf2d280d-b163-408d-a77e-67cf07163139
(hbnb) create User
f5daf06e-dfc2-49ee-ac82-4ee6639656c4
(hbnb) create City
9504f9e8-9e80-4f8e-81ee-2555789c171b
(hbnb) create User
a096d36f-c829-488d-88b4-5a5574b2f729
(hbnb) all
["[User] (a096d36f-c829-488d-88b4-5a5574b2f729) {'created_at': datetime.datetime(2020, 2, 20, 1, 4, 26, 324423), 'updated_at': datetime.datetime(2020, 2, 20, 1, 4, 26, 324496), 'id': 'a096d36f-c829-488d-88b4-5a5574b2f729'}", "[City] (9504f9e8-9e80-4f8e-81ee-2555789c171b) {'created_at': datetime.datetime(2020, 2, 20, 1, 4, 22, 51573), 'updated_at': datetime.datetime(2020, 2, 20, 1, 4, 22, 51646), 'id': '9504f9e8-9e80-4f8e-81ee-2555789c171b'}", "[User] (f5daf06e-dfc2-49ee-ac82-4ee6639656c4) {'created_at': datetime.datetime(2020, 2, 20, 1, 4, 13, 308208), 'updated_at': datetime.datetime(2020, 2, 20, 1, 4, 13, 308285), 'id': 'f5daf06e-dfc2-49ee-ac82-4ee6639656c4'}", "[BaseModel] (cf2d280d-b163-408d-a77e-67cf07163139) {'created_at': datetime.datetime(2020, 2, 20, 1, 4, 8, 788705), 'updated_at': datetime.datetime(2020, 2, 20, 1, 4, 8, 788772), 'id': 'cf2d280d-b163-408d-a77e-67cf07163139'}"]

Contributors:

Elmsafer Abdellah
Mohammed Maarafi: