from typing import NamedTuple, Optional

class LocatorData(NamedTuple):
    selector: str
    description: str
    nth: Optional[int] = None
    click: bool = False
    input: bool = False
