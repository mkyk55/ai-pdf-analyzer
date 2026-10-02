import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-container">

        <Link to="/" className="logo">
          AI PDF Analyzer
        </Link>

        <div className="nav-links">
          <Link to="/">Home</Link>

          <Link to="/analyze-pdf">
            Analyze PDF
          </Link>
        </div>

      </div>
    </nav>
  );
}

export default Navbar;