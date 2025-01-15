from jinja2 import Environment, FileSystemLoader


file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tmp = env.get_template('page.html')
msg = tmp.render(domain='proga.org', title='Моя прога')

print(msg)



