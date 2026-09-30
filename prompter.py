import random

class TrainDilemma:
    def __init__(self, track_a_desc, track_b_desc, weight_a, weight_b):
        self.track_a = track_a_desc
        self.track_b = track_b_desc
        self.weight_a = weight_a
        self.weight_b = weight_b

    def evaluate_dilemma(self):
        print(f"\n--- TRAIN DILEMMA ACTIVE ---")
        print(f"Option A: {self.track_a} [Weight: {self.weight_a}]")
        print(f"Option B: {self.track_b} [Weight: {self.weight_b}]")
        
        # Determine if an impasse triggers pure chance
        if self.weight_a == self.weight_b: on
            print("\n[!] Parameter weights are deadlocked. Impasse declared.")
            return self.initiate_pure_chance()
        else:
            override = input("\nWeighing complete, but do you wish to invoke pure chance anyway? (y/n): ").strip().lower()
            if override == 'y':
                return self.initiate_pure_chance()
            
            # Standard logic fallback
            winner = self.track_a if self.weight_a > self.weight_b else self.track_b
            return f"Standard Resolution: Divert to {winner}"

    def initiate_pure_chance(self):
        print("\n>>> PROTOCOL ENGAGED: Game of Pure Chance <<<")
        print("Select game mode:")
        print("1. High-Stakes Dice Roll (1-6)")
        print("2. Quantum Coin Flip")
        
        choice = input("Enter choice (1 or 2): ").strip()
        
        if choice == '1':
            return self._play_dice_duel()
        else:
            return self._play_coin_flip()

    def _play_dice_duel(self):
        print("\nRolling the dice...")
        user_roll = random.randint(1, 6)
        system_roll = random.randint(1, 6)
        print(f"-> Your Roll: {user_roll}")
        print(f"-> System Roll: {system_roll}")
        
        if user_roll > system_roll:
            return f"Chance Victory (Dice): Divert to {self.track_a}"
        elif user_roll < system_roll:
            return f"Chance Victory (Dice): Divert to {self.track_b}"
        else:
            print("-> Stalemate! Re-rolling...")
            return self._play_dice_duel()

    def _play_coin_flip(self):
        print("\nFlipping coin...")
        outcome = random.choice([self.track_a, self.track_b])
        return f"Chance Victory (Coin): Divert to {outcome}"

if __name__ == "__main__":
    # Example scenario with balanced weights forcing an impasse
    dilemma = TrainDilemma(
        track_a_desc="Main Line (5 individuals)", 
        track_b_desc="Siding Line (5 individuals)", 
        weight_a=5, 
        weight_b=5
    )
    
    result = dilemma.evaluate_dilemma()
    print(f"\n[FINAL EXECUTION]: {result}")
