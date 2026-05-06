# 🚀 Embedding & Semantic Similarity Query

This project demonstrates how to perform **Semantic Similarity Search** using modern AI embeddings. Unlike traditional keyword search, this approach understands the context and meaning of the text.

## 🛠️ Technology Stack
- **Framework**: [LangChain](https://www.langchain.com/)
- **Embedding Model**: [Google Gemini](https://ai.google.dev/models/gemini) (`models/embedding-001`)
- **Mathematics**: [NumPy](https://numpy.org/) for Cosine Similarity calculations.
- **Environment**: `python-dotenv` for secure API key management.

## 🌟 Key Features
- **Semantic Vectorization**: Converts raw text into 768-dimensional vectors.
- **Query vs. Document Comparison**: Compare a user query against a list of documents to find the most relevant match.
- **Mathematical Accuracy**: Implements Cosine Similarity to measure the distance between text meanings.

## 🚀 How to Run
1. Ensure your `.env` file contains a valid `GOOGLE_API_KEY`.
2. Run the script:
   ```bash
   python Embedding_query
   ```

## 📈 Use Cases
This is a foundational building block for:
- **Retrieval Augmented Generation (RAG)**
- **Semantic Search Engines**
- **Recommendation Systems**
- **Clustering and Data Analysis**
