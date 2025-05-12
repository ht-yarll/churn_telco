import pytest
from churn_telco.strategy.LoadToPostgresStrategy import LoadDataPostgres
from churn_telco.utils.config import load_config

import polars as pl

def test_transform_csv_data_local_returns_df(tmp_path):

    df = pl.DataFrame({
        "nome": ["João", "Maria"],
        "idade": [30, 40]
    })

    file_path = tmp_path / "test.parquet"
    df.write_parquet(file_path)

    c = load_config()

    config = {
        "stage_path": str(tmp_path),
        "databanks": {
            "postgres": {
                "db_uri": c['databanks']['postgres']['db_uri'],
                "set_name": {
                    "dataset": "test_dset",
                    "if_exists": "replace",
                    "chunksize": 10000
              }
            }
        }
    }

    loader = LoadDataPostgres(config)
    dfs = loader.load()
    
    assert True