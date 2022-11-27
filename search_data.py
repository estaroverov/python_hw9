# модуль поиска контакта

def search_data(word, data):
    if data == None:
        return None
    found = []
    if len(data) > 0:
        for item in data:
            if word in item:
                found.append(item)
        return found
    else:
        return None

def search_val(word, data, column):
    if data == None:
        return None
    found = []
    if len(data) > 0:
        for item in data:
            if item != []  and item[column] == word:
                found.append(item)
        return found
    else:
        return None