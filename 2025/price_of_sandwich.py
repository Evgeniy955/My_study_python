from tkinter.font import names
ingredients = {
    'cucumber': 0.5,
    'tomato': 0.7,
    'cheese': 1.2,
    'bread': 0.3,
    'ham': 1.5,
    'egg': 0.8,
    'lettuce': 0.4,
    'onion': 0.6,
    'pepper': 0.9,
    'avocado': 1.0,
    'bacon': 1.8,
}
sandwich_price = []

def price_calculator(name: str):
    def inner(func):
        def wrapper(*args, **kwargs):
            if **kwargs in ingredients:
                sandwich_price.append(ingredients[name] * ingredients[name])
            return result
        return wrapper

    return inner



@price_calculator
def make_sandwich(*ingredients: str) -> str:
    return f"There is a sandwich with: {', '.join(ingredients)}"

if __name__ == '__main__':
    make_sandwich('cucumber=1', 'tomatoes=2', 'slices of cheese=3')