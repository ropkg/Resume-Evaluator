# Resume-Evaluator

This Python script extracts information such as name, email, and skills from a PDF resume using spaCy for natural language processing.

## Prerequisites

- Python 3
- Install required libraries using the following command:

  ```bash
  pip install spacy PyPDF2
  python -m spacy download en_core_web_sm

  Usage

Clone the repository:
git clone https://github.com/[your-username]/resume-evaluator.git

Navigate to the project folder:
cd resume-evaluator

Replace 'path/to/resume.pdf' in the main function of resume_evaluator.py with the actual path to your PDF resume.

Run the Python script:
python resume_evaluator.py

Output

The script will print extracted information from the PDF resume, including the name, email, and skills.

Note:

The script uses spaCy for named entity recognition (NER) to identify entities like PERSON, EMAIL, and SKILL. Adjustments may be needed based on the specific content and structure of resumes.
This is a basic example, and the effectiveness may vary for different resume formats.
