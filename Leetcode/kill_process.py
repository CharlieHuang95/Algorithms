# Kill Process

# Given two arrays:
# pid  = [1, 3, 10, 5]
# ppid = [3, 0, 5, 3]
# The first contains the ProcessID of processes.
# The second contains the parent ProcessID of the processes.
# And also given ID, figure out all the processes to be killed.

# This problem can be solved by simulating the process relationships
# with a graph.

def kill_process(pid, ppid, kill_id):
    # Create a graph of the relationships
    graph = {}
    for index, parent in enumerate(ppid):
        if parent in graph:
            graph[parent].add(pid[index])
        else:
            graph[parent] = set([pid[index]])
            
    # Collect all children (sucessors) of all the kill_id
    to_be_killed = set()
    stack = [kill_id]
    while stack:
        cur = stack.pop()
        to_be_killed.add(cur)
        if cur in graph:
            for child in graph[cur]:
                if child in to_be_killed:
                    print "Error: Cyclic Relationship Detected"
                    return
                stack.append(child)
    return list(to_be_killed)
