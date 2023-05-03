import click
import pluggy

hook_specification = pluggy.HookspecMarker("tree-trunk")


@hook_specification
def add_subcommand() -> click.Command:
    """Add an additional sub-command to the tree cli

    Returns
    -------
    click.Command
        The command to add to the tree cli
    """
