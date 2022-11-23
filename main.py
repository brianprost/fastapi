from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Msg(BaseModel):
    msg: str


# define postgres connection
db_vars = {
    # nothing for now :(
}


@app.get("/")
async def root():
    return {"message": "Hello, Chelsea. This is the default landing API. You don't want this..."}


# setup an API endpoint that supplies a platform_item_id, and return the current_item_status, pilot_status, and item_writer
@app.get("/api/v1/item_test/{platform_item_id}")
async def item_details(platform_item_id: int):
    # get from railway items table
    item = await db.fetch_one(query="SELECT * FROM items WHERE platform_item_id = $1", values=[platform_item_id])
    return {"current_item_status": item["current_item_status"], "pilot_status": item["pilot_status"], "item_writer": item["item_writer"]}
