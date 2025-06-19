from flask import Flask, request, jsonify

# Create a Flask web application instance
app = Flask(__name__)

# --- GET API Endpoint ---
# This route handles GET requests to the root URL ('/').
# When you open this URL in a browser, this function will run.
@app.route('/', methods=['GET'])
def get_hello():
    """
    Responds to GET requests on the root path with a simple text message.
    """
    return "<h1>Hello from the GET API!</h1>"

# --- POST API Endpoint ---
# This route handles POST requests to the '/data' URL.
# It expects incoming data to be in JSON format.
@app.route('/data', methods=['POST'])
def post_data():
    """
    Responds to POST requests on the /data path.
    It attempts to parse the request body as JSON and returns it.
    If the request is not JSON, it returns an error.
    """
    # Check if the incoming request has a JSON content type
    if request.is_json:
        # Get the JSON data from the request body.
        # Flask's request.get_json() automatically parses it into a Python dictionary.
        received_json_data = request.get_json()
        
        # You can print this data to your terminal where the Flask app is running
        # to confirm it's received. This is for debugging, not part of the API response.
        print(f"Received POST data: {received_json_data}")
        
        # Return a JSON response back to the client, confirming success and echoing the data.
        # jsonify helps convert Python dictionaries into proper JSON responses.
        return jsonify({
            "status": "success",
            "message": "Data received by POST API!",
            "your_data": received_json_data
        }), 200 # HTTP 200 OK status code
    else:
        # If the request was not JSON, return an error message with a 400 Bad Request status.
        return jsonify({
            "status": "error",
            "message": "Request must be JSON. Please set Content-Type to application/json."
        }), 400 # HTTP 400 Bad Request status code

# This block ensures that the Flask development server only runs when this script
# is executed directly (e.g., by running `python app.py` in your terminal).
if __name__ == '__main__':
    # Run the Flask application.
    # debug=True: Activates Flask's debugger and auto-reloader, useful for development.
    # host='0.0.0.0': Makes the server accessible from any IP address on your network (including localhost).
    # port=5000: Specifies that the server should listen for requests on port 5000.
    app.run(debug=True, host='0.0.0.0', port=5000)
