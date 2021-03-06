from enums import Session


class InvalidValueException(Exception):
    pass


class Step:
    def __init__(self, number_of_sessions, number_of_stars):
        self.number_of_sessions = number_of_sessions
        self.number_of_stars = number_of_stars

    def make_step(self):
        try:
            if self.number_of_sessions not in Session.NUMBER_TO_TEXT_MAP:
                raise InvalidValueException("Invalid number of sessions")
            if self.number_of_stars not in ["one", "two", "three", "four", "five"]:
                raise InvalidValueException("Invalid number of stars")
        except InvalidValueException as ex:
            print(ex)
        else:
            a = Session.NUMBER_TO_TEXT_MAP[self.number_of_sessions]
            for key, value in Session.NUMBER_TO_TEXT_MAP.items():
                if value == self.number_of_stars:
                    b = key
            print("I completed " + a + " sessions and I rated my experience " + str(b) + " stars")

if __name__ == "__main__":
    Step(2, "five").make_step()
    Step(0, "five").make_step()
    Step(2, "ten").make_step()
