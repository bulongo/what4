from dataclasses import dataclass

@dataclass
class Task:
    # category: str
    body: str
    completed: bool = False

    def say_task(self):
        return f"{self.body}"

