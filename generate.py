"""
ai-roblox-game-maker
Describe a Roblox game in plain English and generate a full Lua game scaffold.

Usage:
    python generate.py "a lava obby where the floor disappears"
    python generate.py "a clicker simulator with a coin shop" --out MyGame

Needs OPENAI_API_KEY in your environment (or a .env file).
"""
import os
import sys
import json
import argparse
from pathlib import Path

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """You are a senior Roblox engineer. Given a game idea, output STRICT JSON only.
Schema:
{
  "game_name": str,
  "summary": str,
  "scripts": [
    {"path": "ServerScriptService/Name.server.lua", "code": "<full luau code>"},
    {"path": "StarterPlayer/StarterPlayerScripts/Name.client.lua", "code": "<full luau code>"}
  ],
  "setup_steps": [str]
}
Write complete, runnable Luau. No markdown, no backticks, JSON only."""


def generate(idea: str) -> dict:
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": idea},
        ],
    )
    return json.loads(resp.choices[0].message.content)


def write_game(game: dict, out_dir: str) -> None:
    root = Path(out_dir)
    for script in game["scripts"]:
        target = root / script["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(script["code"], encoding="utf-8")
        print(f"  wrote {target}")
    (root / "README.md").write_text(
        f"# {game['game_name']}\n\n{game['summary']}\n\n## Setup\n"
        + "\n".join(f"{i+1}. {s}" for i, s in enumerate(game["setup_steps"])),
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="AI Roblox game generator")
    parser.add_argument("idea", help="plain-English description of the game")
    parser.add_argument("--out", default="GeneratedGame", help="output folder")
    args = parser.parse_args()

    print(f"Generating game from idea: {args.idea!r}")
    game = generate(args.idea)
    print(f"-> {game['game_name']}")
    write_game(game, args.out)
    print(f"Done. Open '{args.out}' and sync into Studio with Rojo.")


if __name__ == "__main__":
    main()
