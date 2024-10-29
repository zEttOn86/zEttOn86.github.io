from ._registry import register_beer

class Asahi:
    def __init__(self):
        print("Created Asahi beer!")

@register_beer
def asahi_beer():
    return Asahi()