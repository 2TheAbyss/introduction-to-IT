import json
import logging
from utils.statistics import calculate_average, find_max, find_min ,validate_numbers
from utils.reader import read_numbers
from pathlib import Path
#numbers = [12, 5, 8, 19, 3, 24, 7]

def main():
    with open("config.json", "r", encoding="utf-8") as file:
        config = json.load(file)
    log_file = Path(config["log_file"])
    logs_dir = log_file.parent
    logs_dir.mkdir(exist_ok=True)
    
    logging.basicConfig(
        filename="logs/app.log",    
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        encoding="utf-8",
    )
    
    logging.info("Запуск программы")
    current_dir = Path.cwd()
    print(f"Текущий каталог: {current_dir}")
    
    data_file = Path(config["input_file"])
    
    print(f"Каталог {logs_dir} проверен/создан.")
    
    if not data_file.exists():
        error_msg = f"Файл {data_file} не найден!"
        print(f"Ошибка: {error_msg}")
        logging.error(error_msg)
        logging.info("Завершение программы")
        return 
    
    print(f"Файл {data_file} успешно найден.")

    numbers = read_numbers(data_file)
    logging.info(f"Успешное чтение файла {data_file}")
    logging.info(f"Количество прочитанных значений: {len(numbers)}")
    if not numbers:
        print("Обработка прервана: список измерений пуст.")
        return
    try:
        validate_numbers(numbers)
    except ValueError as error:
        print(f"Ошибка валидации данных: {error}")
        logging.error(f"Ошибка валидации данных: {error}")
        logging.info("Завершение программы")
        return
    print(f"Количество значений: {len(numbers)}")
    print(f"Минимум: {find_min(numbers)}")
    print(f"Максимум: {find_max(numbers)}")
    print(f"Среднее значение: {calculate_average(numbers)}")
    logging.info(
      "Завершение программы"
    )
if __name__ == "__main__":
    main()
