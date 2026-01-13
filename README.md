# Diabetes Prediction System

A comprehensive web application for predicting diabetes likelihood based on medical input parameters. This project uses machine learning (Random Forest Classifier) and provides both Flask and FastAPI implementations with Docker support.

## Project Structure

- **main.py**: FastAPI application providing REST API endpoints for diabetes prediction with automatic documentation.
- **app.py**: Flask web application with traditional web interface.
- **train.py**: Script to train the machine learning model using the dataset.
- **models/**: Directory where the trained model (diabetes_model.pkl) is saved.
- **templates/**: HTML files for the Flask web interface.
- **static/**: CSS and other static assets.
- **requirements.txt**: List of Python dependencies.
- **Dockerfile**: Docker configuration for containerized deployment.
- **docker-build.bat** & **docker-run.bat**: Windows batch scripts for Docker operations.

## Prerequisites

- Python 3.8 or higher installed on your system.
- Docker (optional, for containerized deployment).

## Setup Instructions

### Local Development

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

### Running the Applications

#### Option 1: FastAPI with Uvicorn (Recommended)

Run the FastAPI application with Uvicorn:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

- **API Documentation**: Visit <http://127.0.0.1:8000/docs> for interactive API documentation
- **Health Check**: <http://127.0.0.1:8000/health>
- **API Endpoint**: POST to <http://127.0.0.1:8000/predict> with JSON payload

#### Option 2: Flask Application

Start the Flask web server:

```bash
python app.py
```

Access the web interface at <http://127.0.0.1:5000>

### Docker Deployment

#### Using Batch Scripts (Windows)

1. **Build the Docker Image**

    ```bash
    docker-build.bat
    ```

2. **Run the Container**

    ```bash
    docker-run.bat
    ```

#### Manual Docker Commands

1. **Build the Docker Image**

    ```bash
    docker build -t diabetes-prediction-app .
    ```

2. **Run the Container**

    ```bash
    docker run -p 8000:8000 diabetes-prediction-app
    ```

The application will be available at <http://localhost:8000>

## Usage

1. Enter the required patient information:
    - Number of Pregnancies
    - Glucose Level
    - Blood Pressure
    - BMI
    - Age
2. Click the "Predict" button.
3. The system will display whether the patient is "Diabetic" or "Not Diabetic" along with a confidence percentage.
