# Backend - Trivia API

## Setting up the Backend

### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

With Postgres running, create a `trivia` database:

```bash
createdb trivia
```

Populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql trivia < trivia.psql
```

### Run the Server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## To Do Tasks

These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_flaskr.py`

One note before you delve into your tasks: for each endpoint, you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior.

1. Use Flask-CORS to enable cross-domain requests and set response headers.
2. Create an endpoint to handle `GET` requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories.
3. Create an endpoint to handle `GET` requests for all available categories.
4. Create an endpoint to `DELETE` a question using a question `ID`.
5. Create an endpoint to `POST` a new question, which will require the question and answer text, category, and difficulty score.
6. Create a `POST` endpoint to get questions based on category.
7. Create a `POST` endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.
8. Create a `POST` endpoint to get questions to play the quiz. This endpoint should take a category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.
9. Create error handlers for all expected errors including 400, 404, 422, and 500.

## Documenting your Endpoints

`GET '/categories'`

- Fetches a paginated list of categories, with each category represented by its `id` and `type`.
- Request Arguments:
  - `page` (optional): An integer representing the page number (default is 1).
- Returns: An object with the following keys:
  - `success`: A boolean indicating the request status.
  - `categories`: A list of category objects, each containing `id` and `type`.
  - `total_categories`: An integer representing the total number of categories available.

```json
{
  "categories": [
    {
      "id": 1,
      "type": "Science"
    },
    {
      "id": 2,
      "type": "Art"
    },
    {
      "id": 3,
      "type": "Geography"
    },
    {
      "id": 4,
      "type": "History"
    },
    {
      "id": 5,
      "type": "Entertainment"
    },
    {
      "id": 6,
      "type": "Sports"
    }
  ],
  "success": true,
  "total_categories": 6
}
```

`GET '/questions'`

- Fetches a paginated list of questions along with all available categories.
- Request Arguments:
  - `page` (optional): An integer representing the page number (default is 1).
- Returns: An object with the following keys:
  - `success`: A boolean indicating the request status.
  - `questions`: A list of question objects, each containing `id`, `question`, `answer`, `category`, and `difficulty`.
  - `total_questions`: An integer representing the total number of questions available.
  - `categories`: A list of category objects, each containing `id` and `type`.

```json
{
  "categories": [
    {
      "id": 1,
      "type": "Science"
    },
    {
      "id": 2,
      "type": "Art"
    },
    {
      "id": 3,
      "type": "Geography"
    },
    {
      "id": 4,
      "type": "History"
    },
    {
      "id": 5,
      "type": "Entertainment"
    },
    {
      "id": 6,
      "type": "Sports"
    }
  ],
  "questions": [
    {
      "answer": "testing",
      "category": 6,
      "difficulty": 4,
      "id": 26,
      "question": "how to play football"
    },
    {
      "answer": "home",
      "category": 4,
      "difficulty": 3,
      "id": 29,
      "question": "Where are you?"
    },
    {
      "answer": "Hi",
      "category": 3,
      "difficulty": 1,
      "id": 32,
      "question": "Hello there"
    },
    {
      "answer": "Albany",
      "category": 3,
      "difficulty": 1,
      "id": 33,
      "question": "what is the capital of new york?"
    },
    {
      "answer": "Albany",
      "category": 3,
      "difficulty": 1,
      "id": 37,
      "question": "what is the capital of new york?"
    },
    {
      "answer": "Albany",
      "category": 3,
      "difficulty": 1,
      "id": 39,
      "question": "what is the capital of new york?"
    },
    {
      "answer": "Albany",
      "category": 3,
      "difficulty": 1,
      "id": 41,
      "question": "what is the capital of new york?"
    },
    {
      "answer": "Albany",
      "category": 3,
      "difficulty": 1,
      "id": 43,
      "question": "what is the capital of new york?"
    },
    {
      "answer": "Albany",
      "category": 3,
      "difficulty": 1,
      "id": 45,
      "question": "what is the capital of new york?"
    },
    {
      "answer": "Albany",
      "category": 3,
      "difficulty": 1,
      "id": 47,
      "question": "what is the capital of new york?"
    }
  ],
  "success": true,
  "total_questions": 31
}
```

`DELETE '/questions/<int:id>'`

