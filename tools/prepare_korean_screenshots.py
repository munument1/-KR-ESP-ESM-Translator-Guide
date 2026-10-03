"""Build the guide's vector annotations and capture inventory; never alter PNGs."""
import base64
import hashlib
import json
import re
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'images/ko-4.37'
raw = DEST / 'raw'
labels = ['제목 표시줄', '메뉴', '도구 모음', '탭 표시줄', 'GRUP/그룹 창', '게임 정보', '문자열 표', '상태 버튼', '작업 영역', '추가 정보', '상태 표시']
# (marker x/y, arrow target x/y), in the untouched 1024x768 capture.
points = [(690,21,580,16),(490,45,399,45),(697,80,615,78),(275,113,198,113),(153,490,100,320),(144,620,90,636),(870,384,820,350),(980,480,970,429),(546,527,590,497),(839,688,705,661),(664,746,735,752)]
payload = base64.b64encode((raw / 'main.png').read_bytes()).decode()
svg = ['<svg xmlns="http://www.w3.org/2000/svg" width="1364" height="768" viewBox="0 0 1364 768" role="img" aria-labelledby="title desc">', '<title id="title">EET 4.37 한국어 메인 창의 11개 영역</title>', '<desc id="desc">실제 캡처 PNG를 수정 없이 포함하고 번호와 화살표를 SVG 레이어로 겹친 설명도.</desc>', '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#d82020"/></marker></defs>', '<rect width="1364" height="768" fill="white"/>', f'<image x="0" y="0" width="1024" height="768" href="data:image/png;base64,{payload}"/>', '<g font-family="Segoe UI, Malgun Gothic, sans-serif">', '<rect x="1040" y="14" width="310" height="58" rx="10" fill="#17478b"/>', '<text x="1195" y="50" text-anchor="middle" font-size="25" font-weight="bold" fill="white">EET 4.37 화면 구성</text>']
for i, ((x,y,tx,ty), label) in enumerate(zip(points,labels), 1):
    svg += [f'<path d="M{x},{y} L{tx},{ty}" stroke="white" stroke-width="7"/>', f'<path d="M{x},{y} L{tx},{ty}" stroke="#d82020" stroke-width="3" marker-end="url(#arrow)"/>', f'<circle cx="{x}" cy="{y}" r="17" fill="#d82020" stroke="white" stroke-width="2"/>', f'<text x="{x}" y="{y+6}" text-anchor="middle" font-size="18" font-weight="bold" fill="white">{i}</text>']
    ly=107+(i-1)*51
    svg += [f'<rect x="1045" y="{ly-21}" width="300" height="42" rx="9" fill="#edf4fb"/>', f'<circle cx="1068" cy="{ly}" r="17" fill="#d82020"/>', f'<text x="1068" y="{ly+6}" text-anchor="middle" font-size="18" font-weight="bold" fill="white">{i}</text>', f'<text x="1098" y="{ly+7}" font-size="22" fill="#14223c">{label}</text>']
svg += ['<text x="1048" y="718" font-size="17" fill="#24344c">한국어 UI · 영→불 DB 예시</text>', '<text x="1048" y="746" font-size="15" fill="#24344c">번호는 본문 2.1 설명과 대응</text>', '</g></svg>']
(DEST/'main-annotated.svg').write_text('\n'.join(svg),encoding='utf-8')
entries=[]
for path in sorted(raw.glob('*.png')):
    with Image.open(path) as im:
        im.load()
        w,h=im.size
    entries.append({'file':path.relative_to(ROOT).as_posix(),'width':w,'height':h,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'kind':'native-ui-capture'})
entries.append({'file':'images/ko-4.37/main-annotated.svg','kind':'vector-annotation','base_capture':'images/ko-4.37/raw/main.png','sha256':hashlib.sha256((DEST/'main-annotated.svg').read_bytes()).hexdigest(),'embedded_png_sha256':hashlib.sha256(base64.b64decode(payload)).hexdigest()})
(DEST/'sources.json').write_text(json.dumps({'captured_on':'2026-10-03','application':'ESP/ESM Translator 4.37 (Epervier 666)','ui_language':'Korean','sample_plugin':'Knights - Unofficial Patch.esp','sample_source':'Unofficial Oblivion DLC Patches (user-provided local installation; copied to temporary working directory)','translation_database':'BDD_Oblivion_EN-FR.eet (English to French demonstration, not Korean translation results)','captures':entries},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'Indexed {len(entries)-1} PNG captures and one SVG annotation.')
