class Settings:
    dSettings = {}
    sPath = None
    def __init__(self,sPath=""):
        Settings.sPath = sPath
        if sPath:
            Settings.dSettings = Settings.parse_settings(sPath)

    @classmethod
    def __getitem__(cls,sKey):
        return Settings.dSettings[sKey]

    @staticmethod 
    def get(sKey,xDefault=None):
        return Settings.dSettings.get(sKey,xDefault)


    @staticmethod
    def append_pyramid_settings(**dSettings):
        for s in dSettings:
            l = s.split('.')
            if l[0] not in Settings.dSettings:
                Settings.dSettings[l[0]] = {}
            Settings.dSettings[l[0]][l[1]] = dSettings[s]

    @staticmethod
    def parse_setting(sSetting):
        #TODO: other datatypes
        if '\n' in sSetting:
            l = [s for s in [s.strip() for s in sSetting.split('\n')] if s]
            if len(l)==1:
                return Settings.parse_setting(l[0])
            if l:
                return [Settings.parse_setting(s) for s in l]
            return None
        else:
            return sSetting

    @staticmethod
    def parse_settings(sPath):
        """
        return a dictionary of dictionaries containing 
        configuration info
        """
        
        import os
        if not os.path.exists(sPath):
            raise Exception("Missing configuration file {0}".format(sPath))
        
        import ConfigParser
        oConfig = ConfigParser.RawConfigParser()
        oConfig.read(sPath)
        
        dRet = {}
        for sSection in oConfig.sections():
            dRet[sSection] = {}
            for tItem in oConfig.items(sSection):
                dRet[sSection][tItem[0]] = Settings.parse_setting(tItem[1])
        
        return dRet
    
    