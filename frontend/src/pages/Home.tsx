import { Link } from "react-router-dom";

function Home() {
  return (
    <div className="home-page">

      {/* Hero Section */}
      <section className="hero">
        <div className="hero-content">

          <div className="hero-badge">
            🤖 AI-Powered Document Intelligence
          </div>

          <h1>
            Turn Complex PDFs Into
            <span> Clear Insights</span>
          </h1>

          <p>
            Upload a PDF document and let AI analyze the content,
            identify the most important information, and generate
            a structured summary in seconds.
          </p>

          <div className="hero-actions">
            <Link
              to="/analyze-pdf"
              className="primary-button"
            >
              📄 Analyze Your PDF
            </Link>
          </div>

          <p className="hero-note">
            Fast • AI-powered • Easy to understand
          </p>

        </div>
      </section>


      {/* How It Works */}
      <section className="how-it-works">

        <div className="section-header">
          <h2>How It Works</h2>
          <p>
            Analyze your documents in three simple steps.
          </p>
        </div>

        <div className="steps">

          <div className="step-card">
            <div className="step-number">1</div>

            <div className="step-icon">📤</div>

            <h3>Upload Your PDF</h3>

            <p>
              Select any text-based PDF from your computer.
              The document is securely sent to the analysis
              service for processing.
            </p>
          </div>


          <div className="step-card">
            <div className="step-number">2</div>

            <div className="step-icon">🧠</div>

            <h3>AI Understands It</h3>

            <p>
              The application extracts the document text and
              uses AI to identify important information,
              key points, facts, and conclusions.
            </p>
          </div>


          <div className="step-card">
            <div className="step-number">3</div>

            <div className="step-icon">📊</div>

            <h3>Get Clear Insights</h3>

            <p>
              Receive a structured Markdown summary that makes
              long and complicated documents easier to understand.
            </p>
          </div>

        </div>

      </section>


      {/* Features */}
      <section className="features-section">

        <div className="section-header">
          <h2>What Can It Do?</h2>

          <p>
            Designed to make document analysis faster and easier.
          </p>
        </div>


        <div className="features">

          <div className="feature-card">
            <div className="feature-icon">📄</div>

            <h3>PDF Text Extraction</h3>

            <p>
              Automatically extracts readable text from
              uploaded PDF documents.
            </p>
          </div>


          <div className="feature-card">
            <div className="feature-icon">🤖</div>

            <h3>AI Document Analysis</h3>

            <p>
              Uses an AI model to understand the content and
              identify the information that matters most.
            </p>
          </div>


          <div className="feature-card">
            <div className="feature-icon">📝</div>

            <h3>Structured Summaries</h3>

            <p>
              Generates organized summaries with executive
              insights, key points, important facts, and conclusions.
            </p>
          </div>


          <div className="feature-card">
            <div className="feature-icon">⚡</div>

            <h3>Fast Processing</h3>

            <p>
              Analyze documents in seconds instead of manually
              reading through every page.
            </p>
          </div>


          <div className="feature-card">
            <div className="feature-icon">🎯</div>

            <h3>Focus on Important Information</h3>

            <p>
              Quickly understand the core message of lengthy
              reports, documents, and business material.
            </p>
          </div>


          <div className="feature-card">
            <div className="feature-icon">💻</div>

            <h3>Developer-Friendly API</h3>

            <p>
              Built with React, TypeScript, FastAPI and AI,
              making the platform easy to extend with new capabilities.
            </p>
          </div>

        </div>

      </section>


      {/* Use Cases */}
      <section className="use-cases">

        <div className="section-header">
          <h2>Useful For</h2>

          <p>
            A practical tool for working with information-heavy documents.
          </p>
        </div>

        <div className="use-case-grid">

          <div className="use-case">
            📑 Business Reports
          </div>

          <div className="use-case">
            📋 Project Documents
          </div>

          <div className="use-case">
            ⚖️ Legal Documents
          </div>

          <div className="use-case">
            📚 Research Papers
          </div>

          <div className="use-case">
            📊 Financial Reports
          </div>

          <div className="use-case">
            📖 Long Documents
          </div>

        </div>

      </section>


      {/* CTA */}
      <section className="final-cta">

        <h2>
          Have a PDF You Want to Understand?
        </h2>

        <p>
          Upload it and let AI turn the document into
          structured, easy-to-read insights.
        </p>

        <Link
          to="/analyze-pdf"
          className="primary-button"
        >
          Start Analyzing →
        </Link>

      </section>

    </div>
  );
}

export default Home;