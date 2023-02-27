import React from "react";
import Choose from "../components/Choose"
import Clients from "../components/Clients";
import CreateAndSell from "../components/CreateAndSell";
import Footer from "../components/Footer";
import Home from "../components/Home";
import MarketPlace from "../components/MarketPlace";
import ScrollToTop from "../components/ScrollToTop";
import Subscribe from "../components/Subscribe";
import ProfilePage from '../components/profilePage';

export default function HomePage() {
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
