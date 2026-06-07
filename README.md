# AI Roblox Game Maker

Describe a Roblox game in plain English and this tool generates a full Lua game scaffold (server + client scripts + setup guide) using AI. Perfect for a YouTube series like **"I Made a Roblox Game with AI in 10 Minutes"**.

## What it does

1. You type an idea: `"a lava obby where the floor disappears"`
2. The AI returns a structured game (name, summary, scripts, setup steps).
3. The tool writes each Luau script to disk in a Rojo-friendly folder layout.
4. You sync the folder into Roblox Studio and playtest.

## Quick start

```bash
pip install -r requirements.txt
cp .env.example .env   # then add your OPENAI_API_KEY
python generate.py "a clicker simulator with a coin shop" --out MyGame
```

Open `MyGame/` and sync it into Studio with [Rojo](https://rojo.space).

## Example prompts (great for videos)

- "a lava obby where the floor disappears behind you"
- "a pet simulator where you hatch eggs and sell pets for coins"
- "a tycoon where you buy droppers to earn cash"
- "a tower defense game with 3 enemy waves"

## Video ideas

- "Create AI Roblox Games" walkthrough
- "I let AI build my Roblox game in 1 prompt"
- "Turning a viewer's idea into a real Roblox game with AI"

## How this makes money

- Sell finished AI-generated games (gamepasses, dev products).
- Offer it as a Fiverr service: "I will build your Roblox game idea with AI".
- Drive YouTube traffic to the Discord community, then upsell services.

Part of the Rivvak income hub.
