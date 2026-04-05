from matplotlib.axes import Axes

def to_journal_format(
    ax: Axes, 
    width: float = 1.0, 
    length: float = 5
    ) -> None:
    """
    Convert the axes to the journal format.

    Parameters
    ----------
    ax: Axes
        The axes to convert.
    width: float
        The width of the ticks.
    length: float
        The length of the ticks.
    """
    ax.tick_params(direction='out', which='major', width=1.0, length=5)
    ax.tick_params(direction='out', which='minor', width=1.0, length=3)

    ax.xaxis.set_ticks_position('both') 
    ax.yaxis.set_ticks_position('both')

    for spine in ax.spines.values():
        spine.set_edgecolor('black')
        spine.set_linewidth(1.0)
    ax.grid(False) 