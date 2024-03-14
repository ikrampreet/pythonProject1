import random

class Race:
    def _init_(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-20, 20))
            car.drive(1)

    def print_status(self):
        print("Race:", self.name)
        print("{:<15} {:<15} {:<15} {:<15}".format("Car", "Speed (km/h)", "Distance (km)", "Travel Time (hours)"))
        for car in self.cars:
            print("{:<15} {:<15} {:<15} {:<15}".format(car.registration_number, car.current_speed, car.travelled_distance, car.travel_time))

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False