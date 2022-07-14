rec = ("Bob", 40.5, ["dev", "mgr"]) # Запись на основе кортежа
print(rec[0])

rec = {} # Запись на основе словаря
rec["name"] = "Bob"
rec["age"] = 40.5
rec["jobs"] = ["dev", "mgr"]
print(rec["name"])

class rec:
    pass

rec.name = "Bob" # Запись на основе класса
rec.age = 40.5
rec.jobs = ["dev", "mgr"]

print(rec.name)

class Rec_two:
    pass

pers1 = Rec_two() # Запись на основе экземпляров
pers1.name = "Bob"
pers1.age = 40.5
pers1.jobs = ["dev", "mgr"]
pers2 = Rec_two()
pers2.name = "Alina"
pers2.age = 34
pers2.jobs = ["developer"]
print(pers1.name, pers2.name)


class Person:
    def __init__(self, name, job, age=None): # Класс = данные + логика
        self.name = name
        self.job = job
        self.age = age
    def info(self):
        return self.name, self.job

char1 = Person("Evgeniy", "Developer", 32) # Вызов конструктора
char2 = Person("Stefania", "Art") # Вызов конструктора
print(char1.job) # Атрибуты + методы
print(char2.info())
print(char1.info())