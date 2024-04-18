from typing import Dict, Optional
from nicegui.element import Element


class G6(
    Element,
    component="g6.js",
):
    def __init__(
        self,
        defaults: Optional[Dict] = None,
    ) -> None:
        super().__init__()
