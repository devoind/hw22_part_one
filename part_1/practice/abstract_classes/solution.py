from abc import ABC, abstractmethod


class Transport(ABC):

    @abstractmethod
    def start_engine(self):
        raise NotImplementedError

    @abstractmethod
    def stop_engine(self):
        raise NotImplementedError

    @abstractmethod
    def move(self):
        raise NotImplementedError

    @abstractmethod
    def stop(self):
        raise NotImplementedError


class Boat(Transport):
    def start_engine(self):
        print('Катер громко затарахтел')

    def stop_engine(self):
        print('Двигатель катера чихнул напоследок и заглох')

    def move(self):
        print('Катер быстро набирает скорость')

    def stop(self):
        print('Катер остановился')


class Car(Transport):
    def start_engine(self):
        print('Машина заурчала двигателем')

    def stop_engine(self):
        print('Машина стоит с заглушенным двигателем')

    def move(self):
        print('Машина едет к цели назначения')

    def stop(self):
        print('Машина остановилась')


class Electroscooter(Transport):
    def start_engine(self):
        print('Мигнул светодиодом')

    def stop_engine(self):
        print('Мигнул светодиодом дважды')

    def move(self):
        print('Прохожие в ужасе разбегаются от очередного камикадзе')

    def stop(self):
        print('Торможение об стену прошло успешно')


class Person:

    def use_transport(self, transport: Transport):
        transport.start_engine()
        transport.move()
        transport.stop()
        transport.stop_engine()
