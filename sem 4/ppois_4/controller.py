from model.FileRepository import FileRepository
from model.CompanyManager import CompanyManager
import web


class Controller:
    def __init__(self):
        self.model: FileProvider = FileProvider()

    def run(self):
        web.run_web()


class FileProvider:
    FileRepo: FileRepository = None
    Company: CompanyManager = None

    def __init__(self):
        if self.FileRepo is None:
            self.Repository = FileRepository("project_state.pickle")
        if self.Company is None:
            self.Company = CompanyManager(self.Repository)
