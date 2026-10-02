function Loader() {
  return (
    <div className="loader-container">

      <div className="spinner"></div>

      <p>
        Analyzing your PDF...
      </p>

      <span>
        This may take a few seconds.
      </span>

    </div>
  );
}

export default Loader;