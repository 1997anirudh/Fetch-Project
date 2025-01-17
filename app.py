from flask import Flask, request
import uuid
from datetime import datetime

app = Flask(__name__)
receipts_data = {}

def calculate_points(receipt):
    points = 0
    # One point for every alphanumeric character in the retailer name
    points += sum(char.isalnum() for char in receipt['retailer'])

    total = float(receipt['total'])

    # 50 points if the total is a round dollar amount with no cents
    if total.is_integer():
        points += 50

    # 25 points if the total is a multiple of 0.25
    if total % 0.25 == 0:
        points += 25

    # 5 points for every two items on the receipt
    points += (len(receipt['items']) // 2) * 5

    # Apply the LLM-specific rule: 5 points if the total is greater than 10.00
    if total > 10.00:
        points += 5

    # Points based on item descriptions
    for item in receipt['items']:
        desc_len = len(item['shortDescription'].strip())
        if desc_len % 3 == 0:
            points += -(-float(item['price']) * 0.2 // 1)  # Round up to nearest integer

    # 6 points if the day in the purchase date is odd
    day = int(receipt['purchaseDate'].split('-')[-1])
    if day % 2 != 0:
        points += 6

    # 10 points if the time of purchase is between 2:00pm and 4:00pm
    time = datetime.strptime(receipt['purchaseTime'], '%H:%M').time()
    if 14 <= time.hour < 16:
        points += 10

    return points


# Define the home route
@app.route('/')
def home():
    return "Welcome to the Receipt Processor API", 200


# POST method to process a receipt
@app.route('/receipts/process', methods=['POST'])
def process_receipt():
    try:
        receipt = request.json
        if not receipt:
            return "Invalid JSON payload", 400
        receipt_id = str(uuid.uuid4())
        points = calculate_points(receipt)
        receipts_data[receipt_id] = points
        return f"Receipt processed with ID: {receipt_id}", 200
    except Exception as e:
        return f"An error occurred: {str(e)}", 500


# GET method to retrieve points of a receipt by its ID
@app.route('/receipts/<id>/points', methods=['GET'])
def get_points(id):
    if id in receipts_data:
        return f"Points for receipt {id}: {receipts_data[id]}", 200
    return "Receipt not found", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
