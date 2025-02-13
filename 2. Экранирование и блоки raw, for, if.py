from jinja2 import Template


###########################################################################
data = '''{% raw%}Модуль Jinja вместо
определения {{ name }}
подставляет соответствующее значение{% endraw %}'''

tm = Template(data)   # Представление без преобразования
msg = tm.render(name='Федор')

print(msg, '\n')
###########################################################################


###########################################################################
link = '''В HTML-документе ссылки определяются так:
<a href="#">Ссылка</a>'''

tm = Template("{{ link | e }}")   # Экранирование HTML-текта
msg = tm.render(link=link)

print(msg, '\n')
###########################################################################


###########################################################################
cities = [{'id': 1, 'city': 'Moscow'},
          {'id': 2, 'city': 'Krasnodar'},
          {'id': 3, 'city': 'Rostov'}]

link = '''<select name = 'cities'>
{% for c in cities -%}
{% if c['id'] > 1 -%}
    <option value = "{{ c['id'] }}"> {{ c['city'] }} </option>
{% else -%}
    {{ c['city'] }}
{% endif -%}
{% endfor -%}
</select>'''

tm = Template(link)
msg = tm.render(cities = cities)

print(msg)
###########################################################################

