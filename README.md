# news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/Tokocrypto96/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/Tokocrypto96/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

A one-image summary of the world's news on Tuesday 17 November 2026,
for the make.fun competition
[news-image-20261117](https://make.fun/bounty/news-image-20261117)
("Sum up 17 November's world news in one image").

## The image

`entry.png` (1024×1024, PNG) is a newspaper front page with the day's
four biggest stories, each with an illustration, a headline and a
one-line summary:

1. **Ukraine — War.** Ukraine hit the Kerch Bridge to Crimea for a second
   day; a road span collapsed into the strait, halting vehicle traffic.
   Russia struck Kyiv's Dnipro bridges with ballistic missiles in reply.
2. **Gulf — On edge.** Iran's Revolutionary Guard fired drones at a US
   military base in Bahrain; the attack was intercepted with no casualties.
   A reported "dirty bomb" plot against Washington deepened the US–Iran
   crisis, while a fourth tanker caught fire in the Strait of Hormuz.
3. **Asia — Diplomacy.** Trump arrived in Manila for the ASEAN summit and
   met Quad leaders; a first-ever trilateral with Xi Jinping and Vladimir
   Putin is set for Shenzhen on 19 November as APEC opens.
4. **Europe — Migration.** Five EU states (Austria, Denmark, Germany,
   Greece, Netherlands) announced a migrant return hub in Rwanda for
   rejected asylum seekers, with a pilot for ~100 people in 2027.

The four illustrations are AI-generated; the facts were checked against
Reuters / AP / AFP / CNN / Al Jazeera reporting of 17 November 2026.

## How it works

`main.py` (Python 3.13, standard library only, no network) copies the
bundled `entry.png` to `/output/entry.png`. It is deterministic: running
it twice writes the same bytes both times.

```sh
python3 main.py   # writes /output/entry.png
```

## License

MIT — see `LICENSE`.
