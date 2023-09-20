import pandas as pd
from lib import get_mean, get_median, get_stddev


def test_get_stats():
    df = pd.DataFrame({"c": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    assert get_mean(df, "c") == 5.5
    assert get_median(df, "c") == 5.5
    assert int(get_stddev(df, "c")) == 3
