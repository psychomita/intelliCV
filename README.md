# 📝 IntelliCV – Resume Analyzer App

[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red?logo=streamlit)](https://streamlit.io/)
[![Last Commit](https://img.shields.io/github/last-commit/psychomita/intellicv)](https://github.com/psychomita/intellicv/commits/main)
[![GitHub stars](https://img.shields.io/github/stars/psychomita/intellicv?style=social)](https://github.com/psychomita/intellicv/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/psychomita/intellicv?style=social)](https://github.com/psychomita/intellicv/network/members)
[![GitHub contributors](https://img.shields.io/github/contributors/psychomita/intellicv)](https://github.com/psychomita/intellicv/graphs/contributors)
[![GitHub repo size](https://img.shields.io/github/repo-size/psychomita/intellicv)](https://github.com/psychomita/intellicv)

IntelliCV is a machine learning–powered web application that automatically analyzes your resume or CV. Built using **Streamlit**, it takes input resumes (PDF or DOCX), cleans the text, extracts features using **TF-IDF**, and classifies them using a pre-trained **Support Vector Classifier (SVC)**.

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
|── .gitattributes
|── .gitignore
│
├── data/                     # Raw resumes and training dataset
│   ├── resume_dataset.csv
│
├── notebooks/                # Jupyter notebooks for analysis
    └── Resume_Screening.ipynb
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


*Made with 💚 & 🐍*
