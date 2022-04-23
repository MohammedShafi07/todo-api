from fastapi.encoders import jsonable_encoder
from pydantic import validate_arguments
from pymongo.errors import PyMongoError

from src.common import mongoerrors
from src.logger import logger
from .model import Collection, TodoModel

logger = logger.init(__name__)


class Repo(Collection):
    def __init__(self):
        Collection.__init__(self)

    @validate_arguments
    async def create(self, data: TodoModel):
        """create to-do task model in database"""
        logger.info("executing create() in todo repo")

        todo = jsonable_encoder(data)
        try:
            new_todo = await self.collection.insert_one(todo)
        except PyMongoError as exp:
            logger.error(exp)
            err = mongoerrors.parse(exp)
            return err
        except Exception as e:
            logger.error(e)
            return e
        if new_todo.inserted_id is None:
            return "todo creation failed"
        return None
