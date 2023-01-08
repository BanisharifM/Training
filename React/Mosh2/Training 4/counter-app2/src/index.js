import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import Counters from "./components/counters";
import "bootstrap/dist/css/bootstrap.css";
// import "font-awesome/css/font-awesome.css";
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <Counters />
  </React.StrictMode>
);
