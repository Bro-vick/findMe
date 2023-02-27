import React from "react";
//import Choose from "../components/Choose";
import Clients from "../components/Clients";
// import Vid from "../components/video";
import Footer from "../components/Footer";
import Home from "../components/Home";
import MarketPlace from "../components/MarketPlace";
import ScrollToTop from "../components/ScrollToTop";
//import Subscribe from "./components/Subscribe";
//import ProfilePage from '../components/profilePage';
import Choose from "../components/Choose";

export default function LandingPage() {
  return (
      <div>
        <ScrollToTop />
        <Home />
        <Clients />
        <Choose />
        <MarketPlace />
        <Footer />
      </div>
  );
};
