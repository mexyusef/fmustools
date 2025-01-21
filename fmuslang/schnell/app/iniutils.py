import configparser


def read_ini(filepath):
    # Read INI file
    config = configparser.ConfigParser()
    config.read(filepath)
    ini_data = {section: dict(config.items(section)) for section in config.sections()}
    # programming_data['ini'] = ini_data
    return ini_data
