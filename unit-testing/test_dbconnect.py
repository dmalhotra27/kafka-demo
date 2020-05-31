from unittest import TestCase
import dbconnect
import postgres_dbconfig


class Test_conn_db ( TestCase ):

    # simulating NOK case by providing wrong password
    def test_conn_db_NOK(self):
        dbname = postgres_dbconfig.dbname
        user = postgres_dbconfig.user
        host = postgres_dbconfig.host
        password = "abc"
        port = postgres_dbconfig.port
        self.assertEquals ( dbconnect.conn_db(dbname,
                                              user,
                                              host,
                                              password,
                                              port), (None, None) )
    # simulating ok case for db connection
    def test_conn_db_OK(self):
        dbname = postgres_dbconfig.dbname
        user = postgres_dbconfig.user
        host = postgres_dbconfig.host
        password = postgres_dbconfig.password
        port = postgres_dbconfig.port
        self.assertNotEquals(dbconnect.conn_db(dbname,
                                               user,
                                               host,
                                               password,
                                               port), (None, None) )
