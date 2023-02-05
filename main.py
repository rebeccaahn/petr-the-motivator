from fastapi import FastAPI, HTTPException, Path
import random

description = """
Absurd Compliments API helps put you in a better mood whether you appreciate the compliment or 😂 at how
absurd our compliment is.

"*A compliment a day keeps the doctor away*" by Petr the Motivator

Thank you [FastAPI](https://fastapi.tiangolo.com/)!
"""

app = FastAPI(
    title="Absurd Compliments API",
    description=description,
    version="11.30.1965",
    openapi_tags=[
        {
            "name": "compliment",
            "description": "Hear a compliment!",
        }
    ]
)

# List of categories
categories = ["stem", "appearance", "internal"]

# List[dict] of all compliments
compliments = [
    {
        "compliment": "Your computer must be so powerful that I bet it runs C++ code in 1 second!",
        "category": categories[0],
        "level": 8,     # Level of absurdity
        "short": False  # Short: <= 55 characters
    },
    {
        "compliment": "You're so pretty that I bet you can be the hottest celebrity in the whole wide world.",
        "category": categories[1],
        "level": 7,
        "short": False
    },
    {
        "compliment": "You are so big brain that your brain must be the size of a yoga ball!",
        "category": categories[2],
        "level": 9,
        "short": False
    },
    {
        "compliment": "That hat suits you so much that it should be a part of your hairstyle",
        "category": categories[1],
        "level": 6,
        "short": False
    },
    {
        "compliment": "Your heart is as pure as water--clear and fresh",
        "category": categories[2],
        "level": 4,
        "short": True
    },
    {
        "compliment": "Your skin is so clean that I wonder if you're a doll",
        "category": categories[1],
        "level": 5,
        "short": True
    },
    {
        "compliment": "You shine so brightly that I think you must've fallen down from heaven",
        "category": categories[1],
        "level": 8,
        "short": False
    },
    {
        "compliment": "Your passion for coding is so hot that it makes me melt instantly",
        "category": categories[0],
        "level": 9,
        "short": False
    },
]


@app.get("/compliment/random", tags=["compliments"])
async def get_random_compliment():
    return {"compliment": random.choice([comp["compliment"] for comp in compliments])}
    

@app.get("/compliment/{id}", tags=["compliments"])
async def get_compliment_by_id(id: int = Path(title="The compliment's ID", ge=0, lt=len(compliments))):
    return {"compliment": compliments[id]["compliment"]}


@app.get("/compliment/", tags=["compliments"])
async def get_list_of_filtered_compliments(category: str | None = None, level: int | None = None, short: bool | None = None):
    """
    **Available Categories**:
    - stem
    - appearance
    - internal

    **Range of Level**: 1-10 where 1 is the least absurd to 10 is the most absurd
    """
    # Create sets with all possible elements to remove later
    categorySet = {comp["compliment"] for comp in compliments}
    levelSet = {comp["compliment"] for comp in compliments}
    shortSet = {comp["compliment"] for comp in compliments}

    # Remove elements that do not fit the criteria from parameters
    for comp in compliments:
        if category != None:
            if category not in categories:
                raise HTTPException(status_code=404, detail=f"Invalid category. Available categories include {categories}")
            if comp["category"] != category:
                categorySet.remove(comp["compliment"])
        if level != None:
            if level < 1 or level > 10:
                raise HTTPException(status_code=404, detail="Invalid level. Level must be between 1 and 10 inclusive")
            if comp["level"] != level:
                levelSet.remove(comp["compliment"])
        if short != None:
            if comp["short"] != short:
                shortSet.remove(comp["compliment"])

    # Return the intersection of the 3 sets to get only the compliments that fit all 3 criteria
    return {"compliments": categorySet.intersection(levelSet).intersection(shortSet)}