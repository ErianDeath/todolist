# TodoList App

This is a simple TodoList application built using Flask. It allows users to create, view, and manage their tasks. The application supports user authentication and ensures that each user's tasks are private.

## Features

- User authentication (login required to access the app)
- Create new tasks
- View all tasks
- Mark tasks as completed
- Delete tasks

## Requirements

- Python 3.x
- Flask
- SQLAlchemy
- Flask-Login
- bcrypt

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/todolist-app.git
    cd todolist-app
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

5. Run the application:
    ```bash
    flask run
    ```

## Usage

1. Open your web browser and go to `http://127.0.0.1:5000/`.
2. Register a new account or log in with an existing account.
3. Create, view, and manage your tasks.

## Project Structure

The project is organized as follows:



