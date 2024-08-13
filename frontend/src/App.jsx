
import './App.css'
import PlayerScreen from './player.jsx'
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import FrontScreen from './frontscreen.jsx';



function App() {
  

  return (
    
    <>
      
      <Router>
        <Routes>
          <Route path="/playerscreen" element={<PlayerScreen />} />
          <Route path= "/" element={<FrontScreen />} />
        </Routes>
      </Router>
    

    </>
  )
}

export default App
