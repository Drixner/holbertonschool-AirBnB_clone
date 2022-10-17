[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)
![GitHub last commit](https://img.shields.io/github/last-commit/Drixner/holbertonschool-AirBnB_clone)

# AirBnB clone project

<p align="center">
  <img src=" " alt="Hbton logo">
</p>

# Table of Contents
- [Description](#description)
- [Classes](#classes)
- [Storage](#storage)
- [Console](#console)
- [How to Test](#how-to-test)

## Description
HolbertonBnB is a web app with a full development of back-end and front-end API
integrating also SQL storage 
This project is the part 1 of 4 in which the back-end console is created
and deployed.
This is an educational purposes clone from [AirBnB](https://www.airbnb.com/)

## Classes

This projects uses the following classes:

|     | BaseModel | FileStorage | User | Amenity | City | State | Place | Review |
| --- | --------- | ----------- | -----| ----- | -----| ------- | ----- | ------ |
| Public instance attributes | id<br>created_at<br>updated_at | | Inherits from BaseModel | Inherits from BaseModel | Inherits from BaseModel | Inherits from BaseModel | Inherits from BaseModel | Inherits from BaseModel |
| Public instance methods | save<br>to_dict | all<br>new<br>save<br>reload |  |  |  |  |  |  |
| Public class attributes | | | email<br>password<br>first_name<br>last_name| name | name_id<br>name | name | city_id<br>user_id<br>name<br>description<br>number_rooms<br>number_bathrooms<br>max_guest<br>price_by_night<br>latitude<br>longitude<br>amenity_ids | place_id<br>user_id<br>text |
| Private class attributes | | file_path<br>objects | | | | | | |

## Storage

The presented classes are stored in [FileStorage](./models/engine/file_storage.py) class file.
When the console is initialized, the console redirects an instance of
FileStorage named `storage`,
this `storage` object is loaded or reloaded from any class instances stored in the
JSON file file.json.

Class instances are created, updated, or deleted and `storage` object registers
changes into file.json.



## Console
The console is a CLI that allows the use of data as backend tool.
It can be used to handle all classes predefined  previously called into
`storage` object.

<p align="center">
  <img src="https://i.imgur.com/gyqA0od.png" alt="storage">
</p>

### How to Use the CLI non-interactive

To run the console in non-interactive mode:

```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb)
$
```

### How to Use the CLI interactive

To run the console in interactive mode:

run the file console.py:

```
$ ./console.py

```

Running in interactive mode, the console displays a prompt for input:

```
$ ./console.py
(hbnb)
```

To quit the console, enter the command `quit`, or input an EOF signal
(`ctrl+D`).

```
$ ./console.py
(hbnb) quit
$
```

```
$ ./console.py
(hbnb) EOF
$
```

### Console Commands

HolbertonBnB supports the following commands:

 **create**
  * Usage: `create`
creates a new instance of a given class. Class' ID is printed and
the instance is saved to the file file.json.

```
$ ./console.py
(hbnb) create BaseModel
c71c66cc-2aea-4a38-aa05-0a69fbf1b096
(hbnb) quit
$ cat file.json ; echo ""
{"BaseModel.c71c66cc-2aea-4a38-aa05-0a69fbf1b096": {"__class__": "BaseModel",
"id": "c71c66cc-2aea-4a38-aa05-0a69fbf1b096", "updated_at": "2022-10-16T19:12:38
.604135", "created_at": "2022-10-16T19:12:38.604089"}}
```

**show**
  * Usage: `show`
prints a string representation of a class instance based on a given id.

```
$ ./console.py
(hbnb) create User
9d800431-1b19-499b-bc6e-fcb09e8cc699
(hbnb)
(hbnb) show User 1e32232d-5a63-4d92-8092-ac3240b29f46
show User 9d800431-1b19-499b-bc6e-fcb09e8cc699
[User] (9d800431-1b19-499b-bc6e-fcb09e8cc699) {'updated_at': datetime.datetime
(2022, 10, 16, 19, 17, 58, 890984), 'id': '9d800431-1b19-499b-bc6e-fcb09e8cc699'
, 'created_at': datetime.datetime(2022, 10, 16, 19, 17, 58, 890946)}
(hbnb) 
```
**destroy**
  * Usage: `destroy`
deletes a class instance based on a given id from the storage file file.json and
it is updated accordingly.

```
$ ./console.py
(hbnb) create Review
eac9a563-241c-48ef-b73d-e541ab5b96ea
(hbnb) create City
27c62d6b-4925-4c17-9c9e-16f81aa71f7c
(hbnb)
(hbnb) destroy City 27c62d6b-4925-4c17-9c9e-16f81aa71f7c
(hbnb) destroy Review eac9a563-241c-48ef-b73d-e541ab5b96ea
(hbnb) quit
$ cat file.json ; echo ""
{}
```

**all**
  * Usage: `all`
prints the string representations of all instances of a given class. If no
class name is provided, the command prints all instances of every class.

```
$ ./console.py
(hbnb) create City
6b34ebad-9c64-490f-8045-da65ee62c938
(hbnb) create City
6842d2ea-ad84-4331-a4b5-5099a2740bc9
(hbnb) create User
158f0b85-3276-4981-9d9a-6098af29d18
(hbnb)
(hbnb) all City
["[City] (6842d2ea-ad84-4331-a4b5-5099a2740bc0) {'updated_at': datetime.datetime
(2022, 10, 16, 19, 23, 30, 951862), 'id': '6842d2ea-ad84-4331-a4b5-5099a2740bc0'
, 'created_at': datetime.datetime(2022, 10, 16, 19, 23, 30, 951807)}", "[City] 
(6b34ebad-9c64-490f-8045-da65ee62c93a) {'updated_at': datetime.datetime(2022, 10
, 16, 19, 23, 22, 681892), 'id': '6b34ebad-9c64-490f-8045-da65ee62c93a', 'create
d_at': datetime.datetime(2022, 10, 16, 19, 23, 22, 681839)}"]
(hbnb)
(hbnb) all User
["[User] (158f0b85-3276-4981-9d9a-6098af29d182) {'updated_at': datetime.datetime
(2022, 10, 16, 19, 23, 49, 220452), 'id': '158f0b85-3276-4981-9d9a-6098af29d182'
, 'created_at': datetime.datetime(2022, 10, 16, 19, 23, 49, 220403)}"]
hbnb) 
(hbnb) all
["[City] (6842d2ea-ad84-4331-a4b5-5099a2740bc0) {'updated_at': datetime.datetime
(2022, 10, 16, 19, 23, 30, 951862), 'id': '6842d2ea-ad84-4331-a4b5-5099a2740bc0'
, 'created_at': datetime.datetime(2022, 10, 16, 19, 23, 30, 951807)}", "[City] 
(6b34ebad-9c64-490f-8045-da65ee62c93a) {'updated_at': datetime.datetime(2022, 10
, 16, 19, 23, 22, 681892), 'id': '6b34ebad-9c64-490f-8045-da65ee62c93a', 'create
d_at': datetime.datetime(2022, 10, 16, 19, 23, 22, 681839)}",["[User] (158f0b85-
3276-4981-9d9a-6098af29d182) {'updated_at': datetime.datetime
(2022, 10, 16, 19, 23, 49, 220452), 'id': '158f0b85-3276-4981-9d9a-6098af29d182'
, 'created_at': datetime.datetime(2022, 10, 16, 19, 23, 49, 220403)}"]
(hbnb)
```

**update**
  * Usage: `update`
updates a class instance based on a given id with a given key/value attribute	
pair or dictionary of attribute pairs. If update is called with a single 
key/value attribute pair, only "simple" attributes can be updated (ie. not 
id, created_at, and/or updated_at).

```
$ ./console.py
(hbnb) create User
b7c2338a-7971-436b-a212-6beed80cbb33
(hbnb)
(hbnb) update User b7c2338a-7971-436b-a212-6beed80cbb33 first_name "Betty"
<971-436b-a212-6beed80cbb33 first_name "Betty"
(hbnb) User.show("b7c2338a-7971-436b-a212-6beed80cbb33")
[User] (b7c2338a-7971-436b-a212-6beed80cbb33) {'first_name': 'Betty', 'id':
'b7c2338a-7971-436b-a212-6beed80cbb33', 'updated_at': datetime.datetime(2022, 10
, 16, 19, 40, 21, 347198), 'created_at': datetime.datetime(2022, 10, 16, 19, 39,
55, 915377)}
(hbnb)
```

## How to Test:
Unittests for the CLI HolbertonBnB project are defined in the [tests](./tests)
folder. To run the entire test suite simultaneously, execute the following
command:

```
$ python3 unittest -m discover tests
```

Also, you can specify a single test file to run at a time:

```
$ python3 unittest -m tests/test_console.py
```

## Authors
| [<img src="https://avatars.githubusercontent.com/u/103861356?v=4" width=85><br><sub> Drixner Condor </sub>](https://github.com/Drixner) | [<img src="https://avatars.githubusercontent.com/u/98289735?v=4" width=85><br><sub> Salomón Chambi </sub>](https://github.com/schambig) |
| :---: | :---: |
