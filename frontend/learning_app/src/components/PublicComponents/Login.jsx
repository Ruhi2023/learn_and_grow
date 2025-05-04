import React, {useState} from 'react'
import { Navigate, useNavigate } from 'react-router-dom';
import axios from 'axios'
import 'bootstrap/dist/css/bootstrap.min.css';




const Login = () => {
    const [userName, setUserName] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    const [showPopup, setShowPopup] = useState(false);
    const [popupTitle, setPopupTitle] = useState('');

    const navigate = useNavigate();

    const validateForm = () => {
        if (userName.length === 0) {
            setError('Username is required');
            return false;
        }
        if (password.length === 0) {
            setError('Password is required');
            return false;
        }
        setError('');
        return true;
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!validateForm()) {
            return;
        }
        setLoading(true);
        const data = {
            username: userName,
            password: password
        }
        try{
            res = axios.post('http://localhost:2221/login', data)
            setLoading(false);
            if (res.status === 200) {
                // the authentication succeded store the token
                const res_data = res.json()
                localStorage.setItem('token', res_data.data.token);
                navigate('/user-learning-path');
            }
            else{
                const res_data = res.json()
                setError(res_data.message || 'Authentication failed');
                console.log(res)
            }
        }
        catch(err){
            console.log(err)
            setError('An issue occured, please try again')
            setLoading(false);
        }
        // Handle form submission logic here
    } 
  return (
    <div className='container'>
        <div class="row">
    <div className="col-2">
      {/* Empty div */}
    </div>
    <div className="col-8">
    <form>
  <div className="mb-3">
    <label htmlFor="username1" className="form-label">Username</label>
    <input type="email" className="form-control" id="username1" aria-describedby="emailHelp" onChange={(e) => setUserName(e.target.value)}/>
    <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
  </div>
  <div class="mb-3">
    <label htmlFor="exampleInputPassword1" className="form-label">Password</label>
    <input type="password" className="form-control" id="exampleInputPassword1" onChange={(e) => setPassword(e.target.value)}/>
  </div>
  <button type="submit" className="btn btn-primary" onClick={handleSubmit}>Submit</button>
</form>
    </div>
    <div class="col-2">
      {/* Empty div */}
    </div>
  </div>

      
    </div>
  )
};

export default Login;
