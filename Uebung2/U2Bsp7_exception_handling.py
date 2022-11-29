#exception_handling_exercise
def divide_numbers():
    try:
        for i in range(3):
            x = int(input('Please enter number: '))
            y = int(input('Another number: '))
            print(f'{x} / {y} = {x/y}')

    except TypeError as e:
        print(f"Es dürfen keine Kommazahlen verwendet werden! -> {e}")
    except ValueError as e:
        print(f"Es müsssen Zahlen verwendet werden! -> {e}")
    except ZeroDivisionError as e:
        print(f"Es müsssen Zahlen verwendet werden! -> {e}")



def main():
    divide_numbers()

if __name__ == '__main__':
    main()
