#plan is to have a db of recipies with score, and ingredients and link to recipe (if one is needed) 
# Should return 2 meal preps and a list of all ingredients needed.

# FUTURE IDEA
# BE able to add items that are discounted to increase the weight of the chances of being selected
import csv
import random
weeklyList = []

class Recipe:
    def __init__(self, id, name, link, rating, ingredients, frequency):
        self.id = id
        self.name = name
        self.link = link
        self.ingredients = ingredients
        self.rating = rating
        self.frequency = frequency

    def __str__(self):
        return f"Recipe Name: {self.name}\nID: {self.id}\nLink: {self.link}\nIngredients: {self.ingredients}\nRating: {self.rating}\nFrequency: {self.frequency}"


def ImportDB():
    file_path = r"Database.csv"
    recipes = {}

    with open(file_path, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip header if your CSV has one
        for row in csv_reader:
            # row = [id, name, ingredients, rating]
            recipe = Recipe(row[0], row[1], row[2], row[3], row[4], row[5])
            recipes[recipe.name] = recipe  # Index by name

    return recipes


def printDB(db):
    for recipe in db.values():
        print(recipe)
        print("_____________________________")

def PrintDBRecipes(db):
    for recipe in db.values():
        print(recipe.name)
        print("_____________________________")



def RandomSelector(db):
    weeklyList = []
    IngredientsList = []
    while len(weeklyList) < 2:
        meal = random.choice(list(db.values()))
        if meal not in weeklyList:
            weeklyList.append(meal)
            IngredientsList.append(meal.ingredients)
    for meal in weeklyList:
        print(meal)
        print("_____________________________")

    print("Ingredients Needed:")
    for ingredients in IngredientsList:
        print(ingredients)


# def MealSelector():
def main():
    db = ImportDB()
    RandomSelector(db)


main()

