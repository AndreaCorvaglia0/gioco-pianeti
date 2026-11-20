# Gioco dei pianeti

A tiny story-game about the solar system for a four-year-old who cannot read yet.
An astronaut leaves Earth, visits Mercury and the Sun, then flies out to Jupiter and Saturn and comes home.
Cut-paper look, one gesture per page, a warm narrator in Italian.

**Play:** https://andreacorvaglia0.github.io/gioco-pianeti/ (phone, held sideways)

## How to play

- On a planet: touch where you want the astronaut to go. When the page is done the rocket pulses: touch it.
- In flight: the rocket follows your finger. The round fire button is an optional turbo.
- Nothing can go wrong. Arrive too fast and the rocket overshoots, turns round and comes back.

## What is in here

| Path | What |
|---|---|
| `index.html` | The whole game: one file, plain canvas, no build step |
| `audio/` | The narrator's lines, one mp3 per line |
| `narration/lines.json` | The script: line id and text. The game shows the text as a caption and plays `audio/<id>.mp3` if it exists |
| `tools/playthrough.py` | Plays the whole story in a headless browser and takes screenshots |
| `docs/PROGETTO.md` | Design notes and decisions (Italian) |

## Real data, declared licences

Planet sizes, distances, the apparent size of the Sun, Saturn's rings and the moons use real ratios.
Every compression we apply (so that the game is not mostly empty space) is a constant at the top of `index.html`.

## Credits

- Idea and direction: Andrea Corvaglia. Built with Claude.
- Narrator voice generated with [ElevenLabs](https://elevenlabs.io) (voice "Antonio Farina"), free plan: non-commercial use.
- Music and sound effects are synthesised by the game itself.
- Font: Baloo 2, from Google Fonts (SIL Open Font License).
