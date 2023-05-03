import click
import pluggy

from tree import hooks
from tree import leaf, twig

def print_banner():
    print("""
       _-_
    /~~   ~~\\
 /~~         ~~\\
{               }
 \  _-     -_  /
   ~  \\\\ //  ~
_- -   | | _- _
  _ -  | |   -_
      // \\
          """)


@click.group()
def cli() -> None:
    """Silly litte demo."""
    print_banner()

@click.command()
def check() -> None:
    """Check the tree for pests."""
    print("Checking for pests...")
    print("No pests found.")

cli.add_command(check)


def get_plugin_manager():
    pm = pluggy.PluginManager("tree-trunk")
    pm.add_hookspecs(hooks)
    pm.register(leaf)
    pm.register(twig)
    return pm


if __name__ == '__main__':
    pm = get_plugin_manager()
    for plugin in pm.hook.add_subcommand():
        cli.add_command(plugin)
    cli()
