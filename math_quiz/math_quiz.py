import random


def random_int(min, max):
    """
    picking random numbers between min and max range.

    Args:
        min (int): the minimum value.
        max (int): the maximum value.

    Returns:
        int: The random integer within the range of min and max.
    """
    return random.randint(min, max)


def random_operation():
    """
    Randomly pick mathematical operation among ('+', '-', '*').


    Returns:
        str: Random choice among ('+', '-', '*').
    """
    return random.choice(['+', '-', '*'])


def calculate(n1, n2, o):
    """
    Quiz calculation based on the randomly generated n1, n2 adn o

    Args:
        n1 (int): randomly generated first integer.
        n2 (int): randomly generated second integer.
        0 (str): randomly picked mathematical operation.

    Returns:
        tuple: A tuple containing:
            - p (str): A string representation of the mathematical expression.
            - a (int): The result of the arithmetic operation.
    """
    p = f"{n1} {o} {n2}"
    if o == '+':
        # sum operation
        a = n1 + n2
    elif o == '-':
        # subtraction operation
        a = n1 - n2
    else:
        # multiplication operation
        a = n1 * n2
    return p, a


def math_quiz():
    """
    Run an interactive math quiz game where the user answers arithmetic questions.

    This function generates a series of random math problems using basic operations
    (addition, subtraction, or multiplication) and prompts the user to answer each.
    The user’s answers are validated to ensure they are integers, and the score is
    updated based on correct answers.

    The game consists of a fixed number of questions. At the end, the user's score
    is displayed along with the total number of questions.

    Game Process:
        - Three questions are presented to the user.
        - For each question, two random integers and a random operation are generated.
        - The question is displayed, and the user inputs their answer.
        - The answer is validated for correct format (integer).
        - The score is incremented for each correct answer.

    Args:
        None

    Returns:
        None
    """
    s = 0
    t_q = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        # n1 and n2 need to be integer
        n1 = random_int(1, 10)
        n2 = random_int(1, 5)
        o = random_operation()

        (PROBLEM, ANSWER) = calculate(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")

        # added try-except block to handle non-integer user inputs
        while True:
            try:
                useranswer = int(useranswer)
                # breaking the infinite loop
                break
            except ValueError:
                # giving user another chance to provide new input
                useranswer = input("Give answer again (only integer): ")
                # not breaking the while loop here
                # because the user answer need to be validated in the next loop

        # checking the result of the user input
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            # adding marks
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")


if __name__ == "__main__":
    math_quiz()
