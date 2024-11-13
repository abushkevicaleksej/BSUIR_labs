import pickle


class FileRepository():
    def __init__(self, filename: str):
        self.filename = filename

    def save(self, obj) -> None:
        with open(self.filename, "wb") as outfile:
            pickle.dump(obj, outfile)
        print(f"Saved object to {self.filename}")

    def load(self):
        try:
            with open(self.filename, "rb") as infile:
                obj = pickle.load(infile)
            print(f"Loaded object from {self.filename}")
            return obj
        except FileNotFoundError:
            print(f"Loaded failed!")