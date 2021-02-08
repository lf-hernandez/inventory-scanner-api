from fastapi import FastAPI
from graphene import Schema
from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.graphql import GraphQLApp

from schema import schema, Query

app = FastAPI()


app.add_route("/graphql", GraphQLApp(
    schema=Schema(query=Query),
    executor_class=AsyncioExecutor)
    )
