import logger
import view
import model

def run():
    choice = view.choose_mode()
    if choice == 1:
        logger.add_contact()
    elif choice == 2:
        model.search_and_print_contact()
