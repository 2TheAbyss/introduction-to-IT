# def read_numbers(file_path):
#     numbers = []
#     with open(file_path, "r", encoding="utf-8") as file:
#         for line in file:
#             line = line.strip()
#             if line:  # Пропускаем пустые строки, если они есть
#                 numbers.append(float(line))
#     return numbers

def read_numbers(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return [float(x) for x in file.read().split()]
    except FileNotFoundError:
        print(f"Ошибка (FileNotFoundError): файл '{file_path}' не найден.")
        return []
    except ValueError as e:
        print(f"Ошибка (ValueError): файл содержит некорректные данные: {e}")
        return []