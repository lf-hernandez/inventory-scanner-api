from fastapi import FastAPI
from graphene import ObjectType, List, Schema
from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.graphql import GraphQLApp

from db_conf import init_db
from schemas import Product

app = FastAPI()
db = init_db()

class Query(ObjectType):
    get_products = List(Product)

    async def resolve_get_products(self, info):
        products = db.collection(u'products').stream()
        return products


app.add_route("/graphql", GraphQLApp(
    schema=Schema(query=Query),
    executor_class=AsyncioExecutor)
    )
