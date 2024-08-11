from model import SearchParameters
from controllers import SiteController


def main():
    search_params = SearchParameters(origin='Rosario, Santa Fe, Argentina', 
                                    destination='Santiago de Chile, Santiago, Chile',
                                    start_date='20240901',
                                    end_date='20240915',
                                    passangers='1')
    site_controller=SiteController()
    site_controller.run(search_params)


main()

