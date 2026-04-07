from enum import Enum


class Linestyle(Enum):
    """
    Linestyle is the linestyle for the line plot.
    Ref: https://matplotlib.org/stable/api/lines_api.html
    """

    SOLID = "solid"
    DOTTED = "dotted"
    DASHED = "dashed"
    DASHDOT = "dashdot"
    LOOSELY_DOTTED = (0, (1, 10))
    DENSELY_DOTTED = (0, (1, 1))
    LOOSELY_DASHED = (0, (5, 10))
    DENSELY_DASHED = (0, (5, 1))
    LOOSELY_DASHDOT = (0, (3, 10, 1, 10))
    DENSELY_DASHDOT = (0, (3, 1, 1, 1))
    DASHDOTDOT = (0, (3, 5, 1, 5, 1, 5))
    LOOSELY_DASHDOTDOT = (0, (3, 10, 1, 10, 1, 10))
    DENSELY_DASHDOTDOT = (0, (3, 1, 1, 1, 1, 1))


if __name__ == "__main__":
    linestyle = Linestyle("solid")
    print(linestyle)
    linestyle = Linestyle((0, (1, 10)))
    print(linestyle)

    print(Linestyle.SOLID.value)
    print(Linestyle.DOTTED.value)
    print(Linestyle.DASHED.value)
    print(Linestyle.DASHDOT.value)
    print(Linestyle.LOOSELY_DOTTED.value)
    print(Linestyle.DENSELY_DOTTED.value)
    print(Linestyle.LOOSELY_DASHED.value)
    print(Linestyle.DENSELY_DASHED.value)
    print(Linestyle.LOOSELY_DASHDOT.value)
    print(Linestyle.DENSELY_DASHDOT.value)