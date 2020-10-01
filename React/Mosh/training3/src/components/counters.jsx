import React, { Component } from "react";
import Counter from "./counter";

class Counters extends Component {
  render() {
    console.log("Counters - Rendered");
    const {
      onReset,
      onRefresh,
      onDelete,
      onIncrement,
      onDecrement,
      counters
    } = this.props;
    if (counters.length == 0)
      return (
        <button className="btn btn-success m-2" onClick={onRefresh}>
          Refresh
        </button>
      );
    return (
      <div>
        <button className="btn btn-primary btn-sm m-2" onClick={onReset}>
          Reset
        </button>
        {counters.map(counter => (
          <Counter
            key={counter.id}
            counter={counter}
            onIncrement={onIncrement}
            onDecrement={onDecrement}
            onDelete={onDelete}
          >
            {/* <h4>Counter #{counter.id}</h4> */}
          </Counter>
        ))}
      </div>
    );
  }
}

export default Counters;
