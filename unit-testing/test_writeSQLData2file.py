from unittest import TestCase
import writeSQLData2file
import os

# simulate OK case for writing data to a file
class Test_write_to_file ( TestCase ):
    def test_write_to_file(self):
        try:
            fileName = "test.txt"
            writeSQLData2file.write_to_file ("Mary had a little lamb.", fileName)
            f = open(fileName, "r")
            f.seek(0)
            contents = f.read()
            print(contents)
            f.close()
        finally:
            # remove file created
            os.remove ( "test.txt" )

        self.assertEqual(contents, "Mary had a little lamb.\n")
