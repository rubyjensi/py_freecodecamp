# Game Ammo Magazine Reloader (While inside For)
for player_id in range(1, 3): 
    print(f"--- Player {player_id}'s Turn ---")
    bullets_loaded = 0 
    while bullets_loaded < 3:
        bullets_loaded += 1  
        print(f"Click! Bullet {bullets_loaded} slotted into chamber.")
    print("Weapon Ready! Gun Cocked.\n")