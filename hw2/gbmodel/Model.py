class Model():
    def select(self: "model") -> tuple:
        """
        Gets all entries from the database
        :return: Tuple containing all rows of database
        """
        pass

    def insert(self: "model", task: "str", date: "date", due_date: "date", description: "str") -> bool:
        """
        Inserts a new entry into the database
        :param task: Task name
        :param date: Date of task creation
        :param due_date: Date of task due
        :param description: Description of task
        :return: None
        """
        pass
