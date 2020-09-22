import React from 'react';
import { Link, navigate } from 'gatsby';

function goToSlicemasters() {
  setTimeout(() => {
    console.log('slicers');
    navigate('/slicemasters', { replace: true });
  }, 2000);
}

const Nav = () => (
  <div>
    <ul>
      <li>
        <Link to="/">Home</Link>
      </li>
      <li>
        <Link to="/beers">Beers</Link>
      </li>
      <li>
        <button type="button" onClick={goToSlicemasters}>
          Click me to see slicemasters after 2 seconds
        </button>
      </li>
    </ul>
  </div>
);

export default Nav;
