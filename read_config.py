import configparser
class read_config(object):

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("config")

    def get_sections(self):
        '''
        获取配置文件中的sections
        :return:
        '''
        sections = self.config.sections()
        return sections

    def get_options(self, section):
        '''
        获得配置文件中options
        :param section:
        :return: options
        '''
        options = self.config.options(section)
        return options

    def get_option_of_section(self, section, option):
        '''
        获得options of section
        :param section:
        :param option:
        :return: option
        '''
        res_val = self.config.get(section, option)
        return res_val
