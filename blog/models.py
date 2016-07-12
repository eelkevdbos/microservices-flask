from sqlalchemy import Column, Integer, String, Text
from database import Base, db_session
from marshmallow import Schema

class PostSchema(Schema):
    class Meta:
        fields = ('id', 'title', 'content', 'author_id')
        ordered = True

class Post(Base):

    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    content = Column(Text(120))
    author_id = Column(Integer)

    def __init__(self, title = None, content = None, author_id = None):

        self.title = title
        self.content = content
        self.author_id = author_id

    @staticmethod
    def create(data):
        post = Post(data['title'], data['content'], data['user_id'])
        db_session.add(post)
        db_session.commit()

        schema = PostSchema()

        return schema.dumps(post)

    def __repr__(self):
        return '<Post %r>' % (self.title)