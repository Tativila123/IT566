"""Define the MySQLPersistenceWrapper class."""

from mysql.connector.pooling import MySQLConnectionPool


class MySQLPersistenceWrapper:
    """Create a MySQL connection pool from the application configuration."""

    def __init__(self, config: dict) -> None:
        self._db_config = config["db"]

        self._db_pool = MySQLConnectionPool(
            pool_name=self._db_config["pool"]["pool_name"],
            pool_size=self._db_config["pool"]["pool_size"],
            pool_reset_session=self._db_config["pool"]["pool_reset_session"],
            connection_timeout=self._db_config["pool"]["connection_timeout"],
            autocommit=self._db_config["pool"]["autocommit"],
            host=self._db_config["connection"]["host"],
            port=self._db_config["connection"]["port"],
            database=self._db_config["connection"]["database"],
            user=self._db_config["connection"]["user"],
            password=self._db_config["connection"]["password"],
        )