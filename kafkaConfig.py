# configuration parameters
from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError
from json import loads

# default configuration parameters needed for producer and consumer to connect to kafka
Bootstrap_servers = "<insert service URI>"
Security_protocol = "SSL"
Ssl_cafile = "ca.pem"
Ssl_certfile = "service.cert"
Ssl_keyfile = "service.key"

topic = "Users"
auto_offset_reset = "earliest"
client_id = "demo-client-1"
group_id = "None"

producer = None
consumer = None

# function for producer to connect to Kafka broker
def conn_to_kafkaBroker(bservers = Bootstrap_servers,
                        sprot = Security_protocol,
                        sslCA = Ssl_cafile,
                        sslCert = Ssl_certfile,
                        sslKey = Ssl_keyfile):
    try:
        producer = KafkaProducer(
            bootstrap_servers=bservers,
            security_protocol=sprot,
            ssl_cafile=sslCA,
            ssl_certfile=sslCert,
            ssl_keyfile=sslKey,

        )
    except KafkaError as error:
        print("Kafka Error, Exception caught: {}".format(str(error)))
        producer =None
    except (KafkaError, FileNotFoundError) as error:
        print("Kafka Error, File Not Found Exception caught: {}".format(str(error)))
        producer =None
    except (KafkaError, TimeoutError) as error:
        print("Unable to connect to Kafka server!:{}".format(str(error)))
        producer =None
    finally:
        return producer

# function for consumer to establish connection with kafka
def connect_broker(Topic = topic,
                   offset_reset = auto_offset_reset,
                   bservers = Bootstrap_servers,
                   Clientid = client_id,
                   Groupid = group_id,
                   sprot = Security_protocol,
                   sslCA = Ssl_cafile,
                   sslCert = Ssl_certfile,
                   sslKey = Ssl_keyfile,
                   ):
    try:
        consumer = KafkaConsumer(
            Topic,
            auto_offset_reset = offset_reset,
            bootstrap_servers = bservers,
            client_id = Clientid,
            group_id = Groupid,
            security_protocol = sprot,
            ssl_cafile = sslCA,
            ssl_certfile = sslCert,
            ssl_keyfile = sslKey,
            enable_auto_commit=True,
            value_deserializer=lambda x: loads(x.decode('utf-8'))
        )
        print("connected!!\n")
    except KafkaError as error:
        print("Kafka Error, Exception caught: {}".format(str(error)))
        consumer = None
    except (KafkaError, FileNotFoundError) as e:
        print("Kafka Error, File Not Found Exception caught: {}".format(str(e)))
        consumer = None
    finally:
        return consumer

