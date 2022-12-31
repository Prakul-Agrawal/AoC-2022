class State:
    def __init__(self, ore, clay, obs, geode, ore_rob, clay_rob, obs_rob,time):
        self.ore = ore
        self.clay = clay
        self.obs = obs
        self.geode = geode
        self.ore_rob = ore_rob
        self.clay_rob = clay_rob
        self.obs_rob = obs_rob
        self.time = time

def make_ore_robot(cur_state,cost):
    global Max_geode
    l = [0 for i in range(8)]
    if cur_state.ore >= cost[0]:
        req_time = 1
    else:    
        req_time = ((cost[0] - cur_state.ore) - 1) // cur_state.ore_rob + 2

    if req_time + cur_state.time <= 24:
        l[0] = cur_state.ore + req_time * cur_state.ore_rob - cost[0]
        l[1] = cur_state.clay + req_time * cur_state.clay_rob
        l[2] = cur_state.obs + req_time * cur_state.obs_rob
        l[3] = cur_state.geode
        l[4] = cur_state.ore_rob + 1
        l[5] = cur_state.clay_rob
        l[6] = cur_state.obs_rob
        l[7] = cur_state.time + req_time
        if l[7] <= 22:
            return State(*l)

    if cur_state.geode > Max_geode:
        Max_geode = cur_state.geode

def make_clay_robot(cur_state,cost):
    global Max_geode
    l = [0 for i in range(8)]
    if cur_state.ore >= cost[1]:
        req_time = 1
    else:    
        req_time = ((cost[1] - cur_state.ore) - 1) // cur_state.ore_rob + 2

    if req_time + cur_state.time <= 24:
        l[0] = cur_state.ore + req_time * cur_state.ore_rob - cost[1]
        l[1] = cur_state.clay + req_time * cur_state.clay_rob
        l[2] = cur_state.obs + req_time * cur_state.obs_rob
        l[3] = cur_state.geode
        l[4] = cur_state.ore_rob
        l[5] = cur_state.clay_rob + 1
        l[6] = cur_state.obs_rob
        l[7] = cur_state.time + req_time
        if l[7] <= 22:
            return State(*l)

    if cur_state.geode > Max_geode:
        Max_geode = cur_state.geode

def make_obs_robot(cur_state,cost):
    global Max_geode
    l = [0 for i in range(8)]
    if cur_state.ore >= cost[2] and cur_state.clay >= cost[3]:
        req_time = 1
    else:    
        req_time = max(((cost[2] - cur_state.ore) - 1) // cur_state.ore_rob + 2,
                       ((cost[3] - cur_state.clay) - 1) // cur_state.clay_rob + 2)

    if req_time + cur_state.time <= 24:
        l[0] = cur_state.ore + req_time * cur_state.ore_rob - cost[2]
        l[1] = cur_state.clay + req_time * cur_state.clay_rob - cost[3]
        l[2] = cur_state.obs + req_time * cur_state.obs_rob
        l[3] = cur_state.geode
        l[4] = cur_state.ore_rob
        l[5] = cur_state.clay_rob
        l[6] = cur_state.obs_rob + 1
        l[7] = cur_state.time + req_time
        if l[7] <= 22:
            return State(*l)

    if cur_state.geode > Max_geode:
        Max_geode = cur_state.geode

def make_geode_robot(cur_state,cost):
    global Max_geode
    l = [0 for i in range(8)]
    if cur_state.ore >= cost[4] and cur_state.obs >= cost[5]:
        req_time = 1
    else:    
        req_time = max(((cost[4] - cur_state.ore) - 1) // cur_state.ore_rob + 2,
                       ((cost[5] - cur_state.obs) - 1) // cur_state.obs_rob + 2)

    if req_time + cur_state.time <= 24:
        l[0] = cur_state.ore + req_time * cur_state.ore_rob - cost[4]
        l[1] = cur_state.clay + req_time * cur_state.clay_rob
        l[2] = cur_state.obs + req_time * cur_state.obs_rob - cost[5] 
        l[4] = cur_state.ore_rob
        l[5] = cur_state.clay_rob
        l[6] = cur_state.obs_rob
        l[7] = cur_state.time + req_time
        l[3] = cur_state.geode + 24 - cur_state.time - req_time
        if l[7] <= 22:
            return State(*l)
        elif l[3] > Max_geode:
            Max_geode = l[3]

    if cur_state.geode > Max_geode:
        Max_geode = cur_state.geode

def dfs(cur_state):
    rem_time = 24 - cur_state.time
    if rem_time > 2:
        if cur_state.ore_rob * rem_time + cur_state.ore < rem_time * max_ore_rob:
            new_state = make_ore_robot(cur_state, cost)
            if new_state and \
               new_state.geode + (24 - new_state.time) * (23 - new_state.time) // 2 > Max_geode:
                dfs(new_state)
        if cur_state.clay_rob * rem_time + cur_state.clay < rem_time * max_clay_rob:
            new_state = make_clay_robot(cur_state, cost)
            if new_state and \
               new_state.geode + (24 - new_state.time) * (23 - new_state.time) // 2 > Max_geode:
                dfs(new_state)
        if cur_state.obs_rob * rem_time + cur_state.obs < rem_time * max_obs_rob \
           and cur_state.clay_rob:
            new_state = make_obs_robot(cur_state, cost)
            if new_state and \
               new_state.geode + (24 - new_state.time) * (23 - new_state.time) // 2 > Max_geode:
                dfs(new_state)
    if cur_state.obs_rob:
        new_state = make_geode_robot(cur_state, cost)
        if new_state and \
            new_state.geode + (24 - new_state.time) * (23 - new_state.time) // 2 > Max_geode:
             dfs(new_state)

costs = []
while True:
    s = input().split()
    if s == ['-1']:
        break
    cost = [int(s[6]),int(s[12]),int(s[18]),int(s[21]),int(s[27]),int(s[30])]
    costs.append(cost)


total = 0
for i in range(len(costs)):
    cost = costs[i]
    Max_geode = 0
    max_ore_rob = max(cost[1],cost[2],cost[4])
    max_clay_rob = cost[3]
    max_obs_rob = cost[5]
    
    dfs(State(0,0,0,0,1,0,0,0))

    total += (i + 1) * Max_geode
    
print(total)
    
    

