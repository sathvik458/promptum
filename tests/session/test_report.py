from datetime import datetime, timezone

from promptum.session import Report, Prompt, TestResult
from promptum.providers.metrics import Metrics


def _make_result() -> TestResult:
    prompt = Prompt(
        name="name",
        prompt="prompt",
        model="model",
        validator=None,
        tags=(),
    )

    return TestResult(
        test_case=prompt,
        response="response",
        passed=True,
        metrics=Metrics(latency_ms=1.0, cost_usd=0.0),
        validation_details={},
        execution_error=None,
        timestamp=datetime.now(timezone.utc),
    )


def test_report_results_are_converted_to_tuple() -> None:
    result = _make_result()
    original = [result]

    report = Report(results=original)

    assert isinstance(report.results, tuple)


def test_report_results_not_affected_by_external_mutation() -> None:
    result = _make_result()
    original = [result]

    report = Report(results=original)

    original.append(result)

    assert len(report.results) == 1