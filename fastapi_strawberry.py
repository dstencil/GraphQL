
import strawberry
import typing
from fastapi import FastAPI
from strawberry.asgi import GraphQL
@strawberry.type
class Book:
    title: str
    author: str
   
@strawberry.type
class Query:
    books: typing.List[Book]
    
def get_books():
    return [
        Book(
            title='The Great Gatsby',
            author='F.Scott Fitzgerald',
        ),
    ]
    
@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books)

schema = strawberry.Schema(query=Query)
graphql_app = GraphQL(schema)
app = FastAPI()
app.add_route("/graphql", graphql_app)
app.add_websocket_route('/graphql', graphql_app)
