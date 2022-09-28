import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router } from 'react-router-dom';
import Home from "./Home";
import reportWebVitals from './reportWebVitals';



function initFacebookSdk() {
  return new Promise(resolve => {
      // wait for facebook sdk to initialize before starting the react app
      window.fbAsyncInit = function () {
          window.FB.init({
              appId: "614342580170103",
              cookie: true,
              xfbml: true,
              version: 'v15.0'
          });

          // auto authenticate with the api if already logged in with facebook
          window.FB.getLoginStatus(({ authResponse }) => {
              if (authResponse) {
                  // accountService.apiAuthenticate(authResponse.accessToken).then(resolve);
                  console.log('YES');
                  resolve();
              } else {
                  resolve();
              }
          });
      };

      // load facebook sdk script
      (function (d, s, id) {
          var js, fjs = d.getElementsByTagName(s)[0];
          if (d.getElementById(id)) { return; }
          js = d.createElement(s); js.id = id;
          js.src = "https://connect.facebook.net/en_US/sdk.js";
          fjs.parentNode.insertBefore(js, fjs);
      }(document, 'script', 'facebook-jssdk'));    
  });
}

function startApp() {
  ReactDOM.render(
    <React.StrictMode>
      <Router>
        <Home/>
      </Router>
    </React.StrictMode>,
    document.getElementById('root')
  );

  // If you want to start measuring performance in your app, pass a function
  // to log results (for example: reportWebVitals(console.log))
  // or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
  // reportWebVitals();
}

initFacebookSdk().then(startApp);
