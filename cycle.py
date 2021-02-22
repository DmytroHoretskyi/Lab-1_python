class  Cycle:
    className = 'Cycle'

    # Статичний метод, який виводить статичне поле classname класу Cycle
    @staticmethod
    def displayClassName():
        print(f'Назва класу: {Cycle.className}')

    # Конструктор з дефолтними значеннями
    def __init__(self, gearsCount="default", weight="default", weightLimit="default", producerName="default",
                 wheelSize="default", color="default",   isElectric="default"):
        self.gearsCount = gearsCount
        self.weight = weight
        self.weightLimit = weightLimit
        self.producerName = producerName
        self.wheelSize = wheelSize
        self.color = color
        self.isElectric = isElectric

    # Строкове представлення об'єкту
    def __str__(self):
        return str({"К-ть передач: ": self.gearsCount, "Вага: ": self.weight, "Макс. вага: ": self.weightLimit,
                    "Виробник: ": self.producerName, "Розмір колес: ": self.wheelSize, "Колір: ": self.color,
                   "Електровелосипед: ": self.isElectric})

    # Деструктор
    def __del__(self):
        print("Об'єкт був видалений!")

