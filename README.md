## ������� Python

### cut_linef.py
������ ����� �� PATH_ORGNS � ����� �� 1� SIZE_CHUNK ����� � ��������� ����� �� ���� PATH_OUT � ��������� PREFIX_FILE.
������������� ������ ��� ������ � ����������� ������ ������� �� ��� ����� ������� ������ 1� ����� �����������

### fix_urls.py
������ ����� �� PATH_URLS � ��������� ����� �����: "www.maple.ru| www.maple.ru/training/courses/" � "http://www.maple.ru", 
"med-complete.ru| oft32.ru" � "http://med-complete.ru" � "http://oft32.ru", ���������� ����� http ���� ������� �� ������� ������.
��������� ��������� � PATH_FIX_URL_OUT

### get_all_www.py
������ ���� json ������ �� ����� �� ���� PATH_ENTRY � ����������� � ���� ���� www.txt (������ �������������� urls)

### jsons_to_json.py
������� ����������� ���������� ������ PATH_JSONS json � ���� ����� PATH_OUT_JSON � ���������������� �������� �� ������� DNS

### transform_ids_to_urls.py
������ �� (PATH_LOG / path_input) ids �������� � ����������� id � url "https://www.dns-shop.ru/pwa/pwa/get-product/?id=" � 
���������� ���������� � ���� (PATH_URLS / path_out)