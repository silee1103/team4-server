# team4-server

## github-action 관련
team4-server -> Watoon(프로젝트) -> Watoon(앱) 방식으론 자동으로 배포가 안됨!
team4-server -> Watoon, User..(앱)으로 구성되어있어야 배포가 제대로 됨.

team4-server에서 상단에 settings 탭 - Secrets and variables - Action에서 repository secrets 추가하기

여기서 AWS_ACCESS_KEY_ID와 AWS_SECRET_ACCESS_KEY 추가 필요(실제 배포하는 사람의 것)

이후 .github/workflows/deploy.yml에서 secrets.AWS_ACCESS_KEY_ID_jsh 변수 이름을 secrets에 등록한 변수 이름으로 바꿔주기

+ aws에서 미리 어플리케이션과 환경을 생성한 후, deploy 파일에 application_name과 environment_name을 자신의 것으로 맞춰 기재하기

2024-01-12 View 1차 구현
 - user와 webtoon 앱의 migration이 각각 작동해서 실제 migration 하실 때 user것 먼저, 그 다음에 webtoon 것으로 해야 할 것 같습니다. 이유는 잘 모르겠지만 추후 수정하겠습니다. 