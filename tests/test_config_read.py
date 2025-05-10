import pytest
from churn_telco.utils.config import load_config

def test_config_returns_dict():
    config = load_config()
    assert isinstance(config, dict)