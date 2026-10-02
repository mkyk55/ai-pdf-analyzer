import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-brand">
        <Link to="/">AI PDF Analyzer</Link>
      </div>

      <div className="navbar-links">
        <Link to="/">Home</Link>
        <Link to="/analyze-pdf">Analyze PDF</Link>
        <Link to="/chat">Chat with PDF</Link>
      </div>
    </nav>
  );
}

export default Navbar;