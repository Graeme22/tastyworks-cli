from cement import Controller, ex
from textwrap import wrap
from cement.utils.version import get_version_banner
from ..core.version import get_version


VERSION_BANNER = """
An easy-to-use command line interface for Tastyworks! %s
%s
""" % (get_version(), get_version_banner())


class Base(Controller):
    class Meta:
        label = 'base'

        # text displayed at the top of --help output
        description = 'An easy-to-use command line interface for Tastyworks!'

        # text displayed at the bottom of --help output
        epilog = 'Usage: twcli command1 --foo bar'

        # controller level arguments. ex: 'twcli --version'
        arguments = [
            ### add a version banner
            ( [ '-v', '--version' ],
              { 'action'  : 'version',
                'version' : VERSION_BANNER } ),
        ]

    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.args.print_help()


    @ex(
        help='\n'.join(wrap('An option price calculator for a single contract. '
                            'Default args replicate an example from the '
                            'QuantLib documentation. ')),

        # the default args calculate a price for an example from QuantLib docs
        arguments=[
            ( [ '-pu', '--price-underlying' ],
              { 'help' : 'the price of the underlying asset (default = 100)',
                'action'  : 'store', 'default':100.0,
                'dest' : 'price_underlying' } ),
            ( [ '-ps', '--price-strike' ],
              { 'help' : 'the strike price of the contract (default = 100)',
                'action'  : 'store', 'default':100,
                'dest' : 'price_strike' } ),
            ( [ '-vl', '--volatility' ],
              { 'help' : 'the volatility assumption to use (default = 0.2)',
                'action'  : 'store', 'default':0.2,
                'dest' : 'volatility' } ),
            ( [ '-rf', '--rate-risk-free' ],
              { 'help' : 'the risk free rate (default = 0.01)',
                'action'  : 'store', 'default':0.01,
                'dest' : 'rate_risk_free' } ),
            ( [ '-dx', '--date-expiration' ],
              { 'help' : 'expiration date of the contract (default = 2014-06-07)',
                'action'  : 'store', 'default':'2017-06-07',
                'dest' : 'date_expiration' } ),
            ( [ '-de', '--date-evaluation' ],
              { 'help' : 'evaluation date of contract price (default = 2014-03-07)',
                'action'  : 'store', 'default':'2017-03-07',
                'dest' : 'date_evaluation' } ),
            ( [ '-ct', '--contract-type' ],
              { 'help' : 'the contract type, e.g. call or put (default = call)',
                'action'  : 'store', 'default':'call',
                'dest' : 'option_type' } ),
            ( [ '-et', '--exercise-type' ],
              { 'help' : "exercise type; 'european' or 'american' (default = european)",
                'action'  : 'store', 'default':'european',
                'dest' : 'exercise_type' } ),
        ],
        aliases=['omod'],
    )
    def model_opt(self):
        from ..core.quantlib_tools import models 
        pa = self.app.pargs
        args = dict(price_underlying=pa.price_underlying,
                    price_strike=pa.price_strike, volatility=pa.volatility,
                    rate_risk_free=pa.rate_risk_free,
                    date_expiration=pa.date_expiration,
                    date_evaluation=pa.date_evaluation,
                    option_type=pa.option_type, exercise_type=pa.exercise_type,)
        mod = models.Model(**args)
        print(f"    * calculated price = ${mod.option.NPV():.3f}")
        for k,v in args.items():
            print(f"    * {k} = {v}")
