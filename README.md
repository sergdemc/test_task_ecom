# Test task e.com
This is a web application that determines completed forms based on received field data. The application stores a list of form templates in a database, each defined by a unique set of fields with specified data types such as email, phone, date, and text. The goal is to process POST requests with field data and determine the appropriate form template. If a matching form template is found, the application returns its name; otherwise, it dynamically identifies field types and returns a list of fields with their inferred types.

Implementation without using any web frameworks, only a database in Docker and standard libraries.

Form templates are in the _db_data.json_ file.

Example of a POST request with field data:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"field_email": "example@example.com", "field_phone": "+71234567890"}' http://127.0.0.1:5001/get_form

```

Example of a response if the form is found:
```bash
"Form_name"
```
And if the form is not found:
```bash
{"field_email": "email", "field_phone": "phone"}
```

## Installation

### Prerequisites

#### Python

Before installing the package make sure you have Python version 3.8.1 or higher installed:

```bash
>> python --version
Python 3.10+
```

#### Docker

The project uses Docker to run the database. To install Docker use its [official instruction](https://docs.docker.com/get-docker/).

### Application

To use the application, you need to clone the repository to your computer. This is done using the `git clone` command. Clone the project:

```bash
git clone git@github.com:sergdemc/test_task_ecom.git && cd test_task_ecom 
```

Then you have to install all necessary dependencies in your virtual environment:

```bash
make install
```

## Usage

Start the Mongo database in the Docker container by running: 
```bash
make start-mongo
```

Start the application by running:
```bash
make server
```
_By default, the server will be available at http://127.0.0.1:5001._


## Testing

First, run the database server and the application if it is not running:
```bash
make start-mongo
make server
```

To run tests use:
```bash
make test
```
To run tests with coverage use:
```bash
make coverage
```

Stop the database server:
```bash
make stop-mongo
```
