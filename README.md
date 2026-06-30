🌿 Mango-leaf-disease-detection-ai

Mango Disease Detection AI is a web-based application that helps identify diseases in mango leaves using Artificial Intelligence and Deep Learning. Users can upload an image of a mango leaf, and the system predicts the disease category along with suitable remedies.

The project also includes a Non-Mango detection feature to identify images that do not belong to mango leaves.

Features


- Detects multiple mango leaf diseases
- Identifies non-mango leaf images
- Provides disease remedies
- Supports English and Hindi remedies
- User-friendly web interface
- Real-time image prediction


Technologies Used

Machine Learning

- TensorFlow
- Keras
- MobileNetV2
- NumPy

Backend

- Flask

Frontend

- HTML
- CSS
- JavaScript

Project Structure

Mango-leaf-disease-detection-ai/
│
├── app.py
├── requirements.txt
├── README.md
├── class_names_Mango.json
├── mango_disease_model_v2.keras
│
└── templates/
    └── Mango_leaves.html

How to Run

1. Clone the repository.
2. Install the required dependencies.

pip install -r requirements.txt

3. Start the Flask server.

python app.py

4. Open your browser and visit:

http://127.0.0.1:5000

Usage

1. Upload a mango leaf image.
2. Click on Predict Disease.
3. View the predicted disease.
4. Check the recommended remedy.

Future Enhancements

- Support for more plant species
- Mobile application deployment
- Cloud deployment
- Additional regional language support

Author

Jeet Bhandari

AI & Machine Learning Enthusiast