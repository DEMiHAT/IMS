# Insurance Management System

A web-based application built with Python, Flask, and MySQL to manage customers, policies, claims, and payments for an insurance company.

## Table of Contents
- [About The Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Database Schema](#database-schema)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## About The Project

This project is a full-stack Insurance Management System. It provides a web interface for administrators or agents to perform essential CRUD (Create, Read, Update, Delete) operations on insurance data. The backend is powered by Flask, handling business logic and database interaction, while the frontend is built with standard HTML and CSS.

## Features

Based on the project structure, the system includes the following functionalities:

* **Customer Management:** Add and view customer details.
* **Policy Management:** Create new insurance policies and assign them to customers.
* **Claims Processing:** Add new claims for customers and view the status of existing claims.
* **Payment Tracking:** Log payments made by customers for their policies.
* **Agent Management:** (Inferred from database) Ability to store agent data and link them to customers.

## Tech Stack

* **Backend:** Python (Flask)
* **Database:** MySQL
* **Frontend:** HTML & CSS

## Database Schema

The application relies on a relational database (named `insurance_db` in the example) with the following core tables:

* `agents`: Stores information about insurance agents.
* `customers`: Stores customer details (name, DOB, email, etc.).
* `policies`: Defines the different types of insurance policies available.
* `claims`: Tracks claims filed by customers.
* `payments`: Logs all payments received.
* `agent_customers`: A junction table linking agents to their respective customers.
* `customer_policies`: A junction table linking customers to the policies they have purchased.

## Getting Started

Follow these instructions to get a local copy of the project up and running for development and testing.

### Prerequisites

You will need the following software installed on your system:
* [Python 3](https://www.python.org/downloads/)
* [MySQL Server](https://dev.mysql.com/downloads/mysql/)
* [pip](https://pip.pypa.io/en/stable/installation/) (Python package installer)

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/DEMiHAT/IMS.git](https://github.com/DEMiHAT/IMS.git)
    cd IMS
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install the required Python packages:**
    (You should create a `requirements.txt` file by running `pip freeze > requirements.txt` in your project directory. This file would typically include `Flask` and `mysql-connector-python` or `Flask-SQLAlchemy`.)
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set up the database:**
    * Start your MySQL server.
    * Log in and create the database:
        ```sql
        CREATE DATABASE insurance_db;
        ```
    * Create the required tables (e.g., `agents`, `customers`, `policies`, etc.) as seen in your screenshot. You should export your schema to a `.sql` file and provide instructions to import it.

5.  **Configure the application:**
    * Open the `app.py` file.
    * Find the database connection settings and update them with your local MySQL credentials (host, username, password, and database name).

6.  **Run the application:**
    ```sh
    python app.py
    ```

## Usage

Once the Flask server is running, open your web browser and navigate to:

`http://127.0.0.1:5000/`

You can use the navigation links to access different parts of the application, such as adding a new customer, assigning a policy, or viewing claims.

## License

Distributed under the MIT License. See `LICENSE` file for more information.

