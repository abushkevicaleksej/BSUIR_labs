import pickle
from model.FileRepository import FileRepository
import os
from view.Printer import Printer


class CompanyRepository(FileRepository):
    SAVE_FILE = "../company_state.pickle"

    @staticmethod
    def save_state(companies):
        with open(CompanyRepository.SAVE_FILE, 'wb') as f:
            pickle.dump(companies, f)

    @staticmethod
    def load_state():
        try:
            with open(CompanyRepository.SAVE_FILE, 'rb') as f:
                companies = pickle.load(f)
                print("Loaded companies:", companies)
                return companies
        except FileNotFoundError:
            #Printer.print_file_not_found()
            return []

    @staticmethod
    def state_exists():
        return os.path.exists(CompanyRepository.SAVE_FILE)