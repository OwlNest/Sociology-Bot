import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from config import questions, keyboards
import ctypes

knownUsers = []

counter_1_male = 0
counter_1_female = 0
counter_1_other = 0

counter_2_1 = 0
counter_2_2 = 0
counter_2_3 = 0
counter_2_4 = 0
counter_2_5 = 0
counter_2_6 = 0
counter_2_other = 0

counter_3_1 = 0
counter_3_2 = 0
counter_3_3 = 0
counter_3_4 = 0
counter_3_5 = 0
counter_3_other = 0


counter_4_yes = 0
counter_4_no = 0
counter_4_other = 0

counter_5_1 = 0
counter_5_2 = 0
counter_5_3 = 0
counter_5_4 = 0
counter_5_5 = 0
counter_5_other = 0

counter_6_1 = 0
counter_6_2 = 0
counter_6_3 = 0
counter_6_4 = 0
counter_6_5 = 0
counter_6_other = 0

counter_7_1 = 0
counter_7_2 = 0
counter_7_3 = 0
counter_7_4 = 0
counter_7_5 = 0
counter_7_other = 0

counter_8_1 = 0
counter_8_2 = 0
counter_8_3 = 0
counter_8_4 = 0
counter_8_5 = 0
counter_8_other = 0

counter_9_1 = 0
counter_9_2 = 0
counter_9_3 = 0
counter_9_4 = 0
counter_9_5 = 0
counter_9_other = 0

counter_10_1 = 0
counter_10_2 = 0
counter_10_3 = 0
counter_10_4 = 0
counter_10_5 = 0
counter_10_other = 0

counter_11_1 = 0
counter_11_2 = 0
counter_11_3 = 0
counter_11_4 = 0
counter_11_5 = 0
counter_11_other = 0

counter_12_1 = 0
counter_12_2 = 0
counter_12_3 = 0
counter_12_4 = 0
counter_12_5 = 0
counter_12_6 = 0
counter_12_other = 0

def plot(data_names, data_values, id):
    dpi = 80
    fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
    mpl.rcParams.update({'font.size': 9})

    plt.title(questions[id])

    xs = range(len(data_names))

    plt.pie(
        data_values, autopct='%.1f proc', radius = 1.1,
        explode = [0.15] + [0 for _ in range(len(data_names) - 1)] )
    plt.legend(
        bbox_to_anchor = (-0.36, 0.45, 0.25, 0.25),
        loc = 'lower left', labels = data_names )
    plt.show()

g = open('users.txt', 'r')
for line in g:
    knownUsers.append(line.split(';')[0])

ctypes.windll.user32.MessageBoxW(0, "Количество проголосовавших: " + str(len(knownUsers)), "Статистика", 1)

i = 0
f = open('base.txt', 'r')
for line in f:
    for i in range (0, 12):
        string = line.split(';')
        newstring = string[i].split(':')

        #print(newstring)

        if newstring[1] == '1':
            if newstring[2] == 'Мужской':
                counter_1_male += 1
            elif newstring[2] == 'Женский':
                counter_1_female += 1
            else:
                counter_1_other +=1  
        if newstring[1] == '2':
            if newstring[2] == '1':
                counter_2_1 += 1
            elif newstring[2] == '2':
                counter_2_2 += 1
            elif newstring[2] == '3':
                counter_2_3 += 1
            elif newstring[2] == '4':
                counter_2_4 += 1
            elif newstring[2] == '5':
                counter_2_5 += 1
            elif newstring[2] == '6':
                counter_2_6 += 1
            else:
                counter_2_other +=1 

        if newstring[1] == '3':
            if newstring[2] == 'Да':
                counter_3_1 += 1
            elif newstring[2] == 'Всё равно/не знаю':
                counter_3_2 += 1
            elif newstring[2] == 'Нет':
                counter_3_3 += 1
            elif newstring[2] == 'Если это не мешает учебе':
                counter_3_4 += 1
            elif newstring[2] == 'Если не преподает у этого студента':
                counter_3_5 += 1
            else:
                counter_3_other +=1 


        if newstring[1] == '4':
            if newstring[2] == 'Да':
                counter_4_yes += 1
            elif newstring[2] == 'Нет':
                counter_4_no += 1
            else:
                counter_4_other +=1  

        if newstring[1] == '5':
            if newstring[2] == 'Да':
                counter_5_1 += 1
            elif newstring[2] == 'Затрудняюсь ответить':
                counter_5_2 += 1
            elif newstring[2] == 'В определенных случаях':
                counter_5_3 += 1
            elif newstring[2] == 'Скорее нет':
                counter_5_4 += 1
            elif newstring[2] == 'Нет, никогда':
                counter_5_5 += 1
            else:
                counter_5_other +=1 

        if newstring[1] == '6':
            if newstring[2] == 'Да':
                counter_6_1 += 1
            elif newstring[2] == 'Затрудняюсь ответить':
                counter_6_2 += 1
            elif newstring[2] == 'В определенных случаях':
                counter_6_3 += 1
            elif newstring[2] == 'Скорее нет':
                counter_6_4 += 1
            elif newstring[2] == 'Нет, никогда':
                counter_6_5 += 1
            else:
                counter_6_other +=1 

        if newstring[1] == '7':
            if newstring[2] == 'Да':
                counter_7_1 += 1
            elif newstring[2] == 'Затрудняюсь ответить':
                counter_7_2 += 1
            elif newstring[2] == 'В определенных случаях':
                counter_7_3 += 1
            elif newstring[2] == 'Скорее нет':
                counter_7_4 += 1
            elif newstring[2] == 'Нет, никогда':
                counter_7_5 += 1
            else:
                counter_7_other +=1 


        if newstring[1] == '8':
            if newstring[2] == 'Да':
                counter_8_1 += 1
            elif newstring[2] == 'Затрудняюсь ответить':
                counter_8_2 += 1
            elif newstring[2] == 'В определенных случаях':
                counter_8_3 += 1
            elif newstring[2] == 'Скорее нет':
                counter_8_4 += 1
            elif newstring[2] == 'Нет, никогда':
                counter_8_5 += 1
            else:
                counter_8_other +=1 

        if newstring[1] == '9':
            if newstring[2] == 'Да':
                counter_9_1 += 1
            elif newstring[2] == 'Затрудняюсь ответить':
                counter_9_2 += 1
            elif newstring[2] == 'В определенных случаях':
                counter_9_3 += 1
            elif newstring[2] == 'Скорее нет':
                counter_9_4 += 1
            elif newstring[2] == 'Нет, никогда':
                counter_9_5 += 1
            else:
                counter_9_other +=1 

        if newstring[1] == '10':
            if newstring[2] == 'Да':
                counter_10_1 += 1
            elif newstring[2] == 'Затрудняюсь ответить':
                counter_10_2 += 1
            elif newstring[2] == 'В определенных случаях':
                counter_10_3 += 1
            elif newstring[2] == 'Скорее нет':
                counter_10_4 += 1
            elif newstring[2] == 'Нет, никогда':
                counter_10_5 += 1
            else:
                counter_10_other +=1 

        if newstring[1] == '11':
            if newstring[2] == 'Сочувствую доценту':
                counter_11_1 += 1
            elif newstring[2] == 'Негативное':
                counter_11_2 += 1
            elif newstring[2] == 'Не слышал':
                counter_11_3 += 1
            elif newstring[2] == 'Все равно':
                counter_11_4 += 1
            else:
                counter_11_other +=1 

        if newstring[1] == '12':
            if newstring[2] == 'Оправдать':
                counter_12_1 += 1
            elif newstring[2] == 'Домашний арест':
                counter_12_2 += 1
            elif newstring[2] == 'Не знаю, не знаком с инцидентом':
                counter_12_3 += 1
            elif newstring[2] == 'Психбольница':
                counter_12_4 += 1
            elif newstring[2] == 'Тюрьма':
                counter_12_5 += 1
            elif newstring[2] == 'Колония-поселение':
                counter_12_6 += 1
            else:
                counter_12_other +=1 

