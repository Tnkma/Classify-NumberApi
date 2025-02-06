# HNGIntern - Stage 0 - Classify Number API

This repository contains the project for the HNG Internship Stage 1. The primary focus of this project is to build and demonstrate a simple Python-based web application using the Django framework that provides a public API to classify numbers.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Methods](#methods)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is part of the [HNG Internship program](https://hng.tech/hire/python-developers) stage 1. It is designed to help interns understand the basics of web development using Python and Django. The application demonstrates an API that accepts a number as input and returns interesting mathematical properties about it, along with a fun fact fetched from an external Numbers API.

## Features

- Django-based web application
- REST API support using Django REST Framework (DRF)
- Cross-Origin Resource Sharing (CORS) configured for handling requests from any origin
- Classifies numbers by calculating properties like Armstrong, prime, perfect, digit sum, and whether they are odd or even
- Integrates with the Numbers API to fetch a fun fact about the number

## Installation

To install the necessary dependencies for this project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

2. Create a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate   # On Windows use `env\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Setup

To run the project, follow these steps:

1. Run the development server:
    ```bash
    python manage.py runserver
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000/` to access the application. You can also test the API endpoint using a web browser or tools like Postman.

## Usage

To classify a number, send a GET request to the endpoint with a number as a query parameter. For example:
    ```
    GET** <your-domain.com>/api/classify-number?number=371
    ```

The API will return a JSON response with details such as whether the number is prime, perfect, its digit sum, its mathematical properties (e.g., Armstrong, odd, or even), and a fun fact about the number.

## Methods

### API Endpoint: Classify Number

- **Endpoint**: `/api/classify-number`
- **Method**: `GET`
- **Query Parameter**: `number` (integer) - The number to classify.
- **Success Response** (200 OK):
    ```json
    {
        "number": 371,
        "is_prime": false,
        "is_perfect": false,
        "properties": ["armstrong", "odd"],
        "digit_sum": 11,
        "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
    }
    ```
- **Error Response** (400 Bad Request):
    ```json
    {
        "number": "alphabet",
        "error": true
    }
    ```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. If you find any issues, feel free to open an issue in the repository.

## License

This project is licensed under the [MIT License](LICENSE).
