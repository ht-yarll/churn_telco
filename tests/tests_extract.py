import pytest
from churn_telco.strategy.ExtractStrategy import ExtractFromLocalCSV

import polars as pl

def test_transform_csv_data_local_returns_df():
    file_path = tmp_path / "test.csv"
    file_path.write_text("nome,idade\nJoão,30\nMaria,40")

    extractor = ExtractFromLocalCSV()
    dfs = extractor.extract()
    
    assert isinstance(dfs, list)
    assert all(isinstance(df, pl.DataFrame) for df in dfs)
    