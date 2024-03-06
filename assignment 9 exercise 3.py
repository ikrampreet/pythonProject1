class Car:
    def _init_(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change
        if new_speed < 0:
            self.current_speed = 0
        elif new_speed > self.max_speed:
            self.current_speed = self.max_speed
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        distance_travelled = self.current_speed * hours
        self.travelled_distance += distance_travelled

# Main program
if _name_ == "_main_":
    # Create a new car instance
    my_car = Car("ABC-123", 142)

    # Accelerate the car
    my_car.accelerate(30)
    my_car.accelerate(70)
    my_car.accelerate(50)

    # Print out the current speed of the car
    print("Current Speed after acceleration:", my_car.current_speed, "km/h")

    # Apply emergency brake
    my_car.accelerate(-200)

    # Print out the final speed of the car
    print("Final Speed after emergency brake:", my_car.current_speed, "km/h")

    # Drive the car for 1.5 hours
    my_car.drive(1.5)

    # Print out the travelled distance
    print("Travelled Distance after driving for 1.5 hours:", my_car.travelled_distance, "km")