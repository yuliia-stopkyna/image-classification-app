import numpy as np
from keras.utils import load_img, img_to_array
from numpy import ndarray

IMAGE_SIZE = (100, 100)
LABELS = ["Daisy", "Dandelion", "Rose", "Sunflower", "Tulip"]


def preprocess_image(image) -> ndarray:
    img_array = img_to_array(image)
    img_array = np.expand_dims(img_array, axis=0)

    return img_array


def load_and_preprocess_image(image_path: str) -> ndarray:
    image = load_img(image_path, target_size=IMAGE_SIZE)

    return preprocess_image(image)


def classify(model, image_path: str) -> tuple[str, float]:
    preprocessed_image = load_and_preprocess_image(image_path)

    prediction = model.predict(preprocessed_image)
    predicted_label_index = np.argmax(prediction[0])
    probability = round(prediction[0][predicted_label_index] * 100, 2)
    predicted_label = LABELS[predicted_label_index]

    return predicted_label, probability
