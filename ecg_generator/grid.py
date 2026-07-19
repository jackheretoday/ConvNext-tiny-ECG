
"""
ECG Paper Grid Generator
Author: Jay Kshirsagar

Draws standard ECG paper
according to 25 mm/s and 10 mm/mV.
"""

from __future__ import annotations

import numpy as np
import matplotlib.axes as maxes

from config.config import (
    DURATION,
    YLIM,
    MINOR_GRID,
    MAJOR_GRID,
    MINOR_LINEWIDTH,
    MAJOR_LINEWIDTH,
)


def draw_ecg_grid(ax: maxes.Axes) -> None:
    """
    Draw ECG paper grid on the supplied axis.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axis to draw the ECG paper.
    """

    # -----------------------
    # Vertical Grid
    # -----------------------

    minor_x = np.arange(0, DURATION + 0.04, 0.04)
    major_x = np.arange(0, DURATION + 0.20, 0.20)

    # -----------------------
    # Horizontal Grid
    # -----------------------

    minor_y = np.arange(YLIM[0], YLIM[1] + 0.1, 0.1)
    major_y = np.arange(YLIM[0], YLIM[1] + 0.5, 0.5)

    # Minor Vertical
    for x in minor_x:
        ax.axvline(
            x,
            color=MINOR_GRID,
            linewidth=MINOR_LINEWIDTH,
            zorder=0,
        )

    # Major Vertical
    for x in major_x:
        ax.axvline(
            x,
            color=MAJOR_GRID,
            linewidth=MAJOR_LINEWIDTH,
            zorder=0,
        )

    # Minor Horizontal
    for y in minor_y:
        ax.axhline(
            y,
            color=MINOR_GRID,
            linewidth=MINOR_LINEWIDTH,
            zorder=0,
        )

    # Major Horizontal
    for y in major_y:
        ax.axhline(
            y,
            color=MAJOR_GRID,
            linewidth=MAJOR_LINEWIDTH,
            zorder=0,
        )

    ax.set_xlim(0, DURATION)
    ax.set_ylim(YLIM)
