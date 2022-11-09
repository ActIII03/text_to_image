class Model():
    def select(self):
        """
        Gets all entries from the database
        :return: Tuple containing all rows of database
        """
        pass

    def insert(self, task, date, due_date, description):
        """
        Inserts a new entry into the database
        :param task: Task name
        :param date: Date of task creation
        :param due_date: Date of task due
        :param description: Description of task
        :return: None
        """
        pass
    def delete(self, task):
        """
        Deletes an entry from the database
        :param task: Task name
        :return: None
        """
        pass