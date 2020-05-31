from unittest import TestCase
import kafka.producer
import kafka.consumer
from kafka.producer import kafka
import kafkaConfig


class Test_connectKafka ( TestCase ):

    # simulate NOK via wrong bootstrap_servers provided
    def test_conn_to_kafka_broker_NOK(self):
        bootstrap_servers = "kafka-demo:5859"
        security_protocol = kafkaConfig.Security_protocol
        ssl_cafile = kafkaConfig.Ssl_cafile
        ssl_certfile = kafkaConfig.Ssl_certfile
        ssl_keyfile = kafkaConfig.Ssl_keyfile

        self.assertEqual ( kafkaConfig.conn_to_kafkaBroker ( bootstrap_servers ,
                                                 security_protocol ,
                                                 ssl_cafile ,
                                                 ssl_certfile ,
                                                 ssl_keyfile ) , None )

    #simulate NOK via wrong filename provided
    def test_conn_to_kafka_broker_NOK_2(self):
        bootstrap_servers = kafkaConfig.Bootstrap_servers
        security_protocol = kafkaConfig.Security_protocol
        ssl_cafile = "caa.pem"
        ssl_certfile = kafkaConfig.Ssl_certfile
        ssl_keyfile = kafkaConfig.Ssl_keyfile

        self.assertEqual ( kafkaConfig.conn_to_kafkaBroker ( bootstrap_servers ,
                                                 security_protocol ,
                                                 ssl_cafile ,
                                                 ssl_certfile ,
                                                 ssl_keyfile ) , None )

    # simulalte ok case for producer connection with kafka
    def test_conn_to_kafka_broker_OK(self):
        bootstrap_servers = kafkaConfig.Bootstrap_servers
        security_protocol = kafkaConfig.Security_protocol
        ssl_cafile = kafkaConfig.Ssl_cafile
        ssl_certfile = kafkaConfig.Ssl_certfile
        ssl_keyfile = kafkaConfig.Ssl_keyfile

        self.assertNotEqual(kafkaConfig.conn_to_kafkaBroker(bootstrap_servers,
                                                    security_protocol,
                                                    ssl_cafile,
                                                    ssl_certfile,
                                                    ssl_keyfile), None)


class Test_connect_broker (TestCase):

    # simulate ok case for connection of consumer with kafka
    def test_connect_broker_OK(self):
        bootstrap_servers = kafkaConfig.Bootstrap_servers
        security_protocol = kafkaConfig.Security_protocol
        ssl_cafile = kafkaConfig.Ssl_cafile
        ssl_certfile = kafkaConfig.Ssl_certfile
        ssl_keyfile = kafkaConfig.Ssl_keyfile
        topic = kafkaConfig.topic
        auto_offset_reset = kafkaConfig.auto_offset_reset
        client_id = kafkaConfig.client_id
        group_id = kafkaConfig.group_id

        self.assertNotEqual(kafkaConfig.connect_broker(topic,
                                           auto_offset_reset,
                                           bootstrap_servers,
                                           client_id,
                                           group_id,
                                           security_protocol,
                                           ssl_cafile,
                                           ssl_certfile,
                                           ssl_keyfile), None)

    # simulate NOK case of consumer connection to kafka by providing wrong filename
    def test_connect_broker_NOK(self):
        bootstrap_servers = kafkaConfig.Bootstrap_servers
        security_protocol = kafkaConfig.Security_protocol
        ssl_cafile = "caa.pem"
        ssl_certfile = kafkaConfig.Ssl_certfile
        ssl_keyfile = kafkaConfig.Ssl_keyfile
        topic = kafkaConfig.topic
        auto_offset_reset = kafkaConfig.auto_offset_reset
        client_id = kafkaConfig.client_id
        group_id = kafkaConfig.group_id

        self.assertEqual(kafkaConfig.connect_broker(topic,
                                        auto_offset_reset,
                                        bootstrap_servers,
                                        client_id,
                                        group_id,
                                        security_protocol,
                                        ssl_cafile,
                                        ssl_certfile,
                                        ssl_keyfile), None)