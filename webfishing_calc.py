#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Tuple, Set, Callable
import json
import os
import sys

def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")

def spacer() -> None:
    print()

class WaterType(str, Enum):
    SALTWATER = "Saltwater"
    FRESHWATER = "Freshwater"
    MISC = "Misc"

DEFAULT_RARITY_ORDER: List[str] = [
    "Normal", "Shining", "Glistening", "Opulent", "Radiant", "Alpha"
]


@dataclass(frozen=True)
class Bait:
    name: str
    rarity_chances: Tuple[float, float, float, float, float, float]
    allowed_tiers: Optional[Set[int]] = None

    def chance_for_index(self, idx: int) -> float:
        return float(self.rarity_chances[idx])

    def can_catch_tier(self, tier: int) -> bool:
        return self.allowed_tiers is None or tier in self.allowed_tiers


@dataclass(frozen=True)
class Fish:
    name: str
    water: WaterType
    tier: int
    best_lure: str
    default_lure_chance: float
    best_lure_chance: float
    note: str

def clamp_pct(p: float) -> float:
    return max(0.0, min(100.0, float(p)))

def fmt_pct(p: float) -> str:
    p = clamp_pct(p)
    return f"{int(p)}%" if p.is_integer() else f"{p:.2f}%"

def combined_percent(fish_percent: float, rarity_percent: float) -> float:
    return clamp_pct(fish_percent) * clamp_pct(rarity_percent) / 100.0


def _norm(s: str) -> str:
    return " ".join(s.strip().lower().split())

def _find_by_text_choice(
    options: List[str],
    user_text: str,
) -> Optional[int]:

    q = _norm(user_text)
    if not q:
        return None

    normalized = [_norm(o) for o in options]

    # Exact match
    for i, n in enumerate(normalized):
        if n == q:
            return i

    # Unique prefix match
    hits = [i for i, n in enumerate(normalized) if n.startswith(q)]
    if len(hits) == 1:
        return hits[0]

    return None


def ask_choice(options: List[str], prompt: str) -> int:
    while True:
        spacer()
        for i, opt in enumerate(options):
            print(f"[{i}] {opt}")
        spacer()

        raw = input(prompt).strip()
        if not raw:
            clear_screen()
            print("Invalid input. Type an option number or name.")
            continue

        # Number selection
        if raw.isdigit():
            idx = int(raw)
            if 0 <= idx < len(options):
                clear_screen()
                return idx
            print("Invalid number. Try again.")
            continue

        # Text selection
        idx = _find_by_text_choice(options, raw)
        if idx is not None:
            clear_screen()
            return idx

        clear_screen()
        print("Invalid input. Type an option number (e.g., 0) or the option name.")


def load_json(path: str) -> Dict:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Data file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def validate_and_parse(data: Dict) -> Tuple[List[str], List[Bait], List[Fish]]:
    rarities = data.get("rarities", DEFAULT_RARITY_ORDER)

    baits = [
        Bait(
            name=b["name"],
            rarity_chances=tuple(float(x) for x in b["rarity_chances"]),
            allowed_tiers=set(b["allowed_tiers"]) if "allowed_tiers" in b else None,
        )
        for b in data["baits"]
    ]

    fishes = [
        Fish(
            name=f["name"],
            water=WaterType(f["water"]),
            tier=int(f["tier"]),
            best_lure=f["best_lure"],
            default_lure_chance=float(f["default_lure_chance"]),
            best_lure_chance=float(f["best_lure_chance"]),
            note=f.get("note", ""),
        )
        for f in data["fish"]
    ]

    return rarities, baits, fishes


def fish_list_all_sorted(fishes: List[Fish]) -> List[Fish]:
    return sorted(fishes, key=lambda f: f.name.lower())


