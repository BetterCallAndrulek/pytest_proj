from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2  # 3
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([1, 2, 3], -1, "test") == "test"  # new
    assert arrs.get([1, 2, 3], 4, "test") == "test"  # new
    assert arrs.get([1, 2, 3], 3, "test") == "test"  # new


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4], -3, -1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4], -3, 2) == [2]
    assert arrs.my_slice([1, 2, 3, 4], 3, 2) == []
    assert arrs.my_slice([], 3, 2) == []
    assert arrs.my_slice([1, 2, 3, 4], -5, 2) == [1, 2]