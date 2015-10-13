import ConfigParser

class ConfigurationIni(object):
    CONFIGS = [
        ('DEBUG', bool),
        ('SQLALCHEMY_DATABASE_URI', str),
        ('SQLALCHEMY_ECHO', bool)
    ]

    def __init__(self, filename, section_name='flask'):
        #Parsed configuration will be stored here
        self.configuration = {}

        self._cfg = ConfigParser.SafeConfigParser()
        self._cfg.read(filename)

        #Now parse the ini section and load it into configuration dict
        self._parse_ini_file(section_name)


    def _parse_ini_file(self, section_name):
        parse_mapping = {
            bool: self._cfg.getboolean,
            int: self._cfg.getint,
            float: self._cfg.getfloat,
            str: self._cfg.get,
        }

        for cfg, _type in ConfigurationIni.CONFIGS:
            cfg_lower = cfg.lower()
            if self._cfg.has_option(section_name, cfg_lower):
                val = parse_mapping[_type](section_name, cfg_lower)
                if val is not None:
                    self.configuration[cfg] = val

    def load_configuration(self, app):
        for key, value in self.configuration.iteritems():
            app.config[key] = value



def configure_app(app, filename='config.ini'):
    """
    :type app: flask.Flask
    :return:
    """
    config_ini = ConfigurationIni(filename)

    #apply the configuration to our app!
    config_ini.load_configuration(app)

