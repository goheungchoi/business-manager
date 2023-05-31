import { useState } from 'react'

import { 
  BrowserRouter as Router,
  Routes,
  Route,
  Link,
} from 'react-router-dom'

import LogInForm from './components/LogInForm';
import CreateUserForm from './components/CreateUserForm';
import AdminView from './components/AdminView';
import UsersList from './components/DisplayUsersList';
import User from './components/User';
import UserView from './components/UserView';

function Home() {

  return (
    <div style={{ padding: 20 }}>
      <h1>Business Manager</h1>
      <nav style={{margin: 10}}>
        <Link to="/" style={{padding: 5}}>
          Home
        </Link>
        
        <Link to="/about" style={{padding: 5}}>
          About
        </Link>
      </nav>

      <Link to="/login" style={{padding: 5}}>
        <button type='button'>
          Log In
        </button>
      </Link>

      <Link to="/signup" style={{padding: 5}}>
        <button type='button'>
          Sign Up
        </button>
      </Link>
      
    </div>
  )
}

function About() {
  return (
    <div style={{ padding: 20 }}>
      <h2>About</h2>
      <p>Lorem ipsum dolor sit amet, consectetur adip.</p>
    </div>
  );
}

function NoMatch() {
  return (
    <div style={{ padding: 20 }}>
      <h2>404: Page Not Found</h2>
      <p>Lorem ipsum dolor sit amet, consectetur adip.</p>
    </div>
  );
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/login" element={<LogInForm />} />
        <Route path="/signup" element={<CreateUserForm />} />
        <Route path="/user/:id" element={<UserView />} />
        
        <Route path="/admin" element={<AdminView />} > 
          <Route index element={<UsersList />} />
          <Route path=":id" element={<User />} />
        </Route>
        <Route path="*" element={<NoMatch />} />
      </Routes>
    </Router>
  );
}

export default App;
