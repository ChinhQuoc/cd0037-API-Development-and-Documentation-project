import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

from flaskr import create_app
from models import setup_db, Question, Category
from settings import DB_NAME_TEST, DB_USER, DB_PASSWORD

class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.database_name = DB_NAME_TEST
        self.database_user = DB_USER
        self.database_password = DB_PASSWORD
        self.database_path = "postgresql://{}:{}@{}/{}".format(self.database_user, self.database_password, 'localhost:5432', self.database_name)
        
        self.app = create_app({
            "SQLALCHEMY_DATABASE_URI": self.database_path
        })

        self.client = self.app.test_client

    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_pagination_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["categories"])
        self.assertTrue(data["total_categories"])

    def test_error_404_when_get_pagination_categories(self):
        res = self.client().get('/categories?page=100')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"], 404)
        self.assertTrue(data["message"])

    def test_get_pagination_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["questions"])
        self.assertTrue(data["total_questions"])
        self.assertTrue(data["categories"])

    def test_error_404_when_get_pagination_questions(self):
        res = self.client().get('/questions?page=100')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"], 404)
        self.assertTrue(data["message"])

    def test_delete_question(self):
        res = self.client().delete('/questions/47')
        data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data["success"], True)
    #     self.assertEqual(data["message"], 'deleted successfully')

    def test_error_404_when_delete_question(self):
        res = self.client().delete('/questions/100')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"], 404)
        self.assertTrue(data["message"])

    def test_create_question(self):
        res = self.client().post('/questions', json = {
            'question': 'what is the capital of New York?',
            'answer': 'Albany',
            'difficulty': 1,
            'category': '3'
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["message"], 'Create successfully!')

    def test_error_422_when_create_question(self):
        res = self.client().post('/questions', json = {
            'question': 'what is the capital of New York?',
            'answer': 'Albany',
            'difficulty': 1,
            'category': '100'
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"], 422)
        self.assertTrue(data["message"])


    def test_search_questions(self):
        res = self.client().post('/questions/search', json = {
            'searchTerm': 'title'
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["questions"])
        self.assertTrue(data["total_questions"])

    def test_get_all_question(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["questions"])
        self.assertTrue(data["total_questions"])
        self.assertTrue(data["currentCategory"])

    def test_error_404_when_get_all_question(self):
        res = self.client().get('/categories/100/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"], 404)
        self.assertTrue(data["message"])

    def test_get_question_to_play(self):
        res = self.client().post('/quizzes', json = {
            "previous_questions": [5],
            "quiz_category": {"type": "click", "id": 0}
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["question"])
    
    def test_404_when_get_question_to_play(self):
        res = self.client().post('/quizzes', json = {
            "previous_questions": [],
            "quiz_category": {"type": '', "id": 100}
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"], 404)
        self.assertTrue(data["message"])

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()