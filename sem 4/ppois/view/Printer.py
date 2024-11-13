
class Printer:
    @staticmethod
    def print_company_was_deleted():
        print("Компания успешно удалена.")

    @staticmethod
    def print_active_orders():
        print("Активные заказы:")

    @staticmethod
    def print_invest_about_project(self_name, amount, self_budget):
        print(f"Проект {self_name} получил инвестицию в размере {amount}. Новый бюджет проекта: {self_budget}")

    @staticmethod
    def print_become_investor():
        print("Вы стали инвестором!")

    @staticmethod
    def print_your_orders():
        print("Ваши заказы:")

    @staticmethod
    def print_no_proj_invest():
        print("В данный момент нет доступных проектов для инвестирования.")

    @staticmethod
    def print_invalid_number_proj():
        print("Ошибка: Введите целое число для выбора проекта.")

    @staticmethod
    def print_invalid_proj():
        print("Некорректный выбор проекта.")

    @staticmethod
    def print_proj_manag(project_name):
        print(f"\nУправление проектом {project_name}")

    @staticmethod
    def print_no_emp():
        print("Такого сотрудника нет. Пожалуйста, добавьте его сначала.")

    @staticmethod
    def print_invalid_choose():
        print("Некорректный выбор. Пожалуйста, выберите существующий пункт.")

    @staticmethod
    def print_file_not_found():
        print("Файл состояния не найден.")

    @staticmethod
    def print_no_client():
        print("Такого клиента нет.")

    @staticmethod
    def print_success_saving_file():
        print("Состояние успешно сохранено.")

    @staticmethod
    def print_low_age_error():
        print("Возраст сотрудника должен быть не меньше 18 лет.")

    @staticmethod
    def print_high_age_error():
        print("Возраст сотрудника должен быть не больше 60 лет.")

    @staticmethod
    def print_emp_on_proj(employee_name, self_name):
        print(f"Сотрудник {employee_name} назначен ответственным за поддержку проекта {self_name}.")

    @staticmethod
    def print_proj_has_tested(self_name):
        print(f"Проект {self_name} успешно протестирован.")

    @staticmethod
    def print_emp_arent_on_proj(employee_name, self_name):
        print(f"Сотрудник {employee_name} не является частью проекта {self_name} и не может быть назначен ответственным за поддержку.")

    @staticmethod
    def print_incorrect_invest():
        print("Сумма инвестиций должна быть положительной.")

    @staticmethod
    def print_order_success_added():
        print("Заказ успешно добавлен!")

    @staticmethod
    def print_valid_name():
        print("Имя клиента должно состоять только из букв.")

    @staticmethod
    def print_valid_sum():
        print("Ошибка при вводе суммы инвестиций:")

    @staticmethod
    def print_all_proj_for_invest():
        print("Доступные проекты для инвестирования:")

    @staticmethod
    def print_welcome():
        print("Добро пожаловать! Для начала создайте новую IT-компанию.")

    @staticmethod
    def print_error_company():
        print("Вы ввели неверное имя компании. Допускается вводить символы алфавита.")

    @staticmethod
    def print_error_salary():
        print("Ошибка: Зарплата не может превышать бюджет компании.")

    @staticmethod
    def print_no_money_for_proj(project_name):
        print(f"Недостаточно средств для добавления проекта '{project_name}'.")

    @staticmethod
    def print_successfull_del(name_to_remove):
        print(f"Сотрудник {name_to_remove} успешно уволен.")

    @staticmethod
    def print_project_was_successfully_added(project_name,self_budget):
        print(f"Проект '{project_name}' успешно добавлен. Оставшийся бюджет компании: {self_budget}")

    @staticmethod
    def print_no_emps_on_order():
        print("Выполнение этого заказа невозможно! На нём отсутствуют сотрудники")

    @staticmethod
    def print_order_success_with_name(order_name):
        print(f"Заказ '{order_name}' успешно выполнен.")

    @staticmethod
    def print_no_order_by_name():
        print("Заказ с таким названием не найден.")

    @staticmethod
    def print_programming_lang():
        print(f"Выберите язык программирования:")

    @staticmethod
    def print_incorrect_royalty_input():
        print("Ошибка: Неверный ввод зарплаты.")

    @staticmethod
    def print_add_emp_error():
        print("Ошибка при добавлении сотрудника:")

    @staticmethod
    def print_choose_job():
        print(f"Выберите должность:")

    @staticmethod
    def print_error_input():
        print("Ошибка при вводе бюджета проекта:")

    @staticmethod
    def print_the_same_proj():
        print("Проект с таким именем уже существует.")


    @staticmethod
    def print_error_choose_proj():
        print("Ошибка: Некорректный выбор проекта.")

    @staticmethod
    def print_error_choose_proj_number():
        print("Ошибка: Введите число для выбора проекта.")

    @staticmethod
    def print_no_proj_error():
        print("Проекты отсутствуют. Создайте новый проект.")

    @staticmethod
    def print_no_jobs():
        print("Должности отсутствуют")

    @staticmethod
    def print_no_emps():
        print("Сотрудники отсутствуют")

    @staticmethod
    def print_no_clients():
        print("Клиенты отсутствуют")

    @staticmethod
    def print_no_order():
        print("Заказы отсутствуют.")

    @staticmethod
    def print_missing_positions_for_order():
        print("Для выполнения проекта необходим хотя бы 1 разработчик, тестер и дизайнер.")

    @staticmethod
    def print_empty_company_name():
        print("Название компании не может быть пустым. Пожалуйста, попробуйте еще раз.")

    @staticmethod
    def print_invalid_budget():
        print("Бюджет компании не может быть отрицательным. Пожалуйста, попробуйте еще раз.")

    @staticmethod
    def print_no_emps_for_order():
        print("Заказ не может быть выполнен: отсутствуют сотрудники.")

    @staticmethod
    def print_order_has_marked():
        print("Заказ успешно отмечен как выполненный.")

    @staticmethod
    def print_invalid_format():
        print("Неверный формат бюджета. Пожалуйста, введите число.")

    @staticmethod
    def print_invalid_location():
        print("Место дислокации должно быть строкой. Пожалуйста, попробуйте еще раз.")

    @staticmethod
    def print_invalid_input():
        print("Некорректный номер заказа.")

    @staticmethod
    def print_no_free_emps():
        print("Доступных сотрудников нет.")

    @staticmethod
    def print_no_order_found():
        print("Заказ с таким номером не найден.")

    @staticmethod
    def print_incorrect_lang_input():
        print("Ошибка: Некорректный выбор языка программирования.")

    @staticmethod
    def print_error_order_name(e):
        print("Ошибка при вводе названия заказа:", e)

    @staticmethod
    def print_error_lang_exept():
        print("Извините, компания не занимается разработкой на введенных языках")

    @staticmethod
    def print_deadline_error(e):
        print("Ошибка при вводе дедлайна заказа:", e)

    @staticmethod
    def print_error_budget(e):
        print("Ошибка при вводе бюджета заказа:", e)

    @staticmethod
    def print_all_pr_langs():
        print("Доступные языки программирования:")

    @staticmethod
    def print_all_lang_by_value(lang_value):
        print(lang_value)

    @staticmethod
    def print_project_deleted(project_name):
        print(f"Проект '{project_name}' успешно удалён.")

    @staticmethod
    def print_order_deleted_successfully(order_name):
        print(f"Заказ '{order_name}' успешно удален!")

    @staticmethod
    def print_order_not_found(order_name):
        print("Удаляемый заказ не найден.")

    @staticmethod
    def print_incorrect_position_input():
        print("Ошибка: Некорректный выбор должности.")

    @staticmethod
    def print_name_error():
        print("Имя должно состоять только из букв.")

    @staticmethod
    def print_no_support_emp():
        print("Данный проект не может быть протестирован! Отсутствует сотрудник!")

    @staticmethod
    def print_invalid_number():
        print("Возраст должен быть представлен числом.")

    @staticmethod
    def print_no_emp_on_project():
        print("Такой сотрудник не задействован на проекте.")

    @staticmethod
    def print_employee_removed_from_project(employee_name, project_name):
        print(f"Сотрудник '{employee_name}' успешно был снят с проекта '{project_name}'")

    @staticmethod
    def print_company_menu():
        print("\n1. Изменить имя компании")
        print("2. Добавить сотрудника")
        print("3. Добавить проект")
        print("4. Управление проектами")
        print("5. Вывести информацию о компании")
        print("6. Вывести все проекты")
        print("7. Вывести всех сотрудников")
        print("8. Вывести всех клиентов")
        print("9. Просмотреть все заказы")
        print("10. Назад")
        print("11. Сохранение состояния")
        print("12. Загрузка состояния")
        print("13. Уволить сотрудника")

    @staticmethod
    def print_main_menu():
        print("\n1. Посмотреть меню редактирования компании")
        print("2. Стать клиентом")
        print("3. Личный кабинет")
        print("4. Сохранить и выйти")
        print("5. Удалить компанию")

    @staticmethod
    def print_customer_menu():
        print("\nМеню заказчика")
        print("1. Сделать заказ")
        print("2. Мои заказы")
        print("3. Выполненные заказы")
        print("4. Удалить заказ")
        print("5. Назад")

    @staticmethod
    def show_orders():
        print("\n1. Посмотреть заказы")
        print("2. Отметить заказ как выполненный")
        print("3. Назначить сотрудников на заказ")
        print("4. Назад")

    @staticmethod
    def print_project_menu():
        print("1. Назначить сотрудника на проект")
        print("2. Назначить сотрудника ответственным за поддержку")
        print("3. Протестировать проект")
        print("4. Вывести информацию о проекте")
        print("5. Удалить проект")
        print("6. Снять сотрудника с проекта")
        print("7. Назад")
        print("8. Сохранение состояния")
        print("9. Загрузка состояния")

    @staticmethod
    def print_orders(orders):
        if orders:
            for idx, order in enumerate(orders, start=1):
                print(f"{idx}. {order.get_info()}")
        else:
            print("Заказы отсутствуют.")

    @staticmethod
    def print_employee_info(employee):
        print(employee.get_info())

    @staticmethod
    def print_project_info(project):
        print(project.get_info())

    @staticmethod
    def print_role_names(roles):
        if roles:
            for role in roles:
                print(role.name)
        else:
            print("Должности отсутствуют")

    @staticmethod
    def print_clients(clients):
        if clients:
            for client in clients:
                print(f"Имя: {client.name}, Тип: {type(client).__name__}")
        else:
            print("Клиенты отсутствуют")
