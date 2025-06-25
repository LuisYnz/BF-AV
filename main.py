import logging
from core import configure_logging, run_tests_parallel
from home_page import test_suite as home_page_suite
from select_flight.test_suite import run_suite as select_flight_suite
from passenger.test_suite import run_suite as passengers_suite
from services.test_suite import run_suite as services_suite
from seatmap.test_suite import run_suite as seatmap_suite
from payment.test_suite import run_suite as payment_suite

# Configurar el logging
configure_logging()

# Lista de URLs para probar
urls = [
    "https://nuxqa.avtest.ink/es/",  # Primera URL
    #"https://nuxqa5.avtest.ink/es/"   # Segunda URL
]

# Lista de navegadores para probar
browsers = ['chrome', 'edge']  # Lista de navegadores

# Las suites a ejecutar
suite_functions = [
    home_page_suite.run_suite,
    select_flight_suite,
    passengers_suite,
    services_suite,
    seatmap_suite,
    payment_suite,
]

if __name__ == "__main__":
    run_tests_parallel(urls, browsers, suite_functions)

