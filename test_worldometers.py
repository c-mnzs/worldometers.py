import worldometers
import unittest


class TestConfluenceGetSet(unittest.TestCase):
    wo = worldometers.Worldometers()

    def test_getWorldPopulation(self):
        current_pop = self.wo.current_world_population()
        # Output: Integer of the order 10e9
        self.assertIsInstance(current_pop, int)
        print("World population: " + str(current_pop))

    def test_getWorldPopulationMale(self):
        current_pop = self.wo.current_world_population(option="male")
        # Output: Integer of the order 10e9
        self.assertIsInstance(current_pop, int)
        print("World male population: " + str(current_pop))

    def test_getWorldPopulationFemale(self):
        current_pop = self.wo.current_world_population(option="female")
        # Output: Integer of the order 10e9
        self.assertIsInstance(current_pop, int)
        print("World female population: " + str(current_pop))

    def test_getBirthsDay(self):
        births_day = self.wo.births(timescale='day')
        # Output: Integer representing number of births today.
        self.assertIsInstance(births_day, int)
        print("Number of births the last day: " + str(births_day))

    def test_getBirthsYear(self):
        births_year = self.wo.births(timescale='year')
        # Output: Integer representing number of births in the year.
        self.assertIsInstance(births_year, int)
        print("Number of births the last year: " + str(births_year))

    def test_getDeathsDay(self):
        deaths_day = self.wo.deaths(timescale='day')
        # Output: Integer representing number of births today.
        self.assertIsInstance(deaths_day, int)
        print("Number of deaths the last day: " + str(deaths_day))

    def test_getDeathsYear(self):
        deaths_year = self.wo.deaths(timescale='year')
        # Output: Integer representing number of births in the year.
        self.assertIsInstance(deaths_year, int)
        print("Number of deaths the last year: " + str(deaths_year))

    def test_getDeathCausesYear(self):
        deaths_causes_year = self.wo.top_death_causes(timescale='year')
        # Output: dict of top death causes this year and Integer of numer of deaths.
        self.assertIsInstance(deaths_causes_year, dict)
        print("Top death causes and numbers this year: " + str(deaths_causes_year))

    def test_getDeathCausesDay(self):
        deaths_causes_day = self.wo.top_death_causes(timescale='day')
        # Output: dict of top death causes this day and Integer of numer of deaths.
        self.assertIsInstance(deaths_causes_day, dict)
        print("Top death causes and numbers this day: " + str(deaths_causes_day))

    def test_population_history(self):
        world_population_history = self.wo.population_history()
        # Output: Dictionary with the population history in the format {'year': value, 'population': value, 'growth': value}
        self.assertIsInstance(world_population_history, dict)
        print("World population history: " + str(world_population_history))

    def test_projection(self):
        world_population_history = self.wo.population_projection()
        # Output: Dictionary with the population growth in the format {'year': value, 'population': value, 'growth': value}
        self.assertIsInstance(world_population_history, dict)
        print("World population projection: " + str(world_population_history))

    def test_growth_scale(self):
        world_population_growth_day = self.wo.population_growth(timescale='day')
        world_population_growth_year = self.wo.population_growth(timescale='year')

        # Output: Integer with the population growth by timescale
        # self.assertIsInstance(world_population_history_day, int)
        # self.assertIsInstance(world_population_history_year, int)

        print("World population projection day: " + str(world_population_growth_day))
        print("World population projection year: " + str(world_population_growth_year))