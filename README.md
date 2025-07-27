# Resume PDF RAG Assistant

This project is a **Resume PDF RAG Assistant** that enables candidates to interactively analyze their own resumes and allows hiring managers to extract detailed information about candidates from PDF resumes. Using Retrieval-Augmented Generation (RAG), the app leverages [Ollama](https://ollama.com/) for local LLM inference, [LangChain](https://python.langchain.com/) for document processing and retrieval, and [Streamlit](https://streamlit.io/) for a user-friendly web interface.

---

## Features

- **For Candidates:** Instantly gauge your resume, identify strengths, and get feedback by asking questions about your own resume.
- **For Hiring Managers:** Quickly extract and query detailed information about candidates from their PDF resumes.
- **RAG Pipeline:** Combines document retrieval and LLM generation for accurate, context-aware answers.
- **Multi-Query Retrieval:** Improves search relevance by generating multiple query variants.
- **Streamlit UI:** Simple web interface for interactive Q&A.

---

## Requirements

- Python 3.8+
- [Ollama](https://ollama.com/) installed and running locally
- The following Python packages:
  - streamlit
  - langchain-community
  - langchain
  - langchain-ollama
  - langchain-core
  - langchain-text-splitters
  - chromadb
  - unstructured
  - pypdf (optional, for alternative PDF loaders)
  - ollama

Install all dependencies with:

```bash
pip install streamlit langchain-community langchain langchain-ollama langchain-core langchain-text-splitters chromadb unstructured pypdf ollama
```

---

## Steps to Run This Project

1. **Clone the Repository**  
   Download or clone this repository to your local machine.

2. **Set Up Python Environment**  
   It is recommended to use a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**  
   Install all required Python packages:
   ```bash
   pip install streamlit langchain-community langchain langchain-ollama langchain-core langchain-text-splitters chromadb unstructured pypdf ollama
   ```

4. **Start Ollama**  
   Make sure Ollama is installed and running locally. Pull the required models:
   ```bash
   ollama pull llama3.2
   ollama pull nomic-embed-text
   ```

5. **Add Your Resume PDF**  
   Place your resume PDF file in the `data/` directory. Update the `DOC_PATH` variable in `pdf-rag.py` if your file name is different.

6. **Run the Streamlit App**  
   Start the app using Streamlit:
   ```bash
   streamlit run pdf-rag.py
   ```

7. **Interact with the App**  
   Open the local URL provided by Streamlit in your browser. Enter your questions to analyze your resume or extract candidate details.

---

## File Structure

```
Ollama Project/
├── data/
│   └── Your-Resume.pdf
├── chroma_db/
├── pdf-rag.py
└── README.md
```

---

## Troubleshooting

- **ModuleNotFoundError:**  
  Ensure all required packages are installed in your active Python environment.
- **PDF Extraction Fails:**  
  If your PDF is image-based, try running OCR on it before using this app.
- **Ollama Model Not Found:**  
  Make sure you have pulled the required models with `ollama pull`.

---

## License

MIT License