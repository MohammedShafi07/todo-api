
import yaml

PROJECT_NAME = "Todo API Engine"


class Config:
    CONFIG_FILE = "config.yaml"
    config_data: dict
    env: str
    database: dict
    cors: dict

    def __init__(self):
        """
        Load all config data
        """
        self.config_data = self.load()
        self.env = self.config_data["env"]
        self.database = self.config_data["database"]
        self.cors = self.config_data["cors"]

    def load(self):
        """Load environment configuration from config.yaml"""
        with open(self.CONFIG_FILE, "r") as config_file:
            data = yaml.load(config_file, Loader=yaml.FullLoader)
        return data


class Env:
    """get environment name"""

    def __new__(cls):
        return Config().env


class DBConfig:
    dbURL: str
    name: str
    user: str
    password: str

    def __init__(self):
        """
        Load database configuration
        """
        db_config = Config().database
        self.name = db_config["name"]
        self.user = db_config["user"]
        self.password = db_config["password"]
        self.dbURL = db_config["url"]


class Cors:
    origins: []
    methods: []
    headers: []

    def __init__(self):
        """
        Load CORS configuration
        """
        cors_config = Config().cors
        self.origins = cors_config["origins"]
        self.methods = cors_config["methods"]
        self.headers = cors_config["headers"]

