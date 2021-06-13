import pandas as pd

from .plot import Portfolio


@ex(
    help='chart your portfolio\'s net liquidity or realized profit/loss over time',
    arguments=[
        (
            ['csv'],
            {
                'action': 'store',
                'help': 'path to .csv file containing full portfolio transaction history'
            }
        ),
        (
            ['-n', '--netliq'],
            {
                'action': 'store_true',
                'help': 'show net liquidity over time instead of realized profit/loss'
            }
        ),
        (
            ['-d', '--duration'],
            {
                'action': 'store',
                'help': '{all,10y,5y,1y,ytd,6m,3m,1m,5d}',
                'default': 'ytd'
            }
        ),
        (
            ['-p', '--percentage'],
            {
                'action': 'store_true',
                'help': 'show percentage change instead of change in absolute value'
            }
        )
    ]
)
def plot(self):
    # read the given csv file and prepare it
    df = pd.read_csv(self.app.pargs.csv)
    df = df.reindex(index=df.index[::-1])
    df = df.astype(str)

    # create a portfolio with the given history
    pf = Portfolio(df, net_liq=self.app.pargs.netliq)

    # get initial net liq if we're using percentage
    nl = None
    if self.app.pargs.percentage:
        pf_tmp = Portfolio(df, net_liq=True)
        nl = pf_tmp._get_starting_net_liq(self.app.pargs.duration)

    # get the P/L or net liq and save the graph
    val = pf.plot(self.app.pargs.duration, starting_net_liq=nl)

    # print current positions
    if nl is None:
        print(('Current net liquidity' if self.app.pargs.netliq else 'Realized P/L') + f': ${val:.2f}')
    else:
        print(('Change in net liquidity' if self.app.pargs.netliq else 'Realized P/L') + f': {val:.2f}%')
    print('Current positions:')
    for p in pf.positions.values():
        print(p)
