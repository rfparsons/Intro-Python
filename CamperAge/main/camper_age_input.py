def convert_to_months(years):
    months = years * 12
    return months


if __name__ == "__main__":
    user_input = input("Age in years?\n")
    age_in_years = int(user_input)
    age_in_months = convert_to_months(age_in_years)
    print(str(age_in_years) + " years is " + str(age_in_months) + " months")
