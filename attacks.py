import json

def load_json_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def find_attack_group(attack_data, group_name):
    events = [event for event in attack_data if event['attack group'].lower() == group_name.lower()]
    return events

def display_kill_chain_details(events):
    for event in events:
        print(f"Event: {event['event']}")
        print(f"Target: {event['target']}")
        print(f"Tactic: {event['tactic']}")
        print(f"Technique: {event['technique']}")
        print()

def display_data_sources(events):
    data_sources = set()
    for event in events:
        data_sources.update(event['data sources'])
    print("Data Sources:")
    for source in data_sources:
        print(f"- {source}: This source can be used to detect and analyze various phases of an attack by providing relevant information and context.")

def main():
    attack_data = load_json_data('attacks.json')
    attack_group = input("Enter the attack group: ")
    events = find_attack_group(attack_data, attack_group)
    
    if not events:
        print(":(")
        print("Error: Attack group not found.")
    else:
        display_kill_chain_details(events)
        display_data_sources(events)

if __name__ == "__main__":
    main()
