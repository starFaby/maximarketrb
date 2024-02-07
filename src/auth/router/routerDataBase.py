from flask import Blueprint
from src.migrate.migrate import initDB

pfsbdssrb= Blueprint('pfsbdssrb', __name__)

pfsbdssrb.route('/pfsbdssrb', methods=['GET'])(initDB)

