# solution.py
from heapq import heappush, heappop

BOSS_START = 71
BOSS_DAMAGE = 10
HARD_MODE = True  # <- toggle this to False for part 1

SPELLS = {
    "magic missile": {"cost": 53},
    "drain": {"cost": 73},
    "shield": {"cost": 113, "timer": 6},
    "poison": {"cost": 173, "timer": 6},
    "recharge": {"cost": 229, "timer": 5},
}


def apply_effects(boss_hp, player_hp, mana, armor, effects):
    """Apply all active effects once."""
    armor = 0
    new_effects = dict(effects)
    for name, turns in list(effects.items()):
        if name == "poison":
            boss_hp -= 3
        elif name == "recharge":
            mana += 101
        elif name == "shield":
            armor = 7
        new_effects[name] -= 1
        if new_effects[name] == 0:
            del new_effects[name]
    return boss_hp, player_hp, mana, armor, new_effects


def solve():
    start = (BOSS_START, 50, 500, 0, {}, 0)
    pq = []
    heappush(pq, (0, start))
    seen = {}

    while pq:
        mana_spent, state = heappop(pq)
        boss_hp, player_hp, mana, _, effects, _ = state

        # Hard mode: player loses 1 HP at start of their turn
        if HARD_MODE:
            player_hp -= 1
            if player_hp <= 0:
                continue  # dead immediately

        # Start of player's turn: apply effects
        boss_hp, player_hp, mana, armor, effects = apply_effects(
            boss_hp, player_hp, mana, 0, effects)
        if boss_hp <= 0:
            return mana_spent

        # Try each spell
        for spell, spec in SPELLS.items():
            cost = spec["cost"]
            if mana < cost:
                continue
            if spell in effects and spell in ("shield", "poison", "recharge"):
                continue

            nboss, nplayer, nman = boss_hp, player_hp, mana - cost
            neffects = dict(effects)
            nspent = mana_spent + cost

            # Cast spell
            if spell == "magic missile":
                nboss -= 4
            elif spell == "drain":
                nboss -= 2
                nplayer += 2
            elif spell == "shield":
                neffects["shield"] = SPELLS["shield"]["timer"]
            elif spell == "poison":
                neffects["poison"] = SPELLS["poison"]["timer"]
            elif spell == "recharge":
                neffects["recharge"] = SPELLS["recharge"]["timer"]

            if nboss <= 0:
                return nspent

            # Boss turn: apply effects again
            nboss, nplayer, nman, narmor, neffects = apply_effects(
                nboss, nplayer, nman, 0, neffects)
            if nboss <= 0:
                return nspent

            # Boss attacks
            nplayer -= max(1, BOSS_DAMAGE - narmor)
            if nplayer <= 0:
                continue

            # State compression & pruning
            key = (nboss, nplayer, nman, tuple(sorted(neffects.items())))
            prev = seen.get(key)
            if prev is not None and prev <= nspent:
                continue
            seen[key] = nspent

            heappush(pq, (nspent, (nboss, nplayer, nman, narmor, neffects, nspent)))

    return float("inf")


if __name__ == "__main__":
    ans = solve()
    print("Minimum mana to win:", ans)
