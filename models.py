import strawberry
from typing import List
from sqlmodel import Field, SQLModel, select
from utils import get_db
from strawberry.file_uploads import Upload

__all__ = ["Query", "Mutation"]


class BaseModel(SQLModel):

    @classmethod
    def get_records(cls):
        with get_db() as db:
            return db.execute(select(cls)).scalars().all()

    @classmethod
    def add_record(cls, **kwargs):
        entity = cls(**kwargs)
        with get_db() as db:
            db.add(entity)
            db.commit()
            return entity


@strawberry.type
class User(BaseModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str
    age: int


@strawberry.type
class Scenario(BaseModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    creator_id: int = Field(foreign_key='user.id')


@strawberry.type
class ExecutionParameter(BaseModel, table=True):
    id: int = Field(default=None, primary_key=True)
    numCores: int


# Define all models that can be queried
# Q: can this be achieved dynamically? Metaclasses?
@strawberry.type
class Query:
    users: List[User] = strawberry.field(User.get_records)
    scenarios: List[Scenario] = strawberry.field(Scenario.get_records)
    execution_parameters: List[ExecutionParameter] = strawberry.field(ExecutionParameter.get_records)


# Define all possible methods to add to database
# Can this be defined dynamically? Metaclasses?
@strawberry.type
class Mutation:

    @strawberry.field
    def add_user(self, username: str, age: int) -> User:
        return User.add_record(username=username, age=age)

    @strawberry.field
    def add_scenarios(self, name: str, creator_id: int) -> Scenario:
        return Scenario.add_record(name=name, creator_id=creator_id)

    @strawberry.field
    def add_execution_parameter(self, numCores: int) -> ExecutionParameter:
        return ExecutionParameter.add_record(numCores=numCores)
