#Braden Phetsarath
#10/15
# Program #3: US_Population
def main():

    # Have the user input (using a loop) various information that contains three pieces of data:
    all_entered_values = []
    for i in range (3):
        data = input("Enter year, name of state, population (separated by spaces): ")

        year_str, state, population_str = data.split()

        year = int(year_str)
        population = int(population_str)

        all_entered_values.append([year,state,population])
    # year, name of state, and population.
    # Store all of this information in a list of lists.  For example it might be stored like this:

    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]


    # Now have the user enter a year.
    check_year = int(input("Enter year to analyze population: "))
    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year
    total = sum_population_for_year(all_entered_values, check_year)

    # print the totalled population
    print(f"Total population for {check_year}: {total}")
 

def sum_population_for_year(all_entered_values, year_to_sum):
    total = 0

    for record in all_entered_values:
            if record[0] == year_to_sum:
                total += record[2]
    return total
# Loop through and sum the populations for the appropriate year.
# e.g. for the list on line 7 the total would be 8,860,637 if the user entered 2010 for the year to sum,
# or 3,421,988 if they entered 2011 for the year to sum.




# Call the main function.
if __name__ == '__main__':
    main()
