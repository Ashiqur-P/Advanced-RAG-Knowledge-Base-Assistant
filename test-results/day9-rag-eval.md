
## 1. Similarity Threshold Decision

### Baseline Score Analysis

- Answerable questions (Top-3 scores): 0.172956–0.457952
- Unanswerable questions (Top-3 scores): 0.328787–0.540120
- Overlapping range: 0.328787–0.457952

Lower scores indicate better similarity in the current distance-based retrieval metric.

### Decision

No reliable hard similarity threshold was identified because the answerable and unanswerable score ranges overlap significantly.

Therefore:
- No arbitrary similarity threshold was introduced.
- Retrieval filtering was not changed.
- Prompt-based abstention was selected as the improvement approach.
- The assistant must answer only from explicitly supported document context.
- If sufficient supporting information is unavailable, it must return exactly: "আমার কাছে এই তথ্য নেই।"

This is a prompt-based abstention improvement, not a solution to irrelevant retrieval results.


## 2. Evaluation Setup and Baseline

### Dataset and Configuration

- Evaluation date: 2026-11-12
- Source document: বাংলাদেশ ও বিশ্ব পরিচয় এবং বিজ্ঞান .docx
- Document ID: doc_8e29aaea3c73ef1237d82fae0480f78513edcb7bd05f58a40b9e59dbebe97256
- SHA256: 8e29aaea3c73ef1237d82fae0480f78513edcb7bd05f58a40b9e59dbebe97256
- Vector table: rag_document_vectors
- Current indexed chunks: 31
- Embedding model: gemini-embedding-001
- Embedding dimensions: 3072
- Chunk size: 1000
- Chunk overlap: 200
- Generation model: gemini-3-flash-preview
- Evaluation questions: 15 (10 answerable, 5 unanswerable)

Note: This is a separate evaluation dataset from the Day 5 report, which used an earlier document/index version with 195 chunks. The two evaluation reports should not be treated as a direct like-for-like comparison.

### Baseline Results

| Metric | Baseline Result |
|---|---:|
| Answerable questions | 10/10 correct |
| Unanswerable questions | 5/5 semantically abstained |
| Exact Bengali fallback | Not consistently returned |
| Observed hallucinations | 0 |
| Total questions | 15 |

The baseline correctly avoided unsupported answers, but the abstention wording was inconsistent. The Day 9 prompt improvement targets an exact fallback response.

## 3. Question Set and After-test Status

| ID | Question | Expected Result | Baseline | After-test |
|---|---|---|---|---|
| Q1 | ২০২২ সালের আদমশুমারি অনুযায়ী জনসংখ্যা বৃদ্ধির হার কত? | ১.২২% | PASS | PASS |
| Q2 | ২০০১, ২০১১ ও ২০২২ সালের বৃদ্ধির হার কত? | ১.৫৮%, ১.৪৬%, ১.২২% | PASS | PASS |
| Q3 | স্ক্র্যাচ এডিটরের প্রধান তিনটি অংশ কী? | Code Area, Script Area, Stage | PASS | PASS |
| Q4 | বায়ুর জলীয় বাষ্পের পরিমাণকে কী বলে? | আর্দ্রতা | PASS | PASS |
| Q5 | ছোট পরিবারের শিক্ষা, চিকিৎসা ও খাদ্যের সুবিধা কী? | পর্যাপ্ত খাবার, শিক্ষার খরচ, সঠিক চিকিৎসা | PASS | PASS |
| Q6 | অতিরিক্ত জনসংখ্যা কৃষিজমি ও পরিবেশের ক্ষতি করে কীভাবে? | কৃষিজমি হ্রাস, খাদ্য উৎপাদন ও পরিবেশের ক্ষতি | PASS | PASS |
| Q7 | পানির বাষ্প ঠান্ডা হয়ে ফোঁটায় পরিণত হওয়ার প্রক্রিয়া কী? | ঘনীভবন | PASS | PENDING — quota error |
| Q8 | দোকানদার কীভাবে ক্রেতার বিশ্বাস অর্জন করেন? | ন্যায্য দাম ও সঠিক ওজন | PASS | PENDING — not tested |
| Q9 | What are the main stages of the water cycle? | Evaporation, condensation, precipitation | PASS | PENDING — not tested |
| Q10 | Which devices can store digital information? | Computers, phones, pen drives, memory cards, etc. | PASS | PENDING — not tested |
| Q11 | What is the capital of Japan? | Exact fallback | PASS | PASS |
| Q12 | Who invented the telephone? | Exact fallback | PASS | PASS |
| Q13 | ২০২৫ সালে বাংলাদেশের মোট জনসংখ্যা কত? | Exact fallback | PASS | PASS |
| Q14 | বাংলাদেশের বর্তমান সাক্ষরতার হার কত? | Exact fallback | PASS | PASS |
| Q15 | বাংলাদেশের সর্বশেষ জাতীয় নির্বাচনে কোন দল কত আসন পেয়েছে? | Exact fallback | PASS | PASS |

