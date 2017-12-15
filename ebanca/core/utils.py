from random import randint
from datetime import date, timedelta
from core.models import CreditCard


def generateNumCard():
    prefix = 4
    i_num_card = randint(100000000000000, 999999999999999)
    possible_num_card = str(prefix) + str(i_num_card)

    if CreditCard.objects.filter(num_card=possible_num_card):
        return generateNumCard()

    map_possible_num_card = list(map(int, possible_num_card))
    num_card = []

    for position, num in enumerate(map_possible_num_card):
        if position % 2 == 0:
            doubled_num = num * 2
            if doubled_num > 9:
                str_doubled_num = str(doubled_num)
                new_num = int(str_doubled_num[0]) + int(str_doubled_num[1])
                num_card.append(new_num)
                continue
            num_card.append(doubled_num)
        else:
            num_card.append(num)

    if num_card != []:
        sum_num_card = 0
        for d in num_card:
            sum_num_card = sum_num_card + d
        if sum_num_card % 10 == 0:
            return possible_num_card
        else:
            return generateNumCard()


def generateNumAccount():
    return str(randint(100, 999)) + '-' + str(randint(1000000000, 9999999999))


def generateNumCvv():
    return randint(100, 999)


def generateNumPin():
    return randint(1000, 9999)


def generateExpDate():
    return date.today() + timedelta(randint(round(24 * 365 / 12), round(80 * 365 / 12)))
