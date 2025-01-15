from jinja2 import Template


cars = [{'model': 'Ниссае', 'price': 1000},
        {'model': 'Ауди', 'price': 2000},
        {'model': 'Шкода', 'price': 3000},
        {'model': 'Мерседес', 'price': 4000},
        {'model': 'БМВ', 'price': 5000},
]


tpl = ("Суммарная цена автомобиля {{ cs | sum(attribute='price') }}\n"
       "Максимальная цена автомобиля {{ cs | max(attribute='price') }}")
# a = sum(i['price'] for i in cars)
tm = Template(tpl)
msg = tm.render(cs = cars)
print(msg)
