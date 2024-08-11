from pydantic import BaseModel


class SearchParameters(BaseModel):
    origin: str
    destination: str
    start_date: str
    end_date: str
    passangers: str