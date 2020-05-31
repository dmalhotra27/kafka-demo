# Project Title

A short project on Apache Kafka developed in python using python-kafka library. The project includes the following  key compoenents:

1. Producer -> Producing data in Json format 
2. Kafka Broker -> Aiven Kafka to receive data produced by producer and store till it's consumed by consumer
3. Consumer -> Consuming data sent by kafka broker for the topic subscribed. It also writes data to postgres DB based on predefined schema (Json format file as mentioned in step 1)
4. PostGres DB -> An entity to store data sent by consumer


## Getting Started

Register to Aiven at https://console.aiven.io/signup.html and download your account specific 'ca.pem', 'service.cert' & 'service.key' file along with service uri link.

Add new services -> Kafka and PostGres

Links for reference:
https://help.aiven.io/en/articles/489572-getting-started-with-aiven-kafka
https://help.aiven.io/en/articles/489573-getting-started-with-aiven-postgresql

These instructions will get basic service up and running on Aiven which can be integrated with the project

### Prerequisites

This project is based on the following:
i) python 3.7.4 (Any Python IDE example PyCharm)
ii) kafka-python (latest version)

Install below dependencies 
 
 i) pip install pymongo
 ii) python -m pip install psycopg2
 iii) pip install kafka-python //ensure it is compatible with python version 3.7.4 (producer and consumer to be used from kafka-python module)

### Installing

1) Create topic "Users" in AIVEN  Kafka

Reference Link: https://help.aiven.io/en/articles/489572-getting-started-with-aiven-kafka


2) Create below table in POSTGRES db:

Below is schema for table Users (aligned with data which Topic "Users" would contain)

CREATE TABLE Users (
    id UUID PRIMARY KEY,
    str_col VARCHAR(500),
    int_col SMALLINT,
    bool_col BOOLEAN,
     float_col DECIMAL
 		);
 
3) Ensure dependencies mentioned in prerequisites are installed
 
4) Sample Input data (Data transfer from producer to consumer) to be stored in below JSON file inside repository 'kafka-demo'
   input_data.json

5) Download and store the following files in repository 'Kafka-Demo'
	ca.pem
	service.cert
	service.key

6) Update following parameters in 'KafkaConfig.py' file stored in the 'Kafka-demo' repository with your generated credetials above (as mentioned in Getting Started Section)
	Bootstrap_servers = "<Service URI Link>"
	Security_protocol = "SSL"
	Ssl_cafile = "<ca.pem>"
	Ssl_certfile = "<service.cert>"
	Ssl_keyfile = "<service.key>"
	
7) Update following paramters in 'postgres-dbconfig.py' file stored in the 'kafka-demo' repository with your generated DB credentials (as mentioned in Getting Started Section)
    dbname = "<Database Name>"
	user = "<user name>"   // by default avnadmin used
	host = "<host name>"
	password = "<generated password>"
	port = "<generated port>"
	
	

## Running the tests

Run following processes:
i) python producer.py
ii) python consumer.py

For unit testing:
i) python -m unittest

Above command will run all unit testcases in the 'kafka-demo' repository. Ensure sample input json file along with credential files are stored in unit testing folder inside repository 'kafka-demo'.

Link for reference:
 https://docs.python.org/3/library/unittest.html

** Please note that for all ok connection testcases to pass, do below:
i) kafkaConfig.py
  insert your service URI
  
ii) postgres-dbconfig.py
   insert your host, password & port

** For security reasons, above have been removed.

Additional Links:
https://towardsdatascience.com/getting-started-with-apache-kafka-in-python-604b3250aa05
