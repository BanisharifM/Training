import React, { Component } from "react";

// stateless function component
const Navbar = ({ totalCounter }) => {
  console.log("Navbar - Rendered");
  return (
    <nav className="navbar navbar-light bg-light">
      <a className="navbar-brand" href="#">
        Navbar{" "}
        <span className="badge badge-pill badge-secondary">{totalCounter}</span>
      </a>
    </nav>
  );
};

export default Navbar;
