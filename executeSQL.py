import dbconnect
from psycopg2 import connect, Error
import writeSQLData2file
import sys
from psycopg2.errors import UniqueViolation

# Function to execute SQL query in POSTGRES DB after establishing connection to DB
# In case of SQL query error, query is not written into DB, rather rolled back
# All SQL query results (ok or nok) are logged into file 'Insertquery-results.txt' for future reference
def exec_sql(sql_query):
    text = ""
    # function to establish connection with PSOTGRES DB
    conn, cur = dbconnect.conn_db()
    if conn != None and cur != None:
        try:
            text += "========================SQL Query Insertion Start=========================\n"
            text += sql_query
            cur.execute(sql_query)
            conn.commit()
            text += "\n==================RESULT: INSERT into table successful====================\n"
            writeSQLData2file.write_to_file(text, "Insertquery-results.txt")
        except UniqueViolation as e:
            error = e.pgcode
            text += "\n======RESULT: Execute sql error:A duplicate record already exists=========\n"
            writeSQLData2file.write_to_file(text, "Insertquery-results.txt")
            conn.rollback()
        except (Exception, Error) as error:
            print("\nExecute sql error:{}".format(error))
            text += "\n================RESULT: Execute sql error:================================\n"
            text += str(error)
            text += "==========================================================================\n"
            writeSQLData2file.write_to_file(text, "Insertquery-results.txt")
            conn.rollback()

        # close the cursor and connection
        cur.close()
        conn.close()