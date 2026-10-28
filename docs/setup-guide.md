# Setup Guide

This guide explains the basic setup for the Advanced RAG Knowledge Base Assistant.

## Prerequisites

Install or prepare the following:

- Docker Desktop
- n8n
- Python 3.10 or later
- Required Python packages
- A Google Gemini API key
- A Supabase project with PostgreSQL and pgvector support
- Postman or another HTTP client for testing

## 1. Start n8n

If n8n is not already running, start it using Docker:

```bash
docker start n8n
```

Open the n8n interface:

```text
http://localhost:5678
```

## 2. Install Python Dependencies

Open a terminal in the project directory and install the packages required by the DOCX extraction API:

```bash
python -m pip install fastapi uvicorn python-multipart python-docx
```

## 3. Start the DOCX Extraction API

From the project directory, run:

```bash
python -m uvicorn docx_extraction_api:app --host 0.0.0.0 --port 8000
```

Check the health endpoint:

```text
http://localhost:8000/health
```

Expected response:

```json
{
  "status": "ok",
  "service": "DOCX Text Extraction API"
}
```

## 4. Configure Credentials

Configure the Google Gemini and PostgreSQL credentials in n8n.

The document ingestion workflow uses the DOCX extraction endpoint:

```text
http://host.docker.internal:8000/extract-docx
```

Ensure that the database table and vector dimensions match the embedding configuration used by the workflow.

## 5. Import the Workflows

Import the workflow JSON files from the `workflow/` directory into n8n:

- `01-document-ingestion-v4.json`
- `02-document-retrieval-v1.json`

Review the imported nodes and select the appropriate credentials before running them.

## 6. Test the API

Use Postman to send a multipart/form-data POST request to the ingestion webhook with a DOCX file.

For question answering, send a JSON POST request to the retrieval webhook with a `question` field.

Use the actual webhook URLs displayed by n8n. Test URLs and production URLs are different.

## Security Notes

- Never commit real API keys, passwords, or private documents to Git.
- Keep local secrets in environment files excluded by `.gitignore`.
- Configure credentials inside n8n after importing workflows.
- Use only documents you have permission to process.

## Troubleshooting

- If the DOCX API cannot be reached, confirm that the API is running and that Docker can access the host through `host.docker.internal`.
- If retrieval returns no results, verify that document ingestion completed and that the vector store contains the expected records.
- If workflow nodes show credential errors after import, select the correct credentials in n8n.
