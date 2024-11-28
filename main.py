import os

from lib.utils.utilities import Utilities
from lib.process.message_service import MessageService

messaging_service = MessageService()
utils = Utilities()

def main():

    file_name = os.path.abspath('30th.csv')
    data = utils.read_csv(file_name)
    status = messaging_service.send_billing_due(data)
    print(status)


main()