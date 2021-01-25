---  
layout: post  
title:  "리액트 프로젝트 기초(2) - Button 추가해 Event Handling 하기"  
date:   2021-01-25 16:31:00  
category: Github
use_math: true
comments: true
---  

여러 영상을 통해 리액트 기초를 살짝 맛본 후 바로 프로젝트 시작하려니 조금 어렵다. 필자는 Html, CSS도 처음 다뤄보는
웹린이🐣이다. 그래도 무언가 구현하면서 공부하는 것이 제일 효율적임을 알기에 그냥 도전!

기존 Html에서 `<button>` 태그를 바로 넣었던 것과는 달리 리액트에서는
`<button>`이 들어가 있는 Component를 먼저 만든 후, 이 Component를 앱에 넣는다. 

우선 버튼의 

#### 1. Component 만들기

- 만들고자 하는 Component의 이름을 가진 파일을 새로 만든다.
- 다음과 같이 Component를 import 한다. 
- 주의해야 할 점은 기존 javascript 문법과는 달리 JSX 문법을 사용해야 한다는 것이다.
    - `onclick` => `onClick`
    - `class` => `className`
    
**MyButton.js**
```javascript
import React, {Component} from 'react';
```

- Component를 상속받는 클래스를 생성한다.
- 버튼이 클릭되었을 때 `buttonClicked()`가 실행된다.
```javascript
class MyButton extends Component {
    buttonClicked(){
        alert("button clicked");   
    }
    render(){
        return <button className = "btn" onClick={this.buttonClicked}>Click me!</button>;
    }
}
```

외부 모듈에서 해당 component를 import하기 위해서는 export를 필수로 해야한다.
```javascript
export default BtnCalendar;
```

#### 2. 버튼을 예쁘게 만들어 보자!

원시 상태의 버튼은 이렇게 별로 예쁘지 않게 생겼다.

위 Component 생성 코드에서 `className = "btn"`의 속성을 넣어주었다. 클래스 이름은 앞에 `.`을 붙여 CSS를 조작한다.

<img src="https://i.ibb.co/yV8rqcp/button-before-design.png" alt="button-before-design" border="0">

```css
.btn {
    background-color:#405dffd7;
    border-radius:13px;
    border: 0;
    cursor:pointer;
    color:#ffffff;
    margin: 5vmax;
    font-size:15px;
    padding:8px 33px;
    text-decoration:none;
}

/*버튼 위에 커서를 올렸을 때*/
.btn:hover {
	background-color:#405dff;
}

/*버튼을 눌러 포커스된 상태일 때*/
.btn:focus {
    border: none;
    outline: none;
}

/*버튼을 누르고 있는 동안*/
.btn:active {
    border: 0;
    position:relative;
    top:0.5px;
}


```

예쁜 버튼이 만들어졌다!
<img src="https://i.ibb.co/V3HzMxF/button-after-design.png" alt="button-after-design" border="0">

#### 3. App 화면에 삽입하기

- 1에서 export 했던 Component를 import 해준다.
- 현재 이 파일의 같은 폴더 안의 모듈이라는 뜻에서 `./`로 path를 지정 해주었다.
- 다음과 같이 MyButton을 삽입해준다.
**App.js**
```javascript
import './App.css';
import MyButton from "./MyButton";

function App() {
  return (
    <div className="App">
      <MyButton/>
    </div>
  );
}

export default App;
```
