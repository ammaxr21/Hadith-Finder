# Hadith RAG + DPO (Local LLM)

This project is a local-first RAG (Retrieval-Augmented Generation) system over hadith, with optional DPO (Direct Preference Optimization) fine-tuning to make the model:

- **Use the provided hadith context faithfully**
- **Avoid hallucinating new hadith or rulings**
- **Answer conservatively and include a disclaimer**

Everything runs **locally** using:

- A small quantized LLM (Gemma 3 1B Q4_0)
- A dense retriever based on `BAAI/bge-small-en-v1.5`
- FAISS for vector search
- JSONL files for data (no SQL in the MVP)

---

## 🔧 Core Model & Inference Specs

**LLM (generator)**

- **Model:** Gemma 3 1B (instruct variant)
- **Format:** Q4_0 (4-bit quantized)
- **Role:** Answer user questions using retrieved hadith context
- **Inference config:**
  - **Quantization:** 4-bit
  - **Max context tokens:** 1000 (prompt + hadith context + question)
  - **Max answer tokens:** 128 (`max_new_tokens = 128`)
  - **Temperature:** `0.1` (low randomness, conservative answers)

**Embedding model (retriever)**

- **Model:** `BAAI/bge-small-en-v1.5`
- **Dimensionality:** 384-d vectors
- **Role:** Encode hadith and user queries into a shared vector space for semantic search
- **Index:** FAISS `IndexFlatIP` over L2-normalized embeddings (dense vector search)

---

## Repository Structure

Planned layout (no SQL, file-based only):

```text
dpo-rag-hadith-llm/
  app/            # CLI + FastAPI API
  models/         # LLM loading, quantization, DPO adapters
  rag/            # ingestion, embeddings, FAISS retrieval, RAG prompts
  train/          # DPO training scripts
  eval/           # retrieval & answer evaluation, side-by-side scripts
  config/         # shared config (model names, hyperparams)
  data/
    raw/          # raw hadith dumps from external sources
    processed/    # normalized hadiths.jsonl, rag_pairs.jsonl, eval sets
  indexes/        # FAISS index + metadata
  checkpoints/    # LoRA / DPO adapters for the LLM
  scripts/        # one-off utilities (e.g. converters, sanity checks)
  README.md
  requirements.txt
  .gitignore
