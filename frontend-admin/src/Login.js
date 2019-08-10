import React, { useEffect } from 'react';
import { CookiesProvider } from 'react-cookie';
import { useCookies } from 'react-cookie';
import { Redirect } from 'react-router';
import './App.css';

function Login() {

  const [cookie, setCookie] = useCookies(['login'])

  useEffect(() => {
    if (cookies.get('login')) {
      this.setState({
        hasCookie: true
      });
    } else {
        this.setState({
            has
        })
    }
    this.state = {
      name: 
    };
    document.title = `You clicked ${count} times`;
  });

  return (
    <CookiesProvider>
      <div />
    </CookiesProvider>
  );
}

export default Login;
