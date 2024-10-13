class EBook(Book):
    def __init__(self, title: str, author: str, page_count: int, size: float, registration_code: str):
        """
        Initialize an EBook object.
        :param title: Title of the book (inherited from Book).
        :param author: Author of the book (inherited from Book).
        :param page_count: Page count of the book (inherited from Book).
        :param size: Size of the eBook in MB.
        :param registration_code: Registration code, must be 16 digits to be valid.
        """
        # Initialize parent class attributes using super()
        super().__init__(title, author, page_count)

        # Initialize size and registration code
        self.size = size

        # Validate the registration code and set it
        if self.check_code(registration_code):
            self._registration_code = registration_code
        else:
            self._registration_code = None

    @staticmethod
    def check_code(registration_code: str) -> bool:
        """
        Static method to check if the registration code is valid.
        :param registration_code: A string representing the registration code.
        :return: True if the code is valid (16 digits), False otherwise.
        """
        # Check if the code is a string of exactly 16 digits
        return isinstance(registration_code, str) and registration_code.isdigit() and len(registration_code) == 16

    @property
    def registration_code(self) -> str:
        """
        Getter for the registration code.
        :return: The current registration code.
        """
        return self._registration_code

    @registration_code.setter
    def registration_code(self, new_code: str):
        """
        Setter for the registration code.
        The code will be updated only if it is valid.
        :param new_code: The new registration code to be set.
        """
        if self.check_code(new_code):
            self._registration_code = new_code
        else:
            self._registration_code = None



ebook = EBook("Hosi od Bobri reky", "Jaroslav Foglar", 300, 2.5, "1234567890123456")
print(ebook.registration_code)