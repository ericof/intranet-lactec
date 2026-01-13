from lactec.intranet import PACKAGE_NAME
from zope.i18nmessageid.message import Message
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

import pytest


class TestVocabEstados:
    name = f"{PACKAGE_NAME}.vocabulary.estados"

    @pytest.fixture(autouse=True)
    def _setup(self, get_vocabulary, portal):
        """Configura o vocabulário para os testes.

        get_vocabulary: Fixture para obter o vocabulário registrado.
                        Definida em pytest-plone.
        portal: Fixture do portal Plone.
                Definida em pytest-plone.
        """
        self.vocab: SimpleVocabulary = get_vocabulary(self.name, portal)

    def test_vocabulary(self):
        assert self.vocab is not None
        assert isinstance(self.vocab, SimpleVocabulary)

    @pytest.mark.parametrize(
        "token, title",
        [
            ("PR", "Paraná"),
            ("SP", "São Paulo"),
            ("MT", "Mato Grosso"),
            ("DF", "Distrito Federal"),
            ("AM", "Amazonas"),
            ("PB", "Paraíba"),
        ],
    )
    def test_term(self, token: str, title: str):
        """Verifica se o token existe no vocabulário e se o termo corresponde ao título esperado."""
        # Obtém o termo pelo token passado
        term: SimpleTerm = self.vocab.getTermByToken(token)
        assert isinstance(term, SimpleTerm)
        assert term.value == token
        # Título deve ser uma mensagem internacionalizável
        assert isinstance(term.title, Message)
        # Porém a comparação deve ser feita com a string esperada
        assert term.title == title

    def test_total(self):
        """Verifica total de entradas no vocabulário."""
        assert len(self.vocab) == 27
