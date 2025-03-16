from abc import ABC, abstractmethod


class Talker(ABC):
    @abstractmethod
    def talk(self):
        pass


class Knigget(Talker):
    def talk(self):
        print("Ni!")


class Herring:
    def talk(self):
        print("Blub.")


if __name__ == "__main__":
    k = Knigget()
    k.talk()
    isinstance(k, Talker)  # True
    Talker.register(Herring)
    h = Herring()
    isinstance(h, Talker)  # True
    issubclass(Herring, Talker)  # True
