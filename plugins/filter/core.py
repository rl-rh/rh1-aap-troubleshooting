import os
from pathlib import Path
from yaml import load, dump
from ansible.errors import AnsibleFilterError

try:
    from yaml import CSafeDumper as SafeDumper
    from yaml import CSafeLoader as SafeLoader
except ImportError:
    from yaml import SafeDumper, SafeLoader  # type: ignore

def list_scenarios(a):
    """
    a: search directory for scenarios
    """
    search_dir = Path(a)
    if not search_dir.is_dir():
        return []

    data = []
    scenarios = [d for d in search_dir.iterdir() if d.is_dir() and 'scenario_' in d.name]
    for idx, sc in enumerate(scenarios):
        # read in the main `vars/main.yml` for the scenario as this will contain
        # specific information related to the role.
        try:
            with open(f"{sc}/vars/main.yml", 'r') as fd:
                sc_data = load(fd.read(), Loader=SafeLoader)
        except FileNotFoundError:
            continue

        # Got to figure out what is the id of the scenario
        # Format should either be scenario_ or scenario-
        if sc_data.get('_id_override', False):
            sc_id = sc_data.get('_id_override')
        elif 'scenario_' in sc_data.get('_scenario_name'):
            sc_id = sc_data.get('_scenario_name').lstrip('scenario_')
        elif 'scenario-' in sc_data.get('_scenario_name'):
            sc_id = sc_data.get('_scenario_name').lstrip('scenario-')
        else:
            continue

        data.append({
            "id": str(sc_id),
            "name": sc_data.get('_scenario_name', '').strip(),
            'description': sc_data.get('_description', ''),
            'path': f"roles/{os.path.basename(sc)}",
        })

    return data

class FilterModule(object):
    def filters(self):
        return {
            'list_scenarios': list_scenarios
        }