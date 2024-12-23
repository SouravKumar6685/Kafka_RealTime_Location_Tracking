from confluent_kafka import Producer
import json
import os
import time

conf = {
	'bootstrap.servers': 'localhost:9092'
	}

producer = Producer(**conf)

start_latitude = 17.544300
start_longitude = 78.433670
end_latitude = 18.5204
end_longitude = 73.8567
no_of_steps = 10000

step_size_lat = (end_latitude - start_latitude ) / no_of_steps
step_size_long = (end_longitude - start_longitude) / no_of_steps
current_steps = 0

topic = "location_updates"
def delivery_report(err,msg):
	if err is not None:
		print(f"Message delivery failed: {err}")
	else:
		print(f"Message delivered to {msg.topic()} [{msg.partition()}]")


 
while True:
	latitude = start_latitude + step_size_lat*current_steps
	longitude = start_longitude + step_size_long*current_steps
	
	data = {
		"latitude" : latitude,
		"longitude" : longitude,
	}
	print(data)
	
	producer.produce(topic, json.dumps(data).encode('utf-8'), callback = delivery_report)
	
	producer.flush()
	current_steps += 1
	if current_steps > no_of_steps:
		current_steps = 0
	
	time.sleep(2)
