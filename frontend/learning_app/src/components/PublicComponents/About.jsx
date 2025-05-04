import React from 'react'
import { Navigate, useNavigate } from 'react-router-dom';

const About = () => {
  return (
    <div>
      <h1> About</h1>
      <div className='container'>
        <div className='row'>
          <div className='col-6'>
            <h2> Learn</h2>
          </div>
          <div className='col-6'>
            <h2> Get Support</h2>
          </div>
        </div>
      </div>
    </div>
  )
};

export default About;
