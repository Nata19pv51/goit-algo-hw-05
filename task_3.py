import timeit
from boyer_mure import boyer_moore_search
from knut_morrise_pratt import kmp_search
from rabin_carp import rabin_karp_search

def read_file(name):
    with open(name, 'r', encoding='utf-8') as f:
        text_article = f.read()
    return text_article

def timer_measurement(str, function_name, pattern):
    position = function_name(str, pattern)
    
    # Створюємо словник globals, щоб timeit міг бачити функцію
    setup_globals = {
        'func': function_name,
        'str': str,
        'pattern': pattern
    }
    stmt = "func(str, pattern)"
    number_of_runs = 10
    sort_time = timeit.timeit(
        stmt=stmt, 
        globals=setup_globals,
        number=number_of_runs
    )
    avg_time = round(sort_time / number_of_runs, 6)
    return (avg_time, position)

def display_time(file, pattern):
    boyer_mure = timer_measurement(file, boyer_moore_search, pattern)
    knut_morrise_pratt = timer_measurement(file, kmp_search, pattern)
    rabin_carp = timer_measurement(file, rabin_karp_search, pattern)
    print(f"{str(boyer_mure):<25} | {str(knut_morrise_pratt):<25} | {str(rabin_carp):<25}")


if __name__ == '__main__':
    file1 = read_file("стаття 1.txt")
    file2 = read_file("стаття 2.txt")

    boyer_mure_label =  "Боєра-Мура" 
    knut_morrise_pratt_label =  "Кнута-Морріса-Пратта" 
    rabin_carp_label =  "Рабіна-Карпа"

    print(f"\n{boyer_mure_label:<25} | {knut_morrise_pratt_label:<25} | {rabin_carp_label:<25}")
    print(f"********************************** Стаття 1 *************************************")
    display_time(file1, "використовується для пошуку елементів у відсортованому масиві")
    display_time(file1, "Параметри 1 серії експериментів")
    
    print(f"********************************** Стаття 2 *************************************")
    display_time(file2, "Параметри 1 серії експериментів")
    display_time(file2, "використовується для пошуку елементів у відсортованому масиві")
    print(" ")