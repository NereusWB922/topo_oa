# API (FastAPI)

## Restore Dependencies

You can restore dependencies using either `poetry` or `dependencies.txt`.

### Using requirements.txt

First, create a new virtual environment and activate it:

```sh
python -m venv venv

.\venv\Scripts\activate # (Windows)
source venv/bin/activate # (MacOS / Linux)
```

Install depedencies with requirements.txt
```sh
pip install -r requirements.txt
```

### Using Poetry
```sh
poetry install
```

## Run Unit Tests

Run following command:
```sh
pytest --cov=app tests/
```

## Start Development Mode

To start the server in dev mode, run:
```sh
uvicorn app.main:app --host localhost --port 8000 --reload
```

Once the server is up, navigate to [http://localhost:8000/docs](http://localhost:8000/docs) to access the Swagger UI