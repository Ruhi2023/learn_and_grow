import React , { useState, useEffect, use } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
const UserLearningPath = () => {

    const navigate = useNavigate();
    useEffect(() => {
        const verifyUser = async () => {
            const token = localStorage.getItem('token');
            if (!token) {
                navigate('/login');
            }
            else {
                try{
                    const ver_res = await axios.post('http://localhost:5000/verify-user', {token: token});

                    if(ver_res.status !== 200){
                        navigate('/login');
                    }
                }
                catch(err){
                    console.log(err);
                    localStorage.removeItem('token');
                    navigate('/login');
                }
            }
        }
        verifyUser();
    }, [navigate])
  return (
    <div>
      <h1>UserLearningPath</h1>
    </div>
  )
}

export default UserLearningPath
