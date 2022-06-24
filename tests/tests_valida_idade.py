from datetime import date
import pytest

from src.domain.config.config_atributos import IDADE_MINIMA
from src.domain.entities.usuario import Usuario


class TestValidaIdade:
    idade_minima = IDADE_MINIMA

    @pytest.mark.parametrize(
        ('parametro_teste', 'exception_type', 'msg'),
        (
        pytest.param('30/09/1999', Exception, 'Data precisa ser do tipo date.', id='data_do_tipo_string'),
        pytest.param('', Exception, 'Data precisa ser do tipo date.', id='data_string_vazia'),
        pytest.param(' ', Exception, 'Data precisa ser do tipo date.', id='data_string_com_espaco'),
        pytest.param((1999-9-30), Exception, 'Data precisa ser do tipo date.', id='data_do_tipo_int'),
        pytest.param(date(2021, 9, 30), Exception, f'Idade mínima aceita: {idade_minima} anos.', id='idade_menor_que_idade_minima'),
        
        ),
    )

    def test_valida_idade(self, parametro_teste, exception_type, msg):
        with pytest.raises(exception_type) as exc_info:
            usuario = Usuario(None, None, None, None, parametro_teste, None, None)
            usuario.valida_idade()
        assert str(exc_info.value) == msg
