import React from "react";
import { Container, Card } from "react-bootstrap";
import { usePromiseTracker } from "react-promise-tracker";
import { TailSpin } from "react-loader-spinner";

import Tab from "react-bootstrap/Tab";
import Tabs from "react-bootstrap/Tabs";

const Output = ({ data, date }) => {
  const { promiseInProgress } = usePromiseTracker();
  return (
    <Container className="container-output m-2">
      <Tabs
        defaultActiveKey={data[0].id}
        id="output-tabs"
        className="tab mb-2 p-2"
        transition={false}
        fill
      >
        {data.map((item) => (
          <Tab
            key={item.id}
            eventKey={item.id}
            title={
              <Container>
                {item.id.charAt(0).toUpperCase() + item.id.slice(1)}
                <p className="badge bg-dark ms-4 text-light">
                  {item.text && item.text !== "Nrf"
                    ? item.text.length
                    : item.text === "Nrf"
                    ? 0
                    : null}
                </p>
              </Container>
            }
          >
            <Container className="section-container p-3 overflow-auto">
              {promiseInProgress ? (
                <Container className="loading-container">
                  <p>Initiating Time Travel</p>
                  <p>
                    {" " +
                      date[0].value +
                      `/` +
                      date[1].value +
                      `/` +
                      date[2].value}
                  </p>

                  <TailSpin radius={2} color="#000000" wrapperClass="loading" />
                </Container>
              ) : item.text && item.text !== "Nrf" ? (
                item.text.map((data) => (
                  <Container key={data.name}>
                    <Card className="card mb-2 mt-3 p-4">
                      <Card.Img src={data.image} />
                      <Card.Body>
                        <Card.Title>{data.name}</Card.Title>
                        <Card.Body>{data.extract}</Card.Body>
                        <Card.Link
                          href={data.urls}
                          target="_blank"
                          className="text-decoration-none "
                        >
                          {data.urls}
                        </Card.Link>
                      </Card.Body>
                    </Card>
                  </Container>
                ))
              ) : item.text === "Nrf" ? (
                <Nrf />
              ) : null}
            </Container>
          </Tab>
        ))}
      </Tabs>
    </Container>
  );
};

export default Output;

const Nrf = () => {
  return (
    <Container className="nrf-section">
      <h4>No result found</h4>
    </Container>
  );
};
