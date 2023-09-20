import pandas as pd
from stats import generate_stats


def test_stats():
    df = pd.DataFrame({"c": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    res = generate_stats(df, "c")
    assert res["mean"] == 5.5
    assert res["median"] == 5.5
    assert int(res["std"]) == 3
