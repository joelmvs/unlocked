// src/pages/UploadPage.jsx

import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Mail, Camera, Clock, FileText, Key } from 'lucide-react';

export default function UploadPage() {
  const [file, setFile] = useState(null);
  const [isDragging, setIsDragging] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleDrop = (e) => {
    e.preventDefault();
    setIsDragging(false);
    const droppedFile = e.dataTransfer.files[0];
    if (droppedFile) {
      setFile(droppedFile);
      // Auto-upload when file is dropped
      uploadFile(droppedFile);
    }
  };

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
      // Auto-upload when file is selected
      uploadFile(selectedFile);
    }
  };

  const uploadFile = async (fileToUpload) => {
    setLoading(true);
    setError('');
    try {
      const formData = new FormData();
      formData.append('file', fileToUpload);

      const res = await fetch(
        import.meta.env.VITE_API_URL + '/upload',
        { method: 'POST', body: formData }
      );

      if (!res.ok) throw new Error(res.statusText);
      const { contract_id } = await res.json();
      navigate(`/contract/${contract_id}`);
    } catch (err) {
      setError(err.message || 'Upload failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      className="min-h-screen bg-[#fefae0] flex flex-col items-center px-6 py-12 text-gray-800"
      style={{ fontFamily: "'Karla', sans-serif" }}
    >
      <div className="flex items-center justify-center gap-3 mb-10">
        <Key size={32} className="text-black-600" />
        <h1 className="text-4xl font-bold text-black">
          Unlock Your Contract
        </h1>
      </div>

      <div
        onDragOver={(e) => e.preventDefault()}
        onDragEnter={() => setIsDragging(true)}
        onDragLeave={() => setIsDragging(false)}
        onDrop={handleDrop}
        className={`w-full max-w-md border-2 border-dashed rounded-2xl p-12 text-center shadow-sm transition-all ${
          isDragging ? 'border-yellow-500 bg-yellow-100' : 'border-black'
        }`}
      >
        <input
          type="file"
          id="fileInput"
          className="hidden"
          onChange={handleFileChange}
        />
        <label htmlFor="fileInput" className="cursor-pointer">
          <div className="mb-4 text-5xl">📄</div>
          <p className="text-lg font-medium">Drop a file or tap to upload</p>
          <p className="text-sm text-gray-500 mt-1">PDF, DOCX supported</p>
        </label>
      </div>

      {file && (
        <div className="mt-4 text-base text-gray-700">
          Selected file: <strong>{file.name}</strong>
        </div>
      )}

      {loading && (
        <div className="mt-4 text-base text-blue-600">
          Uploading... Please wait
        </div>
      )}

      {error && (
        <p className="mt-2 text-sm text-red-600">{error}</p>
      )}

      {/* OTHER ACTION BUTTONS */}
      <div className="mt-16 w-full max-w-md flex flex-col items-center">
        <div className="space-y-6 w-full flex flex-col items-center">
          {[
            { label: 'Import from Gmail', icon: Mail },
            { label: 'Take a Photo', icon: Camera },
            { label: 'Recent Files', icon: Clock }
          ].map(({ label, icon: Icon }) => (
            <button
              key={label}
              onClick={() => {
                // TODO: Implement these features
                console.log(`${label} clicked`);
              }}
              className="w-full max-w-[320px] text-lg font-medium py-6 px-8 rounded-3xl shadow-lg transition-all duration-200 ease-in-out bg-white border border-black hover:shadow-xl hover:scale-[1.02] active:scale-[0.98] flex items-center justify-center gap-3"
            >
              <Icon size={24} />
              {label}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}