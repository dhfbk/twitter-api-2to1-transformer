from fastapi import Request, FastAPI
import tweetstransform

app = FastAPI()

@app.post("/")
async def root(request: Request):
    tweetsapi1 = tweetstransform.create_json(await request.json())
    return tweetsapi1
