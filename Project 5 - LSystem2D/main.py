import turtle

# https://en.wikipedia.org/wiki/L-system


class LSystem2D:
    def __init__(self, axiom, speed):
        self.turtle = turtle.Turtle()
        self.axiom = axiom
        self.generation_axiom = self.axiom
        self.rules = []
        self.drawing_rules = {}

        self.turtle.speed(speed)

    def set_generation(self, n):
        assert n > 0
        self.generation_axiom = self.axiom

        for _ in range(n):
            new_axiom = ""
            i = 0
            while i < len(self.generation_axiom):
                was_replaced = False
                for rule, replacement in self.rules:
                    if self.generation_axiom[i:i + len(rule)] == rule:
                        new_axiom += replacement
                        i += len(rule)
                        was_replaced = True
                        break
                if not was_replaced:
                    new_axiom += self.generation_axiom[i]
                    i += 1

            self.generation_axiom = new_axiom

    def set_rules(self, iterable):
        self.rules = iterable

    def set_drawing_rules(self, iterable):
        for char, func in iterable:
            self.drawing_rules[char] = func

    def draw(self, start_pos=(0, 0)):
        self.turtle.goto(start_pos)
        self.turtle.clear()
        for symbol in self.generation_axiom:
            if symbol in self.drawing_rules.keys():
                self.drawing_rules[symbol](self.turtle)


#  Треугольник Серпинского
"""
sys = LSystem2D("F-G-G", 100)
sys.set_rules([("F", "F-G+F+G-F"),
               ("G", "GG")])

sys.set_drawing_rules([("F", lambda trtl: trtl.forward(20)),
                       ("G", lambda trtl: trtl.forward(20)),
                       ("+", lambda trtl: trtl.right(120)),
                       ("-", lambda trtl: trtl.left(120))])

sys.set_generation(5)
sys.draw((-250, -250))

turtle.Screen().exitonclick()
"""

#  Кривая дракона
sys = LSystem2D("FX", 100)
sys.set_rules([("X", "X+YF+"),
               ("Y", "-FX-Y")])

sys.set_drawing_rules([("F", lambda trtl: trtl.forward(2)),
                       ("+", lambda trtl: trtl.right(90)),
                       ("-", lambda trtl: trtl.left(90))])

#   remove 1 and 2 to draw in delayed mode
turtle.tracer(0)        # 1

sys.set_generation(15)
sys.draw()

turtle.update()         # 2

turtle.Screen().exitonclick()

