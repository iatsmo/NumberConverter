# In The Name Of God
# Python Programming Project Number One
# Sina Mokhtarvand , 4001830275
import math
zero = 'صفر'
andd = 'و'
negetive = 'منفی'
numbers=[['','یک','دو','سه','چهار','پنج','شش','هفت','هشت','نه',],
        ['ده','یازده','دوازده','سیزده','چهارده','پانزده','شانزده','هفده','هجده','نوزده'],
        ['بیست','بیست و یک','بیست و دو','بیست و سه','بیست و چهار','بیست و پنج','بیست و شش','بیست و هفت','بیست و هشت','بیست و نه'],
        ['سی','سی و یک','سی و دو','سی و سه','سی و چهار','سی و پنج','سی و شش','سی و هفت','سی و هشت','سی و نه'],
        ['چهل','چهل و یک','چهل و دو','چهل و سه','چهل و چهار','چهل و پنج','چهل و شش','چهل و هفت','چهل و هشت','چهل و نه'],
        ['پنجاه','پنجاه و یک','پنجاه و دو','پنجاه و سه','پنجاه و چهار','پنجاه و پنج','پنجاه و شش','پنجاه و هفت','پنجاه و هشت','پنجاه و نه'],
        ['شصت','شصت و یک','شصت و دو','شصت و سه','شصت و چهار','شصت و پنج','شصت و شش','شصت و هفت','شصت و هشت','شصت و نه'],
        ['هفتاد','هفتاد و یک','هفتاد و دو','هفتاد و سه','هفتاد و چهار','هفتاد و پنج','هفتاد و شش','هفتاد و هفت','هفتاد و هشت','هفتاد و نه'],
        ['هشتاد','هشتاد و یک','هشتاد و دو','هشتاد و سه','هشتاد و چهار','هشتاد و پنج','هشتاد و شش','هشتاد و هفت','هشتاد و هشت','هشتاد و نه'],
        ['نود', 'نود و یک', 'نود و دو', 'نود و سه', 'نود و چهار', 'نود و پنج', 'نود و شش', 'نود و هفت','نود و هشت', 'نود و نه']]
hundreds = ['', 'صد', 'دويست', 'سيصد', 'چهارصد', 'پانصد', 'ششصد', 'هفتصد', 'هشتصد', 'نهصد']
big_numbers = [' ', 'هزار', 'میلیون', 'بیلیون', 'تریلیون', 'کوآدریلیون', 'کوینتیلیون', 'سکستیلیون', 'سپتیلیون', 'اکتیلیون', 'نانیلیون', 'دسیلیون', 'آندسیلیون', 'دیودسیلیون', 'تریدسیلیون', 'کواتیوردسیلیون', 'کویندسیلیون', 'سکسدسیلیون', 'سپتدسیلیون', 'اکتودسیلیون', 'نومدسیلیون']
import math
while True:
    number = str(input('Please inter your own number(YOUR NUMBER MUST BE BETWEEN -(10**60) AND 10**60 ):'))
    if number == '0':
        print(zero)
    if number[0] == '-':
        print(negetive, end=' ')
        number = number.lstrip('-')
    count = 0
    for char in number:
        count += 1
    if count % 3 == 1:
        number = number.rjust(count+2, '0')
    elif count % 3 == 2:
        number = number.rjust(count+1, '0')
    newnum = number[3:]
    a = list(number)
    d = math.ceil(len(a)/3)
    c = []
    list = []
    for i in range(d):
        b = len(a)
        c = a[b - 3:b]
        del a[b - 3:b]
        list.append(c)
    list.reverse()
    g = 0
    for x in list:
        lst_int = [hundreds[int(x[0])], '' if int(x[0]) == 0 or int(x[1]) == int(x[2]) == 0 else andd, numbers[int(x[1])][int(x[2])], '' if int(x[0]) == int(x[1]) == int(x[2]) == 0 else big_numbers[len(list) - 1 - g]]
        if lst_int.count('') == 4:
            del lst_int
        else:
            for z in lst_int:
                print(z, end=' ')
        lst_int = [hundreds[int(x[0])], '' if int(x[0]) == 0 or int(x[1]) == int(x[2]) == 0 else andd,numbers[int(x[1])][int(x[2])],'' if int(x[0]) == int(x[1]) == int(x[2]) == 0 else big_numbers[len(list) - 1 - g]]
        if g != len(list)-1:
            if lst_int.count('') != 4:
                print('' if newnum.count('0') == len(newnum) else andd, end='')
        else:
            continue
        g += 1
