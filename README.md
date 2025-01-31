Assistive Vision Program for the Blind
Overview
This project is an assistive tool designed to help visually impaired people by providing real-time captions of their surroundings. Using a webcam, the program captures video feed and generates captions describing what is happening around them. The captions are then read out loud using text-to-speech technology. This tool utilizes machine learning models, a webcam, and speech synthesis to assist the user in understanding their environment.

Features
Real-time caption generation: The program continuously captures video from a webcam and generates captions describing the scene.
Text-to-speech: The generated captions are read out loud using pyttsx3 (text-to-speech library).
Webcam feed: The live webcam feed is displayed for visual monitoring, while the captions are provided for audio feedback.
Installation
Prerequisites
Make sure you have Python 3.x installed on your system. You will also need a webcam for video capture.

Step 1: Clone the repository (or download the code)
To get started, clone the repository to your local machine:

bash
Copy
Edit
git clone <repository-url>
Step 2: Install the dependencies
The program requires a few libraries to run. You can install them by creating a requirements.txt file, which contains the necessary dependencies:

bash
Copy
Edit
torch==2.2.0
transformers==4.33.0
opencv-python==4.7.0.72
Pillow==9.5.0
pyttsx3==2.90
To install the dependencies, run the following command:

bash
Copy
Edit
pip install -r requirements.txt
Step 3: Run the Program
Once the dependencies are installed, you can run the program using the following command:

bash
Copy
Edit
python assistive_vision.py
This will start the webcam, and the program will begin to describe what is happening in real-time through captions.

Step 4: Exit the Program
To exit the program, simply press the 'q' key while the webcam feed window is active.

Usage
When the program is running, it will continuously detect objects and scenes through the webcam.
The captions will be read aloud using text-to-speech.
The captions will update only when there is a new scene or description to share, preventing repetitive speech.
Technologies Used
PyTorch: Used for loading and running the BLIP model (an image captioning model) to generate descriptions.
Transformers: For loading the pre-trained BLIP model from Salesforce.
OpenCV: To capture video from the webcam in real time.
Pillow: For image processing and converting video frames into image formats.
pyttsx3: For text-to-speech functionality that reads out the generated captions.
Contributing
Feel free to fork this project, raise issues, and make contributions via pull requests. Please ensure that any new code is well-documented and follows the coding conventions of the project.
