import sys

# Функция для создания нового словаря книги
def create_book(author, title, publisher, year, pages, copies):
    return {"author": author, "title": title, "publisher": publisher, "year": year, "pages": pages, "copies": copies}

# Функция для создания нового словаря библиотеки
def create_library():
    return {"books": []}

# Функция для добавления книги в библиотеку
def add_book(library, book):
    library["books"].append(book)

# Функция для удаления книги из библиотеки
def remove_book(library, book):
    library["books"].remove(book)

# Словарь для перевода английских слов на русский
translation_dict = {
    "author": "Автор",
    "title": "Название книги",
    "publisher": "Издательство",
    "year": "Год выпуска",
    "pages": "Количество страниц",
    "copies": "Количество экземпляров"
}

# Функция для вывода всех книг в списке книг библиотеки
def print_books(library):
    for book in library["books"]:
        print(", ".join(f"{translation_dict[key]}: {value}" for key, value in book.items()))

# Функция для сортировки списка книг библиотеки по ключу
def sort_books(library, key):
    library["books"].sort(key=key)

# Определение функции для создания кучи по автору
def heapify_by_author(arr, n, i):
    # Начальная позиция наибольшего элемента считается корнем
    largest = i
    # Позиции левого и правого дочерних элементов
    left = 2 * i + 1
    right = 2 * i + 2

    # Если левый дочерний элемент больше корня, то он становится новым корнем
    if left < n and arr[i]["author"] < arr[left]["author"]:
        largest = left

    # Если правый дочерний элемент больше корня, то он становится новым корнем
    if right < n and arr[largest]["author"] < arr[right]["author"]:
        largest = right

    # Если наибольший элемент не является корнем, то меняем его местами с корнем и рекурсивно вызываем функцию для нового корня
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_by_author(arr, n, largest)

# Определение функции для сортировки массива по автору с помощью кучи
def heapsort_by_author(arr):
    # Размер массива
    n = len(arr)
    # Создание кучи из всех элементов
    for i in range(n, -1, -1):
        heapify_by_author(arr, n, i)

    # Извлечение минимального элемента из кучи и помещение его на конец отсортированной части массива
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify_by_author(arr, i, 0)

# Определение функции full_list, которая принимает словарь библиотеки в качестве аргумента
def full_list(library):
    # Извлечение списка книг из словаря библиотеки
    books = library["books"]
    # Сортировка списка книг по автору с помощью функции heapsort_by_author
    heapsort_by_author(books)
    # Возвращение отсортированного списка книг
    return books

# Функция для преобразования массива в кучу по издателю и заголовку
def heapify_by_publisher_and_title(arr, n, i):
    # Инициализируем переменную largest как индекс i
    largest = i
    # Вычисляем индексы левого и правого дочерних элементов
    left = 2 * i + 1
    right = 2 * i + 2

    # Сначала сортируем по издателю
    # Если индекс левого элемента меньше длины массива и пара (издатель, заголовок) текущего элемента меньше, чем у левого элемента, то обновляем largest
    if left < n and (arr[i]["publisher"], arr[i]["title"]) > (arr[left]["publisher"], arr[left]["title"]):
        largest = left

    # Аналогично, если индекс правого элемента меньше длины массива и пара (издатель, заголовок) наибольшего элемента меньше, чем у правого элемента, то обновляем largest
    if right < n and (arr[largest]["publisher"], arr[largest]["title"]) > (arr[right]["publisher"], arr[right]["title"]):
        largest = right

    # Если наибольший элемент не является текущим элементом
    if largest != i:
        # Меняем местами текущий элемент и наибольший элемент
        arr[i], arr[largest] = arr[largest], arr[i]
        # Рекурсивно вызываем heapify_by_publisher_and_title для нового наибольшего элемента
        heapify_by_publisher_and_title(arr, n, largest)

# Функция для сортировки массива с помощью алгоритма сортировки кучей по издателю и заголовку
def heapsort_by_publisher_and_title(arr):
    # Получаем длину массива
    n = len(arr)

    # Преобразуем массив в кучу
    for i in range(n, -1, -1):
        heapify_by_publisher_and_title(arr, n, i)

    # Сортируем массив
    for i in range(n-1, 0, -1):
        # Меняем местами первый и последний элементы
        arr[i], arr[0] = arr[0], arr[i]
        # Преобразуем оставшуюся часть массива в кучу
        heapify_by_publisher_and_title(arr, i, 0)

