import BillardStats
import sys

if __name__ == "__main__":
   if len(sys.argv) == 1:
       BillardStats.app.run()
       sys.exit()

   if sys.argv[1] == 'shell':
       import IPython
       IPython.embed()
       sys.exit()
