import difflib

# Sample recipe database
recipes = {
    "Spaghetti Bolognese": ["spaghetti", "minced meat", "tomato sauce", "onion", "garlic"],
    "Vegetable Stir Fry": ["broccoli", "carrot", "bell pepper", "soy sauce", "garlic"],
    "Pancakes": ["flour", "milk", "egg", "butter", "sugar"],
    "Chicken Curry": ["chicken", "curry powder", "onion", "tomato", "yogurt"]
}

def recommend_recipes(ingredients):
    matches = {}
    for recipe, required_ingredients in recipes.items():
        match_count = sum(1 for ingredient in required_ingredients if ingredient in ingredients)
        matches[recipe] = match_count / len(required_ingredients)
    
    sorted_matches = sorted(matches.items(), key=lambda x: x[1], reverse=True)
    return [recipe for recipe, score in sorted_matches if score > 0]

# Input
user_ingredients = input("Enter available ingredients (comma-separated): ").lower().split(", ")

recommended = recommend_recipes(user_ingredients)
if recommended:
    print("Recommended Recipes:")
    for recipe in recommended:
        print(f"- {recipe}")
else:
    print("No recipes match your ingredients.")
