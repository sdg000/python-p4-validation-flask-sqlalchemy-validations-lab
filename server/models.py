from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'

    # validation to check all Author Instances have name
    @validates('name')
    def validate_name(self, key, author):
        if not author:
            raise ValueError("Author must have name")
        return author
    
    # validation to check all Author Phone Number is 10 Digits
    @validates('phone_number')
    def validate_phone_number(self, key, author):

        if not author or len(author) != 10:
            raise ValueError("Phone number must be 10 Digits")
        return author


    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'

    # validation to check that every Post Instance has a 'title'
    @validates('title')
    def validate_title(self, key, post):
        if not post:
            raise ValueError("requires each post to have a title")
        return post


    # validation to check if 'content' is not too short
    @validates('content')
    def validate_content(self, key, post):
        if not post or len(post) < 250:
            raise ValueError("Content too short test. Less than 250 chars.")
        return post
    
        # validation to check if 'summary' is not too long
    @validates('summary')
    def validate_summary(self, key, summary):
        if len(summary) > 250:
            raise ValueError("Summary too long test. More than 250 chars.")
        return summary
    
    @validates('category')
    def validate_category(self, key, category):
        if category not in ['Fiction', 'Non-Fiction']:
            raise ValueError("Incorrect category")
        return category

    @validates('title')
    def validate_title(self, key, title):
        if title not in ["Wont't Believe", "Secret", "Top", "Guess"]:
            raise ValueError("Incorrect title")
        return title



    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
