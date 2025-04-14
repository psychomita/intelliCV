# 📝 IntelliCV – Resume Classifier Web App

IntelliCV is a machine learning–powered web application that automatically classifies resumes into job categories (e.g., Data Science, HR, Software Engineering). Built using **Streamlit**, it takes input resumes (PDF or DOCX), cleans the text, extracts features using **TF-IDF**, and classifies them using a pre-trained **Support Vector Classifier (SVC)**.

## 🚀 Features

- 📄 Supports **PDF** and **DOCX** resume uploads
- 🧹 Preprocesses resumes with custom text cleaning
- 🔍 Uses **TF-IDF Vectorization** for text feature extraction
- 🧠 Predicts job category using trained **SVC model**
- 🌐 Simple, interactive **Streamlit UI**
- 🧰 Easily extendable for more categories or resume analysis features

## 🛠️ Tech Stack

- Python
- Streamlit
- scikit-learn
- PyPDF2
- python-docx
- pickle (for model + encoder serialization)

## 📂 Project Structure

```
📁 intellicv/
│
├── app.py                    # Streamlit app script
├── requirements.txt          # Dependencies for running the app
├── README.md
│
├── data/                     # Raw resumes and training dataset
│   ├── resume_data.csv
│   ├── network_eng_resume.pdf
│   └── health_fitness_resume.pdf
│
├── models/                   # ML models used in prediction
│   ├── clf.pkl               # Trained SVC model
│   ├── tfidf.pkl             # Trained TF-IDF vectorizer
│   └── encoder.pkl           # Label encoder
│
├── notebooks/                # Jupyter notebooks for analysis
    └── Resume Screening.ipynb
```

## 🧪 How to Run Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/intellicv.git
   cd intellicv
   ```

2. **Create a conda or virtual environment (optional but recommended)**

   ```bash
   conda create -n intellicv-env python=3.13
   conda activate intellicv-env
   ```

3. **Install the required packages**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

## 📊 Dataset Used

The model was trained using a labeled dataset of resumes across various job roles. TF-IDF was used for feature extraction, and Support Vector Machine (SVC) was used for classification.

## 🔮 Future Improvements

- Add detailed resume analysis (skills, experience, etc.)
- Visualize prediction confidence and key terms
- Allow batch resume uploads and classification
- Integrate with job recommendation APIs

## 🙌 Acknowledgements

- [Streamlit](https://streamlit.io/)
- [scikit-learn](https://scikit-learn.org/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [python-docx](https://python-docx.readthedocs.io/)

## 🧑‍💻 Author

**Suchismita Bose**


Made with 💚 & 🐍
