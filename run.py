import BilliardStats
import sys

if __name__ == "__main__":
   if len(sys.argv) == 1:
       BilliardStats.app.run()
       sys.exit()

   if sys.argv[1] == 'shell':
       import IPython
       app = BilliardStats.app
       BilliardStats.models.db.init_app(app)
       with app.app_context():
           IPython.embed()
       sys.exit()
