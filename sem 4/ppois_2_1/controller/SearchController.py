
import datetime
from typing import Optional

class SearchController:
    def __init__(self, name: Optional[str] = None, address: Optional[str] = None, birthdate: Optional[datetime] = None,
                 appdate: Optional[datetime] = None,
                 docname: Optional[str] = None, concl: Optional[str] = None, page_number: int = 1, page_size: int = 10, criteria: str | None = None):
        self.name = name
        self.address = address
        self.birthdate = birthdate
        self.appdate = appdate
        self.docname = docname
        self.concl = concl
        self.page_number: int = page_number
        self.page_size: int = page_size
        self.criteria = criteria

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_birthdate(self):
        return self.birthdate

    def get_appdate(self):
        return self.appdate

    def get_docname(self):
        return self.docname

    def get_concl(self):
        return self.concl


