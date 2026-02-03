import yaml

from promptum.benchmark.report import Report
from promptum.serialization.base import BaseSerializer


class YAMLSerializer(BaseSerializer):
    def serialize(self, report: Report) -> str:
        data = {
            "summary": report.get_summary(),
            "results": [self._serialize_result(r) for r in report.results],
        }
        return yaml.dump(data, default_flow_style=False, sort_keys=False)

    def get_file_extension(self) -> str:
        return "yaml"
