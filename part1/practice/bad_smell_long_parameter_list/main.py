class Unit:

    speed = 1
    position = 'I lying!'

    def __init__(self, field, x_coord: int, y_coord: int):
        self.field = field
        self.x_coord = x_coord
        self.y_coord = y_coord

    def move(self, direction):
        speed = self._get_speed()

        if direction == 'UP':
            self.field.set_unit(y=self.y_coord + speed, x=self.x_coord, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(y=self.y_coord - speed, x=self.x_coord, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(y=self.y_coord, x=self.x_coord - speed, unit=self)
        elif direction == 'RIGHT':
            self.field.set_unit(y=self.y_coord, x=self.x_coord + speed, unit=self)

    def _get_speed(self):
        if self.position == 'fly':
            return self.speed * 1.2
        elif self.position == 'crawl':
            return self.speed * 0.5
        else:
            raise ValueError('Рожденный ползать летать не должен!')
