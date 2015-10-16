import ConfigParser
import logging
import logging.handlers

class ConfigurationIni(object):
    CONFIGS = [
        ('DEBUG', bool),
        ('SQLALCHEMY_DATABASE_URI', str),
        ('SQLALCHEMY_ECHO', bool),
        ('LOG_FILE', str),
        ('LOG_FILE_MAX_BYTES', int)
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

    #Apply logging
    log_file_handler = logging.handlers.RotatingFileHandler(
        app.config.get('LOG_FILE', app.name + '.log'),
        maxBytes=app.config.get('LOG_FILE_MAX_BYTES', 10000),
        backupCount=1
    )
    log_file_handler.setLevel(logging.DEBUG if app.debug else logging.ERROR)

    app.logger.addHandler(log_file_handler)
