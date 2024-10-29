from typing import Callable, Dict, Any

__all__ = ["register_beer", "beer_entry_point"]

_beer_entry_points: Dict[str, Callable[..., Any]] = {}  # Mapping beer name to function to be create beer

def beer_entry_point(beer_name: str):
    # 辞書の中にnameが存在するかの確認をしたほうがベター
    return _beer_entry_points[beer_name]

def register_beer(fn: Callable):
    """ビールを登録する

    Args:
        fn: ビールを作成する関数

    Retunr:
        fn: ビールを作成する関数
    """
    func_name = fn.__name__
    _beer_entry_points[func_name] = fn

    return fn
