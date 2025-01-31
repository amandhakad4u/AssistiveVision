import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
import cv2
from PIL import Image
import pyttsx3
# import threading

def camera():
    # Start the webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        exit()

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        # If frame is read correctly, ret is True
        if not ret:
            print("Error: Failed to capture image.")
            break
        
        # Display the frame (webcam video feed)
        cv2.imshow("Webcam Feed", frame)
        
        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()




def text_to_speech(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set the speed (rate) of speech (default is around 200 words per minute)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate + 0)  # Increase speed (e.g., 50 faster)

    # Set volume (optional)
    engine.setProperty('volume', 1)  # Volume level from 0.0 to 1.0

    # Speak the text
    engine.say(text)

    # Wait until speaking is finished
    engine.runAndWait()


# Load BLIP model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption_from_webcam():
    c=""
    # Start the webcam
    cap = cv2.VideoCapture(0)
    
    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return None
    

    
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        # If frame is read correctly, ret is True
        if not ret:
            print("Error: Failed to capture image.")
            break
        
        # Display the frame
        cv2.imshow("Webcam Feed", frame)
        
        
        if cv2.waitKey(1) :
            # Convert the captured frame to PIL image format
            image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            
            # Process the image
            inputs = processor(image, return_tensors="pt")
            
            # Generate caption
            with torch.no_grad():
                output = model.generate(**inputs)
            
            # Decode and print the caption
            caption = processor.tokenizer.decode(output[0], skip_special_tokens=True)
            # print("Generated Caption:", caption)
            # Example usage
            if c!=caption:
                text = caption
                text_to_speech(text)
                c=caption

         
            
            
    
    # Release the webcam and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

# Example usage




generate_caption_from_webcam()



