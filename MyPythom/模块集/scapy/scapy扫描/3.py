import logging
logging.getLogger('scapy').setLevel(1)
from scapy.all import *
class Test(Packet):
    name = 'Test packet'
    fields_desc = [shortField('test1',1),
                   shortField('test2',2)]
def make_test(x,y):
    return Ether()/IP()/Test(test1=x,test2=y)
if __name__=='main':
    interact(mydict=globals(),mybanner='Test add-on v3.14')