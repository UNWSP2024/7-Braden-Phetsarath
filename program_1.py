# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year,
# the average monthly rainfall, # and the months with the highest and lowest amounts.
#Braden Phetsarath
#10/15
# rainfall list
def main():
    month_list = ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]
    rainfall = []
    for month in month_list:
        amount = float(input(f"Enter the amount of rain for {month}: "))
        rainfall.append(amount)

    max_rainfall = max(rainfall)
    min_rainfall = min(rainfall)
    mxrmonth = rainfall.index(max_rainfall)
    mnrmonth = rainfall.index(min_rainfall)

    wettest_months = [month_list[i] for i in range(len(rainfall)) if rainfall[i] == max_rainfall]
    driest_months = [month_list[i] for i in range(len(rainfall)) if rainfall[i] == min_rainfall]

    total_rainfall = sum(rainfall)
    average = total_rainfall / len(month_list)

    print("\n--- Rainfall Summary ---")
    print(f"Total rainfall: {total_rainfall:.2f} inches")
    print(f"Average monthly rainfall: {average:.2f} inches")
    print(f"Wettest month: {wettest_months} ({max_rainfall:.2f} inches)")
    print(f"Driest month: {driest_months} ({min_rainfall:.2f} inches)")



if __name__ == "__main__":
    main()
