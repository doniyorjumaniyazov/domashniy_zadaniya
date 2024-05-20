from data_create import name_data, surename_data, phone_data, adress_data

def input_data():
    name = name_data()
    surename = surename_data()
    phone = phone_data()
    adress = adress_data()
    var = int(input(f"в каком формате записать данные?\n\n"
    f"1 вариант: \n"
    f"{name}\n{surename}\n{phone}\n{adress}\n\n"
    f"2 вариант: \n"
    f"{name};{surename};{phone};{adress}\n"
    f"выберите вариант:"))
    
    while var != 1 and var != 2:
        print("неправилный ввод")
        var = int(input('введите число: '))
        
    if var == 1:
        with open('data_first_version.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surename}\n{phone}\n{adress}\n\n")
    elif var ==2:
        with open('data_second_version.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surename};{phone};{adress}\n")    
    
    
def print_data():
    print('вывожу из 1 вариатна файл: \n')
    with open('data_first_version.csv', 'r', encoding='utf-8') as f:
         data_first = f.readlines()   
         data_first_list = []
         j = 0
         for i in range(len(data_first)):
             if data_first[i] == '\n' or i == len(data_first) - 1:
                 data_first_list.append(''.join(data_first[j:i+1]))
                 j = i
                 
         print(''.join(data_first_list))
        
    print('вывожу из 2 вариатна файл: \n')
    with open('data_second_version.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)
        
        
def update_data():
    filename = input("Введите название файла: ")
    search_term = input("Введите имя или фамилию для поиска: ")
    
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.readlines()
    
    if filename == 'data_first_version.csv':
        j = 0
        records = []
        for i in range(len(data)):
            if data[i] == '\n' or i == len(data) - 1:
                records.append(data[j:i+1])
                j = i
        record_found = False
        for record in records:
            if search_term in record:
                print("Найдена запись:\n", ''.join(record))
                name = input("Введите новое имя: ")
                surename = input("Введите новую фамилию: ")
                phone = input("Введите новый телефон: ")
                adress = input("Введите новый адрес: ")
                new_record = f"{name}\n{surename}\n{phone}\n{adress}\n\n"
                records[records.index(record)] = new_record
                record_found = True
                break
        if not record_found:
            print("Запись не найдена.")
        else:
            with open(filename, 'w', encoding='utf-8') as f:
                for record in records:
                    f.write(''.join(record))
    elif filename == 'data_second_version.csv':
        record_found = False
        for i in range(len(data)):
            if search_term in data[i]:
                print("Найдена запись:", data[i])
                name = input("Введите новое имя: ")
                surename = input("Введите новую фамилию: ")
                phone = input("Введите новый телефон: ")
                adress = input("Введите новый адрес: ")
                data[i] = f"{name};{surename};{phone};{adress}\n"
                record_found = True
                break
        if not record_found:
            print("Запись не найдена.")
        else:
            with open(filename, 'w', encoding='utf-8') as f:
                f.writelines(data)
                  
                  
def delete_data():
    filename = input("Введите название файла: ")
    search_term = input("Введите имя или фамилию для поиска: ")
    
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.readlines()
    
    if filename == 'data_first_version.csv':
        j = 0
        records = []
        for i in range(len(data)):
            if data[i] == '\n' or i == len(data) - 1:
                records.append(data[j:i+1])
                j = i
        record_found = False
        for record in records:
            if search_term in record:
                print("Найдена запись:\n", ''.join(record))
                records.remove(record)
                record_found = True
                break
        if not record_found:
            print("Запись не найдена.")
        else:
            with open(filename, 'w', encoding='utf-8') as f:
                for record in records:
                    f.write(''.join(record))
    elif filename == 'data_second_version.csv':
        record_found = False
        for i in range(len(data)):
            if search_term in data[i]:
                print("Найдена запись:", data[i])
                data.pop(i)
                record_found = True
                break
        if not record_found:
            print("Запись не найдена.")
        else:
            with open(filename, 'w', encoding='utf-8') as f:
                f.writelines(data)

input_data()
print_data()
update_data()
delete_data()