import click

@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name', default=1)
def hello(count, name):
    for x in range(count):
        click.echo('Hello %s!' % name)

ips = (
    "black",
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "white",
    "bright_black",
    "bright_red",
    "bright_green",
    "bright_yellow",
    "bright_blue",
    "bright_magenta",
    "bright_cyan",
    "bright_white",
)


@click.command()
def cli():
    for x in ips:
        click.echo('http://'+ x +'.com')


if __name__ == '__main__':
  cli()
