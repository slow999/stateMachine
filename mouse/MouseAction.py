class MouseAction:
    def __init__(self, action):
        print('start init..')
        self.action = action

    def __str__(self):
        return self.action

    # def __cmp__(self, other):
    #     return cmp(self.action, other.action)
    # Necessary when __cmp__ or __eq__ is defined
    # in order to make this class usable as a dictionary key:

    def __hash__(self):
        return hash(self.action)


MouseAction.appears = MouseAction("mouse appears")
MouseAction.runsAway = MouseAction("mouse runs away")
MouseAction.enters = MouseAction("mouse enters trap")
MouseAction.escapes = MouseAction("mouse escapes")
MouseAction.trapped = MouseAction("mouse trapped")
MouseAction.removed = MouseAction("mouse removed")