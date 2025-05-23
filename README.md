# A Simple Product Invetory CLI Application
This is an implementation of a simple CLI application for tracking product inventories.

## Set up
- Clone the repository
- Create a virtual environment, activate and install dependancies
    ```
    pipenv install && pipenv shell

    # or

    python -m venv .venv
    source .venv/bin/activate
    pip -r install requirements.txt

    ```

- Run the migrations to create the sqlite database and the tables
    ```
    alembic upgrade head
    ```

- Seed the default data
    ```
    python seed.py
    ```

- Finally run the application
    ```
    python cli.py
    ```

## System Requirements
- Python >= 3.10