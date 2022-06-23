from datetime import date
import pytest

from SRC.Domain.Config.config_atributos import IDADE_MINIMA
from SRC.Domain.Entities.usuario import Usuario


class TestValidaIdade:
    idade_minima = IDADE_MINIMA

    @pytest.mark.parametrize(
        ('parametro_teste', 'exception_type', 'msg'),
        (
        pytest.param('30/09/1999', Exception, 'Data precisa ser do tipo date.', id='data_nao_do_tipo_date'),
        pytest.param(date(2021, 9, 30), Exception, f'Idade mínima aceita: {idade_minima} anos.', id='idade_menor_que_idade_minima'),
        
        ),
    )

    def test_valida_idade(self, parametro_teste, exception_type, msg):
        with pytest.raises(exception_type) as exc_info:
            usuario = Usuario(None, None, None, None, parametro_teste, None, None)
            usuario.valida_idade()
        assert str(exc_info.value) == msg