import pathlib
from churn_telco.interfaces.extract_strategy_interface import ExtractDataStrategy
import polars as pl

class ExtractFromLocalCSV(ExtractDataStrategy):
    def __init__(self, config: dict):
        self.file_path = pathlib.Path(config['raw_path'])

    def extract(self):
        dataframes = self._read_csv()
        return dataframes

    def _read_csv(self):
        dataframes = []
        for file in self.file_path.iterdir():
            extension = file.suffix
            try:
                if extension == '.csv':
                    df = pl.read_csv(file)
                    dataframes.append((file.stem, df))
                elif extension in ['.gz', '.gzip']:
                    size_in_mb = file.stat().st_size / (1024 * 1024)
                    if size_in_mb > 750:
                        df = pl.read_csv_batched(file).collect()
                        dataframes.append((file.stem, df))
                    else:
                        df = pl.read_csv(file)
                        dataframes.append((file.stem, df))
                
            except Exception as e:
                print(f'Unable to read csv: {e}')
                continue

        return dataframes