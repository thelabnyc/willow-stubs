from typing import ClassVar

from .base import OptimizerBase

__all__ = ["Gifsicle"]

class Gifsicle(OptimizerBase):
    library_name: ClassVar[str]
    image_format: ClassVar[str]
    @classmethod
    def get_command_arguments(cls, file_path: str) -> list[str]: ...
