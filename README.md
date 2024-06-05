Sensor Data Service
----------

Quickstart
----------

Run the following commands to bootstrap your environment:

    git clone git@github.com:Pantilei/sensor-data-service.git
    cd sensor-data-service

Check your python version, must be ``3.12``:

    python3 -V 

Upgrade pip and install poetry:

    python3 -m pip install --upgrade pip
    curl -sSL https://install.python-poetry.org | python3 -

Optional. To make virtual enviroment in project directory run below command. Doing this way will make code editor automatically locate the virtual environment.

    poetry config --local virtualenvs.in-project true

Install dependencies with the ``poetry``:

    poetry install

Then create ``.env`` file based on ``.env.example`` in project root and set environment variables for application:

    cp .env.example .env

To run the web application: ::

    poetry run python3 -m sds

Swagger docs will be available on ``http://0.0.0.0:8000/docs`` in your browser.


Running with Docker
----------------------

You must have ``docker`` and ``docker-compose`` tools installed to work with material in this section.
First, create ``.env`` file like in `Quickstart` section or modify ``.env.example``.
Then just run (ensure database url is set as service name):

    docker-compose up --build

Swagger docs will be available on ``http://0.0.0.0:8000/docs`` in your browser.

Code formatting
---------------

Before commiting new changes ensure code quality by running code formatter script:

    poetry run scripts/format

Also in order to ensure the project will pass the tests run linting checker:

    poetry run scripts/lint

To be taken in count on a decision
----------------------------------
_NOTE: The following principles are arranged by importance's_
##### 1. Separation of Concerns (SoC) 

In software architecture, Separation of Concerns as the name says is a design principle that suggests separating each distinct section to address different individual concerns. It follows the idea that we don’t need to mix up things that don’t belong together.  

##### 2. Don’t Repeat Yourself (DRY)

Don’t Repeat Yourself is a principle for software development that aims to minimize the repetition of software patterns. It is widely acknowledged that repeating code all over your application is problematic. With the DRY principle, a system can be designed with a single, authoritative and unambiguous representation for every piece of knowledge. The Pragmatic Programmer written by Andy Hunt and Dave Thomas discusses this principle in their book.  

##### 3. You Ain’t Gonna Need It (YAGNI) 
You Ain’t Gonna Need It is a principle of software development methodology that states that Functionalities shouldn’t be added unless it is deemed necessary. We shouldn’t and don’t need to add complexity that we may not need.

##### 4. Keep it Simple Stupid (KISS) 
This Principle has quite many variations in the title name, “Keep it Simple, Stupid”, “Keep it simple, silly”, “Keep it short and simple”,“Keep it Sweet and Simple”, “Keep it Simple, Soldier”, “Keep it Simple, Sailor” - all meaning the same thing. As said by 15th Century genius, Leonardo Da Vinci, “Simplicity is the Ultimate Sophistication” that even Steve Jobs lived by, the best design if often a simple design and this principle states that most systems would work best if they are kept simple instead of complicated.
