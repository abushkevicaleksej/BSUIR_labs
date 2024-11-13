from view.Printer import Printer
from model.ProjectRepository import ProjectRepository

class ProjectMenu:

    @staticmethod
    def project_menu(company, project):
        while True:
            Printer.print_proj_manag(project.get_proj_name())
            Printer.print_project_menu()
            choice = input("\nВыберите действие: ")

            if choice == '1' or choice == '2':
                employee_name = input("Введите имя сотрудника: ")
                employee = next((e for e in company.get_employees() if e.get_name() == employee_name), None)
                if employee is None:
                    Printer.print_no_emp()
                elif choice == '1':
                    project.add_employee(employee)
                elif choice == '2':
                    project.assign_support_employee(employee)
            elif choice == '3':
                if not project.get_support_employee():
                    Printer.print_no_support_emp()
                else:
                    project.test()
            elif choice == '4':
                print(project.get_info())
            elif choice == '5':
                company.remove_project(project)
                Printer.print_project_deleted(project.get_proj_name())
                break
            elif choice == '6':
                employee_name = input("Введите имя сотрудника, которого хотите снять с проекта: ")
                employee = next((e for e in project.get_employees() if e.get_name() == employee_name), None)
                if employee is None:
                    Printer.print_no_emp_on_project()
                else:
                    project.remove_employee(employee)
                    project.remove_support_employee(employee)
                    Printer.print_employee_removed_from_project(employee.get_name(), project.get_proj_name())

            elif choice == '7':
                ProjectRepository.save_state(project)
                break
            elif choice == '8':
                loaded_project = ProjectRepository.load_state()
                if loaded_project:
                    Printer.print_success_saving_file()
                    project = loaded_project
                else:
                    Printer.print_file_not_found()
            else:
                Printer.print_invalid_choose()