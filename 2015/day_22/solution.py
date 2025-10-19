import sys
from copy import deepcopy

sys.setrecursionlimit(100000000)

BOSS_DAMAGE = 10
options = ['magic missile', 'drain', 'shield', 'poison', 'recharge']


class Game:
    def __init__(self, player_actions=None):
        self.boss_hp = 71
        self.effects = []
        self.total_mana_used = 0
        self.player = {"hp": 50, "mana": 500, "armor": 0}
        self.player_actions = player_actions or []

    def perform_effects(self):
        i = len(self.effects) - 1
        while i >= 0:
            self.handle_effect(self.effects[i])
            if self.effects[i]['turns_remaining'] == 0:
                if self.effects[i]['type'] == 'armor':
                    self.player['armor'] = 0
                self.effects.pop(i)
            i -= 1

    def handle_effect(self, effect):
        if effect['type'] == "damage":
            self.boss_hp -= effect['boost']
        elif effect['type'] == "mana":
            self.player['mana'] += effect['boost']
        elif effect['type'] == "armor":
            self.player['armor'] = effect['boost']
        effect['turns_remaining'] -= 1

    def player_move(self, type):
        if type == "magic missile":
            self.player['mana'] -= 53
            self.total_mana_used += 53
            self.boss_hp -= 4
        elif type == "drain":
            self.player['mana'] -= 73
            self.total_mana_used += 73
            self.boss_hp -= 2
            self.player['hp'] += 2
        elif type == "shield":
            self.player['mana'] -= 113
            self.total_mana_used += 113
            self.effects.append({
                "type": "armor",
                "boost": 7,
                "turns_remaining": 6
            })
        elif type == "poison":
            self.player['mana'] -= 173
            self.total_mana_used += 173
            self.effects.append({
                "type": "damage",
                "boost": 3,
                "turns_remaining": 6
            })
        elif type == "recharge":
            self.player['mana'] -= 229
            self.total_mana_used += 229
            self.effects.append({
                "type": "mana",
                "boost": 101,
                "turns_remaining": 5
            })

    def is_game_over(self):
        return self.boss_hp <= 0 or self.player['hp'] <= 0 or self.player['mana'] <= 0

    def dfs(self, best=float('inf')):
        if self.is_game_over():
            if self.boss_hp <= 0:
                return self.total_mana_used
            return float('inf')

        if self.total_mana_used >= best:
            return float('inf')

        for spell in options:
            cost = {"magic missile": 53, "drain": 73, "shield": 113,
                    "poison": 173, "recharge": 229}[spell]
            if self.player['mana'] < cost:
                continue
            if spell == "shield" and any(e['type'] == "armor" for e in self.effects):
                continue
            if spell == "poison" and any(e['type'] == "damage" for e in self.effects):
                continue
            if spell == "recharge" and any(e['type'] == "mana" for e in self.effects):
                continue

            g = deepcopy(self)

            # Player turn
            g.perform_effects()
            if g.boss_hp <= 0:
                best = min(best, g.total_mana_used)
                continue

            g.player_move(spell)
            if g.is_game_over():
                if g.boss_hp <= 0:
                    best = min(best, g.total_mana_used)
                continue

            # Boss turn
            g.perform_effects()
            if g.boss_hp <= 0:
                best = min(best, g.total_mana_used)
                continue

            g.player['hp'] -= max((BOSS_DAMAGE - g.player['armor']), 1)
            if g.is_game_over():
                if g.boss_hp <= 0:
                    best = min(best, g.total_mana_used)
                continue

            best = min(best, g.dfs(best))

        return best


if __name__ == "__main__":
    game = Game()
    result = game.dfs()
    print("Minimum mana to win:", result)
