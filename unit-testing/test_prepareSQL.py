from unittest import TestCase
import prepareSQL

# simulate OK case for forming static SQL query
class Test_staticQuery ( TestCase ):
    def test_static_query(self):
        querytext = "INSERT INTO Users(id,str_col)\nVALUES "
        mycolumns = ["id", "str_col"]
        self.assertEqual (prepareSQL.staticQuery(mycolumns), querytext)