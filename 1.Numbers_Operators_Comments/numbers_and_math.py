def main():
    things_to_print = {
        "Then number 10 is of type..." : type(10),
        "The number 11.23 is of type..." : type(11.23)
        "1 + 1 = ": 1+1,
        "5 - 3 = ": 5-3,
        "18 / 2 = ": 18 / 2,
        "18 // 2 = ": 18//2,
        "15 % 2 = ":15 % 2,
        "2 ** 3 = ": 2**3}

    for k,v in things_to_print.items():
        print(f"{k}{v}")


if __name__ == "__main__":
    main()
