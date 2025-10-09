from fastapi import FastAPI
from pydantic import BaseModel
import time

app = FastAPI()

# --- Request models ---
class GenerateRequest(BaseModel):
    query: str
    model_version: str = "base"
    top_k: int = 5

class EvalRequest(BaseModel):
    query: str
    models: list[str]  # e.g. ["base", "dpo-v1"]

# --- Endpoints ---
@app.post("/generate")
def generate(req: GenerateRequest):
    start = time.time()
    # --- Stub logic (replace later with RAG+LLM) ---
    answer = f"[{req.model_version}] Stub answer for: {req.query}"
    latency = (time.time() - start) * 1000
    return {
        "answer": answer,
        "citations": [1],  # placeholder
        "latency_ms": latency,
        "tokens_in": 0,
        "tokens_out": 0,
    }

@app.post("/eval/sxs")
def eval_sxs(req: EvalRequest):
    results = {}
    for model in req.models:
        results[model] = f"[{model}] Stub answer for: {req.query}"
    return {"query": req.query, "results": results}
