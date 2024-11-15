from ContentCurator.flask_app.utils import get_data

data = get_data('what is Ai?')
print(type(data))
print(data[0])
