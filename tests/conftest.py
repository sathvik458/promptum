from datetime import datetime

import pytest

from promptum.core import Metrics, TestCase, TestResult
from promptum.validation import Contains


@pytest.fixture
def sample_metrics() -> Metrics:
    return Metrics(
        latency_ms=100.0,
        prompt_tokens=10,
        completion_tokens=20,
        total_tokens=30,
        cost_usd=0.01,
    )


@pytest.fixture
def sample_test_case() -> TestCase:
    return TestCase(
        name="test_example",
        prompt="What is 2+2?",
        model="gpt-3.5-turbo",
        validator=Contains("4"),
        tags=("math", "easy"),
    )


@pytest.fixture
def sample_test_result(sample_test_case: TestCase, sample_metrics: Metrics) -> TestResult:
    return TestResult(
        test_case=sample_test_case,
        response="The answer is 4",
        passed=True,
        metrics=sample_metrics,
        validation_details={"matched": True},
        timestamp=datetime.now(),
    )
