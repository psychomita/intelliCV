import streamlit as st
import pickle
import docx
import PyPDF2
import re
from huggingface_hub import hf_hub_download

st.set_page_config(page_title="IntelliCV", page_icon=":memo:", layout="centered")

# Cache model loading
@st.cache_resource
def load_models():
    repo_id = "psychomita/intellicv-models"
    clf_path = hf_hub_download(repo_id=repo_id, filename="clf.pkl", repo_type="model")
    tfidf_path = hf_hub_download(repo_id=repo_id, filename="tfidf.pkl", repo_type="model")
    encoder_path = hf_hub_download(repo_id=repo_id, filename="encoder.pkl", repo_type="model")
    return clf_path, tfidf_path, encoder_path

# Load models once
clf_path, tfidf_path, encoder_path = load_models()
svc_model = pickle.load(open(clf_path, 'rb'))
tfidf = pickle.load(open(tfidf_path, 'rb'))
le = pickle.load(open(encoder_path, 'rb'))


def cleanResume(txt):
    cleanText = re.sub('http\S+\s', ' ', txt)
    cleanText = re.sub('RT', ' ', cleanText)
    cleanText = re.sub('#\S+\s', ' ', cleanText)
    cleanText = re.sub('@\S+', '  ', cleanText)
    cleanText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', cleanText)
    cleanText = re.sub(r'[^\x00-\x7f]', ' ', cleanText)
    cleanText = re.sub('\s+', ' ', cleanText)
    return cleanText


def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    return ''.join(page.extract_text() or '' for page in pdf_reader.pages)


def extract_text_from_docx(file):
    doc = docx.Document(file)
    return '\n'.join(paragraph.text for paragraph in doc.paragraphs)


def extract_text_from_txt(file):
    try:
        return file.read().decode('utf-8')
    except UnicodeDecodeError:
        return file.read().decode('latin-1')


def handle_file_upload(uploaded_file):
    file_extension = uploaded_file.name.split('.')[-1].lower()
    if file_extension == 'pdf':
        return extract_text_from_pdf(uploaded_file)
    elif file_extension == 'docx':
        return extract_text_from_docx(uploaded_file)
    elif file_extension == 'txt':
        return extract_text_from_txt(uploaded_file)
    else:
        raise ValueError("Unsupported file type. Please upload a PDF, DOCX, or TXT file.")


def pred(input_resume):
    cleaned_text = cleanResume(input_resume)
    vectorized_text = tfidf.transform([cleaned_text])
    vectorized_text = vectorized_text.toarray()
    predicted_category = svc_model.predict(vectorized_text)
    predicted_category_name = le.inverse_transform(predicted_category)
    return predicted_category_name[0]


# Cache resume processing so checkbox doesn't retrigger prediction
@st.cache_data(show_spinner=False)
def extract_and_predict(uploaded_file):
    resume_text = handle_file_upload(uploaded_file)
    category = pred(resume_text)
    return resume_text, category


def main():
    st.title("IntelliCV: Your AI Resume Analyzer")
    st.markdown("Upload a resume in PDF, TXT, or DOCX format and get the predicted job category.")

    uploaded_file = st.file_uploader("Upload a Resume", type=["pdf", "docx", "txt"])

    if uploaded_file is not None:
        with st.spinner("Processing file and analyzing..."):
            try:
                resume_text, category = extract_and_predict(uploaded_file)
                st.success("✅ Resume processed and analyzed successfully.")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                return

        if st.checkbox("Show extracted text"):
            st.text_area("Extracted Resume Text", resume_text, height=300)

        st.subheader("Predicted Category")
        st.success(f"The predicted category of the uploaded resume is: **{category}**")


if __name__ == "__main__":
    main()