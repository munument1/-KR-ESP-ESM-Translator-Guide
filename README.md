# ESP-ESM Translator (EET) 한국어 가이드

ESP-ESM Translator(EET)를 이용해 Bethesda 계열 게임의 ESP/ESM/ESL 플러그인과 관련 문자열을 번역할 때 참고할 수 있도록 정리한 한국어 가이드입니다.

> [!NOTE]
> 이 문서는 프랑스어 커뮤니티 **La Confrérie des Traducteurs**의 Yoplala가 작성한 EET 튜토리얼을 바탕으로 한국어 사용 환경에 맞게 번역·정리한 문서입니다.  
> 원문: https://www.confrerie-des-traducteurs.fr/forum/viewtopic.php?f=372&t=29457  
> 원문 최초 게시: 2019-03-05  
> 프로그램과 메뉴 구성은 버전에 따라 달라질 수 있습니다.

> 스크린샷은 원문에 실린 **프랑스어 UI**를 그대로 사용합니다. 본문의 한국어 메뉴명과 대조해 위치와 기능을 확인하세요.
> 이미지는 저장소에 포함되어 있으며, 원본 이미지 주소와 파일 정보는 [스크린샷 출처 목록](images/SOURCES.md)에서 확인할 수 있습니다.

> [!IMPORTANT]
> 이 가이드에서 사용하는 메뉴명은 한국어 UI에서 이해하기 쉽도록 정리한 표현을 기준으로 합니다.  
> 예: **Validate → 확정**, **Rereading → 검수**, **Custom → 사용자 지정**, **Instant Translation → 즉시 번역**.

---

## 목차

