import matplotlib.pyplot as plt
import csv
def Option(choice):
    if choice == 1:
        file_path = "big_data_canada.csv"
    elif choice == 2:
        file_path = "dl_canada.csv"
    elif choice == 3:
        file_path = "ml_canada.csv"
    elif choice == 4:
        file_path = "py_canada.csv"
    elif choice == 5:
        file_path = "sql_canada.csv"
    elif choice == 6:
        print("Thanks for using")
        exit()
    else:
        print("Invalid Choice! Try Again.")
    return file_path
def Convert(file_path):
    csv_data = []
    # Open the CSV file and read its contents
    with open(file_path, 'r') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)
        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Append each row to the 2D list
            csv_data.append(row)
    return csv_data
def Trend(tech_data):
    # Sample data for tech adoption trends (year, adoption rate)
    # Extracting years and adoption rates from the data
    years = [data[0] for data in tech_data]
    adoption_rates = [data[1] for data in tech_data]
    # Plotting the tech adoption trend
    plt.plot(years, adoption_rates, marker='o')
    # Adding labels and title to the plot
    plt.xlabel('Year')
    plt.ylabel('Adoption Rate (%)')
    plt.title('Tech Adoption Trends')
    plt.axis('off')
    # Displaying the plot
    plt.show()
    return 0

while(True):
    print("CHOOSE THE TECHNOLOGY:\n1. Big Data\n2. Deep Learning\n3. Machine Learning\n4. Python\n5. SQL\n6. Quit\n")
    choice = int(input("Enter: "))
    file_path= Option(choice)
    tech_data = Convert(file_path)
    Trend(tech_data)
