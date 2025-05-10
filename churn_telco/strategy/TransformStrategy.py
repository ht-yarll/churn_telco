from abc import ABC, abstractmethod
import re
import unicodedata
import polars as pl

class TransformDataStrategy(ABC):
    @abstractmethod
    def transform(self):
        ...

class TransformCSVDataLocal(TransformDataStrategy):
    def __init__(self, df: pl.DataFrame, config: dict):
        self.df = df
        self.config = config

    def transform(self) -> pl.DataFrame:
        renamed_cols = {
            col: self._sanitize_column_names(col) for col in self.df.columns
        }
        print(100*'=')
        print("🔁 Renamed columns:", renamed_cols)
        print(100*'=')
        sanitized_df = self.df.rename(renamed_cols)

        for col in sanitized_df.columns:
            if sanitized_df[col].dtype == pl.Utf8:
                sanitized_df = sanitized_df.with_columns(
                    pl.col(col).apply(self._sanitize_it).alias(col)
                )

        sanitized_df.write_parquet(self.config['stage_path'])
        print('🟢 Success On Basic Transformation')
        return sanitized_df
    
    def _sanitize_it(self, text):
        if not isinstance(text, str):
            return text
        
        if re.match(r'^-?\d+[.,]?\d*$', text):
            return text

        text = unicodedata.normalize("NFKD", text)
        text = text.encode("ASCII", "ignore").decode("ASCII") 
        text = re.sub(r'[\x00-\x1F\x7F]', '', text)
        text = re.sub(r'[^A-Za-z0-9\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    
    def _sanitize_column_names(self, name: str) -> str:
        name = unicodedata.normalize("NFKD", name)
        name = name.encode("ASCII", "ignore").decode("ASCII")
        name = re.sub(r'[^A-Za-z0-9_]', '_', name)
        name = re.sub(r'_+', '_', name).strip('_')
        return name.lower()