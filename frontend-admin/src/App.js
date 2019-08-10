import React, { useState, useEffect } from 'react';
import { CookiesProvider } from 'react-cookie';
import { useCookies } from 'react-cookie';
import { Redirect } from 'react-router';
import './App.css';

function App() {

  const [hasCookie] = useState(0)
  const [cookie] = useCookies(['login'])

  useEffect(() => {
    if (cookie.get('login')) {
      this.setState({
        hasCookie: 2
      })
    } else {
      this.setState({
        hasCookie: 1
      })
    }
  })

  if (hasCookie == 2) {
    return (
      <div />
    )
  } else if (hasCookie == 1) {
    return <Redirect to='/login' />
  } else {
    return (
      <CookiesProvider>
        <div />
      </CookiesProvider>
    )
  }
}

export default App;
