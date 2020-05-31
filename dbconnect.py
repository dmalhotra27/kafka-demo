import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2 import connect, Error
import postgres_dbconfig

# function to establish connection with POSTGRES DB and to return connection details
def conn_db(DB = postgres_dbconfig.dbname,
            User = postgres_dbconfig.user,
            Host = postgres_dbconfig.host,
            Pwd = postgres_dbconfig.password,
            Port = postgres_dbconfig.port):
    try:
        # declare a new PostgreSQL connection object
        db_conn = connect(
            dbname=DB,
            user=User,
            host=Host,
            password=Pwd,
            port=Port
            # attempt to connect for 10 seconds then raise exception
            # connect_timeout = 10
        )
        c = db_conn.cursor(cursor_factory=RealDictCursor)
        return db_conn, c
    except (Exception, Error) as err:
        print("\n psycopg2 connect error:", err)
        db_conn = None
        c = None
        return db_conn, c

