import React from 'react';
import ReactDOM from 'react-dom';
import { Router, Route } from 'react-router'
import './index.css';
import App from './App';
import Login from './Login'

ReactDOM.render((
  <Router>
      <Route path="/" component={App}>
        <Route path="login" component={Login} />
      </Route>
  </Router>
), document.getElementById('root'));
