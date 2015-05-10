def get_list():

    user_list = []

    while True:

        user_input = raw_input("Please enter a number, or x to end your list: ")

        if user_input == 'x':
            break
        try:
            user_input = int(user_input)
        except ValueError:
            print "That's not a number!"
            continue
        else:
            user_list.append(user_input)
            continue

    return user_list


def print_list(user_list):
    print
    print "Your list contains the below numbers:"
    for i in user_list:
        print i,
    print


def print_mean(user_list):
    print
    print "The mean of your list is:"
    list_length = len(user_list)
    list_sum = sum(user_list)
    mean = list_sum / list_length
    print mean


def print_mode(user_list):
    print
    print "The mode of your list is:"
    highest = 0
    for i in user_list:
        count = user_list.count(i)
        if count > highest:
            highest = i
    print highest


def print_median(user_list):
    print
    print "The median of your list is:"
    sorted_list = sorted(user_list)
    list_length = len(user_list)

    if list_length % 2 == 0:
        median = sorted_list[int(0.5 * list_length) - 1]
    else:
        median = sorted_list[int(0.5 * list_length)]
    print median


def main():
    numbers = get_list()
    print_list(numbers)
    print_mean(numbers)
    print_mode(numbers)
    print_median(numbers)

main()


