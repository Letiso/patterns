from abc import ABC, abstractmethod


# Products
class EmployeeReport:
    def __init__(self):
        self._data = ['*' * 40]

    def __str__(self):
        return '\n'.join(self._data)

    def add_part(self, *args):
        for arg in args:
            self._data.append(arg)


class ClientReport:
    def __init__(self):
        self._data = ['-' * 40]

    def __str__(self):
        return '\n'.join(self._data)

    def add_part(self, *args):
        for arg in args:
            self._data.append(arg)


# Builders interface
class ReportBuilder(ABC):
    @abstractmethod
    def reset(self): pass

    @abstractmethod
    def add_personal_info(self): pass

    @abstractmethod
    def add_business_info(self): pass

    @abstractmethod
    def add_extended_info(self): pass

    @abstractmethod
    def get_report(self): pass


# Concrete builders
class EmployeeReportBuilder(ReportBuilder):
    def __init__(self):
        self._report = None

    def reset(self):
        self._report = EmployeeReport()
        self._report.add_part(f"Current report type:\n\t{self._report.__class__.__name__}\n")

    def add_personal_info(self):
        first_name, last_name = 'John', 'Switcher'
        self._report.add_part(f"Name: {first_name} {last_name}")

        gender = 'Male'
        self._report.add_part(f"Gender: {gender}")

        age = '33'
        self._report.add_part(f"Age: {age}")

        address = 'Testing street, 3\\14'
        self._report.add_part(f"Address: {address}")

    def add_business_info(self):
        status = 'Python-developer'
        self._report.add_part(f"\nStatus: {status}")

        skills = ['Skill', 'Skill', 'Skill']
        self._report.add_part("Skills:", *[f"\t{skill}" for skill in skills])

        hours = '45'
        self._report.add_part(f"Week working hours: {hours}")

        payment = '1000$'
        self._report.add_part(f"Month payment: {payment}")

        current_project = 'Current project'
        self._report.add_part(f"\nCurrent project: {current_project}")

    def add_extended_info(self):
        project_description = '\tDuis aute irure dolor in reprehenderit in voluptate,\n' \
                              'quis nostrum exercitationem ullam corporis suscipit laboriosam,\n' \
                              'ut et voluptates repudiandae sint et molestiae non recusandae.'
        self._report.add_part(f"\tProject description\n{project_description}")

        current_tasks = ['Task', 'Task', 'Task']
        self._report.add_part("\nEmployee's current project tasks:",
                              *[f"\t{index + 1}: {task}" for index, task in enumerate(current_tasks)])

        done_tasks = ['Task', 'Task', 'Task', 'Task']
        self._report.add_part("\nEmployee's current project done tasks:",
                              *[f"\t{index + 1}: {task}" for index, task in enumerate(done_tasks)])

    def get_report(self):
        self._report.add_part('*' * 40)
        return self._report


class ClientReportBuilder(ReportBuilder):
    def __init__(self):
        self._report = None

    def reset(self):
        self._report = ClientReport()
        self._report.add_part(f"Current report type:\n\t{self._report.__class__.__name__}\n")

    def add_personal_info(self):
        first_name, last_name = 'Alice', 'Bestoffer'
        self._report.add_part(f"Name: {first_name} {last_name}")

        gender = 'Female'
        self._report.add_part(f"Gender: {gender}")

        age = '22'
        self._report.add_part(f"Age: {age}")

        address = 'Testing office street, 1\\2'
        self._report.add_part(f"Address: {address}")

    def add_business_info(self):
        status = 'Client'
        self._report.add_part(f"\nStatus: {status}")

        orders_count = '4'
        self._report.add_part(f"Total orders from this client: {orders_count}")

        last_order_price = '700$'
        self._report.add_part(f"Last order price: {last_order_price}")

        current_order = 'Ordered project'
        self._report.add_part(f"\nCurrent order: {current_order}")

    def add_extended_info(self):
        project_description = '\tDuis aute irure dolor in reprehenderit in voluptate,\n' \
                              'quis nostrum exercitationem ullam corporis suscipit laboriosam,\n' \
                              'ut et voluptates repudiandae sint et molestiae non recusandae.'
        self._report.add_part(f"\tProject description\n{project_description}")

        wishes = ['Wish', 'Wish', 'Wish']
        self._report.add_part("Wishes regarding the order:", *[f"\t{wish}" for wish in wishes])

    def get_report(self) -> EmployeeReport:
        self._report.add_part('-' * 40)
        return self._report


class ReportDirector:
    def __init__(self):
        self._employee_builder = self._client_builder = None

    @property
    def employee_builder(self):
        return self._employee_builder

    @employee_builder.setter
    def employee_builder(self, builder):
        self._employee_builder = builder

    @property
    def client_builder(self):
        return self._client_builder

    @client_builder.setter
    def client_builder(self, builder):
        self._client_builder = builder

    def build_short_report(self):
        self.employee_builder.reset()
        self.client_builder.reset()

        self.employee_builder.add_personal_info()
        self.client_builder.add_personal_info()

        return self.employee_builder.get_report(), self.client_builder.get_report()

    def build_standard_report(self):
        self.employee_builder.reset()
        self.client_builder.reset()

        self.employee_builder.add_personal_info()
        self.client_builder.add_personal_info()

        self.employee_builder.add_business_info()
        self.client_builder.add_business_info()

        return self.employee_builder.get_report(), self.client_builder.get_report()

    def build_extended_report(self):
        self.employee_builder.reset()
        self.client_builder.reset()

        self.employee_builder.add_personal_info()
        self.client_builder.add_personal_info()

        self.employee_builder.add_business_info()
        self.client_builder.add_business_info()

        self.employee_builder.add_extended_info()
        self.client_builder.add_extended_info()

        return self.employee_builder.get_report(), self.client_builder.get_report()


if __name__ == '__main__':
    director = ReportDirector()

    director.employee_builder = EmployeeReportBuilder()
    director.client_builder = ClientReportBuilder()

    def build_report():
        employee, client = director.build_short_report()
        print(employee)
        print(client)
        #
        # employee, client = director.build_standard_report()
        # print(employee)
        # print(client)
        #
        # employee, client = director.build_extended_report()
        # print(employee)
        # print(client)

    build_report()
