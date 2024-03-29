"""This is my submission for Assignment Eight."""


import pgeocode
import math


class HistoricalTemps:
    """Create class with Historical Temperatures."""

    def __init__(self, zip_code: str, start="1950-08-13", end="2023-08-25"):
        """Use 3 parameters in init method, return tuple, and validate lat."""
        self._zip_code = zip_code
        self._start = start
        self._end = end
        lat, lon, loc_name = HistoricalTemps.zip_to_loc_info(zip_code)
        self._lat = lat
        self._lon = lon
        self._loc_name = loc_name
        if math.isnan(lat):
            raise LookupError
        self._temp_list = None
        self._load_temps()

    def _load_temps(self):
        """Load hardcoded historical temp data."""
        hc_temps = [
            ("2020-01-01", 29.0),
            ("2020-01-02", 30.0),
            ("2020-01-03", 31.0),
            ("2020-01-04", 29.5),
            ("2020-01-05", 30.5),
            ("2020-01-06", 31.5),
            ("2020-01-07", 28.5),
            ("2020-01-08", 29.5),
            ("2020-01-09", 30.5),
            ("2020-01-10", 30.0),
            ("2020-01-11", 31.0)
        ]
        self._temp_list = hc_temps

    @staticmethod
    def zip_to_loc_info(zip_code):
        """Use static method by passing zip to return location details."""
        geocoder = pgeocode.Nominatim('us')
        result = geocoder.query_postal_code(zip_code)
        lat = result['latitude']
        lon = result['longitude']
        loc_name = result['place_name']
        return lat, lon, loc_name

    @property
    def start(self):
        """Run start getter here."""
        return self._start

    @start.setter
    def start(self, new_num):
        """Run start setter here."""
        self._start = new_num

    @property
    def end(self):
        """Run end getter here."""
        return self._end

    @end.setter
    def end(self, new_num):
        """Run end setter here."""
        self._end = new_num

    @property
    def zip_code(self):
        """Run zip_code getter here."""
        return self._zip_code

    @property
    def loc_name(self):
        """Run loc_name getter here."""
        return self._loc_name

    def average_temp(self):
        """Compute average temp, then print."""
        temp_sum = 0
        for item in self._temp_list:
            temp_sum += item[1]
        temp_float = temp_sum / len(self._temp_list)
        return temp_float

    def extreme_days(self, threshold: float):
        """Extract date/temp tuples using list comprehension."""
        return [item for item in self._temp_list if item[1] > threshold]


def create_dataset():
    """Prompt user for zip and use builtin LookupError to validate it."""
    zip_code = input("Please enter a zip code: ")
    try:
        hist_temp = HistoricalTemps(zip_code)
    except LookupError:
        hist_temp = None
        print("Data could not be loaded. Please check that the zip code is "
              "correct and that you have a working internet connection")
    return hist_temp


def print_extreme_days(dataset: HistoricalTemps):
    """Check if dataset is loaded, then prompt user for threshold temp."""
    if dataset is None:
        print("Please load this dataset first")
        return
    try:
        threshold = float(input("List days above what temperature? "))
    except ValueError:
        print("Please enter a valid temperature")
        return
    extdays_lc = dataset.extreme_days(threshold)
    print(f"There are {len(extdays_lc)} days above {threshold} degrees in "
          f"{dataset.loc_name}")
    for item in extdays_lc:
        print(f"{item[0]}: {item[1]}")


def main():
    """Prompt user for name, then greet them and state activity."""
    name = input("Please enter your name: ")
    print(f"Hi {name}, let's explore historical temperatures.\n")
    menu()


def menu():
    """Ask user to select item to get output. Pass in dataset arguments."""
    dataset_one = None
    dataset_two = None
    while True:
        print_menu(dataset_one, dataset_two)
        try:
            number = int(input("What is your choice? "))
        except ValueError:
            print("Please enter a number only")
            continue
        match number:
            case 1:
                dataset_one = create_dataset()
                continue
            case 2:
                dataset_two = create_dataset()
                continue
            case 3:
                compare_average_temps(dataset_one, dataset_two)
            case 4:
                print_extreme_days(dataset_one, )
                continue
            case 5:
                print("selection five is not functional yet")
            case 6:
                print("selection six is not functional yet")
            case 7:
                print("selection seven is not functional yet")
            case 9:
                print("Goodbye!  Thank you for using the database")
                break
            case _:
                print("That's not a valid selection")


def print_menu(dataset_one: HistoricalTemps, dataset_two: HistoricalTemps):
    """Display Main Menu for user selection, and include two parameters."""
    print("Main Menu")
    if dataset_one is None:
        print("1 - Load dataset one")
    else:
        print(f"1 - Replace {dataset_one.loc_name}")
    if dataset_two is None:
        print("2 - Load dataset two")
    else:
        print(f"2 - Replace {dataset_two.loc_name}")
    print("3 - Compare average temperatures")
    print("4 - Dates above threshold temperature")
    print("5 - Highest historical dates")
    print("6 - Change start and end dates for dataset one")
    print("7 - Change start and end dates for dataset two")
    print("9 - Quit")


def compare_average_temps(dataset_one: HistoricalTemps,
                          dataset_two: HistoricalTemps):
    """Once loaded, compare average temps of both datasets."""
    if dataset_one is None or dataset_two is None:
        print("Please load two datasets first")
    else:
        print(f"The average maximum temperature for {dataset_one.loc_name} "
              f"was{dataset_one.average_temp(): .2f} degrees Celsius")
        print(f"The average maximum temperature for {dataset_two.loc_name} "
              f"was{dataset_two.average_temp(): .2f} degrees Celsius")


if __name__ == "__main__":
    main()
