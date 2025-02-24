
from transformers import pipeline

# Load RoBERTa NER model
ner_pipeline = pipeline("ner", model="xlm-roberta-large-finetuned-conll03-english")

#Define Functions to Extract Information

# Function to extract full name correctly
def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None


# Function to extract email
def extract_email(text):
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    matches = re.findall(email_pattern, text)
    return matches[0] if matches else None

# Function to extract phone number
def extract_phone(text):
    phone_pattern = r"\+?\d[\d\s\-\(\)]{8,14}\d"
    matches = re.findall(phone_pattern, text)
    return matches[0] if matches else None

# Function to parse resume text
def parse_resume(text):
    return {
        "Name": extract_name(text),
        "Email": extract_email(text),
        "Phone": extract_phone(text)
    }

#Test with Sample Resume
resume_text = """
Name: Sujeet Kumar
Data Scientist
Email: data.sujeet@gmail.com
Phone: +91(798) 228-0339
Experience in machine learning and data science...
"""

parsed_data = parse_resume(resume_text)
print(parsed_data)





