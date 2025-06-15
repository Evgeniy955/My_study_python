

ingredients = {
    'cucumber': 0.5,
    'tomato': 0.7,
    'slices_of_cheese': 1.2,
    'bread': 0.3,
    'ham': 1.5,
    'egg': 0.8,
    'lettuce': 0.4,
    'onion': 0.6,
    'pepper': 0.9,
    'avocado': 1.0,
    'bacon': 1.8,
}

def price_calculator(func):
    def wrapper(**kwargs):
        sandwich_price = 0
        for key, value in kwargs.items():
            if key in ingredients:
                sandwich_price += ingredients[key] * value
        print(f"💰 Общая стоимость сэндвича: {sandwich_price:.2f}$")
        return func(**kwargs)  # ← Вызов оригинальной функции
    return wrapper



@price_calculator
def make_sandwich(**kwargs: any) -> any:
    total_ingredients = []
    for key, value in kwargs.items():
        total_ingredients.append(key+" " + str(value))
    return f"There is a sandwich with: {', '.join(total_ingredients)}"

if __name__ == '__main__':
    print(make_sandwich(cucumber=1, tomato=2, slices_of_cheese=3, bacon=2))