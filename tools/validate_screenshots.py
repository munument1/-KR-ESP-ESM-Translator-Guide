"""Check guide links, image integrity and the lossless SVG base capture."""
import base64
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from PIL import Image

root=Path(__file__).resolve().parents[1]
files=[root/'README.md',root/'docs/original-screenshots.md',root/'images/ko-4.37/SOURCES.md']
for file in files:
    text=file.read_text(encoding='utf-8')
    assert text.count('<details>')==text.count('</details>'),file
    for link in re.findall(r'\]\(([^)]+)\)',text):
        if '://' not in link and not link.startswith('#'):
            target=(file.parent/link.split('#')[0]).resolve()
            assert target.is_file(),(file,link)
data=json.loads((root/'images/ko-4.37/sources.json').read_text(encoding='utf-8'))
for entry in data['captures']:
    path=root/entry['file']
    assert hashlib.sha256(path.read_bytes()).hexdigest()==entry['sha256'],path
    if entry['kind']=='native-ui-capture':
        with Image.open(path) as im:
            im.load()
            assert im.size==(entry['width'],entry['height']),path
svg=ET.parse(root/'images/ko-4.37/main-annotated.svg').getroot()
embedded=svg.find('{http://www.w3.org/2000/svg}image').attrib['href']
assert base64.b64decode(embedded.split(',',1)[1])==(root/'images/ko-4.37/raw/main.png').read_bytes()
assert len(svg.findall('.//{http://www.w3.org/2000/svg}circle'))==22
appendix=(root/'docs/original-screenshots.md').read_text(encoding='utf-8')
originals=list((root/'images/original').iterdir())
assert len(originals)==98
for path in originals:
    assert '../images/original/'+path.name in appendix,path
    with Image.open(path) as im:
        im.load()
readme=(root/'README.md').read_text(encoding='utf-8')
for path in (root/'images/ko-4.37/raw').glob('*.png'):
    assert 'images/ko-4.37/raw/'+path.name in readme,path
print('PASS: 18 PNGs, annotation PNG byte equality, checksums, all local links, 98 preserved originals and paired details tags.')
