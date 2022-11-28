# модуль импорта данных

def import_data(data, filename, sep=None):
    with open(filename, 'a+', encoding='UTF-8') as file:
        if sep == None:
            file.write(','.join(data))
            file.write("\n")
        else:
            file.write(sep.join(data))
            file.write("\n")
