import os
import json
from app.core.logger import logger

class _i18nSingletonMetaclass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # Cria uma chave imutável a partir dos parâmetros
        key = (cls, args, tuple(sorted(kwargs.items())))
        if key not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[key] = instance
        return cls._instances[key]

class i18n(metaclass=_i18nSingletonMetaclass):
    
    # adicionado aspas no nome da classe pois é uma forma de indicar que ela vai ser carregada depois
    def __init__(self, language='PT_br') -> 'i18n':
        
        self.language = language
        self.language_template = {}
        self._load_file_language()

    def _load_file_language(self) -> None:

        file = os.path.join("app","core","i18n",'PT_br.json')
        if os.path.exists(file):
            file =  os.path.join("app","core","i18n",self.language) + '.json'
        else:
            logger.error(f"Arquivo para o idioma {self.language} não encontrado usando o padrão PT-br")

        with open(file, 'r', encoding='utf-8') as arq:
            self.language_template = json.loads(arq.read())
    
    def get_label(self, label_name: str) -> str:

        if label_name not in self.language_template:
            raise ValueError(self.get_label('NOT_FOUND_LABEL').format(label_name))
        return self.get_label(label_name)
        