# A better moustrap using tables
import string, sys
sys.path += ['../stateMachine', '../mouse']
from .State import State
from .StateMachine import StateMachine
from .MouseAction import MouseAction


class StateT(State):
    def __init__(self):
        self.transitions = None

    def next(self, input):
        if input in self.transitions:
            return self.transitions[input]
        else:
            raise("Input not supported for curretn state")


class Waiting(StateT):
    def run(self):
        print("Waiting: Broadcasting cheese smell")

    def next(self, input):
        # Lazy initialization:
        if not self.transitions:
            self.transitions = {
              MouseAction.appears: MouseTrap.luring
            }
        return StateT.next(self, input)


class Luring(StateT):
    def run(self):
        print("Luring: Presenting Cheese, door open")

    def next(self, input):
        # Lazy initialization:
        if not self.transitions:
            self.transitions = {
              MouseAction.enters: MouseTrap.trapping,
              MouseAction.runsAway: MouseTrap.waiting
            }
        return StateT.next(self, input)


class Trapping(StateT):
    def run(self):
        print("Trapping: Closing door")

    def next(self, input):
        # Lazy initialization:
        if not self.transitions:
            self.transitions = {
              MouseAction.escapes: MouseTrap.waiting,
              MouseAction.trapped: MouseTrap.holding
            }
        return StateT.next(self, input)


class Holding(StateT):
    def run(self):
        print("Holding: Mouse caught")

    def next(self, input):
        # Lazy initialization:
        if not self.transitions:
            self.transitions = {
              MouseAction.removed: MouseTrap.waiting
            }
        return StateT.next(self, input)


class MouseTrap(StateMachine):
    def __init__(self):
        # Initial state
        StateMachine.__init__(self, MouseTrap.waiting)


# Static variable initialization:
MouseTrap.waiting = Waiting()
MouseTrap.luring = Luring()
MouseTrap.trapping = Trapping()
MouseTrap.holding = Holding()

moves = map(string.strip,
  open("../mouse/MouseMoves.txt").readlines())
MouseTrap().runAll(map(MouseAction, moves))


# MouseMoves.txt
# mouse appears
# mouse runs away
# mouse appears
# mouse enters trap
# mouse escapes
# mouse appears
# mouse enters trap
# mouse trapped
# mouse removed
# mouse appears
# mouse runs away
# mouse appears
# mouse enters trap
# mouse trapped
# mouse removed
