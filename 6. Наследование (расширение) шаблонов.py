from jinja2 import Environment, FileSystemLoader


# {% block <имя блока> %}
# {% endblock %}

subs = ['Русский', "Английский", "Немецкий"]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tmp = env.get_template('edit_about.html')
msg = tmp.render(list_table = subs)

print(msg)



