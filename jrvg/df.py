import pandas as pd
from pathlib import Path
from jrvg.files import get_suffix


@pd.api.extensions.register_dataframe_accessor("j")
class JrvgAccessor:

    _obj: pd.DataFrame

    def __init__(self, pandas_obj):
        self._validate(pandas_obj)
        self._obj=pandas_obj
        
    @staticmethod
    def _validate(_):
        pass

    def desc(self):
        return self._obj.describe(percentiles=[0.01, 0.1, 0.25, 0.5, 0.75, 0.9, 0.99])


def load_df(file: str | Path) -> pd.DataFrame:
    suffix = get_suffix(file)
    match suffix:
        case 'csv':
            return pd.read_csv(file)
        case 'parquet':
            return pd.read_parquet(file)
        case other:
            raise ValueError(f'File extension `{other}` not supported')
