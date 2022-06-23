from calendar import isleap
from datetime import date
from transfero_validators.validators import AbstractValidator

class DataValidator(AbstractValidator[date]):
    def valida(value: date) -> bool:
        meses_com_31_dias = (1, 3, 5, 7, 8, 10, 12)
        meses_com_30_dias = (4, 6, 9, 11)

        if (not isinstance(value, date)):
            raise Exception ("Data de nascimento deve ser do tipo date.")
        
        if (value.month in meses_com_31_dias):
            if (value.day > 31) or (value.day < 1):
                raise Exception ('Data de nascimento inválida.')
        
        if (value.month in meses_com_30_dias):
            if (value.day > 30) or (value.day < 1):
                raise Exception ('Data de nascimento inválida.')
        
        if (isleap(value.year)):
            if (value.month == 2) and (value.day > 29 or value.day < 1):
                raise Exception ("Data de nascimento inválida.")
        else:
            if (value.month == 2) and (value.day > 28 or value.day < 1):
                raise Exception ("Data de nascimento inválida.")

