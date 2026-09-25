

def scan():
    print("Running network scan...")

def report():
    print("Generating report...")

def clean():
    print("Cleaning logs...")

def analyse():
    print("Analysing traffic...")

dispatch = {
    'scan': scan,
    'report': report,
    'clean': clean,
    'analyse': analyse,
}

actions = ['scan', 'clean', 'report', 'unknown', 'analyse']

for action in actions:
    fn = dispatch.get(action)
    if fn:
        fn()
    else:
        print(f"unknown action: {action}")





