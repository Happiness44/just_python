# for 사용하기
def list1():
    li = []
    print(type(li))


# list1()


def list2():
    basket = ["오렌지", "망고", "사과", "파인애플"]
    print(basket)


# list2()


def list3():
    dice = [1, 2, 3, 4, 5, 6]
    print(dice)


# list3()


def list4():
    lotto = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print(lotto)


# list4()


def list5():
    # 트럼프 카드 덱
    spades = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    clubs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    diamonds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    hearts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

    deck = [spades, clubs, diamonds, hearts]
    print(deck)


# list5()


# for loop 연습
# 1부터 10까지 출력해 봅시다.
def for1():
    for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print(n)


# for1()


# 1부터 20까지 출력해 봅시다.
def for2():
    for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
        if n % 10 == 1:
            print()
        print(n, end=" ")


for2()
