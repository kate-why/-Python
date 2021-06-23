#Task_1.1
from time import sleep

class TrafficLight:
    __color = 'red'

    def running(self):
        print('The traffic light is red')
        sleep(7)
        print('The traffic light is yellow')
        sleep(2)
        print('The traffic light is green')
        sleep(5)

traf_light = TrafficLight()
traf_light.running()


#Task_2
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        return f'Mass: {(self._length * self._width * 25 * 0.05) / 1000} t'

road1 = Road(5000, 20)
print(road1.calc())


#Task_3
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'profit': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_full_profit(self):
        return f'{sum(self._income.values())}'

worker1 = Position('Katerina', 'Petrova', 'clerk', 10, 20)

print(worker1.get_full_name())
print(worker1.get_full_profit())


#Task_4
class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

        print(f'New car: {self.name}, {self.color} color, {self.is_police} police')

    def go(self):
        print(f'{self.name} took off')

    def stop(self):
        print(f'{self.name} stopped')

    def turn(self, direction):
        print(f'{self.name} turned {"left" if direction == 0 else "right"}')

    def show_speed(self):
        print(f"{self.name}'s speed is {self.speed}")

class TownCar(Car):
    def show_speed(self):
        print(f"{self.name}'s speed is {self.speed}, {'Speed limit!' if self.speed > 60 else 'Normal speed'}")

class WorkCar(Car):
    def show_speed(self):
        print(f"{self.name}'s speed is {self.speed}, {'Speed limit!' if self.speed > 40 else 'Normal speed'}")

class SportCar(Car):
    '''Sport car'''

class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)

town_car = TownCar('Mini', 'white', 80)
town_car.turn(0)
town_car.show_speed()

work_car = WorkCar('Truck', 'blue', 30)
work_car.turn(0)
work_car.show_speed()

police_car = PoliceCar('Police', 'white/blue', 100)
police_car.stop()
police_car.show_speed()
print(police_car.is_police)


#Task_5
class Stationery:
    def  __init__(self, title='Can draw'):
        self.title = title

    def draw(self):
        print('Start drawing')

class Pen(Stationery):
    def draw(self):
        print(f'Start drawing with a pen: {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Start drawing with a pencil: {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Start drawing with a handle: {self.title}')


s = Stationery()
s.draw()

p = Pen('the white one')
p.draw()

pc = Pencil('the red one')
pc.draw()


h = Handle('the green one')
h.draw()
