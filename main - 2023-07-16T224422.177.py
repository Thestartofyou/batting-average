def calculate_batting_average(total_runs, total_outs):
    if total_outs == 0:
        return "N/A"
    else:
        batting_average = total_runs / total_outs
        return batting_average

def main():
    runs = int(input("Enter the total runs scored: "))
    outs = int(input("Enter the total outs: "))

    average = calculate_batting_average(runs, outs)
    print("Batting Average:", average)

if __name__ == "__main__":
    main()

