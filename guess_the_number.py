import random

def guess_the_number()
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print(猜猜看，我想的是哪个1到100之间的数字？你有{}次机会。.format(max_attempts))

    while attempts  max_attempts
        guess = int(input(你猜的数字是：))
        attempts += 1

        if guess  number_to_guess
            print(太低了！)
        elif guess  number_to_guess
            print(太高了！)
        else
            print(恭喜你，猜对了！)
            break

    if guess != number_to_guess
        print(很遗憾，你没有猜对。我想的数字是：, number_to_guess)

if __name__ == '__main__'
    guess_the_number()
