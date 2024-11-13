from flask import Flask, request, render_template, redirect, url_for, session, flash
from model.ITCompany import ITCompany
from model.Project import Project
from model.Employee import Employee
from model.Customer import Customer
from model.Investor import Investor
from model.CompanyRepository import CompanyRepository
from model.ProjectRepository import ProjectRepository

app = Flask(__name__)
app.secret_key = 'SECRET_KEY'
companies: list[ITCompany] = []

company_repository = CompanyRepository()
project_repository = ProjectRepository()


@app.route('/')
@app.route('/index')
def index():
    if companies:
        company_name = companies[0].get_name()
        return redirect(url_for('main', company_name=company_name))
    else:
        return render_template('index.html')


@app.route('/save_data')
def save_data():
    if companies:
        company = companies[0]
    projects = company.get_projects()
    company_repository.save_state(companies)
    project_repository.save_state(projects)
    return '', 204


@app.route('/add_company', methods=['POST'])
def add_company():
    name = request.form['name']
    initial_budget = request.form['initial_budget']
    location = request.form['location']

    if not all(char.isalpha() or char.isspace() for char in name):
        flash("Неверное имя компании. Допускается вводить символы алфавита.", "danger")
        return redirect(url_for('index'))

    error_initial_budget = None
    try:
        initial_budget = float(initial_budget)
        if initial_budget < 0:
            error_initial_budget = "Бюджет компании не может быть представлен отрицательным числом."
    except ValueError:
        error_initial_budget = "Неверный формат бюджета. Пожалуйста, введите число."

    if error_initial_budget:
        flash(error_initial_budget, "danger")
        return redirect(url_for('index'))

    new_company = ITCompany(name, initial_budget, location)
    companies.append(new_company)
    return redirect(url_for('main', company_name=new_company.get_name()))


@app.route('/main/<company_name>')
def main(company_name):
    print("Requested company:", company_name)
    company = next((c for c in companies if c.get_name() == company_name), None)
    if company is None:
        return "Company not found.", 404
    return render_template('main.html', company=company)


@app.route('/delete_company', methods=['POST'])
def delete_company():
    company_name = request.form['company_name']
    company_to_delete = None
    for company in companies:
        if company.get_name() == company_name:
            company_to_delete = company
            break
    if company_to_delete:
        companies.remove(company_to_delete)
        flash(f'Компания {company_name} успешно удалена!', 'success')
        return redirect(url_for('index'))
    else:
        flash('Компания не найдена', 'error')
        return redirect(url_for('index'))


@app.route('/go_to_account/<company_name>/<client_name>', methods=['POST'])
def go_to_account(company_name, client_name):
    customer_name = request.form['client_name']
    company_name = request.form['company_name']

    for company in companies:
        if company.get_name() == company_name:
            break
    else:
        flash('Компания не найдена.', 'error')
        return redirect(url_for('index'))

    if not customer_name.isalpha():
        flash('Имя клиента должно содержать только буквы.', 'error')
        return redirect(url_for('index'))

    customer = company.get_customer_by_name(customer_name)
    if customer:
        return redirect(url_for('account', client_name=customer_name))
    else:
        flash('Клиент не найден.', 'error')
        return redirect(url_for('index'))


@app.route('/account/<client_name>')
def account():
    client_name = request.form['client_name']
    return render_template('account.html', client_name=client_name)


@app.route('/add_client', methods=['POST'])
def add_client():
    client_type = request.form['client_type']
    company_name = request.form['company_name']
    for company in companies:
        if company.get_name() == company_name:
            break
    else:
        flash('Компания не найдена.', 'error')
        return redirect(url_for('index'))
    if client_type == 'заказчик':
        name = request.form['customer_name']
        if not name.isalpha():
            flash('Имя должно содержать только буквы.', 'danger')
            return redirect(url_for('main', company_name=company_name))
        flash(f'Клиент {name} добавлен как заказчик.', 'success')
        company.get_client_manager().add_client(Customer(name))

    elif client_type == 'инвестор':
        available_projects = company.get_projects()
        if available_projects:
            name = request.form['investor_name']
            invested_amount = request.form['invested_amount']
            try:
                invested_amount = float(invested_amount)
                if invested_amount <= 0:
                    flash('Инвестиции должны быть отличными от нуля.', 'danger')
                    return redirect(url_for('main', company_name=company_name))
            except ValueError:
                flash('Сумма инвестиций должна быть положительным числом.', 'error')
                return redirect(url_for('main', company_name=company_name))

            project_choice = int(request.form['project_choice'])
            selected_project = available_projects[project_choice - 1]

            investor = Investor(name, invested_amount)
            investor.invest_in_project(selected_project, invested_amount)
            company.increase_budget(invested_amount)
            selected_project.add_investor(investor, invested_amount)
            company.get_client_manager().add_client(investor)
            flash(f'Инвестор {name} добавлен с инвестициями в проект {selected_project.get_proj_name()}.', 'success')
        else:
            flash('Нет доступных проектов для инвестирования.', 'error')
    return redirect(url_for('main', company_name=company_name))


