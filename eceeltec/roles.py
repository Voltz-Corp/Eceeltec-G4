from rolepermissions.roles import AbstractUserRole

class Administrador(AbstractUserRole):
    available_permissions = {
        'register_employee': True,
        'view_employees':True,
        'employee_details':True,
        'config_p-user': True,
        'manage_os': True,
        'create_os':True,
        'os&request_ops':True,
    }

class Funcionario(AbstractUserRole):
    available_permissions = {
        'fazer_coisas': True,
        'config_p-user': True,
        'os&request_ops':True,
    }

class Cliente(AbstractUserRole):
    available_permissions = {
        'fazer_coisas_de_cliente': True,
    }