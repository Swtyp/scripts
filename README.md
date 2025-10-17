## Скрипты Python

### cut_linef.py
Чтение файла из PATH_ORGNS и вывод по 1к SIZE_CHUNK строк в отдельные файлы по пути PATH_OUT с префиксов PREFIX_FILE.
Промежуточный скрипт для вывода в специальный сервис который за раз может принять только 1к строк организаций

### fix_urls.py
Чтение файла из PATH_URLS и обработка строк ввида: "www.maple.ru| www.maple.ru/training/courses/" в "http://www.maple.ru", 
"med-complete.ru| oft32.ru" в "http://med-complete.ru" и "http://oft32.ru", добавление схемы http если таковой не имеется вообще.
Результат выводится в PATH_FIX_URL_OUT

### get_all_www.py
Чтение всех json файлов из папки по пути PATH_ENTRY и объединение в один файл www.txt (список необработанных urls)

### jsons_to_json.py
Обычное объединение нескольких файлов PATH_JSONS json в один общий PATH_OUT_JSON с характеристиками роутеров из сервиса DNS

### transform_ids_to_urls.py
Чтение из (PATH_LOG / path_input) ids карточек и подстановка id в url "https://www.dns-shop.ru/pwa/pwa/get-product/?id=" и 
дальнейшая сохранение в файл (PATH_URLS / path_out)