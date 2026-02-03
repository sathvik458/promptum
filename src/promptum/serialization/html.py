import json
from pathlib import Path

from jinja2 import Template

from promptum.benchmark.report import Report


class HTMLSerializer:
    def __init__(self) -> None:
        template_path = Path(__file__).parent / "report_template.html"
        self._template = Template(template_path.read_text())

    def serialize(self, report: Report) -> str:
        summary = report.get_summary()

        results_data = []
        for result in report.results:
            results_data.append(
                {
                    "test_case": {
                        "name": result.test_case.name,
                        "prompt": result.test_case.prompt,
                        "model": result.test_case.model,
                        "tags": list(result.test_case.tags),
                        "system_prompt": result.test_case.system_prompt,
                        "validator": result.test_case.validator.describe(),
                    },
                    "response": result.response,
                    "passed": result.passed,
                    "metrics": {
                        "latency_ms": result.metrics.latency_ms,
                        "prompt_tokens": result.metrics.prompt_tokens,
                        "completion_tokens": result.metrics.completion_tokens,
                        "total_tokens": result.metrics.total_tokens,
                        "cost_usd": result.metrics.cost_usd,
                        "total_attempts": result.metrics.total_attempts,
                    }
                    if result.metrics
                    else None,
                    "execution_error": result.execution_error,
                }
            )

        return self._template.render(
            summary=summary,
            results=results_data,
            results_json=json.dumps(results_data),
        )

    def get_file_extension(self) -> str:
        return "html"
