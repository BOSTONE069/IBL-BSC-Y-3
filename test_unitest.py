from squarefunction import square

def main():
    test_square()

def test_square():
    assert square(3) == 9
    assert square(7) == 49

if __name__ == "__main__":
    main()