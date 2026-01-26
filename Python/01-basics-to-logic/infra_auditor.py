raw_inventory = [
    {"id": "srv-01", "tags": ["web", "prod", "germany"], "metrics": {"cpu_load": 85, "memory_gb": 16}, "status": "online"},
    {"id": "srv-02", "tags": ["db", "prod"], "metrics": {"cpu_load": 40, "memory_gb": 32}, "status": "online"},
    {"id": "srv-03", "tags": ["app", "dev"], "metrics": {"cpu_load": 15, "memory_gb": 8}, "status": "offline"},
    {"id": "srv-01", "tags": ["web", "prod"], "metrics": {"cpu_load": 85, "memory_gb": 16}, "status": "online"}
]

# --- Basics & Logic ---
unique_ids = list(set(s['id'] for s in raw_inventory))
second_srv_mem = raw_inventory[1]['metrics']['memory_gb']
for s in raw_inventory:
    if s['id'] == "srv-01": s['tags'].append("backup")
prod_servers = [s for s in raw_inventory if "prod" in s['tags']]
uptime = raw_inventory[0].get('uptime', 0)

# Cleaning for aggregation (Removing duplicates)
unique_inventory = {s['id']: s for s in raw_inventory}.values()
total_ram = sum(s['metrics']['memory_gb'] for s in unique_inventory)

# --- Professional DevOps Mastery ---
# 1. List Comprehension
high_load_servers = [s['id'] for s in unique_inventory if s['metrics']['cpu_load'] > 50]

# 2. Dictionary Map
status_report = {s['id']: s['status'] for s in unique_inventory}

# 3. Error Handling Logic
threshold = 80
for s in unique_inventory:
    if s['metrics']['cpu_load'] > threshold:
        print(f"ALERT: {s['id']} is overloaded!")

# 4. Data Integrity (Set Difference)
expected_nodes = {"srv-01", "srv-02", "srv-03", "srv-04"}
current_nodes = set(s['id'] for s in unique_inventory)
missing_nodes = expected_nodes - current_nodes
print(f"Missing: {missing_nodes}")

# 5. Tuple Unpacking
location = ("Frankfurt", "Zone-A", "Rack-12")
city, zone, rack = location
print(f"Location: {city}, {zone}, {rack}")