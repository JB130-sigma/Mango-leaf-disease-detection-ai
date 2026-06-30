from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
from PIL import Image
import json

app = Flask(__name__)

# Load model
model = tf.keras.models.load_model(
    "mango_disease_model_v2(updated).keras"
)

# Load class names
with open("class_names_Mango.json", "r") as f:
    class_names = json.load(f)
    print("Model Loaded Successfully")
    print("Classes:", class_names)
# Remedies
remedies = {
    "Anthracnose": {
        "en": "Remove infected leaves and fruits. Spray a copper-based fungicide every 10-15 days. Avoid water staying on leaves for long periods.",
        "hi": "संक्रमित पत्तियों और फलों को हटाएं। हर 10-15 दिन में कॉपर आधारित फफूंदनाशक का छिड़काव करें। पत्तियों पर लंबे समय तक पानी जमा न रहने दें।"
    },

    "Bacterial Canker": {
        "en": "Cut and destroy infected branches. Apply copper bactericide. Use clean pruning tools to prevent the disease from spreading.",
        "hi": "संक्रमित शाखाओं को काटकर नष्ट करें। कॉपर बैक्टीरिसाइड का उपयोग करें। रोग फैलने से रोकने के लिए साफ उपकरणों का उपयोग करें।"
    },

    "Cutting Weevil": {
        "en": "Remove damaged leaves and shoots. Spray a recommended insecticide. Keep the area around the tree clean.",
        "hi": "क्षतिग्रस्त पत्तियों और टहनियों को हटाएं। उपयुक्त कीटनाशक का छिड़काव करें। पेड़ के आसपास की जगह साफ रखें।"
    },

    "Die Back": {
        "en": "Prune affected branches 10-15 cm below the damaged area. Apply fungicide on cut surfaces and maintain proper tree nutrition.",
        "hi": "प्रभावित शाखाओं को रोगग्रस्त भाग से 10-15 सेमी नीचे से काटें। कटे हुए भाग पर फफूंदनाशक लगाएं और पौधे को उचित पोषण दें।"
    },

    "Gall Midge": {
        "en": "Remove affected leaves and use insect traps. Spray recommended insecticides during infestation.",
        "hi": "प्रभावित पत्तियों को हटाएं और कीट फंदों का उपयोग करें। संक्रमण होने पर अनुशंसित कीटनाशक का छिड़काव करें।"
    },

    "Healthy": {
        "en": "The leaf appears healthy. Continue regular watering, nutrition management, and periodic inspection.",
        "hi": "पत्ती स्वस्थ दिखाई दे रही है। नियमित सिंचाई, पोषण प्रबंधन और समय-समय पर निरीक्षण जारी रखें।"
    },

    "Powdery Mildew": {
        "en": "Spray sulfur-based fungicide. Improve airflow around the tree by pruning overcrowded branches.",
        "hi": "सल्फर आधारित फफूंदनाशक का छिड़काव करें। अतिरिक्त शाखाओं की छंटाई करके हवा का प्रवाह बढ़ाएं।"
    },

    "Sooty Mould": {
        "en": "Control insects such as aphids and mealybugs. Wash affected leaves and improve plant hygiene.",
        "hi": "एफिड और मिलीबग जैसे कीटों को नियंत्रित करें। प्रभावित पत्तियों को साफ करें और पौधे की स्वच्छता बनाए रखें।"
    },

    "Non_Mango": {
        "en": "This image does not appear to be a mango leaf. Please upload a clear image of a mango leaf.",
        "hi": "यह आम के पत्ते की तस्वीर नहीं लगती। कृपया आम के पत्ते की स्पष्ट तस्वीर अपलोड करें।"
    }
}

@app.route("/")
def home():
    return render_template("Mango_leaves.html")

@app.route("/predict", methods=["POST"])
def predict():

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"})

    file = request.files["file"]

    # Image preprocessing
    img = Image.open(file).convert("RGB")
    img = img.resize((224, 224))

    img_array = np.array(img, dtype=np.float32)
    img_array = np.expand_dims(img_array, axis=0)

    # Prediction
    prediction = model.predict(img_array, verbose=0)

    predicted_index = np.argmax(prediction)
    predicted_class = class_names[predicted_index]

    confidence = float(np.max(prediction) * 100)

    # Non mango handling
    if predicted_class == "Non_Mango":
        return jsonify({
            "disease": "Non_Mango",
            "confidence": round(confidence, 2),
            "message": "This image is not a mango leaf."
        })
    language = request.form.get("language", "en")
    return jsonify({
        "disease": predicted_class,
        "confidence": round(confidence, 2),
        "remedy": remedies[predicted_class][language]
    })

if __name__ == "__main__":
    app.run(debug=True)