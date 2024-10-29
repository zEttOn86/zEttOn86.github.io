from ._registry import beer_entry_point

__all__ = ["create_beer"] 

def create_beer(beer_name):
    fn = beer_entry_point(beer_name)
    return fn()