import pytest
import logging
@pytest.fixture(autouse=True)
def raise_logging(caplog):
    caplog.set_level(logging.INFO)
