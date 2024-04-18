from pathlib import Path
from typing import Dict, List, Optional
from nicegui.element import Element


class G6(
    Element,
    component="g6.js",
):
    def __init__(
        self,
        data: Dict,
        options: Optional[Dict] = None,
    ) -> None:
        super().__init__()
        self._props["data"] = data
        self._props["graphOptions"] = options or {}
        self.style("width: 100%; min-height: 16rem;")
