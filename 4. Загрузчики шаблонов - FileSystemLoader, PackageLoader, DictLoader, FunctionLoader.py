from jinja2 import Environment, FileSystemLoader, FunctionLoader, PackageLoader, DictLoader, PrefixLoader, ChoiceLoader, \
    ModuleLoader


# PackageLoader - для загрузки шаблонов из пакетов
# DictLoader - для загрузки шаюлонов из словаря
# FunctionLoader - для загрузки на основе функции
# PrefixLoader - загрузчик, использующий словарь для построения подкаталогов
# ChoiceLoader - загрузчик, содержащий список других загрузчиков
# ModuleLoader - загрузчик для скомпилированных шаблонов


###########################################################################
persons = [{'name': 'Павел', 'old': 25},
           {'name': 'Настя', 'old': 17},
           {'name': 'Иван', 'old': 35}
           ]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)   # Готов загружать шаблоны

tm = env.get_template('main.html')   # Template
msg = tm.render(users=persons)

print(msg)
###########################################################################


###########################################################################
def loadTpl(path):
    if path == 'index':
        return '''Имя {{ u.name }}, возраст {{ u.old }}'''
    else:
        return '''Данные: {{ u }}'''

func_loader = FunctionLoader(loadTpl)
env = Environment(loader=func_loader)

tm = env.get_template('index')
msg = tm.render(u = persons[0])

print(msg)
###########################################################################
