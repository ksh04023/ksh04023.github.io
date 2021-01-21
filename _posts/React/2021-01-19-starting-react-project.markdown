---  
layout: post  
title:  "간편하게 리액트 프로젝트 시작하기"  
date:   2021-01-19 22:52:00  
category: Github
use_math: true
comments: true
---  


### 리액트란?
<img src="https://i.ibb.co/J5F4MXz/react.png" alt="react" border="0">

리액트는 UI를 제작하기 위한 자바스크립트 라이브러리이다.
웹사이트에 기술된 장점을 좀 설명해보았다.\
https://reactjs.org/
1. Declarative 선언적
인터랙티브한 UI 구성을 쉽게 해준다. 애플리케이션의 데이터가 바뀔 때마다 
리액트가 효율적으로 업데이터하고 컴포넌트를 렌더링해 변화되는 각 상태를 나타낼 수 있다. 
2. Component-Based
//TODO
3. Learn Once, Write Anywhere
//TODO

###리액트 설치하기
1. Node.js, npm이 설치되어 있는지, 버전은 무엇인지 확인한다. v13 이상이 아니면 오류가 많다고 하는데 나는 
작년 초에 설치한 v12여서 재설치를 해주었다.
```commandline
node -v
npm --version
```

2. 프로젝트를 시작할 폴더를 하나 생성한다. 다음 명령어를 통해 프로젝트를 시작한다.
```commandline
npx create-react-app your-project-name
```

