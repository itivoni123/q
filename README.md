# Webcam Server

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
   cd webcam_server
   

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
   Navigate to e2e
   Run: pytest -v -s -k test_camera_access
   