import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from typing import List

@strawberry.type
class User:
  name: str
  age: int

@strawberry.type
class Book:
  title: str
  author: str

def get_books() -> List[Book]:
  return [
    Book(
      title='The Great Gatsby',
      author='F. Scott Fitzgerald',
    ),
  ]

@strawberry.input
class AddBookInput:
  title: str
  author: str
  
@strawberry.type
class Query:
  @strawberry.field
  def user(self) -> User:
    return User(name="nakamura", age=33)
  books: List[Book] = strawberry.field(resolver=get_books)

@strawberry.type
class Mutation:
  @strawberry.field
  def add_book(self, book: AddBookInput) -> Book:
    return Book(title=book.title, author=book.author)  
  
schema = strawberry.Schema(query=Query,mutation=Mutation)
graphql_app = GraphQL(schema)

app = FastAPI()
app.add_route("/graphql", graphql_app)