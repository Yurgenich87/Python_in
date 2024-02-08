import warnings

warnings.filterwarnings('ignore')


class InvalidTextError(Exception):
    pass


class InvalidNumberError(Exception):
    pass


class Archive:
    _instance = None

    def __new__(cls, text, number):
        if cls._instance is None:
            cls._instance = super(Archive, cls).__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        return cls._instance

    def __init__(self, text, number):
        self.text = text
        self.number = number
        try:
            if not isinstance(text, str) or text == "":
                raise InvalidTextError(f"Invalid text: {text}. Text should be a non-empty string.")
            if not (isinstance(number, int) and number > 0) and not (isinstance(number, float) and number > 0):
                raise InvalidNumberError(f"Invalid number: {number}. Number should be a positive integer or float.")
            self._instance.archive_text.append(text)
            self._instance.archive_number.append(number)

        except (InvalidTextError, InvalidNumberError) as e:
            return

    def __str__(self):
        return f"Text is {self.text} and number is {self.number}. Also {self._instance.archive_text} and {self._instance.archive_number}"

    def __repr__(self):
        return f"Archive('{self.text}', {self.number})"


invalid_archive_instance = Archive("", -5)
print(invalid_archive_instance)


# archive_instance = Archive("Sample text", 42.5)
# print(archive_instance)
