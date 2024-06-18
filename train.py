import numpy as np
import pandas as pd
import os
from PIL import Image
from sklearn.model_selection import train_test_split
from keras.layers import LSTM, Dense, Dropout
from keras.models import Sequential

# Define the path to your image folders
bodyswing_path = 'path/to/bodyswing_images'
handswing_path = 'path/to/handswing_images'

def load_images_from_folder(folder):
    images = []
    for filename in sorted(os.listdir(folder)):  # Ensure images are sorted to maintain sequence
        img = Image.open(os.path.join(folder, filename))
        img = img.resize((64, 64))  # Resize images to a fixed size
        img_array = np.array(img)
        images.append(img_array)
    return np.array(images)

# Load images
bodyswing_images = load_images_from_folder(bodyswing_path)
handswing_images = load_images_from_folder(handswing_path)

X = []
y = []
no_of_timesteps = 10

# Create sequences of images for bodyswing
n_sample = len(bodyswing_images)
for i in range(no_of_timesteps, n_sample):
    X.append(bodyswing_images[i-no_of_timesteps:i, :])
    y.append(1)

# Create sequences of images for handswing
n_sample = len(handswing_images)
for i in range(no_of_timesteps, n_sample):
    X.append(handswing_images[i-no_of_timesteps:i, :])
    y.append(0)

X, y = np.array(X), np.array(y)
print(X.shape, y.shape)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Build the LSTM model
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(X.shape[1], X.shape[2], X.shape[3], X.shape[4])))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50))
model.add(Dropout(0.2))
model.add(Dense(units=1, activation="sigmoid"))

model.compile(optimizer="adam", metrics=['accuracy'], loss="binary_crossentropy")

# Train the model
model.fit(X_train, y_train, epochs=16, batch_size=32, validation_data=(X_test, y_test))

# Save the model
model.save("model.h5")