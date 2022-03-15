import pandas as pd
import matplotlib.pyplot as plt

# This variable is to output an error in easier to read colors for user experience
ERROR = '\033[95m' + "[" + "ERROR" + "] " + '\033[0m'


def main():
    """This main function is for the whole plot showing and calculations for the plot"""

    # Opens the file as a pandas readable csv
    df = pd.read_csv("EstateAgents.csv")

    # Returns the County's total count in descending order
    count = df["County"].value_counts()

    # Outputs the count variable
    print("Destinations in order of populations:")
    print(count)

    # Makes a plot with country and population as the x and y label
    plt.figure(figsize=(20, 10))
    plt.title("Destinations in order of populations")
    plt.xlabel("Country")
    plt.ylabel("Population")
    # Gets the keys of the county, so the actual name and then saves that only to values
    values = df['County'].value_counts().keys().tolist()

    # Gets the value of county, then counts how many times each county appears then saves it as counts
    counts = df['County'].value_counts().tolist()

    # Saves the values above as x and y, for easier human readability
    x = values
    y = counts

    # Asks the user for 1 of 3 plots, with appropriate error handling and catching
    print("\nWhat plot to show?")
    while True:
        choice = input("1 = bar\n2 = scatter\n3 = plot\nEnter Here: ")
        if choice == "1":
            plt.bar(x, y)
            break
        elif choice == "2":
            plt.scatter(x, y)
            break
        elif choice == "3":
            plt.plot(x, y)
            break
        else:
            print(f"{ERROR}Please select an number 1-3")



    # Outputs the plot graph the user has chosen

    plt.show()


    # A while loop for the exit or continue function
    while True:
        choice = input("Would you like to go again? Y/N: ").upper()
        if choice == "Y":
            main()
        elif choice == "N":
            exit("User exited")
        else:
            print(f"{ERROR}Please select a valid option")


main()
