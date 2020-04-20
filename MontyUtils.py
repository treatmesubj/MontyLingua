__author__="Hugo Liu <hugo@media.mit.edu>"
__version__="2.0"
import os,string,sys


class MontyUtils:

    def __init__(self):
        pass

    def find_file(self,filename):

        # if filename in os.listdir('.'):
        #     return './'+filename

        # if 'MONTYLINGUA' in os.environ:
        #     csplits=os.environ['MONTYLINGUA'].split(';')
        #     csplits=[groupss.strip() for groupss in csplits]

        #     for enabled_arr in csplits:

        #         try :

        #             if filename in os.listdir(enabled_arr):
        #                 return enabled_arr+'/'+filename
        #         except :
        #             pass

        # if 'PATH' in os.environ:
        #     csplits=os.environ['PATH'].split(';')
        #     csplits=[groupss.strip() for groupss in csplits]

        #     for enabled_arr in csplits:

        #         try :

        #             if filename in os.listdir(enabled_arr):
        #                 return enabled_arr+'/'+filename
        #         except :
        #             pass
        # return ''

        return f"{os.path.dirname(__file__)}\\{filename}"
