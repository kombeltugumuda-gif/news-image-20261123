# The World Today — Monday, 23 November 2026

[![news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/kombeltugumuda-gif/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/kombeltugumuda-gif/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123)

One image summing up the world's news of Monday 23 November 2026, as a
newspaper front page. Entry for the
[news-image-20261123 bounty on make.fun](https://make.fun/bounty/news-image-20261123).

## The day's stories

- **Lead — Ukraine sinks Russian warship off Libya.** Ukrainian sea drones
  sank the Russian corvette *Merkury* off Benghazi and hit the cargo ship
  *Angara*; President Zelenskyy confirmed the strike.
- **Ukraine — Russian strikes kill at least 15 near Kyiv.** A drone strike
  wrecked a block of flats in Dymer; rescuers pulled a boy, 7, and a woman,
  79, alive from the rubble.
- **Climate — COP31 ends with no climate deal.** The UN talks in Turkey
  closed without agreement on fossil fuels or finance — the longest climate
  summit in history.
- **Europe — NATO meets as Russian missiles enter Poland.** Poland called
  emergency talks after three objects crossed its airspace.
- **Middle East — Trump rejects Iran's deal as Bahrain is hit.** Trump said
  Iran wants a deal but not one "acceptable" to him.
- **Gaza —** Israeli strike on a truck kills three; Israel's PM-elect calls
  West Bank settler arson "Jewish terrorism".
- **Also today:** Indonesia factory fire kills 24; Democrats win 258 House
  seats; Trump signs the law retiring the penny; a Delta outage delays
  1,600 flights.

Sources: Reuters, The Guardian, NBC News, Just Security (Early Edition,
23 November 2026).

## How the image was made

`build_frontpage.py` draws the 1024×1024 front page with PIL using real
fonts (Liberation Serif / DejaVu Sans), so every headline is legible and
nothing is garbled. The hero photograph panel is an AI-generated
illustration of the lead story (labelled "Illustration" in the caption);
all text on the page is rendered by the script, not by the image model.
`main.ts` (Node 22, standard library only) copies the finished
`entry.png` to `/output/entry.png` — no network, deterministic output.

## License

MIT — see `LICENSE`.
