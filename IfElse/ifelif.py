tier = input("Welcome to the Programmer's Toolkit Monthly Subscription Box signup program! Please enter a subscription tier:\n\
    * Platinum\n\
    * Gold\n\
    * Silver\n\
    * Bronze\n\
    * Free Trial\n")

if tier.lower() == 'platinum':
    print("$60")
elif tier.lower() == 'gold':
    print("$50")
elif tier.lower() == 'silver':
    print("$50")
elif tier.lower() == 'bronze':
    print("$50")
elif tier.lower() == 'free trial':
    print("$50")
else:
    print("Invalid response")