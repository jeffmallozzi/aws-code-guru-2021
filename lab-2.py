import config

def main():
    ask_again = True
    while(ask_again):
        a = input("Enter the numerator: ")
        b = input("Enter the denominator: ")
        result = perform_division(a,b)
        print(result)
        ask_again = input("Do you want to perform another operation? Enter yes or no: ")
        if(ask_again == 'yes'):
            ask_again = True
        else:
            ask_again = False
            print("You performed " + str(config.operations_count) + " operations, bye!")


def perform_division(a,b):

    try:
        config.operations_count += 1
        return int(a)/int(b)
    except ZeroDivisionError as e:
        return(e)


main()