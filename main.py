from fastapi import FastAPI, HTTPException
import random

description = """
Absurd Compliments API helps put you in a better mood whether you appreciate the compliment or 😂 at how
absurd our compliment is.

"A compliment a day keeps the doctor away" by Petr the Motivator
"""

app = FastAPI(
    title="Absurd Compliments API",
    description=description,
    version="11.30.1965",
    openapi_tags=[
        {
            "name": "compliments",
            "description": "Hear a compliment",
        }
    ]
)

compliments = [
    {
        "compliment": "Your computer must be so powerful that I bet it runs C++ code in 1 second!",
        "category": "STEM",
        "level": 8,
        "short": True
    },
]


@app.get("/compliment/random", tags=["compliments"])
async def get_random_compliment():
    return {"compliment": random.choice([x["compliment"] for x in compliments])}
    

@app.get("/compliment/{id}", tags=["compliments"])
async def get_compliment_by_id(id: int):
    if id >= len(compliments):
        raise HTTPException(status_code=404, detail="Invalid ID")
    return {"compliment": compliments[id]["compliment"]}


@app.get("/compliment/", tags=["compliments"])
async def get_list_of_filtered_compliments(category: str | None = None, level: int | None = None, short: bool | None = None):
    categorySet = {x["compliment"] for x in compliments}
    levelSet = {x["compliment"] for x in compliments}
    shortSet = {x["compliment"] for x in compliments}
    for x in compliments:
        if category != None:
            if x["category"] != category:
                categorySet.remove(x["compliment"])
        if level != None:
            if x["level"] != level:
                levelSet.remove(x["compliment"])
        if short != None:
            if x["short"] != short:
                shortSet.remove(x["compliment"])
    return {"compliments": categorySet.intersection(levelSet).intersection(shortSet)}