# rag-based-docs-assistant

A Retrieval-Augmented Generation (RAG) powered assistant that allows you to **ask natural language questions** over your own documents (PDF, DOCX, TXT). It retrieves relevant content from the documents using semantic search and then uses a language model to generate contextual answers.

<p align="center">
  <img src="https://img.shields.io/badge/LLM-GPT2-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/VectorDB-Chroma-green?style=flat-square"/>
  <img src="https://img.shields.io/badge/Embeddings-MiniLM-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/Framework-LangChain-informational?style=flat-square"/>
</p>

---

## 🚀 Features

- 🔍 Semantic search over your documents using vector embeddings.
- 💬 Natural language question-answering using a local LLM (GPT-2 for now).
- 📄 Supports multiple file formats like PDF (more coming soon).
- 🛠️ Modular and extensible codebase (add your own model or UI).
- 💻 CLI interface (Streamlit UI coming soon).

---

## 🧱 Tech Stack

| Component        | Tool/Library                             |
|------------------|-------------------------------------------|
| LLM              | GPT-2 (via HuggingFace Transformers)     |
| Embeddings       | `all-MiniLM-L6-v2` via `sentence-transformers` |
| Vector DB        | ChromaDB                                 |
| Framework        | LangChain                                |
| PDF Parser       | pdfplumber                               |
| Interface        | CLI (Streamlit planned)                  |
| Language         | Python                                   |

---

## 📂 Project Structure

