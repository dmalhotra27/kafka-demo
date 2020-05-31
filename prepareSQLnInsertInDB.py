import prepareSQL
import writeSQLData2file
import executeSQL

# function to form SQL query based on column list & values list
# writes SQL query generated into file "insert-queries.sql"
# executes SQL query into POSTGRES DB
def form_exec_POSTGRES_query(mycolumns, myvalues):
    print("Inside exec query function")
    sql_query = prepareSQL.staticQuery(mycolumns)
    sql_query += "(" + ','.join(myvalues) + "),\n"
    # remove last comma and end statement with a semicolon
    sql_query = sql_query[:-2] + ";"
    print("\nSQL String:{}".format(sql_query))
    # log SQL query into file
    writeSQLData2file.write_to_file(sql_query, "insert-queries.sql")
    # execute SQL query generated above into postgres DB
    executeSQL.exec_sql(sql_query)