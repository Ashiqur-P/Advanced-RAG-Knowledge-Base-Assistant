# Sample Knowledge Base

## Document Information

- Document ID: SAMPLE-001
- Category: General Knowledge
- Purpose: Demonstrate document ingestion and retrieval in a RAG system.

## Topic 1: Document Processing

Document processing converts information from files into text that a computer system can search and retrieve.

A document ingestion workflow extracts text, adds metadata, divides the text into smaller chunks, generates embeddings, and stores the chunks in a vector database.

## Topic 2: Text Chunking

Text chunking divides a long document into smaller sections. Smaller chunks help a retrieval system identify relevant information for a user's question.

Chunk overlap preserves some text between neighboring chunks. This can help maintain context when an important explanation spans a chunk boundary.

In this project, the configured chunk size is 1,000 characters, and the overlap is 200 characters.

## Topic 3: Vector Embeddings

Vector embeddings represent text as numerical vectors. Text with related meanings may have similar vector representations.

The system uses Google Gemini embeddings to convert document chunks and user questions into vectors for semantic retrieval.

## Topic 4: Vector Database

A vector database stores embeddings and associated information. The project uses PostgreSQL with pgvector to store document chunks, metadata, and embeddings.

The configured vector table is named `rag_document_vectors`.

## Topic 5: Retrieval-Augmented Generation

Retrieval-Augmented Generation, or RAG, combines information retrieval with language-model generation.

The system first retrieves relevant document chunks. It then supplies those chunks to a language model to generate an answer grounded in the available information.

## Sample Questions

1. What is document ingestion?
2. Why is text chunking useful?
3. What is the configured chunk size?
4. Which database extension supports vector storage?
5. What are the main stages of a RAG workflow?

## Expected Answers

- Document ingestion extracts, processes, and stores document content for retrieval.
- Text chunking divides long documents into smaller searchable sections.
- The configured chunk size is 1,000 characters, with 200 characters of overlap.
- The project uses pgvector with PostgreSQL.
- A typical RAG workflow retrieves relevant context and uses it to generate a grounded answer.
