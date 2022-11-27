# модуль экспорта данных
import os.path
def export_data(filename):
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='UTF-8') as file:
            data = []
            t = []
            for line in file:
                if ',' in line:
                    temp = line.strip().split(',')
                    data.append(temp)
                elif ';' in line:
                    temp = line.strip().split(';')
                    data.append(temp)
                elif ':' in line:
                    temp = line.strip().split(':')
                    data.append(temp)
                elif ' ' in line:
                    temp = line.strip().split(' ')
                    data.append(temp)
                elif line != '':
                    if line != '\n':
                        t.append(line.strip())
                    else:
                        data.append(t)
                        t = []
        return data
    else:
        return None
