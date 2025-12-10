"""

"""

import pandas as pd

from myapi import config


class ChainLadder:
    """
    Class for creating chainladder values. 
    Used for creating triangles, calculating factors
    """

    def __init__(self):
        self.data = self.load_data()
        self.claim_period = 1
        self.set_claim_period()

    def load_data(self, filename: str = 'claims.csv') -> pd.DataFrame:
        """
        Load monthly data.
        """
        df = pd.read_csv(config.get_data_path(filename=filename))
        return df

    def set_claim_period(self, period: int = None) -> None:
        """
        Adds claims period to dataframe.
        """
        if period is not None:
            self.claim_period = period

        self.data['AccidentMonth'] = pd.to_datetime(self.data['AccidentMonth'])
        self.data['DevelopMonth'] = pd.to_datetime(self.data['DevelopMonth'])

        self.data['AM'] = self.data['AccidentMonth'].apply(
            lambda x: x +
            pd.DateOffset(months=(self.claim_period -
                          (x.month - 1) % self.claim_period - 1))
        )

        self.data['DM'] = self.data['DevelopMonth'].apply(
            lambda x: x +
            pd.DateOffset(months=(self.claim_period -
                                  (x.month - 1) % self.claim_period - 1))
        )

    def create_triangle(self, ) -> pd.pivot_table:
        pass
