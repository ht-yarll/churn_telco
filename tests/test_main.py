import pytest
from churn_telco.main import main

def test_main_funciton_returns_true():
    result = main()
    assert result == '🎉 Success 🎉'