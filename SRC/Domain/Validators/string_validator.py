class ValidaString:
    
    @staticmethod
    def valida_string(valor : str, nome_campo : str, tamanho_maximo : int=0, tamanho_minimo : int=0, tamanho_exato : int=0):
        if not isinstance(valor, str):
            if (valor == None):
                raise Exception (f"{nome_campo} não pode ser nulo.")
            raise Exception (f"{nome_campo} não é do tipo String.")

        
        valor = valor.strip()
        if (len(valor) == 0):
            raise Exception (f"{nome_campo} não pode ser vazio.")
        
        if (tamanho_exato != 0):
            if (len(valor) != tamanho_exato):
                raise Exception (f"{nome_campo} deve ter o tamanho exato {tamanho_exato}.")
        else:
            if (tamanho_maximo != 0):
                if (len(valor) > tamanho_maximo):
                    raise Exception (f"{nome_campo} deve ter o tamanho máximo de {tamanho_maximo}.")
            
            if (tamanho_minimo != 0):
                if (len(valor) < tamanho_minimo):
                    raise Exception (f"Tamanho do {nome_campo} não pode ser menor que {tamanho_minimo}.")
