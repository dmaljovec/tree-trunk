import click

from tree import hook_implementation


@hook_implementation
def add_subcommand():
    
    @click.command()
    def twig():
        print("A single twig breaks, but the bundle of twigs is strong.")
    
    
    return twig
