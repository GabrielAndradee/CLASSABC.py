''''
from abc import ABC, abstractmethod

class Carro(ABC):
    preco_base = 100.00

    def __init__(self, modelo):
        self.modelo = modelo

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, modelo):
        self.modelo = modelo

    @classmethod
    def get_preco_base(cls):
        return cls.preco_base

    @classmethod
    def set_preco_base(cls, preco_base):
        cls.preco_base = preco_base

    @abstractmethod
    def preco_diaria(self):
        pass


class Economico(Carro):
    def preco_diaria(self):
        return self.get_preco_base() * 0.5


class Intermediario(Carro):
    def __init__(self, modelo, ar_condicionado):
        super().__init__(modelo)
        self.ar_condicionado = ar_condicionado

    def preco_diaria(self):
        preco = self.get_preco_base()
        if self.ar_condicionado:
            preco *= 1.2
        return preco


if __name__=='__main__':
    # Testes
    Carro.set_preco_base(120.0)
    print(f"O preço base do carro é {Carro.get_preco_base()}.\n")

    carro1 = Economico("Ford Ka")
    print(f"O modelo do carro 1 é {carro1.get_modelo()} e seu valor diário é {carro1.preco_diaria():.2f}.\n")

    carro2 = Intermediario("Ford Fusion", True)
    print(f"O modelo do carro 2 é {carro2.get_modelo()} e seu valor diário é {carro2.preco_diaria():.2f}.\n")

    carro3 = Intermediario("Gol", False)
    print(f"O modelo do carro 3 é {carro3.get_modelo()} e seu valor diário é {carro3.preco_diaria():.2f}.\n")

    carro1.set_modelo("Golf")
    print(f"O modelo do carro 1 é {carro1.get_modelo()} e seu valor diário é {carro1.preco_diaria():.2f}.\n")

    Carro.set_preco_base(150.0)
    print(f"O preço base do carro é {Carro.get_preco_base()}.\n")

    print(f"O modelo do carro 2 é {carro2.get_modelo()} e seu valor diário é {carro2.preco_diaria():.2f}.\n")

    carro4 = Economico("Onix")
    print(f"O modelo do carro 4 é {carro4.get_modelo()} e seu valor diário é {carro4.preco_diaria():.2f}.\n")
'''

from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @abstractmethod
    def compute_salary(self):
        pass


class FulltimeEmployee(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def compute_salary(self):
        return self.salary + 200


class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, worked_hours, value):
        super().__init__(first_name, last_name)
        self.worked_hours = worked_hours
        self.value = value

    def get_worked_hours(self):
        return self.worked_hours

    def set_worked_hours(self, worked_hours):
        self.worked_hours = worked_hours

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def compute_salary(self):
        return self.worked_hours * self.value


class Payroll:
    def __init__(self):
        self.employee_list = []

    def add_employee(self, employee):
        self.employee_list.append(employee)

    def print_payroll(self):
        print("Payroll:")
        for employee in self.employee_list:
            print(f"{employee.full_name()}: {employee.compute_salary()}")


# criando objetos para teste
fulltime_employee = FulltimeEmployee("John", "Doe", 3000)
hourly_employee = HourlyEmployee("Jane", "Smith", 80, 25)

# mostrando informações dos empregados
print(fulltime_employee.get_first_name())  # John
print(fulltime_employee.full_name())  # John Doe
print(fulltime_employee.get_salary())  # 3000
print(fulltime_employee.compute_salary())  # 3200

print(hourly_employee.get_first_name())  # Jane
print(hourly_employee.full_name())  # Jane Smith
print(hourly_employee.get_value())  # 25
print(hourly_employee.compute_salary())  # 2000

# criando a folha de pagamento
payroll = Payroll()
payroll.add_employee(fulltime_employee)
payroll.add_employee(hourly_employee)
payroll.print_payroll()
