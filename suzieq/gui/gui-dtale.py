from suzieq.sqobjects.bgp import BgpObj
from time import sleep
import dtale

df = BgpObj().get()
d = dtale.show(df)
d.open_browser()
sleep(300)
