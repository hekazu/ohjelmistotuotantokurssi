class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True

        return False


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value


class All:
    def test(self, player):
        return True


class Not:
    def __init__(self, matcher):
        self._matcher = matcher

    def test(self, player):
        return not self._matcher.test(player)


class HasFewerThan:
    def __init__(self, value, attr):
        self._matcher = Not(HasAtLeast(value,attr))

    def test(self, player):
        return self._matcher.test(player)


class QueryBuilder:
    def __init__(self,query_components=All()):
        self.query_components = query_components

    def playsIn(self, team):
        return QueryBuilder(And(PlaysIn(team),self.query_components))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(HasAtLeast(value,attr),self.query_components))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(HasFewerThan(value,attr),self.query_components))

    def build(self):
        return self.query_components

    def oneOf(self, matcher1, matcher2):
        return QueryBuilder(Or(matcher1, matcher2))
