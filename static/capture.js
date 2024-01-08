// capture.js
document.addEventListener('DOMContentLoaded', function () {
    const video = document.getElementById('video');
    const captureBtn = document.getElementById('captureBtn');

    // Use getUserMedia to access the webcam
    navigator.mediaDevices.getUserMedia({ video: true })
        .then((stream) => {
            video.srcObject = stream;
        })
        .catch((error) => {
            console.error('Error accessing webcam:', error);
        });

    // Handle face capture
    captureBtn.addEventListener('click', function () {
        const canvas = document.createElement('canvas');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        const context = canvas.getContext('2d');
        context.drawImage(video, 0, 0, canvas.width, canvas.height);

        const imageDataURL = canvas.toDataURL('image/png');
        // Send imageDataURL to the server for processing and storage
        // You can use AJAX or other methods to send the captured data

        // Assuming you want to submit the form after capturing the face
        // You may need to update this URL based on your routes
        window.location.href = "/process_face_capture";
    });
});