@app.route('/make_order', methods=['POST'])
def make_order():
    company_name = request.form['company_name']
    customer_name = request.form['customer_name']
    make_order(company_name, customer_name)  # Implement this function
    return redirect(url_for('account', client_name=customer_name))


@app.route('/company/<company_name>')
def company_details(company_name):
    company = next((c for c in companies if c.get_name() == company_name), None)
    if company is None:
        return "Company not found", 404
    return render_template('company.html', company=company)


@app.route('/update_company_name/<company_name>', methods=['POST'])
def update_company_name(company_name):
    company = next((c for c in companies if c.get_name() == company_name), None)
    if company is None:
        flash('Компания не найдена', 'error')
        return redirect(url_for('company_details', company_name=company_name))
    new_name = request.form['new_name']
    if not all(char.isalpha() or char.isspace() for char in new_name):
        flash('Недопустимое имя компании. Разрешены только буквы.', 'error')
        return redirect(url_for('company_details', company_name=company_name))
    company.set_name(new_name)
    flash(f'Имя компании успешно изменено на {new_name}!', 'success')
    return redirect(url_for('company_details', company_name=new_name))


@app.route('/add_employee/<company_name>', methods=['POST'])
def add_employee(company_name):
    try:
        company_name = request.form['company_name']
        company = next((c for c in companies if c.get_name() == company_name), None)

        if company is None:
            flash("Компания не найдена", "danger")
            return redirect(url_for('index'))  # Replace 'index' with the appropriate route

        name = request.form['employee_name']
        if not all(char.isalpha() or char.isspace() for char in name):
            flash("Имя должно состоять только из букв и пробелов.", "danger")
            return redirect(url_for('company_details', company_name=company_name))

        age = int(request.form['employee_age'])
        position_value = request.form['employee_pos']
        language_value = request.form['employee_lang']
        level_value = request.form['employee_level']
        work_experience = int(request.form['employee_work_exp'])
        salary = int(request.form['salary'])

        if age <= 18:
            flash("Возраст должен быть целым, положительным числом, больше 18.", "danger")
            return redirect(url_for('company_details', company_name=company_name))
        if work_experience < 0:
            flash("Опыт работы не может быть отрицательным.", "danger")
            return redirect(url_for('company_details', company_name=company_name))
        if work_experience > age - 18:
            flash("Слишком большой стаж работы для такого возраста.", "danger")
            return redirect(url_for('company_details', company_name=company_name))
        if salary <= 0:
            flash("Зарплата должна быть положительным, отличным от нуля числом.", "danger")
            return redirect(url_for('company_details', company_name=company_name))

        project_budget = company.get_budget()
        if salary > project_budget:
            flash("Зарплата сотрудника превышает бюджет компании.", "danger")
            return redirect(url_for('company_details', company_name=company_name))

        employee = Employee(name, age, work_experience, language_value, position_value, level_value, salary)
        company.add_employee(employee)
        flash("Сотрудник успешно добавлен!", "success")
        return redirect(url_for('company_details', company_name=company_name))  # Replace with the appropriate route

    except Exception as e:
        flash(str(e), "danger")
        return redirect(url_for('company_details', company_name=company_name))  # Replace with the appropriate route


@app.route('/add_project/<company_name>', methods=['POST'])
def add_project(company_name):
    company = next((c for c in companies if c.get_name() == company_name), None)
    if company is None:
        flash('Компания не найдена', 'error')
        return redirect(url_for('company_details', company_name=company_name))

    name = request.form['project_name']
    try:
        budget = float(request.form['project_budget'])
        if budget < 0:
            flash("Бюджет проекта не может быть отрицательным.", "danger")
            return redirect(url_for('company_details', company_name=company_name))
        if company.get_budget() < budget:
            flash("Бюджет проекта слишком большой.", "danger")
            return redirect(url_for('company_details', company_name=company_name))
    except ValueError as e:
        flash(str(e), 'error')
        return redirect(url_for('company_details', company_name=company_name))

    project = Project(name, budget)
    company.add_project(project)
    flash(f'Проект {name} успешно добавлен!', 'success')
    return redirect(url_for('company_details', company_name=company_name))


@app.route('/delete_employee/<company_name>', methods=['POST'])
def delete_employee(company_name):
    company = next((c for c in companies if c.get_name() == company_name), None)
    if company is None:
        flash('Компания не найдена', 'danger')
        return redirect(url_for('company_details', company_name=company_name))
    name_to_remove = request.form['employee_name']
    try:
        company.remove_employee_by_name(name_to_remove)
        flash(f'Сотрудник {name_to_remove} успешно удален!', 'success')
        return redirect(url_for('company_details', company_name=company_name))
    except ValueError as e:
        flash(f"Ошибка при удалении сотрудника: {str(e)}", 'danger')
        return redirect(url_for('company_details', company_name=company_name))


@app.route('/manage_project', methods=['POST'])
def manage_project():
    project_name = request.form['project_name']
    company_name = request.form['company_name']
    company = next((c for c in companies if c.get_name() == company_name), None)
    if company is None:
        return "Company not found", 404
    project = next((p for p in company.get_projects() if p.get_proj_name() == project_name), None)
    if project is None:
        return "Project not found", 404
    return redirect(url_for('project_management', company_name=company_name, project_name=project_name))


