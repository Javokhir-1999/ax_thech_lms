from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.database import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author_id = Column(Integer, ForeignKey('authors.id'))
    language = Column(String)
    publication_date = Column(Date)
    category = Column(String)
    isbn = Column(String, unique=True)

    author = relationship("Author", back_populates="books")
