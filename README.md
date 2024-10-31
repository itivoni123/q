# q.ai Task

## Description
This application captures video from the webcam, serves it on a local Flask server, and displays the stream on a web page.

## Requirements
- Python 3
- Flask
- OpenCV
- pytest

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd q
   

2. Set Up a Virtual Environment:
   ```bash 
   python3 -m venv venv
   source venv/bin/activate

3. Install Dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the Application:
   ```bash
   python app.py

5. Run the Tests(Command Line):
   ```bash
   Navigate to q
   Run: pytest -v -s -k test_camera_access
   Run: pytest -v -s -k test_index
   
## Tests Description

### `test_camera_access`
1. **Camera Access**: This test checks if the webcam can be accessed by attempting to open it with OpenCV's `VideoCapture`.
2. **Frame Capture**: It tries to read a frame from the camera, ensuring that the operation is successful and that the captured frame is not `None`.
3. **Screenshot Saving**: The test saves the captured frame as a screenshot in a specified directory, using a timestamp in the filename to ensure uniqueness.
4. **Directory Management**: It checks if the directory for saving screenshots exists and creates it if not.
5. **File Write Verification**: The test verifies that the screenshot was saved successfully.
6. **Resource Cleanup**: Finally, it releases the camera resource to free up the device.

### `test_index`
1. **Page Load Verification**: This test checks if the main page of the web application can be accessed by sending a GET request to the root URL (`/`).
2. **Status Code Check**: It asserts that the HTTP response status code is `200`, indicating a successful request.
3. **Content Check**: The test verifies that the response contains the text "Webcam Feed", ensuring the correct content is rendered on the page.

These tests ensure both the functionality of the camera access and the proper rendering of the web application.