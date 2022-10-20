# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list():
    data = read(csv)
    data = sort_list(data)
    result = filter(data)
    return result


def read(csv):
    data = [item.split(';') for item in csv.split('\n')]
    return data


def sort_list(data):
    return sorted(data, key=lambda x: int(x[1]))


def filter(csv):
    return [item for item in csv if int(item[1]) > 10]


if __name__ == '__main__':
    print(get_users_list())
