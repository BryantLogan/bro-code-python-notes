# method chaining = used to call multiple method sequentially
                    #each call performs an action on the same object and returns Self


class Car:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the car")
        return self

car = Car()

#car.turn_on().drive()

#car.brake().turn_off()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()