1. [설치](#1-설치)
2. [프로그램 구성](#2-프로그램-구성)
   - [메인 창](#21-메인-창)
   - [메뉴와 단축키](#22-메뉴와-단축키)
   - [옵션](#23-옵션)
3. [기본 사용법](#3-기본-사용법)
   - [인코딩](#31-인코딩)
   - [게임 데이터베이스](#32-게임-데이터베이스)
   - [번역하지 않을 항목 먼저 정리하기](#33-번역하지-않을-항목-먼저-정리하기)
   - [검색과 필터](#34-검색과-필터)
   - [번역 저장과 불러오기](#35-번역-저장과-불러오기)
   - [기존 번역 업데이트](#36-기존-번역-업데이트)
   - [번역 마무리](#37-번역-마무리)
4. [고급 기능](#4-고급-기능)
   - [작업 환경](#41-작업-환경)
   - [주석 활용](#42-주석-활용)
   - [미리보기 기능](#43-미리보기-기능)
   - [대화문 번역](#44-대화문-번역)
   - [VMAD](#45-vmad)
   - [스크립트](#46-스크립트)
   - [여러 모드 동시 작업](#47-여러-모드-동시-작업)
   - [여러 모드 분석·비교](#48-여러-모드-분석비교)
   - [개인 데이터베이스](#49-개인-데이터베이스)
5. [검수 작업 팁](#5-검수-작업-팁)
6. [번역할 때 추가로 확인할 것](#6-번역할-때-추가로-확인할-것)
7. [프로그램 업데이트](#7-프로그램-업데이트)
8. [추가 참고 자료](#8-추가-참고-자료)

---

# 1. 설치

EET는 ESP/ESM/ESL을 비롯한 여러 모드 파일에서 번역 가능한 문자열을 추출하고, 번역 DB를 이용해 작업할 수 있는 도구입니다.

원문에서는 La Confrérie des Traducteurs에서 배포되는 EET 패키지를 기준으로 설명합니다.

![원문 배포 페이지의 EET 다운로드 버튼](images/original/Yoplala_1555505085_EET.PNG)

- EET 원문 배포 페이지:  
  https://www.confrerie-des-traducteurs.fr/skyrim/mods/utilitaires/eet___esp_esm_translator
- 압축 해제 도구는 7-Zip 등을 사용할 수 있습니다.
- 구형 배포본에서는 **Visual C++ 2010 Redistributable (x86)**가 필요하다고 안내되어 있습니다.

압축 파일을 원하는 위치에 풀고 실행 파일을 실행하면 됩니다. 모딩 도구를 모아두는 별도 폴더에 버전까지 포함해 저장해 두면 관리하기 편합니다.

예:

```text
Modding Tools/
└─ EET - ESP-ESM Translator 3.xx/
```

플러그인 파일을 EET와 연결해 `.esp`, `.esm`, `.esl` 파일을 바로 열 수도 있습니다.

<details>
<summary>원문 설치 과정 스크린샷 펼쳐보기</summary>

![원문 설치 과정 스크린샷 1](images/original/Yoplala_1555505272_EET_1.PNG)

![원문 설치 과정 스크린샷 2](images/original/Yoplala_1566419931_Yoplala_1555505283_EET_2.PNG)

</details>


---

# 2. 프로그램 구성

## 2.1 메인 창

EET에서 모드를 열면 대략 다음 영역으로 나뉩니다.

![EET 메인 창의 11개 영역: 아래 번호별 설명과 대응](images/original/Yoplala_1566755382_FenA_tre_principale_2.PNG)


1. **제목 표시줄**  
   열린 모드 또는 현재 탭 이름, EET 버전, 적용 중인 DB 등을 표시합니다.

2. **메뉴**  
   파일 열기, 편집, 번역, 데이터베이스, 표시, 검사, 도구 등의 기능이 모여 있습니다.

3. **도구 모음**  
   자주 사용하는 기능을 아이콘으로 빠르게 실행합니다.

4. **탭 표시줄**  
   여러 모드를 열었을 때 모드별 탭이 표시됩니다.

5. **GRUP/그룹 창**  
   플러그인의 레코드를 그룹 단위로 탐색합니다. 상태가 '무시'인 문자열은 작업량 집계에서 제외될 수 있습니다.

6. **게임 정보**  
   불러온 플러그인의 대상 게임을 확인하는 영역입니다.

7. **문자열 표**  
   실제 번역 작업의 중심입니다.

   일반적으로 다음과 같은 정보가 표시됩니다.

   - ID
   - EDID
   - FIELD
   - 원문
   - 번역문
   - 검수
   - 주석

   **ID / EDID / FIELD는 번역문이 아니라 레코드 구조를 식별하는 값이므로 함부로 수정하지 않는 것이 좋습니다.**

8. **상태 버튼**

   문자열을 다음 상태로 변경할 수 있습니다.

   - 확정
   - 확정 대기
   - 사용자 지정
   - 무시

9. **작업 영역**  
   선택한 문자열의 원문과 번역문을 크게 볼 수 있습니다. 검수 열을 활성화하면 검수 문자열도 함께 표시됩니다.

10. **추가 정보**  
    주석, 관련 레코드, DB 검색 결과, 변경 기록 등을 확인할 수 있습니다.

11. **상태 표시**  
    문자열 수와 상태별 분포 등을 확인할 수 있습니다.

---

## 2.2 메뉴와 단축키

### 파일


- **파일 열기**: ESP/ESM/ESL, XML 등 지원 파일 열기
- **파일 목록 열기**: 여러 파일 선택
- **아카이브 열기**: BSA, BA2, ERF 등
- **모드 번역 실행**: 번역 결과를 실제 플러그인에 반영해 출력
- **옵션**
- **언어**
- **모드 닫기**
- **열린 모드 모두 닫기**
- **종료**

<details>
<summary>프로그램 언어 설정 창 펼쳐보기</summary>

![프로그램 언어 설정 창](images/original/Yoplala_1566841668_FenA_tre_Langues.PNG)

</details>

> 번역 결과를 생성할 때는 보통 **확정된 문자열**만 최종 결과에 반영됩니다. 작업 중인 상태와 최종 출력 상태를 구분해서 사용하는 것이 좋습니다.

### 편집


| 기능 | 단축키 |
|---|---|
| 찾기 및 바꾸기 | `Ctrl + F` |
| 선택한 줄 확정 | `F10` |
| 확정 대기로 변경 | `Shift + F10` |
| 사용자 지정 상태 | `Ctrl + F10` |
| 무시 | `Ctrl + Shift + F10` |
| 즉시 번역 | `F5` |
| 게임 DB만 사용해 즉시 번역 | `Shift + F5` |
| 개인 DB만 사용해 즉시 번역 | `Ctrl + F5` |
| OnlyText DB만 사용 | `Alt + F5` |
| 외부 DB만 사용 | `Ctrl + Shift + F5` |
| 원문을 번역문에 그대로 적용 | `F8` |
| 검수 내용을 번역문에 적용 | `Shift + F8` |
| 자동 번역 적용 | `F9` |
| 웹 번역 검색 | `F12` |

<details>
<summary>찾기 및 바꾸기와 텍스트 내보내기 창 펼쳐보기</summary>

![찾기 및 바꾸기와 텍스트 내보내기 창 1](images/original/Yoplala_1566841816_FenA_tre_Recherche.PNG)

![찾기 및 바꾸기와 텍스트 내보내기 창 2](images/original/Yoplala_1566842010_FenA_tre_Exportation.PNG)

</details>

### 번역

- **번역 저장** — `Ctrl + S`
- **다른 이름으로 저장**
- **부분 저장** — `Ctrl + Shift + S`
- **번역 불러오기** — `Ctrl + L`
- **검수 열에 번역 불러오기**
- **DB와 비교**
- **개인 DB와 비교**
- **OnlyText DB와 비교**
- **여러 DB와 비교**
- **이미 번역된 모드 불러오기**
- **스크립트 창**
- **자동 번역 옵션**

<details>
<summary>자동 번역 옵션 화면 펼쳐보기</summary>

![자동 번역 옵션 화면 1](images/original/Yoplala_1566843506_Auto_1.PNG)

![자동 번역 옵션 화면 2](images/original/Yoplala_1566843523_Auto_2.PNG)

![자동 번역 옵션 화면 3](images/original/Yoplala_1566843531_Auto_3.PNG)

![자동 번역 옵션 화면 4](images/original/Yoplala_1566843541_Auto_4.PNG)

![자동 번역 옵션 화면 5](images/original/Yoplala_1566843551_Auto_5.PNG)

![자동 번역 옵션 화면 6](images/original/Yoplala_1566843563_Auto_6.PNG)

![자동 번역 옵션 화면 7](images/original/Yoplala_1566843577_Auto_7.PNG)

![자동 번역 옵션 화면 8](images/original/Yoplala_1566843587_Auto_8.PNG)

</details>

### 데이터베이스 검색

| 대상 | 단축키 |
|---|---|
| 게임 DB 검색 | `F3` |
| 개인 DB 검색 | `Shift + F3` |
| OnlyText DB 검색 | `Ctrl + F3` |
| 현재 모드 검색 | `F4` |
| 외부 DB 검색 | `Shift + F4` |
| 열린 모든 모드 검색 | `Ctrl + F4` |
| 여러 DB 검색 | `F6` |

<details>
<summary>DB 검색·선택·가져오기 화면 펼쳐보기</summary>

![DB 검색·선택·가져오기 화면 1](images/original/Yoplala_1566844671_BDD_3.PNG)

![DB 검색·선택·가져오기 화면 2](images/original/Yoplala_1566844698_BDD_4.PNG)

![DB 검색·선택·가져오기 화면 3](images/original/Yoplala_1566844714_BDD_5.PNG)

![DB 검색·선택·가져오기 화면 4](images/original/Yoplala_1566844730_BDD_6.PNG)

![DB 검색·선택·가져오기 화면 5](images/original/Yoplala_1566842626_FenA_tre_Multiple_1.PNG)

![DB 검색·선택·가져오기 화면 6](images/original/Yoplala_1566842654_FenA_tre_Multiple_2.PNG)

![DB 검색·선택·가져오기 화면 7](images/original/Yoplala_1566842678_FenA_tre_Multiple_3.PNG)

![DB 검색·선택·가져오기 화면 8](images/original/Yoplala_1566842703_FenA_tre_Sauvegardes_1.PNG)

![DB 검색·선택·가져오기 화면 9](images/original/Yoplala_1566842727_FenA_tre_Sauvegardes_2.PNG)

![DB 검색·선택·가져오기 화면 10](images/original/Yoplala_1566842745_FenA_tre_Sauvegardes_3.PNG)

![DB 검색·선택·가져오기 화면 11](images/original/Yoplala_1566846516_Importation.PNG)

![DB 검색·선택·가져오기 화면 12](images/original/Yoplala_1566846540_Importation_rapide.PNG)

![DB 검색·선택·가져오기 화면 13](images/original/Yoplala_1566846621_Dictionnaire_d_analyse.PNG)

</details>

### 표시

- 프로그램 색상/테마 변경
- 줄 색상 변경
- 줄 높이 자동 조정
- 레코드 이미지 표시
- 검수 열 표시
- 각 상태 버튼 표시/숨기기
- 상태별 정렬
- 원래 레코드 순서로 정렬
- 줄 기록 / 전체 기록
- 수정된 줄 표시
- '모든 모드' 탭 표시

<details>
<summary>테마·줄 색상·작업 기록 화면 펼쳐보기</summary>

![테마·줄 색상·작업 기록 화면 1](images/original/Yoplala_1566848160_ThA_mes.PNG)

![테마·줄 색상·작업 기록 화면 2](images/original/Yoplala_1566848183_Couleurs.PNG)

![테마·줄 색상·작업 기록 화면 3](images/original/Yoplala_1566848268_Historique.PNG)

![테마·줄 색상·작업 기록 화면 4](images/original/Yoplala_1566848308_Lises_modifs.PNG)

</details>

### 필터

상태별 색상을 이용해 작업 대상을 빠르게 좁힐 수 있습니다.

주요 의미:

- 번역하지 않을 문자열
- 미번역
- 게임 DB 원문과 일치
- DB 사용자 지정 값
- 자동 번역
- 원문 = 번역문
- 기존 번역 모드에서 가져온 문자열
- 확정 대기
- 동일 원문을 기준으로 자동 적용된 문자열
- 번역 완료 및 확정
- 사용자 지정

> 색상 자체는 테마와 설정에 따라 달라질 수 있으므로 **색깔보다 상태 이름을 기준으로 이해하는 것이 안전합니다.**

### 검사

- 맞춤법 검사
- 선택한 줄의 문법/맞춤법 검사
- 사전 설정
- 구두점 검사 및 보정
- 구두점 뒤 대문자 검사
- 지나치게 긴 줄 검색
- 금지 문자 검색
- 동일 원문인데 번역이 서로 다른 항목 검색

### 도구

- 여러 모드 간 일관성 검사
- DB 변환
- 텍스트 파일 → DB 변환
- Fallout 4 NewDialog 관련 변환
- Oblivion CS 재가져오기용 형식 내보내기
- 로컬라이즈드 모드 형식 변환

<details>
<summary>일관성 검사와 DB 변환 화면 펼쳐보기</summary>

![일관성 검사와 DB 변환 화면 1](images/original/Yoplala_1566848354_CohA_rence_des_mods.PNG)

![일관성 검사와 DB 변환 화면 2](images/original/Yoplala_1566848393_Convertir_BDD.PNG)

![일관성 검사와 DB 변환 화면 3](images/original/Yoplala_1566848425_Convertir_fichier_texte.PNG)

</details>

### 기본 선택 단축키

- 모두 선택: `Ctrl + A`
- 연속 범위 선택: `Shift + 클릭`
- 개별 추가/해제 선택: `Ctrl + 클릭`

---

## 2.3 옵션

EET는 옵션이 매우 많습니다. 처음부터 전부 변경하기보다 **필요한 기능을 이해한 뒤 수정하는 것**이 좋습니다.

### 일반 옵션


주로 다음을 설정합니다.

- 기본 DB
- 인코딩 확인
- 검수 열
- 인터넷 번역 URL
- 자동 저장
- 작업 기록
- 이전 세션의 모드 다시 열기
- 기타 확인 창

자동 저장은 최소 한 개 이상의 백업을 남기도록 설정하는 편이 안전합니다.

<details>
<summary>일반 옵션과 기본 DB 설정 펼쳐보기</summary>

![일반 옵션과 기본 DB 설정 1](images/original/Yoplala_1566765609_Options_gA_nA_rales_1.PNG)

![일반 옵션과 기본 DB 설정 2](images/original/Yoplala_1566765762_Options_BDD.PNG)

![일반 옵션과 기본 DB 설정 3](images/original/Yoplala_1566765638_Options_gA_nA_rales_2.PNG)

![일반 옵션과 기본 DB 설정 4](images/original/Yoplala_1566765651_Options_gA_nA_rales_3.PNG)

![일반 옵션과 기본 DB 설정 5](images/original/Yoplala_1566765675_Options_gA_nA_rales_4.PNG)

![일반 옵션과 기본 DB 설정 6](images/original/Yoplala_1566768100_Options_gA_nA_rales_5.PNG)

![일반 옵션과 기본 DB 설정 7](images/original/Yoplala_1566765706_Options_gA_nA_rales_6.PNG)

![일반 옵션과 기본 DB 설정 8](images/original/Yoplala_1566768949_Capture.PNG)

![일반 옵션과 기본 DB 설정 9](images/original/Yoplala_1566765743_Options_gA_nA_rales_8.PNG)

</details>

### 데이터베이스

- 공식 게임 DB
- 개인 DB
- OnlyText DB
- 여러 DB
- 저장본 DB
- 번역 불러오기 동작
- 기존 번역 모드 불러오기 동작

<details>
<summary>데이터베이스 옵션 펼쳐보기</summary>

![데이터베이스 옵션 1](images/original/Yoplala_1566812725_Options_BDD_1.PNG)

![데이터베이스 옵션 2](images/original/Yoplala_1566812738_Options_BDD_2.PNG)

![데이터베이스 옵션 3](images/original/Yoplala_1566812754_Options_BDD_3.PNG)

![데이터베이스 옵션 4](images/original/Yoplala_1566812768_Options_BDD_4.PNG)

![데이터베이스 옵션 5](images/original/Yoplala_1566812786_Options_BDD_5.PNG)

![데이터베이스 옵션 6](images/original/Yoplala_1566812797_Options_BDD_6.PNG)

![데이터베이스 옵션 7](images/original/Yoplala_1566812811_Options_BDD_7.PNG)

</details>

### 스크립트 및 MCM

스크립트와 MCM 문자열 분석 범위를 정합니다.

VMAD 등은 일반 번역에서는 불필요할 수 있지만, **MCM 또는 스크립트 안에 실제 게임 표시 문자열이 들어간 모드**에서는 필요할 수 있습니다.

<details>
<summary>스크립트 및 MCM 옵션 펼쳐보기</summary>

![스크립트 및 MCM 옵션 1](images/original/Yoplala_1566813733_Scripts_1.PNG)

![스크립트 및 MCM 옵션 2](images/original/Yoplala_1566813745_Scripts_2.PNG)

![스크립트 및 MCM 옵션 3](images/original/Yoplala_1566813759_Scripts_3.PNG)

![스크립트 및 MCM 옵션 4](images/original/Yoplala_1566813772_Scripts_4.PNG)

![스크립트 및 MCM 옵션 5](images/original/Yoplala_1566813782_Scripts_5.PNG)

![스크립트 및 MCM 옵션 6](images/original/Yoplala_1566813796_Scripts_6.PNG)

</details>

### Def_grup.xml

게임별 GRUP과 FIELD 정의를 확인할 수 있습니다. 일부 필드의 최대 문자열 길이도 확인할 수 있습니다.

<details>
<summary>Def_grup.xml 설정 화면 펼쳐보기</summary>

![Def_grup.xml 설정 화면](images/original/Yoplala_1566813818_Grup.PNG)

</details>

### 기타

- 확인 창
- NifSkope 실행 파일 경로
- 외부 번역 서비스 설정
- 각종 보조 기능

<details>
<summary>기타 옵션 펼쳐보기</summary>

![기타 옵션 1](images/original/Yoplala_1566814250_Divers_1.PNG)

![기타 옵션 2](images/original/Yoplala_1566814268_Divers_2.PNG)

![기타 옵션 3](images/original/Yoplala_1566814285_Divers_3.PNG)

![기타 옵션 4](images/original/Yoplala_1566814298_Divers_4.PNG)

![기타 옵션 5](images/original/Yoplala_1566814313_Divers_5.PNG)

![기타 옵션 6](images/original/Yoplala_1566814324_Divers_6.PNG)

![기타 옵션 7](images/original/Yoplala_1566814341_Divers_7.PNG)

</details>

### 검사

게임에서 표시할 수 없는 문자를 검사합니다.

특히 오래된 Bethesda 게임은 폰트와 인코딩 제약 때문에 모든 유니코드 문자를 표시할 수 있는 것이 아닙니다.

<details>
<summary>금지 문자 검사 설정 펼쳐보기</summary>

![금지 문자 검사 설정](images/original/Yoplala_1566814362_VA_rifications.PNG)

</details>

### 원문의 추가 옵션 화면

원문의 옵션 설명에 포함된 폴더 설정(원문에서 구식으로 표시), 특수 검색, 인터페이스, 분석 규칙 화면입니다.

<details>
<summary>폴더·특수 검색·인터페이스·분석 규칙 옵션 펼쳐보기</summary>

![폴더·특수 검색·인터페이스·분석 규칙 옵션 1](images/original/Yoplala_1566813842_Dossiers.PNG)

![폴더·특수 검색·인터페이스·분석 규칙 옵션 2](images/original/Yoplala_1566814210_Recherche_1.PNG)

![폴더·특수 검색·인터페이스·분석 규칙 옵션 3](images/original/Yoplala_1566814223_Recherche_2.PNG)

![폴더·특수 검색·인터페이스·분석 규칙 옵션 4](images/original/Yoplala_1566814234_Recherche_3.PNG)

![폴더·특수 검색·인터페이스·분석 규칙 옵션 5](images/original/Yoplala_1566814382_Interface_1.PNG)

![폴더·특수 검색·인터페이스·분석 규칙 옵션 6](images/original/Yoplala_1566814400_Interface_2.PNG)

![폴더·특수 검색·인터페이스·분석 규칙 옵션 7](images/original/Yoplala_1566814416_Interface_3.PNG)

![폴더·특수 검색·인터페이스·분석 규칙 옵션 8](images/original/Yoplala_1566814437_RA_gles.PNG)

</details>

---

# 3. 기본 사용법

## 3.1 인코딩

EET에서 말하는 인코딩은 **플러그인 파일 포맷 버전**이 아니라 그 안의 **문자열 인코딩**입니다.

원문 튜토리얼은 당시 기준으로 다음과 같이 설명합니다.


- 구형 Bethesda 게임: 주로 Windows-1252 계열
- Skyrim Special Edition / Fallout 4: UTF-8 사용

![문자열 인코딩 선택 창](images/original/Yoplala_1531262351_Capture.PNG)

다만 실제 번역 환경, 플러그인 형식, 사용하는 한글화 방식에 따라 조건이 달라질 수 있으므로 **EET가 자동 감지한 값을 우선 확인하고, 작업 대상 게임의 한글화 방식도 함께 확인**하세요.

---

## 3.2 게임 데이터베이스

EET의 강점 중 하나는 기존 게임 문자열 DB를 검색하고 재사용할 수 있다는 점입니다.

DB에는 보통 다음과 같은 문자열이 들어갑니다.


- 바닐라 게임 문자열
- 비공식 패치 수정 문자열
- 사용자 또는 배포자가 추가한 교정 내용

현재 불러온 DB는 메인 창에서 확인할 수 있습니다.

![메인 창의 게임 DB와 인코딩 선택 영역](images/original/Yoplala_1566422556_Capture.PNG)

### 활용 방법

- `F3`: 게임 DB 검색
- `F5`: 여러 DB를 이용한 즉시 번역
- `Shift + F5`: 공식 게임 DB만 이용한 즉시 번역

DB 검색은 단순 자동 번역보다 **고유명사와 기존 공식 표현을 찾는 용도**로 특히 유용합니다.

예를 들어 새 대사 안에 기존 지명이나 아이템 이름이 들어 있다면, DB에서 해당 단어가 기존 게임에서 어떻게 쓰였는지 먼저 검색하면 용어 일관성을 유지하기 쉽습니다.

![즉시 번역과 게임 DB 검색 화면 1](images/original/Oaristys_1488712761_f5.jpg)

![즉시 번역과 게임 DB 검색 화면 2](images/original/Yoplala_1566844639_BDD_1.PNG)


---

## 3.3 번역하지 않을 항목 먼저 정리하기

모드를 열자마자 모든 미번역 줄을 하나씩 번역하기보다는, 먼저 **실제로 번역할 필요가 없는 레코드**를 걸러내는 것이 효율적입니다.

### 방법 1: 무시 상태


`Ctrl + Shift + F10`

이 상태의 문자열은 번역 작업 대상에서 제외됩니다.

### 방법 2: 원문을 그대로 사용

`F8`

원문과 번역문을 동일하게 만들어 두어야 하는 문자열에 유용합니다.

예:

- 기술적 식별자
- 번역하면 안 되는 일부 스크립트 값
- 이미지 파일 경로
- 태그/코드 조각

### 번역 여부가 애매한 레코드

다음 항목은 게임과 모드에 따라 표시되지 않는 내부 데이터일 수 있습니다.

- 스크립트 트리거용 퀘스트 이름
- 일부 DIAL 보조 필드
- 이미지 경로(`.dds`, `.png`)
- 내부용 faction/class 명칭
- 테스트/FX/trigger 용도의 내부 명칭
- 스크립트 변수

하지만 **레코드 종류만 보고 기계적으로 전부 제외하면 안 됩니다.** 실제 인게임 표시 여부와 모드 구조를 확인하세요.

![번역하지 않을 문자열을 무시 상태로 표시한 예](images/original/Oaristys_1488712504_ignore.jpg)


---

## 3.4 검색과 필터

현재 모드 검색은 `F4`로 열 수 있습니다.


이 기능은 동일한 용어가 여러 곳에서 쓰이는지 확인하거나 번역을 통일할 때 매우 유용합니다.

![현재 모드 검색 창: F4](images/original/Yoplala_1567069862_F4.PNG)

또한 각 열 위의 필터 입력란을 이용해 다음 값으로 범위를 줄일 수 있습니다.

- EDID
- FIELD
- 원문
- 번역문
- 주석
- 상태

작업 중에는 검색과 필터를 적극적으로 사용하는 편이 좋습니다.

![문자열 표의 열별 필터 입력란](images/original/Yoplala_1567250930_Capture.PNG)

---

## 3.5 번역 저장과 불러오기

### 번역 저장

`Ctrl + S`

이 저장은 일반적으로 **작업 상태를 EET용 번역 데이터로 저장하는 것**이며, 최종 ESP/ESM을 생성하는 작업과는 구분됩니다.

장시간 작업한다면 자주 저장하세요.

### 자동 저장

자동 저장을 활성화해 두면 프로그램 또는 PC가 비정상 종료되었을 때 복구하기 쉽습니다.

### 번역 불러오기

`Ctrl + L`

이전 작업 파일을 다시 불러옵니다.

### 부분 저장


`Ctrl + Shift + S`

협업이나 일부 수정 사항만 전달할 때 유용합니다.

GRUP, 상태, 선택한 줄 등을 기준으로 일부 문자열만 내보낼 수 있습니다.

![번역 부분 저장 창](images/original/Yoplala_1566842190_FenA_tre_Sauvegarde_partielle.PNG)

---

## 3.6 기존 번역 업데이트

이미 번역된 이전 버전의 모드가 있고 신버전이 나왔다면:

1. 새 버전의 원문 플러그인을 엽니다.
2. **번역 → 이미 번역된 모드 불러오기**를 사용합니다.
3. 이전 버전의 번역 플러그인을 선택합니다.
4. 서로 대응되는 문자열을 가져온 뒤 새로 추가되거나 바뀐 부분을 확인합니다.

이전 EET 저장 파일을 불러오는 방식도 사용할 수 있습니다.

---

## 3.7 번역 마무리

최종 출력 전에 다음을 확인하세요.

- 이중 공백
- 잘못된 구두점
- 잘못 들어간 특수문자
- 금지 문자
- 원문이 같은데 번역이 제각각인 항목
- 남은 미번역 문자열
- 불필요하게 번역한 내부 문자열
- TES4 헤더/메타데이터
- BASH 태그 등 외부 도구가 사용하는 특수 표기

예를 들어 Wrye Bash용 태그가 있다면 다음 같은 문자열은 번역하거나 망가뜨리면 안 됩니다.

```text
{{BASH:Delev,Names,Relev,Stats}}
```

번역 결과를 생성한 뒤에는 **인게임 테스트가 필수**입니다.

![번역된 플러그인 생성 완료 메시지](images/original/Yoplala_1531262947_le_tour.PNG)


아카이브에서 추출된 파일이나 스크립트/MCM 파일을 함께 번역했다면 최종 배포 폴더에 필요한 파일이 모두 들어갔는지도 확인하세요.

---

# 4. 고급 기능

## 4.1 작업 환경

장시간 EET를 사용한다면 가독성을 먼저 챙기는 것이 좋습니다.


- 작업 영역 글꼴 크기 키우기
- 더 큰 번역 창 사용
- 필요한 열만 표시
- 자주 쓰는 상태와 검색 기능 익히기

메인 표의 줄을 더블 클릭하면 별도의 번역 창을 사용할 수 있는 버전도 있습니다.

![별도의 번역 작업 창](images/original/Yoplala_1566841246_FenA_tre_Traduction.PNG)

---

## 4.2 주석 활용

**주석(Comment)** 열은 큰 모드를 번역할 때 매우 유용합니다.


예:

- INFO 레코드에서 화자 NPC 확인
- 스크립트 함수 구분
- NPC의 성별/종족 확인
- 문맥 추적

대화문의 존댓말/반말, 성별 어미, 인물별 말투를 맞추려면 가능하면 주석과 관련 레코드를 함께 확인하세요.

![주석 열에서 NPC 이름을 필터링한 예](images/original/Oaristys_1488712564_filtre_npc.jpg)


---

## 4.3 미리보기 기능

EET는 레코드에 따라 다음 자료를 미리 볼 수 있습니다.


- 스크립트
- 책
- NIF 모델
- 음성 파일

![스크립트·책·모델·음성 미리보기 버튼](images/original/Yoplala_1567070824_4.PNG)

NIF 미리보기는 NifSkope 경로를 설정해야 할 수 있습니다.

텍스트만 보고 판단하기 어려운 경우 미리보기를 사용하면 문맥 오류를 크게 줄일 수 있습니다.

<details>
<summary>스크립트와 책 미리보기 창 펼쳐보기</summary>

![스크립트와 책 미리보기 창 1](images/original/Yoplala_1566848643_Scripts.PNG)

![스크립트와 책 미리보기 창 2](images/original/Yoplala_1566848659_Livres.PNG)

</details>


---

## 4.4 대화문 번역

Bethesda 플러그인의 대화문은 DIAL과 INFO 등 여러 레코드로 나뉘어 있기 때문에 **한 줄만 보고 번역하면 문맥이 끊기기 쉽습니다.**

권장 방법:


- 가능한 경우 원래 레코드 순서로 보기
- 관련 레코드 확인
- 주석에서 NPC 이름/감정 확인
- 동일 대화 묶음을 연속해서 작업
- 필요하면 현재 모드 검색으로 상대 대사 추적

**DIAL / INFO 관계는 단순 문자열 유사도가 아니라 실제 레코드 연결 관계를 기준으로 보는 것이 안전합니다.**

![관련 레코드에서 연결된 대화문을 확인하는 예](images/original/Oaristys_1488712593_ligne_liee.jpg)


---

## 4.5 VMAD

인게임에서 영어가 보이는데 EET의 일반 문자열 목록에 나오지 않는 경우, 특히 MCM 관련 문자열이라면 VMAD에 들어 있을 가능성이 있습니다.


필요한 경우:

```text
옵션
→ 스크립트 및 MCM
→ 스크립트 분석 및 번역
→ VMAD 분석 및 번역
```

을 활성화하고 모드를 다시 불러옵니다.

![VMAD 분석 및 번역 활성화 옵션](images/original/Yoplala_1566475558_Capture.PNG)

> VMAD에는 번역하면 안 되는 데이터도 많을 수 있습니다. 무조건 전체 번역하지 말고 실제 표시 문자열인지 확인하세요.

---

## 4.6 스크립트

스크립트 문자열은 가장 주의해야 하는 부분입니다.

![번역할 문자열의 문맥을 확인하는 스크립트 창](images/original/Yoplala_1566842921_FenA_tre_Scripts.PNG)


**변수명, 상태명, 내부 식별자 등을 번역하면 스크립트가 망가질 수 있습니다.**

Skyrim/SSE 예시에서 일반적으로 번역하지 않는 함수/값:

```text
self.GotoState
self.Transfer
xxx.SetActorValue
SetAV / RestoreAV / GetAV
akTarget.ModActorValue
debug.SendAnimationEvent
message.ResetHelpMessage
xxx.ShowAsHelpMessage
xxx.PlayGamebryoAnimation
xxx.AdvanceSkill
xxx.QueryStat
xxx.IncrementStat
asStatFilter ==
debug.Trace
xxx.PrintDebugMessage
```

반면 사용자에게 표시되는 문자열을 인자로 갖는 다음 유형은 번역 대상일 수 있습니다.

```text
debug.messagebox
debug.notification
self.AddHeaderOption
self.AddToggleOption
self.AddSliderOption
self.AddTextOption
xxx.SetName
String Property xxx Auto =
```

이 목록도 절대적인 규칙은 아닙니다. **함수명 자체가 아니라 그 함수에 전달되는 문자열이 실제 UI에 표시되는지**를 확인하세요.

---

## 4.7 여러 모드 동시 작업

모드 본편과 여러 패치를 함께 번역할 때 여러 탭을 동시에 열어두면 용어 일관성을 맞추기 쉽습니다.


설정에 따라 한 탭의 번역을 다른 열린 모드에 전달할 수도 있습니다.

한국어 UI에서는 이 기능을 다음처럼 이해하면 편합니다.

- **다른 열린 모드로 번역 전달**
- **다른 열린 모드에서 번역 가져오기**

확정된 문자열까지 무조건 덮어쓰는지 여부는 설정을 확인하세요.

![여러 모드의 문자열을 모아 보는 모든 모드 탭](images/original/Yoplala_1567071867_Onglet_unique.PNG)


---

## 4.8 여러 모드 분석·비교

EET는 다음 작업을 지원합니다.

- 폴더 전체 분석
- 여러 모드 분석
- 두 모드 비교

모드 본편과 패치의 번역을 통일하거나, 어느 플러그인에서 영어 문자열이 들어오는지 찾을 때 유용합니다.

<details>
<summary>여러 모드 분석과 두 모드 비교 창 펼쳐보기</summary>

![여러 모드 분석과 두 모드 비교 창 1](images/original/Yoplala_1566846574_Analyse_mods.PNG)

![여러 모드 분석과 두 모드 비교 창 2](images/original/Yoplala_1566846590_Comparaison.PNG)

</details>


---

## 4.9 개인 데이터베이스

개인 DB는 자신이 번역하고 검수한 문자열을 재사용하는 기능입니다.


장점:

- 반복되는 용어를 빠르게 재사용
- 같은 모드 계열의 패치 번역에 유용
- 대규모 의존 모드의 공식/검수 번역을 재활용 가능

단점:

- 잘못된 번역을 저장하면 이후 모드에도 오류가 퍼질 수 있음
- 문맥이 다른데 동일 문자열이라는 이유로 잘못 적용될 수 있음

따라서 **검수가 끝난 번역만 개인 DB에 넣는 것**을 권장합니다.

![개인 데이터베이스 설정](images/original/Yoplala_1566475166_Capture.PNG)

- 개인 DB 검색: `Shift + F3`
- 개인 DB 적용: `Ctrl + F5`

<details>
<summary>개인 DB 검색과 선택한 줄 추가 메뉴 펼쳐보기</summary>

![개인 DB 검색과 선택한 줄 추가 메뉴 1](images/original/Yoplala_1566844656_BDD_2.PNG)

![개인 DB 검색과 선택한 줄 추가 메뉴 2](images/original/Yoplala_1574693945_EET_Clic_droit.PNG)

</details>


---

# 5. 검수 작업 팁

## 바닐라 문자열이 번역문을 덮어쓰는 문제

기존 번역을 검수할 때 원문 모드를 먼저 열면 자동 비교 기능 때문에 기존 번역 내용이 DB 문자열로 바뀌는 경우가 있을 수 있습니다.

이럴 때는:

- 자동 적용 관련 옵션을 끄거나
- 기존 값이 적용되기 전에 작업 열을 정리한 뒤
- 검수본을 별도 검수 열에 불러오는 방식

을 사용할 수 있습니다.

## 검수 열

큰 번역을 검수하거나 두 번역본을 비교한다면 **검수 열**을 활용하세요.


```text
옵션 → 일반 옵션 → 검수
```

검수 열의 문자열을 최종 번역 열로 옮길 때는 `Shift + F8`을 사용할 수 있습니다.

![일반 옵션의 검수 열 설정](images/original/Yoplala_1566474912_Capture.PNG)

## 수정 사항만 전달하기

전체 번역 파일 대신 수정한 부분만 전달해야 한다면:

1. 수정한 줄을 사용자 지정 상태로 표시합니다.
2. 부분 저장을 실행합니다.
3. 사용자 지정 상태만 골라 내보냅니다.

협업 검수에 유용합니다.

---

# 6. 번역할 때 추가로 확인할 것

플러그인만 번역했다고 작업이 끝나는 것은 아닙니다.

모드 폴더에서 다음도 확인하세요.

- `.txt`
- `.xml`
- `.json`
- `.lua`
- MCM 설정 파일
- Papyrus 스크립트
- 이미지/텍스처 안에 포함된 문자
- 음성 및 자막
- 별도 STRINGS/DLSTRINGS/ILSTRINGS
- 인터페이스 파일

또 게임 UI에는 표시 가능한 문자열 길이 제한이 존재할 수 있습니다.

원문 가이드에서는 Skyrim/SSE 기본 UI의 일부 알림 문자열이 너무 길어지면 보기 어려워진다는 점을 예로 들고 있습니다.

이런 제한은 폰트와 UI 모드에 따라 달라질 수 있으므로 실제 게임에서 테스트하세요.

---

# 7. 프로그램 업데이트

원문 튜토리얼에서도 이 부분은 **추후 작성 예정** 상태로 남아 있습니다.

EET를 새 버전으로 바꿀 때는 최소한 다음 파일을 먼저 백업하는 것을 권장합니다.

- 개인 DB
- 번역 작업 저장본
- 사용자 지정 언어 파일
- 사용자 설정
- 직접 수정한 XML/정의 파일

새 버전에 기존 설정 파일을 그대로 덮어쓰면 호환 문제가 생길 수 있으므로, 새 배포본과 비교해 필요한 것만 옮기는 편이 안전합니다.

---

# 8. 추가 참고 자료

원문 튜토리얼에서 함께 참고하도록 안내하는 자료들입니다.

- 원문 EET 튜토리얼  
  https://www.confrerie-des-traducteurs.fr/forum/viewtopic.php?f=372&t=29457
- EET 관련 원문 포럼/자료  
  https://www.confrerie-des-traducteurs.fr/
- xTranslator  
  https://github.com/MGuffin/xTranslator

원문에는 프랑스어 번역 규칙, Elder Scrolls 문장부호 규칙, 특수문자, 바닐라 음성 처리 등 프랑스어 번역자를 위한 별도 문서도 연결되어 있습니다. 한국어 번역에서는 해당 언어별 규칙을 그대로 적용하기보다 **한국어 문장부호·고유명사·게임별 공식 번역 용어 기준**을 별도로 정해 사용하는 것을 권장합니다.

---

# 빠른 작업 순서

처음 EET를 쓰는 경우 아래 순서로 시작하면 편합니다.

1. 원문 모드 열기
2. 게임/인코딩/DB 확인
3. 번역하지 않을 내부 문자열부터 무시 처리
4. 기존 게임 용어를 DB에서 검색
5. 미번역 문자열 번역
6. 대화문은 관련 레코드와 주석을 확인
7. 스크립트/VMAD는 실제 표시 문자열만 수정
8. 맞춤법·구두점·금지문자·용어 통일 검사
9. 번역 저장
10. 번역된 플러그인 생성
11. 인게임 테스트
12. 수정 후 최종 배포

---

## 출처 및 감사

원문 튜토리얼은 **Yoplala**가 La Confrérie des Traducteurs 포럼에 작성했습니다.

- 원문: https://www.confrerie-des-traducteurs.fr/forum/viewtopic.php?f=372&t=29457
- 원문 작성자: Yoplala
- 프로그램 개발: Épervier 666

이 저장소는 한국어 사용자에게 EET의 기능과 작업 흐름을 이해하기 쉽게 전달하기 위한 한국어 가이드입니다.

---

## 기여

오역, 오래된 설명, 최신 EET에서 달라진 메뉴, 한국어 번역 환경에서 필요한 추가 설명이 있다면 Issue 또는 Pull Request로 수정해 주세요.
