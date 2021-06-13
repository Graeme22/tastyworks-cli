from cement import Controller, ex


@ex(help='buy, sell, and analyze futures')
class FutureController(Controller):
    class Meta:
        label = 'future'
        stacked_on = 'tw'
        stacked_type = 'nested'
        help = description = 'buy, sell, and analyze futures'

    @ex(
        help='buy futures contracts',
        arguments=[
            (
                ['-n', '--number'],
                {
                    'action': 'store',
                    'help': 'the number of contracts to buy',
                    'default': 1
                }
            ),
            (
                ['symbol'],
                {
                    'action': 'store',
                    'help': 'which product to trade'
                }
            ),
            (
                ['price'],
                {
                    'action': 'store',
                    'help': 'limit price for a single contract'
                }
            )
        ]
    )
    def buy(self):
        print(f'Buying {self.app.pargs.number}x {self.app.pargs.symbol} @{self.app.pargs.price} each')

    @ex(
        help='sell futures contracts',
        arguments=[
            (
                ['-n', '--number'],
                {
                    'action': 'store',
                    'help': 'the number of contracts to sell',
                    'default': 1
                }
            ),
            (
                ['symbol'],
                {
                    'action': 'store',
                    'help': 'which product to trade'
                }
            ),
            (
                ['price'],
                {
                    'action': 'store',
                    'help': 'limit price for a single contract'
                }
            )
        ]
    )
    def sell(self):
        print(f'Selling {self.app.pargs.number}x {self.app.pargs.symbol} @{self.app.pargs.price} each')

    @ex(help='display current price and other data for a given symbol')
    def spot(self):
        print('Inside spot')
