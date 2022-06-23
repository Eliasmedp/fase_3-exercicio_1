import pytest
from SRC.Domain.Config.config_atributos import TAMANHO_MAX_NOME
from SRC.Domain.Entities.usuario import Usuario


    
class TestValidaNome:
    tamanho_nome = TAMANHO_MAX_NOME

    @pytest.mark.parametrize(
        ('parametro_teste', 'exception_type', 'msg'),
        (
        pytest.param(None, Exception, 'Nome do Usuário não pode ser nulo.', id='nome_nulo'),
        pytest.param('', Exception, 'Nome do Usuário não pode ser vazio.', id='nome_vazio'),
        pytest.param('Elias'*200, Exception, f'Nome do Usuário deve ter o tamanho máximo de {tamanho_nome}.', id='tamanho_nome_maior'),
        pytest.param(1, Exception, f'Nome do Usuário não é do tipo String.', id='nome_nao_string'),
        
        ),
    )
    
    def test_valida_nome(self, parametro_teste, exception_type, msg):
        with pytest.raises(exception_type) as exc_info:
            usuario = Usuario(parametro_teste, None, None, None, None, None, None)
            usuario.valida_nome()
        assert str(exc_info.value) == msg


        