from cement import App, TestApp
from cement.core.exc import CaughtSignal

from .controller import BaseController
from .crypto import CryptoController
from .future import FutureController
from .option import OptionController
from .order import OrderController
from .portfolio import PortfolioController
from .quant import QuantController
from .stock import StockController
from .utils import TastyworksCLIError
from .watchlist import WatchlistController


class TastyworksCLI(App):
    """tastyworks-cli primary application."""

    class Meta:
        label = 'tw'

        # call sys.exit() on close
        exit_on_close = True

        # register handlers
        handlers = [
            BaseController,
            OptionController,
            StockController,
            FutureController,
            CryptoController,
            PortfolioController,
            WatchlistController,
            OrderController,
            QuantController,
        ]


class TastyworksCLITest(TestApp, TastyworksCLI):
    """A sub-class of TastyworksCLI that is better suited for testing."""

    class Meta:
        label = 'tw'


def main():
    with TastyworksCLI() as app:
        try:
            app.run()

        except AssertionError as e:
            print('AssertionError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except TastyworksCLIError as e:
            print('TastyworksCLIError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('\n%s' % e)
            app.exit_code = 0


if __name__ == '__main__':
    main()
