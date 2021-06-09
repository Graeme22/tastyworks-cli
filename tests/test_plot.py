import pandas as pd

from src.plot.base import _DURATIONS, Portfolio

_CSV_PATH = 'tests/data/transactions.csv'
_NET_LIQUIDITY = 6645.84
_REALIZED_PANDL = -588.58


def gen_portfolio(net_liq=False):
    df = pd.read_csv(_CSV_PATH)
    df = df.reindex(index=df.index[::-1])
    df.index = range(len(df))

    pf = Portfolio(df, net_liq=net_liq)
    pf.calculate()

    return pf


def test_twcli_plot_pandl():
    pf = gen_portfolio()
    val = pf.plot('ytd')

    assert round(val, 2) == _REALIZED_PANDL


def test_twcli_plot_netliq():
    # the value shouldn't change
    for duration in _DURATIONS:
        pf = gen_portfolio(True)
        val = pf.plot('all')

        assert round(val, 2) == _NET_LIQUIDITY


def test_twcli_plot_positions():
    pf = gen_portfolio()
    _ = pf.plot('all')

    assert len(pf.positions) == 2
    for trade in pf.positions.values():
        assert 'GME' in trade.symbol
