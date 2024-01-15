import spacy
from spacy.matcher import Matcher
import PyPDF2

# Load spaCy model for English
nlp = spacy.load("en_core_web_sm")

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Initialize an empty string to store the text
        text = ''

        # Iterate through pages and extract text
        for page_number in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_number]
            text += page.extract_text()

    return text

def extract_information(text):
    # Process the text using spaCy NLP
    doc = nlp(text)

    # Define spaCy Matcher for custom pattern matching
    matcher = Matcher(nlp.vocab)
    
    # Corrected pattern format
    matcher.add("PERSON", [[{"label": "PERSON"}]])
    matcher.add("EMAIL", [[{"label": "EMAIL"}]])
    matcher.add("SKILL", [[{"label": "SKILL"}]])

    # Extract information (e.g., name, email, skills)
    name = None
    email = None
    skills = []

    matches = matcher(doc)
    for match_id, start, end in matches:
        if doc.vocab.strings[match_id] == "PERSON" and not name:
            name = doc[start:end].text.strip()
        elif doc.vocab.strings[match_id] == "EMAIL" and not email:
            email = doc[start:end].text.strip()
        elif doc.vocab.strings[match_id] == "SKILL":
            skills.append(doc[start:end].text.strip())

    return name, email, skills

def main():
    # Replace 'path/to/resume.pdf' with the actual path to your PDF resume
    resume_path = 'path/to/resume.pdf'

    print(f"Reading PDF from: {resume_path}")

    # Read the PDF resume
    resume_text = read_pdf(resume_path)

    # Print extracted text for debugging
    print("Extracted Text:")
    print(resume_text)

    # Extract information from the resume
    name, email, skills = extract_information(resume_text)

    # Print the extracted information
    print(f"\nName: {name}")
    print(f"Email: {email}")
    print(f"Skills: {', '.join(skills)}")

if __name__ == "__main__":
    main()
