import pathlib
from abc import ABC, abstractmethod
from typing import Literal

import polars as pl
import re
from sqlalchemy import create_engine, inspect, text

class LoadDataStrategy(ABC):
    @abstractmethod
    def load():
        ...

class LoadDataPostgres(LoadDataStrategy):
    def __init__(self, config:dict):
        self.db_uri = config['databanks']['postgres']['db_uri']
        self.file_path = config['stage_path']
        self.schema_name = config['databanks']['postgres']['set_name']['dataset']
        self.if_exists = config['databanks']['postgres']['set_name']['if_exists']
        self.chunksize = config['databanks']['postgres']['set_name']['chunksize']

    def load(self):
        engine = create_engine(self.db_uri)

        with engine.begin() as conn:
            conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {self.schema_name}"))

        for file in pathlib.Path(self.file_path).iterdir():
            print(f"👀 reading {file.name}.")
            table_name = self._saniteze_table_names(file.stem)
            table_path = f"{self.schema_name}.{table_name}"

            inspector = inspect(engine)
            tables = inspector.get_table_names(schema=self.schema_name)
            if table_name not in tables:
                print(f"Tabela '{self.schema_name}.{table_name}' não existe e será criada.")

                df = pl.read_parquet(file).to_pandas()
                size_mb = df.memory_usage(deep=True).sum() / (1024**2)

                df.to_sql(
                    name = table_name,
                    schema=self.schema_name,
                    con = engine,
                    if_exists = self.if_exists,
                    method = 'multi',
                    chunksize = self.chunksize if size_mb > 750 else None
                )

                print(f"🟢 DataFrame ({round(size_mb, 2)} MB) loaded to table '{table_path}'.")
    
    def _saniteze_table_names(self, name:str) -> str:
        name = re.sub(r'\W+', '_', name)
        return name.lower().strip('_')