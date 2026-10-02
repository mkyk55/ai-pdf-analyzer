import { useState } from "react";
import ReactMarkdown from "react-markdown";

import Loader from "../components/Loader";

interface AnalysisResponse {
  filename: string;
  summary: string;
}

function AnalyzePDF() {

  const [file, setFile] = useState<File | null>(null);

  const [result, setResult] =
    useState<AnalysisResponse | null>(null);

  const [loading, setLoading] =
    useState(false);

  const [error, setError] =
    useState("");

  const handleFileChange = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {

    const selectedFile =
      event.target.files?.[0];

    if (!selectedFile) {
      return;
    }

    if (selectedFile.type !== "application/pdf") {

      setError("Please select a PDF file.");

      setFile(null);

      return;
    }

    setFile(selectedFile);

    setError("");

    setResult(null);
  };


  const analyzePDF = async () => {

    if (!file) {

      setError("Please select a PDF first.");

      return;
    }

    setLoading(true);

    setError("");

    setResult(null);


    const formData = new FormData();

    formData.append("file", file);


    try {

      const response = await fetch(
        "http://127.0.0.1:8000/analyze-pdf",
        {
          method: "POST",
          body: formData,
        }
      );


      const data = await response.json();


      if (!response.ok) {

        throw new Error(
          data.detail || "Failed to analyze PDF"
        );

      }


      setResult(data);

    } catch (error) {

      if (error instanceof Error) {

        setError(error.message);

      } else {

        setError(
          "Something went wrong while analyzing the PDF."
        );

      }

    } finally {

      setLoading(false);

    }
  };


  return (

    <div className="analyze-page">

            <div className="page-header">
            <div className="hero-badge">
                🤖 AI Document Analysis
            </div>

            <h1>Analyze Your PDF</h1>

            <p>
                Upload a PDF document and our AI will extract the content,
                understand the document, and generate a structured summary
                with the most important insights.
            </p>
            </div>


      <div className="upload-card">

        <div className="upload-area">

          <div className="upload-icon">
            📄
          </div>

          <h2>
            Upload your PDF
          </h2>

          <p>
            Select a PDF document to analyze.
          </p>


          <input
            id="pdf-upload"
            type="file"
            accept=".pdf,application/pdf"
            onChange={handleFileChange}
          />


          {file && (

            <div className="selected-file">

              <span>
                📄 {file.name}
              </span>

              <span>
                {(file.size / 1024 / 1024).toFixed(2)} MB
              </span>

            </div>

          )}


          <button
            className="primary-button analyze-button"
            onClick={analyzePDF}
            disabled={!file || loading}
          >

            {loading
              ? "Analyzing..."
              : "Analyze PDF"}

          </button>


          {error && (

            <div className="error-message">
              {error}
            </div>

          )}

        </div>

      </div>


      {loading && (

        <div className="result-card">

          <Loader />

        </div>

      )}


      {result && !loading && (

        <div className="result-card">

          <div className="result-header">

            <div>

              <h2>
                AI Summary
              </h2>

              <p>
                {result.filename}
              </p>

            </div>

          </div>


          <div className="markdown-content">

            <ReactMarkdown>
              {result.summary}
            </ReactMarkdown>

          </div>

        </div>

      )}

    </div>
  );
}

export default AnalyzePDF;