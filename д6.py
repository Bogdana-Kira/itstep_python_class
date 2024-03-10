result = []

def divider(a, b):
    if a < b:
        raise ValueError("a should be greater than or equal to b")
    if b > 100:
        raise IndexError("b should be less than or equal to 100")
    if b == 0:
        raise ZeroDivisionError("division by zero is not allowed")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, "invalid_key": 15, 8: 4}

for key, value in data.items():
    try:
        res = divider(key, value)
        result.append(res)
    except (ValueError, IndexError, ZeroDivisionError) as e:
        print(f"Error: {e}")

print(result)