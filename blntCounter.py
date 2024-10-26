import csv
from datetime import datetime
from collections import defaultdict

# filename for storing burn session records
FILENAME = 'blunt_log.csv'

def recordBlunt() :
    """Records current date and time for each burn session"""
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")

    with open(FILENAME, mode='a', newline='') as file :
        writer = csv.writer(file)
        writer.writerow([date, time])

    print(f"Burn Session recorded at {time} on {date}.")

def showDailySummary() :
    dailyCounts = defaultdict(int)

    try :
        with open(FILENAME, mode='r') as file :
            reader = csv.reader(file)
            next(reader)

            for row in reader :
                date = row[0]
                dailyCounts[date] += 1

    except FileNotFoundError :
        print("No records found. Start recording to see a summary.")
        return dailyCounts

    print("\nDaily Burn Sessions Summary:")
    for date, count in dailyCounts.items() :
        print(f"{date}: {count} blunts")
    return dailyCounts

def showMonthlySummary() :
    monthlyCounts = defaultdict(int)

    try :
        with open(FILENAME, mode='r') as file :
            reader = csv.reader(file)
            next(reader)

            for row in reader :
                date = datetime.strptime(row[0], "%Y-%m-%d")
                month = date.strftime("%Y-%m")
                monthlyCounts[month] += 1
    
    except FileNotFoundError :
        print("No records found.")
        return monthlyCounts

    print("\nMonthly Burn Sessions Summary:")
    for month, count in monthlyCounts.items() :
        print(f"{month} : {count} blunts")
    return monthlyCounts

def showYearlySummary() :
    yearlyCounts = defaultdict(int)

    try :
        with open(FILENAME, mode='r') as file :
            reader = csv.reader(file)
            next(reader)

            for row in reader :
                date = datetime.strptime(row[0], "%Y-%m-%d")
                year = date.strftime("%Y")
                yearlyCounts[year] += 1

    except FileNotFoundError :
        print("No records found.")
        return yearlyCounts

    print("\nYearly Burn Sessions Summary:")
    for year, count in yearlyCounts.items() :
        print(f"{year}: {count} blunts")
        return yearlyCounts


def exportReport() :
    """Exports a summary report in txt format"""
    # Get summaries
    daily = showDailySummary()
    monthly = showMonthlySummary()
    yearly = showYearlySummary()

    # Export to txt file
    with open("blunt_report.txt", "w") as file :
        file.write("Burn Sessions Report\n")
        file.write("====================\n\n")

        file.write("Daily Summary:\n")
        for date, count in daily.items() :
            file.write(f"{date}: {count} blunts\n")

        file.write("\nMonthly Summary:\n")
        for month, count in monthly.items() :
            file.write(f"{month}: {count} blunts\n")

        file.write("\nYearly Summary:\n")
        for year, count in yearly.items() :
            file.write(f"{year}: {count} blunts\n")

    print("Report exported as blunt_report.txt.")


def main() :
    while True :
        print("\n1.  Record a burn session")
        print("2.  Show daily burn sessions summary")
        print("3.  Show monthly burn sessions summary")
        print("4.  Show yearly burn sessions summary")
        print("5.  Export report")
        print("6.  Exit")
        
        choice = input("Choose an option (1-6): ")

        if choice == '1' :
            recordBlunt()
        elif choice == '2' :
            showDailySummary()
        elif choice == '3' :
            showMonthlySummary()
        elif choice == '4' :
            showYearlySummary()
        elif choice == '5' :
            exportReport()
        elif choice == '6' :
            print("Goodbye! Have a nice session.")
            break
        else :
            print("Invalid choice. Select a valid option!")

if __name__ == "__main__":
    # Initialize file with headers if it doesnt exist
    try :
        with open(FILENAME, mode='x', newline='') as file :
            writer = csv.writer(file)
            writer.writerow(["Date", "Time"]) # CSV Headers

    except FileExistsError :
        pass # File already exists, do not initialize

    main()
