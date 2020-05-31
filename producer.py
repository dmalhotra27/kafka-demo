# producer file to send messages to Kafka

import json
from bson import json_util
from psycopg2 import connect, Error

from kafka import KafkaProducer
from kafka.errors import KafkaError
import kafkaConfig

producer = None

# function to print success message on console after producer sends message to broker
def on_send_success(record_metadata):
    print('Sent successfully:', record_metadata.topic, end=',')
    print(record_metadata.partition, end=',')
    print(record_metadata.offset, end='\n')

# function to print error case when producer is not able to send messages to broker
def on_send_error(excp):
    log.error('ERROR BACK:', exc_info=excp)
    # handle exception
    print("Exception caught!!")
    producer = None

# function to send messages to broker for topic "Users", dumps is used to convert dictionary into JSON string format
# which is further converted to bytes
def send(producer, contents):
    for data in contents['User_details']:
        print("Sending: {}".format(data))
        try:
            producer.send("Users", json.dumps(data, default=json_util.default).encode('utf-8')).add_callback(
                on_send_success).add_errback(on_send_error)
            # record_metadata = future.get(timeout=10)
        except KafkaError as e:
            print("Exception during sending messages : {}".format(e))

    # send all messages
    producer.flush()
    producer.close()

# function to read messages from json file and to send it further to broker
def send_json_data(fname = 'input_data.json'):
    try:
        inputfile = open(fname)
    except IOError as e:
        print("I/O error, File Not Found Exception caught: {}".format(str(e)))
    except:  # handle other exceptions such as attribute errors
        print("Unexpected error:{}").format(sys.exc_info()[0])
    else:
        try:
            contents = json.load(inputfile)
        except ValueError:
            print('Exception: Decoding JSON file input_data1.json has failed')
        else:
            producer = kafkaConfig.conn_to_kafkaBroker()
            if producer != None:
                # function to send messages to broker
                send(producer, contents)

        inputfile.close()

# program execution starts from here
send_json_data()