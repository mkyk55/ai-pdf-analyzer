import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

import Navbar from "./components/Navbar";

import Home from "./pages/Home";
import AnalyzePDF from "./pages/AnalyzePDF";
import ChatPDF from "./pages/ChatPDF";

import "./App.css";


function App() {
  return (
    <BrowserRouter>

      <Navbar />

      <main>

        <Routes>

          <Route
            path="/"
            element={<Home />}
          />

          <Route
            path="/analyze-pdf"
            element={<AnalyzePDF />}
          />

          <Route
            path="/chat"
            element={<ChatPDF />}
          />

        </Routes>

      </main>

    </BrowserRouter>
  );
}


export default App;