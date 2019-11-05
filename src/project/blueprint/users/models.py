from sqlalchemy import Column, String, Index, Integer, Boolean
from sqlalchemy.dialects.postgresql import JSON
from project.db import db


class User(db.Model):
    __tablename__ = "users"
    __table_args__ = {"schema": "example"}

    id = db.Column(Integer, primary_key=True)
    username = db.Column(String)
    is_admin = db.Column(Boolean)
    data = db.Column(JSON)

    def __init__(self, username, data):
        self.username = username
        self.is_admin = False
        self.data = data

    def update(self, is_admin):
        self.is_admin = is_admin

