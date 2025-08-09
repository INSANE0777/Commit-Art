from datetime import date, timedelta
from time import sleep
from subprocess import call

today = date.today()
start_date = today - timedelta(days=today.weekday() + 2, weeks=52)

# should correspond to the first contribution box on GitHub
# print(start_date.ctime())

matrix = """
..........................................
##.##...##..#######..####..##...##.#######
##.###..##..##......##..##.###..##.##.....
##.##.#.##..#######.######.##.#.##.#####..
##.##..###.......##.##..##.##..###.##.....
##.##...##..#######.##..##.##...##.#######
..........................................
"""


lines = matrix.strip().split("\n")
columns = zip(*lines)

counter = 0

# Using shell=True to ensure system commands are recognized
call(['rmdir', '/s', '/q', '.git'], shell=True)  # Removes .git folder (recursive, quiet)
call(['del', '/f', 'delta.txt'], shell=True)    # Deletes delta.txt file
call(['git', 'init'])

def write_delta(d):
    with open('delta.txt', 'w') as f:
        f.write(str(d))

call(['git', 'add', '-A'])
call(['git', 'commit', '-am', 'Initial commit'])

for c in columns:
    for d in c:
        counter += 1
        if d != "#":
            continue
        # print(d, (start_date + timedelta(days=counter)).ctime())
        write_delta(counter)
        call(['git', 'add', '-A'])
        call(['git', 'commit', '--date', (start_date + timedelta(days=counter)).ctime(), '-am', str(counter)])
