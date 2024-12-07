# Import necessary modules from Flask
from flask import Flask, request, jsonify, render_template

# Initialize a Flask app
app = Flask(__name__)

# Define the route for the homepage (root URL) where the booking form is rendered
@app.route('/')
def index():
    # Render the 'booking.html' template when the root URL is accessed
    return render_template('booking.html')  

# Define the route to handle the booking form submission
# This route only accepts POST requests (used for form submissions)
@app.route('/submit-booking', methods=['POST'])
def submit_booking():
    # Get the form data submitted by the user using the 'request.form.get()' method
    name = request.form.get('name') 
    email = request.form.get('email')
    phone = request.form.get('phone')
    date = request.form.get('date')
    time = request.form.get('time')
    guests = request.form.get('guests')
    requests_special = request.form.get('requests')  # Special requests field, which is optional

    # Validate the form data: ensure required fields are not empty
    # If any required field is missing, return a 400 status with an error message
    if not name or not email or not phone or not date or not time or not guests:
        return jsonify({"error": "All fields except Special Requests are required!"}), 400

    # If all required fields are filled, create a booking dictionary
    # This dictionary could later be stored in a database (currently, it's just returned as JSON)
    booking = {
        "name": name,
        "email": email,
        "phone": phone,
        "date": date,
        "time": time,
        "guests": guests,
        "requests": requests_special  
    }

    # Return a JSON response indicating the booking was successful, along with the booking details
    return jsonify({"message": "Booking successful!", "data": booking}), 200

# Check if the script is being run directly (not imported), and if so, run the Flask app
if __name__ == '__main__':
    # Start the Flask app in debug mode (this gives you more detailed error output for debugging)
    app.run(debug=True)
