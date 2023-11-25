
from glob import glob as original_glob
path = 'http://mt.itron-systeam02-install.eng.ssnsgs.net:3009/amm/webservice'

dir  = original_glob(path)

print(dir)