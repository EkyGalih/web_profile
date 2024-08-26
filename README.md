# Website Profile

This project is a personal website profile built using Python and the Flask web framework. The website serves as a digital portfolio where users can showcase their personal information, skills, projects, and other relevant details.

## Features

- **Home Page:** An introduction to the user, including a brief bio and profile picture.
- **About Me:** A detailed section about the user's background, skills, and interests.
- **Projects:** A showcase of the user's projects, including descriptions, technologies used, and links to live demos or GitHub repositories.
- **Contact:** A contact form allowing visitors to send messages directly through the website.

## Technologies Used

- **Python:** The core programming language used to build the backend of the website.
- **Flask:** A lightweight web framework for Python that handles routing, templating, and other web functionalities.
- **HTML5 & CSS3:** For structuring and styling the website.
- **Bootstrap:** A popular CSS framework used to make the website responsive and visually appealing.
- **SQLite:** A lightweight database used for storing user information and project details.

## Installation

To set up this project locally, follow the steps below:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/website-profile.git
    cd website-profile
    ```

2. **Create a virtual environment:**

    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the environment variables:**

    Create a `.env` file in the root directory and add the following environment variables:

    ```env
    FLASK_APP=server.py
    FLASK_ENV=development
    DB_HOST=localhost:3306
    DB_DATABASE=web_profile
    DB_USERNAME=root
    DB_PASSWORD=yourpassword
    ```

5. **Initialize the database:**

    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

6. **Run the application:**

    ```bash
    flask run --debug
    ```

    The website should now be running at `http://127.0.0.1:5000/`.

## Usage

Visit the website in your browser, navigate through the different sections, and explore the content. You can customize the content by editing the template files in the `templates/` directory and the static assets in the `static/` directory.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
