from flask import Flask

from configuration import configure_all

app = Flask(__name__)

configure_all(app)
##Banco de Dados Mysql online
## mysql://root:GCruUsgoPnknKFPZLewtKKWftSVPNYtD@interchange.proxy.rlwy.net:45565/railway
if __name__ == "__main__":
    app.run(debug=True)   