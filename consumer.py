# This script receives messages from a kafka topic

from kafka import KafkaConsumer
from kafka.errors import KafkaError

import prepareSQLnInsertInDB
import kafkaConfig

# function to process messages received from kafka
def processMessages():
    # establishing connection with kafka broker
    consumer = kafkaConfig.connect_broker()

    while True:
        raw_msgs = None

        for _ in range(2):
            try:
                # consumer polling for messages
                raw_msgs = consumer.poll(timeout_ms=1000)
            except ValueError as err:
                print(type(raw_msgs))
                print('Exception: Decoding JSON messages:{}'.format(str(err)))
                print("Raw_msgs is None, continuing")

            else:
                for tp, msgs in raw_msgs.items():
                    for msg in msgs:
                        # type consumer record, so fetching value from it
                        print("Received: {}".format(msg.value))
                        record_dict = msg.value

                        values = []
                        columns = []
                        # enumerate over the record
                        for col_names, val in record_dict.items():
                            # Postgres strings must be enclosed with single quotes
                            if type(val) == str:
                                # escape apostrophies with two single quotations
                                val = val.replace("'", "''")
                                val = "'" + val + "'"

                            values += [str(val)]
                            columns += [col_names]

                        # function to prepare SQL query and to perform insertion into POSTGRES DB
                        prepareSQLnInsertInDB.form_exec_POSTGRES_query(columns, values)


processMessages()









