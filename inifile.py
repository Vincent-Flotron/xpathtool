import configparser

class IniFileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def create_ini_file(self, section, name, value):
        config = configparser.ConfigParser()
        config.add_section(section)
        config.set(section, name, value)

        with open(self.file_path, 'w') as config_file:
            config.write(config_file)

    def load_input_xml_from_ini(self, section, name) :
        config = configparser.ConfigParser()
        config.read(self.file_path)

        value = config.get(section, name)
        return value


