# prepare SQL for below schema 'Users' into POSTGRES DB
# CREATE TABLE Users (
# id UUID PRIMARY KEY,
# str_col VARCHAR(500),
# int_col SMALLINT,
# bool_col BOOLEAN,
# float_col DECIMAL
# );

# function to create static SQL query for schema/topic Users based on column list received
def staticQuery(mycolumns):
    table_name = "Users"
    sql_string = "INSERT INTO {}".format(table_name)
    sql_string += "(" + ','.join(mycolumns) + ")\nVALUES "
    return sql_string

