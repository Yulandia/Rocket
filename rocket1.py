class Rocket:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move_up(self):
        self.y += 1

    def current_position(self):
        print("Current position: x=" + str(self.x) + ", y=" + str(self.y))

    def move_right(self):
        self.x +=1

    def move_down(self):
        self.y -= 1

    def move_left(self):
        self.x -= 1

my_rocket = Rocket()

my_rocket.move_up()
my_rocket.current_position()

my_rocket.move_right()
my_rocket.current_position()

my_rocket.move_down()
my_rocket.current_position()

my_rocket.move_left()
my_rocket.current_position()

