def cleaner(measurements, maximum):
    after_cleaner = []
    for element in measurements:
        if element <= maximum:
            after_cleaner.append(element)
    measurements = after_cleaner
    return measurements


def main():
    measurements = [1.1, 2.2, 3.3, 4.4, 5.5]
    after_cleaner = cleaner(measurements, 4.0)
    print(after_cleaner)


if __name__ == "__main__":
    main()
