# student-ml-api

FastAPI prediction service for MLOPS A1.

## Local run

```bash
pip install -r requirements.txt
python app.py
```

- Health: `GET http://localhost:5000/health`
- Predict: `POST http://localhost:5000/predict` with `{"value": 10}`

## Tests

```bash
pytest -q
```

## Docker

```bash
docker build -t student-ml-api:1.0.0 .
docker run -d --name student-ml-api -p 5000:5000 student-ml-api:1.0.0
```
