class Start:
    START_LIST = []

    def __init__(self, name: str, description: str):
        self.__id: int = Start.get_next_id()
        self.name: str = name
        self.description: str = description
        self.__gradebook: dict = {}
        Start.START_LIST.append(self)

    @staticmethod
    def get_next_id() -> int:
        largest_id = 0
        for start in Start.START_LIST:
            if start.__id > largest_id:
                largest_id = start.__id
        largest_id += 1
        return largest_id

    @staticmethod
    def get_by_id(start_id: int):
        for start in Start.START_LIST:
            if start.__id == int(start_id):
                return start

    def get_id(self) -> int:
        return self.__id

    def add_item(self, subject: str, mark: float) -> None:
        self.__gradebook[subject] = mark

    def get_grade(self, subject: str) -> float:
        return self.__gradebook[subject]

    def get_gradebook(self) -> dict:
        return self.__gradebook