def best_bait_for_rarity_compatible(
    baits: List[Bait], rarity_index: int, fish_tier: int
) -> Optional[Bait]:
    compatible = [b for b in baits if b.can_catch_tier(fish_tier)]
    if not compatible:
        return None
    return sorted(
        compatible,
        key=lambda b: (-b.chance_for_index(rarity_index), b.name.lower())
    )[0]

def expected_baits_from_percent(chance_percent: float) -> float:
    cp = clamp_pct(chance_percent)
    if cp <= 0.0:
        return float("inf")
    return 100.0 / cp

def avg_baits(avg: float) -> str:
    if avg == float("inf"):
        return "Impossible"
    if avg < 10:
        return f"{avg:.2f}"
    if avg < 100:
        return f"{avg:.1f}"
    if avg < 1000:
        return f"{avg:.0f}"
    if avg < 10000:
        return f"{avg/1000:.1f}k"
    return f"{avg/1000:.0f}k"

def main() -> None:
    clear_screen()

    data = load_json("data.json")
    rarities, baits, fishes = validate_and_parse(data)

    print("=== Webfishing Catch Chance Calculator ===")
    print("\nAll data is taken from the webfishing Wiki, you can find it at: https://webfishing.wiki.gg/")

    bait_idx = ask_choice(
        ["Auto (chooses the best bait after rarity is picked)"] + [b.name for b in baits],
        "> "
    )
    is_auto = bait_idx == 0
    selected_bait = None if is_auto else baits[bait_idx - 1]

    fish_candidates = fish_list_all_sorted(fishes)

    # If bait is not auto enforce tier restriction at the fish menu
    if not is_auto and selected_bait is not None:
        fish_candidates = [f for f in fish_candidates if selected_bait.can_catch_tier(f.tier)]
        if not fish_candidates:
            print("\nThis bait cannot catch any fish (tier restriction).")
            return

    fish_idx = ask_choice(
        [f"{f.name} (Tier {f.tier})" for f in fish_candidates],
        "> "
    )
    fish = fish_candidates[fish_idx]

    while True:
        rarity_idx = ask_choice(rarities, "Select rarity: ")
        rarity_name = rarities[rarity_idx]

        used_bait = (
            best_bait_for_rarity_compatible(baits, rarity_idx, fish.tier)
            if is_auto else selected_bait
        )

        if used_bait is None:
            print("\nNo compatible bait exists for this fish tier (check allowed_tiers in data.json).")
            return

        if used_bait.chance_for_index(rarity_idx) == 0:
            print("\nIt is impossible to catch this rarity with this bait.")
            choice = ask_choice(
                ["Change bait", "Choose a different rarity"],
                "> "
            )
            if choice == 0:
                return main()
            continue

        break

    rarity_pct = used_bait.chance_for_index(rarity_idx)

    chance_default = combined_percent(fish.default_lure_chance, rarity_pct)
    chance_best = combined_percent(fish.best_lure_chance, rarity_pct)

    avg_default = expected_baits_from_percent(chance_default)
    avg_best = expected_baits_from_percent(chance_best)

    print("\n=== Result ===")
    print(f"\nFish: {fish.name}")
    print(f"Rarity: {rarity_name}")
    print(f"Water: {fish.water.value}")
    if is_auto:
        print(f"Best bait (Auto): {used_bait.name}")
    else:
        print(f"Bait: {used_bait.name}")
    print(f"Best lure: {fish.best_lure}")
    print(
        f"{rarity_name} w/ Bare Hook: "
        f"{fmt_pct(combined_percent(fish.default_lure_chance, rarity_pct))}"
    )
    print(
        f"{rarity_name} w/ {fish.best_lure}: "
        f"{fmt_pct(combined_percent(fish.best_lure_chance, rarity_pct))}"
    )
    print(f"Avg. baits needed w/ Bare Hook: {avg_baits(avg_default)}")
    print(f"Avg. baits needed w/ {fish.best_lure}: {avg_baits(avg_best)}")
    if fish.note:
        print(f"Note: {fish.note}")
    print("\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
