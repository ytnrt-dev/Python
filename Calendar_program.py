#Pestin, Trinity E.
#BSIT-1B
#CalendarProgram

import calendar


class CalendarDisplay:
    

    MONTH_NAMES = [
        "", "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    DAY_HEADERS_MON = "Mo Tu We Th Fr Sa Su"
    DAY_HEADERS_SUN = "Su Mo Tu We Th Fr Sa"

    def __init__(self):
        self.cal = calendar.Calendar(firstweekday=0)  # Monday start

    def _get_month_lines(self, year: int, month: int,
                        first_day_sunday: bool = False) -> list[str]:
        """Return a list of text lines for one month (width = 20 chars)."""
        title = f"{self.MONTH_NAMES[month]} {year}"
        header = self.DAY_HEADERS_SUN if first_day_sunday else self.DAY_HEADERS_MON

        c = calendar.Calendar(firstweekday=6 if first_day_sunday else 0)
        weeks = c.monthdayscalendar(year, month)

        lines = [title.center(20), header]
        for week in weeks:
            row = " ".join(f"{d:2}" if d != 0 else "  " for d in week)
            lines.append(row)
        return lines

    def display_single_month(self, year: int, month: int) -> None:
        """Option 1 – one month, Monday-first."""
        print(f"\n Calendar for {self.MONTH_NAMES[month]} {year}:\n")
        lines = self._get_month_lines(year, month, first_day_sunday=False)
        for line in lines:
            print(f"   {line}")
        print()

    def display_3_months_per_column(self, year: int) -> None:
        """Option 2 – all 12 months in 3-column groups (4 rows of 3)."""
        print(f"\n Calendar Display (3 Months per Column):\n")
        col_width = 22

        for group_start in range(1, 13, 3):
            months = range(group_start, min(group_start + 3, 13))

            all_lines = [
                self._get_month_lines(year, m, first_day_sunday=True)
                for m in months
            ]

            max_rows = max(len(ml) for ml in all_lines)
            for ml in all_lines:
                while len(ml) < max_rows:
                    ml.append("")


            header_row = "".join(
                self.MONTH_NAMES[m].center(col_width) for m in months
            )
            print(header_row)
            for row_idx in range(1, max_rows):
                row_text = "".join(
                    ml[row_idx].ljust(col_width) for ml in all_lines
                )
                print(row_text)

            print("\n" + "-" * 66 + "\n")

    def display_4_months_per_row(self, year: int) -> None:
        """Option 3 – all 12 months in 4-column groups (3 rows of 4)."""
        print(f"\n Calendar Display (4 Months per Row):\n")
        col_width = 22

        for group_start in range(1, 13, 4):
            months = range(group_start, min(group_start + 4, 13))

            all_lines = [
                self._get_month_lines(year, m, first_day_sunday=True)
                for m in months
            ]

            max_rows = max(len(ml) for ml in all_lines)
            for ml in all_lines:
                while len(ml) < max_rows:
                    ml.append("")

            header_row = "".join(
                self.MONTH_NAMES[m].center(col_width) for m in months
            )
            print(header_row)
            for row_idx in range(1, max_rows):
                row_text = "".join(
                    ml[row_idx].ljust(col_width) for ml in all_lines
                )
                print(row_text)

            print()

    @staticmethod
    def _get_year() -> int:
        while True:
            try:
                year = int(input("Enter a year: "))
                if 1 <= year <= 9999:
                    return year
                print("Please enter a valid year (1–9999).")
            except ValueError:
                print("Invalid input. Please enter an integer.")

    @staticmethod
    def _get_month() -> int:
        while True:
            try:
                month = int(input("Enter the month (1-12): "))
                if 1 <= month <= 12:
                    return month
                print("Please enter a month between 1 and 12.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def run(self) -> None:
        while True:
            print("\nChoose a calendar display option:")
            print("1. Display calendar for a specific month")
            print("2. Display calendar in 3-months-per-column format")
            print("3. Display calendar in 4-months-per-row format")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ").strip()

            if choice == "1":
                year = self._get_year()
                month = self._get_month()
                self.display_single_month(year, month)

            elif choice == "2":
                year = self._get_year()
                self.display_3_months_per_column(year)

            elif choice == "3":
                year = self._get_year()
                self.display_4_months_per_row(year)

            elif choice == "4":
                print("Exiting. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    app = CalendarDisplay()
    app.run()