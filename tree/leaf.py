import click

from tree.trunk import hook_implementation


@hook_implementation
def add_subcommand():
    
    @click.command()
    def leaf():
        print("All the leaves are brown")
    
    
    return leaf
