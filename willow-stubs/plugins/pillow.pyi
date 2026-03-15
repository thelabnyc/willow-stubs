from typing import IO

from PIL.Image import Image as _PILImage

from willow.image import (
    AvifImageFile,
    GIFImageFile,
    HeicImageFile,
    IcoImageFile,
    Image,
    ImageFile,
    JPEGImageFile,
    PNGImageFile,
    RGBAImageBuffer,
    RGBImageBuffer,
    WebPImageFile,
)

class UnsupportedRotation(Exception): ...

class PillowImage(Image):
    image: _PILImage
    def __init__(self, image: _PILImage) -> None: ...
    @classmethod
    def check(cls) -> None: ...
    @classmethod
    def is_format_supported(cls, image_format: str) -> bool: ...
    def get_size(self) -> tuple[int, int]: ...
    def get_frame_count(self) -> int: ...
    def has_alpha(self) -> bool: ...
    def has_animation(self) -> bool: ...
    def resize(self, size: tuple[int, int]) -> PillowImage: ...
    def crop(self, rect: tuple[int, int, int, int]) -> PillowImage: ...
    def rotate(self, angle: int) -> PillowImage: ...
    def set_background_color_rgb(
        self, color: tuple[int, int, int] | list[int]
    ) -> PillowImage: ...
    def get_icc_profile(self) -> bytes | None: ...
    def get_exif_data(self) -> bytes | None: ...
    def transform_colorspace_to_srgb(
        self, rendering_intent: int = 0
    ) -> PillowImage: ...
    def save_as_jpeg(
        self,
        f: IO[bytes],
        quality: int = 85,
        optimize: bool = False,
        progressive: bool = False,
        apply_optimizers: bool = True,
    ) -> JPEGImageFile: ...
    def save_as_png(
        self,
        f: IO[bytes],
        optimize: bool = False,
        apply_optimizers: bool = True,
    ) -> PNGImageFile: ...
    def save_as_gif(
        self, f: IO[bytes], apply_optimizers: bool = True
    ) -> GIFImageFile: ...
    def save_as_webp(
        self,
        f: IO[bytes],
        quality: int = 80,
        lossless: bool = False,
        apply_optimizers: bool = True,
    ) -> WebPImageFile: ...
    def save_as_heic(
        self,
        f: IO[bytes],
        quality: int = 80,
        lossless: bool = False,
        apply_optimizers: bool = True,
    ) -> HeicImageFile: ...
    def save_as_avif(
        self,
        f: IO[bytes],
        quality: int = 80,
        lossless: bool = False,
        apply_optimizers: bool = True,
    ) -> AvifImageFile: ...
    def save_as_ico(
        self, f: IO[bytes], apply_optimizers: bool = True
    ) -> IcoImageFile: ...
    def auto_orient(self) -> PillowImage: ...
    def get_pillow_image(self) -> _PILImage: ...
    @classmethod
    def open(cls, image_file: IO[bytes] | ImageFile) -> PillowImage: ...
    def to_buffer_rgb(self) -> RGBImageBuffer: ...
    def to_buffer_rgba(self) -> RGBAImageBuffer: ...

willow_image_classes: list[type[PillowImage]]
