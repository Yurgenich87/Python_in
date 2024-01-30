class LotteryGame:
    def __init__(self, list1 , list2 ):
        self.list1 = list1
        self.list2 = list2

    def compare_lists(self):
        list_result = []
        counter = 0
        for i in self.list1:
            if i in self.list2:
                list_result.append(i)
                counter += 1

        if counter == 0:
            print("Совпадающих чисел нет.")
        else:
            print(f"Совпадающие числа: {list_result}\nКоличество совпадающих чисел: {counter}")


list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]
game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()