plot(['Мужской', 'Женский', 'Другое'], [counter_1_male, counter_1_female, counter_1_other], 1)
plot(['1', '2', '3', '4', '5', '6', 'Другое'], [counter_2_1, counter_2_2, counter_2_3, counter_2_4, counter_2_5, counter_2_6, counter_2_other], 2)
plot(['Да', 'Все равно\не знаю', 'Нет', 'Если это не мешает учебе', 'Если не преподает у этого студента', 'Другое'], [counter_3_1, counter_3_2, counter_3_3, counter_3_4, counter_3_5, counter_3_other], 3)
plot(['Да', 'Нет', 'Другое'], [counter_4_yes, counter_4_no, counter_4_other], 4)
plot(['Да', 'Затрудняюсь ответить', 'В определенных случаях', 'Скорее нет', 'Нет, никогда', 'Другое'], [counter_5_1, counter_5_2, counter_5_3, counter_5_4, counter_5_5, counter_5_other], 5)
plot(['Да', 'Затрудняюсь ответить', 'В определенных случаях', 'Скорее нет', 'Нет, никогда', 'Другое'], [counter_6_1, counter_6_2, counter_6_3, counter_6_4, counter_6_5, counter_6_other], 6)
plot(['Да', 'Затрудняюсь ответить', 'В определенных случаях', 'Скорее нет', 'Нет, никогда', 'Другое'], [counter_7_1, counter_7_2, counter_7_3, counter_7_4, counter_7_5, counter_7_other], 7)
plot(['Да', 'Затрудняюсь ответить', 'В определенных случаях', 'Скорее нет', 'Нет, никогда', 'Другое'], [counter_8_1, counter_8_2, counter_8_3, counter_8_4, counter_8_5, counter_8_other], 8)
plot(['Да', 'Затрудняюсь ответить', 'В определенных случаях', 'Скорее нет', 'Нет, никогда', 'Другое'], [counter_9_1, counter_9_2, counter_9_3, counter_9_4, counter_9_5, counter_9_other], 9)
plot(['Да', 'Затрудняюсь ответить', 'В определенных случаях', 'Скорее нет', 'Нет, никогда', 'Другое'], [counter_10_1, counter_10_2, counter_10_3, counter_10_4, counter_10_5, counter_10_other], 10)
plot(['Сочувствую доценту', 'Негативное', 'Не слышал', 'Все равно', 'Другое'], [counter_11_1, counter_11_2, counter_11_3, counter_11_4, counter_11_other], 11)
plot(['Оправдать', 'Домашний арест', 'Не знаю, не знаком с инцидентом', 'Психбольница', 'Тюрьма', 'Колония-поселение', 'Другое'], [counter_12_1, counter_12_2, counter_12_3, counter_12_4, counter_12_5, counter_12_6, counter_12_other], 12)