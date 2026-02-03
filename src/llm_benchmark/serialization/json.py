import json
from datetime import datetime
from typing import Any

from llm_benchmark.benchmark.report import Report


class JSONSerializer:
    def __init__(self, indent: int = 2):
        self.indent = indent

    def serialize(self, report: Report) -> str:
        data = {
            "metadata": report.metadata,
            "summary": report.get_summary(),
            "results": [self._serialize_result(r) for r in report.results],
        }
        return json.dumps(data, indent=self.indent, default=self._json_default)

    def get_file_extension(self) -> str:
        return "json"

    @staticmethod
    def _serialize_result(result: Any) -> dict[str, Any]:
        return {
            "test_case": {
                "name": result.test_case.name,
                "prompt": result.test_case.prompt,
                "model": result.test_case.model,
                "tags": list(result.test_case.tags),
                "system_prompt": result.test_case.system_prompt,
                "temperature": result.test_case.temperature,
                "max_tokens": result.test_case.max_tokens,
                "metadata": result.test_case.metadata,
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
                "retry_delays": list(result.metrics.retry_delays),
                "total_attempts": result.metrics.total_attempts,
            }
            if result.metrics
            else None,
            "validation_details": result.validation_details,
            "execution_error": result.execution_error,
            "timestamp": result.timestamp.isoformat(),
        }

    @staticmethod
    def _json_default(obj: Any) -> Any:
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")
