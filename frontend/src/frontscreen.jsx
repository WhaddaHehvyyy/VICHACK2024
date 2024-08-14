import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './frontscreen.css';
import logo from './assets/logo_only.png';
import { useGlobalState } from './GlobalContext';

function FrontScreen() {
  const [file, setFile] = useState(null);
  const [showButton, setShowButton] = useState(false);
  const { globalState, setGlobalState } = useGlobalState();

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    if (selectedFile) {
      if (selectedFile.type === 'video/mp4') {
        setFile(selectedFile);
        setShowButton(true);
        setGlobalState(selectedFile);
      } else {
        setFile(null);
        alert('Please upload a valid MP4 file.');
        setShowButton(false);
        setGlobalState(null);
      }
    }
  };

  return (
    <>
      <img src={logo} className='front-logo' alt="Logo" />
      <h1 className='login-title'>AccuBoxer AI</h1>
      <div className='upload-container'>
        <input
          type="file"
          id="fileInput"
          className="url-input"
          onChange={handleFileChange}
        />
        <label htmlFor="fileInput" className="file-upload-button">
          {file ? 'Select Another File' : 'Choose File'}
        </label>
      </div>
      <p className='video-success' style={{ display: showButton ? 'block' : 'none' }}>
        Video Successfully Uploaded!
      </p>
      <Link to={'/playerscreen'} className='link'>
        <button
          className='analysis-button'
          style={{ display: showButton ? 'block' : 'none' }}
        >
          Start Analysis
        </button>
      </Link>
    </>
  );
}

export default FrontScreen;
