from habit import Habit, habit_tracker
import pandas as pd
from tabulate import tabulate
from datetime import datetime


def main():
    habits: list[Habit] = [
        habit_tracker("Smoke", datetime(2023,10,15,8), 12000, 30),
        habit_tracker("instagram", datetime(2023,11,20,6), 20000, 120),
    ]
    df = pd.DataFrame(habits)
    print(tabulate(df,headers="keys",tablefmt="heavy_grid"))

if __name__ == '__main__':
    main()
