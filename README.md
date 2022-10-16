<p align="center">
  <img src=" " alt="Hbton logo">
</p>

<p align="left"> AirBnB clone project</p>
---
## Description
HolbertonBnB is a web app with a full development of back-end and front-end API
integrating also SQL storage 
This project is the part 1 of 4 in which the back-end console is created
and deployed.
This is an educational purposes clone from [AirBnB](https://www.airbnb.com/)

## Classes

This projects uses the following classes:

|     | BaseModel | FileStorage | User | Amenity | City | Place | Review | State |
| --- | --------- | ----------- | -----| ----- | -----| ------- | ----- | ------ |
| Public instance attributes | id<br>created_at<br>updated_at | | Inherits BaseModel | Inherits BaseModel | Inherits BaseModel | Inherits BaseModel | Inherits BaseModel | Inherits BaseModel |
| Public instance methods | save<br>to_dict | all<br>new<br>save<br>reload |  |  |  |  |  |  |
| Public class attributes | | | email<br>password<br>first_name<br>last_name| name | _id<br>name | name | city_id<br>user_id<br>name<br>description<br>_rooms<br>_bathrooms<br>max_guest<br>price<br>latitude<br>longitude<br>amenity_id | place_id<br>user_id<br>text |
| Private class attributes | | file_path<br>objects | | | | | | |

## Storage

The presented classes are stored in [FileStorage](./models/engine/file_storage.py) class file.
When the console is initialized, the console redirects an instance of
FileStorage named storage.
#Storage object is loaded or reloaded from any class instances stored in the
JSON file file.json.
Class instances are created, updated, or deleted and storage object registers
changes intofile.json.

## Console
The console is a CLI that allows the use of data as backend tool.
It can be used to handle all classes predefined  previously called into
`storage` object.

### How to Use the CLI non-interactive
To run the console in non-interactive mode:

```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
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
(`ctrl-D`).

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
  * Usage: create <class>
Creates a new instance of a given class. Class' ID is printed and
the instance is saved to the file file.json.

```
$ ./console.py
(hbnb) create BaseModel
c71c66cc-2aea-4a38-aa05-0a69fbf1b096
(hbnb) quit
$ cat file.json ; echo ""
{"BaseModel.c71c66cc-2aea-4a38-aa05-0a69fbf1b096": {"__class__": "BaseModel",
"id": "c71c66cc-2aea-4a38-aa05-0a69fbf1b096", "updated_at": "2019-11-13T19:12:38
.604135", "created_at": "2019-11-13T19:12:38.604089"}}
```

 **show**
  * Usage: show <class> <id> or <class>.show(<id>)
Prints a string representation of a class instance based on a given id.

```
$ ./console.py
(hbnb) create User
9d800431-1b19-499b-bc6e-fcb09e8cc699
(hbnb)
(hbnb) show User 1e32232d-5a63-4d92-8092-ac3240b29f46
show User 9d800431-1b19-499b-bc6e-fcb09e8cc699
[User] (9d800431-1b19-499b-bc6e-fcb09e8cc699) {'updated_at': datetime.datetime
(2019, 11, 13, 19, 17, 58, 890984), 'id': '9d800431-1b19-499b-bc6e-fcb09e8cc699'
, 'created_at': datetime.datetime(2019, 11, 13, 19, 17, 58, 890946)}
(hbnb) 
(hbnb) User.show(9d800431-1b19-499b-bc6e-fcb09e8cc699)
[User] (9d800431-1b19-499b-bc6e-fcb09e8cc699) {'updated_at': datetime.datetime
(2019, 11, 13, 19, 17, 58, 890984), 'id': '9d800431-1b19-499b-bc6e-fcb09e8cc699'
, 'created_at': datetime.datetime(2019, 11, 13, 19, 17, 58, 890946)}
(hbnb) 
```
* **destroy**
  * Usage: `destroy <class> <id>` or `<class>.destroy(<id>)`
Deletes a class instance based on a given id from the storage file file.json and
it is updated accordingly.

```
$ ./console.py
(hbnb) create Review
eac9a563-241c-48ef-b73d-e541ab5b96ea
(hbnb) create City
27c62d6b-4925-4c17-9c9e-16f81aa71f7c
(hbnb)
(hbnb) destroy City 27c62d6b-4925-4c17-9c9e-16f81aa71f7c
(hbnb) Place.destroy(eac9a563-241c-48ef-b73d-e541ab5b96ea)
(hbnb) quit
$ cat file.json ; echo ""
{}
```

 **all**
  * Usage: all or all <class> or <class>.all()
Prints the string representations of all instances of a given class. If no
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
(2019, 11, 13, 19, 23, 30, 951862), 'id': '6842d2ea-ad84-4331-a4b5-5099a2740bc0'
, 'created_at': datetime.datetime(2019, 11, 13, 19, 23, 30, 951807)}", "[City] 
(6b34ebad-9c64-490f-8045-da65ee62c93a) {'updated_at': datetime.datetime(2019, 11
, 13, 19, 23, 22, 681892), 'id': '6b34ebad-9c64-490f-8045-da65ee62c93a', 'create
d_at': datetime.datetime(2019, 11, 13, 19, 23, 22, 681839)}"]
(hbnb)
(hbnb) User.all()
["[User] (158f0b85-3276-4981-9d9a-6098af29d182) {'updated_at': datetime.datetime
(2019, 11, 13, 19, 23, 49, 220452), 'id': '158f0b85-3276-4981-9d9a-6098af29d182'
, 'created_at': datetime.datetime(2019, 11, 13, 19, 23, 49, 220403)}"]
hbnb) 
(hbnb) all
["[City] (6842d2ea-ad84-4331-a4b5-5099a2740bc0) {'updated_at': datetime.datetime
(2019, 11, 13, 19, 23, 30, 951862), 'id': '6842d2ea-ad84-4331-a4b5-5099a2740bc0'
, 'created_at': datetime.datetime(2019, 11, 13, 19, 23, 30, 951807)}", "[City] 
(6b34ebad-9c64-490f-8045-da65ee62c93a) {'updated_at': datetime.datetime(2019, 11
, 13, 19, 23, 22, 681892), 'id': '6b34ebad-9c64-490f-8045-da65ee62c93a', 'create
d_at': datetime.datetime(2019, 11, 13, 19, 23, 22, 681839)}",["[User] (158f0b85-
3276-4981-9d9a-6098af29d182) {'updated_at': datetime.datetime
(2019, 11, 13, 19, 23, 49, 220452), 'id': '158f0b85-3276-4981-9d9a-6098af29d182'
, 'created_at': datetime.datetime(2019, 11, 13, 19, 23, 49, 220403)}"]
(hbnb)
```

 **count**
  * Usage: `count <class>` or `<class>.count()`
Retrieves the number of instances of a given class.

```
$ ./console.py
(hbnb) create Amenity
f1fc454f-2405-4e45-98bd-74e293ed377
(hbnb) create Amenity
e4a355f9-7566-4dad-8f1a-2f2037bcc41f
(hbnb) create Amenity
a311915e-0a6c-47a4-ad27-d49f650bc661
(hbnb) create Review
79935285-a783-47e6-9e8f-db3b4a25d6db
(hbnb) create Review
e20a8666-2861-4669-80a0-5da4af6b4c5d
(hbnb)
(hbnb) count Amenity
3
(hbnb) Review.count()
2
(hbnb) 
```

 **update**
  * Usage: update <class> <id> <attribute name> "<attribute value>"` or
`<class>.update(<id>, <attribute name>, <attribute value>)` or `<class>.update(
<id>, <attribute dictionary>).
Updates a class instance based on a given id with a given key/value attribute	
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
'b7c2338a-7971-436b-a212-6beed80cbb33', 'updated_at': datetime.datetime(2019, 11
, 13, 19, 40, 21, 347198), 'created_at': datetime.datetime(2019, 11, 13, 19, 39,
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
| [<img src="https://avatars.githubusercontent.com/u/103861356?v=4" width=115><br><sub> Drixner Condor </sub>](https://github.com/Drixner) | [<img src="https://avatars.githubusercontent.com/u/98289735?v=4" width=115><br><sub> Salomón Chambi </sub>](https://github.com/schambig) |
| :---: | :---: | :---: |
