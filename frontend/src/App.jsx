import { useState } from "react";
import "./App.css";


function App() {
  const [currentDocument, setCurrentDocument] = useState("");
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [sources, setSources] = useState([]);

  const [selectedFile, setSelectedFile] = useState(null);
  const [uploadMessage, setUploadMessage] = useState("");
  const [uploading, setUploading] = useState(false);

  const [loading, setLoading] = useState(false);




  const uploadPDF = async () => {

    if (!selectedFile) {
      setUploadMessage("Please select a PDF first.");
      return;
    }

    setUploading(true);
    setUploadMessage("");

    const formData = new FormData();

    formData.append("file", selectedFile);

    try {

      const response = await fetch(
        "http://127.0.0.1:8000/upload",
        {
          method: "POST",
          body: formData
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Upload failed");
      }
      setCurrentDocument(data.filename);

      setUploadMessage(
        `✅ ${data.filename} uploaded successfully. ` +
        `${data.pages} pages, ${data.chunks} chunks indexed.`
      );

    } catch (error) {

      setUploadMessage(
        `❌ ${error.message}`
      );

    }

    setUploading(false);
  };


  const askQuestion = async () => {

    if (!question.trim()) {
      return;
    }

    setLoading(true);
    setAnswer("");
    setSources([]);

    try {

      const response = await fetch(
        "http://127.0.0.1:8000/ask",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
  question: question,
  source: currentDocument
})
        }
      );

      const data = await response.json();

      setAnswer(data.answer);
      setSources(data.sources);

    } catch (error) {

      setAnswer(
        "Unable to connect to the backend."
      );

    }

    setLoading(false);
  };


  return (

    <div className="app">

      <header>

        <h1>AI Research Assistant</h1>

        <p>
          Upload a document and ask questions about it
        </p>

      </header>


      <main>

        {/* PDF UPLOAD */}

        <div className="upload-box">

          <h2>Upload PDF</h2>

          <input
            type="file"
            accept=".pdf"
            onChange={(e) =>
              setSelectedFile(e.target.files[0])
            }
          />

          <button
            onClick={uploadPDF}
            disabled={uploading}
          >

            {uploading
              ? "Uploading..."
              : "Upload & Index PDF"}

          </button>

          {uploadMessage && (

            <p className="upload-message">
              {uploadMessage}
            </p>

          )}

        </div>


        {/* QUESTION */}

        <div className="question-box">

          <h2>Ask a Question</h2>

          {currentDocument && (
  <p>
    📄 Current document: <strong>{currentDocument}</strong>
  </p>
)}

          <textarea
            placeholder="Ask something about your document..."
            value={question}
            onChange={(e) =>
              setQuestion(e.target.value)
            }
          />

          <button
            onClick={askQuestion}
            disabled={loading}
          >

            {loading
              ? "Thinking..."
              : "Ask AI"}

          </button>

        </div>


        {/* ANSWER */}

        {answer && (

          <div className="answer">

            <h2>AI Answer</h2>

            <p>{answer}</p>

          </div>

        )}


        {/* SOURCES */}

        {sources.length > 0 && (

          <div className="sources">

            <h2>Sources</h2>

            {sources.map((source, index) => (

              <div
                className="source"
                key={index}
              >

                📄 {source.source}
                {" — "}
                Page {source.page}

              </div>

            ))}

          </div>

        )}

      </main>

    </div>
  );
}


export default App;
