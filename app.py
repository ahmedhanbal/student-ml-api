from datetime import datetime, timezone
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

VERSION_FILE = Path(__file__).resolve().parent / "VERSION"


def read_version() -> str:
    return VERSION_FILE.read_text(encoding="utf-8").strip()


APP_VERSION = read_version()
MODEL_VERSION = "model-1"

app = FastAPI(title="student-ml-api", version=APP_VERSION)


class PredictRequest(BaseModel):
    value: float = Field(..., description="Numeric input used for prediction")


class PredictResponse(BaseModel):
    input: float
    prediction: float


class HealthResponse(BaseModel):
    status: str
    application: str
    version: str | None = None
    application_version: str | None = None
    model_version: str | None = None


def predict_value(value: float) -> float:
    return value * 2


@app.get("/health", response_model=HealthResponse, response_model_exclude_none=True)
def health() -> HealthResponse:
    payload: dict[str, str] = {
        "status": "healthy",
        "application": "student-ml-api",
        "application_version": "1.1.0",
        "model_version": "model-1"
    }
    return HealthResponse(**payload)


@app.post("/predict", response_model=PredictResponse)
def predict(body: PredictRequest) -> PredictResponse:
    try:
        prediction = predict_value(body.value)
    except Exception as exc:  # pragma: no cover - defensive
        raise HTTPException(status_code=400, detail="Invalid input") from exc
    return PredictResponse(input=body.value, prediction=prediction)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=False)
