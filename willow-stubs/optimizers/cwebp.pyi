from typing import ClassVar

from .base import OptimizerBase

__all__ = ["Cwebp"]

class Cwebp(OptimizerBase):
    library_name: ClassVar[str]
    image_format: ClassVar[str]
    @classmethod
    def get_check_library_arguments(cls) -> list[str]: ...
    @classmethod
    def get_command_arguments(cls, file_path: str, progressive: bool = False) -> list[str]: ...  # type: ignore[override]
