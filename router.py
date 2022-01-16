import strawberry
from strawberry.fastapi import GraphQLRouter
from fastapi import APIRouter

import models

router = APIRouter()

query = models.get_query_obj()
schema = strawberry.Schema(query=query, mutation=models.Mutation)

graphql_app = GraphQLRouter(schema)

router.include_router(graphql_app, prefix='/graphql')
