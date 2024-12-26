# API (Built with FastAPI)

## Restore Dependencies

You can restore dependencies using either `poetry` or `dependencies.txt`.

### Using Poetry
```sh
poetry install
```

### Using requirements.txt
```sh
pip install -r requirements.txt
```

## Start Development Mode

To start the server in dev mode, run:
```sh
uvicorn main:app --host localhost --port 8000 --reload
```

Once the server is running, navigate to [http://localhost:8000/docs](http://localhost:8000/docs) to access the Swagger UI