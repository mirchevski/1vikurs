date = input("Enter currnet date: ")
month = input("Enter month: ")
if (date.endswith("1")):
    print("Today's date is " + date + "st of " + month)
elif (date.endswith("2")):
    print("Today's date is " + date + "nd of " + month)
elif (date.endswith("3")):
    print("Today's date is " + date + "rd of " + month)
else:
    print("Today's date is " + date + "th and the month is " + month)