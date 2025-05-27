# 🧑‍🤝‍🦊 Human-Animal Classifier

A simple yet educational **Streamlit machine learning web application** that classifies an entity as either a **Human** or an **Animal** based on physical and intelligence features. This project uses a small sample dataset and trains a **Random Forest Classifier** to make predictions.

---

## 📌 Project Overview

This web app demonstrates a beginner-friendly approach to building and deploying a machine learning model using Streamlit. It takes three inputs:
- Height (in cm)
- Weight (in kg)
- Intelligence Level (1–10)

Based on these, the app classifies the input as either a **Human** or an **Animal** using a trained model.

---

## 🧠 Features

- ✅ Simple and interactive **Streamlit UI**
- ✅ Uses **Random Forest Classifier**
- ✅ **Sidebar sliders** for input
- ✅ Displays **prediction result**
- ✅ Shows **sample dataset table**

---

## 🔧 Tech Stack

- Python 3.x
- Streamlit
- Pandas
- scikit-learn (RandomForestClassifier)

---

## 📦 Installation & Setup

1. **Clone the repository:**

```bash
git clone https://github.com/aryan-Patel-web/Human-Animal-Classifier.git
cd Human-Animal-Classifier


Install required packages:

pip install -r requirements.txt

If requirements.txt is not available, install manually:


pip install streamlit pandas scikit-learn

▶️ How to Run

streamlit run ML_project.py
Then, open your browser at:
📍 http://localhost:8501

📊 Sample Dataset
Height (cm)	Weight (kg)	Intelligence Level	Category
160	60	8	Human
170	70	9	Human
180	80	10	Human
50	10	2	Animal
60	20	3	Animal
