import yaml
from sqlalchemy import create_engine
import pandas as pd
import os

class AirportRepository:
    def __init__(self, config_path=None):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_path = config_path or os.path.join(base_dir, "configs", "config.yaml")
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)
        self.engine = create_engine(config["database"]["url"])

    def insert_airports(self, data):
        """Insert airport data into the database."""
        data.to_sql("airports", self.engine, if_exists="replace", index=False)

    def get_airports(self):
        """Retrieve all airport data from the database."""
        return pd.read_sql("SELECT * FROM airports", self.engine)
