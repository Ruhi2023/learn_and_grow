import { createContext,useState } from "react"
import React from 'react'
import aixos from 'axios'
import {BrowserRouter} from 'react-router-dom'

function GlobalContextProvider() {

    const [user,setUser] = useState(null)
    const [loggedIn,setLoggedIn] = useState(false)

  return (
    <div>
      
    </div>
  )
}

export default GlobalContextProvider
