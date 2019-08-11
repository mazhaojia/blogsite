import React, { useState, useEffect } from 'react'
import { useCookies, CookiesProvider } from 'react-cookie'
import { Redirect } from 'react-router'

function Home() {
  const [hasCookie, setHasCookie] = useState(false)
  // eslint-disable-next-line no-unused-vars
  const [cookies, setCookie] = useCookies(['login'])

  useEffect(() => {
    if (cookies.value) {
      setHasCookie(true)
    } else {
      setHasCookie(false)
    }
  }, [cookies.value])

  return (
    <CookiesProvider>
      {
        hasCookie ? (
          <div>Home</div>
        ) : <Redirect to='/login' />
      }
    </CookiesProvider>
  )
}

export default Home
