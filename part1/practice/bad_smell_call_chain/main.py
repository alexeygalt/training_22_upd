# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов
class Person:
    def __init__(self, city_population, room_num):
        self.city_population = city_population
        self.room_num = room_num

    def get_city_population(self):
        return self.city_population

    def get_room_num(self):
        return self.room_num


# TODO после выполнения задания попробуйте

key_person = Person(666, 1408)
print(key_person.city_population, key_person.room_num)

