import pytest

from promptum.validation import Contains, ExactMatch, JsonSchema, Regex


@pytest.fixture
def exact_match_validator() -> ExactMatch:
    return ExactMatch("Hello")


@pytest.fixture
def contains_validator() -> Contains:
    return Contains("world")


@pytest.fixture
def regex_validator() -> Regex:
    return Regex(r"\d{3}-\d{4}")


@pytest.fixture
def json_schema_validator() -> JsonSchema:
    return JsonSchema(required_keys=("name", "age"))
