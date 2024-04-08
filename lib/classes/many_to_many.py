class NationalPark:

    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    # Create a property method that returns the name of the national park
    @property
    def name(self):
        return self.__name

    # Create a setter method that sets the name of the national park
    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, "name") and len(name) >= 3:
            self.__name = name
        else:
            raise Exception

    # Return a list of trips that have visited the national park
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]

    # Return a list of visitors that have visited the national park
    def visitors(self):
        return list(set([trip.visitor for trip in self.trips()]))

    # Return the total number of visits to the national park
    def total_visits(self):
        return len(self.trips())

    # Return the visitor that has visited the national park the most
    def best_visitor(self):
        visitors = [trip.visitor for trip in self.trips()]
        return max(set(visitors), key=visitors.count)

    # Return the national park that has been visited the most
    @classmethod
    def most_visited(cls):
        return max(cls.all, key=lambda park: park.total_visits())


class Trip:

    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        type(self).all.append(self)

    # Create a property method that returns the visitor of the trip
    @property
    def start_date(self):
        return self._start_date

    # Create a setter method that sets the visitor of the trip
    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7:
            self._start_date = start_date
        else:
            raise Exception

    # Create a property method that returns the national park of the trip
    @property
    def end_date(self):
        return self._end_date

    # Create a setter method that sets the national park of the trip
    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7:
            self._end_date = end_date
        else:
            raise Exception

    # Create a property method that returns the visitor of the trip
    @property
    def visitor(self):
        return self._visitor

    # Create a setter method that sets the visitor of the trip
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            raise Exception

    # Create a property method that returns the national park of the trip
    @property
    def national_park(self):
        return self._national_park

    # Create a setter method that sets the national park of the trip
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise Exception


class Visitor:

    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    # Create a property method that returns the name of the visitor
    @property
    def name(self):
        return self._name

    # Create a setter method that sets the name of the visitor
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception

    # Return a list of trips that the visitor has taken
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]

    # Return a list of national parks that the visitor has visited
    def national_parks(self):
        return list(set([trip.national_park for trip in self.trips()]))

    # Return the total number of trips the visitor has taken
    def total_visits_at_park(self, park):
        if not isinstance(park, NationalPark):
            raise Exception

        if not park.visitors():
            return 0

        return len([trip for trip in self.trips() if trip.national_park == park])
