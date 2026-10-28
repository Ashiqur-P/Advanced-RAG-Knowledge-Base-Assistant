# System Architecture

## Overview

The Advanced RAG Knowledge Base Assistant uses a Retrieval-Augmented Generation (RAG) architecture to answer questions from uploaded documents.

The system has two main workflows:

1. **Document Ingestion:** Extracts text from DOCX documents, generates document embeddings, and stores the resulting chunks in a PostgreSQL database with pgvector.
2. **Document Retrieval and Answer Generation:** Accepts a user's question, retrieves relevant document chunks, and uses Google Gemini to generate an answer with source references.

## Document Ingestion Workflow

1. **Webhook Gateway:** Receives the uploaded DOCX document.
2. **DOCX Extraction API:** Extracts readable text from the Word document.
3. **Compute Document Hash:** Generates a SHA-256 hash for document identification.
4. **Enrich Metadata:** Adds document metadata, including filename, document type, and document ID.
5. **Recursive Character Text Splitter:** Splits the document into manageable text chunks.
6. **Google Gemini Embeddings:** Converts text chunks into vector embeddings.
7. **Postgres PGVector Store:** Stores the chunks, metadata, and embeddings in the `rag_document_vectors` table.

## Retrieval and Answer Generation Workflow

1. **Question Webhook:** Receives the user's question.
2. **Input Validation:** Checks that the question is present and within the permitted length.
3. **Vector Retrieval:** Searches the `rag_document_vectors` table for relevant document chunks.
4. **Context Building:** Combines retrieved chunks and prepares source references.
5. **Google Gemini:** Generates an answer using the retrieved context.
6. **Response Formatting:** Returns the answer and available sources as JSON.

## Technology Stack

- n8n for workflow automation
- Python and FastAPI for DOCX text extraction
- Google Gemini for embeddings and answer generation
- PostgreSQL and pgvector for vector storage and similarity search
- Docker for running local services
- Supabase for hosted PostgreSQL infrastructure

## Document Processing Configuration

- Chunk size: 1,000 characters
- Chunk overlap: 200 characters
- Vector table: `rag_document_vectors`
- Document format: DOCX

## Reliability

The retrieval workflow validates incoming questions, handles retrieval or generation errors, and provides a fallback response when relevant document context is unavailable.

## Security Considerations

- Keep API keys and database passwords out of source control.
- Configure credentials securely in n8n.
- Do not publish private documents or sensitive information in the repository.
