# Assistive Vision for the Blind

## Overview
This program is designed to assist blind and visually impaired individuals by describing their surroundings in real-time. Using a webcam, the program captures the environment, generates captions describing the scene, and converts those captions into speech. It leverages cutting-edge machine learning models for image captioning and text-to-speech technology to provide an enhanced user experience.

## Features
- **Real-Time Object and Scene Description:** Continuously captures video from a webcam and generates descriptive captions of the surroundings.
- **Text-to-Speech Feedback:** The generated captions are read aloud to the user, enabling auditory understanding of the environment.
- **Simple Interface:** Easy to use with no complex setup; simply run the program and it starts providing assistance.
- **Instant Updates:** The program updates captions based on changes in the scene or environment.

## Technologies Used
- **PyTorch:** Loads and runs the BLIP (Bootstrapping Language-Image Pretraining) model for real-time image captioning.
- **Transformers:** Handles the pre-trained models for caption generation.
- **OpenCV:** Captures real-time video from the webcam.
- **Pillow:** Converts video frames into a format compatible with the captioning model.
- **pyttsx3:** Provides text-to-speech functionality to read out the generated captions.

## Installation

Follow these steps to set up the program:

### 1. Clone the Repository
Clone the repository to your local machine using the following command:

```bash
git clone <repository-url>
2. Install Dependencies

txt
Copy
Edit
torch==2.2.0
transformers==4.33.0
opencv-python==4.7.0.72
Pillow==9.5.0
pyttsx3==2.90
Install the dependencies with:

bash
Copy
Edit
pip install -r requirements.txt
3. Run the Program
After installing the dependencies, run the program with the following command:

bash
Copy
Edit
python assistive_vision.py
The program will start the webcam, capture the surroundings, and begin reading out captions.

4. Exit the Program
To stop the program, simply press the 'q' key while the webcam feed window is active.

Usage
Once the program is running:

The webcam feed will be displayed in a window.
Captions of the current scene will be generated and read aloud.
The program continuously updates the description based on visual changes in the environment.
Contributing
Contributions are welcome! If you find a bug or have ideas for improvements, please feel free to:

Fork the repository.
Create a new branch for your changes.
Submit a pull request.
Ensure your code follows the project conventions and is properly documented.

Let's make assistive vision technology accessible to all! 🚀
