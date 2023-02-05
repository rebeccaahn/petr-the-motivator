import random
from flask import Flask, jsonify, abort
from flask_cors import CORS
import json

description = """
Absurd Compliments API helps put you in a better mood whether you appreciate the compliment or 😂 at how
absurd our compliment is.

"*A compliment a day keeps the doctor away*" by Petr the Motivatr

Thank you [FastAPI](https://fastapi.tiangolo.com/)!
"""
app = Flask(__name__)
CORS(app)

# List of categories
categories = ["stem", "appearance", "internal"]

# List[dict] of all compliments
compliments = [
    {
        "compliment": "Your computer must be so powerful that I bet it runs C++ code in 1 second!",
        "category": categories[0],
        "level": 8,     # Level of absurdity from 1 to 10 where 1 is the least absurd to 10 is the most absurd
        "short": "false"  # Short: <= 55 characters
    },
    {
        "compliment": "You're so pretty that I bet you can be the hottest celebrity in the whole wide world.",
        "category": categories[1],
        "level": 7,
        "short": "false"
    },
    {
        "compliment": "You are so big brain that your brain must be the size of a yoga ball!",
        "category": categories[2],
        "level": 9,
        "short": "false"
    },
    {
        "compliment": "That hat suits you so much that it should be a part of your hairstyle",
        "category": categories[1],
        "level": 6,
        "short": "false"
    },
    {
        "compliment": "Your heart is as pure as water--clear and fresh",
        "category": categories[2],
        "level": 4,
        "short": "true"
    },
    {
        "compliment": "Your skin is so clean that I wonder if you're a doll",
        "category": categories[1],
        "level": 5,
        "short": "true"
    },
    {
        "compliment": "You shine so brightly that I think you must've fallen down from heaven",
        "category": categories[1],
        "level": 8,
        "short": "false"
    },
    {
        "compliment": "Your passion for coding is so hot that it makes me melt instantly",
        "category": categories[0],
        "level": 9,
        "short": "false"
    },
]


@app.route("/")
def index():
    return jsonify({"message": "Welcome to Absurd Compliments API!"})


@app.route("/compliment/random/")
def get_random_compliment():
    return jsonify({"compliment": random.choice([comp["compliment"] for comp in compliments])})
    

@app.route("/compliment/<int:id>/")
def get_compliment_by_id(id):
    if id < 0 or id > len(compliments):
        abort(404, description=f"Invalid ID. Must be between 0 and {len(compliments)} inclusive")
    return jsonify({"compliment": compliments[id]["compliment"]})


# Optional parameters
@app.route("/compliment/", defaults={"category": None, "level": None, "short": None})
@app.route("/compliment/<string:category>/", defaults={"level": None, "short": None})
@app.route("/compliment/<string:category>/<int:level>/", defaults={"short": None})
@app.route("/compliment/<string:category>/<int:level>/<string:short>")
def get_list_of_filtered_compliments(category: str, level: int, short: str):
    # Create sets with all possible elements to remove later
    categorySet = {comp["compliment"] for comp in compliments}
    levelSet = {comp["compliment"] for comp in compliments}
    shortSet = {comp["compliment"] for comp in compliments}

    # Remove elements that do not fit the criteria from parameters
    for comp in compliments:
        if category != None:
            if category not in categories:
                abort(404, description=f"Invalid category. Available categories include {categories}")
            if comp["category"] != category:
                categorySet.remove(comp["compliment"])
        if level != None:
            if level < 1 or level > 10:
                abort(404, description="Invalid level. Level must be between 1 and 10 inclusive")
            if comp["level"] != level:
                levelSet.remove(comp["compliment"])
        if short != None:
            if short != "true" or short != "false":
                abort(404, description="Invalid short. Short must be either true or false")
            if comp["short"] != short:
                shortSet.remove(comp["compliment"])

    # Return the intersection of the 3 sets to get only the compliments that fit all 3 criteria
    return jsonify({"compliments": list(categorySet.intersection(levelSet).intersection(shortSet))})