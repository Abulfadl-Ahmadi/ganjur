import CutCreateForm from './components/CutCreate';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";


function App() {
  return (
    <div className="App">
      <Router>
        <div>
          <Routes>
            <Route path="/cut-create" element={<CutCreateForm />} />
          </Routes>
        </div>
      </Router>
    </div>
  );
}

export default App;
