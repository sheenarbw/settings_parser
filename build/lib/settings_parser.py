class Settings:
    dSettings = {}
    sPath = None
    def __init__(self,sPath=""):
        Settings.sPath = sPath
        if sPath:
            Settings.dSettings = Settings.parse_settings(sPath)

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
    
    