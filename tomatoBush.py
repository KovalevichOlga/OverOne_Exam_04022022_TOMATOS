# Класс TomatoBush
# 1. Создайте класс TomatoBush
# 2. Определите метод __init__(), который будет принимать в качестве параметра
# количество томатов и на его основе будет создавать список объектов класса
# Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
# 3. Создайте метод grow_all(), который будет переводить все объекты из списка
# томатов на следующий этап созревания
# 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из
# списка стали спелыми
# 5. Создайте метод give_away_all(), который будет чистить список томатов после
# сбора урожая

class TomatoBush:
    def __init__(self, amount):
        self.tomatoes = [Tomato(index) for index in range(0, amount]
    def grow_all(self):
        for i in self.tomatoes:
            i.grow()
    def all_are_ripe(self):
        if self._state == 4:
            return True
    def give_away_all(self):
        self.tomatoes = 0
