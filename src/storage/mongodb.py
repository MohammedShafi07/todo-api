
import motor.motor_asyncio
from src import config
from src.logger import logger

logger = logger.init(__name__)

DB_CLIENT: motor.motor_asyncio.AsyncIOMotorClient  # global variable to store db client and used across the application

db = config.DBConfig()
db_user = db.user
db_pass = db.password
db_name = db.name
db_url = db.dbURL


async def connect():
    """Create database connection."""
    logger.info("connecting to database...")

    global DB_CLIENT
    db_path = get_db_path()
    DB_CLIENT = motor.motor_asyncio.AsyncIOMotorClient(db_path)


async def close():
    """Close database connection."""
    logger.info("disconnecting database...")
    DB_CLIENT.close()


def get_db():
    """get database instance"""
    return DB_CLIENT[db_name]


def get_db_path():
    """
    Load DB path according to environment
    :return: str
    """

    if config.Env() == "prod":
        db_path = (
                "mongodb+srv://"
                + db_user
                + ":"
                + db_pass
                + "@" + db_url + "/"
                + db_name
                + "?retryWrites=true&w=majority"
        )
    elif config.Env() == "stg":
        db_path = (
                "mongodb+srv://"
                + db_user
                + ":"
                + db_pass
                + "@" + db_url + "/"
                + db_name
                + "?retryWrites=true&w=majority"
        )
    else:
        db_path = "mongodb://localhost:27017/" + db_name

    return db_path
