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

## Testing

To run the tests for this application, use the following command:
    ```bash
    pytest
    ```

Make sure you have `pytest` installed in your virtual environment. You can add it to your `requirements.txt` or install it separately using:
    ```bash
    pip install pytest
    ```

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
    ```bash
    git checkout -b feature-name
    ```
3. Make your changes and commit them with descriptive messages:
    ```bash
    git commit -m "Description of the feature or fix"
    ```
4. Push your changes to your forked repository:
    ```bash
    git push origin feature-name
    ```
5. Create a pull request to the main repository. Provide a clear description of your changes and the reasons for them.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

If you have any questions or suggestions, feel free to reach out to the project maintainer at [your-email@example.com].

