# Twitter API 2to1 transformer

This tool convert the Twitter API v2 format into Twitter API v1.

Before running it, you need to install two dependencies:

```
pip install fastapi
pip install "uvicorn[standard]"
```

Then you can run it with:

```
uvicorn server:app
```

One can add `--port XXXX` to run the tool on a particular port or `--host 0.0.0.0` to make it visible from all network interfaces.

Once the server is running, it accepts a POST request containing the whole JSON in v2 format. The answer will be a converted JSON in v1 format.