@app.route('/company/<company_name>/project/<project_name>/manage')
def project_management(company_name, project_name):
    company = next((c for c in companies if c.get_name() == company_name), None)
    if company is None:
        return "Company not found", 404

    project = next((p for p in company.get_projects() if p.get_proj_name() == project_name), None)
    if project is None:
        return "Project not found", 404
    return render_template('project.html', company=company, project=project)


@app.route('/add_employee_to_project/<company_name>/<project_name>', methods=['POST'])
def add_employee_to_project(company_name, project_name):
    employee_name = request.form['employee_name']
    company = next((c for c in companies if c.get_name() == company_name), None)
    if company is None:
        flash('Компания не найдена', 'error')
        return redirect(url_for('project_management', company_name=company_name))
    project = next((p for p in company.get_projects() if p.get_proj_name() == project_name), None)
    if project is None:
        flash('Проект не найден', 'error')
        return redirect(url_for('project_management', company_name=company_name))
    employee = next((e for e in company.get_employees() if e.get_name() == employee_name), None)
    if employee is None:
        flash('Сотрудник не найден', 'error')
        return redirect(url_for('project_management', company_name=company_name, project_name=project_name))
    project.add_employee(employee)
    flash(f'Сотрудник {employee_name} успешно добавлен на проект {project_name}!', 'success')
    return redirect(url_for('project_management', company_name=company_name, project_name=project_name))


@app.route('/assign_project_manager/<company_name>/<project_name>', methods=['POST'])
def assign_project_manager(company_name, project_name):
    employee_name = request.form['employee_name']
    company = next((c for c in companies if c.get_name() == company_name), None)
    if company is None:
        flash('Компания не найдена', 'danger')
        return redirect(url_for('project_management', company_name=company_name))
    project = next((p for p in company.get_projects() if p.get_proj_name() == project_name), None)
    if project is None:
        flash('Проект не найден', 'danger')
        return redirect(url_for('project_management', company_name=company_name))
    if not project.get_employees():
        flash('Сотрудник не найден', 'danger')
        return redirect(url_for('project_management', company_name=company_name, project_name=project_name))
    employee = next((e for e in company.get_employees() if e.get_name() == employee_name), None)
    if employee is None:
        flash('Сотрудник не найден', 'danger')
        return redirect(url_for('project_management', company_name=company_name, project_name=project_name))
    project.assign_support_employee(employee)
    flash(f'Сотрудник {employee_name} назначен ответственным за проект {project_name}!', 'success')
    return redirect(url_for('project_management', company_name=company_name, project_name=project_name))


@app.route('/remove_project/<company_name>/<project_name>', methods=['POST'])
def remove_project(company_name, project_name):
    company = next((c for c in companies if c.get_name() == company_name), None)
    if company is None:
        flash('Компания не найдена', 'error')
        return redirect(url_for('company_details', company_name=company_name))
    project = next((p for p in company.get_projects() if p.get_proj_name() == project_name), None)
    if project is None:
        flash('Проект не найден', 'error')
        return redirect(url_for('company_details', company_name=company_name))
    company.remove_project(project)
    flash(f'Проект {project_name} успешно удален!', 'success')
    return redirect(url_for('company_details', company_name=company_name))


@app.route('/remove_employee_from_project/<company_name>/<project_name>', methods=['POST'])
def remove_employee_from_project(company_name, project_name):
    employee_name = request.form['employee_name']
    company = next((c for c in companies if c.get_name() == company_name), None)
    if company is None:
        return "Company not found", 404
    project = next((p for p in company.get_projects() if p.get_proj_name() == project_name), None)
    if project is None:
        return "Project not found", 404
    employee = next((e for e in project.get_employees() if e.get_name() == employee_name), None)
    if employee is None:
        return "Employee not found", 404
    project.remove_employee(employee)
    project.remove_support_employee(employee)
    flash(f'Сотрудник {employee_name} был удален с проекта.', 'success')
    return redirect(url_for('project_management', company_name=company_name, project_name=project_name))


@app.route('/test_project/<company_name>/<project_name>', methods=['POST'])
def test_project(company_name, project_name):
    company = next((c for c in companies if c.get_name() == company_name), None)
    if company is None:
        flash('Компания не найдена', 'danger')
        return redirect(url_for('project_management'))
    project = next((p for p in company.get_projects() if p.get_proj_name() == project_name), None)
    if project is None:
        flash('Проект не найден', 'danger')
        return redirect(url_for('project_management', company_name=company_name))
    if project.get_tested():
        flash('Проект уже тестирован', 'danger')
        return redirect(url_for('project_management', company_name=company_name))
    emps = project.get_employees()
    if not emps:
        flash('Нет сотрудников для тестирования данного проекта.', 'danger')
        return redirect(url_for('project_management', company_name=company_name, project_name=project_name))
    project.test()
    flash('Тестирование проекта успешно выполнено!', 'success')
    return redirect(url_for('project_management', company_name=company_name, project_name=project_name))


def run():
    app.run(debug=True)
