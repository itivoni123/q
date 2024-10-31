from datetime import datetime
import cv2
import os


# Directory to save screenshots
SCREENSHOT_DIR = 'screenshots'
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


def test_camera_access():
    # Use the UDP stream
    cap = cv2.VideoCapture(0)

    # Check if the camera is accessible
    assert cap.isOpened(), "Camera should be accessible"

    # Attempt to read a frame from the camera
    ret, frame = cap.read()
    assert ret, "Should be able to read a frame from the camera"
    assert frame is not None, "Captured frame should not be None"

    # Save the frame as a screenshot
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_file_path = f"screenshot_{timestamp}.png"
    screenshot_path = os.path.join(SCREENSHOT_DIR, screenshot_file_path)

    # Ensure the screenshot directory exists
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)

    # Write the frame to a file and check if it was successful
    success = cv2.imwrite(screenshot_path, frame)
    assert success, "Failed to save the screenshot"

    print(f"Screenshot saved at {screenshot_path}")

    # Release the camera resource
    cap.release()


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Webcam Feed' in response.data
