import { useState } from 'react';
import { useAuth } from '../../context/AuthContext';
import { useNavigate, Link } from 'react-router-dom';

import './SignUp.css';

const SignUp = () => {

  const { signup } = useAuth();
  const navigate = useNavigate();

  const [firstname, setFirstName] = useState('');
  const [lastname, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    if (password !== confirmPassword) {
      setError('Passwords do not match.');
      return;
    }

    try {
      await signup(firstname, lastname, email, password);
      navigate('/parse');
    } catch (err) {
      const message = err.response?.data?.detail || 'Error signing up. Please try again.';
      setError(message);
    }
  };

  return (
    <div className="auth-page">
      <div className="auth-card">
        <div className="auth-logo">
          <span className="auth-logo-icon">T</span>
          <span className="auth-logo-text">TQA</span>
        </div>

        <h1 className="auth-title">Create account</h1>
        <p className="auth-subtitle">Sign up to start using TQA</p>

        {error && <p className="auth-error">{error}</p>}

        <form className="auth-form" onSubmit={handleSubmit}>
          <div className="auth-field">
            <label htmlFor="firstname">Firstname</label>
            <input
              type="text"
              id="firstname"
              value={firstname}
              onChange={(e) => setFirstName(e.target.value)}
              placeholder="Enter a firstname"
              required
            />
          </div>
          <div className="auth-field">
            <label htmlFor="lastname">Lastname</label>
            <input
              type="text"
              id="lastname"
              value={lastname}
              onChange={(e) => setLastName(e.target.value)}
              placeholder="Enter a lastname"
              required
            />
          </div>

          <div className="auth-field">
            <label htmlFor="email">Email</label>
            <input
              type="email"
              id="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="Enter your email"
              required
            />
          </div>

          <div className="auth-field">
            <label htmlFor="password">Password</label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Create a password"
              required
            />
          </div>

          <div className="auth-field">
            <label htmlFor="confirmPassword">Confirm Password</label>
            <input
              type="password"
              id="confirmPassword"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              placeholder="Confirm your password"
              required
            />
          </div>

          <button type="submit" className="auth-submit">Sign Up</button>
        </form>

        <p className="auth-switch">
          Already have an account? <Link to="/login">Log in</Link>
        </p>
      </div>
    </div>
  );
};

export default SignUp;
