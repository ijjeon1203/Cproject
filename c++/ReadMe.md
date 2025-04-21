# how to use 

cmake -B build -G "Visual Studio 16 2019"


cmake -B build -G "Visual Studio 17 2022"
- v143 툴셋 이슈 



# CMake 빌드 명령어 (Visual Studio 2019용)

```bash
cmake -B build -G "Visual Studio 16 2019"
```

| 옵션 | 의미 |
|------|------|
| `-B build` | CMake 빌드 디렉터리를 `build`로 지정 (out-of-source build 권장) |
| `-G "Visual Studio 16 2019"` | Visual Studio 2019를 빌드 시스템으로 사용 |

---

## 🧩 옵션 추가 예시

### 1. **툴셋 버전 지정 (v142 등)**  
```bash
cmake -B build -G "Visual Studio 16 2019" -T v142
```

### 2. **64비트 플랫폼 설정**
Visual Studio 기본 플랫폼은 Win32이므로 64비트로 하고 싶다면:

```bash
cmake -B build -G "Visual Studio 16 2019" -A x64
```

---

## 🛠 이후 빌드 방법

```bash
cmake --build build --config Release
```
또는

```bash
cmake --build build --config Debug
```

※ Visual Studio 솔루션 파일 (`.sln`)은 `build` 디렉터리에 생성됩니다.

---

## 💡 팁: VS에서 열기

```bash
start build/YourProject.sln
```

또는 그냥 `build` 폴더 들어가서 수동으로 `.sln` 더블클릭해도 됩니다.

---

필요하시면 VS Code에서 디버깅까지 연동하는 `CMakePresets.json` 예제도 드릴 수 있어요.  
추가로 궁금한 설정 있으신가요? 😄