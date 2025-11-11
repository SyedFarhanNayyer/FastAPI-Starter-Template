from pydantic import BaseModel, Field
from typing import Any, List, Dict, Optional


class WelcomeMessage(BaseModel):
    message : str