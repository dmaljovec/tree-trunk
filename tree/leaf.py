import click

from tree import hook_implementation


@hook_implementation
def add_subcommand():
    
    @click.command()
    def leaf():
        print("All the leaves are brown")
    
    
    return leaf
