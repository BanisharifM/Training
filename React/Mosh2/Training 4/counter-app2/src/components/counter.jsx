import React, { Component } from "react";

class Counter extends Component {
  state = {
    value: this.props.value,
  };
  handleIncrement = () => {
    const value = this.state.value + 1;
    this.setState({ value: value });
  };
  handleDecrement = () => {
    let value = this.state.value;
    if (value > 0) value--;
    console.log(value);
    this.setState({ value: value });
  };
  render() {
    return (
      <div>
        <span className={this.styleFormatter()}>{this.state.value}</span>
        <button
          onClick={this.handleIncrement}
          className="btn btn-secondary btn-sm"
        >
          Increment
        </button>
        <button
          onClick={this.handleDecrement}
          className="btn btn-secondary btn-sm m-2"
        >
          Decrement
        </button>
        <button
          onClick={this.props.onDelete}
          className="btn btn-danger btn-sm m-2"
        >
          Delete
        </button>
      </div>
    );
  }
  styleFormatter = () => {
    let style = "btn m-2 btn-";
    style += this.state.value === 0 ? "warning" : "primary";
    return style;
  };
}

export default Counter;
