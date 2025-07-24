import os
import tomllib
from app.core.logger import logger
from app.core.i18n import i18n

i18nImpl = i18n()

def load_configuration(name: str) -> dict:
    config_name =  os.path.join("app","core","graph_config", name + '.toml')
    if os.path.exists(config_name):
        with open(config_name, "rb") as f:
            config = tomllib.load(f)
        return config
    raise ValueError(i18nImpl.get_label("CONFIG_GRAPH_NOT_FOUND").format(config_name=name))