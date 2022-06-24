import pytest

from src.domain.entities.usuario import Usuario
from src.domain.enums.opcaoGeneroEnum import Genero

class TestValidaGenero:

    def test_valida_genero(self):
        with pytest.raises(Exception) as exc_info:
            usuario = Usuario(None, None, None, None, None, None, 'a')
            usuario.valida_genero()
        assert str(exc_info.value) == 'Genero precisa ser do tipo Genero.'
