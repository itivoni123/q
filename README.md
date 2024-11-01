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


3. Build the Docker Image:
   ```bash
   docker build -t web_cam .


4. Run the Tests(Command Line):
   ```bash
   docker run --rm web_cam pytest 
   
5. Run the Tests(Command Line):
   ```bash
   docker run --rm your_image_name pytest
   Run: pytest -v -s -k test_camera_access 
   Run: pytest -v -s -k test_index 
   
### Running Docker Containers
When you run a Docker container using the Ubuntu image, it won't have direct access to your Mac's hardware (like cameras). If you want to use the camera in a Docker container, the following points are important:

1. **Camera Access**:
   Direct access to the camera from Docker on macOS is not supported because Docker for Mac runs containers in a virtualized environment. You won't be able to use `/dev/video*` devices directly.

2. **Virtual Camera**:
   If you want to test camera functionality without physical access, consider using a virtual camera solution that can simulate video input. Unfortunately, creating virtual video devices in Docker on macOS is more complex and often not feasible.

3. **Testing Outside of Docker**:
   If your primary goal is to test camera functionality, consider running your application directly on macOS without Docker. This way, you can access the camera directly from your application.

### Summary
Run the commands on your macOS terminal to check for camera recognition. Since Docker on macOS does not allow direct access to hardware like cameras, consider testing your application outside of Docker or look into virtual camera solutions that are compatible with macOS. If you have further questions, feel free to ask!
   
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

## References
1. **Flask Documentation**
2. **OpenCV Python Documentation**
3. **pytest Documentation**