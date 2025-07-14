import { BrowserRouter as Router, Link } from 'react-router-dom';

function App() {
  return (
    <Router>
      <div style={{
        minHeight: '100vh',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center'
      }}>
        <nav style={{
          display: 'flex',
          width: '600px',
          background: '#1f2937',
          color: 'white',
          marginBottom: '2rem',
          padding: '1rem',
          justifyContent: 'space-between'
        }}>
          <Link to="/" style={{ flex: 1, textAlign: 'center', color: 'white', textDecoration: 'none' }}>Главная</Link>
          <Link to="/about" style={{ flex: 1, textAlign: 'center', color: 'white', textDecoration: 'none' }}>О проекте</Link>
        </nav>
        <div style={{
          width: '600px',
          background: '#111827',
          color: 'white',
          textAlign: 'center',
          padding: '2rem'
        }}>
          Контент
        </div>
      </div>
    </Router>
  );
}

export default App;
