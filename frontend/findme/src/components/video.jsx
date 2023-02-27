import React from 'react';
// import { Link } from "react-router-dom";
import shareVideo from '../assets/share.mp4';
import logo from '../assets/Gold.png';
import { FcGoogle } from 'react-icons/fc';
//import { SiSlack } from 'react-icons/si';
import {  FaGithub } from 'react-icons/fa';
import styled from "styled-components";

const StyledContainer = styled.div`
  display: flex;
  justify-content: start;
  align-items: center;
  flex-direction: column;
  height: 100vh;
`;

const StyledVideoContainer = styled.div`
  position: relative;
  width: 100%;
  height: 100%;  
`;

const StyledVideo = styled.video`
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10%;
`;

const StyledOverlay = styled.div`
  position: absolute;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  top: 0;
  right: 10px;
  bottom: 0;
  left: 0;
  background-color: rgba(0, 0, 0, 0.5);
  @media screen and (width <= 500px) {
    flex-direction: row;
  }
`;

const StyledLogo = styled.img`
  width: 300px;
  height: 300px;
`;

const StyledButton = styled.button`
  background-color: ${props => props.backgroundColor};
  color: ${props => props.color};
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0.75rem;
  right: 10px;
  border-radius: 0.5rem;
  cursor: pointer;
  outline: none;
  margin-left: 3.75rem;
  width: 200px;
`;

const StyledLogin = styled.div`
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: transparent;
  border-radius: 15px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
  width: 105%;
  // margin: 50px auto;
  padding: 20px;
  /* height: 60vh; */
}

.container h2 {
  text-align: center;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
  text-align: center;
  color: #fff;
  
}

input[type="email"],
input[type="text"],
input[type="password"] {
  border: 1px solid #ccc;
  border-radius: 5px;
  box-sizing: border-box;
  padding: 10px;
  display: block;
  width: 18rem;
  // margin-left: 15%;
}

button {
  background-color: darkgrey;
  border: none;
  border-radius: 5px;
  color: black;
  cursor: pointer;
  font-size: 16px;
  margin-top: 10px;
  padding: 5px;
  width: 150px;
}

button:hover {
  background-color: blue;
}
p{
  color: white;
}
`
const StyledSignin = styled.ol`
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: transparent;
  border-radius: 15px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
  width: 100%;
  // margin: 50px auto;
  padding: 50px;
  // /* height: 60vh; */
}
`

const Vid = () => {
//   const handleGoogleSignIn = () => {
//     console.log('Google sign in clicked');
//   };

//   const handleGithubSignIn = () => {
//     console.log('Github sign in clicked');
//   };

//   const handleFacebookSignIn = () => {
//     console.log('Facebook sign in clicked');
//   };

//   const handleSlackSignIn = () => {
//     console.log('Slack sign in clicked');
//   };

  return (
    <StyledContainer>
      <StyledVideoContainer>
        <StyledVideo
          src={shareVideo}
          type="video/mp4"
          loop
          controls={false}
          muted
          autoPlay
        />
        <StyledOverlay>
          <div className="p-5">
            <StyledLogo src={logo} alt="logo" />
          </div>

          
          <StyledLogin>
            <div className='container'>  
            <form>
              <label>
                Email
                <input type="email" name="email" placeholder="youremail@gmail.com" />
              </label>{" "}
              <br />
              <label>
                Password
                <input type="password" name="password" />
              </label>{" "}
              <br />
              <button type="sub">Login</button>
              {/* dont have an account? <a href="#">Sign up</a> */}
              {/* Don't have an account? sign up */}
              <br></br>
              <br />
              <input type="checkbox" name="keepMeLoggedIn" /><span><p>Keep me logged in</p></span>
              <br></br>
            </form>
            </div>
          </StyledLogin>
          <br></br>
          <br />
          <br />
          <StyledSignin>
          <div className='container'>
                <p color='white'>Don't have an account?</p>
                <br></br>
                <StyledButton
                type="button"
                backgroundColor='white'
                color='black'
                >
                <FcGoogle style={{ marginRight: '0.75rem' }} />
                Sign in with Google
                </StyledButton>
                <br></br>
                <StyledButton
                type="button"
                backgroundColor='#24292e'
                color='white'
                >
                <FaGithub style={{ marginRight: '0.75rem' }} />
                Sign in with Github
                </StyledButton>

                {/* <StyledButton
                type="button"
                backgroundColor='#3b5998'
                color='white'
                >
                <FaFacebook style={{ marginRight: '0.75rem' }} />
                Sign in with Facebook
                </StyledButton>

                <StyledButton
                type="button"
                backgroundColor='#4a154b'
                color='white'
                >
                <SiSlack style={{ marginRight: '0.75rem' }} />
                Sign in with Slack
                </StyledButton> */}
          </div>
          </StyledSignin>
        </StyledOverlay>
        </StyledVideoContainer>
    </StyledContainer>
  )
};

export default Vid;