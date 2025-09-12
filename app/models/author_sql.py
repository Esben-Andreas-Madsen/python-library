from app.extentions import db

class AuthorSQL(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    birth_year = db.Column(db.Integer)
