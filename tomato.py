# Класс Tomato:
# 1. Создайте класс Tomato
# 2. Создайте статическое свойство states, которое будет содержать все стадии
# созревания помидора
# 3. Создайте метод __init__(), внутри которого будут определены два динамических
# protected свойства: 1) _index - передается параметром и 2) _state - принимает первое
# значение из словаря states
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию
# созревания
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг
# последней стадии созревания)

class Tomato:
    #Статическое свойство
    states = {0: 'empty', 1: 'sprout', 2: 'flower', 3: 'green_tomato', 4: 'red_tomato', 5: 'rotten_tomato'}
    def __int__(self, index, state):
        self._index = index
        self._state = states[0]
    def grow(self):
        self._state += 1
    def is_ripe(self):
        if self._state == 4:
            print ('Tomato is red!')


