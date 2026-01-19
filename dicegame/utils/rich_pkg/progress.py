from dicegame.utils.rich_pkg.console import console
from rich.progress import Progress
import time


def progress_bar():

    with Progress() as progress:
        task = progress.add_task("[cyan]Rolling dice...",total=10)

        for _ in range(10):
            time.sleep(0.2)
            progress.update(task,advance=2)
