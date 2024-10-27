import csv
import sys
from datetime import datetime, timedelta
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

def showWeeklySummary() :
    weeklyCounts = defaultdict(int)

    try :
        with open(FILENAME, mode="r") as file :
            reader = csv.reader(file)
            next(reader)

            for row in reader :
                date = datetime.strptime(row[0], "%Y-%m-%d")
                # Get the start of the week (Monday)
                week_start = date - timedelta(days=date.weekday())
                weeklyCounts[week_start.strftime("%Y-%m-%d")] += 1

    except FileNotFoundError :
        print(f"No records found!")
        return weeklyCounts
    
    print(f"\nWeekly Burn Sessions Summary:")
    for week_start, count in sorted(weeklyCounts.items()) :
        print(f"Week starting {week_start}: {count} blunts")
    return weeklyCounts

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
    weekly = showWeeklySummary()
    monthly = showMonthlySummary()
    yearly = showYearlySummary()

    # Export to txt file
    with open("blunt_report.txt", "w") as file :
        file.write("Burn Sessions Report\n")
        file.write("====================\n\n")

        file.write("Daily Summary:\n")
        for date, count in daily.items() :
            file.write(f"{date}: {count} blunts\n")

        file.write("Weekly Summary:\n")
        for week_start, count in weekly.items() :
            file.write(f"Week starting {week_start}: {count} blunts\n")

        file.write("\nMonthly Summary:\n")
        for month, count in monthly.items() :
            file.write(f"{month}: {count} blunts\n")

        file.write("\nYearly Summary:\n")
        for year, count in yearly.items() :
            file.write(f"{year}: {count} blunts\n")

    print("Report exported as blunt_report.txt.")


def main() :
    if len(sys.argv) > 1 and sys.argv[1] == '1' : # Check for bash arguments
        try :
            numBlunts = int(sys.argv[2]) if len(sys.argv) > 2 else 1
            if numBlunts <= 0 :
                raise ValueError("The number of blunts must be greater than 0!")

            for _ in range(numBlunts) :
                recordBlunt()

        except ValueError as e :
            print(f"Invalid input for number of blunts: {e}")
            return


    while True :
        print("\n1.  Record a Burn Session")
        print("2.  Show Daily Burn Sessions Summary")
        print("3.  Show Weekly Burn Sessions Summary")
        print("4.  Show Monthly Burn Sessions Summary")
        print("5.  Show Yearly Burn Sessions Summary")
        print("6.  Export Report")
        print("7.  Exit")
        
        choice = input("Choose an Option (1-6): ")

        if choice == '1' :
            recordBlunt()
        elif choice == '2' :
            showDailySummary()
        elif choice == '3' :
            showWeeklySummary()
        elif choice == '4' :
            showMonthlySummary()
        elif choice == '5' :
            showYearlySummary()
        elif choice == '6' :
            exportReport()
        elif choice == '7' :
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
