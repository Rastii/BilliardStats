import ConfigParser
import datetime

class ConfigurationIni(object):
    def __init__(self, filename, default_config, section_name='flask'):
        #Parsed configuration will be stored here
        self.configuration = {}

        self._cfg = ConfigParser.SafeConfigParser()
        self._cfg.read(filename)

        #Now parse the ini section and load it into configuration dict
        self._parse_ini_file(section_name, default_config)


    def _parse_ini_file(self, section_name, default_config):
        for key, _ in self._cfg.items(section_name):
            self._load_cfg_item(section_name, key, default_config)


    def _load_cfg_item(self, section_name, key, default_config):
        default = default_config.get(key)

        # One of the default config vars is a timedelta - interpret it
        # as an int and construct using
        if isinstance(default, datetime.timedelta):
            self.configuration[key] = datetime.timedelta(
                self._cfg.getint(section_name, key))
        elif isinstance(default, bool):
            self.configuration[key] = self._cfg.getboolean(section_name, key)
        elif isinstance(default, float):
            self.configuration[key] = self._cfg.getfloat(section_name, key)
        elif isinstance(default, int):
            self.configuration[key] = self._cfg.getint(section_name, key)


    def load_configuration(self, app):
        for key, value in self.configuration.iteritems():
            app.config[key] = value



def configure_app(app, filename='config.ini'):
    """
    :type app: flask.Flask
    :return:
    """
    config_ini = ConfigurationIni(filename, app.default_config)

    #apply the configuration to our app!
    config_ini.load_configuration(app)

