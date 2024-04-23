from rolepermissions.roles import AbstractUserRole

class Administrador(AbstractUserRole):
    available_permissions = {
        'register_employee': True,
        'view_employees':True,
        'employee_details':True,
    }

class Funcionario(AbstractUserRole):
    available_permissions = {
        'fazer_coisas': True,
    }

class Cliente(AbstractUserRole):
    available_permissions = {
        'fazer_coisas': True,
        'fazer_coisas': True,
    }