from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Task:
    id: int
    title: str
    done: bool = False
    # BUG intencional: usei field(default=...) em vez de default_factory, isso não cria timestamps corretos
    created_at: datetime = field(default=datetime.now)
