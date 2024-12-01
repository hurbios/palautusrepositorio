from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or

class QueryBuilder:
    def __init__(self, stack=All()):
        self._stack = stack

    def plays_in(self, team):
        return QueryBuilder(And(self._stack, PlaysIn(team)))

    def has_at_least(self, value, attr):
        return QueryBuilder(And(self._stack, HasAtLeast(value, attr)))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self._stack, HasFewerThan(value, attr)))

    def one_of(self, stack1, stack2):
        return QueryBuilder(And(self._stack, Or(stack1, stack2)))

    def build(self):
        return self._stack
