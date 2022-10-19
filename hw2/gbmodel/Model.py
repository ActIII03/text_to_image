class Model():
    def select(self: "model") -> tuple:
        """
        Gets all entries from the database
        :return: Tuple containing all rows of database
        """
        pass

    def insert(self: "model", task: str, date: date, description: str) -> None:
        """
        Inserts a new entry into the database
        :param task: Task name
        :param date: Date of task
        :param description: Description of task
        :return: None
        """
        pass
