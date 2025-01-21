import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';

const App = () => (
  <Router>
    <div>
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/about">About</Link>
        </li>
      </ul>

      <hr />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </div>
  </Router>
);

const Home = () => <h2>Home</h2>;
const About = () => <h2>About</h2>;

export default App;

// bentuk spt ini
{/* 
<Router>
  <Routes>
      <Route path='/' element={<Home/>}>
      <Route path='posts'>
          <Route path='new'>
          <Route path=':postId'>
      <Route> 
*/}
