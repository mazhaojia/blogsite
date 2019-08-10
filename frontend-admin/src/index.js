import React from 'react';
import ReactDOM from 'react-dom';
import { Router, Route } from 'react-router'
import './index.css';
import App from './App';
import Login from './Login'

import { CookiesProvider } from 'react-cookie';

function Root() {
  return (
    <CookiesProvider>
      <Login />
    </CookiesProvider>
  );
}

ReactDOM.render((
  <Router>
      <Route path="/" component={Root}>
        <Route path="admin" component={App} />
      </Route>
  </Router>
), document.getElementById('root'));
