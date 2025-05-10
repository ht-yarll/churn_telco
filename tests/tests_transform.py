import pytest

from churn_telco.strategy.TransformStrategy import TransformCSVDataLocal

import polars as pl

def test_transform_csv_data_local_returns_df():
    df = pl.DataFrame({
    "Nome": ["José", "MÁRIA", "João!"],
    "Idade": ["30", "40", "50"]
    })
    stage_path = tmp_path / "output.parquet"

    config = {"stage_path": str(stage_path)}

    transformer = TransformCSVDataLocal(df, config)
    result_df = transformer.transform()

    assert isinstance(result_df, pl.DataFrame)
    assert stage_path.exists()
    assert "nome" in result_df.columns
