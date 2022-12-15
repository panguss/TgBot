import requests
x=[]
all_zp = 0
all_n = 0
#цикл, который скачивает вакансии
for i in range(200):
    # запрос
    url = 'https://api.hh.ru/vacancies'
    #параметры, которые будут добавлены к запросу
    par = {'text': 'Инженер-проектировщик', 'area':'1384','per_page':'10', 'page':i}
    r = requests.get(url, params=par)
    e=r.json()
    x.append(e)
for j in x:
    y = j['items']
    #объявляем переменную n для подсчета, количества итераций цикла перебирающего зарплаты в вакансиях
    n=0
    #объявляем переменную sum_zp для подсчета, суммы зарплат в вакансиях
    sum_zp=0
    #цикл, переберает объекты, т.е перебирает вакансии
    for i in y:
        # проверяем есть ли значения в словаре по ключу salary. Т.е проверяем есть ли в вакансии данные по зарплате
        if i['salary'] !=None:
            #записываем значение в переменную s
            s=i['salary']
            # проверяем есть ли значения по ключу from. Т.е проверяем есть ли в вакансии данные по минимальной зп
            if s['from'] !=None:
                # считаем количество обработанных вакансий в которых указана минимальная ЗП
                n+=1
                #получаем минимальную ЗП по ключу from
                s['from']
                #считаем сумму ЗП по вакансиям
                sum_zp +=s['from']
    #добавляем сумму зп по итерации цикла
    all_zp +=sum_zp
    #добавляем сумму n по итерации цикла
    all_n +=n
    #считаем среднюю ЗП
av_zp=all_zp/all_n
print(av_zp)
print(all_n)
