import React from 'react'
import { Switch, Route } from 'react-router' 
import './App.css';
import Home from './Home'
import LoginForm from './Login'
import NotFound from './NotFound'

function App() {
  return (
    <Switch>
      <Route exact={true} path="/" component={Home} />
      <Route path="/login" component={LoginForm} />
      <Route component={NotFound}/>
    </Switch>
  )
}

export default App
