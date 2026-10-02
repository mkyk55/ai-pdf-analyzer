import { useState } from "react";
import ReactMarkdown from "react-markdown";

interface Source {
  filename: string;
  chunk_index: number;
  score: number;
  text: string;
}

interface AskResponse {
  question: string;
  answer: string;
  sources: Source[];
}

function ChatPDF() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState<AskResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const askQuestion = async () => {
    if (!question.trim()) {
      setError("Please enter a question.");
      return;
    }

    setLoading(true);
    setError("");
    setAnswer(null);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/ask",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            question: question,
            top_k: 3,
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail || "Something went wrong."
        );
      }

      setAnswer(data);
    } catch (err) {
      setError(
        err instanceof Error
          ? err.message
          : "Unable to connect to backend."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-page">
      <div className="chat-container">

        <div className="chat-header">
          <span className="chat-badge">
            AI DOCUMENT ASSISTANT
          </span>

          <h1>Chat with Your PDF</h1>

          <p>
            Ask questions about your uploaded document
            and get answers using AI-powered retrieval.
          </p>
        </div>

        <div className="question-box">

          <textarea
            value={question}
            onChange={(event) =>
              setQuestion(event.target.value)
            }
            placeholder="Ask something about your PDF..."
            rows={4}
          />

          <button
            onClick={askQuestion}
            disabled={loading}
          >
            {loading ? "Thinking..." : "Ask Question"}
          </button>

        </div>

        {error && (
          <div className="error-message">
            {error}
          </div>
        )}

        {answer && (
          <div className="answer-section">

            <div className="answer-card">

              <h2>Answer</h2>

              <div className="markdown-content">
                <ReactMarkdown>
                  {answer.answer}
                </ReactMarkdown>
              </div>

            </div>

            {answer.sources.length > 0 && (
              <div className="sources-card">

                <h2>Sources</h2>

                {answer.sources.map(
                  (source, index) => (
                    <div
                      className="source-item"
                      key={index}
                    >
                      <div className="source-header">
                        <strong>
                          {source.filename}
                        </strong>

                        <span>
                          Score:{" "}
                          {source.score.toFixed(3)}
                        </span>
                      </div>

                      <p>
                        {source.text}
                      </p>
                    </div>
                  )
                )}

              </div>
            )}

          </div>
        )}

      </div>
    </div>
  );
}

export default ChatPDF;