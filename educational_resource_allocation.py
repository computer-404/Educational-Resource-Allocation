from taipy.gui import Gui, notify
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests as request


school = "School"
num_students = 0
num_resources = 0
allocated_resources = []
page = """
# Resource Allocation for Schools

<|layout|columns=1 1 1|
<|
**Number of Students:** <|{num_students}|input|type=number|label=Number of Students|>

**Number of Resources:** <|{num_resources}|input|type=number|label=Number of Resources|>
<|Allocate Resources|button|on_action=allocate_resources|>
|>

<|ResourceAllocation|expandable|
<|{allocated_resources}|table|width=100%|number_format=%.2f|>
|>
|>
"""

def allocate_resources(state):

    state.num_resources = int(state.num_resources)
    state.num_students = int(state.num_students)

    # Calculate the number of resources each student should receive
    resources_per_student = state.num_resources // state.num_students

    # Calculate the remaining resources after equitable allocation
    remaining_resources = state.num_resources % state.num_students

    # Create a list to store the number of resources each student will receive
    allocation = [resources_per_student] * state.num_students

    # Distribute the remaining resources evenly among the students
    for i in range(remaining_resources):
        allocation[i] += 1
    state.allocated_resources = allocation

if __name__ == "__main__":
    Gui(page).run(margin="0em", title="Sales Dashboard")