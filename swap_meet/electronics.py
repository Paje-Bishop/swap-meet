from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, category, condition):
        super().__init__(category = "Electronics", condition = 0)

    def __str__(self):
        return "A gadget full of buttons and secrets."