# Определение функции author_books, которая принимает две переменные: библиотеку и автора
def author_books(library, author):
    # Создание списка книг, написанных данным автором
    books = [book for book in library["books"] if book["author"] == author]
    # Сортировка списка книг по издателю и названию
    heapsort_by_publisher_and_title(books)
    # Возвращение отсортированного списка книг
    return books

# Функция для получения книг в определенном году
def heapify_by_year_and_author(arr, n, i):
    # Инициализация переменных для хранения индекса наибольшего элемента и его левого и правого детей
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Сначала сравниваем годы выпуска
    if left < n and (arr[i]["year"], arr[i]["author"]) > (arr[left]["year"], arr[left]["author"]):
        largest = left

    # Затем сравниваем автора, если годы выпуска равны
    if right < n and (arr[largest]["year"], arr[largest]["author"]) > (arr[right]["year"], arr[right]["author"]):
        largest = right

    # Если год выпуска и автор совпадают, то сравниваем автора
    if largest < len(arr) and arr[i]["year"] == arr[largest]["year"] and arr[i]["author"] > arr[largest]["author"]:
        largest = i

    # Если найден новый наибольший элемент, то меняем местами этот элемент и текущий элемент
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Рекурсивно применяем процесс к поддереву, корнем которого является новый наибольший элемент
        heapify_by_year_and_author(arr, n, largest)

def heapsort_by_year_and_author(arr):
    # Получаем длину массива
    n = len(arr)

    # Преобразуем массив в кучу
    for i in range(n, -1, -1):
        heapify_by_year_and_author(arr, n, i)

    # Сортируем массив, начиная с конца
    for i in range(n-1, 0, -1):
        # Меняем местами первый и последний элементы массива
        arr[i], arr[0] = arr[0], arr[i]
        # Применяем процесс heapify к оставшейся части массива
        heapify_by_year_and_author(arr, i, 0)

# Определение функции year_books
def year_books(library, start, end):
    # Создание списка книг, которые были опубликованы в заданный период
    books = [book for book in library["books"] if start <= book["year"] <= end]
    # Сортировка списка книг по году и автору
    heapsort_by_year_and_author(books)
    # Возвращение отсортированного списка книг
    return books

# Определение функции для добавления новой книги в файл
def add_book_to_file(book):
    # Открытие файла 'books.txt' в режиме добавления
    with open('books.txt', 'a') as file:
        # Запись информации о книге в файл
        file.write(", ".join(str(value) for value in book.values()) + "\n")

# Определение функции для удаления книги из файла
def remove_book_from_file(book):
    # Создание пустого списка строк
    lines = []
    # Открытие файла для чтения и сохранение его содержимого в списке строк
    with open('books.txt', 'r') as file:
        lines = file.readlines()
        
    # Открытие того же файла для записи
    with open('books.txt', 'w') as file:
        # Перебор всех строк в списке
        for line in lines:
            # Если строка не соответствует данным о книге, она записывается в файл
            if line.strip() != ", ".join(str(value) for value in book.values()):
                file.write(line)

# Определение функции для изменения данных книги в файле
def change_book_in_file(old_book, new_book):
    # Создание пустого списка строк
    lines = []
    # Открытие файла для чтения и сохранение его содержимого в списке строк
    with open('books.txt', 'r') as file:
        lines = file.readlines()
        
    # Открытие того же файла для записи
    with open('books.txt', 'w') as file:
        # Перебор всех строк в списке
        for line in lines:
            # Если строка соответствует данным о старой книге, она заменяется на данные новой книги
            if line.strip() == ", ".join(str(value) for value in old_book.values()):
                file.write(", ".join(str(value) for value in new_book.values()) + "\n")
            # Если строка не соответствует данным ни одной из книг, она остается без изменений
            else:
                file.write(line)
               
