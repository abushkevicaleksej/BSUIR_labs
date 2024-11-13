import pickle
from model.FileRepository import FileRepository
from view.Printer import Printer
import os


class ProjectRepository(FileRepository):
    SAVE_FILE = "../project_state.pickle"

    @staticmethod
    def save_state(project):
        with open(ProjectRepository.SAVE_FILE, 'wb') as f:
            pickle.dump(project, f)
        Printer.print_success_saving_file()

    @staticmethod
    def load_state():
        try:
            with open(ProjectRepository.SAVE_FILE, 'rb') as f:
                projects = pickle.load(f)
                print("Loaded projects:", projects)
                return projects
        except FileNotFoundError:
           # Printer.print_file_not_found()
            return []

    @staticmethod
    def state_exists():
        return os.path.exists(ProjectRepository.SAVE_FILE)