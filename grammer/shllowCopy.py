def shallowCopy():
    a = [1,2,3]
    print(id(a))
    a[0]=5
    print(a)
    print(id(a))


if __name__ == "__main__":
    shallowCopy()