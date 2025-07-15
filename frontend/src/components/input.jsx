import React, { Component } from "react";
import { Form, Button, Container } from "react-bootstrap";

class InputSec extends Component {
  state = {};

  getYearList = () => {
    const year = new Date().getFullYear();
    return Array.from(new Array(523), (val, index) => (
      <option key={index} value={year - index}>
        {year - index}
      </option>
    ));
  };

  getDateList = () => {
    return Array.from(new Array(31), (val, index) => (
      <option key={index} value={String(index + 1).padStart(2, "0")}>
        {String(index + 1).padStart(2, "0")}
      </option>
    ));
  };

  randomId = () => {
    return Math.floor(Math.random() * 100);
  };

  render() {
    const months = [
      { month: "January", value: "01" },
      { month: "February", value: "02" },
      { month: "March", value: "03" },
      { month: "April", value: "04" },
      { month: "May", value: "05" },
      { month: "June", value: "06" },
      { month: "July", value: "07" },
      { month: "August", value: "08" },
      { month: "September", value: "09" },
      { month: "October", value: "10" },
      { month: "November", value: "11" },
      { month: "December", value: "12" },
    ];

    const { date, onSubmit, onChange, onReset } = this.props;
    return (
      <Container className="container-input m-2 justify-content-md-center mt-3">
        <Container>
          <Form>
            <Form.Label className="badge label">Select a date</Form.Label>
            <br />
            <Form.Select
              key={date[0].id}
              onChange={(e) => onChange(0, e.target.value)}
              value={date[0].value}
              className="selector-day"
            >
              <option key="day-default" value="default" defaultChecked>
                Day
              </option>
              {this.getDateList()}
            </Form.Select>
            <Form.Label className="slash">/</Form.Label>
            <Form.Select
              key={date[1].id}
              onChange={(e) => onChange(1, e.target.value)}
              value={date[1].value}
              className="selector"
            >
              <option key="month-default" value="default">
                Month
              </option>
              {months.map((month) => (
                <option key={month.month} value={month.value}>
                  {month.month}
                </option>
              ))}
            </Form.Select>
            <br />
            <Form.Label className="badge label">Select a year</Form.Label>
            <br />
            <Form.Select
              key={date[2].id}
              onChange={(e) => onChange(2, e.target.value)}
              value={date[2].value}
              className="selector"
            >
              <option key="year-default" value="default">
                Year
              </option>
              {this.getYearList()}
            </Form.Select>
            <br />
            <Button
              className="badge bg-dark p-2 m-2 "
              onClick={() => {
                onSubmit();
              }}
            >
              OK
            </Button>
            <Button className="badge bg-dark p-2 m-2" onClick={() => onReset()}>
              Reset
            </Button>
          </Form>
        </Container>
      </Container>
    );
  }
}

export default InputSec;
