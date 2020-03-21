import sys
sys.path.insert(0, '..')

try:
    from . import config
    import instance.config as inst_config

    for param in dir(inst_config):
        setattr(config, param, getattr(inst_config, param))
    print('Настройки успешно считаны из папки instance!')

except Exception as e:
    print(
        'Не найден файл конфигурации. Вы можете взять файл из приложения app и изменить его. Полученный файл следует положить в папку instance на уровне проекта. На настоящий момент приняты настройки по умолчанию.'
    )
