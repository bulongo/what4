################## WHAT4 #################

import json
import time
from pathlib import Path
from dataclasses import dataclass, asdict

## custom modules ##
from functions.clear import clear
from action_selector import action_selector
from save_tasks import save_tasks
from show_tasks import show_tasks
from load_tasks import load_tasks
Tasks = []

print("WHAT4")

show_tasks(Tasks)
action_selector(Tasks)
