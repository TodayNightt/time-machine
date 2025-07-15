import React from "react";
import Container from "react-bootstrap/Container";
import Navbar from "react-bootstrap/Navbar";
import icon from "../icon/time-machine.png";

const TitleBar = () => {
  return (
    <Navbar expand="lg">
      <Container className="m-2">
        <Navbar.Brand>
          <img
            src={icon}
            alt=""
            height="60"
            className="d-inline-block align-top badge"
          />
          {``}
          <h1 className="d-inline-block ps-4 ">Time Machine</h1>
        </Navbar.Brand>
      </Container>
    </Navbar>
  );
};

export default TitleBar;
