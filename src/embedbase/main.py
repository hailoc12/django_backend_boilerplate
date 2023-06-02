# main.py
import os
import typing
import uvicorn
from embedbase import get_app
# we also support postgres, supabase, qdrant, or implement your own
# check an example https://github.com/different-ai/embedbase-qdrant
# from embedbase.database.memory_db import MemoryDatabase
from embedbase.database.postgres_db import Postgres
from embedbase.embedding.openai import OpenAI
import dotenv

dotenv.load_dotenv(".env")
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
print("OPENAI_API_KEY: ", OPENAI_API_KEY)

app = (
    get_app()
    .use_embedder(OpenAI(OPENAI_API_KEY))
    .use_db(Postgres())
    .run()
)

if __name__ == "__main__":
    uvicorn.run(app)
