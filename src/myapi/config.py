"""_summary_
"""

from pathlib import Path

# === PATH CONFIGURATION ===
# Using __file__ makes paths work regardless of where the script is run from
PACKAGE_DIR = Path(__file__).parent
PROJECT_ROOT = PACKAGE_DIR.parent.parent
DATA_DIR = PROJECT_ROOT / 'data'


def get_data_path(filename):
    """
    Get full path to a datafile.

    Args:
        filename

    Returns:
        Path object to the file
    """

    return DATA_DIR / filename
