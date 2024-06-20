def main():
    mylist = ["iogwog", "f8i9eh9gw", "fi9e8g93", "f9ewhgbe9rg"]

    ptr = next(iter(mylist))

    print(ptr)

    ptr = next(ptr)
    print(next(ptr))


if __name__ == "__main__":
    main()
