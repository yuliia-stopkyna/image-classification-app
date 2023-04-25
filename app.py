import os

import tensorflow as tf
from flask import Flask, render_template, request

from classifier import classify

app = Flask(__name__)

STATIC_FOLDER = "static"
UPLOAD_FOLDER = "static/uploads/"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

flower_model = tf.keras.models.load_model(STATIC_FOLDER + "/model/flower_model.h5")


@app.get("/")
def upload_page():
    return render_template("upload_page.html")


@app.post("/")
def return_result():
    image = request.files["image"]
    image_path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(image_path)

    predicted_label, probability = classify(flower_model, image_path)

    return render_template(
        "result_page.html",
        predicted_label=predicted_label,
        probability=probability,
        image_path=f"uploads/{image.filename}",
    )


if __name__ == "__main__":
    app.run()
