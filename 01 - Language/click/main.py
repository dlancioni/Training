import click

msg = "Your name please"

@click.command()
@click.option('--name', prompt=f'{msg}')
def main(name):
    click.echo(f"Hello {name}!")
    
if __name__ == '__main__':
    main()