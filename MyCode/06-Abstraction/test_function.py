sum = lambda x, y: x + y;
def test_sum():
    assert sum(1, 2) == 3 
    assert sum(2, 3) == 5
if __name__ == '__main__':
    test_sum()
    assert callable(sum), 'sum is not callable'