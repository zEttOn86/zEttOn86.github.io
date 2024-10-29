from ._registry import register_beer

class Sapporo:
    def __init__(self):
        print("Created Sapporo beer!")

@register_beer
def sapporo_beer():
    return Sapporo()