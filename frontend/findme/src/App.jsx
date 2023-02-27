import React from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import LandingPage from "./pages/landingPage";
import Login from "./pages/loginPage";
import HomePage from "./pages/homePage"

function App () {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<LandingPage/>} />
        <Route path='/home' element={<HomePage/>} />
        <Route path='/login' element={<Login/>} />
      </Routes>
    </BrowserRouter>
  )
}

export default App;




/**import React from "react";
import Choose from "./components/Choose";
import Clients from "./components/Clients";
import CreateAndSell from "./components/CreateAndSell";
import Footer from "./components/Footer";
import Home from "./components/Home";
import MarketPlace from "./components/MarketPlace";
import ScrollToTop from "./components/ScrollToTop";
import Subscribe from "./components/Subscribe";
import ProfilePage from './components/profilePage';

export default function App() {
  return (
      <div>
        <ScrollToTop />
        <Home />
        <ProfilePage/>
        <Clients />
        <CreateAndSell />
        <Choose />
        <MarketPlace />
        <Subscribe />
        <Footer />
      </div>
  );
}
*/
