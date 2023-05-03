import click
import pluggy
import sys

from tree.trunk import hook_implementation

@hook_implementation
def add_subcommand():
    
    @click.command()
    def branch():
        print("We are the leaves of one branch...")
    
    
    return branch

pm = pluggy.PluginManager("tree-trunk")
pm.register(sys.modules[__name__])
