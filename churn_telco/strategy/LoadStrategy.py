from abc import ABC, abstractmethod

class LoadDataStrategy(ABC):
    @abstractmethod
    def load():
        ...

class LoadDataPostgres(LoadDataStrategy):
    def __init__(self):
        ...
    
    def load_file_to_postgres(
        file_path: str | pathlib.Path,
        table_name: str,
        db_uri: str,
        file_type: Literal["csv", "parquet"] = "csv",
        if_exists: Literal["fail", "replace", "append"] = "append",
        chunksize: int | None = None
    ):
        ...