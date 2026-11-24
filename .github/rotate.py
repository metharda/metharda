"""Swap the README banner to the painting of the day."""
import datetime
import pathlib
import re

START = datetime.date(2026, 11, 24)  # ART[0] is shown on this day, then one step per day

ART = [
    ("creation-of-adam", "The Creation of Adam", "Michelangelo, c. 1512"),
    ("ideal-city-urbino", "The Ideal City", "Urbino school, c. 1480"),
    ("delivery-of-the-keys", "Delivery of the Keys", "Perugino, 1482"),
    ("hunters-in-the-snow", "Hunters in the Snow", "Pieter Bruegel the Elder, 1565"),
    ("architectural-veduta", "Architectural Veduta", "attr. Francesco di Giorgio Martini, c. 1490"),
    ("school-of-athens", "The School of Athens", "Raphael, 1511"),
    ("last-supper", "The Last Supper", "Leonardo da Vinci, c. 1498"),
    ("birth-of-venus", "The Birth of Venus", "Sandro Botticelli, c. 1485"),
    ("ideal-city-baltimore", "The Ideal City", "Fra Carnevale, c. 1480"),
    ("flagellation", "The Flagellation of Christ", "Piero della Francesca, c. 1460"),
    ("primavera", "Primavera", "Sandro Botticelli, c. 1480"),
    ("tribute-money", "The Tribute Money", "Masaccio, c. 1425"),
    ("census-at-bethlehem", "The Census at Bethlehem", "Pieter Bruegel the Elder, 1566"),
    ("tower-of-babel", "The Tower of Babel", "Pieter Bruegel the Elder, 1563"),
]

slug, title, by = ART[(datetime.date.today() - START).days % len(ART)]
block = f"""<!-- art:start -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="art/{slug}-dark.png">
  <img alt="{title} by {by}, as ASCII art" src="art/{slug}-light.png">
</picture>
<sub><i>{title}, {by}</i></sub>
<!-- art:end -->"""

readme = pathlib.Path(__file__).resolve().parent.parent / "README.md"
text, n = re.subn(r"<!-- art:start -->.*?<!-- art:end -->", block, readme.read_text(), flags=re.S)
if n != 1:
    raise SystemExit("README needs exactly one <!-- art:start --> ... <!-- art:end --> block")
readme.write_text(text)
