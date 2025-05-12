import pytest

from churn_telco.strategy.TransformCSVLocalStrategy import TransformCSVDataLocal

import polars as pl

def test_transform_csv_data_local_returns_df(tmp_path):
    filename = 'test_df'
    df = pl.DataFrame({
    "Nome": ["José", "MÁRIA", "João!"],
    "Idade": ["30", "40", "50"]
    })
    stage_path = tmp_path / "output.parquet"

    config = {"stage_path": str(stage_path)}

    transformer = TransformCSVDataLocal(config)
    result_df = transformer.transform(df, filename)

    assert isinstance(result_df, pl.DataFrame)
    assert stage_path.exists()
    assert "nome" in result_df.columns
