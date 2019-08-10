import React, { useState, useEffect } from 'react';
import { useCookies } from 'react-cookie';
import { Redirect } from 'react-router';
import './Login.css';

function Login() {

  const [hasCookie] = useState(false)
  const [cookie, setCookie] = useCookies(['login'])

  useEffect(() => {
    if (cookie.get('login')) {
      this.setState({
        hasCookie: true
      })
    } else {
      this.setState({
        hasCookie: false
      })
    }
  })

  if (hasCookie) {
    return <Redirect to='/admin' />
  }
  
  return (
    <div />
  )
}

export default Login;
