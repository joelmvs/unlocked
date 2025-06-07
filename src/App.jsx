import { BrowserRouter, Routes, Route } from 'react-router-dom';
import UploadPage from './pages/UploadPage';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Root path now renders UploadPage */}
        <Route path="/" element={<UploadPage />} />
        <Route path="/upload" element={<UploadPage />} />
        {/* ...other routes */}
      </Routes>
    </BrowserRouter>
  );
}
