
# Day 5 â€” RAG Evaluation Report

**Project:** Advanced RAG Knowledge Base Assistant
**Evaluation Date:** 2026-11-07
**Status:** 13 Evaluation Tests Completed

## 1. Evaluation Summary

| Metric | Result |
|---|---:|
| Total Tests | 13 |
| Answerable Tests Passed | 10/10 |
| Unanswerable Tests Passed | 3/3 |
| Total Tests Passed | 13/13 |
| Observed Hallucinated Answers | 0 |

Note: These results represent the 13 tested questions only. They do not establish 100% overall RAG accuracy.

## 2. Technical Configuration

| Component | Verified Configuration |
|---|---|
| Embedding Model | gemini-embedding-001 |
| Embedding Dimensions | 3072 |
| Chat Model | gemini-3-flash-preview |
| Vector Table | rag_document_vectors |
| Total Stored Chunks | 195 |
| Chunk Size | 1000 |
| Chunk Overlap | 200 |
| Document Format | DOCX |
| Source Document | à¦¬à¦¾à¦‚à¦²à¦¾à¦¦à§‡à¦¶ à¦“ à¦¬à¦¿à¦¶à§à¦¬ à¦ªà¦°à¦¿à¦šà§Ÿ à¦à¦¬à¦‚ à¦¬à¦¿à¦œà§à¦žà¦¾à¦¨ .docx |
| Document Hash | d961733c5a67cc2501f913f233ec1bd420dc1bf2e3f56ccdafc57deedf6c6d93 |

### Retry Configuration

Google Gemini Chat Model:

- Retry On Fail: ON
- Max Tries: 4
- Wait Between Tries: 4000 ms
- On Error: Continue (using error output)

## 3. Evaluation Results

### Answerable Questions

| Test | Category | Result | Observation |
|---|---|---|---|
| 1 | Direct factual â€” Broad | PASS | Bengali answer grounded in the uploaded document with sources. |
| 2 | Direct factual â€” Specific figures | PASS | Correct rates: 2001 = 1.58%, 2011 = 1.46%, 2022 = 1.22%. |
| 3 | Direct factual | PASS | Correctly explained the benefits of smaller families. |
| 4 | Direct factual | PASS | Correctly identified the declining population growth trend. |
| 5 | Combined question | PASS | Explained declining growth rate, increasing population density, and agricultural land impacts. |
| 6 | Combined question | PASS | Explained small-family benefits and problems caused by overpopulation. |
| 7 | Paraphrased Bengali | PASS | Correctly answered a rephrased question about quality of life in smaller families. |
| 8 | Paraphrased Bengali | PASS | Correctly explained the population growth trend using census statistics. |
| 9 | English cross-language | PASS | Answered in English using Bengali document content and correct figures. |
| 10 | English cross-language | PASS | Explained transport, education, healthcare, employment, and housing problems in English. |

### Unanswerable Questions

| Test | Category | Result | Observation |
|---|---|---|---|
| 11 | Irrelevant general knowledge | PASS | Did not guess the national flower; stated that the document did not contain the answer. |
| 12 | Related but missing information | PASS | Did not guess the current population; correctly stated that the document only contains growth-rate information. |
| 13 | Word-match trap | PASS | Did not invent information about Bangladesh's national cricket team. |

## 4. Source and Retrieval Observations

- All 13 responses returned the expected DOCX filename and matching document hash.
- Relevant source chunks were retrieved for answerable questions.
- Some responses included additional chunks that were not directly relevant to the question.
- Unanswerable questions were handled without generating unsupported factual answers.
- Citation references appeared in answers, but citation-number-to-source-chunk mapping has not been independently verified.
- Some abstention responses still included citations to irrelevant chunks.

## 5. Provider Availability Issue

The original retrieval Chat Model was configured as:

`gemini-3.8-flash`

During evaluation, requests returned:

`503 Service Unavailable â€” model is currently experiencing high demand.`

The Chat Model was changed to:

`gemini-3-flash-preview`

The new model successfully generated the subsequent tested answers.

This was recorded as a model availability issue, not as a verified workflow logic failure.

## 6. SHA256 Configuration Verification

The ingestion workflow's `Compute Document Hash` node was inspected.

Configuration:

- Action: Hash
- Type: SHA256
- Value: `={{ $json.text }}`

The existing DOCX document hash is:

`d961733c5a67cc2501f913f233ec1bd420dc1bf2e3f56ccdafc57deedf6c6d93`

**Verification Status: CONFIGURATION VERIFIED**

The Compute Document Hash node configuration was inspected and verified as SHA256 using the input expression `={{ $json.text }}`. The existing document hash was recorded during the verified ingestion process.

A fresh standalone SHA256 execution was not performed during this evaluation because the upstream Webhook had no input data. No unnecessary document re-ingestion was performed.

## 7. Known Limitations

1. Retrieval sometimes returns less relevant chunks alongside relevant chunks.
2. Citation-number-to-source-chunk mapping has not been independently verified.
3. Some unanswerable responses include citations to irrelevant retrieved chunks.
4. The exact Bengali fallback response has not been separately verified.
5. A fresh standalone SHA256 execution was not performed during this evaluation; the existing ingestion hash and node configuration were verified.
6. The 13-question evaluation is a limited test set and does not establish overall production accuracy.

## 8. Final Evaluation

The RAG workflow passed all 13 manually tested evaluation questions.

It demonstrated:

- Bengali question answering.
- English question answering using Bengali source documents.
- Direct factual retrieval.
- Combined question answering.
- Paraphrased question handling.
- Abstention when requested information was unavailable.
- Source document and hash consistency.

Further improvements may be considered for retrieval relevance and citation quality, but no workflow configuration changes were made as part of this baseline evaluation.

**Day 5 Evaluation Status: COMPLETED**
