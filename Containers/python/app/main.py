from fastapi import FastAPI
import os

vers = os.getenv('CODEVERSION')
if not vers:
    vers = "Local"
desc = "Test Python App"

app = FastAPI(title="Container Workshop", description=desc, version=vers)

@app.get("/")
def read_root():
    return {"LucidiaIt": "RocksIT"}