def del_row(filename, data, index):
    output = open(filename, 'w', encoding='UTF-8')
    output.write('')
    output.close()
    output = open(filename, 'a',encoding='UTF-8')
    
    i=0
    for row in data:
        if i != index:
            output.write(','.join(row))
        else:
            item = ','.join(row)
        i+=1
    output.close()
    return item