### After-test Summary (Final)

- Completed after-tests: 15/15
- Completed tests passed: 15/15
- Answerable questions passed: 10/10
- Unanswerable questions returned the exact fallback: 5/5
- Observed hallucinations: 0

Q7 initially encountered a Gemini HTTP 429 daily quota error, surfaced as an HTTP 502 workflow response. After the quota reset, the retry succeeded. Q7–Q10 subsequently completed and all four passed.

## 4. After-test Quality Audit

| ID | Answer Correctness | Citation Count vs Sources | Retrieval Relevance | Status |
|---|---|---|---|---|
| Q1 | Correct: 1.22% | 1 citation / 3 sources — mismatch | Some retrieved chunks were unrelated | PASS |
| Q2 | Correct: all three growth rates | 3 citations / 3 sources — count matches; mapping not verified | Some retrieved chunks were unrelated | PASS |
| Q3 | Correct: Code Area, Script Area, Stage | Citation [1] preserved; source mapping not independently verified | No confirmed irrelevant-source finding recorded | PASS |
| Q4 | Correct: আর্দ্রতা | 1 citation / 3 sources — mismatch | Some retrieved chunks were broad or partially relevant | PASS |
| Q5 | Correct: all expected benefits | 3 citations / 3 sources — count matches; mapping not verified | 2 of 3 chunks were irrelevant or partly irrelevant | PASS |
| Q6 | Correct: expected agricultural land and environmental impacts | 2 citations / 3 sources — mismatch | Third retrieved chunk was less relevant | PASS |
| Q7 | Correct: ঘনীভবন (condensation) | 2 citation markers / 3 sources — mismatch | Chunks 1 and 3 relevant; chunk 2 partially relevant | PASS |
| Q8 | Correct: fair price and correct weight | 3 citation markers / 3 sources — count matches; mapping not verified | Chunk 2 directly relevant; chunks 1 and 3 less relevant | PASS |
| Q9 | Correct: evaporation, condensation/cloud formation, precipitation and recirculation; additional ice/snowfall explanation | 3 citation markers / 3 sources — mismatch | Chunks 1 and 3 relevant; chunk 2 less relevant | PASS |
| Q10 | Correct: smartphones, computers/laptops, pen drives, memory cards and hard disks | 1 citation / 3 sources — mismatch | Chunk 1 relevant; chunk 2 partially relevant; chunk 3 irrelevant | PASS |
| Q11 | Exact fallback returned | No citation; 3 retrieved sources | Retrieved chunks did not directly answer the question | PASS |
| Q12 | Exact fallback returned | No citation; 3 retrieved sources | Retrieved chunks did not directly answer the question | PASS |
| Q13 | Exact fallback returned | No citation; 3 retrieved sources | Near-topic chunks existed, but did not contain the requested 2025 figure | PASS |
| Q14 | Exact fallback returned | No citation; 3 retrieved sources | Retrieved chunks did not contain the requested current literacy rate | PASS |
| Q15 | Exact fallback returned | No citation; 3 retrieved sources | Retrieved chunks did not contain the requested election results | PASS |

### Citation and Retrieval Limitations

- Citation count matching the number of returned sources does not independently prove that each citation points to the correct source.
- Citation-to-source mapping was not independently verified.
- Some answerable questions retrieved partially relevant or irrelevant chunks.
- The prompt-based abstention improvement did not eliminate irrelevant retrieval results.
- Unanswerable questions returned the exact Bengali fallback in all five completed after-tests.