- Deletes a specific question identified by its unique id.
- URL Parameters:
  - `id`: An integer representing the unique identifier of the question to be deleted.
- Returns: An object with the following keys:
  - `success`: A boolean indicating the request status.
  - `message`: A confirmation message indicating that the question was deleted successfully.
- Possible Responses:
  - Returns a `404` status if the question with the specified `id` does not exist.
  - Returns a `422` status if the deletion fails due to a database constraint or error.

```json
{ "message": "deleted successfully", "success": true }
```

`POST '/questions'`

- Creates a new question with the specified details.
- Request Body: A JSON object containing:
  - `question`: A string representing the text of the question.
  - `answer`: A string representing the correct answer to the question.
  - `difficulty`: An integer representing the difficulty level (1 to 5).
  - `category`: An integer representing the ID of the category to which the question belongs.
- Returns: An object with the following keys:
  - `success`: A boolean indicating the request status.
  - `message`: A confirmation message indicating that the question was created successfully.
- Possible Responses:

  - Returns a `422` status if the creation fails due to invalid input or database constraints.

- Body

```json
{
  "question": "what is the capital of New York?",
  "answer": "Albany",
  "difficulty": 1,
  "category": "2"
}
```

- Response

```json
{
  "message": "Create successfully!",
  "success": true
}
```

`POST '/questions/search'`

- Searches for questions containing a specified search term and returns a paginated list of results.
- Request Body: A JSON object containing:
  - `searchTerm`: A string representing the keyword to search for in the questions.
- Request Arguments:
  - `page` (optional): An integer representing the page number (default is 1).
- Returns: An object with the following keys:
  - `success`: A boolean indicating the request status.
  - `questions`: A list of question objects matching the search term, each containing `id`, `question`, `answer`, `category`, and `difficulty`.
  - `total_questions`: An integer representing the total number of questions that matched the search term.
- Possible Responses:

  - Returns an empty list for `questions` if no matches are found, along with `total_questions` equal to 0.

- Body

```json
{
  "searchTerm": "movie"
}
```

- Response

```json
{
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }
  ],
  "success": true,
  "total_questions": 1
}
```

`GET '/categories/<int:id>/questions'`

- Retrieves a paginated list of questions associated with a specific category.
- URL Parameters:
  - `id`: An integer representing the unique identifier of the category.
- Request Arguments:
  - `page` (optional): An integer representing the page number (default is 1).
- Returns: An object with the following keys:
  - `success`: A boolean indicating the request status.
  - `questions`: A list of question objects associated with the specified category, each containing `id`, `question`, `answer`, `category`, and `difficulty`.
  - `total_questions`: An integer representing the total number of questions available in the specified category.
  - `currentCategory`: An object representing the current category, containing its `id` and `type`.
- Possible Responses:
  - Returns a `404` status if the specified category does not exist.

```json
{
  "currentCategory": {
    "id": 2,
    "type": "Art"
  },
  "questions": [
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    },
    {
      "answer": "abc",
      "category": 2,
      "difficulty": 1,
      "id": 53,
      "question": "How are you?"
    }
  ],
  "success": true,
  "total_questions": 5
}
```

`POST '/quizzes'`

- Retrieves a question for a quiz based on the specified category and previously answered questions.
- Request Body: A JSON object containing:
  - `previous_questions`: A list of integers representing the IDs of previously answered questions.
  - `quiz_category`: An object containing:
    - `type`: A string representing the category name.
    - `id`: An integer representing the ID of the category (use `0` to select from all `categories`).
- Returns: An object with the following keys:
  - `success`: A boolean indicating the request status.
  - `question`: An object representing the selected question, containing `id`, `question`, `answer`, `category`, and `difficulty`.
- Possible Responses:

  - Returns a `404` status if no questions are found for the specified category or if the category does not exist.

- Body

```json
{
  "previous_questions": [2],
  "quiz_category": { "type": "Entertainment", "id": 5 }
}
```

- Response

```json
{
  "question": {
    "answer": "Tom Cruise",
    "category": 5,
    "difficulty": 4,
    "id": 4,
    "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
  },
  "success": true
}
```

## Testing

Write at least one test for the success and at least one error behavior of each endpoint using the unittest library.

To deploy the tests, run

```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
