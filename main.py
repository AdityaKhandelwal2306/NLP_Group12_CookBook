from parser import fetch_recipe
from recipe import Recipe
from chatbot import start_conversation
def main():
    url = input("To inititate the cookbook chat please enter the recipe URL: ")
    recipe_data = fetch_recipe(url)
    recipe = Recipe(recipe_data)
    start_conversation(recipe)

if __name__ == "__main__":
    main()
