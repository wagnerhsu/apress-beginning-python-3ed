class Person:
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def greet(self):
        print('Hello {}'.format(self.name))


foo = Person()
foo.name = 'Wagner'
foo.greet()
