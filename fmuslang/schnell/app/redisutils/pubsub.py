import redis
import json


cached_connection = {}

def publish_to_redis_channel(message, redis_host='localhost', redis_port=6380, redis_db=0, redis_channel='ipc/0'):
	try:
		# Connect to the Redis server
		connstring = f"redis://{redis_host}:{redis_port}/{redis_db}"
		if not connstring in cached_connection:
			r = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)
			cached_connection[connstring] = r
		else:
			r = cached_connection[connstring]

		# Format the message
		formatted_message = message
		if isinstance(formatted_message, dict):
			formatted_message = json.dumps(message)

		# Publish the message to the specified channel
		r.publish(redis_channel, formatted_message)
		print(f"<<Message published to {redis_channel} channel: {formatted_message[:100]}>>")
	except Exception as e:
		print(f"Error publishing message to Redis channel: {e}")

def subscribe_to_redis_channel(callback, redis_host='localhost', redis_port=6380, redis_db=0, redis_channel='ipc/0'):
	try:
		# Connect to the Redis server
		# r = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)
		connstring = f"redis://{redis_host}:{redis_port}/{redis_db}"
		if not connstring in cached_connection:
			r = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)
			cached_connection[connstring] = r
		else:
			r = cached_connection[connstring]

		# Create a Pub/Sub instance
		pubsub = r.pubsub()

		# Subscribe to the specified channel
		pubsub.subscribe(redis_channel)

		print(f"Subscribed to {redis_channel} channel. Waiting for messages...")

		# Continuously listen for messages
		for message in pubsub.listen():
			if message['type'] == 'message':
				# Decode and parse the message
				decoded_message = message['data']
				if isinstance(decoded_message, dict):
					decoded_message = json.loads(decoded_message)

				if decoded_message in ['quit', 'exit']:
					break

				# Call the callback function with the parsed message
				callback(decoded_message)
	except Exception as e:
		print(f"Error subscribing to Redis channel: {e}")

# Example usage:

# Define a callback function for handling subscribed messages
def handle_message(message):
	print("Received message:")
	print(message)

def test_pubsub():
	# Example message in the specified format
	example_message = {
		'message': 'Hello, Redis!',
		'title': 'Greeting',
		'status': 'ok',
		'filepath': 'example.py',
		'fileline': 42
	}

	# Publish the example message to the Redis channel
	publish_to_redis_channel(example_message)

	# Subscribe to the Redis channel and provide the callback function
	subscribe_to_redis_channel(handle_message)
