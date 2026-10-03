# EET 4.37 한국어 화면 촬영 기록

2026-10-03에 사용자가 제공한 EET 4.37 설치본(`eet___esp_esm_translator_4.37/EET4.exe`)을 직접 실행해 촬영했습니다. UI 언어는 한국어이며, 예제는 사용자가 제공한 **Unofficial Oblivion DLC Patches**의 `Knights - Unofficial Patch.esp`입니다. 플러그인을 임시 작업 폴더로 복사해 열었습니다. 저장소에는 플러그인 파일을 포함하지 않습니다.

화면의 프랑스어 번역문은 설치본의 `BDD_Oblivion_EN-FR.eet` 예시입니다. 한국어 번역 결과나 패치 배포물이 아닙니다. 기본 DB 선택 목록에는 다른 게임 DB가 표시될 수 있으므로 제목 표시줄의 현재 탭 DB도 확인하세요. 인코딩과 옵션 체크 상태는 촬영 세션의 상태를 보여주며, 모든 게임·플러그인에 권장하는 설정이 아닙니다. 특히 일반 옵션의 백업 수 0은 권장값이 아닙니다.

`raw/`의 PNG 18개는 UI에서 얻은 캡처를 그대로 보관합니다. 메뉴 PNG는 EET가 표시한 팝업 영역 캡처입니다. [main-annotated.svg](main-annotated.svg)는 [메인 원본](raw/main.png)의 PNG 바이트를 그대로 내장하고, SVG 레이어로 번호·화살표·한국어 범례를 겹친 설명도입니다. AI가 다시 그린 UI 이미지는 사용하지 않습니다. 본문 2.1의 1~11번 설명과 대응합니다.

| 화면 | 실제 캡처 |
|---|---|
| 메인 창 | [main.png](raw/main.png) |
| 인코딩 선택 | [encoding.png](raw/encoding.png) |
| 파일 메뉴 | [menu-file.png](raw/menu-file.png) |
| 편집 메뉴·단축키 | [menu-edit.png](raw/menu-edit.png) |
| 번역 메뉴 | [menu-translation.png](raw/menu-translation.png) |
| 데이터베이스 메뉴 | [menu-database.png](raw/menu-database.png) |
| 찾기 및 바꾸기 | [find-replace.png](raw/find-replace.png) |
| 게임 DB 검색 | [database-search.png](raw/database-search.png) |
| 현재 모드 검색(F4) | [current-mod-search.png](raw/current-mod-search.png) |
| 부분 저장(창 확인만 수행) | [partial-save.png](raw/partial-save.png) |
| 일반 옵션 상단 | [options-general.png](raw/options-general.png) |
| 일반 옵션 작업 기록·자동 저장 | [options-save.png](raw/options-save.png) |
| 데이터베이스 옵션 상단 | [options-database.png](raw/options-database.png) |
| 스크립트·MCM·VMAD 옵션 | [options-scripts-vmad.png](raw/options-scripts-vmad.png) |
| GRUP/FIELD 정의 | [options-grup.png](raw/options-grup.png) |
| 기타 옵션 상단 | [options-other.png](raw/options-other.png) |
| 금지 문자 검사 | [options-checks.png](raw/options-checks.png) |
| 인터페이스·글꼴·단축키 | [options-interface.png](raw/options-interface.png) |

파일 크기·SHA-256·이미지 치수는 [sources.json](sources.json)에 기록되어 있습니다. `python tools/prepare_korean_screenshots.py`로 SVG와 기록을 재생성할 수 있습니다(Pillow 필요). 원문의 프랑스어 화면은 [별도 보관본](../../docs/original-screenshots.md)으로 유지합니다.
