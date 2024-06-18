import os
import numpy as np
import pandas as pd
import mediapipe as mp
from PIL import Image

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True, model_complexity=2, min_detection_confidence=0.5)

def process_image_with_mediapipe(image_path):
    image = Image.open(image_path).convert('RGB')
    image = image.resize((256, 256))  # Resize to a fixed size
    img_array = np.array(image)

    results = pose.process(img_array)

    if results.pose_landmarks:
        # Extract specific pose landmarks (lower body)
        pose_landmarks = results.pose_landmarks
        # Define indices of the landmarks for lower body
        lower_body_indices = [23, 24, 25, 26, 27, 28, 29, 30]
        landmarks = np.array([[pose_landmarks.landmark[idx].x, 
                               pose_landmarks.landmark[idx].y,
                               pose_landmarks.landmark[idx].z,
                               pose_landmarks.landmark[idx].visibility] for idx in lower_body_indices]).flatten()
    else:
        # No pose detected, return a vector of zeros
        landmarks = np.zeros(8 * 4)  # 10 landmarks with 4 attributes (x, y, z, visibility)

    return landmarks

def load_and_process_images_from_folder(folder):
    images = []
    for filename in sorted(os.listdir(folder)):  # Ensure images are sorted to maintain sequence
        file_path = os.path.join(folder, filename)
        landmarks = process_image_with_mediapipe(file_path)
        images.append(landmarks)
    return np.array(images)

# Define the path to your image folders
left_path = './output/left'
right_path = './output/right'

# Process images
left_images = load_and_process_images_from_folder(left_path)
right_images = load_and_process_images_from_folder(right_path)

# Create labels
left_labels = np.ones(len(left_images))  # Label for left images
right_labels = np.zeros(len(right_images))  # Label for right images

# Combine the data
X = np.concatenate((left_images, right_images), axis=0)
y = np.concatenate((left_labels, right_labels), axis=0)

# Create a DataFrame
data = pd.DataFrame(X)
data['label'] = y

# Save to CSV
data.to_csv('mediapipe_lower_body_pose_data_2.csv', index=False)

# Release MediaPipe resources
pose.close()