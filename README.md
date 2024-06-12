# flask_release
플라스크 배포용

## 설치
이 프로젝트를 설치하려면 다음 단계를 따르세요:

1. 리포지토리를 클론합니다:
    ```bash
    git clone https://github.com/KimTaekgyoon/repository.git
    ```
2. 필요한 패키지를 설치합니다:
    ```bash
    cd repository/flask_server
    pip install -r requirements.txt
    ```

## 사용법

다음은 이 프로젝트를 사용하는 예제입니다:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
