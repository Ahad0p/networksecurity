# 🛡️ Network Security ML Pipeline (MLOps Project)

An end-to-end Machine Learning project for **Phishing Website Detection**, built using a complete **MLOps pipeline** with:

- 🧪 Data Ingestion & Validation  
- ⚙️ Data Transformation  
- 🤖 Model Training & Selection  
- 📈 Model Tracking with **MLflow + Dagshub**  
- 🚀 Deployment using **FastAPI**

---

## 🚀 Tech Stack

| Layer            | Tools Used                                |
|------------------|--------------------------------------------|
| Language         | Python                                     |
| ML Models        | Random Forest, Logistic Regression, etc.  |
| MLOps Framework  | MLflow, Dagshub                            |
| Web API          | FastAPI                                    |
| Model Tracking   | MLflow + Dagshub                           |
| Version Control  | Git + GitHub                               |
| Cloud Storage    | AWS S3 (Optional - via `s3_sync`)          |
| Others           | NumPy, Pandas, Sklearn, Joblib, PyMongo   |

---

## 📂 Project Structure

├── app.py # FastAPI App (train & predict routes)
├── main.py # Direct CLI execution
├── networksecurity/ # Core module with all components
│ ├── components/ # Data ingestion, validation, transformation, model trainer
│ ├── entity/ # Artifact and config classes
│ ├── constant/ # All project-wide constants
│ ├── utils/ # Utility functions & evaluation metrics
│ ├── pipeline/ # Main TrainingPipeline class
├── final_model/ # Stores the final model.pkl
├── artifacts/ # Auto-generated pipeline outputs
├── data_schema/ # Schema definition for validation
├── .env # For environment variables (MongoDB, etc.)
├── .gitignore # To exclude unnecessary files
├── README.md # You're reading this


---

## 🧠 ML Pipeline Overview

1. **Data Ingestion**  
   - Loads CSV data (phishing URLs)
   - Stores in feature store & train/test split

2. **Data Validation**  
   - Validates columns against a predefined schema
   - Performs data drift detection

3. **Data Transformation**  
   - Applies preprocessing with `KNNImputer`, encoders
   - Saves transformed `.npy` and preprocessor object

4. **Model Training**  
   - Trains multiple classifiers using GridSearchCV
   - Selects best model & saves with `NetworkModel` class
   - Logs metrics and model to MLflow/Dagshub

5. **Deployment**  
   - FastAPI exposes `/train` and `/predict`
   - Run via `uvicorn app:app --reload`

---

## 🚀 How to Run the Project

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/networksecurity.git
cd networksecurity

# 2. Setup Virtual Environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set your environment variables in `.env`

# 5. Start training via FastAPI
uvicorn app:app --reload

# Visit http://127.0.0.1:8000/docs to interact


📦 Model Prediction
Upload a test file via /predict endpoint in Swagger UI.
Response will return predictions based on your trained model.

📁 .env Example
MONGODB_URL_KEY="mongodb+srv://<your-user>:<password>@cluster.mongodb.net/DB_NAME"

🙌 Acknowledgments
Thanks to:

Krish Naik’s MLOps guidance

Dagshub for easy tracking

FastAPI for rapid deployment

📬 Connect With Me
🔗 https://www.linkedin.com/in/mohd-abdul-ahad-khan-3b4428317
📧 ahadkhan.ai306@gmail.com