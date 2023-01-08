import React, { Component } from "react";

class Counter extends Component {
  componentDidUpdate(prevProps, prevState) {
    console.log("prevProps", prevProps);
    console.log("prevState", prevState);
  }
  componentWillUnmount() {
    console.log("Counter - Unmount");
  }
  render() {
    const { onDelete, onIncrement, onDecrement, counter } = this.props;
    return (
      <div>
        <span className={this.getBadgeClasses()}>{this.formatCount()}</span>
        <button
          onClick={() => onIncrement()}
          className="btn btn-secondary btn-sm"
        >
          Increment
        </button>
        <button
          onClick={() => onDecrement()}
          className="btn btn-secondary btn-sm m-2"
          disabled={counter.value > 0 ? false : true}
        >
          Decrement
        </button>
        <button className="btn btn-danger btn-sm m-2" onClick={onDelete}>
          Delete
        </button>
      </div>
    );
  }

  getBadgeClasses() {
    let classes = "btn m-2 btn-";
    classes += this.props.counter.value === 0 ? "warning" : "primary";
    return classes;
  }

  formatCount() {
    const { value } = this.props.counter;
    return value === 0 ? "Zero" : value;
  }
}

export default Counter;
