
class RepoTextFile:
    def __init__(self, save_file):
        self.__text_file_name = save_file
        self.__data = self.read_from_file()

    def read_from_file(self):
        lines = list()
        try:
            with open(self.__text_file_name, "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"File not found! Input = {self.__text_file_name}")
        return lines

    def write_to_file(self, user_input):
        try:
            with open(self.__text_file_name, "a") as f:
                f.write("\n")
                f.write(str(user_input))
        except FileNotFoundError:
            print(f"File not found! Input = {self.__text_file_name}")

    def repo_add(self, entity):
        self.__data.append(entity)
        self.write_to_file(entity)

    def get_entity(self, index):
        return self.__data[index]

    def get_all(self):
        return self.__data
