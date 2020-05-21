from collections import defaultdict
import dis
import sys
import os

res = {}

for root, dirs, files in os.walk(sys.argv[1]):
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

                for mod in set(grouped['IMPORT_NAME']):
                    print(mod)
        except:
            pass



