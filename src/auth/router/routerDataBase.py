from flask import Blueprint
from src.migrate.migrate import initDB

pfsbdmmrb= Blueprint('pfsbdmmrb', __name__)

pfsbdmmrb.route('/pfsbdmmrb', methods=['GET'])(initDB)

