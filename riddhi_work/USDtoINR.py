# w.a.p. to convert US to INR(Indian Rupees) take any value from user it should be dynamic.


def currency(usd):
    USD = float(usd)
    try:
        if USD > 0:
            INR = float(USD) * 68.50
            return INR

        else:
            return 'The value should be Positive, not a Negative.'
    except:
        return "It should be a value, not a STRING."

# currency(input("Enter USD amount to convert in INR: "))
