# KeySpeed

KeySpeed is a typing speed test application that allows users to test their typing speed and accuracy.

## Features

- Typing speed and accuracy test
- User authentication (registration, login, logout)
- Profile management
- Leaderboard to track top scores

## Installation

1. Clone the repository:
    ```
    git clone <repository-url>
    cd keyspeed
    ```

2. Set up a virtual environment:
    ```
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Run database migrations:
    ```
    python manage.py migrate
    ```

5. Run the development server:
    ```
    python manage.py runserver
    ```

## Usage

- Navigate to `http://127.0.0.1:8000/` to access the home page.
- Register or log in to take a typing test.
- View and edit your profile information.

## API Documentation

- **Endpoint:** `/api/v1/UserProfile/`
- Provides CRUD operations for UserProfiles.

## Contributing

Feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributors

See the [CONTRIBUTORS](CONTRIBUTORS) file for the list of contributors to this project.
