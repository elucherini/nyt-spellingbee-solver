# New York Times Spelling Bee solver

This script uses a simple linear search algorithm in a dictionary of English words to generate a **superset** of the words in the solution.

**Note:** Some of the generated words cannot be used in the solution. The NYTimes uses a more limited dictionary.

**Usage**

`python3 solve.py -l (letters in gray separated by a space) -r (required central letter)`

**Example:**

`python3 solve.py -l w a m o n l k -r n`

