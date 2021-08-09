class Person:
    # name = 'aaaa'
    # age = 18


    def run(self):
        print('{},今年{}岁，正在跑步'.format(self.name, self.age))


p = Person()
p.name = 'aa'
p.age = 18
p.run()

p1 = Person()
p1.run()
p1.age=20


p2 = Person()
p2.run()