def main():
    # Создаем новую библиотеку
    library = create_library()

   # Открываем файл с данными о книгах
    with open('books.txt', 'r') as file:
       # Читаем каждую строку в файле
        for line in file:
           # Разделяем строку на поля
            fields = line.strip().split(',')
           # Проверяем, есть ли хотя бы шесть полей
            if len(fields) >= 6:
               # Извлекаем данные из полей
                author, title, publisher, year, pages, copies = fields[0], fields[1], fields[2], int(fields[3]), int(fields[4]), int(fields[5])
               # Создаем новый объект книги
                book = create_book(author, title, publisher, year, pages, copies)
               # Добавляем книгу в библиотеку
                add_book(library, book)
           # Если меньше шести полей, выводим предупреждающее сообщение
            else:
                print(f"Пропущена строка: '{line.strip()}'. Она содержит меньше шести полей.")


    # Приветственное сообщение
    print("Добро пожаловать в Библиотеку!")
    # Основной цикл для взаимодействия с пользователем
    while True:
        # Выводим опции меню
        print("\nМеню:")
        print("1. Показать полный список книг")
        print("2. Показать книги определенного автора")
        print("3. Показать книги, выпущенные в период с N1 до N2 года")
        print("4. Добавить новую информацию в библиотеку")
        print("5. Удалить информацию из библиотеки")
        print("6. Изменить определённую информацию в библиотеке")
        print("7. Выход")

        # Получаем выбор пользователя
        choice = input("Выберите нужный для себя пункт: ")

        # Обрабатываем выбор пользователя
        if choice == "1":
            full_list(library)
            print_books(library)

        elif choice == "2":
        # Запрашиваем имя автора
            author = input("Введите имя автора: ")
            # Получаем книги этого автора
            books = author_books(library, author)
            # Если такой автора нет в библиотеке, выводим сообщение
            if not books:
                print("К сожалению, этого автора нет в библиотеке")
            # Иначе выводим книги
            else:
                for book in books:
                    print(", ".join(f"{translation_dict[key]}: {value}" for key, value in book.items()))

        # Если пользователь выбрал опцию 3
        elif choice == "3":
            # Запрашиваем у пользователя начальный год периода
            start = int(input("Введите начало периода (год): "))
            # Запрашиваем у пользователя конечный год периода
            end = int(input("Введите конец периода (год): "))
            # Извлекаем книги из библиотеки за указанный период времени
            books = year_books(library, start, end)
            # Если книги за этот период не найдены
            if not books:
                # Выводим сообщение о том, что книги не найдены
                print("Не найдено ни одной книги из этого периода")
            else:
                # Перебираем все найденные книги и выводим их на экран
                for book in books:
                    print(", ".join(f"{translation_dict[key]}: {value}" for key, value in book.items()))
        
        elif choice == "4":
            # Запрашиваем данные новой книги
            author = input("Введите имя автора: ")
            title = input("Введите название книги: ")
            publisher = input("Введите издательство: ")
            year = int(input("Введите год выпуска: "))
            pages = int(input("Введите количество страниц: "))
            copies = int(input("Введите количество экземпляров: "))
            # Создаем новый объект книги
            book = create_book(author, title, publisher, year, pages, copies)
            # Добавляем книгу в файл
            add_book_to_file(book)

        elif choice == "5":
            # Запрашиваем данные книги для удаления
            author = input("Введите имя автора: ")
            title = input("Введите название книги: ")
            publisher = input("Введите издательство: ")
            year = int(input("Введите год выпуска: "))
            pages = int(input("Введите количество страниц: "))
            copies = int(input("Введите количество экземпляров: "))
            # Создаем объект книги для удаления
            book = create_book(author, title, publisher, year, pages, copies)
            # Удаляем книгу из файла
            remove_book_from_file(book)

        elif choice == "6":
            # Запрашиваем данные книги для изменения
            author = input("Введите имя автора: ")
            title = input("Введите название книги: ")
            publisher = input("Введите издательство: ")
            year = int(input("Введите год выпуска: "))
            pages = int(input("Введите количество страниц: "))
            copies = int(input("Введите количество экземпляров: "))
            # Создаем объект книги для изменения
            old_book = create_book(author, title, publisher, year, pages, copies)
            # Запрашиваем новые данные для книги
            author = input("Введите новое имя автора: ")
            title = input("Введите новое название книги: ")
            publisher = input("Введите новое издательство: ")
            year = int(input("Введите новый год выпуска: "))
            pages = int(input("Введите новое количество страниц: "))
            copies = int(input("Введите новое количество экземпляров: "))
            # Создаем новый объект книги с обновленными данными
            new_book = create_book(author, title, publisher, year, pages, copies)
            # Изменяем книгу в файле
            change_book_in_file(old_book, new_book)
            
        # Если пользователь выбрал опцию 4
        elif choice == "7":
            # Благодарим пользователя за использование библиотеки
            print("Спасибо за использование Библиотеки, будем ждать Вас снова!")
            # Завершаем выполнение программы
            sys.exit()
            
        # Если пользователь ввел что-то другое
        else:
            # Информируем пользователя о том, что его ввод был некорректным
            print("Некорректный ввод. Пожалуйста, убедитесь, что Вы ввели число из меню (оно прописано слева).")

# Проверяем, запущен ли скрипт напрямую
if __name__ == "__main__":
    # Вызываем функцию main
    main()