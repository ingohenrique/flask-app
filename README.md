Flask Sample App

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

## Docker

```bash
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```
