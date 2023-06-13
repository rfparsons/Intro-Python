def average(score1, score2, score3):
    NUMBER_TESTS = 3
    if (score1 < 0 or score2 < 0 or score3 < 0):
        raise ValueError
    return float((score1 + score2 + score3)/NUMBER_TESTS)


if __name__ == "__main__":
    NUMBER_TESTS = 3
    firstname = input("Enter student first name: ")
    lastname = input("Enter student last name: ")
    age = input("Enter student age: ")
    scores = []
    for i in range(0 , NUMBER_TESTS):
        score = input("Enter score #" + str(i+1) + ": ")
        scores.append(int(score))

    try:
        average = average(scores[0], scores[1], scores[2])

        print(lastname + ", " + firstname)
        print("Age: " + age)
        print("Average test score: {0:.2f}".format(average))
    except ValueError:
        print("Negative value entered! Please try again.")