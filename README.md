# AirBnB_clone_v4: Web dynamic

![hbnb](https://camo.githubusercontent.com/a0c52a69dc410e983b8c63fa4aa57e83cb4157cd/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67)

## Table of Contents

* [Description](#description)
* [Purpose](#purpose)
* [Requirements](#requirements)
* [File Descriptions](#file-descriptions)
* [Environmental Variables](#environmental-variables)
* [Usage](#usage)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)

## Description

**hbnb** is a full-stack clone of the web application [AirBnB](https://www.airbnb.com/). This clone was built in four iterative phases. This version includes completion of [Phase 1](https://github.com/bchen528/AirBnB_clone_v1), [Phase 2](https://github.com/bchen528/AirBnB_clone_v2), [Phase 3](https://github.com/bchen528/AirBnB_clone_v3) plus Phase 4 (Final version!), which involves loading objects from the client-side using our custom RESTful API and jQuery.

### Load objects from the client-side using a custom RESTful API and jQuery
![webdynamic](https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step5.png)

**Links to other versions:**
* [AirBnB_clone_v1: Console and web static](https://github.com/bchen528/AirBnB_clone_v1)
* [AirBnB_clone_v2: MySQL, deploy web static, web framework](https://github.com/bchen528/AirBnB_clone_v2)
* [AirBnB_clone_v3: RESTful API](https://github.com/bchen528/AirBnB_clone_v3)

## Purpose
The purpose of Phase 4 is to learn how to:
* request own API
* modify an HTML element style
* get/update HTML element style
* make a GET request with jQuery Ajax
* make a POST request with jQuery Ajax
* modify the DOM
* listen/bind to DOM events
* listen/bind to user events

## Requirements
* All files compiled with Ubuntu 14.04 LTS
* Documentation
* Organized files in proper folders
* Python unit tests for all files
* All files must be pep8 and semistandard compliant

## Environment

* __OS:__ Ubuntu 14.04 LTS
* __language:__ Python 3.4.3
* __web server:__ nginx/1.4.6
* __application server:__ Flask 0.12.2, Jinja2 2.9.6
* __web server gateway:__ gunicorn (version 19.7.1)
* __database:__ mysql Ver 14.14 Distrib 5.7.18
* __documentation:__ Swagger (flasgger==0.6.6)
* __style:__
  * __python:__ PEP 8 (v. 1.7.0)
  * __web static:__ [W3C Validator](https://validator.w3.org/)
  * __bash:__ ShellCheck 0.3.3

## File Descriptions
  **Note:** Below highlights only new file additions for Phase 4. For file descriptions from previous phases: [Phase 1](https://github.com/bchen528/AirBnB_clone_v1) | [Phase 2](https://github.com/bchen528/AirBnB_clone_v2) | [Phase3](https://github.com/bchen528/AirBnB_clone_v3)
  * [tests](/tests/) - unit test files
  * [web_dynamic](web_dynamic) - contains Flask, template, static files
    * [0-hbnb.py](web_dynamic/0-hbnb.py) - Flask app that integrates with AirBnB static HTML template, include caching ids
      * `teardown_db` - after each request, this method calls .close() (i.e. .remove()) on the current SQLAlchemy Session
      * `hbnb_filters` - handles request to custom template with states, cities & amentities
    * [1-hbnb.py](web_dynamic/1-hbnb.py) - Flask app that integrates with AirBnB static HTML template, add checkboxes
      * `teardown_db` - after each request, this method calls .close() (i.e. .remove()) on the current SQLAlchemy Session
      * `hbnb_filters` - handles request to custom template with states, cities & amentities
    * [2-hbnb.py](web_dynamic/2-hbnb.py) - Flask app that integrates with AirBnB static HTML template, check API status functionality and then test requesting HBNB API
      * `teardown_db` - after each request, this method calls .close() (i.e. .remove()) on the current SQLAlchemy Session
      * `hbnb_filters` - handles request to custom template with states, cities & amentities
    * [3-hbnb.py](web_dynamic/3-hbnb.py) - Flask app that integrates with AirBnB static HTML template, make Places article dynamic
      * `teardown_db` - after each request, this method calls .close() (i.e. .remove()) on the current SQLAlchemy Session
      * `hbnb_filters` - handles request to custom template with states, cities & amentities
    * [4-hbnb.py](web_dynamic/4-hbnb.py) - Flask app that integrates with AirBnB static HTML template, implement filter places by amenity with search button click
      * `teardown_db` - after each request, this method calls .close() (i.e. .remove()) on the current SQLAlchemy Session
      * `hbnb_filters` - handles request to custom template with states, cities & amentities
    * [100-hbnb.py](web_dynamic/100-hbnb.py) - Flask app that integrates with AirBnB static HTML template, implement State and Cities filters with search button click
      * `teardown_db` - after each request, this method calls .close() (i.e. .remove()) on the current SQLAlchemy Session
      * `hbnb_filters` - handles request to custom template with states, cities & amentities
    * [101-hbnb.py](web_dynamic/101-hbnb.py) - Flask app that integrates with AirBnB static HTML template, show and hide reviews
      * `teardown_db` - after each request, this method calls .close() (i.e. .remove()) on the current SQLAlchemy Session
      * `hbnb_filters` - handles request to custom template with states, cities & amentities
    * [templates](web_dynamic/templates) - contains HTML templates
      * [0-hbnb.html](web_dynamic/templates/0-hbnb.html) - add variable cache_id as query string to each `<LINK>` tag URL
      * [1-hbnb.html](web_dynamic/templates/1-hbnb.html) - add jQuery and JS to make dynamic filters
      * [2-hbnb.html](web_dynamic/templates/2-hbnb.html) - add API status checker
      * [3-hbnb.html](web_dynamic/templates/3-hbnb.html) - fetch places, make places article dynamic
      * [4-hbnb.html](web_dynamic/templates/4-hbnb.html) - filter places by amenity
      * [100-hbnb.html](web_dynamic/templates/100-hbnb.html) - filter states and cities
      * [101-hbnb.html](web_dynamic/templates/101-hbnb.html) - show/hide reviews
    * [static](web_dynamic/static) - contains CSS, Javascript, image files
      * [scripts](web_dynamic/static/scripts) - Javascript files
        * [1-hbnb.js](web_dynamic/static/scripts/1-hbnb.js) - make dynamic filters
        * [2-hbnb.js](web_dynamic/static/scripts/2-hbnb.js) - add API status checker
        * [3-hbnb.js](web_dynamic/static/scripts/3-hbnb.js) - fetch places from API
        * [4-hbnb.js](web_dynamic/static/scripts/4-hbnb.js) - filter places by amenity
        * [100-hbnb.js](web_dynamic/static/scripts/100-hbnb.js) - filter states and cities
        * [101-hbnb.js](web_dynamic/static/scripts/101-hbnb.js) -  show/hide reviews
      * [styles](web_dynamic/static/styles) - CSS files
        * [3-footer.css](web_dynamic/static/3-footer.css) - footer style
        * [3-header.css](web_dynamic/static/3-header.css) - header style
        * [4-common.css](web_dynamic/static/4-common.css) - body style
        * [6-filters.css](web_dynamic/static/6-filters.css) - filter style
        * [8-places.css](web_dynamic/static/8-places.css) - places style
      

## Environmental Variables
```
HBNB_ENV: running environment. It can be “dev” or “test” for the moment (“production” soon!)
HBNB_MYSQL_USER: the username of your MySQL
HBNB_MYSQL_PWD: the password of your MySQL
HBNB_MYSQL_HOST: the hostname of your MySQL
HBNB_MYSQL_DB: the database name of your MySQL
HBNB_TYPE_STORAGE: the type of storage used. It can be “file” (using FileStorage) or db (using DBStorage)
```

## Two storage systems

 This application is designed to run with 2 storage engine models:

* File Storage Engine:

  * `/models/engine/file_storage.py`

* Database Storage Engine:

  * `/models/engine/db_storage.py`

  * To Setup the DataBase for testing and development, there are 2 setup
  scripts that setup a database with certain privileges: `setup_mysql_test.sql`
  & `setup_mysql_test.sql` (for more on setup, see below).

  * The Database uses Environmental Variables for tests.  To execute tests with
  the environmental variables prepend these declarations to the execution
  command:

```
$ HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd \
HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db \
[COMMAND HERE]
```

## Usage
Run your api in one terminal window:
```
user@ubuntu:~/AirBnB_v4$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db HBNB_API_PORT=5001 python3 -m api.v1.app
...
```
And your Flask file in another:
```
user@ubuntu:~/AirBnB_v4$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_dynamic.2-hbnb
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
Open up a web browser and type `0.0.0.0:5000/2-hbnb`

**In place of `2-hbnb` you can specify other Flask files versions**

Look at upper right dot: that's your API status checker! Red means that our API is available. Grey means that our API is not available.

API not available
![2hbnb](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/309/hbnb_2_0.jpg)

API available!
![2hbnbapi](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/309/hbnb_2_1.jpg)

Filters functionality
![checkbox](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/309/hbnb_1_2.jpg)

## Configuration Files

The `/config/` directory contains configuration files for `nginx` and the
Upstart scripts.  The nginx configuration file is for the configuration file in
the path: `/etc/nginx/sites-available/default`.  The enabled site is a sym link
to that configuration file.  The upstart script should be saved in the path:
`/etc/init/[FILE_NAME.conf]`.  To begin this service, execute:

```
$ sudo start airbnb.conf
```
This script's main task is to execute the following `gunicorn` command:

```
$ gunicorn --bind 127.0.0.1:8001 wsgi.wsgi:web_flask.app
```

The `gunicorn` command starts an instance of a Flask Application.

---

### Web Server Gateway Interface (WSGI)

All integration with gunicorn occurs with `Upstart` `.conf` files.  The python
code for the WSGI is listed in the `/wsgi/` directory.  These python files run
the designated Flask Application.

## Setup

This project comes with various setup scripts to support automation, especially
during maintanence or to scale the entire project.  The following files are the
setupfiles along with a brief explanation:

* **`dev/setup.sql`:** Drops test and dev databases, and then reinitializes
the datbase.

  * Usage: `$ cat dev/setup.sql | mysql -uroot -p`

* **`setup_mysql_dev.sql`:** initialiezs dev database with mysql for testing

  * Usage: `$ cat setup_mysql_dev.sql | mysql -uroot -p`

* **`setup_mysql_test.sql`:** initializes test database with mysql for testing

  * Usage: `$ cat setup_mysql_test.sql | mysql -uroot -p`

* **`0-setup_web_static.sh`:** sets up nginx web server config file & the file
  structure.

  * Usage: `$ sudo ./0-setup_web_static.sh`

* **`3-deploy_web_static.py`:** uses 2 functions from (1-pack_web_static.py &
  2-do_deploy_web_static.py) that use the fabric3 python integration, to create
  a `.tgz` file on local host of all the local web static fils, and then calls
  the other function to deploy the compressed web static files.  Command must
  be executed from the `AirBnB_clone` root directory.

  * Usage: `$ fab -f 3-deploy_web_static.py deploy -i ~/.ssh/holberton -u ubuntu`

## Testing

### `unittest`

This project uses python library, `unittest` to run tests on all python files.
All unittests are in the `./tests` directory with the command:

* File Storage Engine Model:

  * `$ python3 -m unittest discover -v ./tests/`

* DataBase Storage Engine Model

```
$ HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd \
HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db \
python3 -m unittest discover -v ./tests/
```

---

### All Tests

The bash script `init_test.sh` executes all these tests for both File Storage &
DataBase Engine Models:

  * checks `pep8` style

  * runs all unittests

  * runs all w3c_validator tests

  * cleans up all `__pycache__` directories and the storage file, `file.json`

  * **Usage `init_test.sh`:**

```
$ ./dev/init_test.sh
```

---

### CLI Interactive Tests

* This project uses python library, `cmd` to run tests in an interactive command
  line interface.  To begin tests with the CLI, run this script:

#### File Storage Engine Model

```
$ ./console.py
```

#### To execute the CLI using the Database Storage Engine Model:

```
$ HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd \
HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db \
./console.py
```

#### For a detailed description of all tests, run these commands in the CLI:

```
(hbnb) help help
List available commands with "help" or detailed help with "help cmd".
(hbnb) help

Documented commands (type help <topic>):
========================================
Amenity    City  Place   State  airbnb  create   help  show
BaseModel  EOF   Review  User   all     destroy  quit  update

(hbnb) help User
class method with .function() syntax
        Usage: User.<command>(<id>)
(hbnb) help create
create: create [ARG] [PARAM 1] [PARAM 2] ...
        ARG = Class Name
        PARAM = <key name>=<value>
                value syntax: "<value>"
        SYNOPSIS: Creates a new instance of the Class from given input ARG
                  and PARAMS. Key in PARAM = an instance attribute.
        EXAMPLE: create City name="Chicago"
                 City.create(name="Chicago")
```

* Tests in the CLI may also be executed with this syntax:

  * **destroy:** `<class name>.destroy(<id>)`

  * **update:** `<class name>.update(<id>, <attribute name>, <attribute value>)`

  * **update with dictionary:** `<class name>.update(<id>,
    <dictionary representation>)`

---

### Continuous Integration Tests

Uses [Travis-CI](https://travis-ci.org/) to run all tests on all commits to the
github repo

## Bugs

At this time, there are no known bugs.

## Authors
Phase 4:
* Becky Chen, [bchen528](https://github.com/abdelrahman21-arch)

**Note: As per Holberton's requirements, we practice working with new Phase 1, 2, 3 codebases in our Phase 4 version.**

Phases 1 - 3:
* MJ Johnson, [@mj31508](https://github.com/mj31508)
* David John Coleman II, [davidjohncoleman.com](http://www.davidjohncoleman.com/) | [@djohncoleman](https://twitter.com/djohncoleman)
* Kimberly Wong, [kjowong](https://github.com/kjowong) | [@kjowong](https://twitter.com/kjowong) | [kjowong@gmail.com](kjowong@gmail.com)
* Carrie Ybay, [hicarrie](https://github.com/hicarrie) | [@hicarrie_](https://twitter.com/hicarrie_)
* Jared Heck, [jarehec](https://github.com/jarehec) | [@jarehec](https://twitter.com/jarehec)

## License

MIT License
