import pandas as pd
events = pd.read_json("normalized_events.json")
row_count = len(events)
print(row_count)
