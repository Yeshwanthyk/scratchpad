import React from 'react';
import Footer from './Footer';
import Nav from './Nav';
import 'normalize.css';

const Layout = ({ children }) => (
  <div>
    <Nav />
    {children}
    <Footer />
  </div>
);

export default Layout;
