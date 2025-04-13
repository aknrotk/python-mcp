import logging.config
from logging import getLogger

logging.config.fileConfig(
    "logging_settings.ini", encoding="utf-8"
)  # ファイルから設定を読み込む
logger = getLogger("root")  # logging_settings.iniのrootの設定が呼び出される


logger.info("this is fileConfig from logging_settings.ini")
