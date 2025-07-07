import functools

pizza_ingredients = {
    "cheese": 2.0,
    "pepperoni": 2.3,
    "mushrooms": 1.5,
    "olives": 1.0,
    "onions": 0.8,
    "green_peppers": 1.0,
    "bacon": 3.1,
    "pineapple": 1.8
}


def price_calculator(func):
    @functools.wraps(func)
    def wrapper(*args):
        price = 0
        new_ingredients = []
        for ingredient in args:
            try:
                price += pizza_ingredients[ingredient.lower()]
            except KeyError:
                new_ingredients = [ingredient for ingredient in args if ingredient in pizza_ingredients]
                print(f"Ingredient '{ingredient}' not found in the menu.")
        print("Price: ", price)
        return func(*new_ingredients)
    return wrapper


@price_calculator
def make_sandwich(*ingredients):
    return f"There is a sandwich with: {', '.join(ingredients)}"

if __name__ == "__main__":
    print(make_sandwich("Cheese", "pepperoni", "earth", "mushrooms", "olives", "paper"))
