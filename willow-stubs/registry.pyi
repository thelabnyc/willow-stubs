import types
from collections.abc import Callable, Generator
from typing import Any

from .image import Image
from .optimizers.base import OptimizerBase

_ConverterFunc = Callable[..., Image]
_OperationFunc = Callable[..., Any]
_PathStep = tuple[_ConverterFunc, type[Image]]

class UnrecognisedOperationError(LookupError): ...
class UnavailableOperationError(LookupError): ...
class UnroutableOperationError(LookupError): ...

class WillowRegistry:
    def __init__(self) -> None: ...
    def register_operation(
        self,
        image_class: type[Image],
        operation_name: str,
        func: _OperationFunc,
    ) -> None: ...
    def register_converter(
        self,
        from_image_class: type[Image],
        to_image_class: type[Image],
        func: _ConverterFunc,
        cost: int | None = None,
    ) -> None: ...
    def register_image_class(self, image_class: type[Image]) -> None: ...
    def register_plugin(self, plugin: types.ModuleType) -> None: ...
    def register_optimizer(self, optimizer_class: type[OptimizerBase]) -> None: ...
    def get_operation(
        self, image_class: type[Image], operation_name: str
    ) -> _OperationFunc: ...
    def operation_exists(self, operation_name: str) -> bool: ...
    def get_converter(
        self, from_image_class: type[Image], to_image_class: type[Image]
    ) -> _ConverterFunc: ...
    def get_converter_cost(
        self, from_image_class: type[Image], to_image_class: type[Image]
    ) -> int: ...
    def get_image_classes(
        self,
        with_operation: str | None = None,
        available: bool | None = None,
    ) -> set[type[Image]]: ...
    def get_optimizers_for_format(
        self, image_format: str
    ) -> list[type[OptimizerBase]]: ...
    def get_converters_from(
        self, from_image_class: type[Image]
    ) -> Generator[_PathStep]: ...
    def find_all_paths(
        self,
        start: type[Image],
        end: type[Image],
        path: list[_PathStep] = ...,
        seen_classes: set[type[Image]] = ...,
    ) -> list[list[_PathStep]]: ...
    def get_path_cost(
        self,
        start: type[Image],
        path: list[_PathStep],
    ) -> int: ...
    def find_shortest_path(
        self, start: type[Image], end: type[Image]
    ) -> tuple[list[_PathStep] | None, int | None]: ...
    def find_closest_image_class(
        self, start: type[Image], image_classes: set[type[Image]]
    ) -> tuple[
        type[Image] | None,
        list[_PathStep] | None,
        int | None,
    ]: ...
    def find_operation(
        self, from_class: type[Image], operation_name: str
    ) -> tuple[
        _OperationFunc,
        type[Image],
        list[_PathStep],
        int,
    ]: ...

registry: WillowRegistry
