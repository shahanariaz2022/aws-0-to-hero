from flask import Flask
import time
import random
import boto3


app = Flask(__name__)

# Initialize AWS CloudWatch client
cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')

# Sample product data for our online store
products = {
    '1': {'name': 'Product 1', 'price': 10.99},
    '2': {'name': 'Product 2', 'price': 19.99},
    '3': {'name': 'Product 3', 'price': 5.49}
}

@app.route('/')
def index():
    start_time = time.time()

    # Simulate processing time
    time.sleep(random.uniform(0.1, 0.5))

    # Log the page view metric to CloudWatch
    log_metric('PageViews', 1)
