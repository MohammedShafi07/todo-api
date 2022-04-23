import pymongo
from bson import ObjectId
from pydantic import BaseModel, Field

import src.storage.mongodb as database
from src.common.mongo import PyObjectId


class Collection:
    COLLECTION_NAME = "todo"
    collection: pymongo.collection.Collection

    def __init__(self):
        self.collection = database.get_db().get_collection(self.COLLECTION_NAME)


class TodoModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    message: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
