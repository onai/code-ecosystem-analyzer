from collections import defaultdict
import dis
import json
import sys
import os

res = {}

for repo_dir in os.listdir(sys.argv[1]):
    repo_imports = []
    full_repo_path = os.path.join(sys.argv[1], repo_dir)
    for root, dirs, files in os.walk(full_repo_path):
        for filename in files:
            if not filename.endswith('.py'):
                continue

            full_path = os.path.join(root, filename)

            try:
                with open(full_path) as handle:

                    statements = handle.read()
                    instructions = dis.get_instructions(statements)
                    imports = [__ for __ in instructions if 'IMPORT' in __.opname]
                    grouped = defaultdict(list)
                    for instr in imports:
                        grouped[instr.opname].append(instr.argval)

                    repo_imports.extend(grouped['IMPORT_NAME'])
            except:
                pass

    print(json.dumps(repo_imports))




