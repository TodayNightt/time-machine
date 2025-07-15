import React from "react";
import { Container } from "react-bootstrap";

const Calender = ({ currentDate }) => {
  const randomId = (i) => Math.floor(Math.random() * Number(i) * 100);

  return (
    <>
      <React.StrictMode>
        <Container className="container-calender m-2 mt-5 ">
          <br />

          {/* Day */}
          <Container className="day">
            <p>Day</p>
            <Container
              key={"day" + randomId(currentDate[0].value[0] + 10)}
              className={"num"}
            >
              <p>{currentDate[0].value[0]}</p>
            </Container>
            <Container
              key={"day" + randomId(currentDate[0].value[1] + 5)}
              className={"num"}
            >
              <p>{currentDate[0].value[1]}</p>
            </Container>
          </Container>

          {/* Month */}
          <Container className="month">
            <p>Month</p>
            <Container
              key={"month" + randomId(currentDate[1].value[0] + 10)}
              className={"num"}
            >
              <p>{currentDate[1].value[0]}</p>
            </Container>
            <Container
              key={"month" + randomId(currentDate[1].value[1] + 5)}
              className={"num"}
            >
              <p>{currentDate[1].value[1]}</p>
            </Container>
          </Container>

          {/* Year */}
          <Container className="year">
            <p>Year</p>
            <Container
              key={"year" + randomId(currentDate[2].value[0] + 56)}
              className={"num"}
            >
              <p>{currentDate[2].value[0]}</p>
            </Container>
            <Container
              key={"year" + randomId(currentDate[2].value[1] + 1)}
              className={"num"}
            >
              <p>{currentDate[2].value[1]}</p>
            </Container>
            <Container
              key={"year" + randomId(currentDate[2].value[2] + 3)}
              className={"num"}
            >
              <p>{currentDate[2].value[2]}</p>
            </Container>
            <Container
              key={"year" + randomId(currentDate[2].value[3] + 2)}
              className={"num"}
            >
              <p>{currentDate[2].value[3]}</p>
            </Container>
          </Container>
        </Container>
      </React.StrictMode>
    </>
  );
};

export default Calender;
