import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import "bootstrap" 
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
{
  /* The following line can be included in your src/index.js or App.js file */
}
import Login from './components/PublicComponents/Login'
import Register from './components/PublicComponents/Register'
import Home from './components/PublicComponents/Home'
import About from './components/PublicComponents/About'
import UserLearningPath from './components/learningAppSpecific/UserLearningPath'
import NavBarLP from './components/PublicComponents/NavBarLP'
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <BrowserRouter>
      <Routes>
        <Route path='/' element={<NavBarLP/>} >
          <Route path ='/home' element={<Home />} />
          <Route path='/about' element={<About />} />
          <Route path='/login' element={<Login />} />
          <Route path='/register' element={<Register />} />
          <Route path='/user-learning-path' element={<UserLearningPath />} />
          <Route path='*' element={<h1>404</h1>}/>
        </Route >
        
      </Routes>
      
      </BrowserRouter>
    </>
  )
}

export default App
