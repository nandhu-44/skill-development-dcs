# Diabetes Prediction System

A comprehensive web application for predicting diabetes likelihood based on medical input parameters. This project uses machine learning (Random Forest Classifier) and a Flask web interface.

## Project Structure

- **app.py**: The main Flask application file handling web requests and predictions.
- **train.py**: Script to train the machine learning model using the dataset.
- **models/**: Directory where the trained model (diabetes_model.pkl) is saved.
- **templates/**: HTML files for the web interface.
- **static/**: CSS and other static assets.
- **requirements.txt**: List of Python dependencies.

## Prerequisites

- Python 3.8 or higher installed on your system.

## Setup Instructions

1. **Install Dependencies**

    Open a terminal in the project directory and run the following command to install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

2. **Train the Model**

    Before running the application, you must generate the machine learning model. Run the training script:

    ```bash
    python train.py
    ```

    This will download the dataset, train the Random Forest model, and save it to `models/diabetes_model.pkl`.

3. **Run the Application**

    Start the Flask web server:

    ```bash
    python app.py
    ```

4. **Access the Application**

    Open your web browser and navigate to the address shown in the terminal (usually <http://127.0.0.1:5000>).

## Usage

1. Enter the required patient information:
    - Number of Pregnancies
    - Glucose Level
    - Blood Pressure
    - BMI
    - Age
2. Click the "Predict" button.
3. The system will display whether the patient is "Diabetic" or "Not Diabetic" along with a confidence percentage.
