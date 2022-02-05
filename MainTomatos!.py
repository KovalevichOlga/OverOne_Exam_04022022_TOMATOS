# Тесты:
# 1. Вызовите справку по садоводству
# 2. Создайте объекты классов TomatoBush и Gardener
# 3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
# 4. Попробуйте собрать урожай
# 5. Если томаты еще не дозрели, продолжайте ухаживать за ними
# 6. Соберите урожай


from tomato import Tomato
from tomatoBush import TomatoBush
from gardener import Gardener


if __name__ == '__main__':
    Gardener.knowledge_base()
    first_tomato_bush = TomatoBush()
    first_gardener = Gardener()
    first_gardener.work()
    first_gardener.harvest()
    first_gardener.work()
    first_gardener.harvest()