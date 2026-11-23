def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def find_min(numbers):
    if not numbers:
        return None
    mn = numbers[0]
    for x in numbers:
        if x < mn:
            mn = x
    return mn


def find_max(numbers):
    if not numbers:
        return None
    mx = numbers[0]
    for x in numbers:
        if x > mx:
            mx = x
    return mx

def validate_numbers(numbers):
    if not numbers:
        raise ValueError("Список измерений пуст")