import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import AnalyzePDF from "./pages/AnalyzePDF";
import "./App.css";

function App() {
  return (
    <BrowserRouter>
      <Navbar />

      <main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/analyze-pdf" element={<AnalyzePDF />} />
        </Routes>
      </main>
    </BrowserRouter>
  );
}

export default App;