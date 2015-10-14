import BillardStats
import sys

if __name__ == "__main__":
   if len(sys.argv) == 1:
       BillardStats.app.run()
       sys.exit()

   if sys.argv[1] == 'shell':
       import IPython
       app = BillardStats.app
       BillardStats.models.db.init_app(app)
       with app.app_context():
           IPython.embed()
       sys.exit()
