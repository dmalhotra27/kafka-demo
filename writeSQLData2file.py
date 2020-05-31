import sys

# function to write data to specified file, file is created at run time if not existing already
def write_to_file(data, fileName):
    try:
        outputfile = open(fileName, "a+")
        outputfile.write(data)
        outputfile.write("\n")
    except IOError as e:
        print("I/O error({0}): {1}").format(e.errno, e.strerror)
    except: #handle other exceptions such as attribute errors
        print("Unexpected error:{}").format(sys.exc_info()[0])
    else:
        outputfile.close()