from collections.abc import Callable, Generator
from typing import Any

from .image import Image
from .optimizers.base import OptimizerBase

class UnrecognisedOperationError(LookupError): ...
class UnavailableOperationError(LookupError): ...
class UnroutableOperationError(LookupError): ...

class WillowRegistry:
    def __init__(self) -> None: ...
    def register_operation(
        self,
        image_class: type[Image],
        operation_name: str,
        func: Callable[..., Any],
    ) -> None: ...
    def register_converter(
        self,
        from_image_class: type[Image],
        to_image_class: type[Image],
        func: Callable[..., Any],
        cost: int | None = None,
    ) -> None: ...
    def register_image_class(self, image_class: type[Image]) -> None: ...
    def register_plugin(self, plugin: Any) -> None: ...
    def register_optimizer(self, optimizer_class: type[OptimizerBase]) -> None: ...
    def get_operation(
        self, image_class: type[Image], operation_name: str
    ) -> Callable[..., Any]: ...
    def operation_exists(self, operation_name: str) -> bool: ...
    def get_converter(
        self, from_image_class: type[Image], to_image_class: type[Image]
    ) -> Callable[..., Any]: ...
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
    ) -> Generator[tuple[Callable[..., Any], type[Image]]]: ...
    def find_all_paths(
        self,
        start: type[Image],
        end: type[Image],
        path: list[tuple[Callable[..., Any], type[Image]]] = ...,
        seen_classes: set[type[Image]] = ...,
    ) -> list[list[tuple[Callable[..., Any], type[Image]]]]: ...
    def get_path_cost(
        self,
        start: type[Image],
        path: list[tuple[Callable[..., Any], type[Image]]],
    ) -> int: ...
    def find_shortest_path(
        self, start: type[Image], end: type[Image]
    ) -> tuple[list[tuple[Callable[..., Any], type[Image]]] | None, int | None]: ...
    def find_closest_image_class(
        self, start: type[Image], image_classes: set[type[Image]]
    ) -> tuple[
        type[Image] | None,
        list[tuple[Callable[..., Any], type[Image]]] | None,
        int | None,
    ]: ...
    def find_operation(
        self, from_class: type[Image], operation_name: str
    ) -> tuple[
        Callable[..., Any],
        type[Image],
        list[tuple[Callable[..., Any], type[Image]]],
        int,
    ]: ...

registry: WillowRegistry
