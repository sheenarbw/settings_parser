class Settings:
    dSettings = {}
    
    def __init__(self,sPath=""):
        if sPath:
            Settings.dSettings = Settings.parse_settings(sPath)

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
                dRet[sSection][tItem[0]] = tItem[1]
        
        return dRet
    
    