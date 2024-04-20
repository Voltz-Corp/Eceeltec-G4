from rolepermissions.roles import AbstractUserRole

class Administrador(AbstractUserRole):
    available_permissions = {
        'register_employee': True,
        'view_functionaries':True,
    }

class Funcionario(AbstractUserRole):
    available_permissions = {
        'fazer_coisas': True,
    }