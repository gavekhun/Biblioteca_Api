import os

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")


"""   MYSQL  """
MYSQL_HOST = os.getenv("MYSQL_HOST", default="localhost")
MYSQL_USER = os.getenv("MYSQL_USER", default="root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", default="admin")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", default="biblioteca_db")
MYSQL_PORT = os.getenv("MYSQL_PORT", default=3306)

