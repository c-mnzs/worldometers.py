# worldometers.py
### Get real time Earth statistics.
Parses information from countrymeters.info. Initially a test project as an introduction to Python classes but later reworked and refactored to be released to the public.

---

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

1. Download and install [Python](https://www.python.org/downloads/).
2. Install `worldometers.py` with `$ pip install worldometers.py`.

---

## Usage
Assume `worldometers = Worldometers()`.

* Get current world population:

    ```python
        current_pop = worldometers.current_world_population()
        # Output: Integer of the order 10e9
    ```

* Get births:

    ```python
        births_day = worldometers.births(timescale='day')
        # Output: Integer representing number of births today.

        births_year= worldometers.births(timescale='year')
        # Output: Integer representing number of births in the year.
    ```

The code is fairly easy to understand and apply. Read `worldometers.py` and you should get up to speed within seconds.

---

## Future
I've got to add a lot of stuff to this package. Keep your eyes peeled!

---

## Authors
* **Carlos Menezes** — *Initial work* - [c-mnzs](https://github.com/c-mnzs)

