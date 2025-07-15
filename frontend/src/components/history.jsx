import React, { Component } from "react";
import { Container, Card } from "react-bootstrap";

class History extends Component {
  state = {
    data: [],
  };
  randomId = (i) => Math.floor(Math.random() * Number(i) * 100);

  componentDidMount() {
    fetch("/db/get", {
      method: "GET",
    }).then((response) => {
      response
        .json(response)
        .then((response) => this.setState({ data: response }));
    }, []);
  }

  handleRefresh = () => {
    fetch("/db/get", { method: "GET" }).then((response) => {
      response
        .json(response)
        .then((response) => this.setState({ data: response }));
    });
  };

  handleClear = async () => {
    await fetch("/db/clear", { method: "GET" });
    this.handleRefresh();
  };

  render() {
    return (
      <Container className="container-history">
        <h2>History</h2>
        <button className="badge bg-dark" onClick={this.handleRefresh}>
          Refresh
        </button>
        <button className="badge bg-dark" onClick={this.handleClear}>
          Clear
        </button>
        <Container className="input-text overflow-auto">
          {this.state.data.map((item) => (
            <Container key={item[0] + 1 + this.randomId(10)} className="mb-4 ,">
              <Card className="p-3">
                <Card.Title>{item[0]}</Card.Title>
                <Card.Subtitle>Birth</Card.Subtitle>
                {item[1][0] !== "No result found" ? (
                  item[1].map((item) => (
                    <p key={item.name}>
                      {item.name}
                      <br />
                      <Card.Link
                        href={item.urls}
                        target="_blank"
                        className="text-decoration-none "
                      >
                        {item.urls}
                      </Card.Link>
                    </p>
                  ))
                ) : (
                  <p>No result found</p>
                )}

                <Card.Subtitle>Death</Card.Subtitle>

                {item[2][0] !== "No result found" ? (
                  item[2].map((item) => (
                    <p key={item.name}>
                      {item.name}
                      <br />
                      <Card.Link
                        href={item.urls}
                        target="_blank"
                        className="text-decoration-none "
                      >
                        {item.urls}
                      </Card.Link>
                    </p>
                  ))
                ) : (
                  <p>No result found</p>
                )}

                <Card.Subtitle>Event</Card.Subtitle>
                {item[3][0] !== "No result found" ? (
                  item[3].map((item) => (
                    <p key={item.name}>
                      {item.name}
                      <br />
                      <Card.Link
                        href={item.urls}
                        target="_blank"
                        className="text-decoration-none "
                      >
                        {item.urls}
                      </Card.Link>
                    </p>
                  ))
                ) : (
                  <p>No result found</p>
                )}
                <Card.Subtitle>Holiday</Card.Subtitle>
                <Container className="holiday overflow-auto m-0">
                  {item[4][0] !== "No result found" ? (
                    item[4].map((item) => (
                      <p key={item.name + this.randomId(10 + 2)}>
                        {item.name}
                        <br />
                        <Card.Link
                          href={item.urls}
                          target="_blank"
                          className="text-decoration-none "
                        >
                          {item.urls}
                        </Card.Link>
                      </p>
                    ))
                  ) : (
                    <p>No result found</p>
                  )}
                </Container>
              </Card>
            </Container>
          ))}
        </Container>
      </Container>
    );
  }
}

export default History;
