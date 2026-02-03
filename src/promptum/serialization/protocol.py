from typing import Protocol

from promptum.benchmark.report import Report


class Serializer(Protocol):
    def serialize(self, report: Report) -> str:
        """Serializes a Report to a string format."""
        ...

    def get_file_extension(self) -> str:
        """Returns the file extension for this format (e.g., 'json', 'html')."""
        ...
