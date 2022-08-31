# NotJustMe
### 랜덤 번호 생성기

---

#### 원하는 번호 개수와 범위를 입력하고 버튼을 눌러 실행하면 입력된 개수만큼의 랜덤한 수를 범위 내에서 생성해 보여준다.
---
* #### terminal
    * #### pyinstaller -w -F --icon=./sources/icons/icon.ico ./sources/name.py
    * #### pyinstaller -w -F --icon=./sources/icons/icon.ico ./name.spec


* #### example.spec
    * #### added_files = [('./sources/notjustme.ui', '.'), ('./sources/notjustme_result.ui', '.')]
    * #### datas=added_files, 