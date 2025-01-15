from jinja2 import Template

#   {% %}   - спецификатор шаблона
#   {{ }}   - выражение для вставки контрукций Python в шаблон
#   {# #}   - блок комментариев
#   # ##    - строковый комментарий

name = 'Федор'
age = 28

tm = Template('Мне {{ a }} лет и зовут {{ n }}.')
msg = tm.render(n=name, a=age)

print(msg)
