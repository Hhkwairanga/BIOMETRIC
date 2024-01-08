<!-- fingerprint_capture.html -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
    <script src="{{ url_for('static', filename='capture.js') }}"></script>
    <title>Fingerprint Capture - NDIC Enrolment System</title>
</head>

<body>
    <div class="background-logo"></div>
    <div class="content">
        <div class="header">
            <img src="{{ url_for('static', filename='images/top_left_logo.png') }}" alt="NDIC Logo" class="logo">
            <h1>Fingerprint Capture</h1>
        </div>
    </div>

    <div id="fingerprintCapture" class="biometric-capture">
        <p>Place your finger on the fingerprint scanner:</p>
        <!-- Add elements for displaying the fingerprint image and status -->

        <button id="captureFingerprintBtn">Capture Fingerprint</button>
    </div>
</body>

</html>
