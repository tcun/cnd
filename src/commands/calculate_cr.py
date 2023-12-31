# calculate_cr.py

def xp_to_cr(xp):
    cr_to_xp = {
        0: 10,
        0.125: 25,
        0.25: 50,
        0.5: 100,
        1: 200,
        2: 450,
        3: 700,
        4: 1100,
        5: 1800,
        6: 2300,
        7: 2900,
        8: 3900,
        9: 5000,
        10: 5900,
        11: 7200,
        12: 8400,
        13: 10000,
        14: 11500,
        15: 13000,
        16: 15000,
        17: 18000,
        18: 20000,
        19: 22000,
        20: 25000,
        21: 33000,
        22: 41000,
        23: 50000,
        24: 62000,
        25: 75000,
        26: 90000,
        27: 105000,
        28: 120000,
        29: 135000,
        30: 155000
    }
    
    # Find the nearest XP threshold without going over
    cr_values = sorted(list(cr_to_xp.keys()))
    for i in range(len(cr_values) - 1, -1, -1):
        if xp >= cr_to_xp[cr_values[i]]:
            return cr_values[i]
    return 0

def calculate_party_cr(num_of_players, avg_level):
    xp_thresholds = {
        1: (25, 50, 75, 100),
        2: (50, 100, 150, 200),
        3: (75, 150, 225, 400),
        4: (125, 250, 375, 500),
        5: (250, 500, 750, 1100),
        6: (300, 600, 900, 1400),
        7: (350, 750, 1100, 1700),
        8: (450, 900, 1400, 2100),
        9: (550, 1100, 1600, 2400),
        10: (600, 1200, 1900, 2800),
        11: (800, 1600, 2400, 3600),
        12: (1000, 2000, 3000, 4500),
        13: (1100, 2200, 3400, 5100),
        14: (1250, 2500, 3800, 5700),
        15: (1400, 2800, 4300, 6400),
        16: (1600, 3200, 4800, 7200),
        17: (2000, 3900, 5900, 8800),
        18: (2100, 4200, 6300, 9500),
        19: (2400, 4900, 7300, 10900),
        20: (2800, 5700, 8500, 12700)
    }

    encounter_multipliers = {
        1: 1,
        2: 1.5,
        3: 2,
        6: 2.5,
        10: 3,
        14: 4,
        15: 5  # Assuming 15+ all have a multiplier of 5
    }

    # Determine individual XP thresholds
    individual_threshold = xp_thresholds[avg_level]

    # Determine Party's XP Threshold
    party_thresholds = [x * num_of_players for x in individual_threshold]

    # Encounter multipliers based on party size
    if num_of_players < 3:
        party_multiplier = 1.5
    elif num_of_players > 5:
        party_multiplier = 0.5
    else:
        party_multiplier = 1

    # Adjust party thresholds based on the multiplier
    adjusted_party_thresholds = [x * party_multiplier for x in party_thresholds]


    easy = adjusted_party_thresholds[0]
    medium = adjusted_party_thresholds[1]
    hard = adjusted_party_thresholds[2]
    deadly = adjusted_party_thresholds[3]

    total_easy = easy 
    total_medium = medium 
    total_hard = hard 
    total_deadly = deadly 
    
    return {
        "Easy": xp_to_cr(total_easy),
        "Medium": xp_to_cr(total_medium),
        "Hard": xp_to_cr(total_hard),
        "Deadly": xp_to_cr(total_deadly)
    }


