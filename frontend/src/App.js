import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';

function App() {

  const [selectImage, setSelectImage] = useState(null);

  const handleFileChange = (e) => {
    const file = e.target.file[0];
    setSelectImage(file);
  };

  return (
    <div>
      <p>Upload Image: </p>
      <input type="file" accept="image/*" onChange={handleFileChange} />
    </div>
  );
}

export default App;
