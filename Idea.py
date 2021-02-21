from functools import reduce
import os


def shop_cal():
    while True:
        print("----Welcome----")
        print("----ENTER THE PRICE OF ITEMS----")

        n = int(input("ENTER THE TOTAL NUMBER OF ITEMS:"))
        init_list = []
        print("ENTER THE PRICES ONE BY ONE")
        for i in range(1, n + 1):
            init_list.append(float(input()))

        total_list = reduce(lambda x, y: x + y, init_list)
        print("TOTAL AMOUNT OF", n, "ITEMS", total_list)

        last = input("PRESS \'a\' TO ADD MORE ITEMS OR PRESS \'q\' To EXIT:")
        while True:
            if last == "a":
                init_list.append(int(input("ENTER THE PRICE OF NEW ITEM:")))
            total_list = reduce(lambda x, y: x + y, init_list)
            print("NEW TOTAL", total_list)
            last = input("PRESS \'a\' TO ADD MORE ITEMS OR PRESS \'q\' To EXIT:")

            if last == "q":
                print("----THANK YOU----", )
                print("---------------------------------------------------------------------------------------------")
                os.system("cls")
                break


shop_cal()
