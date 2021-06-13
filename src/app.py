import click

from .utils import VERSION

@click.group()
@click.version_option(VERSION)
def main():
    pass

@main.group(chain=True, help='Buy, sell, and trade options.')
def option():
    pass

@option.command(help='Buy an option with the given parameters.')
@click.argument('quantity', type=int)
@click.argument('underlying', type=str)
@click.argument('price', type=float)
@click.option('-s', '--strike', type=float)
def buy(quantity: int, underlying: str, price: float, strike: float):
    print(f'Buying {quantity}x {underlying} ~ {strike:.2f} @ ${price:.2f}')

@option.command(help='Sell an option with the given parameters.')
@click.argument('quantity', type=int)
@click.argument('underlying', type=str)
@click.argument('price', type=float)
@click.option('-s', '--strike', type=float)
def sell(quantity: int, underlying: str, price: float, strike: float):
    print(f'Selling {quantity}x {underlying} ~ {strike:.2f} @ ${price:.2f}')

@option.command(help='Fetch and display an options chain.')
@click.argument('underlying', type=str)
@click.option('-e', '--expiration', type=str)
def chain(underlying: str, expiration: str):
    print(f'Options chain for {underlying} on {expiration}:')


if __name__ == '__main__':
    main()
