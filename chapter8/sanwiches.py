def make_sandwich(*items):
    print("I will make sandwich for you")
    for item in items:
        print(".... adding", item, "to your sandwich.")
    print("Your sandwich is ready")

make_sandwich('roast beef', 'corn', 'egg', 'tomato')
make_sandwich('potato', 'tomato', 'egg')