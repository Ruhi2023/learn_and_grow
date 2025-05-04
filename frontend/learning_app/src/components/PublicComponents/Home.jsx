import React, { useState } from 'react'
import { Navigate, useNavigate } from 'react-router-dom';

const Home = () => {
    const Navmap = {'login': '/login', 
        'about': '/about', 
        'home': '/home' , 
        'register': '/register',
        "continue": '/user-learning-path'};
    const [going_to, setGoing_to] = useState('/'); 
    const [yesGo,setGo] = useState(false);
    const handleSend = (to) => {
        console.log("Navigating to " + Navmap[to]);
        setGoing_to(Navmap[to]);
        setGo(true);
    }
  return (
    <>
    <div className='container' style={{minHeight: '100vh', textAlign: 'center'}}><h1>Home</h1><div class="container">
  <div className="row">
  <div className="col-4">
    <button onClick={()=>{handleSend('about')}}>Do nothing</button></div>
    <div className="col-4">
      <button onClick={()=>{handleSend('about')}} >About</button></div>
    <div className="col-4">
      <button onClick={()=>{handleSend('login')}} >Login</button></div>
    
  </div>
  <div className="row">
  <div className="col-6" style={{textAlign: 'center'}}>
    <button onClick={()=>{handleSend('register')}}>Register</button></div>
    <div className="col-6">
      <button onClick={()=>{handleSend('about')}} >Do nothing</button></div>
  </div>
</div>
</div>
{yesGo && (<Navigate to={going_to} replace={true} />)}
</>
  ) 
}

export default Home


// import React, { useState } from 'react'
// import { Navigate } from 'react-router-dom';

// const Home = () => {
//     const Navmap = {
//         'login': '/login', 
//         'about': '/about', 
//         'home': '/', 
//         'register': '/register',
//         'continue': '/user-learning-path'
//     };
    
//     const [destination, setDestination] = useState('');
//     const [shouldNavigate, setShouldNavigate] = useState(false);
    
//     const handleNavigation = (to) => {
//         console.log("Navigating to " + Navmap[to]);
//         setDestination(Navmap[to]);
//         setShouldNavigate(true);
//     }
    
//     return (
//         <>
//             <div className='container' style={{minHeight: '100vh', textAlign: 'center'}}>
//                 <h1>Home</h1>
//                 <div className="container">
//                     <div className="row">
//                         <div className="col-4">
//                             <button onClick={() => {/* Do nothing */}}>Do nothing</button>
//                         </div>
//                         <div className="col-4">
//                             <button onClick={() => handleNavigation('about')}>About</button>
//                         </div>
//                         <div className="col-4">
//                             <button onClick={() => handleNavigation('login')}>Login</button>
//                         </div>
//                     </div>
//                     <div className="row">
//                         <div className="col-6" style={{textAlign: 'center'}}>
//                             <button onClick={() => handleNavigation('register')}>Register</button>
//                         </div>
//                         <div className="col-6">
//                             <button onClick={() => {/* Do nothing */}}>Do nothing</button>
//                         </div>
//                     </div>
//                 </div>
//             </div>
//             {shouldNavigate && <Navigate to={destination} replace={false} />}
//         </>
//     ) 
// }

// export default Home