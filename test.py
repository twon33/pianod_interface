import pianod_interface
from pianod_interface import PianodInterface

pianod_interface._set_module_log_enable(True)

pd = PianodInterface()
pd.connect('localhost',8999,'administrator','bpibot_pianod')
pd.disconnect()


