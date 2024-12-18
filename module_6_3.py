import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        new_x = self._cords[0] + dx * self.speed
        new_y = self._cords[1] + dy * self.speed
        new_z = self._cords[2] + dz * self.speed

        if new_z < 0:
            print("It's too deep, i can't dive :(")
            return

        self._cords[0] = new_x
        self._cords[1] = new_y
        self._cords[2] = new_z

    def get_cords(self):
        return f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}"

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        eggs_count = random.randint(1, 4)
        print(f"Here are(is) {eggs_count} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)
        new_z = self._cords[2] - dz

        if new_z < 0:
            print("It's too deep, i can't dive :(")
            return

        self._cords[2] = new_z
        self.speed /= 2  # Уменьшаем скорость вдвое при нырянии


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"


if __name__ == "__main__":
    db = Duckbill(10)

    print(db.live)  # True
    print(db.beak)  # True

    db.speak()  # Click-click-click
    db.attack()  # Sorry, i'm peaceful :)

    db.move(1, 2, 3)
    print(db.get_cords())  # X: 10, Y: 20, Z: 30

    db.dive_in(6)
    print(db.get_cords())  # X: 10, Y: 20, Z: 24 (или другое значение выше 0)

    db.lay_eggs()  # Here are(is) X eggs for you (где X - случайное число от 1 до 4)
