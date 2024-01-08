# Import necessary modules
import base64
import cv2
import numpy as np
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data to store enrolled users and their biometric data
enrolled_corpers = []
enrolled_it_students = []

# Route for the index page
@app.route('/')
def index():
    return render_template('index.html')

# Route for Corper enrollment form
@app.route('/enroll', methods=['POST'])
def enroll():
    user_type = request.form.get('user_type')
    if user_type == 'corper':
        return render_template('corper_form.html')
    elif user_type == 'it_student':
        return render_template('it_students_form.html')
    else:
        return redirect(url_for('index'))

# Route for submitting Corper form
@app.route('/submit_corper_form', methods=['POST'])
def submit_corper_form():
    corper_data = {
        'name': request.form['name'],
        'state_code': request.form['state_code'],
        'batch': request.form['batch'],
        'cds_day': request.form['cds_day'],
        'passing_out_date': request.form['passing_out_date']
    }
    enrolled_corpers.append(corper_data)
    return "Corper form submitted successfully!"

# Route for submitting IT Student form
@app.route('/submit_it_student_form', methods=['POST'])
def submit_it_student_form():
    it_student_data = {
        'name': request.form['name'],
        'institution': request.form['institution'],
        'registration_number': request.form['registration_number'],
        'it_duration': request.form['it_duration'],
        'resumption_date': request.form['resumption_date']
    }
    enrolled_it_students.append(it_student_data)
    return "IT Student form submitted successfully!"

# Route for face capture
@app.route('/capture_face', methods=['GET'])
def capture_face():
    return render_template('face_capture.html')

# Route for fingerprint capture
@app.route('/capture_fingerprint', methods=['GET'])
def capture_fingerprint():
    return render_template('fingerprint_capture.html')

# Handle captured face data
@app.route('/process_face_capture', methods=['GET', 'POST'])
def process_face_capture():
    if request.method == 'POST':
        # Get the captured image data (base64-encoded)
        image_data = request.form['imageData']

        # Decode base64 and process the image (you may use py_facerecognition here)
        img_bytes = base64.b64decode(image_data.split(',')[1])
        img_array = np.frombuffer(img_bytes, dtype=np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        # TODO: Perform face recognition and store the data

        return "Face capture processed successfully!"
    else:
        # Handle GET request (if needed)
        return render_template('process_face_capture.html')

# Handle captured fingerprint data
@app.route('/process_fingerprint_capture', methods=['POST'])
def process_fingerprint_capture():
    # Get the captured fingerprint data
    fingerprint_data = request.form['fingerprintData']

    # TODO: Process and store the fingerprint data (use pyfingerprint library)

    return "Fingerprint capture processed successfully!"

if __name__ == '__main__':
    app.run(debug=True)
