# to transfer number in words in RU


def num_to_word(num, kops):
    number = []
    # get number in separate
    while num != 0:
        n = num % 10
        number.append(n)
        num = num // 10

    # dictionaries
    numb_units_dict = {
        0: "", 1: ["один", "одна"], 2: ["два", "две"], 3: "три", 4: "четыре", 5: "пять",
        6: "шесть", 7: "семь", 8: "восемь", 9: "девять", 10: "десять",
        11: "одиннадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать",
        15: "пятнадцать", 16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать"
    }
    numb_dozens_dict = {0: '',
        20: "двадцать", 30: "тридцать", 40: "сорок", 50: "пятьдесят",
        60: "шестьдесят", 70: "семьдесят", 80: "восемьдесят", 90: "девяносто"
    }
    numb_hundreds_dict = {0: '',
        100: "сто", 200: "двести", 300: "триста", 400: "четыреста", 500: "пятьсот",
        600: "шестьсот", 700: "семьсот", 800: "восемьсот", 900: "девятьсот"
    }
    numb_th_mill_dict = {0: "", 1: "",
        2: ["тысяч", "тысяча", "тысячи"], 3: ("миллионов", "миллион", "миллиона"),
        4: ("милиардов", "милиард", "милиарда")
    }
    currency_dict = {
        1: ["рублей", "рубль", "рубля"],
        2: ["копеек", "копейка", "копейки"]
    }

    a, b, s = [], [], []                          # temporary lists for number reversing

    # number splitting and reversing
    if len(number) % 3 != 0:
        for i in range(0, len(number)-len(number) % 3, 3):
            for j in range(3):
                a.append(number[j+i])
            a = a[::-1]
            b.append(a)
            a = []
        n = len(number) % 3
        for i in range(1, n+1):
            a.append(number[-i])
        b.append(a)
        a = []
    else:
        for i in range(0, len(number), 3):
            for j in range(3):
                a.append(number[j+i])
            a = a[::-1]
            b.append(a)
            a = []
    semi_list = b[::-1]                             # as the result - separate list with numbers combined in 3 symbols (further - unit) in nests

                                                    # main algorithm
    for index, semi in enumerate(semi_list):
        print(semi)
        if len(semi_list) == 0:
            print('Nothing to convert')
        elif len(semi_list) == 1:                   # this is for numbers from 0 up to 999
            if len(semi) == 3:                      # from 100 to 999
                if int(semi[2]) > 4 and int(semi[1]) != 1:
                    x = f'{numb_hundreds_dict[semi[0] * 100]} {numb_dozens_dict[semi[1] * 10]} {numb_units_dict[semi[2]]} '
                elif int(semi[2]) == 1 and int(semi[1]) != 1:
                    x = f'{numb_hundreds_dict[semi[0] * 100]} {numb_dozens_dict[semi[1] * 10]} {numb_units_dict[semi[2]][0]} '
                elif int(semi[2]) == 1 and int(semi[1]) == 1:
                    x = f'{numb_hundreds_dict[semi[0] * 100]} {numb_units_dict[semi[1] * 10 + semi[2]]} '
                elif int(semi[2]) == 2:
                    x = f'{numb_hundreds_dict[semi[0] * 100]} {numb_dozens_dict[semi[1] * 10]} {numb_units_dict[semi[2]][0]} '
                elif 2 < int(semi[2]) <= 4:
                    x = f'{numb_hundreds_dict[semi[0] * 100]} {numb_dozens_dict[semi[1] * 10]} {numb_units_dict[semi[2]]} '

                elif int(semi[2]) == 0:
                    x = f'{numb_hundreds_dict[semi[0] * 100]} {numb_dozens_dict[semi[1] * 10]} '
                elif int(semi[1]) == 1 and int(semi[2]) != 0:
                    x = f'{numb_hundreds_dict[semi[0] * 100]} {numb_units_dict[semi[1] * 10 + semi[2]]} '
            elif len(semi) == 2:                    # from 10 to 99
                n = semi[0] * 10 + semi[1]
                if 9 < n < 20:
                    x = f'{numb_units_dict[n]}'
                elif n >= 20:
                    if semi[1] == 1:
                        x = f'{numb_dozens_dict[semi[0] * 10]} {numb_units_dict[semi[1]][0]} '
                    elif semi[1] == 2:
                        x = f'{numb_dozens_dict[semi[0] * 10]} {numb_units_dict[semi[1]][0]} '
                    else:
                        x = f'{numb_dozens_dict[semi[0] * 10]} {numb_units_dict[semi[1]]} '
            elif len(semi) == 1:                    # from 0 to 9
                if semi[0] == 1 or semi[0] == 2:
                    x = f'{numb_units_dict[semi[0]][0]} '
                elif semi[0] > 2:
                    x = f'{numb_units_dict[semi[0]]} '
                elif semi[0] == 0:
                    x = ' '


        elif 1 < len(semi_list) <= 4:               # this is for numbers from 1 000 up to 999 999 999
            if 0 <= index < (len(semi_list) - 1):   # if amount of units in number is up to 999 999 999

                if len(semi) == 3:
                    n = semi[0] * 100 + semi[1] * 10 + semi[2]      # calculating value of unit
                    if n >= 100:                    # for number from 100 to 999
                        if int(semi[2]) == 0 and int(semi[1]) != 1:       # for last number equals to 0,1,2
                            x = f'{numb_hundreds_dict[int(semi[0]) * 100]} {numb_dozens_dict[int(semi[1]) * 10]} {numb_th_mill_dict[len(semi_list) - index][0]}'
                        elif int(semi[2]) == 0 and int(semi[1]) == 1:       # for last number equals to 0,1,2
                            x = f'{numb_hundreds_dict[int(semi[0]) * 100]} {numb_units_dict[int(semi[1]) * 10 + semi[2]]} {numb_th_mill_dict[len(semi_list) - index][0]}'
                        elif int(semi[2]) == 1:     #
                            if (len(semi_list) == 3 and index == 0) or (len(semi_list) == 4 and index <= 1) and semi[1] != 1:
                                x = f'{numb_hundreds_dict[int(semi[0]) * 100]} {numb_dozens_dict[int(semi[1]) * 10]} {numb_units_dict[semi[2]][0]} ' \
                                    f'{numb_th_mill_dict[len(semi_list) - index][1]}'
                            elif (len(semi_list) == 3 and index == 0) or (len(semi_list) == 4 and index <= 1) and semi[1] == 1:
                                x = f'{numb_hundreds_dict[int(semi[0]) * 100]} {numb_units_dict[int(semi[1]) * 10]} {numb_units_dict[semi[2]][0]} ' \
                                    f'{numb_th_mill_dict[len(semi_list) - index][1]}'
                            elif ((len(semi_list) == 3 and index == 1) or (len(semi_list) == 4 and index == 2) or (len(semi_list) == 2 and index == 0)) and int(semi[1]) != 1:
                                x = f'{numb_hundreds_dict[int(semi[0]) * 100]} {numb_dozens_dict[int(semi[1]) * 10]} {numb_units_dict[semi[2]][1]} ' \
                                    f'{numb_th_mill_dict[len(semi_list) - index][1]}'
                            elif (len(semi_list) == 3 and index == 1) or (len(semi_list) == 4 and index == 2) or (len(semi_list) == 2 and index == 0) and int(semi[1]) == 1:
                                x = f'{numb_hundreds_dict[int(semi[0]) * 100]} {numb_units_dict[int(semi[1]) * 10 + semi[2]]} ' \
                                    f'{numb_th_mill_dict[len(semi_list) - index][0]}'
                        elif int(semi[2]) >= 1 and 11 <= (semi[1] * 10 + semi[2]) <= 19:
                            x = f'{numb_hundreds_dict[int(semi[0]) * 100]} {numb_units_dict[int(semi[1]) * 10 + semi[2]]} ' \
                                f'{numb_th_mill_dict[len(semi_list) - index][0]}'
                        elif int(semi[2]) == 2:
                            if (len(semi_list) == 3 and index == 0) or (len(semi_list) == 4 and index <= 1):
                                x = f'{numb_hundreds_dict[int(semi[0]) * 100]} {numb_dozens_dict[int(semi[1]) * 10]} {numb_units_dict[semi[2]][0]} ' \
                                    f'{numb_th_mill_dict[len(semi_list) - index][2]}'
                            elif (len(semi_list) == 3 and index == 1) or (len(semi_list) == 4 and index == 2) or (len(semi_list) == 2 and index == 0):
                                x = f'{numb_hundreds_dict[int(semi[0]) * 100]} {numb_dozens_dict[int(semi[1]) * 10]} {numb_units_dict[semi[2]][1]} ' \
                                    f'{numb_th_mill_dict[len(semi_list) - index][2]}'
                                # for number equals more than 4 in dozens
                        elif int(semi[2]) > 4 and (semi[1] * 10 + semi[2]) > 19 :
                            x = f'{numb_hundreds_dict[int(semi[0]) * 100]} {numb_dozens_dict[int(semi[1]) * 10]} {numb_units_dict[semi[2]]} ' \
                                f'{numb_th_mill_dict[len(semi_list) - index][0]}'
                        elif int(semi[2]) > 4 and (semi[1] * 10 + semi[2]) <= 9 :
                            x = f'{numb_hundreds_dict[int(semi[0]) * 100]} {numb_dozens_dict[int(semi[1]) * 10]} {numb_units_dict[semi[2]]} ' \
                                f'{numb_th_mill_dict[len(semi_list) - index][0]}'
                        elif 2 < int(semi[2]) <= 4 and (semi[1] * 10 + semi[2]) > 19 :
                            x = f'{numb_hundreds_dict[int(semi[0]) * 100]} {numb_dozens_dict[int(semi[1]) * 10]} {numb_units_dict[semi[2]]} ' \
                                f'{numb_th_mill_dict[len(semi_list) - index][2]}'
                        elif 2 < int(semi[2]) <= 4 and (semi[1] * 10 + semi[2]) < 10:
                            x = f'{numb_hundreds_dict[int(semi[0]) * 100]} {numb_dozens_dict[int(semi[1]) * 10]} {numb_units_dict[semi[2]]} ' \
                                f'{numb_th_mill_dict[len(semi_list) - index][2]}'


                        elif int(semi[2]) == 2:
                            if len(semi_list) >= 3:
                                x = f'{numb_hundreds_dict[int(semi[0]) * 100]} {numb_dozens_dict[int(semi[1]) * 10]} {numb_units_dict[semi[2]][0]} ' \
                                    f'{numb_th_mill_dict[len(semi_list) - index][1]}'
                            elif len(semi_list) == 2:
                                x = f'{numb_hundreds_dict[int(semi[0]) * 100]} {numb_dozens_dict[int(semi[1]) * 10]} {numb_units_dict[semi[2]][1]} ' \
                                    f'{numb_th_mill_dict[len(semi_list) - index][2]}'
                    elif n == 0:
                        continue
                    elif 20 <= n <= 99:
                        if int(semi[2]) == 0:
                            x = f'{numb_dozens_dict[int(semi[1]) * 10]} {numb_th_mill_dict[len(semi_list) - index][0]}'
                        elif int(semi[2]) > 4:
                            x = f' {numb_dozens_dict[int(semi[1]) * 10]} {numb_units_dict[semi[2]]} {numb_th_mill_dict[len(semi_list) - index][0]}'
                        elif int(semi[2]) == 1:
                            if len(semi_list) >= 3:
                                x = f'{numb_dozens_dict[int(semi[1]) * 10]} {numb_units_dict[semi[2]][0]} {numb_th_mill_dict[len(semi_list) - index][1]}'
                            elif len(semi_list) == 2:
                                x = f' {numb_dozens_dict[int(semi[1]) * 10]} {numb_units_dict[semi[2]][1]} ' \
                                    f'{numb_th_mill_dict[len(semi_list) - index][1]}'
                        elif int(semi[2]) == 2:
                            if len(semi_list) >= 3:
                                x = f'{numb_hundreds_dict[int(semi[0]) * 100]} {numb_dozens_dict[int(semi[1]) * 10]} {numb_units_dict[semi[2]][0]} ' \
                                    f'{numb_th_mill_dict[len(semi_list) - index][2]}'
                            elif len(semi_list) == 2:
                                x = f'{numb_hundreds_dict[int(semi[0]) * 100]} {numb_dozens_dict[int(semi[1]) * 10]} {numb_units_dict[semi[2]][1]} ' \
                                    f'{numb_th_mill_dict[len(semi_list) - index][2]}'
                        elif 3 <= int(semi[2]) <= 4:
                            x = f'{numb_hundreds_dict[int(semi[0]) * 100]} {numb_dozens_dict[int(semi[1]) * 10]} {numb_units_dict[semi[2]]} ' \
                                f'{numb_th_mill_dict[len(semi_list) - index][2]} {numb_th_mill_dict[len(semi_list) - index][2]}'
                    elif 10 <= n <= 19:
                        x = f'{numb_units_dict[(int(semi[1]) * 10) + int(semi[2])]} {numb_th_mill_dict[len(semi_list) - index][0]}'
                    elif 1 <= n <= 9:
                        if n >= 5:
                            x = f'{numb_units_dict[semi[2]]} {numb_th_mill_dict[len(semi_list) - index][0]}'
                        elif 2 < n <= 4:
                            x = f'{numb_units_dict[semi[2]]} {numb_th_mill_dict[len(semi_list) - index][2]}'
                        elif n == 2:
                            x = f'{numb_units_dict[semi[2]][1]} {numb_th_mill_dict[len(semi_list) - index][2]}'
                        elif n == 1:
                            x = f'{numb_units_dict[semi[2]][1]} {numb_th_mill_dict[len(semi_list) - index][1]}'


                elif len(semi) == 2:
                    n = int(semi[0]) * 10 + int(semi[1])
                    if 9 < n < 20:
                        x = f'{numb_units_dict[n]} {numb_th_mill_dict[len(semi_list) - index][0]}'
                    elif n >= 20:
                        if int(semi[1]) == 1:
                            x = f'{numb_dozens_dict[int(semi[0]) * 10]} {numb_units_dict[semi[1]][1]} {numb_th_mill_dict[len(semi_list) - index][1]}'
                        elif int(semi[1]) == 2:
                            x = f'{numb_dozens_dict[int(semi[0]) * 10]} {numb_units_dict[semi[1]][1]} {numb_th_mill_dict[len(semi_list) - index][2]}'
                        elif int(semi[1]) == 3 or int(semi[1]) == 4:
                            x = f'{numb_dozens_dict[int(semi[0]) * 10]} {numb_units_dict[semi[1]]} {numb_th_mill_dict[len(semi_list) - index][2]}'
                        else:
                            x = f'{numb_dozens_dict[int(semi[0]) * 10]} {numb_units_dict[semi[1]]} {numb_th_mill_dict[len(semi_list) - index][0]}'
                elif len(semi) == 1:
                    if int(semi[0]) == 1:
                        if len(semi_list) >= 3:
                            x = f'{numb_units_dict[semi[0]][0]} {numb_th_mill_dict[len(semi_list) - index][1]}'
                        elif len(semi_list) == 2:
                            x = f'{numb_units_dict[semi[0]][1]} {numb_th_mill_dict[len(semi_list) - index][1]}'
                    elif int(semi[0]) == 2:
                        if len(semi_list) >=3:
                            x = f'{numb_units_dict[semi[0]][0]} {numb_th_mill_dict[len(semi_list) - index][2]}'
                        elif len(semi_list) == 2:
                            x = f'{numb_units_dict[semi[0]][1]} {numb_th_mill_dict[len(semi_list) - index][2]}'
                        elif len(semi_list) == 1:
                            x = f'{numb_units_dict[semi[0]][1]} {numb_th_mill_dict[len(semi_list) - index][2]}'
                    elif 2 < int(semi[0]) <= 4:
                        x = f'{numb_units_dict[semi[0]]} {numb_th_mill_dict[len(semi_list) - index][2]}'
                    elif int(semi[0]) > 4:
                        x = f'{numb_units_dict[semi[0]]} {numb_th_mill_dict[len(semi_list) - index][0]}'

            elif index == (len(semi_list)-1):
                n = int(semi[0]) * 100 + int(semi[1]) * 10 + int(semi[2])
                if n >= 100:
                    if 10 < (int(semi[1])*10 + int(semi[2])) < 20:
                        x = f'{numb_hundreds_dict[int(semi[0]) * 100]} {numb_units_dict[int(semi[1]) * 10 + int(semi[2])]}'
                    elif int(semi[2]) > 4:
                        x = f'{numb_hundreds_dict[int(semi[0]) * 100]} {numb_dozens_dict[int(semi[1]) * 10]} {numb_units_dict[semi[2]]} '
                    elif int(semi[2]) == 1:
                        x = f'{numb_hundreds_dict[int(semi[0]) * 100]} {numb_dozens_dict[int(semi[1]) * 10]} {numb_units_dict[semi[2]][0]} '
                    elif int(semi[2]) == 2:
                        x = f'{numb_hundreds_dict[int(semi[0]) * 100]} {numb_dozens_dict[int(semi[1]) * 10]} {numb_units_dict[semi[2]][0]} '
                    elif 3 <= int(semi[2]) <= 4:
                        x = f'{numb_hundreds_dict[int(semi[0]) * 100]} {numb_dozens_dict[int(semi[1]) * 10]} {numb_units_dict[semi[2]]} '
                    elif int(semi[2]) == 0 and int(semi[1]) != 1:
                        x = f'{numb_hundreds_dict[int(semi[0]) * 100]} {numb_dozens_dict[int(semi[1]) * 10]} {numb_units_dict[semi[2]]}'
                    elif int(semi[2]) == 0 and int(semi[1]) == 1:
                        x = f'{numb_hundreds_dict[int(semi[0]) * 100]} {numb_units_dict[int(semi[1]) * 10 + semi[2]]} '
                elif 10 <= n <= 99:
                    if 10 <= n < 20:
                        x = f'{numb_units_dict[semi[1] * 10 + semi[2]]}'
                    elif n >= 20:
                        if int(semi[2]) == 1 or int(semi[2]) == 2:
                            x = f'{numb_dozens_dict[int(semi[1]) * 10]} {numb_units_dict[semi[2]][0]} '
                        else:
                            x = f'{numb_dozens_dict[int(semi[1]) * 10]} {numb_units_dict[semi[2]]} '
                elif 1 <= n <= 9:
                    if int(semi[2]) == 1:
                        x = f'{numb_units_dict[semi[2]][0]} '
                    elif int(semi[2]) == 2:
                        x = f'{numb_units_dict[semi[2]][1]} '
                    else:
                        x = f'{numb_units_dict[semi[2]]} '
                elif n == 0:
                    x = ' '
            # composing number in words from dictionaries
        s.append(x.lstrip().rstrip())
        trim = []
        for slovo in s:
            c = list(slovo.split(' '))
            for i in range(len(c)):
                d = str(c[i]).rstrip().lstrip()
                trim.append(d)
            c = []
        semi_result = ' '.join(list(filter(lambda x: x != '', trim))).capitalize()
        semi_result_list = list(semi_result.split(' '))
        for i in range(len(semi_result_list)):
            if semi_result_list[i] == 'тысячи' and semi_result_list[i] == semi_result_list[i-1]: semi_result_list[i] = ''
        # adding currency wording
        if str(semi_result_list[-1]) == 'один':
            semi_result_list.append(str(currency_dict[1][1]))
        elif str(semi_result_list[-1]) == 'два' or str(semi_result_list[-1]) == 'три' or str(semi_result_list[-1]) == 'четыре':
            semi_result_list.append(str(currency_dict[1][2]))
        else:
            semi_result_list.append(str(currency_dict[1][0]))

        # adding koppeks in proccess
        kopeeks = []
        semi_kops = kops
        while semi_kops != 0:
            ld = semi_kops % 10
            kopeeks.append(ld)
            semi_kops = semi_kops // 10
        kopeeks = kopeeks[::-1]
        print(kopeeks)

        if len(kopeeks) != 0 and int(kopeeks[-1]) == 1:
            k = f'{kops} {currency_dict[2][1]}'
        elif len(kopeeks) != 0 and 2 <= int(kopeeks[-1]) <= 4:
            k = f'{kops} {currency_dict[2][2]}'
        elif int(kops) == 0:
            k = f'00 {currency_dict[2][0]}'
        elif len(kopeeks) != 0 and int(kops) >= 5:
            k = f'{kops} {currency_dict[2][0]}'

        result = ' '.join(list(filter(lambda x: x != '', semi_result_list))).capitalize() + ' ' + str(k)

    try:
        return result
    except:
        'ошибка конвертации'





