---  
layout: post  
title:  "[React] 리액트 프로젝트 기초(3) - react-router 알아보기"  
date:   2021-01-25 17:44:00  
category: Github
use_math: true
comments: true
---  

### react-router란?
SPA(Single Page Application)에 최적화 되어있는 React를 이용해 사용자의 요청에 따라 여러 동적 요소를 구현하기 위해 사용한다.
웹과 앱을 동시에 구현하려는 목적이라면 `react-router`를 설치하면 되지만, 필자는 웹만 구현하고 있기 때문에 `react-router-dom`을 설치한다.

현재 진행중인 프로젝트에 바로 설치해준다.
```commandline
$ npm install react-router-dom
```

어랏 이런 에러가 뜬다?
```
npm ERR! Maximum call stack size exceeded
npm ERR! A complete log of this run can be found in:
...
```

[갓스택오버플로우](https://stackoverflow.com/questions/40566348/maximum-call-stack-size-exceeded-on-npm-install) 의
도움을 받아 해결했다.

```commandline
npm cache clean
```
로 했더니 또 다음과 같은 에러가 발생했다.
```commandline
As of npm@5, the npm cache self-heals from corruption issues and data extracted from thache verify' instead.
```

다음 command로 해결했다.
```commandline
npm cache clean --force
```


