from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def submit_survey(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment, created_at, updated_at) VALUE (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"
        results = connectToMySQL('dojo_survey_schema').query_db(query, data)
        print(results)
        return results
    @classmethod
    def get_survey(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL('dojo_survey_schema').query_db(query, data)
        return cls(results[0])
    @staticmethod
    def validate_survey(name, location, language, comment):
        is_valid = True
        if len(name) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if location == "none":
            flash("Must select a location.")
            is_valid = False
        if language == "none":
            flash("Must select a favorite language.")
            is_valid = False
        if len(comment) < 3:
            flash("Comment must be at least 3 characters.")
            is_valid = False
        return is_valid
