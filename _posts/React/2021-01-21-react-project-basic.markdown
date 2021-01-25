---  
layout: post  
title:  "리액트 프로젝트 기초(1) - Default 파일의 역할, Html 안에 변수 넣기"  
date:   2021-01-21 17:14:00  
category: Github
use_math: true
comments: true
---  

#### 프로젝트 default 파일이 어떻게 동작하는가!
create-react-app을 이용하면 여러 폴더와 파일들이 뜬다. 
1. `index.js`의 역할
여기서 `App.js` 파일 안에 있는 html 태그들을 public 폴더 안에 있는 `index.html` 파일 안에 넣어 달라는 명령을 한다.

**index.js**
```javascript
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```   
정확히는 Id가 `root`인 `<div>`태그에다 `App.js`에 있는 것들을 다 가져다 주세요. 하는 것이다.    
    
**App.js**
```javascript
function App() {
  return (
    <div className="App">
      Hello World!
    </div>
  );
}
```
App이라는 함수에 간단하게 html을 return 하도록 하면 된다.


### JSX란?
리액트에서 사용하는 html 대신의 문법

1. `class` 대신 `className` 으로 정의한다.
```javascript
<div className="App">

</div>
```
2. {}을 이용해 Data binding을 쉽게 한다.
Data binding: 데이터를 제 자리에 집어 넣는 것

- 변수 삽입하기

**App.js**
```javascript
function App(){
    let posts = 'your post';
    
    return (
        <div className="App">
            <h4>{ posts }</h4>
        </div>
    );
}
```

- 함수 삽입하기

다음과 같은 함수를 추가해준다.
**App.js**
```javascript
function result(){
    return 2 + 3;
}
```

**App.js**
```
function App(){
    let posts = 'your post';
    
    return (
        <div className="App">
            <h4>{ result() }</h4>
        </div>
    );
}
```

- 이미지 삽입하기
사진 파일을 import 해준다.
```javascript
import logo from './logo.svg'
```

`<img>` 태그 안에 source를 { }로 바로 넣어준다.

**App.js**
```javascript
<img src={ logo } />
```

3. Style 속성 넣기
object 자료형으로 스타일을 만들어 넣는다.

**App.js**
```javascript
<div style = {{color: 'blue', font-size : 30px }} >Your Title</div>
```