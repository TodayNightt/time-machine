import React, { Component } from "react";
import "./App.css";
import { Row, Col, Container } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";

//TrackPromise module
import { trackPromise } from "react-promise-tracker";

//Component
import TitleBar from "./components/navbar";
import InputSec from "./components/input";
import Output from "./components/output";
import Calender from "./components/calender";
import History from "./components/history";

//Fonts
import "./fonts/Poppins-Regular.ttf";
import "./fonts/Poppins-SemiBold.ttf";
import "./fonts/Poppins-Bold.ttf";
import "./fonts/PressStart2P-Regular.ttf";

class App extends Component {
  state = {
    today: [],
    date: [
      { id: "day", value: "" },
      { id: "month", value: "" },
      { id: "year", value: "" },
    ],
    currentDate: [
      { id: "day", value: [1, 1] },
      { id: "month", value: [1, 1] },
      { id: "year", value: [1, 1, 1, 1] },
    ],
    data: [
      { id: "birth", text: null },
      { id: "death", text: null },
      { id: "event", text: null },
      { id: "holiday", text: null },
    ],
    childKey: 1,
    count: 0.5,
  };

  //Get today's date
  componentDidMount() {
    const todaydate = new Date();
    const today = this.state.today;
    const current = this.state.currentDate;
    today[0] = todaydate.toString().substring(8, 10).split("");
    today[1] = todaydate.toISOString().substring(5, 7).split("");
    today[2] = todaydate.toISOString().substring(0, 4).split("");
    current.map((item, i) => (item.value = today[i]));
    this.setState({ today, current });
  }

  //changes in input component
  handleChange = (index, value) => {
    const date = this.state.date;
    date[index].value = value;
    this.setState({ date });
  };

  //Change calender display
  transfer = () => {
    const current = this.state.currentDate;
    const date = this.state.date;
    let current_day = current[0].value.join("");
    let current_month = current[1].value.join("");
    let current_year = current[2].value.join("");

    //Day
    if (Number(date[0].value) > Number(current_day)) {
      current_day++;
      current[0].value = current_day.toString().padStart(2, "0").split("");
    } else if (Number(date[0].value) < Number(current_day)) {
      current_day--;
      current[0].value = current_day.toString().padStart(2, "0").split("");
    }

    //Month
    if (Number(date[1].value) > Number(current_month)) {
      current_month++;
      current[1].value = current_month.toString().padStart(2, "0").split("");
    } else if (Number(date[1].value) < Number(current_month)) {
      current_month--;
      current[1].value = current_month.toString().padStart(2, "0").split("");
    }

    //Year
    if (Number(date[2].value) > Number(current_year)) {
      current_year++;
      current[2].value = current_year.toString().split("");
    } else if (Number(date[2].value) < Number(current_year)) {
      current_year -= 4;
      current[2].value = current_year.toString().split("");
    }

    this.setState({ current, count: this.state.count + 0.4 });
    const timeout = setTimeout(() => this.transfer(), 100 / this.state.count);
    if (
      current_day === date[0].value &&
      current_month === date[1].value &&
      current_year === date[2].value
    ) {
      this.setState({ count: 1.5 }, () => clearInterval(timeout));
    }
  };

  //fetch data from python
  fetchdata = async (date) => {
    const response = await fetch("/on_this_day", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(date),
    });
    const data = response.json();
    if (!response.ok) {
      const error = (data && data.message) || response.status;
      return Promise.reject(error);
    }
    return Promise.resolve(data);
  };

  //Initialze when button pressed
  handleSubmit = () => {
    if (this.state.date[0].value) {
      this.transfer();
      const date = {
        day: this.state.date[0].value,
        month: this.state.date[1].value,
        year: this.state.date[2].value,
      };
      trackPromise(
        this.fetchdata(date)
          .then((response_data) => {
            const data = this.state.data;
            data.map((item) => {
              return (item.text = response_data[item.id]);
            });
            this.setState({
              data,
              childKey: this.state.childKey + 1,
            });
          })
          .catch((err) =>
            err === 405
              ? alert("'GET' Method Not Allowed: " + err)
              : alert("Internal Server Error: " + err)
          )
      );
    } else {
      alert("You haven't Enter a Date");
    }
  };

  handleReset = () => {
    const date = this.state.date;
    const currentDate = this.state.currentDate;
    const data = this.state.data;
    date.map((item) => (item.value = ""));
    currentDate.map((item, i) => (item.value = this.state.today[i]));
    data.map((item) => (item.text = null));
    this.setState({ date, currentDate, childKey: 1 });
  };

  render() {
    return (
      <React.Fragment>
        <React.StrictMode>
          <TitleBar />
          <Container>
            <Row>
              <Col xs="11" md="" lg="8">
                <Calender
                  today={this.state.today}
                  currentDate={this.state.currentDate}
                  key={this.state.childKey}
                />
              </Col>
              <Col md="4" xs="11" lg="3">
                <InputSec
                  date={this.state.date}
                  onSubmit={this.handleSubmit}
                  onChange={this.handleChange}
                  onReset={this.handleReset}
                />
              </Col>
            </Row>
            <Row>
              <Col xs="11" lg="8">
                <Output
                  data={this.state.data}
                  key={this.state.childKey}
                  date={this.state.date}
                />
              </Col>
              <Col xs="11" lg="4">
                <History />
              </Col>
            </Row>
          </Container>
          <Container className="footer bg-dark">
            <p>
              Link :
              <a
                href="https://www.flaticon.com/free-icons/time-machine"
                title="time machine icons"
              >
                Time machine icons created by Freepik - Flaticon
              </a>
            </p>
          </Container>
        </React.StrictMode>
      </React.Fragment>
    );
  }
}

export default App;
